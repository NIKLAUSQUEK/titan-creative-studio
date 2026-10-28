"""Learn an edit style from 3-5 reference videos (links or files) -> a measured STYLE_STUDY.md + a ready preset.

`editor.py study <url|file> ... --name <style>`:
1. downloads each link with yt-dlp, to study only; the videos stay local and are never reused in an edit;
2. measures each one locally: cuts and average shot, words per minute, pauses, when speech starts, loudness, and hook and full frame sheets;
3. aggregates the numbers into StyleCard dna, then converts that to a preset with stylecard_to_preset (deterministic);
4. optional `--llm claude-cli`: one Claude call LOOKS at the sheets and names what numbers can't (caption look and position, fonts, colours,
   layout such as split screen or a top header, graphics, sound). Those strings merge into the dna before conversion.
Klaus reviews STYLE_STUDY.md + the sheets, then uses `assemble --preset style-<name>`. Nothing posts, nothing spends credits.
"""
import json, re
from pathlib import Path

from .common import REPO, TOOL, claude, cb, ffmpeg, log, probe, slug, wjson
from .ingest import load_audio, run, transcribe_words

STUDY_ROOT = REPO / "research" / "style-studies"
LOOK = """You are studying an editing style for Klaus's studio. Look at the contact sheets in {d} (sheet_*.jpg = 1 frame/s over the whole video,
hook_*.jpg = 4 frames/s over the first 3 s) and the measured numbers below. Return ONLY JSON with short concrete strings:
{{"captions": "position, words per group, case, font feel (sans/serif/handwritten), colours, highlight style, animation guess",
  "header": "any persistent title/header text: position, style, or none",
  "layout": "framing + layout (full frame, split top/bottom, picture-in-picture, screen recordings, green screen, cards)",
  "graphics": "motion graphics / diagrams / icons / stickers used, or none",
  "lighting": "grade and lighting feel",
  "camera": "camera moves and zooms",
  "sound": "music/SFX feel you can infer (energy, hits on cuts)",
  "pacing": "pacing in words",
  "vibe": "one line",
  "signature": "the 1-2 moves that make this style recognisable",
  "steal": ["3-5 concrete, copyable techniques"], "avoid": ["what would look off-brand for a health clinic"]}}
Measured: {m}"""


def fetch(src, d, browser=None):
    """browser: read the cookies of YOUR logged-in browser on this PC (chrome/edge/firefox/brave) so login-only
    Facebook posts and rate-limited Instagram reels download as you. Cookies stay on this PC and are never saved."""
    p = Path(src)
    if p.exists():
        return p
    import yt_dlp
    d.mkdir(parents=True, exist_ok=True)
    opts = {"outtmpl": str(d / "%(id)s.%(ext)s"), "format": "mp4/bestvideo*+bestaudio/best", "quiet": True, "noprogress": True, "merge_output_format": "mp4"}
    if browser and Path(browser).is_file():
        opts["cookiefile"] = str(browser)          # a cookies.txt you exported yourself
    elif browser:
        opts["cookiesfrombrowser"] = (browser,)
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(src, download=True)
    f = Path(y.prepare_filename(info)).with_suffix(".mp4")
    meta = {k: info.get(k) for k in ("id", "title", "channel", "uploader", "like_count", "comment_count", "view_count", "duration", "webpage_url")}
    wjson(d / f"{info['id']}.meta.json", meta)
    return f if f.exists() else next(d.glob(f"{info['id']}.*"))


def cuts_of(src, thr=0.2):
    """Lower threshold than ingest: split screens and panel swaps only change part of the frame."""
    r = run(["ffmpeg", "-hide_banner", "-i", str(src), "-vf", f"scale=320:-2,select='gt(scene,{thr})',showinfo", "-an", "-f", "null", "-"])
    return [round(float(m), 2) for m in re.findall(r"pts_time:([\d.]+)", r.stderr)]


def loudness(src):
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(src), "-vn", "-af", "ebur128", "-f", "null", "-"])
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    return float(m[-1]) if m else None


def measure(src, d, whisper_model):
    m = probe(src)
    dur = m.get("duration") or 0
    d.mkdir(parents=True, exist_ok=True)
    cuts = [c for c in cuts_of(src) if 0.2 < c < dur - 0.2]
    shots = [b - a for a, b in zip([0.0] + cuts, cuts + [dur])]
    audio = load_audio(str(src), d)
    words = transcribe_words(audio, whisper_model, "auto", None)[0] if audio is not None and len(audio) else []
    talk = sum(w["t1"] - w["t0"] for w in words)
    gaps = [b["t0"] - a["t1"] for a, b in zip(words, words[1:])]
    sid = src.stem
    ffmpeg(["-i", str(src), "-vf", "fps=1,scale=180:-1,tile=8x8", "-frames:v", "1", d / f"sheet_{sid}.jpg"], check=False)
    ffmpeg(["-t", "3", "-i", str(src), "-vf", "fps=4,scale=240:-1,tile=6x2", "-frames:v", "1", d / f"hook_{sid}.jpg"], check=False)
    return {"file": src.name, "duration_s": round(dur, 1), "width": m.get("width"), "height": m.get("height"), "cuts": len(cuts),
            "cuts_per_min": round(60 * len(cuts) / dur, 1) if dur else 0, "avg_shot_s": round(sum(shots) / len(shots), 2) if shots else dur,
            "median_shot_s": round(sorted(shots)[len(shots) // 2], 2) if shots else dur, "first_cut_s": cuts[0] if cuts else None,
            "words_per_min": round(60 * len(words) / dur) if dur else 0, "speech_share": round(talk / dur, 2) if dur else 0,
            "first_word_s": words[0]["t0"] if words else None, "pauses_over_0_5s": sum(1 for g in gaps if g > 0.5),
            "lufs": loudness(src), "opening_words": " ".join(w["w"] for w in words if w["t0"] < 3.0)}


def to_dna(ms, look=None):
    n = len(ms)
    avg = sorted(x["median_shot_s"] for x in ms)[n // 2]          # median of medians: one long-take ref can't skew the style
    wpm = sum(x["words_per_min"] for x in ms) / n
    cpm = sum(x["cuts_per_min"] for x in ms) / n
    energy = max(1, min(5, round(1 + (cpm / 12) + (wpm - 120) / 50)))
    pauses = sum(x["pauses_over_0_5s"] for x in ms) / n
    dna = {"avg_shot_s": round(avg, 2), "energy": energy,
           "pacing": ("very fast" if avg < 1.6 else "fast" if avg < 3 else "held long takes" if avg > 5 else "steady") +
                     (", natural pauses kept" if pauses > 6 else ", tight jump cuts")}
    for k, v in (look or {}).items():
        if isinstance(v, str) and v:
            dna[k] = (dna.get(k, "") + ", " + v).strip(", ") if k == "pacing" else v
    return dna


def study(srcs, name, llm="none", whisper_model="small", model=None, browser=None):
    d = STUDY_ROOT / slug(name)
    vids = d / "videos"
    ms, failed = [], []
    for s in srcs:
        log(f"study: {s}")
        try:
            f = fetch(s, vids, browser)
        except Exception as e:  # one bad link (login wall, image-only post, cookie error) must not sink the rest
            msg = str(e).splitlines()[-1]
            if re.search(r"DPAPI|decrypt|cookie", msg, re.I):
                msg += "  -> Chrome/Edge lock their cookies; log into the site in Firefox and use -Browser firefox, or pass a cookies.txt path"
            log(f"study: SKIPPED {s}: {msg}")
            failed.append(s)
            continue
        x = measure(f, d, whisper_model)
        meta = vids / f"{f.stem}.meta.json"
        if meta.exists():
            x["source"] = json.loads(meta.read_text(encoding="utf-8"))
        ms.append(x)
    if not ms:
        raise SystemExit("study: no reference could be downloaded (see SKIPPED lines above)")
    look = None
    if llm == "claude-cli":
        out = claude(LOOK.format(d=d, m=json.dumps(ms)), image_dir=d, model=model, step="study")
        look = cb.parse_json(out) if out else None
    dna = to_dna(ms, look)
    from .presets import stylecard_to_preset
    preset = stylecard_to_preset({"creator": {"name": name}, "dna": dna})
    preset["source"] = {"study": str(d.relative_to(REPO)), "refs": [x.get("source", {}).get("webpage_url") or x["file"] for x in ms]}
    if look and re.search(r"split", look.get("layout", ""), re.I):
        preset.setdefault("broll", {})["mode"] = "split"
    wjson(TOOL / "presets" / f"{preset['name']}.json", preset)
    wjson(d / "study.json", {"measured": ms, "look": look, "dna": dna, "preset": preset["name"]})
    rows = "\n".join(f"| {x['file']} | {x['duration_s']} | {x['avg_shot_s']} / {x['median_shot_s']} | {x['cuts_per_min']} | {x['words_per_min']} | "
                     f"{x['first_word_s']} | {x['speech_share']} | {x['lufs']} | {x['opening_words'][:60]} |" for x in ms)
    lk = "\n".join(f"- **{k}:** {v if isinstance(v, str) else '; '.join(v)}" for k, v in (look or {}).items()) or \
        "- (numbers only; run with `--llm claude-cli`, or open the sheets and describe the captions, layout and graphics)"
    md = f"""# Style study: {name}

Refs: {', '.join(preset['source']['refs'])}

| Ref | Dur s | Avg / median shot s | Cuts/min | Words/min | First word s | Speech share | LUFS | Opening words |
|---|---|---|---|---|---|---|---|---|
{rows}

## What it looks like
{lk}

## Preset
`{preset['name']}` (tools/editor/presets/{preset['name']}.json): pacing max shot {preset['pacing']['max_shot_s']} s, captions {json.dumps(preset.get('captions', {}))},
zoom every {preset['zoom']['every_s']} s, B-roll every {preset.get('broll', {}).get('every_s')} s, music {preset['music']['energy']}.
Use: `editor.py assemble --preset {preset['name']}`. The brand's edit-brand block and the ledger still win (fonts, placement, compliance).

Sheets: sheet_*.jpg (1 frame/s), hook_*.jpg (first 3 s). The downloaded videos are study material only (videos/ is git-ignored); never cut them into an edit.
"""
    (d / "STYLE_STUDY.md").write_text(md, encoding="utf-8")
    log(f"study -> {d / 'STYLE_STUDY.md'}  preset {preset['name']}")
    return d, preset


def cmd_study(a):
    d, p = study(a.refs, a.name, a.llm, a.whisper_model, a.claude_model, getattr(a, "browser", None))
    print((d / "STYLE_STUDY.md").read_text(encoding="utf-8"))
    return 0
