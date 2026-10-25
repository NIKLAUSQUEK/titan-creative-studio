"""Extra QC checks + handoff exports (from the 2026-10-25 reference-video review):
script coverage / leaked retakes, face occlusion by overlays, asset attribution manifest, CMX3600 EDL export."""
import csv, re
from pathlib import Path

from .common import REPO, log

_norm = lambda t: re.sub(r"[^\w']", "", t.lower())


# ---------------- script coverage + leaked retakes ----------------
def repeated_runs(words, n=6):
    """Word runs of length n that occur twice in the cut = a retake that survived (returns [(text, t_first, t_second)])."""
    toks = [(_norm(w["w"]), w["t0"]) for w in words if _norm(w["w"])]
    seen, hits = {}, []
    for i in range(len(toks) - n + 1):
        key = " ".join(t for t, _ in toks[i:i + n])
        if key in seen and toks[i][1] - seen[key] > 1.0:
            if not hits or toks[i][1] - hits[-1][2] > 2.0:
                hits.append((key, round(seen[key], 2), round(toks[i][1], 2)))
        else:
            seen.setdefault(key, toks[i][1])
    return hits


def script_coverage(lines, words, min_ratio=0.8):
    """Each approved script line must appear, in order, in the cut. Returns the lines that are missing or out of order."""
    toks = [_norm(w["w"]) for w in words if _norm(w["w"])]
    pos, missing = 0, []
    for line in lines:
        lt = [_norm(t) for t in line.split() if _norm(t)]
        if not lt:
            continue
        best, best_end = 0.0, None
        for i in range(pos, max(pos, len(toks) - len(lt)) + 1):
            window = toks[i:i + len(lt) + 2]
            got, j = 0, 0
            for t in lt:  # in-order match tolerant of small insertions
                while j < len(window) and window[j] != t:
                    j += 1
                if j < len(window):
                    got, j = got + 1, j + 1
            ratio = got / len(lt)
            if ratio > best:
                best, best_end = ratio, i + j
            if ratio == 1.0:
                break
        if best >= min_ratio:
            pos = best_end
        else:
            missing.append(line if len(line) <= 70 else line[:67] + "...")
    return missing


# ---------------- face occlusion ----------------
def _boxes_overlap(a, b):
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def face_occlusion(video, W, H, overlays, samples=12):
    """overlays: [(t0, t1, (x0, y0, x1, y1) in 0-1 frame units, label)]. Uses OpenCV's bundled Haar face detector.
    Returns (ok, detail); ok=None when OpenCV is not installed (check skipped)."""
    try:
        import cv2
    except Exception:
        return None, "skipped: pip install \"opencv-python-headless<5\" to enable face-occlusion QC"
    yunet = REPO / "assets" / "models" / "face_detection_yunet_2023mar.onnx"
    if hasattr(cv2, "CascadeClassifier"):  # OpenCV 4.x ships the Haar model
        haar = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        detect = lambda img, g: [tuple(f) for f in haar.detectMultiScale(g, scaleFactor=1.1, minNeighbors=5, minSize=(max(24, g.shape[1] // 12),) * 2)]
    elif hasattr(cv2, "FaceDetectorYN") and yunet.exists():  # OpenCV 5: YuNet (model from the opencv_zoo repo)
        yn = cv2.FaceDetectorYN.create(str(yunet), "", (320, 320), 0.8)
        def detect(img, g):
            yn.setInputSize((img.shape[1], img.shape[0]))
            _, faces = yn.detect(img)
            return [tuple(int(v) for v in f[:4]) for f in (faces if faces is not None else [])]
    else:
        return None, "skipped: OpenCV 5 has no bundled face model - pip install \"opencv-python-headless<5\" or put face_detection_yunet_2023mar.onnx in assets/models/"
    cap = cv2.VideoCapture(str(video))
    hits = []
    times = sorted({round(t0 + (t1 - t0) * k / 3, 2) for t0, t1, _, _ in overlays for k in (0, 1, 2)})[: samples * 3]
    for t in times:
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
        ok, frame = cap.read()
        if not ok:
            continue
        g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fh, fw = g.shape
        for (x, y, w, h) in detect(frame, g):
            fb = (x / fw, y / fh, (x + w) / fw, (y + h) / fh)
            for t0, t1, box, label in overlays:
                if t0 <= t <= t1 and _boxes_overlap(fb, box):
                    hits.append(f"{label} over face at {t:.1f}s")
    cap.release()
    hits = sorted(set(hits))
    return (not hits), ("; ".join(hits[:6]) if hits else f"{len(times)} frames checked")


def text_overlays(r, starts, caption_words, total):
    """Approximate on-screen boxes (0-1 units) for hook/title text and caption bands."""
    st, out = r["style"], []
    cap = st.get("captions", {})
    if cap.get("enabled", True) and caption_words:
        y, s = cap.get("position_y", 0.7), cap.get("size", 0.042)
        out.append((caption_words[0]["t0"], caption_words[-1]["t1"], (0.08, y - s * 1.4, 0.92, y + s * 1.4), "captions"))
    ht = st.get("hook_text", {})
    for t in r.get("texts", []):
        if t["type"] in ("hook", "title"):
            a = t.get("anchor", {})
            t0 = float(a["at"]) if "at" in a else starts.get(a.get("item"), 0) + float(a.get("offset", 0))
            y, s = ht.get("position_y", 0.2), ht.get("size", 0.05)
            out.append((t0, min(total, t0 + float(t.get("dur", 2.6))), (0.06, y - s * 1.6, 0.94, y + s * 1.6), f"{t['type']} text"))
    return out


# ---------------- attribution manifest ----------------
def _licence_rows():
    f = REPO / "assets" / "licences.csv"  # columns: path,source_url,licence,scope,attribution
    if not f.exists():
        return {}
    with f.open(encoding="utf-8") as fh:
        return {Path(row["path"]).name.lower(): row for row in csv.DictReader(fh)}


def attribution_manifest(r, out_md):
    """Every third-party asset in the edit with source, licence, platform scope and credit line → ATTRIBUTION.md (feeds /publish)."""
    rows, unknown = _licence_rows(), []
    assets = []
    m = r["audio"].get("music") or {}
    if m.get("path"):
        assets.append(("music", m["path"], m.get("licence")))
    for b in r.get("broll", []):
        assets.append(("b-roll", b["path"], None))
    for s in r["audio"].get("sfx", []):
        if s.get("file"):
            assets.append(("sfx", s["file"], None))
    L = ["# Asset attribution", "", "Source of truth: `assets/licences.csv` (path,source_url,licence,scope,attribution). Own footage = licence `original`.", "",
         "| type | file | licence | scope | source | credit line |", "|---|---|---|---|---|---|"]
    for kind, path, lic in assets:
        row = rows.get(Path(path).name.lower(), {})
        lic = row.get("licence") or lic or ""
        if not lic:
            unknown.append(Path(path).name)
        L.append(f"| {kind} | `{Path(path).name}` | {lic or '**unknown**'} | {row.get('scope', '')} | {row.get('source_url', '')} | {row.get('attribution', '')} |")
    credits = [rows[k]["attribution"] for k in {Path(p).name.lower() for _, p, _ in assets} if k in rows and rows[k].get("attribution")]
    L += ["", "## Credits for the description", *(f"- {c}" for c in credits or ["(none required)"])]
    Path(out_md).write_text("\n".join(L) + "\n", encoding="utf-8")
    return unknown


# ---------------- EDL export (human editor handoff) ----------------
def _tc(sec, fps):
    f = int(round(sec * fps))
    return f"{f // (3600 * fps):02d}:{f // (60 * fps) % 60:02d}:{f // fps % 60:02d}:{f % fps:02d}"


def export_edl(r, clips, out, fps=30):
    """CMX3600 EDL of the A-roll cut (items) + B-roll as V2 events, for Premiere/Resolve finishing. Source files are named in comments."""
    L = [f"TITLE: {r.get('brand') or 'titan'} edit v{r['version']}", "FCM: NON-DROP FRAME", ""]
    rec, n = 0.0, 0
    starts = {}
    for it in r["items"]:
        c = clips[it["clip"]]
        dur = (it["out"] - it["in"]) / it.get("speed", 1)
        starts[it["id"]] = rec
        n += 1
        reel = re.sub(r"\W", "", c["id"])[:8].upper() or "AX"
        L += [f"{n:03d}  {reel:<8} AA/V  C        {_tc(it['in'], fps)} {_tc(it['out'], fps)} {_tc(rec, fps)} {_tc(rec + dur, fps)}",
              f"* FROM CLIP NAME: {Path(c['meta'].get('path', c['id'])).name}", ""]
        if it.get("speed", 1) != 1:
            L.insert(-1, f"M2   {reel:<8} {it['speed'] * fps:05.1f} {_tc(it['in'], fps)}")
        rec += dur
    for b in r.get("broll", []):
        a = b.get("anchor", {})
        t0 = float(a["at"]) if "at" in a else starts.get(a.get("item"), 0) + float(a.get("offset", 0))
        n += 1
        L += [f"{n:03d}  BROLL    V     C        {_tc(b.get('src_in', 0), fps)} {_tc(b.get('src_in', 0) + b['dur'], fps)} {_tc(t0, fps)} {_tc(t0 + b['dur'], fps)}",
              f"* FROM CLIP NAME: {Path(b['path']).name}", "* TRACK: V2", ""]
    Path(out).write_text("\n".join(L) + "\n", encoding="utf-8")
    log(f"EDL -> {out} ({n} events; captions/graphics stay in the burned render)")
    return out
