#!/usr/bin/env python3
"""Shot-spec harness for Higgsfield.

  python compile_shots.py validate spec.json        # lint before spending credits
  python compile_shots.py compile  spec.json [--model ID] [--shot 1a]  # emit model-native payload (JSON); --shot = one named prompt

Shotlist data model (ai-video-playbook.md §10): `style_prefix` is glued to every prompt (change it once, it changes
everywhere); `scene_overrides` {scene: "lighting/grade override"} applies to shots with that `scene`; shots carry stable
ids (1a, 1b, 2a...) so revisions address one prompt ("edit 1a") while everything else stays locked.

Spec format: see templates/shot-spec.example.json
"""
import json, re, sys

WPS = 2.5          # comfortable spoken words per second
REACTION_PAD = 0.8 # seconds of breathing room after a line
LIMITS = {         # total duration (s) per generation, from live catalog 10 Oct 2026
    "kling3_0": (3, 15), "kling_o3_image_reference": (3, 15), "kling_o3_flf": (3, 15),
    "seedance_2_5": (4, 30), "seedance_2_0": (4, 15), "cinematic_studio_video_4_0": (4, 30),
    "cinematic_studio_video_v2": (3, 12), "minimax_h3": (4, 15),
}
MULTISHOT = {"kling_o3_image_reference", "kling_o3_flf", "cinematic_studio_video_v2"}
RISKY = [r"\bwet (crotch|shorts|spot)\b", r"\bleak(s|ing)?\b", r"\bcrotch\b", r"\bgroin\b", r"\bnaked\b", r"\bpee\b|\burin"]
NEG_PHRASES = [r"\bnever\b", r"\bdon'?t\b", r"\bnot looking\b", r"\bwithout\b"]
VAGUE_MOVES = re.compile(r"\b(dances?|dancing|fights?|fighting|celebrates?|works? out|exercis(?:es|ing))\b", re.I)
OWNERS = {"neutral", "A-POV", "B-POV", "C-POV", "D-POV"}

def load(p):
    with open(p) as f: return json.load(f)

def words(s): return len(re.findall(r"[A-Za-z0-9']+", s or ""))

def validate(spec):
    errs, warns = [], []
    shots = spec.get("shots", [])
    model = spec.get("model", "")
    if not spec.get("set_map"): errs.append("No set_map - geography will drift. Write a top-down floor plan.")
    if not spec.get("cast"): errs.append("No cast sheet - identities will drift.")
    if not spec.get("look"): warns.append("No look line - brand grade not locked.")
    total = sum(s.get("dur", 0) for s in shots)
    lo, hi = LIMITS.get(model, (0, 999))
    if total and not (lo <= total <= hi):
        errs.append(f"Total {total}s outside {model} range {lo}-{hi}s - split into multiple generations or change model.")
    if len(shots) > 1 and model and model not in MULTISHOT and model not in ("seedance_2_5","seedance_2_0","cinematic_studio_video_4_0"):
        warns.append(f"{len(shots)} shots on {model}: no native multi-shot - prefer kling_o3_* multi_shots or seedance 'cut to'.")
    if model in MULTISHOT and len(shots) > 6: errs.append("Kling multi-shot max 6 shots.")
    cast_tags = set((spec.get("cast") or {}).keys())
    ids = [s.get("id") for s in shots]
    for d in sorted({i for i in ids if ids.count(i) > 1}, key=str):
        errs.append(f"Shot id {d} is used twice - shot ids must be unique so revisions can address one prompt.")
    if len(shots) > 1 and not spec.get("style_prefix"):
        warns.append("No style_prefix - put the shared look/physics/acting/continuity rules in one prefix so a single edit updates every prompt.")
    for sc in (spec.get("scene_overrides") or {}):
        if not any(str(s.get("scene")) == str(sc) for s in shots):
            warns.append(f"scene_overrides['{sc}'] matches no shot (set shot.scene).")
    for s in shots:
        sid = s.get("id")
        owner = s.get("owner")
        if owner not in OWNERS: errs.append(f"Shot {sid}: camera owner '{owner}' must be one of {sorted(OWNERS)} - bare 'POV' is ambiguous.")
        elif owner.endswith("-POV") and owner.split("-")[0] not in cast_tags:
            errs.append(f"Shot {sid}: {owner} but no cast member {owner.split('-')[0]}.")
        d = s.get("dialogue")
        if d:
            need = words(d.get("line")) / WPS + REACTION_PAD
            if s.get("dur", 0) < need:
                errs.append(f"Shot {sid}: line '{d.get('line')}' needs ~{need:.1f}s, shot is {s.get('dur')}s.")
            if d.get("speaker") not in cast_tags: errs.append(f"Shot {sid}: speaker '{d.get('speaker')}' not in cast.")
            if not d.get("tone"): warns.append(f"Shot {sid}: no tone keyword for the line - lip-sync/expression will guess.")
        if s.get("dur", 0) < 1.5: warns.append(f"Shot {sid}: {s.get('dur')}s is very short for generative video.")
        text = " ".join(str(s.get(k, "")) for k in ("action", "angle"))
        for pat in RISKY:
            if re.search(pat, text, re.I): errs.append(f"Shot {sid}: moderation-risk wording ({pat}) - restage.")
        for pat in NEG_PHRASES:
            if re.search(pat, text, re.I): warns.append(f"Shot {sid}: negative phrasing ({pat}) - describe what IS visible instead.")
        if not s.get("move"): warns.append(f"Shot {sid}: no camera move stated (Kling defaults to static).")
        act = s.get("action", "")
        if VAGUE_MOVES.search(act) and act.count(",") + act.count(";") < 2:
            warns.append(f"Shot {sid}: '{VAGUE_MOVES.search(act).group(0)}' without beats - spell the moves out one by one (e.g. two head nods, shoulder roll, knee dip, finger snap).")
    if shots and shots[0].get("dur", 0) > 2.5: warns.append("Hook shot > 2.5s - first 1.5s must carry the visual hook.")
    # Asset Bible gate (Gate 4): every @handle a shot uses must exist and be approved
    assets = spec.get("assets")
    if assets is None and any(s.get("uses") for s in shots):
        import os, pathlib
        ap = pathlib.Path(spec.get("_dir", ".")) / "assets.json"
        if ap.exists(): assets = json.load(open(ap))
    for s in shots:
        for h in s.get("uses", []) or []:
            a = (assets or {}).get(h)
            if a is None: errs.append(f"Shot {s.get('id')}: asset {h} not in Asset Bible (assets.json).")
            elif not a.get("approved"): errs.append(f"Shot {s.get('id')}: asset {h} not visually approved yet (Gate 4).")
        if len(s.get("uses", []) or []) > 4: warns.append(f"Shot {s.get('id')}: >4 reference assets - identity may blur.")
    return errs, warns

def prefix_for(spec, s):
    """Global style prefix + the shot's scene override (if any)."""
    parts = [spec.get("style_prefix", "")]
    ov = (spec.get("scene_overrides") or {}).get(str(s.get("scene"))) if s.get("scene") is not None else None
    if ov: parts.append(f"Scene override: {ov}")
    return " ".join(p.strip() for p in parts if p).strip()

def shot_text(spec, s, first=False):
    cast = spec.get("cast", {})
    who = "; ".join(f"{k}: {v}" for k, v in cast.items()) if first else ", ".join(cast.keys())
    parts = [
        f"{s['size']}, camera owner {s['owner']}, {s.get('angle','')}, {s.get('lens','')} lens, {s.get('move','static')}",
        f"Characters - {who}",
        s.get("action", ""),
        f"Set: {spec.get('set_map','')}" if first else "Same set as shot 1, positions unchanged",
        spec.get("look", ""),
    ]
    d = s.get("dialogue")
    if d: parts.append(f'[{d["speaker"]}, {d.get("tone","")}]: "{d["line"]}"')
    if s.get("audio"): parts.append(f"Audio: {s['audio']}")
    parts.append(spec.get("continuity", ""))
    return ". ".join(p.strip().rstrip(".") for p in parts if p) + "."

def compile_spec(spec, model=None):
    model = model or spec.get("model", "kling_o3_image_reference")
    shots = spec["shots"]
    total = round(sum(s["dur"] for s in shots))
    if model in MULTISHOT:
        mp, t = [], 0.0
        for i, s in enumerate(shots):
            # models_explore advertises string_array, but the backend validates KlingMultiPrompt objects
            # {prompt, duration} (422 on strings, 10 Oct 2026). Trust the backend.
            pre = prefix_for(spec, s)
            mp.append({"prompt": (pre + " " if pre else "") + f"Shot {s['id']}: " + shot_text(spec, s, i == 0), "duration": s["dur"]})
            t += s["dur"]
        return {"model": model, "aspect_ratio": spec.get("aspect_ratio", "9:16"), "duration": total,
                "multi_shots": True, "multi_prompt": mp, "sound": "on", "mode": "std",
                "_note": "multi_prompt items = {prompt, duration} objects (backend-verified); std first, pro after QC PASS."}
    # single prompt w/ cut markers (Seedance / Cinema Studio)
    t, chunks = 0.0, []
    pre0 = spec.get("style_prefix", "").strip()
    if pre0: chunks.append(pre0)
    for i, s in enumerate(shots):
        ov = (spec.get("scene_overrides") or {}).get(str(s.get("scene"))) if s.get("scene") is not None else None
        chunks.append(("" if i == 0 else "Cut to: ") + f"[{t:.1f}-{t+s['dur']:.1f}s] " + (f"(Scene override: {ov}) " if ov else "") + shot_text(spec, s, i == 0))
        t += s["dur"]
    out = {"model": model, "aspect_ratio": spec.get("aspect_ratio", "9:16"), "duration": max(total, 4), "prompt": " ".join(chunks)}
    if model == "seedance_2_5": out.update({"mode": "omni_reference", "draft": True, "generate_audio": True})
    return out

if __name__ == "__main__":
    if len(sys.argv) < 3: print(__doc__); sys.exit(1)
    cmd, path = sys.argv[1], sys.argv[2]
    model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else None
    spec = load(path); spec.setdefault("_dir", __import__("os").path.dirname(os.path.abspath(path)) if False else __import__("os").path.dirname(__import__("os").path.abspath(path)))
    if model: spec["model"] = model
    if "--shot" in sys.argv:  # compile one named prompt (e.g. after "edit 1a"); the prefix still applies
        want = sys.argv[sys.argv.index("--shot") + 1]
        spec["shots"] = [s for s in spec.get("shots", []) if str(s.get("id")) == want]
        if not spec["shots"]: print(f"No shot with id {want}"); sys.exit(1)
    errs, warns = validate(spec)
    for e in errs: print("ERROR  ", e)
    for w in warns: print("WARN   ", w)
    if cmd == "validate":
        print("RESULT ", "FAIL" if errs else "PASS"); sys.exit(1 if errs else 0)
    if errs: print("Refusing to compile with errors."); sys.exit(1)
    print(json.dumps(compile_spec(spec, model), indent=2))
