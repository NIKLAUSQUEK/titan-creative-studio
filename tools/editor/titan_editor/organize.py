"""ORGANIZE a big personal media library (10k+ photos and videos) with AI, locally and for free; Claude only names events.

Pipeline (each step incremental, safe to re-run; originals are NEVER moved, renamed or deleted):
  1. index    reuse the B-roll index (open_clip embeddings, sensitivity flags) for images + videos
  2. analyse  EXIF date/GPS/camera, sharpness, exposure, resolution, faces (YuNet) + face embeddings (SFace)
  3. classify CLIP zero-shot: category (headshot, speaking, meeting, working, screen, gym, clinic, food, product, event,
              travel, family, document, meme, pet, selfie), sensitive flags, brand fit
  4. people   cluster faces -> people_sheet.jpg -> `organize name <cluster> klaus` labels a whole cluster at once
  5. dedupe   near-duplicate bursts within an event -> one "best" pick per group (sharpness x exposure x resolution x faces)
  6. events   time gaps -> events; optional `--llm claude-cli` names each event from ONE contact sheet (cheap)
  7. report   REVIEW.html gallery (by category / event / person, flags, best picks) + catalog.csv
  8. apply    an organised COPY or hardlink tree (Category/YYYY-MM-DD event/file) and/or export best picks to the studio
              library (assets/library/index.csv) so carousels can use "lib:klaus speaking"

All local models: open_clip ViT-B-32 (already used for B-roll), OpenCV YuNet + SFace (assets/models/, ~39 MB, fetched once).
"""
import csv, hashlib, html, json, os, shutil, sqlite3, subprocess, tempfile, time, urllib.request
from pathlib import Path

from .common import REPO, ffmpeg, log, parse_json, probe

MODELS = REPO / "assets" / "models"
FACE_MODELS = {"face_detection_yunet_2023mar.onnx": "https://huggingface.co/opencv/face_detection_yunet/resolve/main/face_detection_yunet_2023mar.onnx",
               "face_recognition_sface_2021dec.onnx": "https://huggingface.co/opencv/face_recognition_sface/resolve/main/face_recognition_sface_2021dec.onnx"}
CATEGORIES = {  # folder name: CLIP prompts (an ensemble of "a photo of ..." phrasings beats one prompt zero-shot)
    "Headshots": ["a professional headshot portrait of one person looking at the camera", "a close-up portrait photo of a person's face and shoulders"],
    "Selfies": ["a casual selfie taken with a phone at arm's length", "a person taking a selfie with a smartphone"],
    "Speaking": ["a person speaking on stage at a conference with a microphone", "a presenter giving a talk in front of a projector screen"],
    "Meetings": ["people in a business meeting around a table", "a team discussing ideas at a whiteboard"],
    "Working": ["a person working on a laptop at a desk", "an office desk with a laptop and computer monitors"],
    "Screens": ["a screenshot of a computer or phone screen showing an app or dashboard", "a screen capture of a website, chart or chat"],
    "Gym": ["a person exercising or lifting weights in a gym", "a workout with barbells, dumbbells or fitness machines"],
    "Clinic": ["a physiotherapist treating a patient on a treatment table", "a therapist massaging or stretching a patient's back, knee or shoulder", "a medical rehabilitation session in a clinic"],
    "Food": ["a plate of food or a meal on a table", "a healthy meal, salad or breakfast bowl"],
    "Product": ["a product photo of a bottle, package, tub or supplement", "a protein shake or supplement container"],
    "Events": ["a crowd of people mingling at a networking event or party", "a group of people holding drinks and chatting at a reception", "an audience at an event"],
    "Travel": ["a landscape, beach or mountain scenery", "a city skyline or street scene while travelling"],
    "Family": ["young children playing outdoors in a park or playground", "a family photo with kids", "toddlers and small children"],
    "Documents": ["a photo of a document, receipt, invoice or ID card", "paperwork with printed text"],
    "Memes": ["a meme or social media post with large text", "an image with a funny caption"],
    "Pets": ["a photo of a pet dog or cat", "a dog or puppy"],
}
KIDS = ("a photo showing young children or babies", "a photo of adults only, no children")
SENSITIVE_CATS = {"Family": "minors/family", "Documents": "personal data", "Clinic": "patient (consent needed)"}
BRAND_FIT = {"Headshots": ["klaus", "titan-ai"], "Speaking": ["klaus", "titan-ai"], "Meetings": ["titan-ai"], "Working": ["titan-ai", "klaus"],
             "Screens": ["titan-ai"], "Gym": ["peachform", "power-protein", "klaus"], "Clinic": ["physio-spot", "heal360"],
             "Food": ["power-protein"], "Product": ["power-protein"], "Events": ["klaus", "titan-ai"], "Travel": ["klaus"], "Selfies": ["klaus"]}
SCHEMA = """
create table if not exists org(clip_id text primary key, taken text, taken_src text, gps text, camera text, sharp real, bright real,
  mp real, faces int, quality real, category text, cat_score real, cat2 text, sens text, brands text, people text,
  dup_group text, best int, event text, caption text, tags text, analysed_at text);
create table if not exists faces(clip_id text, k int, emb blob, box text, cluster int, primary key(clip_id, k));
create table if not exists people(cluster int primary key, name text, consent text, centroid blob);
create table if not exists events(event text primary key, name text, caption text, tags text, story text, brands text);
"""


# ---------------- helpers ----------------
def db(index_dir):
    from .broll import db_open
    con = db_open(index_dir)
    con.executescript(SCHEMA)
    if "centroid" not in [r[1] for r in con.execute("pragma table_info(people)")]:
        con.execute("alter table people add column centroid blob")
    return con


def face_models():
    MODELS.mkdir(parents=True, exist_ok=True)
    for name, url in FACE_MODELS.items():
        p = MODELS / name
        if not p.exists():
            log(f"downloading {name} (once) ...")
            urllib.request.urlretrieve(url, p)
    import cv2
    det = cv2.FaceDetectorYN.create(str(MODELS / "face_detection_yunet_2023mar.onnx"), "", (320, 320), 0.85, 0.3, 50)
    rec = cv2.FaceRecognizerSF.create(str(MODELS / "face_recognition_sface_2021dec.onnx"), "")
    return det, rec


def exif(path):
    """(taken ISO, source, gps 'lat,lon', camera) from EXIF; falls back to file time."""
    from PIL import Image, ExifTags
    taken, src, gps, cam = None, None, "", ""
    try:
        with Image.open(path) as im:
            ex = im.getexif()
            ifd = ex.get_ifd(0x8769) if hasattr(ex, "get_ifd") else {}
            dt = ifd.get(36867) or ex.get(306)
            if dt:
                taken, src = str(dt).replace(":", "-", 2).replace(" ", "T"), "exif"
            cam = " ".join(str(x) for x in (ex.get(271), ex.get(272)) if x).strip()
            g = ex.get_ifd(0x8825) if hasattr(ex, "get_ifd") else {}
            if g and 2 in g and 4 in g:
                def deg(v):
                    return float(v[0]) + float(v[1]) / 60 + float(v[2]) / 3600
                lat = deg(g[2]) * (-1 if g.get(1) == "S" else 1)
                lon = deg(g[4]) * (-1 if g.get(3) == "W" else 1)
                gps = f"{lat:.5f},{lon:.5f}"
    except Exception:
        pass
    return taken, src, gps, cam


def name_date(name):
    """Dates phones/apps put in file names: IMG_20240911_183012, PXL_20240911..., 2024-09-11 18.30.12, Screenshot 2024-09-11 at..."""
    import re
    m = re.search(r"(20\d{2}|19\d{2})[-_.]?(0[1-9]|1[0-2])[-_.]?(0[1-9]|[12]\d|3[01])(?:[ _T-]?([01]\d|2[0-3])[.:_-]?([0-5]\d)[.:_-]?([0-5]\d)?)?", name)
    if not m:
        return None, None
    y, mo, d, hh, mm, ss = m.groups()
    return f"{y}-{mo}-{d}T{hh or '12'}:{mm or '00'}:{ss or '00'}", "filename"


def video_time(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format_tags=creation_time", "-of", "default=nw=1:nk=1", str(path)],
                             capture_output=True, text=True, timeout=30).stdout.strip()
        return (out[:19], "metadata") if out else (None, None)
    except Exception:
        return None, None


def still(path, kind, dur, tmp):
    """A representative frame (middle of a video) as a BGR array for quality + faces."""
    import cv2
    if kind == "image":
        src = path
    else:
        src = Path(tmp) / "mid.jpg"
        ffmpeg(["-ss", f"{max(0, (dur or 0) / 2):.2f}", "-i", str(path), "-frames:v", 1, "-q:v", 3, src], check=False)
    img = cv2.imread(str(src))
    if img is None and kind == "image":  # HEIC/odd formats: let ffmpeg decode
        alt = Path(tmp) / "img.jpg"
        ffmpeg(["-i", str(path), "-frames:v", 1, alt], check=False)
        img = cv2.imread(str(alt))
    return img


def quality(img):
    import cv2
    h, w = img.shape[:2]
    k = 768 / max(h, w)
    small = cv2.resize(img, (int(w * k), int(h * k))) if k < 1 else img
    g = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    sharp = float(cv2.Laplacian(g, cv2.CV_64F).var())
    bright = float(g.mean())
    return sharp, bright, w * h / 1e6


def qscore(sharp, bright, mp, faces):
    """0..1: sharp, well exposed, decent resolution; a face helps (people content performs)."""
    import math
    s = min(1.0, math.log1p(sharp) / math.log1p(800))
    e = max(0.0, 1 - abs(bright - 125) / 125)
    r = min(1.0, mp / 8)
    return round(0.5 * s + 0.25 * e + 0.15 * r + (0.1 if faces else 0), 3)


# ---------------- 2. analyse ----------------
def analyse(index_dir, limit=None, force=False):
    import numpy as np, cv2
    con = db(index_dir)
    det, rec = face_models()
    rows = con.execute("select c.id, c.path, c.kind, c.duration, c.mtime from clips c left join org o on o.clip_id = c.id "
                       + ("" if force else "where o.clip_id is null")).fetchall()
    if limit:
        rows = rows[:limit]
    log(f"analyse: {len(rows)} items")
    for n, (cid, path, kind, dur, mtime) in enumerate(rows, 1):
        p = Path(path)
        if not p.exists():
            continue
        taken, src, gps, cam = exif(p) if kind == "image" else (*video_time(p), "", "")
        if not taken:
            taken, src = name_date(p.name)
        if not taken:  # file time is often the copy/download date, so it never defines an event (see events_and_dupes)
            taken, src = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(mtime or p.stat().st_mtime)), "file"
        with tempfile.TemporaryDirectory() as td:
            img = still(p, kind, dur, td)
        if img is None:
            continue
        sharp, bright, mp = quality(img)
        h, w = img.shape[:2]
        k = min(1.0, 1280 / max(h, w))
        sm = cv2.resize(img, (int(w * k), int(h * k))) if k < 1 else img
        det.setInputSize((sm.shape[1], sm.shape[0]))
        _, fs = det.detect(sm)
        fs = [] if fs is None else fs
        con.execute("delete from faces where clip_id=?", (cid,))
        kept = 0
        for i, f in enumerate(fs[:12]):
            if f[2] < 40 or f[3] < 40:  # tiny background faces: skip
                continue
            feat = rec.feature(rec.alignCrop(sm, f)).astype(np.float32).flatten()
            feat /= (np.linalg.norm(feat) + 1e-9)
            box = [round(float(x) / k) for x in f[:4]]
            con.execute("insert into faces values(?,?,?,?,NULL)", (cid, i, feat.tobytes(), json.dumps(box)))
            kept += 1
        con.execute("insert or replace into org(clip_id, taken, taken_src, gps, camera, sharp, bright, mp, faces, quality, analysed_at) values(?,?,?,?,?,?,?,?,?,?,?)",
                    (cid, taken, src, gps, cam, round(sharp, 1), round(bright, 1), round(mp, 2), kept, qscore(sharp, bright, mp, kept), time.strftime("%Y-%m-%d %H:%M")))
        if n % 50 == 0:
            con.commit(); log(f"  {n}/{len(rows)}")
    con.commit()


# ---------------- 3. classify ----------------
def mean_embs(con):
    import numpy as np
    out = {}
    for cid, emb in con.execute("select clip_id, emb from frames"):
        out.setdefault(cid, []).append(np.frombuffer(emb, dtype=np.float16).astype(np.float32))
    return {k: (lambda m: m / (np.linalg.norm(m) + 1e-9))(np.mean(v, axis=0)) for k, v in out.items()}


def classify(index_dir):
    import numpy as np
    from .broll import embed_text
    con = db(index_dir)
    names = list(CATEGORIES)
    T = np.stack([(lambda m: m / np.linalg.norm(m))(np.mean([embed_text(t) for t in CATEGORIES[c]], axis=0)) for c in names]).astype(np.float32)
    K = np.stack([embed_text(t) for t in KIDS]).astype(np.float32)
    E = mean_embs(con)
    for cid, e in E.items():
        if not con.execute("select 1 from org where clip_id=?", (cid,)).fetchone():
            continue
        s = T @ e
        p = np.exp(s * 100) / np.exp(s * 100).sum()  # CLIP logit scale
        o = np.argsort(-p)
        cat, cat2 = names[o[0]], names[o[1]]
        flag = con.execute("select flag from clips where id=?", (cid,)).fetchone()[0]
        kids = K @ e
        sens = flag or (SENSITIVE_CATS.get(cat) if p[o[0]] > 0.35 else None) or (SENSITIVE_CATS.get(cat2) if p[o[1]] > 0.3 else None) \
            or ("minors/family" if kids[0] - kids[1] > 0.02 else None)  # children anywhere -> consent check
        con.execute("update org set category=?, cat_score=?, cat2=?, sens=?, brands=? where clip_id=?",
                    (cat, round(float(p[o[0]]), 3), cat2, sens, ",".join(BRAND_FIT.get(cat, [])), cid))
    con.commit()
    log(f"classify: {len(E)} items")


# ---------------- 4. people ----------------
def cluster_faces(index_dir, thr=0.42):
    """Greedy centroid clustering on SFace embeddings (cosine; SFace same-person threshold is ~0.36, 0.42 favours precision)."""
    import numpy as np
    con = db(index_dir)
    rows = con.execute("select f.clip_id, f.k, f.emb from faces f join org o on o.clip_id=f.clip_id order by o.quality desc").fetchall()
    cents, members = [], []
    for cid, k, emb in rows:
        v = np.frombuffer(emb, dtype=np.float32)
        best, bi = -1, -1
        for i, c in enumerate(cents):
            s = float(c @ v)
            if s > best:
                best, bi = s, i
        if best >= thr:
            members[bi].append((cid, k)); c = cents[bi] * (len(members[bi]) - 1) + v; cents[bi] = c / np.linalg.norm(c)
        else:
            cents.append(v.copy()); members.append([(cid, k)])
    order = sorted(range(len(members)), key=lambda i: -len(members[i]))  # cluster 1 = most frequent face (usually the owner)
    con.execute("update faces set cluster=NULL")
    for new_id, i in enumerate(order, 1):
        con.executemany("update faces set cluster=? where clip_id=? and k=?", [(new_id, c, k) for c, k in members[i]])
    # cluster numbers change between runs; named people follow their stored face signature, not the number
    named = con.execute("select name, consent, centroid from people where centroid is not null").fetchall()
    con.execute("delete from people")
    taken = set()
    for name, consent, cen in named:
        v = np.frombuffer(cen, dtype=np.float32)
        sims = [(float(cents[i] @ v), new_id) for new_id, i in enumerate(order, 1) if new_id not in taken]
        if sims and max(sims)[0] >= thr:
            s_, nid = max(sims)
            taken.add(nid)
            con.execute("insert into people values(?,?,?,?)", (nid, name, consent, cents[order[nid - 1]].astype(np.float32).tobytes()))
        else:
            log(f"  could not re-find '{name}' this run (kept for next time)")
            con.execute("insert into people values(?,?,?,?)", (-len(taken) - 1000, name, consent, cen))
    con.commit()
    log(f"people: {len(rows)} faces -> {len(members)} clusters ({sum(len(m) >= 3 for m in members)} with 3+ photos); named carried over: {len(taken)}")
    return [(n, len(members[i])) for n, i in enumerate(order, 1)]


def people_sheet(index_dir, out, top=12, per=6):
    from PIL import Image, ImageDraw
    con = db(index_dir)
    cl = con.execute("select cluster, count(*) n from faces where cluster is not null group by cluster order by n desc limit ?", (top,)).fetchall()
    names = {r[0]: r[1] for r in con.execute("select cluster, name from people")}
    T = 140
    sheet = Image.new("RGB", (T * per + 220, T * max(1, len(cl))), (24, 24, 24))
    d = ImageDraw.Draw(sheet)
    for row, (c, n) in enumerate(cl):
        d.text((10, row * T + 10), f"#{c}  ({n} photos)", fill=(255, 255, 255))
        if names.get(c):
            d.text((10, row * T + 30), names[c], fill=(255, 220, 80))
        faces = con.execute("select f.clip_id, f.box, c.path, c.kind, c.duration from faces f join clips c on c.id=f.clip_id where f.cluster=? limit ?", (c, per)).fetchall()
        for j, (cid, box, path, kind, dur) in enumerate(faces):
            try:
                with tempfile.TemporaryDirectory() as td:
                    import cv2
                    img = still(Path(path), kind, dur, td)
                x, y, w, h = json.loads(box)
                pad = int(0.35 * max(w, h))
                crop = img[max(0, y - pad):y + h + pad, max(0, x - pad):x + w + pad][:, :, ::-1]
                sheet.paste(Image.fromarray(crop).resize((T - 6, T - 6)), (220 + j * T + 3, row * T + 3))
            except Exception:
                continue
    sheet.save(out)
    return out


def name_cluster(index_dir, cluster, name, consent=None):
    con = db(index_dir)
    consent = consent or ("yes" if name.lower() in ("klaus", "me", "self", "founder") else "unknown")
    import numpy as np
    embs = [np.frombuffer(e, dtype=np.float32) for (e,) in con.execute("select emb from faces where cluster=?", (int(cluster),))]
    if not embs:
        raise SystemExit(f"no faces in cluster #{cluster}: check people_sheet.jpg (numbers change after each `organize people`)")
    cen = np.mean(embs, axis=0); cen = (cen / np.linalg.norm(cen)).astype(np.float32)
    con.execute("delete from people where name=?", (name.lower(),))
    con.execute("insert or replace into people values(?,?,?,?)", (int(cluster), name.lower(), consent, cen.tobytes()))
    con.commit()
    apply_people(con)
    log(f"cluster #{cluster} = {name} (consent: {consent})")


def apply_people(con):
    names = {r[0]: r[1] for r in con.execute("select cluster, name from people")}
    per = {}
    for cid, c in con.execute("select clip_id, cluster from faces where cluster is not null"):
        per.setdefault(cid, set()).add(names.get(c, f"person{c}"))
    con.execute("update org set people=NULL")
    con.executemany("update org set people=? where clip_id=?", [(",".join(sorted(v)), k) for k, v in per.items()])
    con.commit()


# ---------------- 5-6. events + dedupe ----------------
def events_and_dupes(index_dir, gap_h=6.0, dup_sim=0.95):
    import numpy as np
    from datetime import datetime
    con = db(index_dir)
    con.execute("update org set event='undated' where taken_src='file'")  # no camera/file-name date: never invent an event
    rows = con.execute("select clip_id, taken, quality, category from org where taken is not null and taken_src != 'file' order by taken").fetchall()
    E = mean_embs(con)
    ev, last = None, None
    group, gid, recent = {}, 0, []  # recent = [(cid, time)] in the current event, last 15 min
    for cid, taken, q, cat in rows:
        try:
            t = datetime.fromisoformat(taken[:19])
        except ValueError:
            continue
        if last is None or (t - last).total_seconds() > gap_h * 3600:
            ev = t.strftime("%Y-%m-%d") + ("" if last is None or t.date() != last.date() else t.strftime("-%H%M"))
            recent = []
        recent = [(c, tt) for c, tt in recent if (t - tt).total_seconds() < 900]
        match = None
        if cid in E:  # compare with every recent shot, not just the previous one (a blurred frame must not break a burst)
            for c, tt in recent:
                if c in E:
                    sim, dt = float(E[cid] @ E[c]), (t - tt).total_seconds()
                    if sim >= dup_sim or (sim >= 0.85 and dt < 60):
                        if not match or sim > match[1]:
                            match = (c, sim)
        if match:
            group[cid] = group[match[0]]
        else:
            gid += 1; group[cid] = f"g{gid}"
        con.execute("update org set event=? where clip_id=?", (ev, cid))
        recent.append((cid, t))
        last = t
    for cid, g in group.items():
        con.execute("update org set dup_group=? where clip_id=?", (g, cid))
    # event label = dominant category (until Claude names it)
    # undated items still get near-duplicate grouping, by similarity alone
    und = [r[0] for r in con.execute("select clip_id from org where event='undated' order by clip_id")]
    reps = []
    for cid in und:
        hit = next((g for c, g in reps if cid in E and c in E and float(E[cid] @ E[c]) >= 0.97), None)
        if hit:
            group[cid] = hit
        else:
            gid += 1; group[cid] = f"g{gid}"; reps.append((cid, group[cid]))
    for cid in und:
        con.execute("update org set dup_group=? where clip_id=?", (group[cid], cid))
    con.execute("update org set best=0")
    for (g,) in con.execute("select distinct dup_group from org where dup_group is not null").fetchall():
        b = con.execute("select clip_id from org where dup_group=? order by quality desc limit 1", (g,)).fetchone()
        con.execute("update org set best=1 where clip_id=?", (b[0],))
    con.execute("insert or ignore into events(event, name, caption) values('undated', 'Undated', 'no camera or file-name date')")
    for (e,) in con.execute("select distinct event from org where event is not null and event != 'undated'").fetchall():
        cat = con.execute("select category, count(*) n from org where event=? group by category order by n desc limit 1", (e,)).fetchone()
        con.execute("insert or ignore into events(event, name) values(?, ?)", (e, f"{e} {cat[0] if cat else ''}".strip()))
    con.commit()
    n_dup = con.execute("select count(*) from org where best=0").fetchone()[0]
    log(f"events: {con.execute('select count(distinct event) from org').fetchone()[0]}; near-duplicates hidden behind best picks: {n_dup}")


def name_events(index_dir, model=None, max_events=None, per=12):
    """One contact sheet + one short Claude call per event -> name, caption, tags, story potential, brand fit."""
    from PIL import Image
    from .common import claude
    con = db(index_dir)
    evs = con.execute("select e.event from events e where e.caption is null and e.event != 'undated' order by e.event desc").fetchall()
    done = 0
    out_dir = Path(index_dir) / "organize" / "sheets"
    out_dir.mkdir(parents=True, exist_ok=True)
    for (e,) in evs:
        if max_events and done >= max_events:
            break
        items = con.execute("select o.clip_id from org o where o.event=? and o.best=1 and o.sens is null order by o.quality desc limit ?", (e, per)).fetchall()
        if not items:  # sensitive-only events are never sent to Claude
            continue
        done += 1
        thumbs = [Image.open(thumb(index_dir, cid)).convert("RGB") for (cid,) in items if thumb(index_dir, cid)]
        if not thumbs:
            continue
        cols = 4
        sheet = Image.new("RGB", (cols * 320, ((len(thumbs) + cols - 1) // cols) * 320), (20, 20, 20))
        for i, t in enumerate(thumbs):
            t.thumbnail((316, 316)); sheet.paste(t, ((i % cols) * 320 + 2, (i // cols) * 320 + 2))
        sp = out_dir / f"{e}.jpg"
        sheet.save(sp, quality=80)
        meta = con.execute("select min(taken), max(taken), count(*), group_concat(distinct category), group_concat(distinct people) from org where event=?", (e,)).fetchone()
        prompt = (f"Read the image {sp} (a contact sheet of one event from a founder's personal photo library). Event {e}, {meta[2]} items, "
                  f"{meta[0]} to {meta[1]}, detected categories: {meta[3]}, people: {meta[4] or 'none named'}. "
                  "Reply ONLY JSON: {\"name\": \"<=6 words, e.g. 'PLATFORM talk, Middlesbrough' or 'Team offsite whiteboard day'\", "
                  "\"caption\": \"one factual sentence\", \"tags\": [\"5-8 lowercase tags\"], "
                  "\"story\": \"one line: what founder story or post this could support, or 'none'\", "
                  "\"brands\": [\"subset of: titan-ai, klaus, physio-spot, heal360, power-protein, peachform\"]}. "
                  "Describe only what is visible; do not guess identities or locations you cannot see.")
        try:
            j = parse_json(claude(prompt, image_dir=out_dir, model=model))
            con.execute("update events set name=?, caption=?, tags=?, story=?, brands=? where event=?",
                        (j.get("name"), j.get("caption"), " ".join(j.get("tags", [])), j.get("story"), ",".join(j.get("brands", [])), e))
            con.commit(); log(f"  {e}: {j.get('name')}")
        except Exception as ex:
            log(f"  {e}: naming skipped ({ex})")


# ---------------- 7. report ----------------
def thumb(index_dir, cid, size=360):
    d = Path(index_dir) / "organize" / "thumbs"
    d.mkdir(parents=True, exist_ok=True)
    t = d / f"{cid}.jpg"
    if t.exists():
        return t
    con = db(index_dir)
    r = con.execute("select path, kind, duration from clips where id=?", (cid,)).fetchone()
    if not r:
        return None
    seek = ["-ss", f"{max(0, (r[2] or 0) / 2):.2f}"] if r[1] == "video" else []
    ffmpeg(seek + ["-i", r[0], "-vf", f"scale={size}:-2", "-frames:v", 1, "-q:v", 5, t], check=False)
    return t if t.exists() else None


def report(index_dir, out_dir=None):
    con = db(index_dir)
    out = Path(out_dir or Path(index_dir) / "organize")
    out.mkdir(parents=True, exist_ok=True)
    rows = con.execute("""select c.id, c.path, c.kind, c.duration, o.taken, o.category, o.cat_score, o.sens, o.people, o.quality, o.best, o.event,
                          o.brands, o.faces, e.name, e.story from clips c join org o on o.clip_id=c.id left join events e on e.event=o.event order by o.taken""").fetchall()
    cols = ["id", "path", "kind", "duration", "taken", "category", "confidence", "sensitive", "people", "quality", "best", "event", "brands", "faces", "event_name", "story"]
    with open(out / "catalog.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(cols); w.writerows(rows)
    R = [dict(zip(cols, r)) for r in rows]
    by = {}
    for r in R:
        by.setdefault(r["category"] or "Unsorted", []).append(r)
    def card(r):
        t = thumb(index_dir, r["id"])
        rel = os.path.relpath(t, out).replace("\\", "/") if t else ""
        badges = "".join(f'<span class="b {c}">{html.escape(x)}</span>' for c, x in
                         [("s", r["sensitive"] or ""), ("p", r["people"] or ""), ("v", "video" if r["kind"] == "video" else ""), ("q", f"q{r['quality']:.2f}" if r["quality"] else "")] if x)
        return (f'<figure title="{html.escape(r["path"])}"><img loading="lazy" src="{rel}"><figcaption>{badges}<br>'
                f'<small>{html.escape((r["event_name"] or r["event"] or "")[:40])}</small></figcaption></figure>')
    total, best = len(R), sum(1 for r in R if r["best"])
    sens = [r for r in R if r["sensitive"]]
    parts = [f"<h1>Media library: {total} items, {best} best picks</h1><p>Near-duplicates are hidden behind the best shot. "
             f"{len(sens)} items need a consent/privacy check before any use. Hover a tile for its original path.</p>",
             "<nav>" + " · ".join(f'<a href="#{html.escape(k)}">{html.escape(k)} ({len(v)})</a>' for k, v in sorted(by.items(), key=lambda x: -len(x[1]))) + "</nav>"]
    if sens:
        parts.append('<h2 id="review">Needs review (sensitive)</h2><div class="g">' + "".join(card(r) for r in sens[:200]) + "</div>")
    for k, v in sorted(by.items(), key=lambda x: -len(x[1])):
        picks = [r for r in v if r["best"] and not r["sensitive"]]
        parts.append(f'<h2 id="{html.escape(k)}">{html.escape(k)} <small>({len(picks)} best of {len(v)})</small></h2><div class="g">'
                     + "".join(card(r) for r in sorted(picks, key=lambda r: -(r["quality"] or 0))[:120]) + "</div>")
    evs = con.execute("select event, name, caption, story from events order by event desc").fetchall()
    parts.append("<h2>Events</h2><table>" + "".join(f"<tr><td>{html.escape(e or '')}</td><td><b>{html.escape(n or '')}</b></td><td>{html.escape(c or '')}</td><td>{html.escape(s or '')}</td></tr>" for e, n, c, s in evs) + "</table>")
    css = ("body{font:14px system-ui;margin:24px;background:#faf8f3;color:#141414}nav a{margin-right:6px}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px}"
           "figure{margin:0;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 3px #0002}img{width:100%;height:150px;object-fit:cover;display:block}"
           "figcaption{padding:6px}.b{display:inline-block;font-size:11px;padding:1px 6px;border-radius:9px;margin:1px;background:#eee}.s{background:#ffd5cc}.p{background:#d6e4ff}.v{background:#e6f5d6}"
           "td{padding:4px 10px;border-bottom:1px solid #ddd;vertical-align:top}")
    (out / "REVIEW.html").write_text(f"<!doctype html><meta charset=utf-8><title>Media library review</title><style>{css}</style>" + "".join(parts), encoding="utf-8")
    log(f"report: {out / 'REVIEW.html'}  +  {out / 'catalog.csv'}")
    return out / "REVIEW.html"


# ---------------- 8. apply ----------------
def apply_tree(index_dir, to, mode="link", best_only=True, include_sensitive=False):
    """Build Organised/<Category>/<event name>/<file>. link = hardlink (same drive, no extra space) else copy. Originals untouched."""
    con = db(index_dir)
    to = Path(to)
    q = ("select c.path, o.category, coalesce(e.name, o.event), o.sens, o.best from clips c join org o on o.clip_id=c.id left join events e on e.event=o.event")
    n, fell_back = 0, False
    for path, cat, ev, sens, best in con.execute(q).fetchall():
        if (best_only and not best) or (sens and not include_sensitive):
            continue
        src = Path(path)
        safe_ev = "".join(ch for ch in (ev or "Undated") if ch not in '<>:"/\\|?*').strip()[:60]
        dest = to / ("_Review_sensitive" if sens else (cat or "Unsorted")) / safe_ev / src.name
        if dest.exists():
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            if mode == "link":
                os.link(src, dest)
            else:
                raise OSError("copy requested")
        except OSError:
            if mode == "link" and not fell_back:
                log("hardlinks not possible here (different drive / cloud folder): copying instead")
                fell_back = True
            shutil.copy2(src, dest)
        n += 1
    log(f"apply: {n} files placed under {to} ({'hardlinks/copies' if mode == 'link' else 'copies'}); originals untouched")


def export_library(index_dir, person=None, min_quality=0.55, categories=None, brand=None):
    """Best non-sensitive picks -> assets/library/index.csv (absolute paths), so cards can use lib:<person> <category>."""
    from .assets import read_index, write_index
    con = db(index_dir)
    rows = read_index()
    known = {r["path"] for r in rows}
    consent = {r[0]: r[1] for r in con.execute("select name, consent from people")}
    add = 0
    for path, cat, people, qv, tags, ename in con.execute(
            "select c.path, o.category, o.people, o.quality, e.tags, e.name from clips c join org o on o.clip_id=c.id left join events e on e.event=o.event "
            "where o.best=1 and o.sens is null and o.quality>=?", (min_quality,)):
        if categories and cat not in categories:
            continue
        ppl = [p for p in (people or "").split(",") if p]
        if person and person not in ppl:
            continue
        if path in known:
            continue
        ok = all(consent.get(p) == "yes" for p in ppl)  # every recognised person must have consent
        rows.append({"path": path, "tags": " ".join(filter(None, [cat.lower() if cat else "", " ".join(ppl), tags or "", (ename or "").lower()])),
                     "people": ",".join(ppl), "consent": "yes" if ok and ppl else ("" if not ppl else "no"), "source": "own", "licence": "original",
                     "attribution": "", "brand": brand or ""})
        add += 1
    write_index(rows)
    log(f"library: +{add} best picks -> assets/library/index.csv (use lib:<tags> on cards; people without consent stay unusable)")


# ---------------- CLI ----------------
def cmd_organize(a):
    from argparse import Namespace
    idx = a.index_dir
    if a.action in ("index", "run"):
        from .broll import cmd_index
        cmd_index(Namespace(roots=a.roots, index_dir=idx, frames=3, min_dur=0.5, images=True, creator_brain_work=None))
    if a.action in ("analyse", "run"):
        analyse(idx, a.limit, a.force)
    if a.action in ("classify", "run"):
        classify(idx)
    if a.action in ("people", "run"):
        cluster_faces(idx)
        apply_people(db(idx))
        s = people_sheet(idx, Path(idx) / "organize" / "people_sheet.jpg") if (Path(idx) / "organize").mkdir(parents=True, exist_ok=True) is None else None
        log(f"people sheet: {s}  -> name clusters: editor.py organize name <#> <name>")
    if a.action in ("events", "run"):
        events_and_dupes(idx)
        if a.llm == "claude-cli":
            name_events(idx, a.claude_model, a.max_events)
    if a.action in ("report", "run"):
        report(idx, a.out)
    if a.action == "name":
        name_cluster(idx, a.roots[0], a.roots[1], a.consent)
    if a.action == "apply":
        apply_tree(idx, a.to, a.mode, not a.all, a.include_sensitive)
    if a.action == "export-library":
        export_library(idx, a.person, a.min_quality, set(a.categories.split(",")) if a.categories else None, a.brand)
