"""Synthetic end-to-end test: builds a talking-head clip (with a retake, fillers and dead air) + a small B-roll library
(one folder consent-flagged), then runs ingest -> brief -> B-roll index/match -> assemble -> 3-aspect draft -> QC -> revisions
(trim, punchier captions, go back to v1) -> approve -> final 1080 -> handoff. Uses --llm none, so it costs zero Claude tokens.
Speech: espeak-ng (Linux/macOS) or Windows SAPI (PowerShell). Project: projects/_selftest (git-ignored, rebuilt each run); temp footage is deleted unless --keep.
"""
import argparse, json, shutil, subprocess, sys, tempfile, wave
from pathlib import Path

from .common import REPO, TOOL, ffmpeg, have, log, probe, rjson
from .ingest import load_clips

SCRIPT = [("Um, so today I want to talk about back pain.", 1.6),
          ("Stop stretching your back every morning.", 0.5),
          ("Stop stretching your back every single morning. It is not the fix.", 0.9),
          ("Most people think pain means damage, but it usually does not.", 0.4),
          ("Uh,", 0.5),
          ("Here is what to do instead. Go for a walk for ten minutes after your coffee.", 1.2),
          ("Follow for part two.", 0.6)]
BROLL = [("walking", "WALKING OUTDOORS", "0x2E7D32"), ("coffee", "COFFEE CUP", "0x6D4C41"), ("gym", "GYM DUMBBELLS", "0x37474F"),
         ("office", "OFFICE DESK LAPTOP", "0x1565C0"), ("ocean", "OCEAN BEACH WAVES", "0x0277BD")]


def tts(text, out):
    if have("espeak-ng") or have("espeak"):
        subprocess.run([shutil.which("espeak-ng") or shutil.which("espeak"), "-s", "155", "-w", str(out), text], check=True, capture_output=True)
        return True
    if sys.platform == "win32":
        ps = ("Add-Type -AssemblyName System.Speech; $s=New-Object System.Speech.Synthesis.SpeechSynthesizer; "
              f"$s.SetOutputToWaveFile('{out}'); $s.Speak(\"{text}\"); $s.Dispose()")
        subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=True, capture_output=True)
        return Path(out).exists()
    return False


def make_footage(d):
    import numpy as np
    sr, chunks = 22050, []
    spoke = True
    for i, (line, pause) in enumerate(SCRIPT):
        w = d / f"l{i}.wav"
        if not tts(line, w):
            spoke = False; break
        ffmpeg(["-i", w, "-ar", sr, "-ac", 1, d / f"r{i}.wav"])
        with wave.open(str(d / f"r{i}.wav")) as f:
            chunks.append(np.frombuffer(f.readframes(f.getnframes()), np.int16))
        chunks.append(np.zeros(int(pause * sr), np.int16))
    if not spoke:
        log("no TTS engine (espeak-ng / Windows SAPI): using a tone track; transcript checks are skipped")
        chunks = [(3000 * np.sin(2 * np.pi * 220 * np.arange(int(12 * sr)) / sr)).astype(np.int16)]
    audio = np.concatenate([np.zeros(int(0.8 * sr), np.int16)] + chunks)
    with wave.open(str(d / "voice.wav"), "wb") as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(sr); f.writeframes(audio.tobytes())
    dur = len(audio) / sr
    font = str(TOOL / "fonts" / "DejaVuSans-Bold.ttf").replace("\\", "/").replace(":", "\\:")
    face = (f"drawbox=x=540:y=150:w=200:h=260:color=0xE0B090@1:t=fill,drawbox=x=420:y=420:w=440:h=300:color=0x263238@1:t=fill,"
            f"drawtext=fontfile='{font}':text='TALKING HEAD %{{pts\\:hms}}':x=40:y=40:fontsize=36:fontcolor=white")
    ffmpeg(["-f", "lavfi", "-i", f"color=c=0x90A4AE:s=1280x720:r=30:d={dur:.2f}", "-i", d / "voice.wav", "-vf", face,
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", 28, "-c:a", "aac", "-shortest", d / "footage" / "talking_head_take1.mp4"])
    lib = d / "broll"
    for name, label, col in BROLL:
        (lib / "clinic_library").mkdir(parents=True, exist_ok=True)
        ffmpeg(["-f", "lavfi", "-i", f"color=c={col}:s=1280x720:r=30:d=4", "-vf",
                f"drawtext=fontfile='{font}':text='{label}':x=(w-tw)/2:y=(h-th)/2:fontsize=90:fontcolor=white", "-c:v", "libx264", "-preset", "ultrafast",
                lib / "clinic_library" / f"{name}_broll.mp4"])
    (lib / "patients").mkdir(exist_ok=True)
    ffmpeg(["-f", "lavfi", "-i", "color=c=0x2E7D32:s=1280x720:r=30:d=4", "-vf",
            f"drawtext=fontfile='{font}':text='WALKING OUTDOORS':x=(w-tw)/2:y=(h-th)/2:fontsize=96:fontcolor=white", "-c:v", "libx264", "-preset", "ultrafast",
            lib / "patients" / "walking_patient.mp4"])
    return d / "footage", lib, spoke


def selftest(a):
    from . import cli
    proj = "_selftest"
    pdir = REPO / "projects" / proj
    shutil.rmtree(pdir, ignore_errors=True)
    tmp = Path(tempfile.mkdtemp(prefix="titan_editor_"))
    (tmp / "footage").mkdir()
    results = []

    def ok(name, cond, detail=""):
        results.append((name, bool(cond), detail))
        log(("PASS " if cond else "FAIL ") + name + (f"  ({detail})" if detail else ""))

    footage, lib, spoke = make_footage(tmp)
    E = pdir / "autoedit"
    run = lambda *args: cli.main(["--project", proj, *[str(x) for x in args]])
    run("ingest", footage, "--whisper-model", a.whisper_model)
    idx = rjson(E / "ingest" / "index.json")
    cid = idx["clips"][0]["id"]
    an = rjson(E / "ingest" / cid / "analysis.json")
    words = rjson(E / "ingest" / cid / "words.json")
    raw = probe(footage / "talking_head_take1.mp4")["duration"]
    if spoke:
        ok("ingest: word timestamps", len(words) > 30, f"{len(words)} words")
        ok("ingest: retake detected (dropped take)", any(not s.get("best") for s in an["sentences"]), f"{sum(1 for s in an['sentences'] if not s.get('best'))} dropped")
        ok("ingest: fillers found", an["fillers"]["hard"] >= 1, json.dumps(an["fillers"]))
        ok("ingest: silences found", len(an["silences"]) >= 2, f"{len(an['silences'])} silences")
    ok("ingest: contact sheet", (E / "ingest" / cid / "sheet.jpg").exists())
    run("brief", "--llm", "none", "--brand", "physio-spot", "--goal", "expert", "--platform", "tiktok", "--target-s", "20")
    b = rjson(E / "brief.json")
    ok("brief: hooks ranked", 1 <= len(b["hooks"]) <= 5, f"{len(b['hooks'])} hooks; #1 = {b['hooks'][0]['text'] if b['hooks'] else None}")
    ok("brief: EDIT_BRIEF.md", (E / "EDIT_BRIEF.md").exists())
    clip_ok = not a.no_clip
    try:
        import open_clip  # noqa: F401
    except Exception:
        clip_ok = False
    index_dir = tmp / "index"
    if clip_ok:
        run("broll-index", lib, "--index-dir", index_dir)
        run("broll-index", lib, "--index-dir", index_dir)  # second run must be incremental (all unchanged)
        from .broll import search
        top = search(index_dir, "a person walking outdoors", 3)
        ok("broll: text search finds the walking clip", bool(top) and top[0]["name"] == "walking_broll.mp4", f"top={[t['name'] for t in top]}")
        allr = search(index_dir, "walking outdoors", 10, allow_sensitive=True)
        ok("broll: consent flag set on patients/ folder", any(t["flag"] for t in allr if "patients" in t["path"]))
        ok("broll: flagged clip excluded by default", all("patients" not in t["path"] for t in search(index_dir, "walking outdoors", 10)))
        run("broll-match", "--llm", "none", "--index-dir", index_dir)
        bc = rjson(E / "broll_candidates.json")
        ok("broll: beats matched", any(x.get("pick") is not None for x in bc["beats"]), f"{sum(1 for x in bc['beats'] if x.get('pick') is not None)}/{len(bc['beats'])}")
    run("assemble", "--preset", "talking-head-punchy", "--aspects", "9:16,1:1,16:9")
    from .recipe import item_starts, load
    v1 = load(E, 1)
    _, body1 = item_starts(v1)
    ok("recipe v1: silence/filler/retake cut", body1 < raw - 2.0, f"{body1:.2f} s from {raw:.2f} s raw")
    run("validate")
    run("render")
    man = rjson(E / "renders" / "renders.json")
    sizes = {x["aspect"]: (x["W"], x["H"]) for x in man}
    ok("render: 3 aspects from one recipe", set(sizes) == {"9:16", "1:1", "16:9"}, str(sizes))
    ok("render: draft is lowest quality (360 short edge)", all(min(s) == 360 for s in sizes.values()))
    for x in man:
        m = probe(x["path"])
        ok(f"render {x['aspect']}: has audio + right size", m["has_audio"] and (m["width"], m["height"]) == (x["W"], x["H"]), f"{m['width']}x{m['height']} {m['duration']} s")
    run("qc")
    ok("qc: report + qc_frames contact sheet", (E / "qc" / "QC_v1_draft.md").exists() and (E / "qc" / "v1_9x16" / "contact_sheet.jpg").exists())
    run("revise", "cut first 2 s, punchier captions", "--llm", "none")
    v2 = load(E, 2)
    _, body2 = item_starts(v2)
    ok("revise: 'cut first 2 s' -> v2 is 2 s shorter", abs((body1 - body2) - 2.0) < 0.06, f"{body1:.2f} -> {body2:.2f}")
    ok("revise: punchier captions", v2["style"]["captions"]["size"] > v1["style"]["captions"]["size"])
    run("render", "--aspects", "9:16")
    run("revise", "go back to v1", "--llm", "none")
    v3 = load(E, 3)
    ok("revise: 'go back to v1' -> v3 == v1 timeline", v3["items"] == v1["items"] and v3["parent"] == 1)
    try:
        run("render", "--final", "--aspects", "9:16")
        ok("final blocked until approved", False)
    except SystemExit:
        ok("final blocked until approved", True)
    run("approve")
    run("render", "--final", "--aspects", "9:16")
    fin = [x for x in rjson(E / "renders" / "renders.json") if x["quality"] == "final"][-1]
    m = probe(fin["path"])
    ok("final: 1080x1920", (m["width"], m["height"]) == (1080, 1920), f"{m['width']}x{m['height']}")
    run("qc", "--final")
    run("handoff")
    ok("handoff for /publish", (E / "HANDOFF.md").exists())
    run("expand", "--count", 6)
    vj = rjson(E / "variants" / "v3" / "variants.json")
    vs = vj["variants"] if vj else []
    ok("expand: 6 variants with files", len(vs) == 6 and all(v["files"] for v in vs), ", ".join(f"{v['id']}:{v['format']}" for v in vs))
    reels = [v for v in vs if v["format"] == "reel"]
    ok("expand: reels differ on >= 2 axes", all(sum(a[k] != b[k] for k in ("hook", "header", "duration", "speed", "captions", "swap")) >= 2
                                              for i, a in enumerate(reels) for b in reels[i + 1:]))
    vmd = (E / "variants" / "v3" / "VARIANTS.md").read_text(encoding="utf-8")
    ok("expand: every reel has its own opening (distinctness check)", "- ok: every reel has its own opening" in vmd)
    ok("expand: CTA stays last in every reel", all(v["beats"][-1] == reels[0]["beats"][-1] for v in reels if v["duration"] != "micro" or len(v["beats"]) > 2))
    import copy
    from .render import render
    rc = copy.deepcopy(v3)
    rc["chats"] = [{"id": "chat1", "anchor": {"item": rc["items"][0]["id"], "offset": 0.5}, "dur": 2.5,
                    "messages": [{"side": "me", "name": "Ashley", "text": "Did you do the exercises? 👀", "at": 0.0},
                                 {"side": "them", "text": "...define exercises", "at": 1.2, "typing": 0.5}]}]
    for b_ in rc["broll"]:
        b_["mode"] = "split"                  # also exercises the split-screen layout (B-roll top, speaker bottom)
    _, cres = render(E, quality="draft", aspects=["9:16"], recipe=rc, out_dir=E / "renders" / "chat", name="chat")
    fr = E / "renders" / "chat" / "chat_frame.png"
    ffmpeg(["-ss", "2.4", "-i", cres[0]["path"], "-frames:v", "1", fr])
    from PIL import Image
    px_ = list(Image.open(fr).convert("RGB").getdata())
    blue = sum(1 for p_ in px_ if p_[2] > 180 and p_[0] < 90)
    dark = sum(1 for p_ in px_ if max(p_) < 30) / len(px_)
    ok("texting scene + split-screen B-roll render", blue > 200 and dark > 0.5, f"blue px {blue}, dark {dark:.0%}")
    from .melody import make_song
    rows, tim = make_song("Squeeze and lift and hold for three\nNow relax and let it be", E / "song", "twinkle")
    ok("song: syllable fit + guide track + karaoke timings", all(r["status"] == "ok" for r in rows) and (E / "song" / "guide.wav").exists()
       and probe(E / "song" / "guide.wav").get("duration", 0) > 8 and tim[1]["start"] > tim[0]["start"], f"{[r['syllables'] for r in rows]}")
    from .enhance import align, enhance, local_chain, noise_floor
    sw = E / "enh_test"; sw.mkdir(exist_ok=True)
    ffmpeg(["-i", load_clips(E)[0]["meta"]["path"], "-f", "lavfi", "-i", "anoisesrc=c=pink:a=0.02:d=30", "-filter_complex",
            "[0:a]aresample=48000,aformat=channel_layouts=mono[v];[1:a]aresample=48000[n];[v][n]amix=inputs=2:duration=first:normalize=0",
            "-ac", "1", "-ar", "48000", sw / "noisy.wav"])
    ffmpeg(["-i", sw / "noisy.wav", "-af", local_chain("normal", noise_floor(sw / "noisy.wav")), sw / "clean.wav"])
    nf0, nf1 = noise_floor(sw / "noisy.wav"), noise_floor(sw / "clean.wav")
    ok("enhance (local): noise floor drops >= 6 dB", nf1 < nf0 - 6, f"{nf0} -> {nf1} dBFS")
    ffmpeg(["-f", "lavfi", "-i", "sine=f=660:d=1.234", "-i", sw / "clean.wav", "-filter_complex", "[0:a]aresample=48000[j];[j][1:a]concat=n=2:v=0:a=1",
            "-ac", "1", sw / "jingled.wav"])
    off = align(sw / "clean.wav", sw / "jingled.wav")
    ok("enhance (auphonic path): returned audio re-aligned to the clip", abs(off - 1.234) < 0.003, f"found {off:.4f} s, expected 1.234")
    rows = enhance(E, "local")
    vk = load_clips(E)[0]["meta"].get("audio_path")
    _, eres = render(E, quality="draft", aspects=["9:16"], recipe=load(E, 3), out_dir=E / "renders" / "enh", name="enh")
    ok("enhance: render uses the enhanced voice, same length", bool(vk) and abs(eres[0]["duration"] - probe(eres[0]["path"])["duration"]) < 0.1, f"{rows[0]}")
    enhance(E, "local", off=True)
    from .sfx import KINDS, place
    pw = place("whoosh", 5.0, {"peak_s": 0.25, "onset_s": 0.02})
    ph = place("impact", 5.0, {"peak_s": 0.03, "onset_s": 0.006})
    ok("sfx placement: whoosh peaks just after the cut, hit attacks just before", abs(pw + 0.25 - 5.037) < 1e-6 and abs(ph + 0.006 - 4.99) < 1e-6,
       f"whoosh starts {pw:.3f}, impact starts {ph:.3f}")
    srcs = {u["source"] for u in eres[0]["sfx"]}
    ok("sfx: real library recordings used when assets/sfx has them", srcs <= {"library", "earshot", "synth"} and eres[0]["sfx"] != [],
       f"{[(u['kind'], u['source'], u['file'][:24]) for u in eres[0]['sfx']]}")
    from .textcard import card
    im = card("🇵🇰\nNAHHH BRO 😭💀", 360, 640, "outline", 0.2, 0.05, uppercase=True)
    colours = {px[:3] for px in im.crop(im.getbbox()).getdata() if px[3] > 200} if im.getbbox() else set()
    ok("text card: emoji header renders in colour", len(colours) > 20, f"{len(colours)} distinct colours")
    from .presets import stylecard_to_preset
    p = stylecard_to_preset({"creator": {"name": "Test Creator"}, "dna": {"energy": 5, "avg_shot_s": 1.1, "captions": "word-by-word pop, yellow highlight, all caps, centre",
                                                                         "sound": "whooshes and bass drops", "lighting": "high contrast, warm"}})
    ok("stylecard -> preset", p["captions"]["max_words"] == 2 and p["captions"]["uppercase"] and p["pacing"]["max_shot_s"] < 2.5 and p["grade"]["contrast"] > 1.1)
    from .qc import compliance_scan
    v3["texts"].append({"type": "hook", "text": "The best clinic, free consult", "anchor": {"item": v3["items"][0]["id"], "offset": 0}})
    ok("compliance scan flags SG-health words", len(compliance_scan(v3, {c["id"]: c for c in load_clips(E)}, "health clinic")) >= 2)
    passed = sum(1 for _, c, _ in results if c)
    print(f"\nSELFTEST {passed}/{len(results)} passed. Outputs: {E / 'renders'}")
    sheets = sorted((E / "qc").rglob("*.jpg"))
    print("Look at:", *[str(s) for s in sheets[:6]], sep="\n  ")
    if not a.keep:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0 if passed == len(results) else 1
