"""Image assets for cards and boards: the founder's own library first, free-licensed downloads second, AI generation last.

Where an image comes from (card "image" field):
  "assets/people/klaus/stage.jpg"   a path (repo-relative or absolute)
  "lib:klaus whiteboard"            best match in the brand/founder library (assets/library/index.csv tags) - Klaus's own photos win
  "immich:speaking on stage@klaus"  best usable match from the self-hosted Immich library (immich_bridge.pick)
  "gen:<prompt>"                    an AI asset to make; cards render a labelled placeholder and `cards` writes ASSETS_NEEDED.md
                                    (free: Nano Banana in the Gemini app / Google Flow images; premium: Higgsfield after a cost quote)
  {"src": ..., "focus": [0.5, 0.35], "credit": "..."}   same, with crop focus and an on-slide credit

Library index (assets/library/index.csv): path, tags, people, consent, source, licence, attribution, brand
  people + consent matter: a photo with a person is usable only when consent = yes (real staff/clients; patients never for health brands).
Free downloads: Openverse (no key; commercial-use licences only), recorded in the index + assets/licences.csv with attribution.
Cutouts: rembg (local, free) -> <name>_cutout.png, so a founder photo can sit beside the text like a magazine cover.
"""
import csv, json, re, urllib.parse, urllib.request
from pathlib import Path

from .common import REPO, log

LIB = REPO / "assets" / "library"
INDEX = LIB / "index.csv"
FIELDS = ["path", "tags", "people", "consent", "source", "licence", "attribution", "brand"]
UA = {"User-Agent": "TitanCreativeStudio/1.0 (content production; contact via repo owner)"}
IMG_EXT = (".jpg", ".jpeg", ".png", ".webp")


def read_index():
    if not INDEX.exists():
        return []
    with open(INDEX, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_index(rows):
    LIB.mkdir(parents=True, exist_ok=True)
    with open(INDEX, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})


def scan_library(brand=None):
    """Add any new image files under assets/library/ and assets/people/ to the index (tags from folder + file names).
    Klaus drops photos in a folder; this makes them findable. Existing rows (and their consent/licence) are kept."""
    rows = read_index()
    known = {r["path"] for r in rows}
    added = 0
    for root in (LIB, REPO / "assets" / "people", REPO / "assets" / "brands"):
        if not root.exists():
            continue
        for p in sorted(root.rglob("*")):
            if p.suffix.lower() not in IMG_EXT:
                continue
            rel = str(p.relative_to(REPO)).replace("\\", "/")
            if rel in known:
                continue
            parts = [x for x in p.relative_to(REPO).parts[1:-1]] + re.split(r"[-_ .]+", p.stem)
            tags = " ".join(sorted({t.lower() for t in parts if t and not t.isdigit() and len(t) > 1}))
            person = p.relative_to(REPO).parts[2] if p.relative_to(REPO).parts[1] == "people" else ""
            rows.append({"path": rel, "tags": tags, "people": person, "consent": "yes" if person else "",
                         "source": "own", "licence": "original", "attribution": "", "brand": brand or ""})
            added += 1
    write_index(rows)
    return added, len(rows)


def find(query, brand=None, person=None, allow_people=True):
    """Best library match for a tag query; own photos beat downloads; people photos need consent."""
    q = {w for w in re.findall(r"[a-z0-9]+", query.lower()) if len(w) > 1}
    best, score = None, 0
    for r in read_index():
        tags = set(r["tags"].split()) | set(re.findall(r"[a-z0-9]+", Path(r["path"]).stem.lower()))
        if r.get("people") and (not allow_people or r.get("consent", "").lower() not in ("yes", "y", "true")):
            continue
        s = 3 * len(q & tags) + (2 if r.get("source") == "own" else 0) + (1 if brand and r.get("brand") == brand else 0) \
            + (2 if person and r.get("people") == person else 0)
        if q and not (q & tags):
            continue
        if s > score:
            best, score = r, s
    return best


def resolve(img, brand=None):
    """Card image spec -> dict(path or None, kind, label, credit, focus). Never raises: missing images become placeholders."""
    if not img:
        return None
    spec = img if isinstance(img, dict) else {"src": img}
    src = str(spec.get("src", ""))
    out = {"path": None, "kind": "file", "label": src, "credit": spec.get("credit", ""), "focus": spec.get("focus", [0.5, 0.38]),
           "frame": spec.get("frame")}
    if src.startswith("gen:"):
        out.update(kind="gen", label=src[4:].strip())
        return out
    if src.startswith("immich:"):  # "immich:speaking on stage@klaus" -> best usable match straight from Immich
        q, _, person = src[7:].partition("@")
        try:
            from .immich_bridge import Immich, fetch_original, pick
            api = Immich()
            rows = pick(q.strip(), person.strip() or None, n=1, api=api)
            if rows:
                r0 = rows[0]
                out.update(path=Path(r0["path"]) if r0["path"] else fetch_original(api, r0["id"], r0["file"]), kind="immich", label=r0["file"])
                return out
        except SystemExit as e:
            log(f"immich image '{src}': {e}")
        out.update(kind="missing", label=f"immich: {src[7:]}")
        return out
    if src.startswith("lib:"):
        r = find(src[4:], brand, spec.get("person"), allow_people=True)
        if r:
            out.update(path=REPO / r["path"], kind="lib", label=r["path"])
            if not out["credit"] and r.get("licence") not in ("", "original", "own") and r.get("attribution"):
                out["credit"] = r["attribution"]
        else:
            out.update(kind="missing", label=f"library: {src[4:].strip()}")
        return out
    p = Path(src)
    p = p if p.is_absolute() else REPO / p
    if p.exists():
        out["path"] = p
    else:
        out.update(kind="missing", label=f"file: {src}")
    return out


# ---------------- free-licensed downloads (Openverse) ----------------
def openverse(query, n=6, licence_type="commercial", out_dir=None, brand=None, allow_sa=False):
    """Search Openverse (CC / public-domain, commercial-use filter), download the top n, record licence + attribution.
    Returns rows. CC BY / BY-SA need the on-slide credit (cards add it automatically from the index)."""
    out_dir = Path(out_dir or LIB / "web" / re.sub(r"[^a-z0-9]+", "-", query.lower()).strip("-"))
    out_dir.mkdir(parents=True, exist_ok=True)
    url = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode({"q": query, "license_type": licence_type, "page_size": max(n * 2, 10),
                                                                           "mature": "false"})
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        res = json.loads(r.read())["results"]
    rows, idx = [], read_index()
    for it in res:
        if len(rows) >= n:
            break
        lic = (it.get("license") or "").lower()
        if "nc" in lic or "nd" in lic or (lic == "by-sa" and not allow_sa):
            continue  # no NC; no ND (crop/overlay = adaptation); BY-SA would make our slide ShareAlike, so opt-in only
        ext = Path(urllib.parse.urlparse(it["url"]).path).suffix.lower() or ".jpg"
        if ext not in IMG_EXT:
            ext = ".jpg"
        dest = out_dir / f"{it['id'][:8]}{ext}"
        try:
            with urllib.request.urlopen(urllib.request.Request(it["url"], headers=UA), timeout=40) as r, open(dest, "wb") as f:
                f.write(r.read())
        except Exception as e:  # dead links are common on aggregated sources
            log(f"skip {it['url']}: {e}")
            continue
        credit = f"{it.get('title') or 'Image'} by {it.get('creator') or 'unknown'} ({lic.upper()} {it.get('license_version') or ''})".strip()
        row = {"path": str(dest.relative_to(REPO)).replace("\\", "/"), "tags": " ".join(sorted({t["name"].lower() for t in it.get("tags", [])[:12]} | set(query.lower().split()))),
               "people": "", "consent": "", "source": it.get("foreign_landing_url") or it["url"], "licence": f"cc-{lic} {it.get('license_version') or ''}".strip(),
               "attribution": credit, "brand": brand or ""}
        idx.append(row); rows.append(row)
        lc = REPO / "assets" / "licences.csv"
        new = not lc.exists()
        with open(lc, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["path", "source_url", "licence", "scope", "attribution"])
            w.writerow([row["path"], row["source"], row["licence"], "commercial (CC, adaptation allowed)", credit])
    write_index(idx)
    return rows


# ---------------- cutouts ----------------
def cutout(path, model="isnet-general-use"):
    """Remove the background locally (rembg). isnet-general-use is the default (best on our people + product tests); u2net_human_seg is lighter for clean studio portraits."""
    try:
        from rembg import new_session, remove
    except ImportError:
        raise SystemExit("rembg not installed: pip install rembg  (or use Higgsfield remove_background / Canva BG remover, then save as *_cutout.png)")
    from PIL import Image
    p = Path(path)
    p = p if p.is_absolute() else REPO / p
    out = p.with_name(p.stem + "_cutout.png")
    im = remove(Image.open(p).convert("RGB"), session=new_session(model))
    bb = im.getbbox()
    if bb:
        im = im.crop(bb)
    im.save(out)
    rows = read_index()
    src = next((r for r in rows if r["path"] == str(p.relative_to(REPO)).replace("\\", "/")), None)
    rel = str(out.relative_to(REPO)).replace("\\", "/")
    if src and not any(r["path"] == rel for r in rows):
        rows.append(dict(src, path=rel, tags=src["tags"] + " cutout"))
        write_index(rows)
    return out


# ---------------- AI asset plan ----------------
def assets_needed(cards, theme, out_md):
    """List gen:/missing images with ready prompts in the brand look. Generation itself goes through the studio gates."""
    need = []
    for i, c in enumerate(cards, 1):
        img = c.get("image")
        if not img:
            continue
        r = resolve(img, theme.get("brand"))
        if r and r["kind"] in ("gen", "missing"):
            need.append((i, r, c.get("layout", "split")))
    if not need:
        return None
    look = theme.get("look", "studio")
    style = {"creator": "natural light, candid documentary photo, warm neutral tones, real textures, shallow depth of field, no text, no logos",
             "editorial": "editorial magazine photography, soft window light, muted warm palette, generous negative space, no text, no logos",
             "brand-block": f"clean graphic photo, solid {theme.get('bg', 'brand')} colour backdrop, crisp studio light, no text, no logos"}.get(look, "no text, no logos")
    lines = ["# Assets needed", "", "Order of preference: **Klaus's or the brand's own photo** (drop it in `assets/library/` or `assets/people/<who>/`, run `editor.py assets scan`, "
             "then use `lib:<tags>`) → **free-licensed** (`editor.py assets fetch \"<query>\"`) → **AI** (free: Nano Banana in the Gemini app or Google Flow images; "
             "premium: Higgsfield after a cost quote). Never AI-generate a real person, a patient or a fake result.", "",
             "| slide | layout | need | prompt (paste into the image model) |", "|---|---|---|---|"]
    for i, r, lay in need:
        ar = {"photo": "4:5 full-bleed", "split": "16:10 landscape", "inset": "4:3", "screen": "16:10 UI screenshot (capture the real screen instead)",
              "polaroid": "1:1", "cutout": "portrait, plain background (then `editor.py assets cutout`)"}.get(lay, "4:3")
        prompt = f"{r['label']}, {style}, aspect {ar.split()[0]}" if r["kind"] == "gen" else "(own photo or `assets fetch`)"
        lines.append(f"| {i} | {lay} | {r['label']} | {prompt} |")
    Path(out_md).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_md


def cmd_assets(a):
    if a.action == "scan":
        added, total = scan_library(a.brand)
        print(f"library index: +{added} new, {total} total -> {INDEX.relative_to(REPO)}  (set consent=yes for photos of people who agreed)")
    elif a.action == "fetch":
        rows = openverse(a.query, a.n, brand=a.brand, allow_sa=a.allow_sa)
        for r in rows:
            print(f"{r['path']}  [{r['licence']}]  {r['attribution']}")
        print(f"{len(rows)} downloaded; use them as lib:<tags> or by path. Look before using: free archives vary in quality.")
    elif a.action == "find":
        r = find(a.query, a.brand)
        print(json.dumps(r, indent=1) if r else "no match")
    elif a.action == "cutout":
        print(cutout(a.query, a.model))
