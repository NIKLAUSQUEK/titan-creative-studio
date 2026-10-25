"""Licensed web images for beats your own footage can't cover (a person, a product, a place, a concept). No API keys.

Sources: Openverse (api.openverse.org: CC + public-domain images incl. Wikimedia/Flickr) and Wikimedia Commons.
Not Google Images: it returns no licence data and its terms forbid automated scraping, so nothing found there is safe to post.
Only commercial-use licences are kept (CC0, Public Domain, CC BY, CC BY-SA; never NC/ND). Each image keeps its credit;
CC BY/BY-SA images get an on-screen credit and a line in web/ATTRIBUTION.md for the caption.
Real people: allowed only as editorial/commentary context with credit, never in ads or anything implying endorsement (QC flags it).
"""
import hashlib, html, json, re, urllib.parse, urllib.request
from pathlib import Path

from .common import log, rjson, wjson

UA = "TitanEditor/0.3 (local video editor; contact via github.com/niklausquek/titan-creative-studio)"
OK = re.compile(r"^(cc0|pdm|public domain|cc[- ]by(-sa)?([- ][\d.]+)?)$", re.I)


def _get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def openverse(q, n=8):
    u = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode({"q": q, "license_type": "commercial", "page_size": n, "mature": "false"})
    out = []
    for r in json.loads(_get(u)).get("results", []):
        lic = (r.get("license") or "").lower()
        lic_name = "CC0" if lic == "cc0" else "Public Domain" if lic == "pdm" else f"CC {lic.upper()} {r.get('license_version') or ''}".strip()
        if lic not in ("cc0", "pdm", "by", "by-sa"):
            continue
        out.append({"source": f"openverse/{r.get('source')}", "title": r.get("title"), "url": r.get("url"), "thumb": r.get("thumbnail"),
                    "creator": r.get("creator") or "unknown", "licence": lic_name, "licence_url": r.get("license_url"), "page": r.get("foreign_landing_url"),
                    "w": r.get("width"), "h": r.get("height")})
    return out


def commons(q, n=8):
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": 6, "gsrsearch": f"{q} filetype:bitmap", "gsrlimit": n,
        "prop": "imageinfo", "iiprop": "url|extmetadata|size", "iiurlwidth": 1600})
    out = []
    for p in (json.loads(_get(u)).get("query", {}).get("pages", {}) or {}).values():
        ii = (p.get("imageinfo") or [{}])[0]
        md = ii.get("extmetadata", {})
        lic = (md.get("LicenseShortName", {}).get("value") or "").strip()
        if not OK.match(lic.replace("Public domain", "public domain")):
            continue
        artist = re.sub(r"<[^>]+>", "", html.unescape(md.get("Artist", {}).get("value") or "unknown")).strip()
        out.append({"source": "wikimedia-commons", "title": p.get("title"), "url": ii.get("thumburl") or ii.get("url"), "thumb": ii.get("thumburl"),
                    "creator": artist[:80], "licence": lic, "licence_url": md.get("LicenseUrl", {}).get("value"), "page": ii.get("descriptionurl"),
                    "w": ii.get("width"), "h": ii.get("height")})
    return out


def find(query, out_dir, n=6, real_person=False, min_side=600):
    """Search both sources, download up to n usable images to out_dir, return candidate dicts (kind=image) with credit + licence."""
    from PIL import Image
    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    found = []
    for fn in (openverse, commons):
        try:
            found += fn(query)
        except Exception as e:
            log(f"  {fn.__name__}: {str(e)[:120]}")
        if len(found) >= n * 2:
            break
    cands = []
    for r in found:
        if len(cands) >= n:
            break
        if r.get("w") and r.get("h") and min(r["w"], r["h"]) < min_side:
            continue
        key = hashlib.sha1((r.get("page") or r["url"] or "").encode()).hexdigest()[:12]
        jpg = out_dir / f"{key}.jpg"
        if not jpg.exists():
            for url in [u for u in (r.get("url"), r.get("thumb")) if u]:
                try:
                    raw = out_dir / f"{key}.raw"
                    raw.write_bytes(_get(url, 40))
                    im = Image.open(raw).convert("RGB")
                    im.thumbnail((1600, 1600))
                    im.save(jpg, quality=88)
                    raw.unlink(missing_ok=True)
                    break
                except Exception:
                    continue
        if not jpg.exists():
            continue
        credit = f"{'Photo' if not real_person else 'Image'}: {r['creator']} / {r['licence']}"
        meta = {**r, "path": str(jpg), "credit": credit, "real_person": real_person, "query": query}
        wjson(jpg.with_suffix(".json"), meta)
        cands.append(meta)
    return cands


def rank(cands, queries):
    """Order web candidates by local CLIP similarity to the beat's queries (zero tokens)."""
    if not cands:
        return []
    import numpy as np
    from .broll import embed_images, embed_text
    E = embed_images([c["path"] for c in cands]).astype(np.float32)
    s = np.max(np.stack([E @ embed_text(q).astype(np.float32) for q in queries]), axis=0)
    for c, v in zip(cands, s):
        c["score"] = round(float(v), 4)
    return sorted(cands, key=lambda c: -c["score"])


def attribution(edit_dir, used):
    """Write web/ATTRIBUTION.md for the images an edit actually uses (paste into the caption / description)."""
    L = ["# Image credits (paste into the post caption or description)", ""]
    for c in used:
        L.append(f"- {c.get('title') or Path(c['path']).name}: {c['creator']}, {c['licence']} ({c.get('licence_url') or ''}) via {c['source']} {c.get('page') or ''}")
    p = Path(edit_dir) / "web" / "ATTRIBUTION.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(L) + "\n", encoding="utf-8")
    return p


def cmd_web(a, edit_dir):
    qs = [x.strip() for x in a.query.split("|") if x.strip()]
    cands = rank(find(qs[0], Path(edit_dir) / "web", a.n, a.real_person), qs)
    for c in cands:
        print(f"{c['score']:.3f}  {c['licence']:14} {c['creator'][:30]:30} {c['path']}")
