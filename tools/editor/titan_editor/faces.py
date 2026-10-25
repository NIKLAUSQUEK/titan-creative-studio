"""Who is in the footage: local face detection + recognition (OpenCV YuNet + SFace, Apache-2.0 models, CPU, no API).

  editor.py people enroll klaus "D:\\Photos\\me" --consent self     # 5-20 clear photos of the person
  editor.py people list | people scan                               # scan = add faces to clips indexed before enrolment
  editor.py broll-search "@klaus walking outdoors"                  # only clips where Klaus is recognised

Faces found during `broll-index` are stored per clip (embeddings only, never uploaded). Enrolment builds a reference
embedding per person; matching is a cosine check at search time, so enrolling later needs no re-index of CLIP.
Unknown faces are counted per clip so QC can warn about people who may not have consented.
"""
import json, tempfile, time, urllib.request
from pathlib import Path

from .common import IMAGE, VIDEO, ffmpeg, log, probe

MODELS = {"yunet": ("face_detection_yunet_2023mar.onnx", "https://huggingface.co/opencv/face_detection_yunet/resolve/main/face_detection_yunet_2023mar.onnx"),
          "sface": ("face_recognition_sface_2021dec.onnx", "https://huggingface.co/opencv/face_recognition_sface/resolve/main/face_recognition_sface_2021dec.onnx")}
MATCH = 0.42      # SFace cosine; OpenCV's suggested threshold is 0.363, we stay a bit stricter to avoid false "me"
_FR = {}


def available():
    try:
        import cv2
        return hasattr(cv2, "FaceDetectorYN")
    except Exception:
        return False


def models(index_dir):
    d = Path(index_dir) / "models"
    d.mkdir(parents=True, exist_ok=True)
    out = {}
    for k, (name, url) in MODELS.items():
        p = d / name
        if not p.exists():
            log(f"downloading face model {name} (one-time)")
            urllib.request.urlretrieve(url, p)
        out[k] = str(p)
    return out


def engine(index_dir):
    if "det" not in _FR:
        import cv2
        m = models(index_dir)
        _FR["det"] = cv2.FaceDetectorYN.create(m["yunet"], "", (320, 320), 0.8, 0.3, 50)
        _FR["rec"] = cv2.FaceRecognizerSF.create(m["sface"], "")
        _FR["cv2"] = cv2
    return _FR


def faces_in_image(path, index_dir, min_px=28):
    """[(embedding float32[128], box[x,y,w,h], score)] for each face big enough to identify."""
    import numpy as np
    E = engine(index_dir); cv2 = E["cv2"]
    img = cv2.imread(str(path))
    if img is None:
        return []
    h, w = img.shape[:2]
    if max(h, w) > 1280:
        k = 1280 / max(h, w); img = cv2.resize(img, (int(w * k), int(h * k))); h, w = img.shape[:2]
    E["det"].setInputSize((w, h))
    _, dets = E["det"].detect(img)
    out = []
    for d in (dets if dets is not None else []):
        if min(d[2], d[3]) < min_px:
            continue
        aligned = E["rec"].alignCrop(img, d)
        f = E["rec"].feature(aligned).flatten().astype(np.float32)
        out.append((f / (np.linalg.norm(f) + 1e-9), [int(x) for x in d[:4]], float(d[-1])))
    return out


def ensure_tables(con):
    con.executescript("""
      create table if not exists faces(clip_id text, k int, t real, emb blob, box text);
      create index if not exists faces_clip on faces(clip_id);
      create table if not exists people(name text primary key, emb blob, n int, consent text, added text);
    """)


def store_faces(con, clip_id, frames, index_dir):
    """frames: [(t, jpg path)]; replaces this clip's faces."""
    con.execute("delete from faces where clip_id=?", (clip_id,))
    n = 0
    for k, (t, p) in enumerate(frames):
        for emb, box, _ in faces_in_image(p, index_dir):
            con.execute("insert into faces values(?,?,?,?,?)", (clip_id, k, t, emb.astype("float16").tobytes(), json.dumps(box))); n += 1
    return n


def people(con):
    import numpy as np
    ensure_tables(con)
    return {r[0]: {"emb": np.frombuffer(r[1], np.float32), "n": r[2], "consent": r[3]} for r in con.execute("select name,emb,n,consent from people")}


def clip_people(con, ppl=None):
    """{clip_id: {"people": {name: best_sim}, "unknown": n_unknown_face_frames}}"""
    import numpy as np
    ensure_tables(con)
    ppl = ppl if ppl is not None else people(con)
    names = list(ppl)
    P = np.stack([ppl[n]["emb"] for n in names]) if names else np.zeros((0, 128), np.float32)
    out = {}
    for cid, emb in con.execute("select clip_id, emb from faces"):
        e = np.frombuffer(emb, np.float16).astype(np.float32)
        rec = out.setdefault(cid, {"people": {}, "unknown": 0})
        sims = P @ e if len(P) else np.zeros(0)
        if len(sims) and sims.max() >= MATCH:
            n = names[int(sims.argmax())]
            rec["people"][n] = round(max(rec["people"].get(n, 0), float(sims.max())), 3)
        else:
            rec["unknown"] += 1
    return out


def cmd_people(a):
    from .broll import db_open, sample_frames
    import numpy as np
    con = db_open(a.index_dir)
    ensure_tables(con)
    if a.action == "list":
        cp = clip_people(con)
        for n, p in people(con).items():
            hits = sum(1 for v in cp.values() if n in v["people"])
            print(f"{n:16} photos={p['n']:3} consent={p['consent']:10} clips_with_face={hits}")
        return
    if a.action == "enroll":
        if not a.consent:
            raise SystemExit("Pass --consent self|written|verbal-recorded: only enrol people who agreed to be recognised in your footage.")
        src = Path(a.photos)
        files = [f for f in (src.rglob("*") if src.is_dir() else [src]) if f.suffix.lower() in IMAGE | VIDEO]
        embs = []
        with tempfile.TemporaryDirectory() as td:
            for f in files[:60]:
                imgs = [(0, f)] if f.suffix.lower() in IMAGE else sample_frames(f, probe(f).get("duration") or 0, 6, Path(td), "video", width=960)
                for _, p in imgs:
                    if Path(p).suffix.lower() in (".heic",):
                        continue
                    fs = faces_in_image(p, a.index_dir)
                    if len(fs) == 1:      # only single-face photos, so we know whose face it is
                        embs.append(fs[0][0])
        if len(embs) < 3:
            raise SystemExit(f"Only {len(embs)} usable single-face photos found in {src}; give 5-20 clear photos with just {a.name} in them.")
        E = np.stack(embs)
        mean = E.mean(0); mean /= np.linalg.norm(mean)
        keep = E[(E @ mean) > 0.3]           # drop outliers (wrong person, bad crops)
        mean = keep.mean(0); mean /= np.linalg.norm(mean)
        con.execute("insert or replace into people values(?,?,?,?,?)", (a.name.lower(), mean.astype(np.float32).tobytes(), len(keep), a.consent, time.strftime("%Y-%m-%d")))
        con.commit()
        log(f"enrolled {a.name.lower()} from {len(keep)}/{len(embs)} face photos (consent: {a.consent})")
        return
    if a.action == "scan":
        rows = con.execute("select id, path, kind, duration from clips where id not in (select distinct clip_id from faces)").fetchall()
        log(f"scanning {len(rows)} indexed clips for faces")
        for cid, path, kind, dur in rows:
            if not Path(path).exists():
                continue
            with tempfile.TemporaryDirectory() as td:
                fr = sample_frames(path, dur or 0, 4, Path(td), kind, width=960)
                store_faces(con, cid, fr, a.index_dir)
        con.commit()
        log("scan done; `people list` shows matches")
        return
    if a.action == "forget":
        con.execute("delete from people where name=?", (a.name.lower(),)); con.commit()
        log(f"removed {a.name.lower()} (face embeddings of clips stay; they are anonymous without a reference)")
