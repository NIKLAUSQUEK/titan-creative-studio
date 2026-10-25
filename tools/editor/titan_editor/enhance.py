"""Voice enhancement for recorded speech: make a phone or lav mic sound closer to a studio.

`editor.py enhance [--engine local|auphonic] [--clips c01,c02]` writes ingest/<clip>/voice.enhanced.wav and sets meta.audio_path.
The renderer then uses that voice instead of the camera audio. The picture and the timings are untouched, because the enhanced
track is aligned sample-exactly to the original. `enhance --off` goes back to the camera audio.

Engines:
- local (default, free, offline): an ffmpeg chain of
  rumble high-pass -> adaptive denoise (afftdn, noise floor learnt from the clip's quietest stretch) -> optional RNNoise (arnndn,
  if a model is in assets/models/rnnoise/) -> de-mud / presence EQ -> de-esser -> gentle compressor -> peak limit.
  Good on hiss, fan and room tone; it cannot remove heavy reverb or a loud second voice.
- auphonic (optional, AUPHONIC_API_KEY in the environment, never in a file): Auphonic's leveler + AI noise/reverb reduction + filtering.
  Free plan: 2 h of audio a month, billed at least 3 min per production. So every selected clip goes up as ONE batched production
  (clips joined with gaps) and is split back afterwards. Free-plan productions carry an Auphonic jingle at the start and end, by
  their terms. The jingle sits outside the clips' timeline, so it never lands in the edit; for published brand work, buy credits
  (no jingle) or use the local engine. Uploading sends the voice to Auphonic (EU servers): Klaus's own voice is fine; other
  people's recordings need their consent, and patient audio never goes up.
"""
import json, os, subprocess, time, urllib.request, uuid as _uuid
from pathlib import Path

from .common import REPO, ffmpeg, log, rjson, wjson
from .ingest import load_clips

API = "https://auphonic.com/api"
SR = 48000


def rnnoise_model():
    d = REPO / "assets" / "models" / "rnnoise"
    ms = sorted(d.glob("*.rnnn")) if d.is_dir() else []
    return ms[0] if ms else None


def local_chain(strength="normal", floor_db=-50.0):
    """floor_db = the clip's measured noise floor: the denoiser is told where the noise sits, and a soft gate (-20 dB range, so pauses
    stay natural) sits 10 dB above it, BEFORE the compressor, so make-up gain can't lift the hiss back up."""
    nr = {"light": 10, "normal": 20, "strong": 30}[strength]
    fl = max(-80.0, min(-20.0, floor_db if floor_db is not None else -50.0))
    gate = 10 ** ((fl + 10) / 20)
    chain = ["highpass=f=75:poles=2", f"afftdn=nr={nr}:nf={fl:.0f}:tn=1"]
    m = rnnoise_model()
    if m:
        chain.append(f"arnndn=m='{m.as_posix()}':mix=0.85")
    chain += [f"agate=threshold={gate:.5f}:ratio=3:range={0.1 if strength != 'light' else 0.25}:attack=5:release=150",
              "equalizer=f=220:t=q:w=1.1:g=-2.5",          # mud
              "equalizer=f=3200:t=q:w=1.3:g=2.5",           # presence / intelligibility
              "equalizer=f=11000:t=h:w=0.7:g=1.5",          # air
              "deesser=i=0.35:m=0.5:f=0.5",
              "acompressor=threshold=-22dB:ratio=3:attack=8:release=160:makeup=5",
              "alimiter=limit=0.89:level=false"]
    return ",".join(chain)


def extract(src, out):
    ffmpeg(["-i", str(src), "-vn", "-ac", "1", "-ar", str(SR), "-c:a", "pcm_s16le", str(out)])


def noise_floor(wav):
    """dBFS of the quietest 10 % of 50 ms windows: a rough noise-floor read for the before/after report."""
    import numpy as np
    from .sfx import pcm
    y = pcm(wav, SR)
    hop = SR // 20
    fr = y[: len(y) // hop * hop].reshape(-1, hop)
    db = np.sort(20 * np.log10(np.sqrt((fr ** 2).mean(1)) + 1e-9))
    return round(float(db[: max(1, len(db) // 10)].mean()), 1) if len(db) else None


def align(orig, enh, max_shift_s=40.0):
    """Offset (s) of orig inside enh, by cross-correlating 10 ms energy envelopes (FFT), refined to the sample on a 1 s window."""
    import numpy as np
    from .sfx import pcm
    a, b = pcm(orig, SR), pcm(enh, SR)
    hop = SR // 100

    def env(y):
        f = y[: len(y) // hop * hop].reshape(-1, hop)
        e = np.log10((f ** 2).mean(1) + 1e-8)
        return e - e.mean()
    ea, eb = env(a[: SR * 60]), env(b[: int(SR * (60 + max_shift_s))])
    n = 1 << int(np.ceil(np.log2(len(ea) + len(eb))))
    xc = np.fft.irfft(np.fft.rfft(eb, n) * np.conj(np.fft.rfft(ea, n)), n)[: int(max_shift_s * 100) + 1]
    lag = int(np.argmax(xc)) * hop
    i0 = int(np.argmax(np.abs(a[: SR * 10]))) if len(a) > SR else 0          # refine around the loudest early sample
    w = a[max(0, i0 - SR // 2): i0 + SR // 2]
    seg = b[max(0, lag + i0 - SR // 2 - hop): lag + i0 + SR // 2 + hop]
    if len(w) and len(seg) > len(w):
        c = np.correlate(seg, w, mode="valid")
        lag += int(np.argmax(c)) - hop
    return max(0, lag) / SR


# ---------------- auphonic ----------------
def _req(method, path, key, data=None, files=None, ctype=None):
    url = path if path.startswith("http") else API + path
    headers = {"Authorization": f"bearer {key}"}
    body = None
    if files:
        bnd = "----titan" + _uuid.uuid4().hex
        parts = []
        for name, fp in files.items():
            parts.append((f"--{bnd}\r\nContent-Disposition: form-data; name=\"{name}\"; filename=\"{Path(fp).name}\"\r\n"
                          f"Content-Type: application/octet-stream\r\n\r\n").encode() + Path(fp).read_bytes() + b"\r\n")
        body = b"".join(parts) + f"--{bnd}--\r\n".encode()
        headers["Content-Type"] = f"multipart/form-data; boundary={bnd}"
    elif data is not None:
        body = json.dumps(data).encode()
        headers["Content-Type"] = "application/json"
    r = urllib.request.urlopen(urllib.request.Request(url, data=body, headers=headers, method=method), timeout=600)
    raw = r.read()
    return raw if ctype == "raw" else json.loads(raw.decode("utf-8"))


def auphonic(in_wav, out_wav, key, denoise="dynamic", loudness=-16):
    prod = _req("POST", "/productions.json", key, data={
        "metadata": {"title": f"TITAN editor {Path(in_wav).stem}"},
        "output_files": [{"format": "flac"}],
        "algorithms": {"filtering": True, "leveler": True, "normloudness": True, "loudnesstarget": loudness,
                       "denoise": True, "denoisemethod": denoise, "denoiseamount": 0, "silence_cutter": False, "filler_cutter": False,
                       "cough_cutter": False}})["data"]
    uid = prod["uuid"]
    log(f"auphonic: production {uid} (upload {Path(in_wav).stat().st_size / 1e6:.1f} MB)")
    _req("POST", f"/production/{uid}/upload.json", key, files={"input_file": in_wav})
    _req("POST", f"/production/{uid}/start.json", key, data={})
    t0 = time.time()
    while True:
        d = _req("GET", f"/production/{uid}.json", key)["data"]
        if d["status"] == 3:
            break
        if d["status"] in (2, 9, 11) or time.time() - t0 > 3600:
            raise SystemExit(f"auphonic production {uid}: {d.get('status_string')} {d.get('error_message') or ''}")
        time.sleep(8)
    url = d["output_files"][0]["download_url"]
    tmp = Path(out_wav).with_suffix(".flac")
    tmp.write_bytes(_req("GET", url, key, ctype="raw"))
    ffmpeg(["-i", str(tmp), "-ac", "1", "-ar", str(SR), "-c:a", "pcm_s16le", str(out_wav)])
    tmp.unlink(missing_ok=True)
    return d


# ---------------- command ----------------
def enhance(edit_dir, engine="local", clip_ids=None, strength="normal", off=False):
    clips = [c for c in load_clips(edit_dir) if not clip_ids or c["id"] in clip_ids]
    clips = [c for c in clips if c["meta"].get("has_audio")]
    if not clips:
        raise SystemExit("no clips with audio (ingest first)")
    if off:
        for c in clips:
            c["meta"].pop("audio_path", None); c["meta"].pop("audio_enhance", None)
            wjson(c["dir"] / "meta.json", c["meta"])
        log(f"enhance off: {len(clips)} clip(s) back on camera audio")
        return []
    work = edit_dir / "enhance"
    work.mkdir(parents=True, exist_ok=True)
    origs = []
    for c in clips:
        o = work / f"{c['id']}.orig.wav"
        extract(c["meta"]["path"], o)
        origs.append(o)
    outs = []
    if engine == "local":
        for c, o in zip(clips, origs):
            e = c["dir"] / "voice.enhanced.wav"
            ffmpeg(["-i", str(o), "-af", local_chain(strength, noise_floor(o)), "-ar", str(SR), "-c:a", "pcm_s16le", str(e)])
            outs.append((c, o, e, 0.0))
    elif engine == "auphonic":
        key = os.environ.get("AUPHONIC_API_KEY")
        if not key:
            raise SystemExit("set AUPHONIC_API_KEY in your environment first (Auphonic > Account > API key). Never paste it into a file or chat.")
        gap = 1.5                                                 # one batched production: clips joined with silence, split back after
        lst, offs, t = work / "batch.txt", [], 0.0
        lst.write_text("".join(f"file '{o.name}'\nfile 'gap.wav'\n" for o in origs), encoding="utf-8")
        ffmpeg(["-f", "lavfi", "-i", f"anullsrc=r={SR}:cl=mono", "-t", str(gap), "-c:a", "pcm_s16le", str(work / "gap.wav")])
        for o in origs:
            offs.append(t)
            t += float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(o)],
                                      capture_output=True, text=True).stdout or 0) + gap
        batch = work / "batch.wav"
        ffmpeg(["-f", "concat", "-safe", "0", "-i", lst.name, "-c:a", "pcm_s16le", batch.name], cwd=work)
        log(f"auphonic: {len(origs)} clip(s), {t / 60:.1f} min in one production (free plan bills >= 3 min per production)")
        enh_all = work / "batch.enhanced.wav"
        auphonic(batch, enh_all, key)
        lead = align(batch, enh_all)                             # anything Auphonic put before the timeline (e.g. a free-plan jingle)
        log(f"auphonic: output aligned, timeline starts at {lead:.3f} s of the returned file")
        for c, o, off in zip(clips, origs, offs):
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(o)],
                                       capture_output=True, text=True).stdout or 0)
            e = c["dir"] / "voice.enhanced.wav"
            ffmpeg(["-ss", f"{lead + off:.4f}", "-t", f"{dur:.4f}", "-i", str(enh_all), "-c:a", "pcm_s16le", str(e)])
            outs.append((c, o, e, lead + off))
    else:
        raise SystemExit("engine: local | auphonic")
    rows = []
    for c, o, e, _ in outs:
        drift = align(o, e, 2.0) if engine == "auphonic" else 0.0
        nf0, nf1 = noise_floor(o), noise_floor(e)
        c["meta"]["audio_path"] = str(e.resolve())
        c["meta"]["audio_enhance"] = {"engine": engine, "strength": strength if engine == "local" else None, "noise_floor_db": [nf0, nf1],
                                      "sync_check_s": round(drift, 4)}
        wjson(c["dir"] / "meta.json", c["meta"])
        rows.append({"clip": c["id"], "engine": engine, "noise_floor_before": nf0, "noise_floor_after": nf1, "sync_check_s": round(drift, 4)})
        log(f"  {c['id']}: noise floor {nf0} -> {nf1} dBFS{'' if not drift else f', residual offset {drift * 1000:.1f} ms'}")
    for o in origs:
        o.unlink(missing_ok=True)
    wjson(work / "enhance.json", rows)
    return rows


def cmd_enhance(a, edit_dir):
    enhance(edit_dir, a.engine, a.clips.split(",") if a.clips else None, a.strength, a.off)
    log("re-render to hear it: editor.py render (cache keys include the voice track)")
    return 0
