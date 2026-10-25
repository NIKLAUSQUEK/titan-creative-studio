"""Sound effects: real recordings first, matched by measurement, placed on the frame.

Source order for a cue kind (whoosh, impact, pop, ding, riser, click, bass, sting, scratch, drone):
1. assets/sfx/<kind>/: real recordings. Klaus's own packs, or `editor.py sfx-fetch <kind>` from Openverse (Freesound CC0 / CC BY;
   commercial use OK; credits in assets/sfx/CREDITS.md). Takes rotate per cue so a reel never repeats one file.
2. Earshot (github.com/Leonxlnx/earshot, MIT, optional). If the `earshot` CLI is installed, its bank of 252 code-made SFX renders by id,
   with whooshes aimed so their loudest moment lands on the cut (`--apex`). Original audio, no licence questions.
3. The built-in synth (render.SFX_SYNTH): always available, the plainest.
Placement (the "matching" fix, after Clipwing real-sfx and Earshot's launch-film measurements): each file's onset and peak are measured
once (cached), and the cue is placed by role. Hits, pops and clicks land their attack a few ms BEFORE the cut; whooshes put their
loudest moment just AFTER it; risers peak ON it. Before this, every file started at the cue, so a whoosh peaked ~0.3 s late.
"""
import hashlib, json, re, shutil, subprocess, urllib.parse, urllib.request, wave
from pathlib import Path

from .common import REPO, ffmpeg, log, rjson, wjson

LIB = REPO / "assets" / "sfx"
KINDS = {  # Openverse query words, wanted length range (s), earshot ids (first that renders wins), placement
    "whoosh": {"q": ["whoosh", "swoosh", "swish"], "dur": (0.25, 1.4), "avoid": ["combat", "sword", "melee", "wind loop"], "earshot": ["whoosh_fast/crisp", "swish/bright", "whoosh_fast"], "align": "peak", "offset_ms": 37},
    "impact": {"q": ["cinematic impact", "trailer hit boom", "deep impact boom"], "dur": (0.3, 3.0), "centroid_max": 2500,
               "avoid": ["glass", "ice", "metal", "door", "car", "gun", "shot", "boxing", "punch"], "earshot": ["cut_hit/punch", "pro_impact", "impact"], "align": "onset", "offset_ms": -10},
    "pop": {"q": ["pop", "bubble pop", "ui pop"], "dur": (0.04, 0.6), "avoid": ["music", "song", "cork", "balloon"], "earshot": ["ui_pop/soft", "pro_pop", "pop"], "align": "onset", "offset_ms": -11},
    "ding": {"q": ["ding", "notification chime", "bell ding"], "dur": (0.2, 2.0), "earshot": ["notify/mid_tine", "pro_notify", "notify"], "align": "onset", "offset_ms": -11},
    "riser": {"q": ["riser", "tension riser", "rising swell"], "dur": (0.8, 4.0), "earshot": ["riser/dark", "pro_riser", "riser"], "align": "peak", "offset_ms": 0},
    "click": {"q": ["click", "mouse click", "ui click"], "dur": (0.01, 0.3), "earshot": ["pro_click", "click"], "align": "onset", "offset_ms": -11},
    "bass": {"q": ["sub drop", "bass drop", "low boom"], "dur": (0.4, 3.0), "centroid_max": 900, "avoid": ["music", "loop", "song"], "earshot": ["cut_hit/sub", "pro_sub_drop", "sub_drop"], "align": "onset", "offset_ms": -10},
    "sting": {"q": ["suspense sting", "dramatic sting", "logo sting"], "avoid": ["baseball", "cartoon", "tabla", "ambience", "ambient", "loop"], "dur": (0.5, 4.0), "earshot": ["pro_logo_sting", "logo_sting"], "align": "onset", "offset_ms": -10},
    "scratch": {"q": ["record scratch", "vinyl scratch"], "dur": (0.15, 1.2), "earshot": ["pro_glitch", "glitch/burst"], "align": "onset", "offset_ms": -10},
    "shutter": {"q": ["camera shutter"], "dur": (0.08, 0.6), "earshot": ["shutter/snap", "shutter"], "align": "onset", "offset_ms": -11},
    "drone": {"q": ["drone ambience dark", "dark ambience"], "dur": (8.0, 120.0), "earshot": [], "align": "onset", "offset_ms": 0},
}
PACK = re.compile(r"\b(pack|collection|set|kit|loop|stings|hits|impacts|whooshes|risers|x ?\d+|\d+ \w+s)\b", re.I)   # multi-sound files
OV = "https://api.openverse.org/v1/audio/"
DESCRIBE = {"whoosh": "a fast clean air whoosh passing by", "impact": "a deep cinematic impact hit with a low boom", "pop": "a short soft bubble pop",
            "ding": "a clean bright notification ding", "riser": "a tension riser building up", "click": "a short crisp interface click",
            "bass": "a deep sub bass drop", "sting": "a short dramatic suspense sting", "scratch": "a vinyl record scratch",
            "shutter": "a camera shutter click", "drone": "a dark low ambient drone"}
UA = {"User-Agent": "TITAN-editor/1.0 (local video editor; sfx fetch)"}


# ---------------- measuring ----------------
def pcm(path, sr=48000):
    import numpy as np
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True)
    return np.frombuffer(r.stdout, np.int16).astype("float32") / 32768.0


def measure(path):
    """Onset (first 1 ms frame within 30 dB of the max), peak (loudest 5 ms), audible end, attack, centroid: Earshot's definitions."""
    import numpy as np
    sr = 48000
    y = pcm(path, sr)
    if not len(y):
        return None
    hop = sr // 1000
    fr = y[: len(y) // hop * hop].reshape(-1, hop)
    db = 20 * np.log10(np.sqrt((fr ** 2).mean(1)) + 1e-9)
    mx = db.max()
    onset = int(np.argmax(db > mx - 30))
    k = 5
    e5 = np.convolve(10 ** (db / 10), np.ones(k) / k, mode="same")
    peak = int(np.argmax(e5))
    alive = np.where(db > mx - 50)[0]
    end = int(alive[-1]) if len(alive) else len(db)
    e25 = 10 * np.log10(np.convolve(10 ** (db / 10), np.ones(25) / 25, mode="same") + 1e-12)
    hits, low = 0, True                       # separate strong events: within 6 dB of the max, with >= 10 dB dips between them
    for v in e25:
        if low and v > e25.max() - 6:
            hits += 1; low = False
        elif not low and v < e25.max() - 16:
            low = True
    spec = np.abs(np.fft.rfft(y[: sr * 2] * np.hanning(min(len(y), sr * 2))))
    f = np.fft.rfftfreq(min(len(y), sr * 2), 1 / sr)
    return {"dur_s": round(len(y) / sr, 3), "onset_s": onset / 1000, "peak_s": peak / 1000, "end_s": end / 1000,
            "attack_ms": peak - onset, "centroid_hz": int((spec * f).sum() / (spec.sum() + 1e-9)), "peak_dbfs": round(float(20 * np.log10(np.abs(y).max() + 1e-9)), 1), "events": hits}


def meta_of(path, cache_dir):
    key = hashlib.sha1(f"{Path(path).resolve()}|{Path(path).stat().st_mtime}".encode()).hexdigest()[:16]
    p = Path(cache_dir) / f"sfxmeta_{key}.json"
    m = rjson(p)
    if m is None:
        m = measure(path) or {}
        wjson(p, m)
    return m


def place(kind, cue_s, m):
    """File start time so the sound's onset/peak lands where the role wants it relative to the cue."""
    spec = KINDS.get(kind, {"align": "onset", "offset_ms": -10})
    point = (m or {}).get("peak_s" if spec["align"] == "peak" else "onset_s", 0.0) or 0.0
    return cue_s + spec["offset_ms"] / 1000.0 - point


# ---------------- choosing a file ----------------
def library_files(kind):
    d = LIB / kind
    return sorted(f for f in d.iterdir() if f.suffix.lower() in (".wav", ".mp3", ".ogg", ".flac", ".aif", ".aiff")) if d.is_dir() else []


def earshot_render(kind, cache, seed=0, dur=None, apex=None):
    exe = shutil.which("earshot")
    if not exe or not KINDS.get(kind, {}).get("earshot"):
        return None
    ids = list(KINDS[kind]["earshot"])
    try:   # resolve bare categories to real members once (`earshot sfx list` prints ids as <category>/<member>)
        lst = cache / "earshot_ids.txt"
        if not lst.exists():
            lst.write_text(subprocess.run([exe, "sfx", "list"], capture_output=True, text=True, timeout=120).stdout, encoding="utf-8")
        known = set(re.findall(r"\b([a-z0-9_]+/[a-z0-9_]+)\b", lst.read_text(encoding="utf-8")))
        ids = [i if "/" in i else next((k for k in sorted(known) if k.startswith(i + "/")), i) for i in ids]
        ids = [i for i in ids if not known or i in known] or ids
    except Exception:
        pass
    for sid in ids:
        out = cache / f"earshot_{sid.replace('/', '_')}_{seed}_{dur}_{apex}.wav"
        if out.exists():
            return out
        args = [exe, "sfx", "render", sid, "-o", str(out)] + (["--seed", str(seed)] if seed else []) + \
               (["--dur", f"{dur:.3f}"] if dur else []) + (["--apex", f"{apex:.3f}"] if apex else [])
        r = subprocess.run(args, capture_output=True, text=True, timeout=180)
        if r.returncode == 0 and out.exists():
            return out
        log(f"earshot: {sid} failed ({(r.stderr or '').strip()[:120]})")
    return None


def pick(kind, cue_s, cache, synth):
    """Return (file, source). Library takes rotate by cue time (stable across re-renders); earshot takes vary by seed."""
    files = library_files(kind)
    if files:
        i = int(hashlib.md5(f"{kind}{cue_s:.2f}".encode()).hexdigest(), 16) % len(files)
        return files[i], "library"
    seed = int(cue_s * 10) % 6
    f = earshot_render(kind, cache, seed=seed)
    if f:
        return f, "earshot"
    return synth(kind, cache), "synth"


# ---------------- fetching (Openverse) ----------------
def ov_search(q, licences, page_size=20):
    params = {"q": q, "page_size": page_size, "license": ",".join(licences), "license_type": "commercial", "mature": "false"}
    req = urllib.request.Request(OV + "?" + urllib.parse.urlencode(params), headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8")).get("results", [])


def trim_norm(src, out, max_s):
    """Cut leading silence (< -50 dBFS) and anything past max_s, fade the tail, peak-normalise to -1 dBFS, 48 kHz stereo wav."""
    ffmpeg(["-i", str(src), "-af", f"silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.005,atrim=0:{max_s:.2f},"
            f"afade=t=out:st={max(0.0, max_s - 0.08):.2f}:d=0.08,loudnorm=I=-16:TP=-1:LRA=11:linear=true,aresample=48000", "-ac", "2", str(out)])


def fetch(kind, n=6, query=None, allow_by=True, dry=False):
    spec = KINDS.get(kind)
    if not spec:
        raise SystemExit(f"unknown kind {kind}; kinds: {', '.join(KINDS)}")
    lic = ["cc0", "pdm"] + (["by"] if allow_by else [])
    lo, hi = spec["dur"]
    seen, cands = set(), []
    for q in ([query] if query else spec["q"]):
        for r in ov_search(q, lic):
            d = (r.get("duration") or 0) / 1000.0
            if r["id"] in seen or not r.get("url") or not (lo <= d <= hi * 3):
                continue
            if any(w in (r.get("title") or "").lower() for w in spec.get("avoid", [])) or PACK.search(r.get("title") or ""):
                continue
            seen.add(r["id"]); cands.append(r)
    log(f"sfx-fetch {kind}: {len(cands)} Openverse candidates ({'/'.join(lic)}, commercial use)")
    if dry:
        return cands
    d = LIB / kind
    d.mkdir(parents=True, exist_ok=True)
    tmp = d / "_tmp"
    tmp.mkdir(exist_ok=True)
    credits = rjson(LIB / "credits.json", {})
    kept = []
    for r in cands:
        if len(kept) >= n:
            break
        raw = tmp / f"{r['id']}.{r.get('filetype') or 'mp3'}"
        try:
            req = urllib.request.Request(r["url"], headers=UA)
            raw.write_bytes(urllib.request.urlopen(req, timeout=60).read())
            out = d / f"ov_{re.sub(r'[^a-z0-9]+', '_', r['title'].lower())[:40]}_{r['id'][:8]}.wav"
            trim_norm(raw, out, hi)
            m = measure(out)
            ok = m and lo * 0.6 <= (m["end_s"] - m["onset_s"]) <= hi * 1.2 and m["peak_dbfs"] > -40
            if kind in ("pop", "click", "impact", "bass", "ding") and m and m["attack_ms"] > 120:
                ok = False      # a "hit" that takes >120 ms to arrive reads late on a cut
            if m and kind not in ("riser", "drone", "scratch") and m.get("events", 1) > 1:
                ok = False      # two or more separate hits in one file: a stutter on one cut
            if m and spec.get("centroid_max") and m["centroid_hz"] > spec["centroid_max"]:
                ok = False      # too bright for the role (a "boom" that is really a glass clink)
            if not ok:
                out.unlink(missing_ok=True); continue
            credits[out.name] = {"title": r["title"], "creator": r.get("creator"), "licence": r["license"], "licence_version": r.get("license_version"),
                                 "licence_url": r.get("license_url"), "source": r.get("source"), "page": r.get("foreign_landing_url"), "kind": kind,
                                 "attribution": r.get("attribution"), "measured": m}
            kept.append(out)
        except Exception as e:
            log(f"  skip {r.get('title')}: {str(e)[:100]}")
        finally:
            raw.unlink(missing_ok=True)
    shutil.rmtree(tmp, ignore_errors=True)
    if len(kept) > 1 and shutil.which("earshot"):        # Earshot listens (CLAP): order the takes by how well they fit the role
        r = subprocess.run(["earshot", "rank", DESCRIBE.get(kind, kind)] + [str(k) for k in kept], capture_output=True, text=True, timeout=600)
        order = sorted(kept, key=lambda k: (r.stdout.find(k.name) if k.name in r.stdout else 1e9))
        for i, k in enumerate(order):
            credits[k.name]["earshot_rank"] = i + 1
        log("  earshot rank: " + ", ".join(k.name for k in order))
    wjson(LIB / "credits.json", credits)
    write_credits(credits)
    log(f"  kept {len(kept)} -> {d}")
    return kept


def write_credits(credits):
    rows = ["# SFX credits", "", "Sounds fetched from Openverse (mostly Freesound). CC0/PDM need no credit; **CC BY needs the credit line in the post caption or description.**",
            "", "| File | Kind | Licence | Credit |", "|---|---|---|---|"]
    for f, c in sorted(credits.items()):
        rows.append(f"| {f} | {c['kind']} | {c['licence']} {c.get('licence_version') or ''} | {c.get('attribution') or c.get('title')} |")
    (LIB / "CREDITS.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def credits_for(files):
    """Credit lines owed for the library files actually used in a render (CC BY only)."""
    c = rjson(LIB / "credits.json", {})
    return sorted({c[Path(f).name]["attribution"] for f in files if Path(f).name in c and c[Path(f).name]["licence"] == "by" and c[Path(f).name].get("attribution")})


def cmd_sfx(a):
    if a.action == "list":
        for k in KINDS:
            fs = library_files(k)
            print(f"{k:8s} library {len(fs):2d}   earshot {'yes' if shutil.which('earshot') and KINDS[k]['earshot'] else 'no '}   align {KINDS[k]['align']} {KINDS[k]['offset_ms']:+d} ms")
        return 0
    kinds = list(KINDS) if a.kind == "all" else [a.kind]
    for k in kinds:
        if k == "drone" and a.kind == "all":
            continue
        fetch(k, a.n, a.query, not a.cc0_only)
    return 0
