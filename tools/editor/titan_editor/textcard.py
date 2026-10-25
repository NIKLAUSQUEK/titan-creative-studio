"""On-screen text as transparent PNG cards (Pillow), for what libass can't do: colour emoji/flags and rounded caption boxes.

Styles (from Klaus's reference reels, 2026-10):
  outline : Gen Z header. Bold white, heavy black outline, emoji inline. e.g. "🇵🇰\\nNAHHH BRO 😭💀" at the top.
  box     : TikTok classic. Each line in its own white rounded box, black text. e.g. "My name is …" / "but they call me…".
  label   : one centred word per montage clip ("Jessie", "Willow"), white with soft shadow.
  kicker  : news/expose. Coloured bar with a short tag ("⚠️ SCAM ALERT") above a headline.
Cards are overlaid only for their own window (ledger 2026-10-10: windowed overlays, never full-length loops).
"""
import os, re, sys, urllib.request
from pathlib import Path

from .common import TOOL, log

EMOJI = re.compile("(" + "|".join([
    r"[\U0001F1E6-\U0001F1FF]{2}",                                  # flags
    r"[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF](?:\uFE0F)?(?:\u200D[\U0001F300-\U0001FAFF\u2600-\u27BF](?:\uFE0F)?)*(?:[\U0001F3FB-\U0001F3FF])?",
]) + ")")
NOTO_URL = "https://github.com/googlefonts/noto-emoji/raw/main/fonts/NotoColorEmoji.ttf"
_EF = {}


def emoji_font():
    if "f" in _EF:
        return _EF["f"]
    from PIL import ImageFont
    cands = [(r"C:\Windows\Fonts\seguiemj.ttf", 109), ("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109),
             ("/System/Library/Fonts/Apple Color Emoji.ttc", 160)]
    local = Path(os.environ.get("LOCALAPPDATA") or Path.home() / ".titan-editor") / "TitanEditor" / "NotoColorEmoji.ttf"
    cands.append((str(local), 109))
    for path, size in cands:
        if Path(path).exists():
            try:
                _EF["f"] = (ImageFont.truetype(path, size), size); return _EF["f"]
            except Exception:
                continue
    try:
        local.parent.mkdir(parents=True, exist_ok=True)
        log("downloading Noto Color Emoji (one-time, OFL licence)")
        urllib.request.urlretrieve(NOTO_URL, local)
        _EF["f"] = (ImageFont.truetype(str(local), 109), 109)
    except Exception as e:
        log(f"no colour emoji font ({str(e)[:80]}); emoji will be dropped from cards")
        _EF["f"] = None
    return _EF["f"]


def text_font(name, px, bold=True):
    from PIL import ImageFont
    files = []
    if name and Path(name).suffix.lower() in (".ttf", ".otf"):
        files.append(name)
    fam = (name or "DejaVu Sans").lower()
    key = fam.replace(" italic", "").replace(" ", "")
    bundled = sorted((TOOL / "fonts").glob("*.ttf"))       # the style font pack (OFL/Apache, see fonts/FONTS.md)
    own = [f for f in bundled if f.stem.lower().replace("-", "").startswith(key)]
    if own:
        pref = ("extrabold", "bold") if bold else ("regular", "")
        own.sort(key=lambda f: (("italic" in f.stem.lower()) != ("italic" in fam), next((i for i, w in enumerate(pref) if w and w in f.stem.lower()), len(pref))))
        files.append(own[0])
    if "serif" in fam and "sans" not in fam:
        files.append(TOOL / "fonts" / "DejaVuSerif.ttf")
    files += [TOOL / "fonts" / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")]
    if sys.platform == "win32" and name:
        files.insert(0, Path(r"C:\Windows\Fonts") / (name.replace(" ", "") + ("bd.ttf" if bold else ".ttf")))
    for f in files:
        try:
            return ImageFont.truetype(str(f), int(px))
        except Exception:
            continue
    return ImageFont.load_default()


def runs(line):
    out, pos = [], 0
    for m in EMOJI.finditer(line):
        if m.start() > pos:
            out.append(("t", line[pos:m.start()]))
        out.append(("e", m.group(0)))
        pos = m.end()
    if pos < len(line):
        out.append(("t", line[pos:]))
    return out


def draw_line(line, font, px, fill, stroke, stroke_fill):
    """Render one line (text + emoji runs) to a tight RGBA image."""
    from PIL import Image, ImageDraw
    parts = []
    ef = emoji_font()
    for kind, s in runs(line):
        if kind == "t":
            if not s:
                continue
            d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
            l, t, r, b = d.textbbox((0, 0), s, font=font, stroke_width=stroke)
            im = Image.new("RGBA", (max(1, r - l), int(px * 1.35)), (0, 0, 0, 0))
            ImageDraw.Draw(im).text((-l, int(px * 0.12)), s, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
            parts.append(im)
        elif ef:
            f, size = ef
            im = Image.new("RGBA", (int(size * 1.4 * max(1, len(s) // 2)), int(size * 1.3)), (0, 0, 0, 0))
            ImageDraw.Draw(im).text((0, 0), s, font=f, embedded_color=True)
            bb = im.getbbox()
            if bb:
                im = im.crop(bb)
                h = int(px * 1.05)
                im = im.resize((max(1, int(im.width * h / im.height)), h))
                pad = Image.new("RGBA", (im.width + int(px * 0.15), int(px * 1.35)), (0, 0, 0, 0))
                pad.alpha_composite(im, (int(px * 0.075), int(px * 0.12)))
                parts.append(pad)
    if not parts:
        return None
    W = sum(p.width for p in parts)
    out = Image.new("RGBA", (W, int(px * 1.35)), (0, 0, 0, 0))
    x = 0
    for p in parts:
        out.alpha_composite(p, (x, 0)); x += p.width
    return out


def wrap_lines(text, font, max_w):
    from PIL import Image, ImageDraw
    d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    lines = []
    for para in str(text).split("\n"):
        cur = ""
        for w in para.split():
            t = (cur + " " + w).strip()
            n_emoji = len(EMOJI.findall(t))
            width = d.textlength(EMOJI.sub("", t), font=font) + n_emoji * font.size * 1.2  # emoji drawn ~1.05 em + padding
            if width <= max_w or not cur:
                cur = t
            else:
                lines.append(cur); cur = w
        lines.append(cur)
    return [l for l in lines if l is not None]


def card(text, W, H, style="outline", y=0.18, size=0.05, font=None, color="#FFFFFF", box="#FFFFFF", box_text="#111111",
         accent="#E53935", uppercase=False, out=None):
    """Full-frame transparent PNG with the text block centred at height y (fraction). size = fraction of 9:16 height."""
    from PIL import Image, ImageDraw, ImageFilter
    U = 1920 * min(W, H) / 1080 * (0.75 if W > H else 1.0)
    px = max(10, int(size * U))
    txt = text.upper() if uppercase else text
    f = text_font(font, px, True)
    lines = wrap_lines(txt, f, W * (0.86 if style != "box" else 0.80))
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    stroke = max(2, px // 9) if style == "outline" else 0
    imgs = [draw_line(l, f, px, color if style != "box" else box_text, stroke, "#000000") for l in lines]
    imgs = [i for i in imgs if i]
    gap = int(px * (0.35 if style == "box" else 0.05))
    blocks = []
    for im in imgs:
        if style == "box":
            padx, pady = int(px * 0.45), int(px * 0.12)
            b = Image.new("RGBA", (im.width + 2 * padx, im.height + 2 * pady), (0, 0, 0, 0))
            ImageDraw.Draw(b).rounded_rectangle([0, 0, b.width - 1, b.height - 1], radius=int(px * 0.35), fill=box)
            b.alpha_composite(im, (padx, pady)); blocks.append(b)
        elif style == "kicker" and not blocks:
            padx = int(px * 0.4)
            b = Image.new("RGBA", (im.width + 2 * padx, im.height), (0, 0, 0, 0))
            ImageDraw.Draw(b).rectangle([0, 0, b.width, b.height], fill=accent)
            b.alpha_composite(im, (padx, 0)); blocks.append(b)
        else:
            blocks.append(im)
    total = sum(b.height for b in blocks) + gap * (len(blocks) - 1)
    yy = int(H * y - total / 2)
    if style == "label":  # soft shadow
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        y2 = yy
        for b in blocks:
            mask = Image.new("RGBA", b.size, (0, 0, 0, 160)); mask.putalpha(b.getchannel("A").point(lambda a: int(a * 0.6)))
            sh.alpha_composite(mask, ((W - b.width) // 2 + px // 20, y2 + px // 20)); y2 += b.height + gap
        canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(px // 10)))
    for b in blocks:
        canvas.alpha_composite(b, ((W - b.width) // 2, max(0, yy))); yy += b.height + gap
    if out:
        canvas.save(out)
    return canvas


def needs_card(t, st):
    """Use a PNG card when the text has emoji, or the style asks for a card look libass can't draw."""
    ht = st.get("hook_text", {})
    return bool(EMOJI.search(t.get("text", ""))) or t.get("style") in ("box", "label", "kicker", "outline") or \
        (t["type"] in ("hook", "header", "title") and ht.get("renderer") == "card")
