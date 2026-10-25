"""AI voices: natural stock voices (Piper) and consented voice clones (Chatterbox), all local, no API keys.

editor.py voice list
editor.py voice enroll <name> <audio/video files or a folder> --consent self|release:<path to signed release> [--who "Full Name"]
editor.py voice say <name | piper> "text or path/to/script.txt" --out vo.wav [--exaggeration 0.5] [--cfg 0.5]
editor.py voice forget <name>

- piper: neural stock voices (rhasspy/piper-voices), fast on CPU. For test footage, scratch VO and placeholders.
- clone (Chatterbox, Resemble AI, MIT licence): zero-shot cloning from 10-30 s of clean speech. Runs in its own venv
  (%LOCALAPPDATA%\\TitanEditor\\voice-venv; Run-Editor.ps1 -Voice installs it) because it pins its own torch.
  Outputs carry Resemble's inaudible PerTh watermark, which helps disclosure.
- voicestudio (github.com/debpalash/VoiceStudio, AGPL-3.0 desktop app; we only call its LOCAL API, nothing is bundled): if the app is
  running (http://localhost:3900), `voice say <name> ... --engine voicestudio` uses its OpenAI-compatible /v1/audio/speech with the
  voice profile you created in the app (`--vs-voice <profile id>`, or the id saved at enroll). Also: 646-language dubbing, voice
  design and demucs clean-up in the app. Model weights carry their OWN licences: check the app's Model Manager notice per engine
  before commercial use.
Rules (ledger 2026-10-20 voice + 2026-10-25 robotic voices):
- Clone only Klaus, staff or clients who consent, with a consent record. Never public figures, celebrities or anyone without a release.
- Voice samples stay on this PC (never in git); cast/registry.md lists the voice name, owner and consent only.
- Generated speech is labelled AI wherever the platform or market requires it; a cloned client voice is used only within the scope of
  their release. Real recorded voice beats any AI voice for testimony-like or health content.
"""
import json, os, re, shutil, subprocess, sys
from pathlib import Path

from .common import REPO, ffmpeg, log, now, rjson, wjson

HOME = Path(os.environ.get("LOCALAPPDATA") or Path.home() / ".cache") / "TitanEditor"
VOICES = HOME / "voices"
WORKER = Path(__file__).with_name("voice_worker.py")


def voice_python():
    """The interpreter that has chatterbox-tts installed (its own venv), or None."""
    cands = [os.environ.get("TITAN_VOICE_PY"), HOME / "voice-venv" / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python"), sys.executable]
    for c in cands:
        if c and Path(c).exists():
            r = subprocess.run([str(c), "-c", "import chatterbox"], capture_output=True)
            if r.returncode == 0:
                return str(c)
    return None


def speech_segments(wav, min_len=8.0, max_total=30.0):
    """Pick the cleanest continuous speech (by RMS) up to max_total seconds: the clone reference."""
    import numpy as np
    from .sfx import pcm
    y = pcm(wav, 24000)
    hop = 2400
    fr = y[: len(y) // hop * hop].reshape(-1, hop)
    db = 20 * np.log10(np.sqrt((fr ** 2).mean(1)) + 1e-9)
    speech = db > (np.percentile(db, 90) - 25)
    runs, s = [], None
    for i, v in enumerate(list(speech) + [False]):
        if v and s is None:
            s = i
        elif not v and s is not None:
            if i - s >= 5:
                runs.append((s, i))
            s = None
    out, total = [], 0.0
    for a, b in sorted(runs, key=lambda r: r[1] - r[0], reverse=True):
        d = (b - a) * hop / 24000
        out.append((a * hop / 24000, d)); total += d
        if total >= max_total:
            break
    return sorted(out), total


def cmd_enroll(name, sources, consent, who=None, strength="light"):
    if not consent or not (consent == "self" or consent.startswith("release:")):
        raise SystemExit("cloning needs consent: --consent self (it's your own voice) or --consent release:<path to the signed release>")
    if consent.startswith("release:") and not Path(consent[8:]).exists():
        raise SystemExit(f"release file not found: {consent[8:]}")
    files = []
    for s in sources:
        p = Path(s)
        files += sorted(f for f in p.rglob("*") if f.suffix.lower() in (".wav", ".mp3", ".m4a", ".mp4", ".mov", ".flac", ".ogg")) if p.is_dir() else [p]
    if not files:
        raise SystemExit("no audio/video samples given")
    d = VOICES / re.sub(r"[^a-z0-9_-]+", "-", name.lower())
    d.mkdir(parents=True, exist_ok=True)
    from .enhance import local_chain, noise_floor
    joined = d / "_all.wav"
    lst = d / "_list.txt"
    parts = []
    for i, f in enumerate(files):
        raw = d / f"_raw{i}.wav"
        ffmpeg(["-i", str(f), "-vn", "-ac", "1", "-ar", "24000", str(raw)])
        clean = d / f"_clean{i}.wav"
        ffmpeg(["-i", str(raw), "-af", local_chain(strength, noise_floor(raw)), "-ar", "24000", "-ac", "1", str(clean)])
        parts.append(clean); raw.unlink(missing_ok=True)
    lst.write_text("".join(f"file '{p.name}'\n" for p in parts), encoding="utf-8")
    ffmpeg(["-f", "concat", "-safe", "0", "-i", lst.name, "-c", "copy", joined.name], cwd=d)
    segs, total = speech_segments(joined)
    if total < 8:
        raise SystemExit(f"only {total:.1f} s of clear speech found; record 15-30 s of natural talking in a quiet room")
    sel = "+".join(f"between(t,{a:.2f},{a + l:.2f})" for a, l in segs)
    ffmpeg(["-i", joined.name, "-af", f"aselect='{sel}',asetpts=N/SR/TB", "-ar", "24000", "ref.wav"], cwd=d)
    for p in parts + [joined, lst]:
        Path(p).unlink(missing_ok=True)
    meta = {"name": name, "who": who or ("Klaus" if consent == "self" else None), "consent": consent, "enrolled": now(), "ref_seconds": round(total, 1),
            "sources": [str(f) for f in files], "engine": "chatterbox", "scope": "as per consent; label AI where required"}
    wjson(d / "voice.json", meta)
    reg = REPO / "cast" / "registry.md"
    line = f"| voice:{name} | {meta['who'] or 'CONFIRM'} | clone (chatterbox, local) | consent: {consent if consent == 'self' else 'release on file'} | {meta['enrolled'][:10]} |\n"
    txt = reg.read_text(encoding="utf-8") if reg.exists() else "# Cast registry\n"
    if f"voice:{name} |" not in txt:
        if "## Voices" not in txt:
            txt += "\n## Voices (samples stay on the PC; this lists names + consent only)\n| Voice | Person | Engine | Consent | Enrolled |\n|---|---|---|---|---|\n"
        reg.write_text(txt + line, encoding="utf-8")
    log(f"voice '{name}' enrolled: {total:.1f} s reference -> {d / 'ref.wav'} (consent: {consent})")
    return d


VS = os.environ.get("VOICESTUDIO_URL", "http://localhost:3900")


def voicestudio_up():
    import urllib.request
    try:
        urllib.request.urlopen(VS + "/v1/audio/voices", timeout=3).read()
        return True
    except Exception:
        return False


def voicestudio_voices():
    import urllib.request
    return json.loads(urllib.request.urlopen(VS + "/v1/audio/voices", timeout=10).read().decode("utf-8"))


def voicestudio_say(text, out, voice="default", model=None, speed=1.0, language=None):
    """POST /v1/audio/speech (OpenAI-compatible). Returns the wav path."""
    import base64, urllib.request
    body = {"input": text[:4096], "voice": voice, "response_format": "wav", "speed": speed}
    if model:
        body["model"] = model
    if language:
        body["language"] = language
    req = urllib.request.Request(VS + "/v1/audio/speech", data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}, method="POST")
    r = urllib.request.urlopen(req, timeout=1800)
    data, ctype = r.read(), r.headers.get("Content-Type", "")
    if "json" in ctype:                               # some builds return {"audio": base64} or {"url": ...}
        j = json.loads(data.decode("utf-8"))
        if j.get("audio"):
            data = base64.b64decode(j["audio"])
        elif j.get("url"):
            u = j["url"] if j["url"].startswith("http") else VS + j["url"]
            data = urllib.request.urlopen(u, timeout=600).read()
        else:
            raise SystemExit(f"VoiceStudio returned no audio: {str(j)[:200]}")
    Path(out).write_bytes(data)
    return Path(out)


def chunks(text, max_chars=260):
    sents = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text.strip()))
    out, cur = [], ""
    for s in sents:
        if len(cur) + len(s) > max_chars and cur:
            out.append(cur); cur = s
        else:
            cur = (cur + " " + s).strip()
    return out + ([cur] if cur else [])


def cmd_say(name, text, out, exaggeration=0.5, cfg=0.5, gap=0.22, engine="auto", vs_voice=None, language=None):
    text = Path(text).read_text(encoding="utf-8") if Path(text).exists() else text
    out = Path(out)
    d = VOICES / re.sub(r"[^a-z0-9_-]+", "-", name.lower())
    meta = rjson(d / "voice.json") or {}
    vs_voice = vs_voice or meta.get("voicestudio_profile")
    if engine == "voicestudio" or (engine == "auto" and vs_voice and voicestudio_up()):
        if not voicestudio_up():
            raise SystemExit(f"VoiceStudio isn't running at {VS}: open the app (voicestudio.sh) first")
        if name != "piper" and not meta:
            raise SystemExit(f"no consent record for '{name}': enroll it here first (editor.py voice enroll ... --consent ...), even if the clone lives in VoiceStudio")
        parts = []
        for i, c in enumerate(chunks(text, 3500)):
            parts.append(voicestudio_say(c, out.with_name(f"_{out.stem}_{i}.wav"), vs_voice or "default", language=language))
    elif name.startswith("piper"):
        from .selftest import tts
        parts = []
        for i, c in enumerate(chunks(text)):
            p = out.with_name(f"_{out.stem}_{i}.wav")
            if not tts(c, p):
                raise SystemExit("piper not available: pip install piper-tts")
            parts.append(p)
    else:
        if not meta or not (d / "ref.wav").exists():
            raise SystemExit(f"no enrolled voice '{name}'. editor.py voice enroll {name} <samples> --consent self|release:<file>")
        py = voice_python()
        if not py:
            raise SystemExit("voice cloning engine not installed: run .\\Run-Editor.ps1 -Voice (creates the chatterbox venv)")
        job = out.with_suffix(".job.json")
        parts = [out.with_name(f"_{out.stem}_{i}.wav") for i in range(len(chunks(text)))]
        wjson(job, {"ref": str(d / "ref.wav"), "chunks": chunks(text), "outs": [str(p) for p in parts], "exaggeration": exaggeration, "cfg": cfg})
        r = subprocess.run([py, str(WORKER), str(job)], text=True, capture_output=True)
        job.unlink(missing_ok=True)
        if r.returncode != 0:
            raise SystemExit("voice clone failed: " + r.stderr[-800:])
    gapf = out.with_name("_gap.wav")
    ffmpeg(["-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(gap), str(gapf)])
    lst = out.with_name(f"_{out.stem}.txt")
    norm = []
    for p in parts:
        q = p.with_name(p.stem + "_n.wav")
        ffmpeg(["-i", str(p), "-ar", "24000", "-ac", "1", str(q)]); norm.append(q)
    lst.write_text("".join(f"file '{p.name}'\nfile '{gapf.name}'\n" for p in norm), encoding="utf-8")
    ffmpeg(["-f", "concat", "-safe", "0", "-i", lst.name, "-af", "loudnorm=I=-16:TP=-1.5:LRA=9", "-ar", "48000", out.name], cwd=out.parent)
    for p in parts + norm + [gapf, lst]:
        Path(p).unlink(missing_ok=True)
    wjson(out.with_suffix(".voice.json"), {"voice": name, "engine": engine if engine != "auto" else ("voicestudio" if vs_voice else "chatterbox/piper"), "ai_generated": True, "label": "AI voice", "created": now(), "chars": len(text)})
    log(f"voice -> {out} (AI-generated: label it where required)")
    return out


def cmd_voice(a):
    if a.action == "list":
        print("piper (stock neural voice, local)")
        for d in sorted(VOICES.glob("*/voice.json")):
            m = rjson(d)
            print(f"{m['name']:16s} {m.get('who') or '?':16s} consent={m['consent']}  ref={m['ref_seconds']} s  enrolled {m['enrolled'][:10]}")
        print("clone engine (chatterbox):", "ready" if voice_python() else "not installed (Run-Editor.ps1 -Voice)")
        if voicestudio_up():
            print("VoiceStudio app: running at", VS)
            try:
                for v in (voicestudio_voices().get("voices") or voicestudio_voices().get("data") or [])[:30]:
                    print("   vs:", v.get("id") or v.get("voice_id"), v.get("name") or "")
            except Exception as e:
                print("   (couldn't list VoiceStudio voices:", str(e)[:80], ")")
        else:
            print("VoiceStudio app: not running (optional: voicestudio.sh)")
        return 0
    if a.action == "enroll":
        d = cmd_enroll(a.name, a.inputs, a.consent, a.who)
        if a.vs_voice:
            m = rjson(d / "voice.json"); m["voicestudio_profile"] = a.vs_voice; wjson(d / "voice.json", m)
        return 0
    if a.action == "say":
        cmd_say(a.name, " ".join(a.inputs), a.out or "vo.wav", a.exaggeration, a.cfg, engine=a.engine, vs_voice=a.vs_voice, language=a.language); return 0
    if a.action == "forget":
        d = VOICES / re.sub(r"[^a-z0-9_-]+", "-", a.name.lower())
        shutil.rmtree(d, ignore_errors=True)
        log(f"voice '{a.name}' samples deleted from this PC (remove its row from cast/registry.md if it shouldn't be listed)")
        return 0
    return 1
