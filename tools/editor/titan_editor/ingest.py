"""INGEST (local, free): word timestamps, silences, fillers, scene cuts, best takes, hook shortlist, contact sheets.

Output per clip: <edit>/ingest/<clip_id>/{meta.json, words.json, analysis.json, sheet.jpg}
Project level:   <edit>/ingest/index.json + summary.md (the compact text Claude reads instead of raw transcripts).
"""
import difflib, json, re, shutil
from pathlib import Path

from .common import studio, VIDEO, AUDIO, cb, ffmpeg, log, probe, rjson, run, slug, wjson

HARD_FILLERS = {"um", "umm", "uh", "uhh", "erm", "er", "ah", "hmm", "mm", "eh"}
SOFT_FILLERS = {"like", "basically", "actually", "literally", "so", "right", "okay", "lah", "leh", "lor"}
SOFT_PHRASES = [("you", "know"), ("i", "mean"), ("kind", "of"), ("sort", "of")]
THROAT = re.compile(r"\b(hey guys|hi guys|what'?s up guys|welcome back|in (this|today'?s) video|today i (want|wanna|'?m going|am going) to (talk|share|tell)|so today|let me (just )?start|before we (start|begin))\b", re.I)
HOOK_PATTERNS = [
    ("contrarian", r"\b(stop|don'?t|never|lie|lies|myth|wrong|mistake|nobody|no one|most (people|men|guys)|truth|actually isn'?t|isn'?t)\b"),
    ("confession", r"\b(i'?ve never|i never told|nobody knows|i used to|i was (so|too)|i lost|i failed)\b"),
    ("curiosity", r"\b(what happens|here'?s (why|what|the)|the reason|secret|nobody tells|why (you|your|most))\b"),
    ("number", r"(\b\d+\b|\b(one|two|three|five|ten) (in|out of|things|reasons|ways|mistakes)\b)"),
    ("outcome-twist", r"\b(but|then|anyway|until)\b.*\b(left|lost|changed|realised|realized)\b"),
]
_WHISPER = {}


def whisper(model_name, device):
    key = (model_name, device)
    if key not in _WHISPER:
        from faster_whisper import WhisperModel
        if device == "auto":
            device = "cuda" if shutil.which("nvidia-smi") else "cpu"
        log(f"loading whisper {model_name} on {device}")
        _WHISPER[key] = WhisperModel(model_name, device=device, compute_type="float16" if device == "cuda" else "int8")
    return _WHISPER[key]


def load_audio(src, d):
    """16 kHz mono float32 via ffmpeg -> wav -> numpy (avoids the PyAV clash, ledger 2026-10-10)."""
    import wave, numpy as np
    wav = d / "audio16k.wav"
    ffmpeg(["-i", src, "-vn", "-ac", "1", "-ar", "16000", wav], check=False)
    if not wav.exists():
        return None
    try:
        with wave.open(str(wav), "rb") as w:
            return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768.0
    finally:
        wav.unlink(missing_ok=True)


def rms_db(audio, hop=0.05, sr=16000):
    import numpy as np
    n = int(hop * sr)
    if audio is None or len(audio) < n:
        return np.zeros(0)
    frames = audio[: len(audio) // n * n].reshape(-1, n)
    return 20 * np.log10(np.sqrt((frames ** 2).mean(axis=1)) + 1e-6)


def transcribe_words(audio, model_name, device, language):
    segs, info = whisper(model_name, device).transcribe(audio, vad_filter=True, word_timestamps=True, language=language or None, beam_size=5)
    words = []
    for s in segs:
        for w in s.words or []:
            t = w.word.strip()
            if t:
                words.append({"w": t, "t0": round(w.start, 3), "t1": round(w.end, 3), "p": round(w.probability, 3)})
    return words, info.language


def norm(w):
    return re.sub(r"[^\w']", "", w.lower())


def mark_fillers(words):
    for i, w in enumerate(words):
        n = norm(w["w"])
        if n in HARD_FILLERS:
            w["filler"] = "hard"
        elif n in SOFT_FILLERS:
            w["filler"] = "soft"
        elif i + 1 < len(words) and (n, norm(words[i + 1]["w"])) in SOFT_PHRASES:
            w["filler"] = words[i + 1]["filler"] = "soft"
    return words


def sentences(words, gap=0.7):
    out, cur = [], []
    for i, w in enumerate(words):
        if cur and w["t0"] - cur[-1]["t1"] > gap:
            out.append(cur); cur = []
        cur.append(w)
        if re.search(r"[.?!]$", w["w"]):
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    res = []
    for k, ws in enumerate(out):
        text = " ".join(x["w"] for x in ws)
        res.append({"i": k, "t0": ws[0]["t0"], "t1": ws[-1]["t1"], "text": text,
                    "n": len(ws), "fillers": sum(1 for x in ws if x.get("filler") == "hard"),
                    "p": round(sum(x["p"] for x in ws) / len(ws), 3),
                    "key": " ".join(norm(x["w"]) for x in ws if not x.get("filler") and norm(x["w"]))})
    return res


def same_line(a, b):
    """Is b a retake of a? (similar text, same opening, or a is an abandoned start of b)."""
    ka, kb = a["key"].split(), b["key"].split()
    if not ka or not kb:
        return False
    if difflib.SequenceMatcher(None, ka, kb).ratio() > 0.6:
        return True
    k = min(4, len(ka), len(kb))
    if k >= 3 and ka[:k] == kb[:k]:
        return True
    return len(ka) >= 2 and len(ka) < len(kb) and kb[: len(ka)] == ka


def group_takes(sents):
    groups, i = [], 0
    while i < len(sents):
        g = [sents[i]]
        j = i + 1
        while j < len(sents) and j <= i + 3 and any(same_line(x, sents[j]) for x in g):
            g.append(sents[j]); j += 1
        groups.append(g); i = j
    takes = []
    for gi, g in enumerate(groups):
        mx = max(s["n"] for s in g)
        full = [s for s in g if s["n"] >= 0.8 * mx and s["p"] >= 0.45] or g
        best = sorted(full, key=lambda s: (s["fillers"], -s["i"]))[0] if len(full) > 1 and full[-1]["fillers"] > full[0]["fillers"] + 1 else full[-1]
        for s in g:
            s["take_group"] = gi
            s["best"] = s is best
        takes.append({"group": gi, "best": best["i"], "takes": [s["i"] for s in g]})
    return takes


def silences_from_rms(db, hop=0.05, thresh=None, min_len=0.35):
    import numpy as np
    if not len(db):
        return []
    thresh = thresh if thresh is not None else max(-45.0, float(np.percentile(db, 90)) - 30)
    quiet = db < thresh
    out, start = [], None
    for k, q in enumerate(list(quiet) + [False]):
        if q and start is None:
            start = k
        elif not q and start is not None:
            if (k - start) * hop >= min_len:
                out.append({"t0": round(start * hop, 2), "t1": round(k * hop, 2)})
            start = None
    return out


def scene_cuts(src):
    r = run(["ffmpeg", "-hide_banner", "-i", str(src), "-vf", "scale=320:-2,select='gt(scene,0.3)',showinfo", "-an", "-f", "null", "-"])
    return [round(float(m), 2) for m in re.findall(r"pts_time:([\d.]+)", r.stderr)]


def hook_score(s, db, hop=0.05):
    import numpy as np
    text, sc, why = s["text"].lower(), 0.0, []
    if 5 <= s["n"] <= 18:
        sc += 1; why.append("tight length")
    elif 3 <= s["n"] <= 25:
        sc += 0.3
    formula = None
    for name, pat in HOOK_PATTERNS:
        if re.search(pat, text):
            sc += 1; why.append(name); formula = formula or name
    if text.rstrip().endswith("?"):
        sc += 0.6; why.append("question"); formula = formula or "question"
    if re.search(r"\byou(r)?\b", text):
        sc += 0.3; why.append("talks to viewer")
    if re.match(r"(and|but|so|because|which|or)\b", text):
        sc -= 0.6; why.append("starts mid-thought")
    sc -= 0.3 * s["fillers"]
    if len(db):
        a, b = int(s["t0"] / hop), max(int(s["t1"] / hop), int(s["t0"] / hop) + 1)
        seg = db[a:b]
        if len(seg):
            z = (float(seg.mean()) - float(np.median(db))) / (float(db.std()) + 1e-6)
            sc += 0.5 * max(-1.0, min(2.0, z))
            if z > 0.5:
                why.append("high energy")
    return round(sc, 2), formula or "statement", why


def ingest_clip(src, out_root, model, device, language, force=False):
    src = Path(src)
    cid = slug(src.stem, 24) + "-" + cb.item_id(src)[:6]
    d = out_root / cid
    if (d / "analysis.json").exists() and not force:
        return cid
    d.mkdir(parents=True, exist_ok=True)
    m = probe(src)
    m.update({"id": cid, "path": str(src.resolve()), "name": src.name})
    log(f"ingest {src.name} ({m.get('duration')} s)")
    if src.suffix.lower() in VIDEO:
        cb.contact_sheet(src, m.get("duration") or 0, d / "sheet.jpg")
    words, lang, db = [], None, []
    if m.get("has_audio"):
        audio = load_audio(src, d)
        if audio is not None and len(audio):
            db = rms_db(audio)
            words, lang = transcribe_words(audio, model, device, language)
    mark_fillers(words)
    sents = sentences(words)
    takes = group_takes(sents)
    for s in sents:
        s["hook_score"], s["formula"], s["why"] = hook_score(s, db)
        if THROAT.search(s["text"]):
            s["throat_clearing"] = True; s["hook_score"] -= 1.5; s["why"].append("throat-clearing")
    gaps = [{"t0": a["t1"], "t1": b["t0"]} for a, b in zip(words, words[1:]) if b["t0"] - a["t1"] > 0.35]
    an = {"language": lang, "sentences": sents, "takes": takes, "word_gaps": gaps,
          "silences": silences_from_rms(db), "scenes": scene_cuts(src) if src.suffix.lower() in VIDEO else [],
          "fillers": {"hard": sum(1 for w in words if w.get("filler") == "hard"), "soft": sum(1 for w in words if w.get("filler") == "soft")},
          "speech_s": round(sum(w["t1"] - w["t0"] for w in words), 2)}
    wjson(d / "meta.json", m)
    wjson(d / "words.json", words)
    wjson(d / "analysis.json", an)
    return cid


def brand_language():
    """Speech language from the active brand's edit-brand block ("language": "en"). Whisper auto-detect misreads
    Singapore English as Malay (overnight genre research 2026-10-25), so brands pin it; None = auto-detect."""
    try:
        from .presets import brand_guide
        return (brand_guide(studio("active_brand"))[0] or {}).get("language")
    except Exception:
        return None


def cmd_ingest(a, edit_dir):
    root = edit_dir / "ingest"
    root.mkdir(parents=True, exist_ok=True)
    files = []
    for s in a.footage:
        p = Path(s)
        if p.is_dir():
            files += [f for f in sorted(p.rglob("*")) if f.suffix.lower() in VIDEO | AUDIO and not f.name.startswith(".")]
        elif p.exists():
            files.append(p)
        else:
            log(f"not found: {s}")
    idx = rjson(root / "index.json", {"clips": []})
    known = {c["id"] for c in idx["clips"]}
    for f in files:
        cid = ingest_clip(f, root, a.whisper_model, a.device, a.language or brand_language(), a.force)
        if cid not in known:
            idx["clips"].append({"id": cid, "path": str(f.resolve())}); known.add(cid)
    wjson(root / "index.json", idx)
    write_summary(edit_dir)
    log(f"ingest done: {len(idx['clips'])} clip(s) -> {root / 'summary.md'}")


def load_clips(edit_dir):
    root = edit_dir / "ingest"
    out = []
    for c in rjson(root / "index.json", {"clips": []})["clips"]:
        d = root / c["id"]
        if (d / "analysis.json").exists():
            out.append({"id": c["id"], "dir": d, "meta": rjson(d / "meta.json"), "an": rjson(d / "analysis.json"), "words": rjson(d / "words.json", [])})
    return out


def hook_shortlist(clips, k=8):
    cands = []
    for c in clips:
        for s in c["an"]["sentences"]:
            if s.get("best"):
                cands.append({"clip": c["id"], "t0": s["t0"], "t1": s["t1"], "text": s["text"], "score": s["hook_score"], "formula": s["formula"], "why": s["why"]})
    return sorted(cands, key=lambda x: -x["score"])[:k]


def write_summary(edit_dir):
    """Compact, token-cheap view of all footage for Claude (kept lines only, dropped takes as one line each)."""
    clips = load_clips(edit_dir)
    L = ["# Footage summary (auto, from ingest)", ""]
    for c in clips:
        m, an = c["meta"], c["an"]
        sil = sum(s["t1"] - s["t0"] for s in an["silences"])
        L.append(f"## {c['id']}  ({m['name']}, {m.get('duration')} s, {m.get('width')}x{m.get('height')}, lang={an['language']}, "
                 f"speech {an['speech_s']} s, silence {sil:.1f} s, fillers {an['fillers']['hard']} hard/{an['fillers']['soft']} soft, scene cuts {len(an['scenes'])})")
        L.append(f"contact sheet: ingest/{c['id']}/sheet.jpg")
        for s in an["sentences"]:
            tag = ("" if s.get("best") else "  [dropped retake]") + ("  [throat-clearing]" if s.get("throat_clearing") else "")
            if s.get("best") or len(an["sentences"]) < 40:
                L.append(f"- [{s['t0']:.2f}-{s['t1']:.2f}] {s['text']}{tag}")
        L.append("")
    L.append("## Hook shortlist (local scoring: length, hook formula, energy, standalone)")
    for h in hook_shortlist(clips):
        L.append(f"- {h['score']:>4}  {h['clip']} [{h['t0']:.2f}-{h['t1']:.2f}] ({h['formula']}) \"{h['text']}\"")
    (edit_dir / "ingest" / "summary.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return clips
