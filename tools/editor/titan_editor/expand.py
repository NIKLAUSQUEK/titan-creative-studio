"""TRIAL REEL EXPANDER: one finished edit -> 10-15 genuinely different variants for testing (IG Trial Reels, TikTok, Shorts, A/B ads).

  editor.py expand --project P [--count 12] [--version 4] [--final] [--speeds 1.0,1.4] [--reels-only]

Axes it varies (each variant differs from every other on at least 3):
  format     reel | carousel (text-heavy / image-heavy) | single image (quote card / poster)
  hook       original | another footage hook moved first (payoff-first cold open) | a different on-screen hook header
  header     intro header (first ~2.5 s) | persistent top header | none
  duration   full | short (~60%) | micro (hook + payoff + CTA)
  speed      1.0-1.4x (pitch-preserving atempo), from --speeds
  captions   7 style packs (pop, karaoke, sentence, serif, caps-punch, minimal, brand)
  sequence   original | one swap of two adjacent self-contained body beats
  framing    punch-in level and crop offset, small grade nudge
Story guard: hook stays first (or is replaced by another hook beat), CTA stays last, turn/lesson/payoff beats are never dropped,
beats marked fixed never move, and a beat whose line leans on the previous one ("so", "and", "but", "that's why", "this") is never
swapped. Zero Claude tokens: hooks and headers come from the brief; Claude only needs to review the VARIANTS.md table.
"""
import copy, itertools, json, random, re, shutil
from pathlib import Path

from .common import REPO, TOOL, ffmpeg, log, rjson, wjson
from .ingest import load_clips
from .presets import deep_merge
from .recipe import auto_sfx, item_starts, load, place_zooms, prune_anchors

MOVABLE = {"body", "context", "example", "proof", None}
KEEP = {"hook", "turn", "lesson", "payoff", "cta"}
LEANS = re.compile(r"^\s*(so|and|but|because|that'?s why|this|which|then|also|plus|it|they|that)\b", re.I)
PACKS = {
    "brand": {},
    "pop-yellow": {"animation": "pop", "max_words": 2, "uppercase": True, "highlight": "#FFE14D", "keyword_caps": True, "size_mul": 1.2},
    "karaoke-green": {"animation": "karaoke", "max_words": 4, "uppercase": False, "highlight": "#3CFF6E", "size_mul": 1.05},
    "sentence-clean": {"animation": "fade", "max_words": 7, "uppercase": False, "keyword_caps": False, "size_mul": 0.9},
    "serif-classic": {"font": "DejaVu Serif", "bold": False, "animation": "static", "max_words": 5, "keyword_caps": False},
    "caps-punch": {"animation": "pop", "max_words": 1, "uppercase": True, "highlight": "#FF5FC8", "size_mul": 1.45},
    "minimal-low": {"animation": "static", "max_words": 4, "position_y": 0.76, "outline": 2, "size_mul": 0.85, "keyword_caps": False},
}
FILLERS = re.compile(r"\b(um+|uh+|erm|er|ah|hmm)\b[,.]?\s*", re.I)
CTA_LIKE = re.compile(r"\b(follow|subscribe|link in (my )?bio|comment|dm me|book (now|a|your)|save this|share this|part \d|part two)\b", re.I)


def headline(text, max_words=11):
    """Header text: whole hook if short, else cut at a clause boundary, never mid-phrase."""
    t = clean(text)
    w = t.split()
    if len(w) <= max_words:
        return t.rstrip(".")
    for m in re.finditer(r"[,:;.?!]", t):
        if 3 <= len(t[: m.start()].split()) <= max_words:
            cut = t[: m.start()]
    return (locals().get("cut") or " ".join(w[:max_words])).rstrip(",;: .")


def clean(line, n=None):
    t = re.sub(r"\s+", " ", FILLERS.sub("", line or "")).strip()
    t = t[0].upper() + t[1:] if t else t
    if n and len(t.split()) > n:
        t = " ".join(t.split()[:n]).rstrip(",;:") + "…"
    return t


# ---------------- beat planning ----------------
def beat_table(r, brief, clips):
    bb = brief.get("beats", [])
    score = {}
    for c in clips.values():
        for s in c["an"]["sentences"]:
            score[(c["id"], round(s["t0"], 2))] = s.get("hook_score", 0)
    rows = []
    for b in r["beats"]:
        src = bb[b["i"]] if b["i"] < len(bb) else {}
        role = src.get("role") or (b.get("beat") if b.get("beat") in KEEP | MOVABLE else "body")
        rows.append({"i": b["i"], "role": role, "fixed": bool(src.get("fixed")) or role in ("hook", "cta"), "line": src.get("line") or "",
                     "dur": b["t1"] - b["t0"], "score": score.get((b["clip"], round(b["t0"], 2)), 0)})
    return rows


def plan_order(rows, hook_i=None, swap=False, duration="full", rng=None):
    order = list(rows)
    if hook_i is not None and order and order[0]["i"] != hook_i:
        k = next((j for j, x in enumerate(order) if x["i"] == hook_i), None)
        if k is not None and order[k]["role"] != "cta":
            order.insert(0, order.pop(k))
    if swap:
        pairs = [j for j in range(1, len(order) - 2) if order[j]["role"] in MOVABLE and order[j + 1]["role"] in MOVABLE
                 and not order[j]["fixed"] and not order[j + 1]["fixed"] and not LEANS.match(order[j]["line"]) and not LEANS.match(order[j + 1]["line"])]
        if pairs:
            j = (rng or random).choice(pairs)
            order[j], order[j + 1] = order[j + 1], order[j]
        else:
            swap = False
    if duration != "full":
        total = sum(x["dur"] for x in order)
        target = total * 0.6 if duration == "short" else min(12.0, total * 0.4)
        droppable = sorted([x for x in order[1:] if x["role"] not in KEEP and not x["fixed"]], key=lambda x: x["score"])
        while droppable and sum(x["dur"] for x in order) > target:
            order.remove(droppable.pop(0))
        if duration == "micro":  # still too long: keep hook + the strongest non-CTA beat + CTA
            if sum(x["dur"] for x in order) > target and len(order) > 3:
                mid = max(order[1:-1], key=lambda x: (x["role"] in KEEP, x["score"]))
                order = [order[0], mid] + ([order[-1]] if order[-1]["role"] == "cta" else [])
    return order, swap


# ---------------- reel variant recipe ----------------
def reel_recipe(base, rows, v, brief, hooks):
    r = copy.deepcopy(base)
    order, swapped = plan_order(rows, v["hook_i"], v["swap"], v["duration"], v["rng"])
    v["swap"] = swapped
    groups = {}
    for it in r["items"]:
        groups.setdefault(it["beat"], []).append(it)
    r["items"] = [dict(it) for x in order for it in groups.get(x["i"], [])]
    r["beats"] = [b for x in order for b in base["beats"] if b["i"] == x["i"]]
    for it in r["items"]:
        it["speed"] = round(it.get("speed", 1.0) * v["speed"], 3)
        it["focus_x"] = round(min(0.6, max(0.4, it.get("focus_x", 0.5) + v["shift"])), 3)
    st = r["style"]
    pack = dict(PACKS[v["captions"]])
    mul = pack.pop("size_mul", 1.0)
    st["captions"] = deep_merge(st["captions"], pack)
    st["captions"]["size"] = round(st["captions"]["size"] * mul, 4)
    sz = st.get("safe_zone", {})
    st["captions"]["position_y"] = min(1 - sz.get("bottom", 0.2), max(sz.get("top", 0.14) + 0.05, st["captions"].get("position_y", 0.7)))
    st["zoom"]["scale"] = round(st["zoom"].get("scale", 1.08) * v["punch"], 3)
    st["grade"] = deep_merge(st.get("grade", {}), {"saturation": round(st.get("grade", {}).get("saturation", 1.0) + v["sat"], 3)})
    place_zooms(r["items"], st)
    r["texts"] = [t for t in r["texts"] if t["type"] not in ("hook", "header")]
    if v["header"] != "none" and r["items"]:
        _, body = item_starts(r)
        dur = body if v["header"] == "persistent" else st["hook_text"].get("dur_s", 2.6)
        r["texts"].insert(0, {"type": "header" if v["header"] == "persistent" else "hook", "text": v["header_text"],
                              "anchor": {"item": r["items"][0]["id"], "offset": 0.0}, "dur": round(dur, 2),
                              **({"position_y": max(sz.get("top", 0.14) + 0.04, 0.19)} if v["header"] == "persistent" else {})})
    prune_anchors(r)
    r["audio"]["sfx"] = auto_sfx(r)
    r["outputs"] = [{"aspect": a} for a in v["aspects"]]
    r["variant"] = {k: v[k] for k in ("id", "format", "hook", "header", "header_text", "duration", "speed", "captions", "swap", "punch")}
    return r, order


# ---------------- stills: carousel + single image ----------------
def font(style_font, size, bold=True, brand=None):
    from PIL import ImageFont
    cands = []
    if brand and style_font:
        cands += sorted((REPO / "assets" / "fonts" / brand).glob(f"{style_font.replace(' ', '')}*.[ot]tf")) + \
                 sorted((REPO / "assets" / "fonts" / brand).glob(f"{style_font.split()[0]}*.[ot]tf"))
    cands += [TOOL / "fonts" / ("DejaVuSerif.ttf" if style_font and "Serif" in style_font else "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")]
    for c in cands:
        try:
            return ImageFont.truetype(str(c), int(size))
        except Exception:
            continue
    return ImageFont.load_default()


def wrap(draw, text, f, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= width or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + ([cur] if cur else [])


def frame_for(r, beat_i, clips, out, W, H):
    """Best still for a beat: its B-roll if it has one, else the middle of its first A-roll item; cover-cropped to W x H."""
    its = [it for it in r["items"] if it["beat"] == beat_i]
    if not its:
        return None
    br = next((b for b in r["broll"] if b["anchor"].get("item") in {i["id"] for i in its}), None)
    if br:
        src, t = br["path"], (br.get("src_in", 0) + br["dur"] / 2) if br.get("kind") == "video" else None
    else:
        it = its[0]; src, t = clips[it["clip"]]["meta"]["path"], (it["in"] + it["out"]) / 2
    ffmpeg((["-ss", f"{t:.2f}"] if t is not None else []) + ["-i", src, "-vf", f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}", "-frames:v", 1, "-q:v", 3, out], check=False)
    return out if Path(out).exists() else None


def hex_rgb(h, default=(17, 17, 17)):
    try:
        h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    except Exception:
        return default


def slide(kind, text, img, W, H, st, brand, page=None, sub=None):
    from PIL import Image, ImageDraw, ImageFilter
    colors = st.get("colors", {})
    bg, fg = hex_rgb(colors.get("primary"), (17, 17, 17)), hex_rgb(colors.get("text"), (255, 255, 255))
    if sum(bg) > 600 and sum(fg) > 600:
        fg = (20, 20, 20)
    fonts = st.get("fonts", {})
    if kind == "text":   # text-heavy: brand colour field, big words, optional small photo strip
        im = Image.new("RGB", (W, H), bg)
        d = ImageDraw.Draw(im)
        if img:
            ph = Image.open(img).convert("RGB").resize((W, int(H * 0.28)))
            im.paste(ph, (0, H - ph.height))
        f = font(fonts.get("display"), W * 0.075, True, brand)
        lines = wrap(d, text, f, W * 0.84)
        y = H * 0.12
        for ln in lines[:9]:
            d.text((W * 0.08, y), ln, font=f, fill=fg); y += f.size * 1.22
        if sub:
            d.text((W * 0.08, y + f.size * 0.4), sub, font=font(fonts.get("body"), W * 0.035, False, brand), fill=fg)
    else:                # image-heavy: full-bleed photo, gradient, short line
        im = Image.open(img).convert("RGB").resize((W, H)) if img else Image.new("RGB", (W, H), bg)
        grad = Image.new("L", (1, H))
        for yy in range(H):
            grad.putpixel((0, yy), int(max(0, (yy / H - 0.5)) * 2 * 210))
        im = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), im, grad.resize((W, H)))
        d = ImageDraw.Draw(im)
        f = font(fonts.get("display"), W * 0.062, True, brand)
        lines = wrap(d, text, f, W * 0.86)[:4]
        y = H * 0.93 - len(lines) * f.size * 1.2
        for ln in lines:
            d.text((W * 0.07, y), ln, font=f, fill=(255, 255, 255), stroke_width=max(1, W // 400), stroke_fill=(0, 0, 0)); y += f.size * 1.2
    if page:
        d.text((W * 0.9, H * 0.03), page, font=font(None, W * 0.03, True), fill=(255, 255, 255) if kind != "text" else fg)
    return im


def stills_variant(base, rows, v, brief, clips, out_dir, W, H, tmp):
    order, _ = plan_order(rows, None, False, "full")
    hook = v["header_text"]
    st = base["style"]
    brand = base.get("brand")
    cta = (brief.get("cta") or {}).get("on_screen") or " · ".join(base["end_card"].get("lines") or []) or (brand or "").replace("-", " ").title()
    out_dir.mkdir(parents=True, exist_ok=True)
    files, texts = [], [hook, cta]
    if v["format"].startswith("carousel"):
        kind = "text" if v["format"].endswith("text") else "image"
        body = [x for x in order[1:] if x["role"] != "cta"][:6]
        pages = 2 + len(body)
        img0 = frame_for(base, order[0]["i"], clips, tmp / f"{v['id']}_0.jpg", W, H if kind == "image" else int(H * 0.28))
        sl = [slide(kind, hook, img0, W, H, st, brand, f"1/{pages}")]
        for k, x in enumerate(body, 2):
            txt = clean(x["line"], 26 if kind == "text" else 12)
            texts.append(txt)
            img = frame_for(base, x["i"], clips, tmp / f"{v['id']}_{k}.jpg", W, H if kind == "image" else int(H * 0.28))
            sl.append(slide(kind, txt, img if kind == "image" or k % 2 == 0 else None, W, H, st, brand, f"{k}/{pages}"))
        sl.append(slide("text", cta, None, W, H, st, brand, f"{pages}/{pages}", sub="Save this. Share it with someone who needs it."))
        for k, im in enumerate(sl, 1):
            p = out_dir / f"slide_{k:02d}.png"; im.save(p); files.append(str(p))
    else:
        kind = "text" if v["format"].endswith("quote") else "image"
        best = max(order[1:] or order, key=lambda x: (x["role"] in ("lesson", "payoff", "turn"), x["score"]))
        txt = hook if kind == "image" else clean(best["line"], 24)
        texts.append(txt)
        img = frame_for(base, order[0]["i"] if kind == "image" else best["i"], clips, tmp / f"{v['id']}_s.jpg", W, H if kind == "image" else int(H * 0.28))
        p = out_dir / "image.png"; slide(kind, txt, img, W, H, st, brand, sub=None if kind == "image" else cta).save(p); files.append(str(p))
    return files, texts


# ---------------- matrix ----------------
def build_matrix(n, rows, brief, base, speeds, reels_only, seed):
    rng = random.Random(seed)
    hooks = [h for h in sorted(brief.get("hooks", []), key=lambda h: h.get("rank", 9)) if h.get("text")]
    first_line = rows[0]["line"] if rows else ""
    cta_lines = {clean(x["line"]).lower() for x in rows if x["role"] == "cta"}
    texts = [headline(h["text"]) for h in hooks if clean(h["text"]).lower() not in cta_lines and not CTA_LIKE.search(h["text"])]
    texts += [headline(x) for x in brief.get("headers", [])]
    texts = list(dict.fromkeys(t for t in texts if t)) or [headline(first_line) or "Watch this"]
    by_line = {}
    for x in rows:
        by_line[clean(x["line"]).lower()[:40]] = x["i"]
    alt_hooks = []
    for h in hooks[1:]:
        if h.get("source") == "footage" and not CTA_LIKE.search(h["text"]):
            i = by_line.get(clean(h["text"]).lower()[:40])
            if i is not None and i != rows[0]["i"] and not any(x["i"] == i and x["role"] == "cta" for x in rows):
                alt_hooks.append((i, h.get("rank")))
    hook_opts = [("original", None)] + [(f"hook#{rk}-first", i) for i, rk in alt_hooks[:3]]
    lo, hi = speeds
    sp = sorted({round(lo + (hi - lo) * k / 4, 2) for k in range(5)})
    reel_axes = list(itertools.product(hook_opts, ["intro", "persistent", "none"], ["full", "short", "micro"], sp, list(PACKS), [False, True]))
    rng.shuffle(reel_axes)
    stills = [] if reels_only else ["carousel-text", "carousel-image", "single-quote", "single-poster"]
    n_stills = min(len(stills), max(0, n // 4))
    chosen = []

    def dist(a, b):
        return sum(1 for x, y in zip(a, b) if x != y)
    for cand in reel_axes:
        if len(chosen) >= n - n_stills:
            break
        key = (cand[0][0], cand[1], cand[2], cand[3], cand[4], cand[5])
        if all(dist(key, c) >= 3 for c in chosen):
            chosen.append(key)
    for cand in reel_axes:  # few hook options: relax to >= 2 differing axes
        if len(chosen) >= n - n_stills:
            break
        key = (cand[0][0], cand[1], cand[2], cand[3], cand[4], cand[5])
        if key not in chosen and all(dist(key, c) >= 2 for c in chosen):
            chosen.append(key)
    out = []
    for k, (hk, hdr, dur, s, cap, swp) in enumerate(chosen):
        hi_ = dict(hook_opts)[hk]
        out.append({"id": f"V{k + 1:02d}", "format": "reel", "hook": hk, "hook_i": hi_, "header": hdr, "header_text": texts[k % len(texts)],
                    "duration": dur, "speed": s, "captions": cap, "swap": swp, "punch": round(1 + 0.015 * (k % 4), 3),
                    "shift": [0, 0.04, -0.04, 0.02][k % 4], "sat": [0, 0.04, -0.03, 0.02][k % 4], "rng": random.Random(seed + k)})
    for j, fmt in enumerate(stills[:n_stills]):
        out.append({"id": f"V{len(out) + 1:02d}", "format": fmt, "hook": "header", "hook_i": None, "header": "-", "header_text": texts[(j + 1) % len(texts)],
                    "duration": "-", "speed": "-", "captions": "-", "swap": False, "punch": "-", "shift": 0, "sat": 0, "rng": random.Random(seed + 100 + j)})
    return out


def compliance_hits(strings, base, brand):
    from .qc import FORBID_HEALTH
    words = list((base["style"].get("compliance") or {}).get("forbid_words", []))
    bf = REPO / "brands" / f"{brand}.md"
    if bf.exists() and re.search(r"health|clinic|physio|medical", bf.read_text(encoding="utf-8"), re.I):
        words += FORBID_HEALTH
    low = " " + " ".join(strings).lower() + " "
    return sorted({w for w in words if re.search(r"(?<![\w])" + re.escape(w.lower()) + r"(?![\w])", low)})


def expand(edit_dir, count=12, version=None, quality="draft", speeds=(1.0, 1.4), reels_only=False, aspects=None, seed=7, render_files=True):
    from .render import canvas, render
    base = load(edit_dir, version)
    if quality == "final" and not base.get("approved"):
        raise SystemExit(f"v{base['version']} is not approved: expand drafts first, or approve the base edit before final variants.")
    brief = rjson(edit_dir / "brief.json", {})
    clips = {c["id"]: c for c in load_clips(edit_dir)}
    rows = beat_table(base, brief, clips)
    master = (aspects or [base["outputs"][0]["aspect"]])
    matrix = build_matrix(count, rows, brief, base, speeds, reels_only, seed)
    run_dir = edit_dir / "variants" / f"v{base['version']}"
    if run_dir.exists():
        shutil.rmtree(run_dir)
    tmp = run_dir / "_frames"; tmp.mkdir(parents=True)
    res = []
    for v in matrix:
        v["aspects"] = master
        if v["format"] == "reel":
            r, order = reel_recipe(base, rows, v, brief, None)
            r["approved"] = base.get("approved")
            vd = run_dir / v["id"]
            wjson(vd / "edit.json", r)
            _, total = item_starts(r)
            files = []
            if render_files:
                _, out = render(edit_dir, quality=quality, recipe=r, out_dir=vd, name=f"{v['id']}")
                files = [x["path"] for x in out]
                total = out[0]["duration"]
            from .render import caption_words
            strings = [t["text"] for t in r["texts"]] + [" ".join(w["w"] for w in caption_words(r, clips))]
            res.append({**{k: v[k] for k in ("id", "format", "hook", "header", "header_text", "duration", "speed", "captions", "swap", "punch")},
                        "beats": [x["i"] for x in order], "seconds": round(total, 1), "files": files, "compliance": compliance_hits(strings, base, base.get("brand"))})
        else:
            W, H = (540, 675) if quality == "draft" else (1080, 1350)
            if v["format"].startswith("single") and v["format"].endswith("poster"):
                W, H = (540, 960) if quality == "draft" else (1080, 1920)
            files, strings = stills_variant(base, rows, v, brief, clips, run_dir / v["id"], W, H, tmp) if render_files else ([], [])
            res.append({**{k: v[k] for k in ("id", "format", "hook", "header", "header_text", "duration", "speed", "captions", "swap", "punch")},
                        "beats": [], "seconds": "-", "files": files, "compliance": compliance_hits(strings, base, base.get("brand"))})
        log(f"{v['id']} {v['format']:15} {v['hook']:11} hdr={v['header']:10} {v['duration']:5} x{v['speed']} {v['captions']}")
    shutil.rmtree(tmp, ignore_errors=True)
    wjson(run_dir / "variants.json", {"base_version": base["version"], "quality": quality, "variants": res})
    L = [f"# Variants of v{base['version']} ({quality})", "",
         "| id | format | hook | header | header text | length | speed | captions | reordered | s | compliance | file |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for x in res:
        f = Path(x["files"][0]).relative_to(edit_dir) if x["files"] else "-"
        L.append(f"| {x['id']} | {x['format']} | {x['hook']} | {x['header']} | {x['header_text']} | {x['duration']} | {x['speed']} | {x['captions']} | "
                 f"{'yes' if x['swap'] else 'no'} | {x['seconds']} | {', '.join(x['compliance']) or 'ok'} | `{f}`{' +' + str(len(x['files']) - 1) if len(x['files']) > 1 else ''} |")
    L += ["", "How to use: post one variant per slot as an IG Trial Reel / TikTok test with its own caption (run /publish per variant), keep the "
          "winner's hook + header + caption style, and log the result with /review → /learn. Change one thing you can learn from per test.",
          "Note: platforms fingerprint audio and video, so speed or crop tweaks alone don't make a repost 'new'; the hook, structure and format "
          "changes are what earn a fresh test. Never post the same variant from several accounts."]
    (run_dir / "VARIANTS.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    log(f"{len(res)} variants -> {run_dir / 'VARIANTS.md'}")
    return run_dir, res


def cmd_expand(a, edit_dir):
    lo, hi = (float(x) for x in a.speeds.split(","))
    expand(edit_dir, a.count, a.version, "final" if a.final else "draft", (lo, hi), a.reels_only, a.aspects.split(",") if a.aspects else None, a.seed)
