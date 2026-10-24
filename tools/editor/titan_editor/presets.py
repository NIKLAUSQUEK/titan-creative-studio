"""Style presets, StyleCard -> preset conversion, and the brand guide (brands/<brand>.md §6).

Merge order (later wins, mirrors CLAUDE.md precedence): _defaults < preset < StyleCard preset < brand guide < recipe overrides.
"""
import copy, json, os, re
from pathlib import Path

from .common import REPO, TOOL, log, rjson, slug, wjson

PRESETS = TOOL / "presets"


def deep_merge(a, b):
    out = copy.deepcopy(a)
    for k, v in (b or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def list_presets():
    return [rjson(p) for p in sorted(PRESETS.glob("*.json")) if not p.name.startswith("_")]


def load_preset(name):
    base = rjson(PRESETS / "_defaults.json")
    p = PRESETS / f"{name}.json"
    if not p.exists():
        raise SystemExit(f"Unknown preset '{name}'. Available: " + ", ".join(x["name"] for x in list_presets()))
    return deep_merge(base, rjson(p))


# ---------------- StyleCard -> preset ----------------
COLOURS = {"yellow": "#FFE14D", "green": "#3CFF6E", "red": "#FF3B3B", "blue": "#3BA7FF", "pink": "#FF5FC8", "orange": "#FF9F1C",
           "purple": "#A970FF", "white": "#FFFFFF", "cyan": "#29E3FF"}


def _num(x, default=None):
    try:
        return float(re.findall(r"[\d.]+", str(x))[0])
    except Exception:
        return default


def stylecard_to_preset(card, base="talking-head-punchy"):
    """Deterministic: StyleCard dna strings -> concrete edit parameters (no Claude call)."""
    dna = card.get("dna", card)
    name = (card.get("creator") or {}).get("name") or dna.get("name") or "creator"
    p = {"name": "style-" + slug(name), "label": f"Edit like {name}", "kind": "stylecard", "base": base,
         "description": (dna.get("vibe") or "") + (" | signature: " + dna["signature"] if dna.get("signature") else ""),
         "source": {"creator": name, "sources": dna.get("sources", [])}}
    energy = _num(dna.get("energy"), 3) or 3
    avg = _num(dna.get("avg_shot_s"))
    pacing_txt = (dna.get("pacing") or "").lower()
    if not avg:
        avg = 1.2 if re.search(r"hyper|very fast|rapid", pacing_txt) else 4.0 if re.search(r"slow|long take|held", pacing_txt) else 2.2
    p["pacing"] = {"max_shot_s": round(max(1.0, avg * 1.8), 2), "remove_silence_over_s": 0.2 if avg < 1.6 else 0.35 if avg < 3.5 else 0.7,
                   "pad_s": 0.04 if avg < 1.6 else 0.08 if avg < 3.5 else 0.18,
                   "remove_fillers": "none" if re.search(r"pauses kept|keeps pauses|natural pauses", pacing_txt) else "hard"}
    cap = (dna.get("captions") or "").lower()
    c = {}
    if re.search(r"none|no caption", cap):
        c["enabled"] = False
    c["animation"] = "karaoke" if re.search(r"karaoke|highlight(ed)? word|word.by.word colou?r", cap) else \
        "pop" if re.search(r"pop|bounce|word.by.word|one word|1-2 word", cap) else \
        "fade" if re.search(r"fade|subtle", cap) else "static" if re.search(r"static|sentence", cap) else "pop"
    if re.search(r"one word|single word|1 word", cap):
        c["max_words"] = 1
    elif re.search(r"word.by.word|1-2|two word", cap):
        c["max_words"] = 2
    elif re.search(r"sentence|full line", cap):
        c["max_words"] = 6
    if re.search(r"top", cap):
        c["position_y"] = 0.22
    elif re.search(r"cent(er|re)|middle", cap):
        c["position_y"] = 0.55
    elif re.search(r"bottom|lower", cap):
        c["position_y"] = 0.72
    if re.search(r"caps|uppercase|all-caps", cap):
        c["uppercase"] = True
    if "emoji" in cap:
        c["emoji"] = True
    for word, hexv in COLOURS.items():
        if re.search(rf"{word}\s+(highlight|keyword|emphasis|accent)|(highlight|keyword|accent)\w*\s+(in\s+)?{word}", cap):
            c["highlight"] = hexv
    if re.search(r"serif", cap) and "sans" not in cap:
        c["font"] = "DejaVu Serif"
    p["captions"] = c
    zoom_every = 0 if re.search(r"no zoom|static|locked", (dna.get("camera") or "").lower() + pacing_txt) else round(max(1.2, avg * 1.4), 2)
    p["zoom"] = {"every_s": zoom_every, "scale": round(1.04 + 0.025 * energy, 3), "mode": "smooth" if re.search(r"push.in|slow zoom|ken burns", pacing_txt + (dna.get("camera") or "").lower()) else "snap"}
    snd = (dna.get("sound") or "").lower()
    sfxmap = {}
    for k in ("whoosh", "riser", "impact", "pop", "ding"):
        if k in snd or (k == "impact" and re.search(r"boom|bass drop|hit", snd)):
            sfxmap.setdefault("zoom" if k == "whoosh" else "hook" if k in ("impact", "riser") else "title", k)
    p["sfx"] = {"density_per_10s": round(0.3 * energy ** 1.3, 2), **({"map": sfxmap} if sfxmap else {})}
    p["music"] = {"energy": "high" if energy >= 4 else "low" if energy <= 2 else "mid", "db": -16 if energy >= 4 else -21 if energy <= 2 else -19}
    if re.search(r"no music|voice only|silence", snd):
        p["music"]["energy"] = "none"
    lt = (dna.get("lighting") or "").lower()
    g = {}
    if re.search(r"warm|golden|amber", lt):
        g["warmth"] = 0.05
    if re.search(r"cool|blue|teal", lt):
        g["warmth"] = -0.04
    if re.search(r"high contrast|crushed|punchy|moody", lt):
        g["contrast"] = 1.12
    if re.search(r"desaturat|muted|film", lt):
        g["saturation"] = 0.88
    if re.search(r"saturated|vivid|bright colou?r", lt):
        g["saturation"] = 1.15
    if "vignette" in lt:
        g["vignette"] = True
    p["grade"] = g
    p["broll"] = {"every_s": round(max(2.5, avg * 3), 1)}
    return p


def fetch_stylecard(name):
    """Supabase titan-os style_cards via REST env vars (same as style_lab.py); None if not configured."""
    import urllib.parse, urllib.request
    url, key = os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_ANON_KEY")
    if not (url and key):
        return None
    q = "style_cards?select=card_md,dna,style_creators!inner(id,name,category,country)&style_creators.name=ilike." + urllib.parse.quote(f"*{name}*")
    req = urllib.request.Request(f"{url}/rest/v1/{q}", headers={"apikey": key, "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        rows = json.loads(r.read() or b"[]")
    if not rows:
        return None
    row = rows[0]
    return {"creator": row.get("style_creators"), "dna": row.get("dna") or {}, "card_md": row.get("card_md")}


def cmd_preset(a):
    if a.action == "list":
        for p in list_presets():
            print(f"{p['name']:28} {p['kind']:9} {p.get('label', '')}")
        return
    if a.action == "show":
        print(json.dumps(load_preset(a.name), indent=2)); return
    if a.action == "from-stylecard":
        card = None
        if a.file:
            j = rjson(a.file)
            cards = j if isinstance(j, list) else [j]
            card = next((c for c in cards if not a.name or a.name.lower() in json.dumps(c.get("creator", {})).lower()), cards[0] if cards else None)
        else:
            card = fetch_stylecard(a.name)
        if not card:
            raise SystemExit("No StyleCard found. Pass --file <card.json | style_cards_export.json> or set SUPABASE_URL + key in this shell. "
                             "(In Claude Code: run /style <creator>, save the dna JSON to a file, then use --file.)")
        p = stylecard_to_preset(card, a.base)
        out = wjson(PRESETS / f"{p['name']}.json", p)
        log(f"preset written: {out}")
        print(json.dumps(p, indent=2))


# ---------------- brand guide ----------------
def brand_guide(brand):
    """Brand overrides for the edit. Prefers a ```edit-brand json block in brands/<brand>.md; else best-effort parse of §6."""
    f = REPO / "brands" / f"{brand}.md"
    if not brand or not f.exists():
        return {}, None
    text = f.read_text(encoding="utf-8")
    m = re.search(r"```edit-brand\s*\n(.*?)```", text, re.S)
    if m:
        g = json.loads(m.group(1))
        g.setdefault("_source", f"brands/{brand}.md edit-brand block")
        return g, text
    sec = re.search(r"## 6\.[^\n]*\n(.*?)(\n## |\Z)", text, re.S)
    body = sec.group(1) if sec else text
    hexes = re.findall(r"#[0-9A-Fa-f]{6}\b", body)
    g = {"_source": f"brands/{brand}.md (heuristic parse; add an edit-brand block to make it exact)"}
    if hexes:
        g["colors"] = {"primary": hexes[0], "accent": hexes[1] if len(hexes) > 1 else hexes[0], "text": hexes[2] if len(hexes) > 2 else "#FFFFFF"}
    fonts = re.findall(r"([A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+){0,2}) (?:Italic|Bold|Regular|Medium|Sans|Serif|Display)", body)
    if fonts:
        g["fonts"] = {"display": fonts[0], "body": fonts[-1]}
    logo = re.search(r"(assets/[\w/\-]+\.(?:png|svg))", text)
    if logo:
        g["logo"] = {"path": logo.group(1), "position": "top-right", "size": 0.12, "opacity": 0.9}
    return g, text


def apply_brand(style, guide):
    """Turn a brand guide into style overrides (captions/hook fonts+colours, end card, safe zones)."""
    if not guide:
        return style
    s = copy.deepcopy(style)
    for k in ("captions", "hook_text", "lower_third", "end_card", "safe_zone", "grade", "compliance"):
        if isinstance(guide.get(k), dict):
            s[k] = deep_merge(s.get(k, {}), guide[k])
    if guide.get("fonts", {}).get("body") and "captions" not in guide:
        s["captions"]["font"] = guide["fonts"]["body"]
    if guide.get("colors", {}).get("accent") and "captions" not in guide:
        s["captions"]["highlight"] = guide["colors"]["accent"]
    if guide.get("logo"):
        s["logo"] = guide["logo"]
    if guide.get("colors"):
        s["colors"] = guide["colors"]
    if guide.get("fonts"):
        s["fonts"] = guide["fonts"]
    return s
