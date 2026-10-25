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

DEFAULT_THEME = {"look": "studio", "bg": "#0E0F13", "panel": "#16181F", "text": "#FFFFFF", "muted": "#A7ADBB", "accent": "#FFD43B", "accent2": "#4DA3FF",
                 "good": "#3CCB7F", "bad": "#FF5A5F", "font_display": None, "font_body": None, "font_hand": "Caveat:Bold", "radius": 0.035, "handle": "",
                 "highlight_style": "color", "grain": 0.0, "author": None, "logo": None}
# LOOKS = whole design systems, not colour swaps. "studio" is the old dark default (fine for video boards, reads generic on LinkedIn).
# The human looks copy what top creator carousels do: a person (headshot + name) on every slide, warm paper not black,
# a real type pairing, a marker stroke behind key words, handwritten notes/arrows, quiet page chrome. Brand colours slot into accent/marker.
LOOKS = {
    "studio": {},
    "creator": {"bg": "#F7F3EA", "panel": "#FFFFFF", "text": "#141414", "muted": "#6B6B6B", "accent": "#1B4DFF", "marker": "#FFE45C",
                "good": "#1E9E5A", "bad": "#D9412B", "font_display": "Space Grotesk:Bold", "font_body": "Inter:Regular",
                "highlight_style": "marker", "grain": 0.05, "radius": 0.03, "header": True, "footer": "hand"},
    "editorial": {"bg": "#F3EEE4", "panel": "#FFFFFF", "text": "#171512", "muted": "#6E675C", "accent": "#C2410C", "marker": "#F6D7B8",
                  "good": "#2F7D4F", "bad": "#B42318", "font_display": "Instrument Serif:Regular", "font_body": "Inter:Regular",
                  "highlight_style": "italic", "grain": 0.06, "radius": 0.0, "header": True, "footer": "rule", "kicker_style": "rule"},
    "brand-block": {"bg": "#1B4DFF", "panel": "#FFFFFF", "text": "#FFFFFF", "muted": "#DCE3FF", "accent": "#FFFFFF", "marker": "#0B1F7A",
                    "good": "#B8F5CF", "bad": "#FFC9C2", "font_display": "Inter:Black", "font_body": "Inter:Medium",
                    "highlight_style": "underline", "accent2": "#FFFFFF", "grain": 0.03, "radius": 0.02, "header": True, "footer": "bar", "alt_bg": "#F7F3EA", "alt_text": "#141414"},
}
BUNDLED = {"inter": "Inter-Variable.ttf", "space grotesk": "SpaceGrotesk-Variable.ttf", "instrument serif": "InstrumentSerif-Regular.ttf",
           "instrument serif italic": "InstrumentSerif-Italic.ttf", "fraunces": "Fraunces-Variable.ttf", "caveat": "Caveat-Variable.ttf",
           "dejavu sans": "DejaVuSans.ttf", "dejavu sans bold": "DejaVuSans-Bold.ttf", "dejavu serif": "DejaVuSerif.ttf"}
WEIGHTS = {"thin": 100, "extralight": 200, "light": 300, "regular": 400, "medium": 500, "semibold": 600, "bold": 700, "extrabold": 800, "black": 900}
CARDS_VERSION = 13  # bump when card layout changes (invalidates cached board clips)
TYPES = ("title", "stat", "list", "steps", "quote", "compare", "definition", "myth_fact", "chart", "cta")
ASPECT_PX = {"4:5": (1080, 1350), "1:1": (1080, 1080), "9:16": (1080, 1920), "16:9": (1920, 1080)}


# ---------------- theme + fonts ----------------
def theme_for(brand=None, overrides=None):
    """Brand guide colours/fonts (brands/<brand>.md edit-brand block) over the default dark theme."""
    t = dict(DEFAULT_THEME)
    look = (overrides or {}).get("look")
    if brand:
        from .presets import brand_guide
        g, _ = brand_guide(brand)
        c = g.get("colors", {})
        f = g.get("fonts", {})
        t["handle"] = g.get("handle", "")
        t["brand"] = brand
        cards = g.get("cards") if isinstance(g.get("cards"), dict) else {}
        look = look or cards.get("look")
        t.update(LOOKS.get(look or "studio", {}))  # look first, then the brand's own colours/fonts win
        exact = "edit-brand" in str(g.get("_source", ""))  # heuristic §6 parses may only tint the accent
        t.update({k: v for k, v in {"bg": c.get("background") if exact else None, "text": c.get("text") if exact else None, "accent": c.get("accent") or c.get("primary"),
                                     "accent2": c.get("secondary"), "marker": c.get("marker")}.items() if v})
        if f.get("display"):
            t["font_display"] = f["display"]
        if f.get("body"):
            t["font_body"] = f["body"]
        if g.get("logo"):
            t["logo"] = g["logo"].get("path") if isinstance(g["logo"], dict) else g["logo"]
        if g.get("author"):
            t["author"] = g["author"]
        t.update(cards)
    else:
        t.update(LOOKS.get(look or "studio", {}))
    t.update(overrides or {})
    t["look"] = look or t.get("look", "studio")
    return t


_FONT_CACHE = {}
_WARNED = set()


def font(theme, role, px):
    """Font for a role (display|body|hand). Theme values look like "Space Grotesk:Bold". Order: brand files in
    assets/fonts/<brand>/ (matched by family name), then bundled OFL fonts (tools/editor/fonts), then DejaVu."""
    spec = theme.get({"display": "font_display", "body": "font_body", "hand": "font_hand"}[role]) or ""
    fam, _, wt = spec.partition(":")
    wt = (wt or {"display": "Bold", "body": "Regular", "hand": "Bold"}[role]).replace(" ", "").lower()
    key = (theme.get("brand"), spec, role, px)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    cands = []
    bdir = REPO / "assets" / "fonts" / str(theme.get("brand") or "_none")
    if bdir.exists() and fam:
        want = fam.replace(" ", "").lower()
        base = want.replace("italic", "")
        files = [p for p in sorted(bdir.glob("*.[ot]tf")) if base in p.stem.replace(" ", "").replace("-", "").lower()
                 and (("italic" in p.stem.lower()) == ("italic" in want))]
        cands += sorted(files, key=lambda p: (wt not in p.stem.lower(), "variable" not in p.stem.lower()))
    if fam.lower() in BUNDLED:
        cands.append(TOOL / "fonts" / BUNDLED[fam.lower()])
    elif fam and not cands:  # brand font not installed yet: use the look's designed pairing, never silently DejaVu
        lk = LOOKS.get(theme.get("look") or "studio", {})
        alt = (lk.get({"display": "font_display", "body": "font_body", "hand": "font_hand"}[role]) or "").partition(":")[0].lower()
        if alt in BUNDLED:
            cands.append(TOOL / "fonts" / BUNDLED[alt])
            wk = (theme.get("brand"), fam)
            if wk not in _WARNED:
                _WARNED.add(wk)
                log(f"font '{fam}' not found in assets/fonts/{theme.get('brand')}/ - using {alt} (drop the brand font files there)")
    cands.append(TOOL / "fonts" / ("DejaVuSans-Bold.ttf" if role != "body" else "DejaVuSans.ttf"))
    for c in cands:
        try:
            f = ImageFont.truetype(str(c), px)
        except OSError:
            continue
        try:  # variable font: set weight (and optical size for display)
            axes = f.get_variation_axes()
            vals = []
            for ax in axes:
                n = ax["name"].decode() if isinstance(ax["name"], bytes) else ax["name"]
                v = ax["default"]
                if n.lower() == "weight":
                    v = max(ax["minimum"], min(ax["maximum"], WEIGHTS.get(wt, 400)))
                elif n.lower() == "optical size":
                    v = ax["maximum"] if role == "display" else ax["minimum"]
                vals.append(v)
            f.set_variation_by_axes(vals)
        except Exception:
            pass
        _FONT_CACHE[key] = f
        return f
    return ImageFont.load_default()


def lum(hexv):
    r, g, b, _ = rgb(hexv)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ink_on(hexv):
    """Readable text colour on a fill."""
    return "#141414" if lum(hexv) > 150 else "#FFFFFF"


def soft(draw, paint):
    """Translucent drawing that really blends (Pillow overwrites alpha when drawing on RGBA): paint on a layer, composite."""
    im = draw._image
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    paint(ImageDraw.Draw(layer))
    im.alpha_composite(layer)


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


_STYLE = {"hl": "color", "marker": "#FFE45C", "theme": None}


def _jit(seed, amp):
    """Deterministic wobble so hand-drawn marks look human but never flicker between animation frames."""
    return ((hash(seed) % 1000) / 1000.0 - 0.5) * 2 * amp


def marker_stroke(draw, x0, y0, x1, y1, colour, seed=""):
    """Highlighter swipe behind a word: slightly skewed, uneven ends, translucent."""
    h = y1 - y0
    j = lambda k: _jit(f"{seed}{k}", h * 0.08)
    pts = [(x0 - h * 0.08 + j(1), y0 + h * 0.18 + j(2)), (x1 + h * 0.1 + j(3), y0 + h * 0.12 + j(4)),
           (x1 + h * 0.06 + j(5), y1 - h * 0.02 + j(6)), (x0 - h * 0.04 + j(7), y1 + h * 0.04 + j(8))]
    soft(draw, lambda dd: dd.polygon(pts, fill=rgb(colour, 200)))


def scribble_underline(draw, x0, x1, y, colour, width, seed=""):
    """Hand-drawn underline: a gentle wave with a little overshoot."""
    n = 14
    pts = [(x0 - width + (x1 - x0 + 2 * width) * i / n, y + math.sin(i * 0.9 + (hash(seed) % 7)) * width * 0.6 + _jit(f"{seed}{i}", width * 0.3)) for i in range(n + 1)]
    draw.line(pts, fill=colour, width=width, joint="curve")


def italic_font(theme, px):
    """The brand display family's italic if its file exists (e.g. PlayfairDisplay-Italic), else Instrument Serif Italic."""
    fam, _, wt = (theme.get("font_display") or "").partition(":")
    bdir = REPO / "assets" / "fonts" / str(theme.get("brand") or "_none")
    if fam and bdir.exists() and any("italic" in p.stem.lower() and fam.replace(" ", "").lower() in p.stem.replace("-", "").lower() for p in bdir.glob("*.[ot]tf")):
        return font(dict(theme, font_display=f"{fam} Italic:{wt or 'Regular'}"), "display", px)
    return font(dict(theme, font_display="Instrument Serif Italic"), "display", px)


def draw_lines(draw, xy, lines, fnt, px, fill, spacing=1.18, align="left", box_w=None, highlight=None, hl_fill=None):
    """Draw wrapped lines. Text between *asterisks* (one word or a phrase) is highlighted in the theme's style:
    color (accent text) | marker (one highlighter swipe per run) | underline (scribble under the run) | italic (serif italic in accent)."""
    x0, y = xy
    style = _STYLE["hl"]
    th = _STYLE["theme"] or {}
    on = False  # inside a *phrase* across words and lines
    for li, ln in enumerate(lines):
        words = ln.split(" ")
        total = draw.textlength(ln.replace("*", ""), font=fnt)
        x = x0 + ((box_w - total) / 2 if align == "center" and box_w else 0)
        placed = []
        for i, w in enumerate(words):
            starts = w.startswith("*")
            hl = on or starts or (highlight and w.lower().strip(".,!?") in highlight)
            if starts and w.count("*") == 1:
                on = True
            if w.endswith("*") and (w.count("*") == 1 and not starts or w.count("*") == 2):
                on = False
                hl = True
            hl = hl and hl_fill is not None
            clean = w.replace("*", "")
            f = fnt
            if hl and style == "italic" and th:
                f = italic_font(th, px)
            wl = draw.textlength(clean, font=f)
            placed.append((x, clean, f, wl, hl))
            x += wl + (draw.textlength(" ", font=fnt) if i < len(words) - 1 else 0)
        if style in ("marker", "underline"):  # one stroke per contiguous run
            runs, cur = [], None
            for (wx, clean, f, wl, hl) in placed:
                if hl:
                    cur = [cur[0], wx + wl] if cur else [wx, wx + wl]
                elif cur:
                    runs.append(cur); cur = None
            if cur:
                runs.append(cur)
            for k, (rx0, rx1) in enumerate(runs):
                if style == "marker":
                    marker_stroke(draw, rx0, y + px * 0.12, rx1, y + px * 1.02, _STYLE["marker"], seed=f"{ln}{k}")
                else:
                    a = hl_fill[3] if isinstance(hl_fill, tuple) and len(hl_fill) == 4 else 255
                    scribble_underline(draw, rx0, rx1, y + px * 1.04, rgb(_STYLE.get("ul") or "#FFFFFF", a), max(2, int(px * 0.07)), seed=f"{ln}{k}")
        for (wx, clean, f, wl, hl) in placed:
            draw.text((wx, y), clean, font=f, fill=hl_fill if hl and style in ("color", "italic") else fill)
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


# ---------------- page furniture: paper, header, footer, notes ----------------
_BG = {}


def paint_bg(theme, W, H, colour=None):
    """Solid colour + fine paper grain (cached). Grain is what stops a flat fill from reading as a template."""
    colour = colour or theme["bg"]
    key = (colour, W, H, theme.get("grain", 0))
    if key not in _BG:
        im = Image.new("RGBA", (W, H), rgb(colour))
        g = float(theme.get("grain", 0) or 0)
        if g > 0:
            import random
            rnd = random.Random(7)
            small = Image.new("L", (W // 2, H // 2))
            small.putdata([int(128 + rnd.gauss(0, 60)) for _ in range((W // 2) * (H // 2))])
            noise = small.resize((W, H)).convert("RGBA")
            im = Image.blend(im, Image.composite(noise, im, Image.new("L", (W, H), 255)), g)
        _BG[key] = im
    return _BG[key].copy()


def header_h(theme, W, H, page):
    return int(min(W, H) * 0.12) if page and theme.get("header") and (theme.get("author") or theme.get("logo") or theme.get("handle")) else 0


def _path(p):
    if not p:
        return None
    q = Path(p)
    q = q if q.is_absolute() else REPO / q
    return q if q.exists() else None


def avatar(theme, size):
    """Round headshot from author.photo; initials disc when there is no photo yet (never a generated face)."""
    a = theme.get("author") or {}
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    m = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(m).ellipse([0, 0, size * 4 - 1, size * 4 - 1], fill=255)
    m = m.resize((size, size), Image.LANCZOS)
    ph = _path(a.get("photo"))
    if ph:
        src = Image.open(ph).convert("RGBA")
        sw, sh = src.size
        k = min(sw, sh)
        src = src.crop(((sw - k) // 2, max(0, int((sh - k) * 0.25)), (sw - k) // 2 + k, max(0, int((sh - k) * 0.25)) + k)).resize((size, size), Image.LANCZOS)
        im.paste(src, (0, 0), m)
    else:
        disc = Image.new("RGBA", (size, size), rgb(theme["accent"]))
        im.paste(disc, (0, 0), m)
        d = ImageDraw.Draw(im)
        ini = "".join(w[0] for w in str(a.get("name") or theme.get("handle") or "?").replace("@", "").split()[:2]).upper()
        f = font(theme, "display", int(size * 0.42))
        d.text((size / 2 - d.textlength(ini, font=f) / 2, size * 0.24), ini, font=f, fill=rgb(ink_on(theme["accent"])))
    return im


def chrome(img, d, theme, card, page, W, H, S, T, MU, A):
    """Header (who is talking) + footer (where you are). Quiet on purpose: content is the hero."""
    m = int(S * 0.08)
    hh = header_h(theme, W, H, page)
    if hh:
        a = theme.get("author") or {}
        size = int(S * 0.075)
        x = m
        if a or theme.get("handle"):
            img.alpha_composite(avatar(theme, size), (m, int(S * 0.045)))
            x = m + size + int(S * 0.022)
            nf = font(theme, "body", int(S * 0.03))
            nf_b = font(dict(theme, font_body=(theme.get("font_body") or "Inter").split(":")[0] + ":SemiBold"), "body", int(S * 0.03))
            d.text((x, int(S * 0.05)), a.get("name") or theme.get("handle", ""), font=nf_b, fill=T)
            sub = a.get("title") or (theme.get("handle") if a.get("name") else "")
            if sub:
                d.text((x, int(S * 0.05) + int(S * 0.038)), sub, font=nf, fill=MU)
        lp = _path(theme.get("logo"))
        if lp:
            lg = Image.open(lp).convert("RGBA")
            lh = int(S * 0.05)
            lg = lg.resize((max(1, int(lg.width * lh / lg.height)), lh), Image.LANCZOS)
            img.alpha_composite(lg, (W - m - lg.width, int(S * 0.058)))
    if not page:
        return
    i, n = page
    fy = H - int(H * 0.065)
    pf = font(theme, "body", int(S * 0.026))
    style = theme.get("footer", "text")
    if style == "rule":  # editorial: hairline + "03 / 08"
        d.line([m, fy - int(S * 0.02), W - m, fy - int(S * 0.02)], fill=rgb(theme["muted"], 110), width=max(1, int(S * 0.0025)))
        lab = f"{i:02d} / {n:02d}"
        d.text((W - m - d.textlength(lab, font=pf), fy), lab, font=pf, fill=MU)
        if theme.get("handle"):
            d.text((m, fy), theme["handle"], font=pf, fill=MU)
    elif style == "bar":  # progress bar segments
        seg_w = (W - 2 * m) / n
        for k in range(n):
            d.rounded_rectangle([m + k * seg_w + 3, fy + S * 0.012, m + (k + 1) * seg_w - 3, fy + S * 0.02], radius=4,
                                fill=rgb(theme["text"], 230 if k < i else 70))
    else:
        lab = f"{i}/{n}"
        if style == "hand":  # page count bottom-left, the handwritten swipe owns the right
            d.text((m, fy), lab, font=pf, fill=MU)
        else:
            d.text((W - m - d.textlength(lab, font=pf), fy), lab, font=pf, fill=MU)
            if theme.get("handle") and not hh:
                d.text((m, fy), theme["handle"], font=pf, fill=MU)
    if i < n and card.get("type") != "cta" and card.get("layout") != "cutout":
        if style == "hand":  # handwritten "swipe" + drawn arrow
            hf = font(theme, "hand", int(S * 0.05))
            txt = card.get("swipe", "swipe")
            tw = d.textlength(txt, font=hf)
            x = W - m - tw - int(S * 0.1)
            yy = fy - int(S * 0.035)
            d.text((x, yy), txt, font=hf, fill=A)
            ax0, ax1, ay = x + tw + int(S * 0.015), x + tw + int(S * 0.09), yy + int(S * 0.04)
            d.line([(ax0, ay + 4), ((ax0 + ax1) / 2, ay - 3), (ax1, ay)], fill=A, width=max(2, int(S * 0.005)), joint="curve")
            d.line([(ax1 - S * 0.02, ay - S * 0.018), (ax1, ay), (ax1 - S * 0.022, ay + S * 0.014)], fill=A, width=max(2, int(S * 0.005)))
        elif style not in ("bar", "rule"):
            d.text((W / 2 - d.textlength("swipe →", font=pf) / 2, fy), "swipe →", font=pf, fill=A)


def hand_note(d, theme, note, x, y, S, A):
    """A handwritten aside ("this one surprised me") - the cheapest way to look made by a person."""
    hf = font(theme, "hand", int(S * 0.055))
    d.text((x, y), note, font=hf, fill=A)
    return y + S * 0.07


# ---------------- images: own photos, free-licensed downloads, AI assets ----------------
def cover(im, w, h, focus=(0.5, 0.38)):
    """Crop-to-fill around a focus point (faces usually sit in the upper third)."""
    sw, sh = im.size
    k = max(w / sw, h / sh)
    im = im.resize((max(1, int(sw * k + 0.5)), max(1, int(sh * k + 0.5))), Image.LANCZOS)
    fx, fy = focus
    x = int(min(max(0, im.width * fx - w / 2), im.width - w))
    y = int(min(max(0, im.height * fy - h / 2), im.height - h))
    return im.crop((x, y, x + w, y + h))


def rounded(im, r):
    m = Image.new("L", (im.width * 2, im.height * 2), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width * 2 - 1, im.height * 2 - 1], radius=r * 2, fill=255)
    out = im.convert("RGBA")
    out.putalpha(Image.composite(out.getchannel("A"), Image.new("L", im.size, 0), m.resize(im.size, Image.LANCZOS)))
    return out


def placeholder(w, h, theme, label, kind):
    """Visible stand-in while the asset is missing: drafts show the layout, nobody mistakes it for final."""
    im = Image.new("RGBA", (w, h), rgb(theme.get("panel", "#FFFFFF")))
    d = ImageDraw.Draw(im)
    step = max(12, w // 18)
    for x in range(-h, w, step):
        d.line([(x, h), (x + h, 0)], fill=rgb(theme["muted"], 45), width=2)
    d.rectangle([1, 1, w - 2, h - 2], outline=rgb(theme["muted"], 160), width=3)
    S = min(w, h)
    f = font(theme, "body", max(14, int(S * 0.07)))
    head = {"gen": "AI ASSET", "missing": "ADD PHOTO"}.get(kind, "IMAGE")
    d.text((S * 0.08, S * 0.08), head, font=font(theme, "display", max(16, int(S * 0.09))), fill=rgb(theme["accent"]))
    for i, ln in enumerate(wrap(d, label[:140], f, w - S * 0.16)[:4]):
        d.text((S * 0.08, S * 0.22 + i * S * 0.09), ln, font=f, fill=rgb(theme["text"]))
    return im


def load_image(r, w, h, theme, keep_alpha=False):
    if r and r.get("path"):
        im = Image.open(r["path"])
        if keep_alpha and im.mode in ("RGBA", "LA", "P"):
            return im.convert("RGBA")
        return cover(im.convert("RGB"), w, h, tuple(r.get("focus") or (0.5, 0.38))).convert("RGBA")
    return placeholder(w, h, theme, (r or {}).get("label", "image"), (r or {}).get("kind", "missing"))


def image_layer(img, theme, card, W, H, S, top):
    """Lay out the card's image; returns (text box, theme override). Layouts:
    photo (full-bleed + scrim, text bottom) | split (image top, text below) | inset (text top, framed image below) |
    screen (browser frame around a real screenshot) | polaroid (tilted print + handwritten caption) | cutout (founder PNG beside the text)."""
    from .assets import resolve
    r = resolve(card["image"], theme.get("brand"))
    lay = card.get("layout") or ("photo" if card.get("type") in ("title", "quote", "cta") else "split")
    m = int(S * 0.08)
    foot = H - int(H * 0.11)
    rad = int(S * max(0.012, theme.get("radius", 0.03)))
    credit = (r or {}).get("credit")
    over = {}
    if lay == "photo":
        im = load_image(r, W, H, theme)
        img.alpha_composite(im)
        scrim = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(scrim)
        for yy in range(H):  # bottom scrim for the text + light top scrim for the header
            a = max(0.0, (yy / H - 0.36) / 0.64) ** 1.1 * 225 + max(0.0, (0.22 - yy / H) / 0.22) ** 0.8 * 170
            sd.line([(0, yy), (W, yy)], fill=(10, 10, 12, int(min(235, a))))
        img.alpha_composite(scrim)
        over = {"text": "#FFFFFF", "muted": "#E4E4E4", "_photo": True, "highlight_style": "color", "accent": theme.get("marker", "#FFE45C")}
        box = (m, int(H * 0.5), W - m, foot)
        cy = foot - S * 0.03
    elif lay == "cutout":
        ch = int(H * (0.62 if H > W else 0.8))
        im = load_image(r, int(ch * 0.8), ch, theme, keep_alpha=True)
        if im.mode == "RGBA" and r and r.get("path") and im.getchannel("A").getextrema()[0] < 250:
            k = min(ch / im.height, W * 0.5 / im.width)  # never wider than half the slide
            im = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))), Image.LANCZOS)
            blob = Image.new("RGBA", (W, H), (0, 0, 0, 0))  # soft brand-colour shape behind the person
            bd = ImageDraw.Draw(blob)
            cx = W - im.width // 2 - int(S * 0.02)
            bd.ellipse([cx - im.width * 0.55, H - ch * 0.78, cx + im.width * 0.55, H - ch * 0.78 + im.width * 1.1], fill=rgb(theme.get("marker", theme["accent"]), 170))
            img.alpha_composite(blob)
            img.alpha_composite(im, (W - im.width, H - im.height))
        else:  # no transparent cutout yet: framed portrait in the right column
            pw, ph = int(W * 0.4), int(H * 0.5)
            img.alpha_composite(rounded(load_image(r, pw, ph, theme), rad), (W - m - pw, int(top + (foot - top - ph) / 2)))
        box = (m, top, int(W * 0.58), foot)
        cy = foot
    else:  # split / inset / screen / polaroid
        if lay == "split":
            iy0, iy1 = top, int(top + (foot - top) * 0.5)
            box = (m, iy1 + int(S * 0.05), W - m, foot)
        else:
            iy0, iy1 = int(top + (foot - top) * 0.47), foot - int(S * 0.02)
            box = (m, top, W - m, iy0 - int(S * 0.04))
        iw, ih = W - 2 * m, iy1 - iy0
        if lay == "screen":
            bar = int(S * 0.045)
            frame = Image.new("RGBA", (iw, ih), rgb("#FFFFFF"))
            fd = ImageDraw.Draw(frame)
            fd.rectangle([0, 0, iw, bar], fill=rgb("#ECECEC"))
            for k, col in enumerate(("#FF5F57", "#FEBC2E", "#28C840")):
                fd.ellipse([bar * 0.45 + k * bar * 0.55, bar * 0.33, bar * 0.45 + k * bar * 0.55 + bar * 0.34, bar * 0.67], fill=rgb(col))
            frame.alpha_composite(load_image(r, iw, ih - bar, theme), (0, bar))
            sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(sh).rounded_rectangle([m, iy0 + S * 0.012, m + iw, iy1 + S * 0.018], radius=rad, fill=(0, 0, 0, 70))
            from PIL import ImageFilter
            img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(S * 0.015)))
            img.alpha_composite(rounded(frame, rad), (m, iy0))
        elif lay == "polaroid":
            side = min(iw * 0.72, (ih - S * 0.05) / 1.2)  # leave room for tilt + credit
            pad = side * 0.05
            pol = Image.new("RGBA", (int(side), int(side + pad * 2.6)), rgb("#FFFFFF"))
            pol.alpha_composite(load_image(r, int(side - 2 * pad), int(side - 2 * pad), theme), (int(pad), int(pad)))
            cap = (card["image"].get("caption") if isinstance(card["image"], dict) else None) or card.get("caption")
            if cap:
                pd = ImageDraw.Draw(pol)
                hf = font(theme, "hand", int(side * 0.075))
                pd.text((pad, side - pad * 0.6), cap, font=hf, fill=rgb("#2A2A2A"))
            ang = card.get("tilt", -3)
            rot = pol.rotate(ang, expand=True, resample=Image.BICUBIC)
            sh = Image.new("RGBA", rot.size, (0, 0, 0, 0))
            sh.putalpha(rot.getchannel("A").point(lambda v: int(v * 0.35)))
            from PIL import ImageFilter
            sh = sh.filter(ImageFilter.GaussianBlur(S * 0.01))
            px_ = int(m + (iw - rot.width) / 2)
            img.alpha_composite(sh, (px_ + int(S * 0.008), iy0 + int(S * 0.012)))
            img.alpha_composite(rot, (px_, iy0))
        else:
            img.alpha_composite(rounded(load_image(r, iw, ih, theme), rad), (m, iy0))
        cy = iy1 + S * 0.004
    if credit:
        cf = font(theme, "body", int(S * 0.019))
        cd = ImageDraw.Draw(img, "RGBA")
        ctext = credit[:110]
        cx = m if over.get("_photo") else W - m - cd.textlength(ctext, font=cf)  # right-aligned under the image
        cd.text((cx, cy), ctext, font=cf, fill=rgb("#FFFFFF" if over.get("_photo") else theme["muted"], 210))
    return box, over


# ---------------- card renderer ----------------
_DY = {}


def render_card(card, W, H, theme, p=1.0, mode="full", page=None):
    """One frame of a card at reveal progress p (1.0 = static). Returns RGBA Image (transparent outside the panel in 'panel' mode).
    Full-frame cards are optically centred (slightly above middle) using the finished layout, so animation frames never jitter."""
    if mode == "full" and card.get("type") in ("title", "stat", "quote", "definition", "steps", "list", "cta") and not card.get("image"):
        key = json.dumps([card, W, H, theme.get("brand"), theme.get("look"), theme.get("font_display"), bool(page)], sort_keys=True)
        if key not in _DY:
            probe_img = _render(card, W, H, theme, 1.0, mode, page, 0, content_only=True)
            bb = probe_img.getbbox()
            S = min(W, H)
            top, bottom = int(H * 0.09) + header_h(theme, W, H, page), H - int(H * 0.11)
            _DY[key] = max(0, int(((bottom - top) - (bb[3] - bb[1])) * 0.42 + top - bb[1])) if bb else 0
        return _render(card, W, H, theme, p, mode, page, _DY[key])
    if mode == "panel":
        key = json.dumps(["panel", card, W, H, theme.get("brand"), theme.get("look"), theme.get("font_display")], sort_keys=True)
        if key not in _DY:
            bb = _render(card, W, H, theme, 1.0, mode, None, 0, content_only=True).getbbox()
            S = min(W, H)
            _DY[key] = int(min(H * 0.40, max(H * 0.16, (bb[3] - int(H * 0.06)) + S * 0.09))) if bb else int(H * 0.40)
        return _render(card, W, H, theme, p, mode, page, 0, panel_h=_DY[key])
    return _render(card, W, H, theme, p, mode, page, 0)


def _render(card, W, H, theme, p, mode, page, dy, content_only=False, panel_h=None):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img, "RGBA")  # blend translucent fills (pills, markers, shadows) instead of punching holes
    S = min(W, H)
    alt = card.get("alt") and theme.get("alt_bg")  # brand-block: alternate slides flip to paper
    if alt:
        theme = dict(theme, bg=theme["alt_bg"], text=theme.get("alt_text", "#141414"), muted="#6B6B6B", accent=theme.get("marker", "#1B4DFF"))
    _STYLE.update(hl=theme.get("highlight_style", "color"), marker=theme.get("marker", theme["accent"]), theme=theme,
                  ul=theme.get("accent2") if theme.get("look") == "brand-block" else theme.get("accent"))
    if mode == "panel":
        bx0, by0, bx1 = int(W * 0.05), int(H * 0.06), int(W * 0.95)
        by1 = int(H * 0.06 + H * 0.40)
        lift = int((1 - ease_out(p / 0.35)) * S * 0.04)
        if not content_only:
            a = int(235 * ease_out(p / 0.25))
            if theme.get("look", "studio") != "studio":  # soft shadow under a light card
                sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                ImageDraw.Draw(sh).rounded_rectangle([bx0, by0 + lift + S * 0.01, bx1, by0 + (panel_h or (by1 - by0)) + lift + S * 0.015],
                                                    radius=int(S * theme["radius"]), fill=(0, 0, 0, int(60 * a / 235)))
                from PIL import ImageFilter
                img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(S * 0.012)))
            d.rounded_rectangle([bx0, by0 + lift, bx1, by0 + (panel_h or (by1 - by0)) + lift], radius=int(S * theme["radius"]),
                                fill=rgb(theme["bg"] if theme.get("look", "studio") != "studio" else theme["panel"], a))
        box = (bx0 + int(S * 0.05), by0 + lift + int(S * 0.045), bx1 - int(S * 0.05), by1 + lift - int(S * 0.045))
    else:
        if not content_only:
            bg = paint_bg(theme, W, H)
            if p < 0.2:
                bg.putalpha(int(255 * ease_out(p / 0.2)))
            img.alpha_composite(bg)
        m = int(S * 0.08)
        box = (m, int(H * 0.09) + header_h(theme, W, H, page) + dy, W - m, H - int(H * 0.11))
        if card.get("image") and not content_only:
            box, over = image_layer(img, theme, card, W, H, S, int(H * 0.07) + header_h(theme, W, H, page))
            if over:
                theme = dict(theme, **{k: v for k, v in over.items() if not k.startswith("_")})
                _STYLE.update(theme=theme, hl=theme.get("highlight_style", "color"))
    x0, y0, x1, y1 = box
    foot_y = H - int(H * 0.11)
    src_y = (foot_y + S * 0.015) if mode == "full" else (by0 + (panel_h or (by1 - by0)) - S * 0.04)
    bw, bh = x1 - x0, y1 - y0
    T, A, MU = rgb(theme["text"]), rgb(theme["accent"]), rgb(theme["muted"])
    t = card.get("type", "title")
    y = y0
    if card.get("kicker"):
        kf = font(dict(theme, font_body=(theme.get("font_body") or "Inter").split(":")[0] + ":SemiBold"), "body", int(S * 0.03))
        ktxt = card["kicker"].upper()
        if theme.get("kicker_style") == "rule":
            d.line([x0, y + S * 0.018, x0 + S * 0.06, y + S * 0.018], fill=A, width=max(2, int(S * 0.004)))
            d.text((x0 + S * 0.08, y), ktxt, font=kf, fill=A)
        elif theme.get("look") == "creator":
            tw = d.textlength(ktxt, font=kf)
            pill = (0, 0, 0, 110) if theme["text"].upper() == "#FFFFFF" else rgb(theme["accent"], 30)  # dark backing on photos
            soft(d, lambda dd: dd.rounded_rectangle([x0, y - S * 0.008, x0 + tw + S * 0.04, y + S * 0.045], radius=int(S * 0.026), fill=pill))
            d.text((x0 + S * 0.02, y), ktxt, font=kf, fill=A)
        else:
            d.text((x0, y), ktxt, font=kf, fill=A)
        y += int(S * 0.065)
    reveal = lambda i, n: stagger(p, i, n)

    if t in ("title", "cta"):
        f, lines, px = fit_text(d, card.get("title", ""), theme, "display", bw, bh * 0.55, int(S * 0.11))
        y = draw_lines(d, (x0, y + (1 - reveal(0, 2)) * S * 0.03), lines, f, px, T, hl_fill=A)
        if card.get("body"):
            f2, l2, px2 = fit_text(d, card["body"], theme, "body", bw, bh * 0.3, int(S * 0.045))
            y = draw_lines(d, (x0, y + S * 0.03), l2, f2, px2, rgb(theme["muted"], int(255 * reveal(1, 2))))
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
        y = y + n * row_h

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
            d.rounded_rectangle([cx0, cy0, cx1, cy1], radius=int(S * 0.025), fill=rgb((theme["panel"] if mode == "full" else theme["bg"]), int(al * (0.9 if theme.get("look", "studio") == "studio" else 1.0))),
                                outline=rgb(colr, al), width=max(2, int(S * 0.005)))
            pad = S * 0.035
            pfill = theme["panel"] if mode == "full" else theme["bg"]
            ptxt = rgb(ink_on(pfill), al) if theme.get("look", "studio") != "studio" else rgb(theme["text"], al)
            if theme.get("look", "studio") != "studio" and abs(lum(colr) - lum(pfill)) < 60:  # label colour too close to the panel
                colr = theme.get("marker") if abs(lum(theme.get("marker", "#000000")) - lum(pfill)) > 60 else ink_on(pfill)
            d.text((cx0 + pad, cy0 + pad), str(col.get("title", "")).upper(), font=font(theme, "display", int(S * 0.04)), fill=rgb(colr, al))
            txt = "\n".join(col.get("items", []))
            ff, ll, pp = fit_text(d, txt, theme, "body", cx1 - cx0 - 2 * pad, cy1 - cy0 - pad * 2 - S * 0.07, int(S * 0.05))
            draw_lines(d, (cx0 + pad, cy0 + pad + S * 0.07), ll, ff, pp, ptxt, hl_fill=rgb(theme["accent"], al))

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

    if card.get("note") and t not in ("compare", "myth_fact", "chart"):
        hand_note(d, theme, card["note"], x0 + S * 0.02, min(y + S * 0.05, y1 - S * 0.06), S, A)
    if content_only:
        return img
    if card.get("source"):
        sf = font(theme, "body", int(S * 0.022))
        d.text((x0, src_y), "Source: " + card["source"], font=sf, fill=rgb(theme["muted"], int(200 * min(1, p * 2))))
    if page or header_h(theme, W, H, page):
        chrome(img, d, theme, card, page, W, H, S, T, MU, A)
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
    """editor.py cards SPEC.json [--aspect 4:5 --brand B --look creator|editorial|brand-block|studio --out DIR --no-pdf]"""
    spec = rjson(a.spec)
    cards = spec.get("cards", spec if isinstance(spec, list) else [])
    over = dict(spec.get("theme") or {})
    if getattr(a, "look", None):
        over["look"] = a.look
    theme = theme_for(a.brand or spec.get("brand"), over)
    bad = [i + 1 for i, c in enumerate(cards) if c.get("type") not in TYPES]
    if bad:
        raise SystemExit(f"unknown card type on slide(s) {bad}; types: {', '.join(TYPES)}")
    nosrc = [i + 1 for i, c in enumerate(cards) if c.get("type") in ("stat", "chart") and not c.get("source")]
    if nosrc:
        log(f"WARNING slides {nosrc}: stat/chart without a source (studio rule: no invented stats)")
    out = Path(a.out or Path(a.spec).with_suffix("")).resolve()
    aspect = a.aspect or spec.get("aspect", "4:5")
    paths = render_carousel(cards, out, aspect, theme, pdf=not a.no_pdf)
    from .assets import assets_needed, resolve
    need = assets_needed(cards, theme, out / "ASSETS_NEEDED.md")
    if need:
        log(f"placeholders on some slides: see {need}")
    credits = [f"- slide {i}: {r['credit']}" for i, c in enumerate(cards, 1) if c.get("image")
               for r in [resolve(c["image"], theme.get("brand"))] if r and r.get("credit")]
    if credits:
        (out / "CREDITS.md").write_text("# Image credits (keep in the post caption or first comment when the licence asks for it)\n" + "\n".join(credits) + "\n", encoding="utf-8")
    sheet = contact_sheet(paths, out / "contact_sheet.jpg")
    for p in paths:
        print(p)
    if sheet:
        print(sheet)
