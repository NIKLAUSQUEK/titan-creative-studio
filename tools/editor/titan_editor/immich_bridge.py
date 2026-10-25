"""Studio bridge to IMMICH (self-hosted, open source): Immich organises the library; this file only adds what Immich lacks.

Immich (tools/immich/, Setup-Immich.ps1) does the heavy lifting on Klaus's PC: natural-language smart search (SigLIP2/CLIP,
benchmarked), face recognition + naming (InsightFace), duplicates, timeline/map, OCR, phone backup. His folders are mounted
READ-ONLY, so Immich never moves, edits or deletes a file.

This bridge adds the studio layer:
  setup          first run without clicking: admin user, read-scoped API key (saved outside the repo), read-only external
                 libraries, scan + smart-search/face jobs
  pick           "best photos of klaus speaking": Immich smart search (+ person filter) -> drop sensitive/unconsented ->
                 one per duplicate group -> re-rank by sharpness/exposure/resolution/face -> contact sheet + local paths
  sync-library   Klaus's hearts / "Studio Picks" album -> assets/library/index.csv, so cards can use lib:<tags>
  tag-sensitive  nightly: candidates for children / documents / patients go into "⚠ Sensitive – …" review albums in Immich
                 (over-flags on purpose; Klaus removes a photo from the album and it stays removed). Albums, not tags:
                 Immich stores tags in XMP sidecars, which it can't write on read-only folders.
  consent        people other than Klaus are unusable until consent=yes here (Immich has no consent field)
Cards can also ask Immich directly: "image": "immich:speaking on stage@klaus".

Config (never in the repo): %LOCALAPPDATA%/TitanEditor/immich.json {"url", "api_key", "path_map": {"/mnt/photos1": "D:/..."}}
or env IMMICH_URL / IMMICH_API_KEY.
"""
import json, math, os, secrets, string, time, urllib.error, urllib.request
from pathlib import Path

from .common import REPO, log

READ_SCOPES = ["asset.read", "asset.view", "asset.download", "person.read", "album.read", "tag.read", "duplicate.read", "library.read", "queue.read"]
TAG_SCOPES = ["album.create", "albumAsset.create"]  # only for tag-sensitive (review albums)
# Read-only folders mean Immich can't persist TAGS (it writes them to XMP sidecars next to the photo and the write fails),
# so studio flags live in ALBUMS, which are database-only: "⚠ Sensitive – minors" etc. Remove a photo from the album = cleared.
SENSITIVE_ALBUM = {"sensitive/minor": "⚠ Sensitive – minors", "sensitive/document": "⚠ Sensitive – documents", "sensitive/patient": "⚠ Sensitive – patients"}
SENSITIVE_QUERIES = {  # tag: (smart-search candidate queries, positive descriptions, margin over the best negative)
    # margins calibrated 2026-10-25 on a 76-item test library: documents 4/4 + 1 text-heavy infographic, patients 2/2 with
    # zero founder headshots, minors over-flag on purpose (a wrong tag only hides a photo until Klaus removes it)
    "sensitive/minor": (["young children playing", "a baby or toddler", "kids at school or a playground"], ["young children or babies", "kids playing"], 0.02),
    "sensitive/document": (["a passport, ID card or credit card", "a receipt or invoice", "a medical report or letter"],
                           ["a document, receipt, invoice or ID card with printed text"], 0.04),
    "sensitive/patient": (["a physiotherapist treating a patient", "a patient lying on a treatment table", "a hospital or clinic patient"],
                          ["a patient lying on a treatment table receiving physiotherapy", "a medical patient being examined"], 0.01),
}
NEGATIVES = ["a portrait or headshot of an adult", "adults in a business meeting or office", "a person exercising in a gym",
             "a landscape, city or travel photo", "food, a product or an object", "a crowd of adults at an event", "a selfie of an adult"]
STUDIO_QUERIES = {  # saved searches = the old categories, now answered by Immich's model
    "speaking": "a person speaking on stage at a conference with a microphone", "meeting": "people in a business meeting or at a whiteboard",
    "working": "a person working on a laptop at a desk", "headshot": "a professional headshot portrait looking at the camera",
    "screen": "a screenshot of an app, dashboard or chart", "gym": "a person training in a gym", "clinic-space": "an empty modern clinic treatment room",
    "food": "a healthy meal on a plate", "product": "a supplement bottle or protein tub product photo", "event": "people networking at an event",
    "travel": "city skyline or landscape while travelling"}


def cfg_path():
    base = os.environ.get("LOCALAPPDATA")
    return (Path(base) / "TitanEditor" if base else Path.home() / ".titan-editor") / "immich.json"


def cfg():
    c = {}
    if cfg_path().exists():
        c = json.loads(cfg_path().read_text(encoding="utf-8"))
    c["url"] = os.environ.get("IMMICH_URL") or c.get("url") or "http://localhost:2283"
    c["api_key"] = os.environ.get("IMMICH_API_KEY") or c.get("api_key")
    c.setdefault("path_map", {})
    c.setdefault("consent", {})
    return c


def save_cfg(c):
    cfg_path().parent.mkdir(parents=True, exist_ok=True)
    cfg_path().write_text(json.dumps({k: v for k, v in c.items()}, indent=1), encoding="utf-8")


class Immich:
    def __init__(self, url=None, api_key=None, token=None):
        c = cfg()
        self.url = (url or c["url"]).rstrip("/")
        self.key, self.token = api_key or c.get("api_key"), token

    def req(self, method, path, body=None, raw=False, timeout=60):
        h = {"Accept": "application/json"}
        if self.key:
            h["x-api-key"] = self.key
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        data = None
        if body is not None:
            data = json.dumps(body).encode(); h["Content-Type"] = "application/json"
        r = urllib.request.Request(self.url + "/api" + path, data=data, method=method, headers=h)
        try:
            with urllib.request.urlopen(r, timeout=timeout) as resp:
                b = resp.read()
                return b if raw else (json.loads(b) if b else None)
        except urllib.error.HTTPError as e:
            raise SystemExit(f"Immich {method} {path}: HTTP {e.code} {e.read()[:300]!r}")
        except urllib.error.URLError as e:
            raise SystemExit(f"Immich not reachable at {self.url} ({e.reason}). Start it: tools/immich/Setup-Immich.ps1 (or docker compose up -d in tools/immich)")

    # --- lookups ---
    def person(self, name):
        if not name:
            return None
        hits = self.req("GET", "/search/person?name=" + urllib.request.quote(name)) or []
        exact = [p for p in hits if (p.get("name") or "").lower() == name.lower()]
        return (exact or hits or [None])[0]

    def album(self, name):
        return next((a for a in (self.req("GET", "/albums") or []) if a.get("albumName") == name), None)

    def sensitive_ids(self):
        """Asset ids currently in any sensitive review album (the studio never uses these)."""
        out = set()
        for name in SENSITIVE_ALBUM.values():
            al = self.album(name)
            if al:
                out |= {a["id"] for a in self.metadata(albumIds=[al["id"]])}
        return out

    def smart(self, query, person_ids=None, kind="IMAGE", size=100, **filters):
        body = {"query": query, "size": size, "withExif": True, **({"personIds": person_ids} if person_ids else {}), **({"type": kind} if kind else {}), **filters}
        return ((self.req("POST", "/search/smart", body) or {}).get("assets") or {}).get("items", [])

    def metadata(self, **filters):
        out, page = [], 1
        while True:
            res = (self.req("POST", "/search/metadata", {"size": 1000, "page": page, "withPeople": True, "withExif": True, **filters}) or {}).get("assets") or {}
            out += res.get("items", [])
            if not res.get("nextPage"):
                return out
            page = int(res["nextPage"])

    def thumb(self, asset_id, size="preview"):
        return self.req("GET", f"/assets/{asset_id}/thumbnail?size={size}", raw=True)


# ---------------- quality re-rank (Immich has no best-shot score) ----------------
def quality_bytes(img_bytes, faces=0):
    """0..1 from a preview: sharpness (Laplacian variance), exposure, resolution proxy; a visible face helps."""
    import numpy as np, cv2
    img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        return 0.0
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sharp, bright = float(cv2.Laplacian(g, cv2.CV_64F).var()), float(g.mean())
    s = min(1.0, math.log1p(sharp) / math.log1p(800))
    e = max(0.0, 1 - abs(bright - 125) / 125)
    return round(0.6 * s + 0.3 * e + (0.1 if faces else 0), 3)


def local_path(asset, c=None):
    """Container path -> PC path via path_map (read-only external libraries), else None (download instead)."""
    c = c or cfg()
    op = asset.get("originalPath") or ""
    for cont, host in sorted(c["path_map"].items(), key=lambda x: -len(x[0])):
        if op.startswith(cont):
            p = Path(host + op[len(cont):])
            return p if p.exists() else None
    return None


def usable(asset, sensitive_ids, consent, owner_names=("klaus",)):
    if asset["id"] in sensitive_ids:
        return False, "sensitive (review album)"
    for p in asset.get("people") or []:
        n = (p.get("name") or "").lower()
        if not n:
            continue  # unnamed background faces: not identifiable people we track
        if n not in owner_names and consent.get(n) != "yes":
            return False, f"no consent: {n}"
    return True, ""


def pick(query, person=None, n=12, kind="IMAGE", candidates=120, out_dir=None, api=None):
    """Best usable matches for a text query (optionally containing a named person), re-ranked by quality, one per duplicate group."""
    api = api or Immich()
    c = cfg()
    pid = None
    if person:
        p = api.person(person)
        if not p:
            raise SystemExit(f"No person named '{person}' in Immich: open Immich → Explore → People and name the face first.")
        pid = p["id"]
    sens = api.sensitive_ids()
    items = api.smart(query, [pid] if pid else None, kind, candidates)
    # smart search returns relevance order but not people/tags: fetch details for the shortlist
    rows, seen_dup = [], set()
    for rank, a in enumerate(items):
        full = api.req("GET", f"/assets/{a['id']}")
        ok, why = usable(full, sens, c["consent"])
        if not ok:
            continue
        if full.get("duplicateId"):
            if full["duplicateId"] in seen_dup:
                continue
            seen_dup.add(full["duplicateId"])
        q = quality_bytes(api.thumb(a["id"]), faces=len(full.get("people") or []))
        score = round(0.65 * (1 - rank / max(1, len(items))) + 0.35 * q, 3)  # relevance first, quality breaks ties
        rows.append({"id": a["id"], "file": full.get("originalFileName"), "path": str(local_path(full, c) or ""), "relevance_rank": rank + 1,
                     "quality": q, "score": score, "taken": (full.get("exifInfo") or {}).get("dateTimeOriginal") or full.get("fileCreatedAt"),
                     "people": [p.get("name") for p in full.get("people") or [] if p.get("name")]})
        if len(rows) >= n * 3:
            break
    rows.sort(key=lambda r: -r["score"])
    rows = rows[:n]
    if out_dir:
        sheet(api, rows, Path(out_dir) / "picks.jpg")
    return rows


def sheet(api, rows, out, cols=4, w=300):
    from io import BytesIO
    from PIL import Image, ImageDraw
    ims = []
    for r in rows:
        try:
            im = Image.open(BytesIO(api.thumb(r["id"]))).convert("RGB")
            im.thumbnail((w, w)); ims.append((im, r))
        except Exception:
            continue
    if not ims:
        return None
    rws = math.ceil(len(ims) / cols)
    sh = Image.new("RGB", (cols * w, rws * (w + 22)), (24, 24, 24))
    d = ImageDraw.Draw(sh)
    for i, (im, r) in enumerate(ims):
        x, y = (i % cols) * w, (i // cols) * (w + 22)
        sh.paste(im, (x + (w - im.width) // 2, y))
        d.text((x + 6, y + w + 4), f"#{i + 1} q{r['quality']:.2f} {r['file'][:24]}", fill=(230, 230, 230))
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    sh.save(out, quality=85)
    return out


def fetch_original(api, asset_id, name, cache=None):
    cache = Path(cache or (cfg_path().parent / "immich_cache"))
    cache.mkdir(parents=True, exist_ok=True)
    p = cache / f"{asset_id[:8]}_{name}"
    if not p.exists():
        p.write_bytes(api.req("GET", f"/assets/{asset_id}/original", raw=True, timeout=300))
    return p


# ---------------- studio library sync ----------------
def sync_library(album="Studio Picks", favourites=True, brand=None, api=None):
    """Klaus curates in Immich (heart, or add to the album 'Studio Picks'); this mirrors them into assets/library/index.csv.
    (Tags are not used: on read-only folders Immich can't persist them.)"""
    from .assets import read_index, write_index
    api = api or Immich()
    c = cfg()
    sens = api.sensitive_ids()
    found = {}
    if favourites:
        for a in api.metadata(isFavorite=True):
            found[a["id"]] = (a, "favourite")
    al = [x for x in (api.req("GET", "/albums") or []) if x.get("albumName", "").lower() == album.lower()]
    if al:
        for a in api.metadata(albumIds=[al[0]["id"]]):
            found[a["id"]] = (a, album.lower())
    rows = read_index()
    known = {r["path"] for r in rows}
    add = skipped = 0
    for aid, (a, why) in found.items():
        ok, reason = usable(a, sens, c["consent"])
        if not ok:
            skipped += 1; continue
        p = local_path(a, c) or fetch_original(api, aid, a.get("originalFileName", "asset"))
        if str(p) in known:
            continue
        people = [x.get("name", "").lower() for x in a.get("people") or [] if x.get("name")]
        ex = a.get("exifInfo") or {}
        tags = {why, a.get("type", "").lower(), *(people), *(t.get("value", "").replace("/", " ") for t in a.get("tags") or []),
                (ex.get("city") or "").lower(), (ex.get("country") or "").lower()}
        rows.append({"path": str(p), "tags": " ".join(sorted(t for t in tags if t)), "people": ",".join(people),
                     "consent": "yes" if people else "", "source": "own (immich)", "licence": "original", "attribution": "", "brand": brand or ""})
        add += 1
    write_index(rows)
    log(f"library sync: +{add} from Immich ({len(found)} curated, {skipped} skipped as sensitive/unconsented)")
    return add


# ---------------- sensitive tagging ----------------
def tag_sensitive(per_query=150, dry_run=False, api=None):
    """Smart-search candidates per sensitive kind, confirmed locally (CLIP: positive vs best of several negatives), placed in
    '⚠ Sensitive – …' review albums. A photo Klaus removes from an album is remembered and never re-added."""
    import numpy as np
    from io import BytesIO
    from PIL import Image
    from .broll import embed_text, model
    api = api or Immich()
    c = cfg()
    cleared = set(c.get("sensitive_cleared", []))
    have = {tag: api.album(name) for tag, name in SENSITIVE_ALBUM.items()}
    # remember photos Klaus removed from a review album so they're never re-added
    for tag, ids in (c.get("sensitive_tagged") or {}).items():
        al = have.get(tag)
        if not al:
            continue
        still = {a["id"] for a in api.metadata(albumIds=[al["id"]])}
        for aid in ids:
            if aid not in still:
                cleared.add(f"{tag}:{aid}")
    M = model(); torch = M["torch"]
    total, report = 0, {}
    N = np.stack([embed_text(t) for t in NEGATIVES])
    for tag, (queries, positives, margin) in SENSITIVE_QUERIES.items():
        P = np.stack([embed_text(t) for t in positives])
        cand = {}
        for q in queries:
            for a in api.smart(q, None, None, per_query):
                cand[a["id"]] = a
        hits = []
        for aid in cand:
            if f"{tag}:{aid}" in cleared:
                continue
            if tag == "sensitive/patient":  # a photo where every face is a named, consented person (e.g. Klaus) is not a patient shot
                ppl = [p.get("name", "").lower() for p in (api.req("GET", f"/assets/{aid}").get("people") or [])]
                if ppl and all(n and (n == "klaus" or c["consent"].get(n) == "yes") for n in ppl):
                    continue
            try:
                im = Image.open(BytesIO(api.thumb(aid))).convert("RGB")
            except Exception:
                continue
            with torch.no_grad():
                e = M["m"].encode_image(M["pre"](im).unsqueeze(0).to(M["dev"]))
                e = (e / e.norm(dim=-1, keepdim=True)).cpu().numpy()[0]
            if float((P @ e).max()) - float((N @ e).max()) > margin:
                hits.append(aid)
        log(f"{tag}: {len(cand)} candidates -> {len(hits)} tagged")
        report[tag] = [cand[h].get("originalFileName") or h for h in hits]
        if hits and not dry_run:
            al = have.get(tag)
            if al:
                api.req("PUT", f"/albums/{al['id']}/assets", {"ids": hits})
            else:
                have[tag] = api.req("POST", "/albums", {"albumName": SENSITIVE_ALBUM[tag], "assetIds": hits,
                                                         "description": "Studio: possible sensitive photos. Remove any that are fine; they won't be re-added."})
            c.setdefault("sensitive_tagged", {}).setdefault(tag, [])
            c["sensitive_tagged"][tag] = sorted(set(c["sensitive_tagged"][tag]) | set(hits))
        total += len(hits)
    c["sensitive_cleared"] = sorted(cleared)
    save_cfg(c)
    return report if dry_run else total


# ---------------- first-run setup ----------------
MODELS = {"cpu": "ViT-B-16-SigLIP2__webli",            # 84.86% recall, ~3 GB RAM, fast (Immich docs table, 2026-10)
          "gpu": "ViT-SO400M-16-SigLIP2-384__webli",   # 85.99% recall (best English), ~3.9 GB VRAM
          "multilingual": "nllb-clip-large-siglip__mrl"}  # if searching in Chinese / Malay etc.


def setup(email, name, password=None, import_paths=("/mnt/photos1",), path_map=None, url=None, tagging=True, model="cpu"):
    """Fresh Immich: admin user, scoped API key (read + tag), read-only external library over the mounted folders, scan."""
    u = (url or cfg()["url"]).rstrip("/")
    anon = Immich(url=u, api_key="")
    anon.key = None
    password = password or "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(20))
    try:
        anon.req("POST", "/auth/admin-sign-up", {"email": email, "name": name, "password": password})
        log(f"admin created: {email}")
    except SystemExit as e:
        if "400" not in str(e):
            raise
        log("admin already exists: logging in with the given password")
    tok = anon.req("POST", "/auth/login", {"email": email, "password": password})
    me = Immich(url=u, token=tok["accessToken"]); me.key = None
    # better smart-search model BEFORE the first scan, so nothing has to be re-indexed
    sc = me.req("GET", "/system-config")
    want = MODELS.get(model, model)
    if sc.get("machineLearning", {}).get("clip", {}).get("modelName") != want:
        sc["machineLearning"]["clip"]["modelName"] = want
        me.req("PUT", "/system-config", sc)
        log(f"smart-search model: {want}")
        if (me.req("GET", "/libraries") or []):  # existing install: re-index with the new model
            me.req("PUT", "/jobs/smartSearch", {"command": "start", "force": True})
    key = me.req("POST", "/api-keys", {"name": "titan-studio", "permissions": READ_SCOPES + (TAG_SCOPES if tagging else [])})
    secret = key.get("secret") or key.get("apiKey", {}).get("secret")
    libs = me.req("GET", "/libraries") or []
    lib = next((l for l in libs if l.get("name") == "Studio library"), None)
    if not lib:
        lib = me.req("POST", "/libraries", {"ownerId": tok["userId"], "name": "Studio library", "importPaths": list(import_paths),
                                            "exclusionPatterns": ["**/@eaDir/**", "**/.tmp.drivedownload/**", "**/*.ini", "**/.DS_Store", "**/Thumbs.db"]})
    me.req("POST", f"/libraries/{lib['id']}/scan")
    c = cfg()
    c.update(url=u, api_key=secret, path_map=path_map or c.get("path_map", {}))
    save_cfg(c)
    log(f"API key saved to {cfg_path()} (outside the repo). Library scanning; open {u} → Explore → People to name faces.")
    return {"password": password, "library": lib["id"]}


def status(api=None):
    api = api or Immich()
    v = api.req("GET", "/server/version")
    q = api.req("GET", "/queues") or []
    busy = {x["name"]: x["statistics"] for x in q if any((x.get("statistics") or {}).get(k) for k in ("active", "waiting"))}
    stats = api.req("GET", "/server/statistics") if False else None
    return {"version": f"{v['major']}.{v['minor']}.{v['patch']}", "busy_queues": busy}


def cmd_immich(a):
    if a.action == "setup":
        pm = dict(x.split("=", 1) for x in (a.map or []))
        r = setup(a.email, a.name, a.password, a.paths or ["/mnt/photos1"], pm, a.url, model=a.model)
        print(json.dumps({k: v for k, v in r.items() if k != "password"} | {"note": "admin password printed once below; store it in your password manager"}))
        print(r["password"])
    elif a.action == "status":
        print(json.dumps(status(), indent=1))
    elif a.action == "pick":
        q = a.query
        rows = pick(q, a.person, a.n, None if a.videos else "IMAGE", out_dir=a.out)
        for i, r in enumerate(rows, 1):
            print(f"{i:2}. q{r['quality']:.2f} rank{r['relevance_rank']:3}  {r['file']}  {r['path'] or '(download: immich ' + r['id'] + ')'}  {','.join(r['people'])}")
        if a.out:
            print(f"contact sheet: {Path(a.out) / 'picks.jpg'}  (LOOK before using)")
    elif a.action == "sync-library":
        sync_library(brand=a.brand)
    elif a.action == "tag-sensitive":
        r = tag_sensitive(dry_run=a.dry_run)
        if a.dry_run:
            for k, v in r.items():
                print(f"{k}: {len(v)} would be tagged: {', '.join(v[:40])}")
        else:
            print(f"{r} photos placed in '⚠ Sensitive – …' review albums (remove any that are fine; they won't come back)")
    elif a.action == "consent":
        c = cfg(); c["consent"][a.query.lower()] = a.value; save_cfg(c)
        print(f"consent[{a.query.lower()}] = {a.value}")
    elif a.action == "queries":
        for k, v in STUDIO_QUERIES.items():
            print(f"{k:14} {v}")
