"""Brand CARDS engine: one renderer for explainer boards (animated overlays timed to words) and static carousels (IG 4:5 PNGs, LinkedIn PDF).

A card is data:
  {"type": "title|stat|list|steps|quote|compare|definition|myth_fact|chart|cta", "kicker", "title", "body",
   "value", "label", "source", "items": [...], "left": {"title", "items"}, "right": {...}, "bars": [{"label", "value"}], "cta"}
Boards in a recipe (render.py overlays them like B-roll, with alpha):
  boards: [{"id": "k01", "card": {...}, "anchor": {"item", "offset"}, "dur": 3.5, "mode": "full|panel"}]
"panel" keeps the speaker visible (card in the top 46 %); "full" replaces the frame (faceless explainers, data-heavy beats).
Every number on a card needs a "source" (studio rule: evidence over folklore); qc flags stat/chart cards without one.

Free + local: Pillow frames -> ffmpeg (qtrle .mov with alpha). Premium path (HyperFrames/Remotion) takes the same card JSON.
"""
import json, math, re, shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from .common import REPO, TOOL, ffmpeg, log, rjson, wjson

DEFAULT_THEME = {"bg": "#0E0F13", "panel": "#16181F", "text": "#FFFFFF", "muted": "#A7ADBB", "accent": "#FFD43B", "accent2": "#4DA3FF",
                 "good": "#3CCB7F", "bad": "#FF5A5F", "font_display": None, "font_body": None, "radius": 0.035, "handle": ""}
CARDS_VERSION = 4  # bump when card layout changes (invalidates cached board clips)
TYPES = ("title", "stat", "list", "steps", "quote", "compare", "definition", "myth_fact", "chart", "cta")
ASPECT_PX = {"4:5": (1080, 1350), "1:1": (1080, 1080), "9:16": (1080, 1920), "16:9": (1920, 1080)}


# ---------------- theme + fonts ----------------
def theme_for(brand=None, overrides=None):
    """Brand guide colours/fonts (brands/<brand>.md edit-brand block) over the default dark theme."""
    t = dict(DEFAULT_THEME)
    if brand:
        from .presets import brand_guide
        g, _ = brand_guide(brand)
        c = g.get("colors", {})
        t.update({k: v for k, v in {"bg": c.get("background") or c.get("primary"), "text": c.get("text"), "accent": c.get("accent"),
                                     "accent2": c.get("secondary")}.items() if v})
        f = g.get("fonts", {})
        t["font_display"], t["font_body"] = f.get("display"), f.get("body")
        t["handle"] = g.get("handle", "")
        t["brand"] = brand
        if isinstance(g.get("cards"), dict):
            t.update(g["cards"])
    t.update(overrides or {})
    return t


_FONT_CACHE = {}


def font(theme, role, px):
    """Resolve brand font files (assets/fonts/<brand>/*), then bundled DejaVu. role: display|body."""
    name = theme.get("font_display" if role == "display" else "font_body") or ""
    key = (theme.get("brand"), name, role, px)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    cands = []
    bdir = REPO / "assets" / "fonts" / str(theme.get("brand") or "_none")
    if bdir.exists():
        files = sorted(bdir.glob("*.[ot]tf"))
        want = name.replace(" ", "").lower()
        bold = role == "display"
        cands += sorted(files, key=lambda p: (want not in p.stem.replace(" ", "").lower(), bold != bool(re.search(r"bold|black|heavy", p.stem, re.I))))
    cands += [TOOL / "fonts" / ("DejaVuSans-Bold.ttf" if role == "display" else "DejaVuSans.ttf")]
    for c in cands:
        try:
            f = ImageFont.truetype(str(c), px)
            _FONT_CACHE[key] = f
            return f
        except OSError:
            continue
    return ImageFont.load_default()


def rgb(hexv, a=255):
    h = (hexv or "#FFFFFF").lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)


# ---------------- text layout ----------------
def wrap(draw, text, fnt, max_w):
    lines = []
    for para in str(text or "").split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            if draw.textlength(t, font=fnt) <= max_w or not cur:
                cur = t
            else:
                lines.append(cur); cur = w
        lines.append(cur)
    return lines


def fit_text(draw, text, theme, role, max_w, max_h, start_px, min_px=18, spacing=1.18):
    """Largest font size where the wrapped text fits the box."""
    px = start_px
    while px >= min_px:
        f = font(theme, role, px)
        lines = wrap(draw, text, f, max_w)
        if len(lines) * px * spacing <= max_h:
            return f, lines, px
        px = int(px * 0.92)
    f = font(theme, role, min_px)
    return f, wrap(draw, text, f, max_w), min_px


def draw_lines(draw, xy, lines, fnt, px, fill, spacing=1.18, align="left", box_w=None, highlight=None, hl_fill=None):
    """Draw wrapped lines; words wrapped in *asterisks* render in the highlight colour."""
    x0, y = xy
    for ln in lines:
        words = ln.split(" ")
        total = draw.textlength(ln.replace("*", ""), font=fnt)
        x = x0 + ((box_w - total) / 2 if align == "center" and box_w else 0)
        for i, w in enumerate(words):
            hl = w.startswith("*") or w.endswith("*") or (highlight and w.lower().strip(".,!?") in highlight)
            clean = w.replace("*", "")
            draw.text((x, y), clean, font=fnt, fill=hl_fill if hl and hl_fill else fill)
            x += draw.textlength(clean + (" " if i < len(words) - 1 else ""), font=fnt)
        y += px * spacing
    return y


# ---------------- easing ----------------
def ease_out(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def stagger(p, i, n, span=0.55):
    """Progress of element i of n when the whole card is at progress p (0..1): elements start one after another."""
    if n <= 1:
        return ease_out(p / max(span, 1e-6))
    start = (1 - span) * i / (n - 1)
    return ease_out((p - start) / span)


# ---------------- card renderer ----------------
_DY = {}


def render_card(card, W, H, theme, p=1.0, mode="full", page=None):
    """One frame of a card at reveal progress p (1.0 = static). Returns RGBA Image (transparent outside the panel in 'panel' mode).
    Full-frame cards are optically centred (slightly above middle) using the finished layout, so animation frames never jitter."""
    if mode == "full" and card.get("type") in ("title", "stat", "quote", "definition", "steps", "list", "cta"):
        key = json.dumps([card, W, H, theme.get("brand"), theme.get("font_display")], sort_keys=True)
        if key not in _DY:
            probe_img = _render(card, W, H, theme, 1.0, mode, None, 0, content_only=True)
            bb = probe_img.getbbox()
            S = min(W, H)
            top, bottom = int(H * 0.09), H - int(H * 0.11)
            _DY[key] = max(0, int(((bottom - top) - (bb[3] - bb[1])) * 0.42 + top - bb[1])) if bb else 0
        return _render(card, W, H, theme, p, mode, page, _DY[key])
    if mode == "panel":
        key = json.dumps(["panel", card, W, H, theme.get("brand"), theme.get("font_display")], sort_keys=True)
        if key not in _DY:
            bb = _render(card, W, H, theme, 1.0, mode, None, 0, content_only=True).getbbox()
            S = min(W, H)
            _DY[key] = int(min(H * 0.40, max(H * 0.16, (bb[3] - int(H * 0.06)) + S * 0.09))) if bb else int(H * 0.40)
        return _render(card, W, H, theme, p, mode, page, 0, panel_h=_DY[key])
    return _render(card, W, H, theme, p, mode, page, 0)


def _render(card, W, H, theme, p, mode, page, dy, content_only=False, panel_h=None):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    S = min(W, H)
    if mode == "panel":
        bx0, by0, bx1 = int(W * 0.05), int(H * 0.06), int(W * 0.95)
        by1 = int(H * 0.06 + H * 0.40)
        lift = int((1 - ease_out(p / 0.35)) * S * 0.04)
        if not content_only:
            a = int(235 * ease_out(p / 0.25))
            d.rounded_rectangle([bx0, by0 + lift, bx1, by0 + (panel_h or (by1 - by0)) + lift], radius=int(S * theme["radius"]), fill=rgb(theme["panel"], a))
        box = (bx0 + int(S * 0.05), by0 + lift + int(S * 0.045), bx1 - int(S * 0.05), by1 + lift - int(S * 0.045))
    else:
        if not content_only:
            d.rectangle([0, 0, W, H], fill=rgb(theme["bg"], int(255 * ease_out(p / 0.2))))
        m = int(S * 0.08)
        box = (m, int(H * 0.09) + dy, W - m, H - int(H * 0.11))
    x0, y0, x1, y1 = box
    foot_y = H - int(H * 0.11)
    src_y = (foot_y + S * 0.015) if mode == "full" else (by0 + (panel_h or (by1 - by0)) - S * 0.04)
    bw, bh = x1 - x0, y1 - y0
    T, A, MU = rgb(theme["text"]), rgb(theme["accent"]), rgb(theme["muted"])
    t = card.get("type", "title")
    y = y0
    if card.get("kicker"):
        kf = font(theme, "body", int(S * 0.032))
        d.text((x0, y), card["kicker"].upper(), font=kf, fill=A)
        y += int(S * 0.055)
    reveal = lambda i, n: stagger(p, i, n)

    if t in ("title", "cta"):
        f, lines, px = fit_text(d, card.get("title", ""), theme, "display", bw, bh * 0.55, int(S * 0.11))
        y = draw_lines(d, (x0, y + (1 - reveal(0, 2)) * S * 0.03), lines, f, px, T, hl_fill=A)
        if card.get("body"):
            f2, l2, px2 = fit_text(d, card["body"], theme, "body", bw, bh * 0.3, int(S * 0.045))
            draw_lines(d, (x0, y + S * 0.03), l2, f2, px2, rgb(theme["muted"], int(255 * reveal(1, 2))))
        if t == "cta" and card.get("cta"):
            cf = font(theme, "display", int(S * 0.05))
            tw = d.textlength(card["cta"], font=cf)
            k = reveal(1, 2)
            bx, by = x0, y1 - int(S * 0.11)
            d.rounded_rectangle([bx, by, bx + tw + S * 0.08, by + S * 0.09], radius=int(S * 0.045), fill=rgb(theme["accent"], int(255 * k)))
            d.text((bx + S * 0.04, by + S * 0.017), card["cta"], font=cf, fill=rgb(theme["bg"], int(255 * k)))

    elif t == "stat":
        raw = str(card.get("value", ""))
        m = re.match(r"^([^\d\-]*)(-?[\d,]*\.?\d+)(.*)$", raw)
        k = reveal(0, 2)
        if m:
            num = float(m.group(2).replace(",", ""))
            dec = len(m.group(2).split(".")[1]) if "." in m.group(2) else 0
            cur = num * k
            shown = f"{m.group(1)}{cur:,.{dec}f}{m.group(3)}" if "," in m.group(2) else f"{m.group(1)}{cur:.{dec}f}{m.group(3)}"
        else:
            shown = raw
        f, lines, px = fit_text(d, raw, theme, "display", bw, bh * 0.42, int(S * 0.26))
        d.text((x0, y), shown, font=f, fill=A)
        y += px * 1.15
        if card.get("label"):
            f2, l2, px2 = fit_text(d, card["label"], theme, "display", bw, bh * 0.3, int(S * 0.06))
            y = draw_lines(d, (x0, y), l2, f2, px2, rgb(theme["text"], int(255 * reveal(1, 2))), hl_fill=A)

    elif t in ("list", "steps"):
        items = card.get("items", [])[:7]
        if card.get("title"):
            f, lines, px = fit_text(d, card["title"], theme, "display", bw, bh * 0.24, int(S * 0.075))
            y = draw_lines(d, (x0, y), lines, f, px, T, hl_fill=A) + S * 0.025
        n = max(1, len(items))
        row_h = min((y1 - y) / n, S * 0.17)
        fpx = int(min(S * 0.052, row_h * 0.42))
        for i, it in enumerate(items):
            k = reveal(i, n)
            if k <= 0:
                continue
            ry = y + i * row_h + (1 - k) * S * 0.02
            al = int(255 * k)
            if t == "steps":
                r_ = fpx * 0.95
                d.ellipse([x0, ry, x0 + 2 * r_, ry + 2 * r_], fill=rgb(theme["accent"], al))
                nf = font(theme, "display", int(fpx * 1.05))
                s = str(i + 1)
                d.text((x0 + r_ - d.textlength(s, font=nf) / 2, ry + r_ * 0.28), s, font=nf, fill=rgb(theme["bg"], al))
                tx = x0 + 2 * r_ + S * 0.03
            else:
                d.rounded_rectangle([x0, ry + fpx * 0.35, x0 + fpx * 0.5, ry + fpx * 0.85], radius=int(fpx * 0.1), fill=rgb(theme["accent"], al))
                tx = x0 + fpx * 0.5 + S * 0.03
            ff, ll, pp = fit_text(d, it, theme, "body", x1 - tx, row_h * 0.92, fpx, min_px=int(fpx * 0.6))
            draw_lines(d, (tx, ry), ll, ff, pp, rgb(theme["text"], al), hl_fill=rgb(theme["accent"], al))

    elif t == "quote":
        qf = font(theme, "display", int(S * 0.2))
        d.text((x0, y - S * 0.03), "“", font=qf, fill=A)
        f, lines, px = fit_text(d, card.get("title", ""), theme, "display", bw, bh * 0.6, int(S * 0.075))
        y = draw_lines(d, (x0, y + S * 0.15), lines, f, px, rgb(theme["text"], int(255 * reveal(0, 2))), hl_fill=A)
        if card.get("label"):
            d.text((x0, y + S * 0.03), "— " + card["label"], font=font(theme, "body", int(S * 0.04)), fill=rgb(theme["muted"], int(255 * reveal(1, 2))))

    elif t == "definition":
        f, lines, px = fit_text(d, card.get("title", ""), theme, "display", bw, bh * 0.28, int(S * 0.1))
        y = draw_lines(d, (x0, y), lines, f, px, A)
        if card.get("label"):
            d.text((x0, y), card["label"], font=font(theme, "body", int(S * 0.035)), fill=MU)
            y += S * 0.06
        d.line([x0, y + S * 0.01, x0 + bw * reveal(0, 2), y + S * 0.01], fill=rgb(theme["muted"], 120), width=max(2, int(S * 0.004)))
        f2, l2, px2 = fit_text(d, card.get("body", ""), theme, "body", bw, y1 - y - S * 0.05, int(S * 0.055))
        draw_lines(d, (x0, y + S * 0.04), l2, f2, px2, rgb(theme["text"], int(255 * reveal(1, 2))), hl_fill=A)

    elif t in ("compare", "myth_fact"):
        L = card.get("left") or {"title": "Myth", "items": [card.get("myth", "")]}
        R = card.get("right") or {"title": "Fact", "items": [card.get("fact", "")]}
        if card.get("title"):
            f, lines, px = fit_text(d, card["title"], theme, "display", bw, bh * 0.18, int(S * 0.07))
            y = draw_lines(d, (x0, y), lines, f, px, T, hl_fill=A) + S * 0.02
        vertical = W < H * 0.9
        cols = [(L, theme["bad"]), (R, theme["good"])] if t == "myth_fact" else [(L, theme["muted"]), (R, theme["accent"])]
        for i, (col, colr) in enumerate(cols):
            k = reveal(i, 2)
            if k <= 0:
                continue
            if vertical:
                cx0, cy0, cx1, cy1 = x0, y + i * (y1 - y) / 2 + S * 0.01, x1, y + (i + 1) * (y1 - y) / 2 - S * 0.02
            else:
                cx0, cy0, cx1, cy1 = x0 + i * bw / 2 + (S * 0.01 if i else 0), y, x0 + (i + 1) * bw / 2 - (0 if i else S * 0.01), y1
            al = int(255 * k)
            d.rounded_rectangle([cx0, cy0, cx1, cy1], radius=int(S * 0.025), fill=rgb(theme["panel"] if mode == "full" else theme["bg"], int(al * 0.9)),
                                outline=rgb(colr, al), width=max(2, int(S * 0.005)))
            pad = S * 0.035
            d.text((cx0 + pad, cy0 + pad), str(col.get("title", "")).upper(), font=font(theme, "display", int(S * 0.04)), fill=rgb(colr, al))
            txt = "\n".join(col.get("items", []))
            ff, ll, pp = fit_text(d, txt, theme, "body", cx1 - cx0 - 2 * pad, cy1 - cy0 - pad * 2 - S * 0.07, int(S * 0.05))
            draw_lines(d, (cx0 + pad, cy0 + pad + S * 0.07), ll, ff, pp, rgb(theme["text"], al), hl_fill=rgb(theme["accent"], al))

    elif t == "chart":
        bars = card.get("bars", [])[:6]
        if card.get("title"):
            f, lines, px = fit_text(d, card["title"], theme, "display", bw, bh * 0.2, int(S * 0.07))
            y = draw_lines(d, (x0, y), lines, f, px, T, hl_fill=A) + S * 0.03
        vmax = max([float(b.get("value", 0)) for b in bars] + [1e-9])
        n = max(1, len(bars))
        row = (y1 - y - S * 0.05) / n
        lf = font(theme, "body", int(min(S * 0.04, row * 0.35)))
        for i, b in enumerate(bars):
            k = reveal(i, n)
            ry = y + i * row
            d.text((x0, ry), str(b.get("label", "")), font=lf, fill=T)
            bwid = (bw * 0.8) * float(b.get("value", 0)) / vmax * k
            hi = b.get("highlight") or (i == max(range(n), key=lambda j: float(bars[j].get("value", 0))))
            d.rounded_rectangle([x0, ry + row * 0.42, x0 + max(bwid, 2), ry + row * 0.82], radius=int(row * 0.1), fill=rgb(theme["accent"] if hi else theme["muted"]))
            d.text((x0 + bwid + S * 0.015, ry + row * 0.42), f"{b.get('value')}{card.get('unit', '')}", font=lf, fill=T)

    if content_only:
        return img
    if card.get("source"):
        sf = font(theme, "body", int(S * 0.022))
        d.text((x0, src_y), "Source: " + card["source"], font=sf, fill=rgb(theme["muted"], int(200 * min(1, p * 2))))
    if page:
        pf = font(theme, "body", int(S * 0.026))
        i, n = page
        lab = f"{i}/{n}"
        d.text((W - int(S * 0.08) - d.textlength(lab, font=pf), H - int(H * 0.065)), lab, font=pf, fill=MU)
        if theme.get("handle"):
            d.text((int(S * 0.08), H - int(H * 0.065)), theme["handle"], font=pf, fill=MU)
        if i < n and card.get("type") != "cta":
            d.text((W / 2 - d.textlength("swipe →", font=pf) / 2, H - int(H * 0.065)), "swipe →", font=pf, fill=A)
    return img


# ---------------- animation (boards) ----------------
def board_clip(board, W, H, theme, cache, quality="draft"):
    """Animated card -> .mov with alpha (qtrle), cached by content hash. In 0.45 s staggered reveal, hold, out 0.25 s fade."""
    import hashlib
    fps = 15 if quality == "draft" else 30
    dur = float(board.get("dur", 3.0))
    mode = board.get("mode", "panel")
    key = hashlib.sha1(json.dumps([board["card"], W, H, theme, fps, dur, mode, CARDS_VERSION], sort_keys=True).encode()).hexdigest()[:16]
    out = Path(cache) / f"board_{key}.mov"
    if out.exists():
        return out
    tmp = Path(cache) / f"board_{key}_frames"
    tmp.mkdir(parents=True, exist_ok=True)
    n = max(1, int(round(dur * fps)))
    rin, rout = min(0.9, dur * 0.35), min(0.25, dur * 0.15)
    still = None
    for i in range(n):
        t = i / fps
        p = min(1.0, t / rin)
        if p >= 1.0:
            still = still or render_card(board["card"], W, H, theme, 1.0, mode)
            fr = still
        else:
            fr = render_card(board["card"], W, H, theme, p, mode)
        if t > dur - rout:
            k = max(0.0, (dur - t) / rout)
            fr = fr.copy()
            fr.putalpha(fr.getchannel("A").point(lambda v: int(v * k)))
        fr.save(tmp / f"f{i:05d}.png")
    ffmpeg(["-framerate", str(fps), "-i", str(tmp / "f%05d.png"), "-c:v", "qtrle", "-pix_fmt", "argb", str(out)])
    shutil.rmtree(tmp, ignore_errors=True)
    return out


# ---------------- carousels ----------------
def render_carousel(cards, out_dir, aspect="4:5", theme=None, pdf=True, prefix="slide"):
    """Static slides (PNG per slide) + optional multipage PDF for LinkedIn document posts. Returns list of paths."""
    W, H = ASPECT_PX[aspect]
    theme = theme or dict(DEFAULT_THEME)
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    pages, paths = [], []
    for i, c in enumerate(cards, 1):
        im = render_card(c, W, H, theme, 1.0, "full", page=(i, len(cards))).convert("RGB")
        pth = out / f"{prefix}_{i:02d}.png"
        im.save(pth, optimize=True)
        pages.append(im); paths.append(pth)
    if pdf and pages:
        pp = out / f"{prefix}s.pdf"
        pages[0].save(pp, save_all=True, append_images=pages[1:], resolution=150)
        paths.append(pp)
    return paths


def contact_sheet(paths, out, cols=4, thumb_w=360):
    ims = [Image.open(p).convert("RGB") for p in paths if str(p).endswith(".png")]
    if not ims:
        return None
    th = int(thumb_w * ims[0].height / ims[0].width)
    rows = math.ceil(len(ims) / cols)
    sheet = Image.new("RGB", (cols * thumb_w, rows * th), (30, 30, 30))
    for i, im in enumerate(ims):
        sheet.paste(im.resize((thumb_w, th)), ((i % cols) * thumb_w, (i // cols) * th))
    sheet.save(out)
    return out


# ---------------- board planning (zero tokens) ----------------
NUM = re.compile(r"(\$|S\$|RM|£)?\d[\d,]*(\.\d+)?\s?(%|percent|x|k|m|million|billion|hours?|days?|weeks?|years?|minutes?|reps?|kg|g)?", re.I)
STEP_WORDS = re.compile(r"\b(first|second|third|step one|step two|step 1|step 2|number one|number two|finally|next)\b", re.I)
DEF_WORDS = re.compile(r"\b(is called|means|is defined as|stands for|refers to|what is)\b", re.I)
YEAR = re.compile(r"\b(19|20)\d{2}\b")


def needs_board(text):
    """The listening-alone test, as a heuristic: lines with a number, date, step or definition get a visual layer."""
    reasons = []
    if NUM.search(text) and re.search(r"\d", text):
        reasons.append("number")
    if YEAR.search(text):
        reasons.append("date")
    if STEP_WORDS.search(text):
        reasons.append("step")
    if DEF_WORDS.search(text):
        reasons.append("definition")
    return reasons


def draft_card(text, reasons):
    """Best-effort card from one spoken phrase; Claude/Klaus refine. Numbers become stat cards that still need a source."""
    if "number" in reasons:
        m = NUM.search(text)
        val = m.group(0).strip() if m else ""
        val = re.sub(r"\s?percent$", "%", val, flags=re.I)
        before, after = text[: m.start()].split(), text[m.end():].split() if m else ([], [])
        label = " ".join(after[:8]) if len(after) >= 3 else " ".join(before[-8:])
        return {"type": "stat", "value": val, "label": label.strip(" ,.-"), "source": "", "_todo": "add source"}
    if "definition" in reasons:
        parts = DEF_WORDS.split(text, maxsplit=1)
        term = " ".join(parts[0].split()[-4:]).strip(" ,.") if parts else ""
        body = parts[-1].strip(" ,.") if len(parts) > 2 else text
        return {"type": "definition", "title": term or "Definition", "body": body[:160]}
    if "step" in reasons:
        return {"type": "steps", "title": "", "items": [STEP_WORDS.sub("", text).strip(" ,.")[:90]], "_todo": "merge consecutive steps into one card"}
    return {"type": "title", "title": text[:80]}


def phrases(words, max_words=14, gap=0.45):
    """Split word timestamps into spoken phrases: sentence punctuation, a pause, or a step/sequence word starts a new phrase."""
    cur = []
    for i, w in enumerate(words):
        if cur and (len(cur) >= max_words or w["t0"] - cur[-1]["t1"] > gap or STEP_WORDS.match(w["w"].strip().lower())):
            yield cur; cur = []
        cur.append(w)
        if re.search(r"[.!?]$", w["w"].strip()):
            yield cur; cur = []
    if cur:
        yield cur


def plan_boards(r, edit_dir, max_boards=None, mode="panel", min_gap_s=4.0):
    """Scan the cut's spoken words per item; propose boards[] anchored to the phrase start. Returns list (does not save).
    Ingest words are {"w", "t0", "t1"} in source seconds."""
    from .ingest import load_clips
    from .recipe import item_starts
    clips = {c["id"]: c for c in load_clips(edit_dir)}
    starts, _ = item_starts(r)
    out, last = [], -1e9
    for it in r["items"]:
        words = [w for w in clips[it["clip"]].get("words", []) if it["in"] <= w["t0"] < it["out"] and w.get("filler") != "hard"]
        for ph in phrases(words):
            text = " ".join(w["w"].strip() for w in ph)
            why = needs_board(text)
            if not why:
                continue
            off = (ph[0]["t0"] - it["in"]) / it.get("speed", 1)
            at = starts[it["id"]] + off
            if at - last < min_gap_s:
                continue
            spoken = (ph[-1]["t1"] - ph[0]["t0"]) / it.get("speed", 1)
            out.append({"id": f"k{len(out) + 1:02d}", "card": draft_card(text, why), "anchor": {"item": it["id"], "offset": round(max(0, off - 0.1), 2)},
                        "dur": round(min(5.0, max(3.0, spoken + 1.5)), 1), "mode": mode, "why": why, "line": text})
            last = at
            if max_boards and len(out) >= max_boards:
                return out
    return out


# ---------------- CLI ----------------
def cmd_cards(a):
    """editor.py cards render SPEC.json [--aspect 4:5 --brand B --out DIR --no-pdf] | preview SPEC.json"""
    spec = rjson(a.spec)
    cards = spec.get("cards", spec if isinstance(spec, list) else [])
    theme = theme_for(a.brand or spec.get("brand"), spec.get("theme"))
    bad = [i + 1 for i, c in enumerate(cards) if c.get("type") not in TYPES]
    if bad:
        raise SystemExit(f"unknown card type on slide(s) {bad}; types: {', '.join(TYPES)}")
    nosrc = [i + 1 for i, c in enumerate(cards) if c.get("type") in ("stat", "chart") and not c.get("source")]
    if nosrc:
        log(f"WARNING slides {nosrc}: stat/chart without a source (studio rule: no invented stats)")
    out = Path(a.out or Path(a.spec).with_suffix("")).resolve()
    aspect = a.aspect or spec.get("aspect", "4:5")
    paths = render_carousel(cards, out, aspect, theme, pdf=not a.no_pdf)
    sheet = contact_sheet(paths, out / "contact_sheet.jpg")
    for p in paths:
        print(p)
    if sheet:
        print(sheet)
