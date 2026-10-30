"""Deterministic renderer: edit.vN.json -> mp4 per aspect, with ffmpeg only (libass for animated captions/titles).

Draft = lowest quality (short edge 360 px, crf 30, ultrafast) per studio rule. Final = 1080 short edge, crf 17, slow; only for an approved version.
Segments are cached by content hash, so a revision re-renders only the items it changed.
"""
import hashlib, json, re, shutil
from pathlib import Path

from .common import REPO, TOOL, ffmpeg, log, probe, rjson, studio, wjson
from .ingest import load_clips
from .recipe import at_of, item_starts, load

FPS = 30
CANVAS = {"9:16": (1080, 1920), "1:1": (1080, 1080), "16:9": (1920, 1080), "4:5": (1080, 1350), "2.39:1": (1920, 804)}
STOP = set("the a an and or but so to of in on at for with is are was it this that i you we my your me be just do not".split())
SFX_SYNTH = {
    "whoosh": "anoisesrc=d=0.45:c=pink:a=0.7,highpass=f=400,lowpass=f=5000,afade=t=in:d=0.28:curve=exp,afade=t=out:st=0.28:d=0.17",
    "impact": "aevalsrc='0.95*sin(2*PI*(70-45*t)*t)*exp(-4.5*t)+0.25*(random(0)-0.5)*exp(-30*t)':d=0.9",
    "pop": "aevalsrc='0.8*sin(2*PI*880*t)*exp(-35*t)':d=0.16",
    "ding": "aevalsrc='0.45*sin(2*PI*1320*t)*exp(-5*t)+0.25*sin(2*PI*2640*t)*exp(-7*t)':d=1.0",
    "riser": "aevalsrc='0.35*sin(2*PI*(180+500*t*t)*t)*(t/1.6)':d=1.6,afade=t=out:st=1.5:d=0.1",
    "click": "aevalsrc='0.7*sin(2*PI*2000*t)*exp(-120*t)':d=0.05",
    "bass": "aevalsrc='0.95*sin(2*PI*(55-25*t)*t)*exp(-2.2*t)':d=1.2",
    "sting": "aevalsrc='0.5*(sin(2*PI*311*t)+sin(2*PI*329.6*t)+sin(2*PI*466*t))*exp(-1.8*t)*min(1,t*40)':d=1.6",
    "scratch": "aevalsrc='0.6*sin(2*PI*(900-1700*t)*t)*(1-t/0.35)':d=0.35",
    "swell": "anoisesrc=d=0.9:c=white:a=0.6,highpass=f=2500,afade=t=in:d=0.85:curve=exp,afade=t=out:st=0.86:d=0.04",
    "boom": "aevalsrc='0.95*sin(2*PI*(48-20*t)*t)*exp(-1.6*t)':d=1.8",
    "tick": "aevalsrc='0.6*sin(2*PI*3200*t)*exp(-260*t)+0.2*(random(0)-0.5)*exp(-400*t)':d=0.04",
    "glitch": "aevalsrc='0.5*sin(2*PI*(400+3000*floor(mod(t*40,4)))*t)*lt(mod(t*25,1),0.6)':d=0.3",
    "paper": "anoisesrc=d=0.12:c=pink:a=0.8,bandpass=f=2500:w=2000,afade=t=out:st=0.02:d=0.1",
    "drone": "aevalsrc='0.35*sin(2*PI*48*t)+0.2*sin(2*PI*72.3*t)*(0.6+0.4*sin(2*PI*0.2*t)):d=90",
}


def canvas(aspect, quality):
    W, H = CANVAS[aspect]
    if quality == "draft":
        k = 360 / min(W, H)
        W, H = int(W * k) // 2 * 2, int(H * k) // 2 * 2
    return W, H


def ass_color(hexv, alpha=0.0):
    h = (hexv or "#FFFFFF").lstrip("#")
    return f"&H{int(alpha * 255):02X}{h[4:6]}{h[2:4]}{h[0:2]}".upper()


def grade_filter(g, lut_name=None):
    f = []
    c, s, b, gm = g.get("contrast", 1), g.get("saturation", 1), g.get("brightness", 0), g.get("gamma", 1)
    if (c, s, b, gm) != (1, 1, 0, 1):
        f.append(f"eq=contrast={c}:saturation={s}:brightness={b}:gamma={gm}")
    w = g.get("warmth", 0) or 0
    if w:
        f.append(f"colorbalance=rm={w:.3f}:bm={-w:.3f}:rh={w / 2:.3f}:bh={-w / 2:.3f}")
    tt = g.get("teal", 0) or 0          # horror/thriller: cold teal shadows, slightly green mids
    if tt:
        f.append(f"colorbalance=rs={-tt:.3f}:gs={tt * 0.4:.3f}:bs={tt:.3f}:gm={tt * 0.3:.3f}")
    if lut_name:
        f.append(f"lut3d={lut_name}")
    if g.get("vignette"):
        f.append("vignette=PI/5")
    return f


def fit_filter(src_w, src_h, W, H, fit="auto", fx=0.5, fy=0.4):
    sr, cr = (src_w or W) / (src_h or H), W / H
    if fit == "auto":
        fit = "blur" if sr < cr / 1.5 else "cover"
    if fit == "blur":
        return (f"split[fa][fb];[fa]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=20:2[bg];"
                f"[fb]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2")
    return f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}:(in_w-{W})*{fx}:(in_h-{H})*{fy}"


def zoom_chain(keys, d, W, H):
    """Return list of (t0, t1, filter) sub-ranges for snap zooms, or one smooth push."""
    keys = sorted(keys or [{"at": 0, "scale": 1.0}], key=lambda k: k["at"])
    if keys[0]["at"] > 0:
        keys = [{"at": 0, "scale": 1.0}] + keys
    if len(keys) == 2 and keys[1].get("ease") == "drift":   # premium virtual camera: eased push + slow pan on overscanned footage
        s0, s1 = keys[0]["scale"], keys[1]["scale"]
        x0, x1 = keys[0].get("x", 0.5), keys[1].get("x", 0.5)
        y0 = keys[0].get("y", 0.38)
        P = f"(min(1,t/{max(d, 0.1):.3f})*min(1,t/{max(d, 0.1):.3f})*(3-2*min(1,t/{max(d, 0.1):.3f})))"   # smoothstep ease-in-out
        return [(0, d, f"scale=w='trunc({W}*({s0}+({s1}-{s0})*{P})/2)*2':h=-2:eval=frame,"
                       f"crop={W}:{H}:'(in_w-{W})*({x0}+({x1}-{x0})*{P})':'(in_h-{H})*{y0}',setsar=1")]
    if len(keys) == 2 and keys[1].get("ease") == "linear":
        s0, s1 = keys[0]["scale"], keys[1]["scale"]
        expr = f"{s0}+({s1}-{s0})*t/{max(d, 0.1):.3f}"
        return [(0, d, f"scale=w='trunc({W}*({expr})/2)*2':h=-2:eval=frame,crop={W}:{H}:(in_w-{W})/2:(in_h-{H})*0.4,setsar=1")]
    out = []
    for i, k in enumerate(keys):
        t0, t1 = k["at"], keys[i + 1]["at"] if i + 1 < len(keys) else d
        if t1 - t0 < 0.02:
            continue
        s = k["scale"]
        f = "setsar=1" if abs(s - 1) < 1e-3 else f"scale={int(W * s) // 2 * 2}:-2,crop={W}:{H}:(in_w-{W})/2:(in_h-{H})*0.35,setsar=1"
        out.append((t0, min(t1, d), f))
    return out or [(0, d, "null")]


def h(obj):
    return hashlib.sha1(json.dumps(obj, sort_keys=True).encode()).hexdigest()[:14]


def voice_key(meta):
    ap = meta.get("audio_path")
    return f"{ap}|{Path(ap).stat().st_mtime}" if ap and Path(ap).exists() else None


def render_item(it, clip, W, H, q, style, cache, lut):
    src, meta = clip["meta"]["path"], clip["meta"]
    sp = it.get("speed", 1.0)
    d = (it["out"] - it["in"]) / sp
    key = h({"src": src, "in": it["in"], "out": it["out"], "sp": sp, "z": it.get("zoom"), "fx": it.get("focus_x"), "fit": it.get("fit"),
             "W": W, "H": H, "q": q, "g": style.get("grade"), "fx": it.get("fx"), "voice": voice_key(meta), "v": 4})
    out = cache / f"seg_{key}.mkv"
    if out.exists():
        return out, d
    fit = fit_filter(meta.get("width"), meta.get("height"), W, H, it.get("fit", "auto"), it.get("focus_x", 0.5))
    fx = ["eq=brightness='-0.55*lt(t,0.45)*gt(mod(t*14,2),1)':eval=frame"] if "flicker" in (it.get("fx") or []) else []  # bulb flicker in
    pre = ",".join([f"setpts=(PTS-STARTPTS)/{sp}" if sp != 1 else "setpts=PTS-STARTPTS"] + grade_filter(style.get("grade", {}), lut) + fx + [f"fps={FPS}", "format=yuv420p", "setsar=1"])
    parts = zoom_chain(it.get("zoom"), d, W, H)
    fc = f"[0:v]{fit}[fit];[fit]{pre}[g]"
    if len(parts) == 1:
        fc += f";[g]{parts[0][2]}[v]"
    else:
        fc += f";[g]split={len(parts)}" + "".join(f"[s{i}]" for i in range(len(parts)))
        for i, (t0, t1, f) in enumerate(parts):
            fc += f";[s{i}]trim={t0:.3f}:{t1:.3f},setpts=PTS-STARTPTS,{f}[z{i}]"
        fc += ";" + "".join(f"[z{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[v]"
    args = ["-ss", f"{it['in']:.3f}", "-t", f"{it['out'] - it['in']:.3f}", "-i", src]
    ap = meta.get("audio_path")
    if ap and Path(ap).exists():                      # enhanced voice (enhance.py), sample-aligned to the clip
        args += ["-ss", f"{it['in']:.3f}", "-t", f"{it['out'] - it['in']:.3f}", "-i", ap]
    if meta.get("has_audio"):
        at = f"atempo={sp}," if sp != 1 else ""
        fc += f";[{1 if ap and Path(ap).exists() else 0}:a]{at}aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.012,afade=t=out:st={max(0, d - 0.015):.3f}:d=0.015[a]"
    else:
        args += ["-f", "lavfi", "-t", f"{d:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
        fc += ";[1:a]anull[a]"
    ffmpeg(args + ["-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", f"{d:.3f}"] + venc(q) + ["-c:a", "pcm_s16le", out], cwd=cache)
    return out, d


def venc(q):
    return ["-c:v", "libx264", "-preset", "ultrafast" if q == "draft" else "slow", "-crf", "30" if q == "draft" else "17", "-pix_fmt", "yuv420p", "-r", str(FPS)]


def render_broll(b, W, H, q, style, cache, lut):
    pip = b.get("mode") == "pip"
    w, hh = (int(W * 0.42) // 2 * 2, int(H * 0.42) // 2 * 2) if pip else (W, H // 2 // 2 * 2) if b.get("mode") == "split" else (W // 2 // 2 * 2, H) if b.get("mode") == "side" else (W, H)
    key = h({"p": b.get("path") or json.dumps([b.get("template"), b.get("data")], sort_keys=True), "in": b.get("src_in", 0), "d": b["dur"], "W": w, "H": hh, "q": q, "g": style.get("grade"), "v": 3})
    out = cache / f"broll_{key}.mkv"
    if out.exists():
        return out
    if b.get("kind") == "motion":                      # code-made card (tools/motion), rendered at the window size
        from .motion import cached
        b = dict(b, path=str(cached(b, w, hh, FPS, cache)), src_in=0.0)
    if b.get("kind") == "image":
        args = ["-loop", "1", "-framerate", str(FPS), "-t", f"{b['dur']:.3f}", "-i", b["path"]]
        kb = f",zoompan=z='1+0.06*on/{int(b['dur'] * FPS)}':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={w}x{hh}:fps={FPS}"  # slow Ken Burns
        fit = f"scale={w * 2}:{hh * 2}:force_original_aspect_ratio=increase,crop={w * 2}:{hh * 2}" + kb
    else:
        m = probe(b["path"])
        args = ["-ss", f"{b['src_in']:.3f}", "-t", f"{b['dur']:.3f}", "-i", b["path"]]
        fit = fit_filter(m.get("width"), m.get("height"), w, hh, "cover")
    chain = ",".join(["setpts=PTS-STARTPTS"] + grade_filter(style.get("grade", {}), lut) + [f"fps={FPS}", "format=yuv420p", "setsar=1"])
    ffmpeg(args + ["-filter_complex", f"[0:v]{fit}[f];[f]{chain}[v]", "-map", "[v]", "-an", "-t", f"{b['dur']:.3f}"] + venc(q) + [out], cwd=cache)
    return out


def end_card_seg(r, W, H, q, cache):
    ec = r["end_card"]
    bg = (r["style"].get("end_card", {}).get("bg") or r["style"].get("colors", {}).get("primary") or "#000000")
    key = h({"ec": ec.get("dur"), "bg": bg, "W": W, "H": H, "q": q})
    out = cache / f"end_{key}.mkv"
    if not out.exists():
        ffmpeg(["-f", "lavfi", "-t", f"{ec['dur']:.3f}", "-i", f"color=c=0x{bg.lstrip('#')}:s={W}x{H}:r={FPS}", "-f", "lavfi", "-t", f"{ec['dur']:.3f}",
                "-i", "anullsrc=r=48000:cl=stereo", "-map", "0:v", "-map", "1:a"] + venc(q) + ["-c:a", "pcm_s16le", out], cwd=cache)
    return out


def sfx_file(kind, cache):
    """The built-in synthesised take (last resort; sfx.pick prefers real library recordings, then Earshot)."""
    out = cache / f"sfx_{kind}.wav"
    if not out.exists():
        ffmpeg(["-f", "lavfi", "-i", SFX_SYNTH.get(kind, SFX_SYNTH["whoosh"]), "-ar", "48000", "-ac", "2", out], cwd=cache)
    return out


# ---------------- captions + text (ASS) ----------------
def ass_escape(t):
    return str(t).replace("{", "(").replace("}", ")").replace("\n", "\\N")


def caption_words(r, clips):
    starts, _ = item_starts(r)
    rep = {k.lower(): v for k, v in (r["captions"].get("replace") or {}).items()}
    hide = list(r["captions"].get("hide") or [])
    for c in r.get("chats", []):                  # the chat card is the text; no subtitles on top (ref: MUSK doc reel)
        a = at_of(r, c["anchor"], starts)
        if a is not None and c.get("captions", "hide") == "hide":
            hide.append((a, a + float(c.get("dur") or 6)))
    out = []
    for it in r["items"]:
        sp = it.get("speed", 1)
        for w in clips[it["clip"]]["words"]:
            if w["t1"] <= it["in"] + 0.02 or w["t0"] >= it["out"] - 0.02 or w.get("filler") == "hard":
                continue
            t0 = starts[it["id"]] + (max(w["t0"], it["in"]) - it["in"]) / sp
            t1 = starts[it["id"]] + (min(w["t1"], it["out"]) - it["in"]) / sp
            if any(a <= t0 < b for a, b in hide):
                continue
            txt = rep.get(re.sub(r"[^\w']", "", w["w"].lower()), w["w"])
            out.append({"w": txt, "t0": t0, "t1": t1})
    return out


def group_words(words, max_words):
    groups, cur = [], []
    for w in words:
        if cur and (len(cur) >= max_words or w["t0"] - cur[-1]["t1"] > 0.45 or re.search(r"[.?!,]$", cur[-1]["w"])):
            groups.append(cur); cur = []
        cur.append(w)
    if cur:
        groups.append(cur)
    return groups


def pick_emphasis(g, explicit):
    ex = {e.lower() for e in explicit}
    for i, w in enumerate(g):
        if re.sub(r"[^\w']", "", w["w"].lower()) in ex:
            return i
    cands = [(len(re.sub(r"\W", "", w["w"])), i) for i, w in enumerate(g)
             if re.sub(r"[^\w']", "", w["w"].lower()) not in STOP and (len(w["w"]) >= 5 or re.search(r"\d", w["w"]))]
    return max(cands)[1] if cands and (len(g) > 1 or cands[0][0] >= 6) else None


def ass_style(name, font, px, color, outline_px, outline_color="#000000", bold=True, align=5, back="#000000", back_alpha=1.0, border_style=1, shadow=0):
    italic = str(font).lower().endswith(" italic")
    font = font[:-7] if italic else font                 # "Instrument Serif Italic" -> family + Italic flag (libass matches families)
    return (f"Style: {name},{font},{int(px)},{ass_color(color)},{ass_color(color)},{ass_color(outline_color)},{ass_color(back, back_alpha)},"
            f"{-1 if bold else 0},{-1 if italic else 0},0,0,100,100,0,0,{border_style},{outline_px},{shadow},{align},40,40,40,1")


def t_ass(t):
    t = max(0, t)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def build_ass(r, clips, W, H, total, path):
    st = r["style"]
    c, ht, lt = st["captions"], st["hook_text"], st.get("lower_third", {})
    k = min(W, H) / 1080 * (0.75 if W > H else 1.0)  # sizes are fractions of a 9:16 frame height (1920 at 1080 wide)
    U = 1920 * k
    cap_px = c["size"] * U
    styles = [ass_style("Cap", c.get("font", "DejaVu Sans"), cap_px, c.get("color", "#FFFFFF"), max(1, round(c.get("outline", 4) * k)), c.get("outline_color", "#000000"), c.get("bold", True)),
              ass_style("Hook", ht.get("font", "DejaVu Sans"), ht.get("size", 0.05) * U, ht.get("color", "#FFFFFF"), max(1, round(ht.get("outline", 6) * k)), "#000000", ht.get("bold", True)),
              ass_style("Lower", lt.get("font", "DejaVu Sans"), lt.get("size", 0.028) * U, lt.get("color", "#FFFFFF"), max(2, round(10 * k)), lt.get("box", "#000000"),
                        True, 1, lt.get("box", "#000000"), 1 - lt.get("box_alpha", 0.55), 3)]
    glow = c.get("glow", c.get("highlight", "#FFE14D"))
    styles += [ass_style("Small", c.get("small_font", c.get("font", "DejaVu Sans")), cap_px * c.get("small_scale", 0.5), c.get("small_color", "#E8E8E8"),
                         max(1, round(2 * k)), "#000000", False),
               ass_style("Key", c.get("key_font", c.get("font", "DejaVu Sans")), cap_px * c.get("key_scale", 1.55), c.get("highlight", "#FFE14D"),
                         max(1, round(2 * k)), glow, True),
               ass_style("KeyGlow", c.get("key_font", c.get("font", "DejaVu Sans")), cap_px * c.get("key_scale", 1.55), glow,
                         max(2, round(12 * k)), glow, True)]
    fonts = st.get("fonts", {})
    ec = st.get("end_card", {})
    styles.append(ass_style("EndTitle", ec.get("font") or fonts.get("display") or "DejaVu Sans", ec.get("title_size", 0.05) * U, ec.get("color") or st.get("colors", {}).get("text") or "#FFFFFF", 0, bold=False))
    styles.append(ass_style("EndSub", ec.get("sub_font") or fonts.get("body") or "DejaVu Sans", ec.get("sub_size", 0.03) * U, ec.get("sub_color") or ec.get("color") or "#FFFFFF", 0, bold=False))
    ev = []
    cx = W // 2
    starts, body = item_starts(r)
    if r["captions"].get("enabled", True) and c.get("enabled", True):
        y = int(H * c.get("position_y", 0.7))
        hl = ass_color(c.get("highlight", "#FFE14D"))
        base = ass_color(c.get("color", "#FFFFFF"))
        groups = group_words(caption_words(r, clips), max(1, int(c.get("max_words", 3))))
        for gi, g in enumerate(groups):
            t0 = g[0]["t0"]
            nxt = groups[gi + 1][0]["t0"] if gi + 1 < len(groups) else body
            t1 = max(g[-1]["t1"], t0 + 0.3)
            t1 = nxt if nxt - t1 < 0.35 else t1
            emph = pick_emphasis(g, r["captions"].get("emphasis") or []) if c.get("keyword_caps", True) or r["captions"].get("emphasis") else None

            def word(i, w, active=False):
                s = w["w"].upper() if c.get("uppercase") or (i == emph and c.get("keyword_caps", True)) else w["w"]
                s = ass_escape(s)
                return f"{{\\c{hl}}}{s}{{\\c{base}}}" if i == emph or active else s
            anim = c.get("animation", "pop")
            if c.get("layout") == "two_level" and len(g) > 0:
                ki = emph if emph is not None else max(range(len(g)), key=lambda i: len(g[i]["w"]))
                small = " ".join(ass_escape(w["w"].lower() if c.get("small_lower", True) else w["w"]) for i, w in enumerate(g) if i != ki)
                kw = g[ki]["w"].strip(".,!?;:\"'")
                key = ass_escape(kw.upper() if c.get("uppercase", True) else kw)
                ys, yk = y - int(cap_px * 0.95), y + int(cap_px * 0.35)
                if small:
                    ev.append(f"Dialogue: 0,{t_ass(t0)},{t_ass(t1)},Small,,0,0,0,,{{\\an5\\pos({cx},{ys})\\fad(90,60)}}{small}")
                ga = g[ki]["t0"] if ki else t0
                ev.append(f"Dialogue: 0,{t_ass(ga)},{t_ass(t1)},KeyGlow,,0,0,0,,{{\\an5\\pos({cx},{yk})\\blur14\\t(0,140,\\blur8)\\fad(60,60)}}{key}")
                ev.append(f"Dialogue: 1,{t_ass(ga)},{t_ass(t1)},Key,,0,0,0,,{{\\an5\\pos({cx},{yk})\\blur10\\t(0,120,\\blur0)\\fscx92\\fscy92\\t(0,120,\\fscx100\\fscy100)\\fad(60,60)}}{key}")
                continue
            if anim == "karaoke":
                for i, w in enumerate(g):
                    a = w["t0"] if i else t0
                    b = g[i + 1]["t0"] if i + 1 < len(g) else t1
                    ev.append(f"Dialogue: 0,{t_ass(a)},{t_ass(b)},Cap,,0,0,0,,{{\\an5\\pos({cx},{y})}}" + " ".join(word(j, x, j == i) for j, x in enumerate(g)))
                continue
            tag = {"pop": "\\fscx82\\fscy82\\t(0,90,\\fscx100\\fscy100)", "fade": "\\fad(110,70)"}.get(anim, "")
            ev.append(f"Dialogue: 0,{t_ass(t0)},{t_ass(t1)},Cap,,0,0,0,,{{\\an5\\pos({cx},{y}){tag}}}" + " ".join(word(i, w) for i, w in enumerate(g)))
    from .textcard import needs_card
    for t in r.get("texts", []):
        if t["type"] == "credit":
            continue  # never drawn (ledger [credits]): older recipes may still carry credit texts; the credit lives in web/ATTRIBUTION.md -> caption
        a = at_of(r, t["anchor"], starts)
        if a is None or needs_card(t, st):
            continue  # emoji / box / label texts are drawn as PNG cards in render()
        b = min(a + float(t.get("dur", 2.5)), body)
        txt = ass_escape(t["text"])
        if t["type"] in ("hook", "title", "header"):
            if t.get("uppercase", ht.get("uppercase", True)):
                txt = txt.upper()
            y = int(H * t.get("position_y", ht.get("position_y", 0.2) if t["type"] in ("hook", "header") else 0.32))
            ev.append(f"Dialogue: 1,{t_ass(a)},{t_ass(b)},Hook,,0,0,0,,{{\\an5\\pos({cx},{y})\\fscx90\\fscy90\\t(0,120,\\fscx100\\fscy100)\\fad(0,120)}}{txt}")
        elif t["type"] == "lower_third":
            ly, cy = lt.get("position_y", 0.8), c.get("position_y", 0.7)
            if abs(ly - cy) < 0.09:  # never sit on the caption band
                ly = cy - 0.09
            y = int(H * ly)
            ev.append(f"Dialogue: 1,{t_ass(a)},{t_ass(b)},Lower,,0,0,0,,{{\\an1\\pos({int(W * 0.06)},{y})\\fad(150,150)}}{txt}")
    ecr = r.get("end_card", {})
    if ecr.get("enabled"):
        lines = ecr.get("lines") or [r.get("brand", "").replace("-", " ").title()]
        a, b = body, total
        y0 = int(H * 0.42)
        for i, ln in enumerate(lines[:3]):
            ev.append(f"Dialogue: 2,{t_ass(a + 0.15 * i)},{t_ass(b)},{'EndTitle' if i == 0 else 'EndSub'},,0,0,0,,{{\\an5\\pos({cx},{y0 + int(i * H * 0.07)})\\fad(250,0)}}{ass_escape(ln)}")
        if ecr.get("cta"):
            ev.append(f"Dialogue: 2,{t_ass(a + 0.4)},{t_ass(b)},EndSub,,0,0,0,,{{\\an5\\pos({cx},{int(H * 0.62)})\\fad(250,0)}}{ass_escape(ecr['cta'])}")
    head = f"[Script Info]\nScriptType: v4.00+\nPlayResX: {W}\nPlayResY: {H}\nWrapStyle: 0\nScaledBorderAndShadow: yes\n\n[V4+ Styles]\n" \
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, " \
           "Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n" + "\n".join(styles) + \
           "\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    Path(path).write_text(head + "\n".join(ev) + "\n", encoding="utf-8")
    return len(ev)


# ---------------- main render ----------------
def music_ok(r):
    m = r["audio"].get("music") or {}
    if not m.get("path"):
        return False, "no music"
    lic = (m.get("licence") or "").lower()
    personal = "personal" in (r.get("brand") or "") or (r.get("account") == "personal")
    if lic.startswith("original") or lic.startswith("licensed"):
        return True, lic
    if lic == "in-app":
        return False, "in-app sound: add it inside TikTok/IG at posting, never baked into the file"
    return (True, "unlicensed, personal account draft only") if personal else (False, "music has no licence (set audio.music.licence to original|licensed:<source>); brand accounts use licensed/original audio only")


def render(edit_dir, version=None, quality="draft", aspects=None, force=False, recipe=None, out_dir=None, name=None):
    """recipe/out_dir/name let the variant expander render recipes that live outside the edit.vN chain."""
    r = recipe or load(edit_dir, version)
    if quality == "final" and not r.get("approved") and not force:
        raise SystemExit(f"v{r['version']} is not approved. Show Klaus the draft, then: editor.py approve --version {r['version']} (studio rule: draft -> approval -> final).")
    clips = {c["id"]: c for c in load_clips(edit_dir)}
    out_dir = Path(out_dir) if out_dir else edit_dir / "renders"
    cache = edit_dir / "renders" / "cache"
    out_dir.mkdir(parents=True, exist_ok=True)
    cache.mkdir(parents=True, exist_ok=True)
    fonts = cache / "fonts"
    fonts.mkdir(exist_ok=True)
    for f in list((TOOL / "fonts").glob("*.[ot]tf")) + list((REPO / "assets" / "fonts").glob(f"{r.get('brand')}/*.[ot]tf")):
        if not (fonts / f.name).exists():
            shutil.copy(f, fonts / f.name)
    lut = None
    if r["style"].get("grade", {}).get("lut"):
        src = Path(r["style"]["grade"]["lut"])
        src = src if src.is_absolute() else REPO / src
        if src.exists():
            lut = src.name; shutil.copy(src, cache / lut)
    results = []
    for o in [o for o in r["outputs"] if not aspects or o["aspect"] in aspects]:
        A = o["aspect"]
        W, H = canvas(A, quality)
        log(f"render v{r['version']} {A} {quality} {W}x{H}")
        segs = [render_item(it, clips[it["clip"]], W, H, quality, r["style"], cache, lut) for it in r["items"]]
        body = sum(d for _, d in segs)
        files = [s for s, _ in segs]
        if r["end_card"].get("enabled"):
            files.append(end_card_seg(r, W, H, quality, cache))
        total = body + (r["end_card"]["dur"] if r["end_card"].get("enabled") else 0)
        tag = f"{name or 'v' + str(r['version'])}_{A.replace(':', 'x')}_{quality}"
        lst = cache / f"{tag}.txt"
        lst.write_text("ffconcat version 1.0\n" + "".join(f"file '{f.name}'\n" for f in files), encoding="utf-8")
        base = cache / f"{tag}_base.mkv"
        ffmpeg(["-f", "concat", "-safe", "0", "-i", lst.name, "-c", "copy", base.name], cwd=cache)
        n_ev = build_ass(r, clips, W, H, total, cache / f"{tag}.ass")
        starts, _ = item_starts(r)
        inputs, fc, last, n = ["-i", base.name], [], "0:v", 1
        for b in r["broll"]:
            a = at_of(r, b["anchor"], starts)
            if a is None or a >= body:
                continue
            d = min(b["dur"], body - a)
            f = render_broll(b, W, H, quality, r["style"], cache, lut)
            inputs += ["-i", f.name]
            fc.append(f"[{n}:v]setpts=PTS-STARTPTS+{a:.3f}/TB[b{n}]")
            win = f"enable='between(t,{a:.3f},{a + d:.3f})'"
            if b.get("mode") == "pip":
                fc.append(f"[{last}][b{n}]overlay=x=W-w-{int(W * 0.04)}:y={int(H * 0.15)}:eof_action=pass:{win}[o{n}]")
            elif b.get("mode") == "split":       # B-roll on top half, speaker's centre band on the bottom half (refs #8, #9)
                hh = H // 2 // 2 * 2
                fc.append(f"[{last}]split[p{n}][q{n}];[q{n}]crop={W}:{hh}:0:{(H - hh) // 2}[c{n}];[p{n}][c{n}]overlay=0:{H - hh}:{win}[s{n}];"
                          f"[s{n}][b{n}]overlay=0:0:eof_action=pass:{win}[o{n}]")
            elif b.get("mode") == "side":        # side-by-side A/B: speaker's centre column left, B-roll (e.g. the AI version) right
                ww = W // 2 // 2 * 2
                fc.append(f"[{last}]split[p{n}][q{n}];[q{n}]crop={ww}:{H}:{(W - ww) // 2}:0[c{n}];[p{n}][c{n}]overlay=0:0:{win}[s{n}];"
                          f"[s{n}][b{n}]overlay={W - ww}:0:eof_action=pass:{win}[o{n}]")
            elif b.get("mode") == "greenscreen":
                fc.append(f"[{last}]split[p{n}][q{n}];[q{n}]colorkey=0x00FF00:0.30:0.10[k{n}];[b{n}][k{n}]overlay=0:0[g{n}];[p{n}][g{n}]overlay=0:0:eof_action=pass:{win}[o{n}]")
            else:
                fc.append(f"[{last}][b{n}]overlay=0:0:eof_action=pass:{win}[o{n}]")
            last, n = f"o{n}", n + 1
        pops = []                                   # texting scenes: full-frame cutaway, a soft pop per message
        for c in r.get("chats", []):
            a = at_of(r, c["anchor"], starts)
            if a is None or a >= body:
                continue
            over = c.get("layout", "overlay") == "overlay"
            key = h({"c": c, "W": W, "H": H, "v": 2})
            f = cache / f"chat_{key}.{'mov' if over else 'mp4'}"
            if not f.exists():
                from .chatanim import render_chat
                render_chat(c, W, H, FPS, f)
            d = min(float(c.get("dur") or 0) or 99, body - a)
            inputs += ["-i", f.name]
            win = f"enable='between(t,{a:.3f},{a + d:.3f})'"
            if over:   # bubbles over the same shot, dimmed + blurred (ledger [edit]: no blank pages)
                fc.append(f"[{last}]split[p{n}][q{n}];[q{n}]gblur=sigma=14,eq=brightness=-0.18:saturation=0.8[d{n}];"
                          f"[p{n}][d{n}]overlay=0:0:{win}[m{n}];[{n}:v]format=rgba,setpts=PTS-STARTPTS+{a:.3f}/TB[b{n}];"
                          f"[m{n}][b{n}]overlay=0:0:eof_action=pass:{win}[o{n}]")
            else:
                fc.append(f"[{n}:v]setpts=PTS-STARTPTS+{a:.3f}/TB[b{n}];[{last}][b{n}]overlay=0:0:eof_action=pass:{win}[o{n}]")
            last, n = f"o{n}", n + 1
            if c.get("sfx", "pop"):
                pops += [(a + float(m["at"]), c.get("sfx", "pop")) for m in c["messages"] if float(m["at"]) < d]
        from .textcard import card, needs_card
        st_ = r["style"]
        for t in r.get("texts", []):
            if not needs_card(t, st_):
                continue
            a = at_of(r, t["anchor"], starts)
            if a is None or a >= body:
                continue
            d = min(float(t.get("dur", 2.5)), body - a)
            ht = st_.get("hook_text", {})
            kind = t.get("style") or ht.get("card_style") or ("outline" if t["type"] in ("hook", "header", "title") else "label")
            y = t.get("position_y", ht.get("position_y", 0.2) if t["type"] in ("hook", "header") else 0.5 if kind == "label" else 0.32)
            size = t.get("size", ht.get("size", 0.05) if kind != "label" else 0.045)
            up = t.get("uppercase", ht.get("uppercase", True) if kind == "outline" else False)
            key = h({"t": t["text"], "k": kind, "y": y, "s": size, "u": up, "W": W, "H": H, "f": ht.get("font"), "c": ht.get("color"), "v": 1})
            png = cache / f"card_{key}.png"
            if not png.exists():
                card(t["text"], W, H, kind, y, size, ht.get("font"), ht.get("color", "#FFFFFF"), ht.get("box", "#FFFFFF"), ht.get("box_text", "#111111"),
                     st_.get("colors", {}).get("accent", "#E53935"), up, out=png)
            inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{d:.3f}", "-i", png.name]
            fc.append(f"[{n}:v]format=rgba,setpts=PTS-STARTPTS+{a:.3f}/TB[k{n}];[{last}][k{n}]overlay=0:0:eof_action=pass[o{n}]")
            last, n = f"o{n}", n + 1
        logo = r["style"].get("logo")
        if logo and logo.get("path"):
            lp = Path(logo["path"]); lp = lp if lp.is_absolute() else REPO / lp
            if lp.exists():
                shutil.copy(lp, cache / ("logo" + lp.suffix))
                lw = int(W * logo.get("size", 0.12))
                pos = {"top-right": f"W-w-{int(W * .04)}:{int(H * .06)}", "top-left": f"{int(W * .04)}:{int(H * .06)}",
                       "bottom-right": f"W-w-{int(W * .04)}:H-h-{int(H * .22)}"}.get(logo.get("position", "top-right"), f"W-w-{int(W * .04)}:{int(H * .06)}")
                inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{body:.3f}", "-i", "logo" + lp.suffix]
                fc.append(f"[{n}:v]scale={lw}:-1,format=rgba,colorchannelmixer=aa={logo.get('opacity', 0.9)}[lg];[{last}][lg]overlay={pos}:eof_action=pass[o{n}]")
                last, n = f"o{n}", n + 1
        tr = r["style"].get("transitions", {}) or {}
        kind = tr.get("default")
        if kind in ("flash", "dip", "glow"):            # brightness pulse on beat changes (or every cut): white flash, dip to black, glow flash
            cuts, prev = [], None
            for it in r["items"]:
                if prev is not None and (tr.get("on") == "cuts" or it.get("beat") != prev.get("beat")):
                    cuts.append(starts[it["id"]])
                prev = it
            cuts = [c for c in cuts if 0.2 < c < body - 0.2][:60]
            if cuts:
                d = float(tr.get("dur_s", 0.12 if kind != "dip" else 0.2))
                amp = {"flash": 0.55, "glow": 0.32, "dip": -0.6}[kind] * float(tr.get("strength", 1.0))
                pulse = "+".join(f"between(t,{c - d / 2:.3f},{c + d / 2:.3f})*(1-abs(t-{c:.3f})/{d / 2:.3f})" for c in cuts)
                sat = f":saturation='1+{0.6 if kind == 'glow' else 0}*({pulse})'" if kind == "glow" else ""
                fc.append(f"[{last}]eq=brightness='{amp}*({pulse})'{sat}:eval=frame[tr]")
                last = "tr"
        fc.append(f"[{last}]ass={tag}.ass:fontsdir=fonts[vout]" if n_ev else f"[{last}]null[vout]")
        # audio: voice + ducked music + sfx -> loudness
        ok, why = music_ok(r)
        mix = ["[0:a]asplit=2[voice][vsc]"] if ok and r["audio"]["music"].get("duck", True) else ["[0:a]anull[voice]"]
        mix_in = ["[voice]"]
        if ok:
            mp = Path(r["audio"]["music"]["path"]); mp = mp if mp.is_absolute() else REPO / mp
            inputs += ["-stream_loop", "-1", "-i", str(mp.resolve())]
            dips = r["audio"].get("dips") or []          # bed holes before reveals (150-300 ms), editbymmh R5
            dip = (",volume='1-0.85*(" + "+".join(f"between(t,{d - 0.28:.3f},{d:.3f})" for d in dips) + ")':eval=frame") if dips else ""
            mix.append(f"[{n}:a]atrim=0:{total:.3f},aresample=48000,aformat=channel_layouts=stereo,volume={r['audio']['music'].get('db', -19)}dB{dip},"
                       f"afade=t=out:st={max(0, total - 1.2):.3f}:d=1.2[mus]")
            if r["audio"]["music"].get("duck", True):
                mix.append("[mus][vsc]sidechaincompress=threshold=0.03:ratio=6:attack=15:release=350[duck]"); mix_in.append("[duck]")
            else:
                mix_in.append("[mus]")
            n += 1
        elif r["audio"]["music"].get("path"):
            log(f"music skipped: {why}")
        from . import sfx as sfxlib
        cues = [(at_of(r, s["anchor"], starts), s.get("type", "whoosh"), s.get("db", -12), s.get("place", "auto")) for s in r["audio"].get("sfx", [])]
        cues += [(t_, kind, -14, "auto") for t_, kind in pops]
        used = []
        for a, kind, db, how in cues:
            if a is None or a >= total:
                continue
            f, src = sfxlib.pick(kind, a, cache, sfx_file)
            start = sfxlib.place(kind, a, sfxlib.meta_of(f, cache)) if how == "auto" else a   # onset/peak lands on the cut by role
            head = max(0.0, -start)
            ms = int(max(0.0, start) * 1000)
            inputs += ["-i", str(Path(f).resolve())]
            mix.append(f"[{n}:a]atrim=start={head:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume={db}dB,adelay={ms}|{ms}[s{n}]")
            mix_in.append(f"[s{n}]")
            used.append({"t": round(a, 3), "kind": kind, "file": Path(f).name, "source": src, "start": round(start, 3)})
            n += 1
        lufs = r["audio"].get("loudness", -14)
        mix.append("".join(mix_in) + (f"amix=inputs={len(mix_in)}:normalize=0:duration=first," if len(mix_in) > 1 else "anull,") +
                   f"loudnorm=I={lufs}:TP=-1.5:LRA=11,aresample=48000,alimiter=limit=0.84:level=false[aout]")
        final = out_dir / f"{tag}.mp4"
        ab = ["-c:a", "aac", "-b:a", "96k" if quality == "draft" else "192k"]
        ffmpeg(inputs + ["-filter_complex", ";".join(fc + mix), "-map", "[vout]", "-map", "[aout]", "-t", f"{total:.3f}"] + venc(quality) + ab +
               ["-movflags", "+faststart", str(final.resolve())], cwd=cache)
        log(f"  -> {final}  ({total:.2f} s)")
        owed = sfxlib.credits_for([sfxlib.LIB / u["kind"] / u["file"] for u in used if u["source"] == "library"])
        results.append({"aspect": A, "quality": quality, "path": str(final), "duration": round(total, 2), "W": W, "H": H, "music": why,
                        "sfx": used, "sfx_credits": owed})
        if owed:
            log("  SFX credits for the caption (CC BY): " + "; ".join(owed))
    if not name:
        man = rjson(out_dir / "renders.json", [])
        man += [dict(x, version=r["version"]) for x in results]
        wjson(out_dir / "renders.json", man)
    return r, results


def cmd_render(a, edit_dir):
    return render(edit_dir, a.version, "final" if a.final else "draft", a.aspects.split(",") if a.aspects else None, a.force)
