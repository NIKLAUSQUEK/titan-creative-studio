#!/usr/bin/env python3
"""STYLE HOME: one index of every style the studio can make, so Klaus can pick and agents can offer.

Families (source of truth -> this script only reads them):
  edit       tools/editor/presets/*.json        auto-editor presets (pace, captions, B-roll, music, grade)
  script     styles/script.json                 writing/voice DNA (Hormozi math, Meakins myth-bust, SLAY...) - structure only, never impersonation
  animation  styles/animation.json              stickman, whiteboard, flat vector, anime, 3D, clay, collage, kinetic type, data-viz, parallax, diorama, AI doc
  carousel   styles/carousel.json               16 slide archetypes, rendered by the cards engine
  linkedin   styles/linkedin.json               LinkedIn post/document/video/newsletter/ads formats
  creator    Supabase style_cards (via /style)  a specific creator's measured StyleCard -> `style-<creator>` edit preset

  python scripts/styles.py offer --brand titan-ai --platform linkedin --goal "explain AI agents" [-n 3]
  python scripts/styles.py find "stickman psychology" [--family animation --brand physio-spot --platform tiktok --funnel TOFU]
  python scripts/styles.py show hormozi          (id or alias; prints the bundle: script + edit + animation + carousel pairings)
  python scripts/styles.py list [--family script]
  python scripts/styles.py build                 regenerate styles/index.json + styles/STYLE_MENU.md (run after editing any source)
"""
import argparse, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FAMILIES = ("edit", "script", "animation", "carousel", "linkedin")
BRANDS = {  # free-text brand names in presets -> brand ids (brands/<id>.md)
    "physio-spot": ["physio spot", "physio", "clinic", "clinician", "health"], "heal360": ["heal360", "heal 360", "clinic", "health"],
    "power-protein": ["power protein", "protein"], "peachform": ["peachform", "women's fitness", "womens fitness"],
    "titan-ai": ["titan.ai", "titan ai", "ai agency", "b2b"], "klaus": ["klaus", "founder", "personal"],
    "personal-gym-skits": ["gym skits", "personal gym"], "clinic-director": ["clinic directors", "clinic director"]}
HEALTH = {"physio-spot", "heal360"}
PLATFORM_ALIASES = {"ig": "instagram", "reels": "instagram", "instagram": "instagram", "tiktok": "tiktok", "yt": "youtube", "youtube": "youtube",
                    "shorts": "youtube", "linkedin": "linkedin", "li": "linkedin", "facebook": "facebook", "fb": "facebook", "x": "x", "threads": "threads"}
STOP = set("a an the and or for to of in on with my our your me make do it this that like style video post".split())


def stem(w):
    for suf in ("ers", "er", "ing", "ies", "es", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def tok(s):
    return {stem(w) for w in re.findall(r"[a-z0-9']+", str(s).lower()) if w not in STOP and len(w) > 1}


def brand_ids(values):
    out = set()
    for v in values or []:
        v = str(v).lower()
        for bid, keys in BRANDS.items():
            if v == bid or any(k in v for k in keys):
                out.add(bid)
    return sorted(out)


def plat_norm(values):
    return sorted({PLATFORM_ALIASES.get(str(p).lower(), str(p).lower()) for p in values or []})


def load():
    items = []
    for f in sorted((REPO / "tools" / "editor" / "presets").glob("*.json")):
        if f.name.startswith("_"):
            continue
        p = json.loads(f.read_text(encoding="utf-8"))
        asp = str(p.get("aspect", "9:16"))
        plats = ["tiktok", "instagram", "youtube"] + (["linkedin"] if "linkedin" in (p.get("label", "") + p["name"]).lower() or "b2b" in p["name"] else [])
        items.append({"id": p["name"], "family": "edit", "name": p.get("label", p["name"]), "aliases": [p["name"].replace("-", " ")],
                      "what": p.get("description", ""), "brands": brand_ids(p.get("brands")) or ["all"], "platforms": plats, "funnel": p.get("funnel", []),
                      "aspect": asp, "kind": p.get("kind"), "compliance": "; ".join(p["compliance_lock"]) if isinstance(p.get("compliance_lock"), list) else p.get("compliance_lock", ""),
                      "route": f"python tools/editor/editor.py assemble --preset {p['name']}  (or /edit with this preset)",
                      "sync": p.get("sync", {}), "sources": p.get("references", [])})
    for fam in FAMILIES[1:]:
        f = REPO / "styles" / f"{fam}.json"
        if f.exists():
            for s in json.loads(f.read_text(encoding="utf-8")):
                s.setdefault("family", fam)
                s["platforms"] = plat_norm(s.get("platforms"))
                items.append(s)
    return items


def resolve(items, key):
    k = key.lower().strip()
    exact = [s for s in items if s["id"] == k or k in [a.lower() for a in s.get("aliases", [])]]
    if exact:
        return exact
    return [s for s in items if k in s["id"] or any(k in a.lower() for a in s.get("aliases", []))]


def score(s, q, brand=None, platform=None, funnel=None, fmt=None):
    qt = tok(q) | tok(fmt or "")
    hay = tok(" ".join([s["id"], s.get("name", ""), " ".join(s.get("aliases", [])), s.get("what", ""), s.get("best_for", ""),
                        " ".join(s.get("formats", []) if isinstance(s.get("formats"), list) else [])]))
    sc = 3.0 * len(qt & hay)
    if any(a.lower() in q.lower() for a in s.get("aliases", []) if len(a) > 3):
        sc += 12
    if brand:
        bs = s.get("brands", ["all"])
        sc += 3 if brand in bs else (1 if "all" in bs else -2)
        if brand in HEALTH and re.search(r"not for health|never for clinics|not for clinic", (s.get("compliance", "") + s.get("what", "")).lower()):
            sc -= 50
    if platform:
        pl = s.get("platforms") or []
        sc += 2 if platform in pl else (-3 if pl else 0)
    if funnel and any(funnel.lower() in str(f).lower() for f in s.get("funnel", [])):
        sc += 1.5
    return sc


def rank(items, q="", family=None, brand=None, platform=None, funnel=None, fmt=None, n=5):
    pool = [s for s in items if not family or s["family"] == family]
    ranked = sorted(pool, key=lambda s: -score(s, q, brand, platform, funnel, fmt))
    return [s for s in ranked if score(s, q, brand, platform, funnel, fmt) > -20][:n]


def line(s):
    extra = s.get("route") or ""
    return f"[{s['family']}] {s['id']} - {s.get('name', '')}: {s.get('what', '')[:150]}" + (f"\n      how: {extra[:160]}" if extra else "")


def bundle(items, s):
    """Cross-family pairing for one style: what to combine it with."""
    by = {x["id"]: x for x in items}
    out = [s]
    for fam, ids in (s.get("pairs") or {}).items():
        if isinstance(ids, str):
            out.append({"family": "creator", "id": ids, "name": "StyleCard", "what": f"/style {ids} -> editor.py preset from-stylecard \"{ids}\" for a measured edit preset"})
            continue
        out += [by[i] for i in ids if i in by]
    if s["family"] == "edit":  # reverse lookups: which script/animation styles point at this preset
        out += [x for x in items if s["id"] in sum([v for v in (x.get("pairs") or {}).values() if isinstance(v, list)], [])][:4]
    return out


def which_families(platform, goal, fmt):
    g = f"{goal or ''} {fmt or ''}".lower()
    fams = []
    if re.search(r"carousel|slides|document|pdf|infographic", g):
        fams.append("carousel")
    if platform == "linkedin":
        fams.append("linkedin")
    if re.search(r"animat|cartoon|stickman|faceless|explainer|doodle|whiteboard|3d|anime|clay", g):
        fams.append("animation")
    if re.search(r"script|hook|write|post|caption|story|voice|tone", g) or not fams:
        fams.append("script")
    if re.search(r"edit|footage|video|reel|short|talking|clip|ugc|vlog", g) or not re.search(r"carousel|document|post only", g):
        fams.append("edit")
    return list(dict.fromkeys(fams))


def offer(items, brand=None, platform=None, goal="", fmt=None, funnel=None, n=3):
    fams = which_families(platform, goal, fmt)
    res = {f: rank(items, goal, f, brand, platform, funnel, fmt, n) for f in fams}
    return fams, res


def build(items):
    (REPO / "styles").mkdir(exist_ok=True)
    idx = [{k: s.get(k) for k in ("id", "family", "name", "aliases", "what", "brands", "platforms", "funnel", "route", "compliance") if s.get(k) is not None} for s in items]
    (REPO / "styles" / "index.json").write_text(json.dumps(idx, indent=1, ensure_ascii=False), encoding="utf-8")
    md = ["# Style menu (generated by `python scripts/styles.py build` - edit the sources, not this file)", "",
          "Pick by number or name, or say \"show me <family> styles\". Agents offer the top 3 from `styles.py offer` when a request has no style.",
          "A style is a starting point. Precedence still holds: ledger > brand file > Klaus's brief > style > model defaults.",
          "Script styles borrow STRUCTURE only: never a creator's catchphrases, voice clone or implied endorsement.", ""]
    names = {"edit": "Edit styles (auto-editor presets)", "script": "Script / voice styles", "animation": "Animated & faceless styles",
             "carousel": "Carousel archetypes (cards engine)", "linkedin": "LinkedIn formats"}
    for fam in FAMILIES:
        rows = [s for s in items if s["family"] == fam]
        md += [f"## {names[fam]} ({len(rows)})", "", "| id | style | use for | brands | aka |", "|---|---|---|---|---|"]
        for s in rows:
            aka = ", ".join(a for a in s.get("aliases", [])[:3] if a != s["id"].replace("-", " "))
            md.append(f"| `{s['id']}` | {s.get('name', '')} | {s.get('what', '')[:110].replace('|', '/')} | {', '.join(s.get('brands', []))[:60]} | {aka} |")
        md.append("")
    md += ["## Creator StyleCards", "", "Specific creators (Hormozi, Night Owl Cinematics, Jun Yuh...): `/style <creator>` reads the Supabase StyleCard; "
           "`editor.py preset from-stylecard <name>` turns it into a `style-<creator>` edit preset. `styles.py show <creator>` gives the script + edit pairing.", ""]
    (REPO / "styles" / "STYLE_MENU.md").write_text("\n".join(md), encoding="utf-8")
    return len(idx)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    for name in ("offer", "find"):
        p = sp.add_parser(name)
        if name == "find":
            p.add_argument("query", nargs="?", default="")
            p.add_argument("--family", choices=FAMILIES)
        p.add_argument("--brand"); p.add_argument("--platform"); p.add_argument("--goal", default=""); p.add_argument("--format", dest="fmt")
        p.add_argument("--funnel"); p.add_argument("-n", type=int, default=3 if name == "offer" else 5); p.add_argument("--json", action="store_true")
    p = sp.add_parser("show"); p.add_argument("key"); p.add_argument("--json", action="store_true")
    p = sp.add_parser("list"); p.add_argument("--family", choices=FAMILIES)
    sp.add_parser("build")
    a = ap.parse_args(argv)
    items = load()
    plat = PLATFORM_ALIASES.get((getattr(a, "platform", None) or "").lower(), getattr(a, "platform", None))
    if a.cmd == "build":
        print(f"styles/index.json + styles/STYLE_MENU.md: {build(items)} styles"); return
    if a.cmd == "list":
        for s in items:
            if not a.family or s["family"] == a.family:
                print(f"{s['family']:10} {s['id']:26} {s.get('name', '')}")
        return
    if a.cmd == "show":
        hits = resolve(items, a.key)
        if not hits:
            print(f"No style '{a.key}'. Try: styles.py find \"{a.key}\"  (or /style {a.key} for a creator StyleCard)"); sys.exit(1)
        out = bundle(items, hits[0])
        if a.json:
            print(json.dumps(out, indent=1, ensure_ascii=False)); return
        s = hits[0]
        print(json.dumps(s, indent=1, ensure_ascii=False))
        if len(out) > 1:
            print("\nPairs well with:")
            for x in out[1:]:
                print("  " + line(x))
        return
    if a.cmd == "find":
        res = rank(items, a.query or a.goal, a.family, a.brand, plat, a.funnel, a.fmt, a.n)
        if a.json:
            print(json.dumps(res, indent=1, ensure_ascii=False)); return
        for i, s in enumerate(res, 1):
            print(f"{i}. " + line(s))
        return
    if a.cmd == "offer":
        fams, res = offer(items, a.brand, plat, a.goal, a.fmt, a.funnel, a.n)
        if a.json:
            print(json.dumps(res, indent=1, ensure_ascii=False)); return
        k = 0
        for f in fams:
            print(f"\n{f.upper()}")
            for s in res[f]:
                k += 1
                print(f"  {k}. {s['id']} - {s.get('name', '')}: {s.get('what', '')[:120]}")
        if a.brand in HEALTH:
            print("\n(health brand: options carrying a 'not for health' lock were removed; SG health pack still applies to whatever is picked)")


if __name__ == "__main__":
    main()
