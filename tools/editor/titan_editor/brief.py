"""STRATEGIST FIRST: decide what the piece is for before cutting. Output: EDIT_BRIEF.md (1 page) + brief.json.

Inputs (all trimmed to what matters, to keep tokens low): ledger rules, brand file, brain profile, story-engine.md,
the brand's compliance packs, marketing strategy, Course Brain notes (if any), the ingest summary, the preset menu.
Modes: --llm claude-cli (one `claude -p` call on Klaus's login) | --llm none (local heuristic brief, zero tokens)
       | --pack-only (write brief_prompt.md so the Claude Code session itself writes brief.json; no nested call).
"""
import json, os, re
from pathlib import Path

from .common import REPO, claude, log, parse_json, rjson, studio, wjson
from .ingest import hook_shortlist, load_clips
from .presets import brand_guide, list_presets

PLATFORMS = {"tiktok": ("9:16", [15, 60]), "reels": ("9:16", [15, 60]), "shorts": ("9:16", [15, 58]), "youtube": ("16:9", [240, 900]),
             "linkedin": ("1:1", [30, 90]), "feed": ("4:5", [15, 60]), "facebook": ("4:5", [15, 60]), "x": ("16:9", [15, 140])}
GOALS = ["wise", "expert", "trust", "sell", "founder", "entertain"]
STOP = set("a an the and or but so to of in on at for with is are was were be been it this that i you we he she they my your our me "
           "just really very do does did not no yes can will would could should have has had from as by about what when how why "
           "there their them then than if because like um uh okay right gonna get got its it's i'm you're don't".split())
SCHEMA = {
    "goal": "|".join(GOALS), "audience": "who exactly, in one line", "platform": "|".join(PLATFORMS), "aspect": "9:16|1:1|16:9|4:5",
    "extra_aspects": ["other aspects to render from the same recipe"], "target_s": "seconds (number)", "preset": "one preset name from the menu",
    "trope_stance": "agree|challenge|subvert|flip|both + the trope, or null", "structure": "short|story-lesson|myth-buster|founder|long|parable|ugc-<type>",
    "hooks": [{"rank": 1, "text": "hook (<=12 words)", "formula": "contrarian|confession|cold-open|curiosity|outcome-twist|question|number|pattern-interrupt",
               "source": "footage (verbatim line) | text-overlay | new-vo", "clip": "clip id if footage", "t0": 0.0, "t1": 0.0, "why": ""}],
    "beats": [{"beat": "hook|context|turn|lesson|proof|cta|...", "purpose": "", "clip": "clip id", "t0": 0.0, "t1": 0.0,
               "line": "verbatim kept line(s) from the summary", "on_screen_text": "or null", "broll_query": "short visual description or null", "sfx": "or null",
               "role": "hook|context|body|example|proof|turn|lesson|payoff|cta (the expander only reorders/drops context/body/example/proof)", "fixed": "true if this beat must not move",
               "visual": {"type": "none|own_broll|me (the speaker in other footage)|person (an enrolled person)|web_image (licensed photo of a named thing/place/person)|text_card",
                          "query": "literal visual (3-8 concrete words)", "metaphor": "a visual metaphor for the idea, or null", "person": "enrolled name or null",
                          "entity": "named product/place/person to fetch if own footage lacks it, or null", "real_person": "true if entity is a real person (editorial only)"}}],
    "cta": {"spoken": "", "on_screen": "", "end_card": ""}, "compliance": ["rule that bites + how this edit obeys it"],
    "sound": {"vibe": "", "energy": "none|low|mid|high", "licence_rule": "brand=licensed/original only; personal=trending in-app"},
    "assumptions": ["anything you assumed"]}


def _read(p, limit=None):
    p = Path(p)
    if not p.exists():
        return ""
    t = p.read_text(encoding="utf-8", errors="replace")
    return t[:limit] + ("\n[...truncated]" if limit and len(t) > limit else "") if limit else t


def ledger_rules():
    t = _read(REPO / "ledger" / "learnings.md")
    keep = [l for l in t.splitlines() if re.match(r"- \[(edit|hook|sfx|render|legal|quality|audio|cta|locale|script|rule|process|brand|captions?)\]", l)]
    return "\n".join(keep[:40])


def compliance_text(brand_text):
    t = _read(REPO / ".claude/skills/marketing-engine/references/compliance-packs.md")
    out = []
    a = re.search(r"## A\..*?(?=\n## B\.)", t, re.S)
    if a:
        out.append(a.group(0))
    bt = (brand_text or "").lower()
    keys = {"health": "Health", "clinic": "Health", "physio": "Health", "supplement": "Supplements", "protein": "Supplements", "fitness": "Fitness",
            "gym": "Fitness", "weight": "Fitness", "beauty": "Beauty", "cosmetic": "Beauty", "finance": "Finance", "crypto": "Finance",
            "alcohol": "Alcohol", "food": "Food", "property": "Real estate", "course": "Education", "coaching": "Education", "legal": "Legal",
            "dating": "Dating", "sexual": "Dating", "recruit": "Employment"}
    for k, title in keys.items():
        if k in bt:
            m = re.search(rf"### {title}.*?(?=\n### |\n## )", t, re.S)
            if m and m.group(0) not in out:
                out.append(m.group(0))
    for country in ("Singapore", "Malaysia", "Vietnam", "Thailand", "Indonesia", "Philippines", "Australia", "United Kingdom", "United States", "India", "Nigeria"):
        if country.lower() in bt or (country == "Singapore" and re.search(r"\bSG\b", brand_text or "")):
            out += [l for l in t.splitlines() if l.startswith(f"| {country}") or (country in ("Indonesia", "Vietnam", "Thailand") and "Indonesia / Vietnam" in l)]
    if re.search(r"singapore|\bSG\b", brand_text or "", re.I) and re.search(r"health|clinic|physio", bt):
        out.append(_read(REPO / ".claude/skills/marketing-engine/references/compliance-sg.md", 2500))
    return "\n".join(dict.fromkeys(out))


def course_brain(path=None):
    cands = [Path(p) for p in [path, os.environ.get("TITAN_COURSE_BRAIN")] if p] + list(REPO.glob("**/Course Brain"))
    for d in cands:
        if d.is_dir():
            parts = [_read(d / n, 2500) for n in ("Apply to TITAN.md", "Templates and Prompts.md", "00 Home.md")]
            txt = "\n".join(x for x in parts if x)
            if txt:
                return f"(from {d})\n" + txt
    return ""


def context_pack(a, edit_dir):
    brand = a.brand or studio("active_brand")
    who = a.brain or studio("active_brain")
    _, brand_text = brand_guide(brand)
    presets = "\n".join(f"- {p['name']}: {p.get('description', '')[:140]}" for p in list_presets())
    parts = {
        "ASK FROM KLAUS": a.ask or "(none given: infer the best use of this footage)",
        "LEDGER RULES (highest precedence)": ledger_rules(),
        f"BRAND FILE brands/{brand}.md": brand_text or "(no brand file: run /onboard first; assume a generic brand and say so)",
        f"BRAIN brains/{who}/identity/profile.md (voice)": _read(REPO / "brains" / who / "identity" / "profile.md", 3000),
        "STORY ENGINE (goal, trope stance, hooks, structures)": _read(REPO / ".claude/skills/creator-brain/references/story-engine.md", 6000),
        "COMPLIANCE PACKS THAT APPLY": compliance_text(brand_text),
        "MARKETING STRATEGY": _read(REPO / "marketing" / "strategy" / f"{brand}.md", 3500),
        "COURSE BRAIN FRAMEWORKS": course_brain(getattr(a, "course_brain", None)),
        "PLATFORM DEFAULTS": json.dumps(PLATFORMS),
        "PRESET MENU": presets,
        "FOOTAGE (ingest summary: kept lines with source timestamps, dropped retakes, hook shortlist)": _read(edit_dir / "ingest" / "summary.md", 14000),
    }
    return brand, who, "\n\n".join(f"=== {k} ===\n{v}" for k, v in parts.items() if v)


PROMPT = """You are TITAN's content strategist and edit planner. Decide what this piece is FOR before anyone cuts it.
Use ONLY the footage lines given (verbatim, with their clip id and timestamps); never invent lines that are not in the footage.
A hook can be a footage line (source=footage), an on-screen text overlay (text-overlay) or a short new VO line (new-vo, flag it).
Respect precedence: ledger > brand file + brain voice > Klaus's ask > preset > defaults. Apply every compliance pack rule to hooks,
captions, on-screen text and CTA. Pick the preset from the menu that best fits the goal and footage. Beats must be in playback order,
each mapped to a clip range from the footage; add a broll_query (3-8 concrete visual words) where a cutaway helps.
For every beat choose a visual that makes the LINE land (literal for things, a metaphor for ideas, 'me' for personal moments, web_image only for a named
thing/place the footage can't show; never a real person in a sell piece). Mark roles so variants can shorten/reorder without breaking the story.
Rank exactly 5 hooks. Return ONLY one JSON object with exactly these keys:
{schema}

{context}
"""


def heuristic_brief(a, edit_dir, brand):
    clips = load_clips(edit_dir)
    hooks = hook_shortlist(clips, 5)
    plat = a.platform or "tiktok"
    aspect, rng = PLATFORMS.get(plat, ("9:16", [15, 60]))
    beats = []
    for c in clips:
        for s in c["an"]["sentences"]:
            if s.get("best") and not s.get("throat_clearing"):
                words = [w for w in re.findall(r"[a-zA-Z']+", s["text"].lower()) if w not in STOP and len(w) > 2]
                entity = next((m for m in re.findall(r"(?<=\s)([A-Z][a-zA-Z0-9]+(?:\s[A-Z][a-zA-Z0-9]+)*)", s["text"]) if m not in ("I", "I'm", "OK")), None)
                personal = bool(re.search(r"\b(I|I'm|I've|my|me)\b", s["text"]))
                q = " ".join(words[:5]) or None
                beats.append({"beat": "body", "purpose": "", "clip": c["id"], "t0": s["t0"], "t1": s["t1"], "line": s["text"],
                              "on_screen_text": None, "broll_query": q, "sfx": None, "role": "body", "fixed": False,
                              "visual": {"type": ("me" if personal else "own_broll") if q else "none", "query": q, "metaphor": None, "person": None,
                                         "entity": entity, "real_person": False}})
    if hooks and beats and (beats[0]["clip"], beats[0]["t0"]) != (hooks[0]["clip"], hooks[0]["t0"]) and hooks[0]["score"] >= 1.5:
        i = next((k for k, b in enumerate(beats) if (b["clip"], b["t0"]) == (hooks[0]["clip"], hooks[0]["t0"])), None)
        if i is not None:
            beats.insert(0, beats.pop(i))
    if beats:
        beats[0]["beat"] = beats[0]["role"] = "hook"; beats[0]["on_screen_text"] = None; beats[0]["fixed"] = True
        beats[0]["visual"] = {"type": "none"}
        if len(beats) > 2:
            beats[-1]["beat"] = beats[-1]["role"] = "cta"; beats[-1]["fixed"] = True
            beats[-1]["visual"] = {"type": "none"}; beats[-1]["broll_query"] = None  # stay on the face for the ask
        beats[0]["broll_query"] = None  # never cut away from the face on the hook
    _, brand_text = brand_guide(brand)
    comp = [l.strip("- ").strip() for l in (brand_text or "").splitlines() if "COMPLIANCE" in l or l.strip().startswith("- Don't")]
    return {"goal": a.goal or "expert", "audience": "[draft] from brand file", "platform": plat, "aspect": a.aspect or aspect,
            "extra_aspects": [x for x in ("9:16", "1:1", "16:9") if x != (a.aspect or aspect)],
            "target_s": a.target_s or round(max(rng[0], min(rng[1], sum(b["t1"] - b["t0"] for b in beats) + 2))),
            "preset": a.preset or "talking-head-punchy", "trope_stance": None, "structure": "short",
            "hooks": [{"rank": i + 1, "text": h["text"], "formula": h["formula"], "source": "footage", "clip": h["clip"], "t0": h["t0"], "t1": h["t1"],
                       "why": ", ".join(h["why"])} for i, h in enumerate(hooks)],
            "beats": beats, "cta": {"spoken": "", "on_screen": "", "end_card": ""},
            "compliance": comp or ["apply the brand's compliance pack (no pack found in brand file)"],
            "sound": {"vibe": "", "energy": "mid", "licence_rule": "brand=licensed/original only; personal=trending in-app"},
            "assumptions": ["heuristic brief (--llm none): best takes in recorded order, top-scoring hook moved first as a cold open; "
                            "rerun with --llm claude-cli or let the Claude Code session refine brief.json"]}


def render_md(b, brand):
    L = [f"# Edit brief — {brand}", "",
         f"**Goal:** {b.get('goal')}  ·  **Audience:** {b.get('audience')}  ·  **Platform/aspect:** {b.get('platform')} {b.get('aspect')} "
         f"(+ {', '.join(b.get('extra_aspects') or []) or 'none'})  ·  **Target:** {b.get('target_s')} s  ·  **Preset:** {b.get('preset')}",
         f"**Structure:** {b.get('structure')}  ·  **Trope stance:** {b.get('trope_stance') or '—'}", "", "## Hooks (ranked)"]
    for h in b.get("hooks", []):
        src = f"{h.get('clip')} {h.get('t0')}-{h.get('t1')}" if h.get("source") == "footage" else h.get("source")
        L.append(f"{h.get('rank')}. \"{h.get('text')}\" — {h.get('formula')} [{src}] {h.get('why') or ''}")
    L += ["", "## Beats", "| # | beat | source | line | on-screen | B-roll | sfx |", "|---|---|---|---|---|---|---|"]
    for i, x in enumerate(b.get("beats", []), 1):
        L.append(f"| {i} | {x.get('beat')} | {x.get('clip')} {x.get('t0')}-{x.get('t1')} | {(x.get('line') or '')[:90]} | {x.get('on_screen_text') or ''} | {x.get('broll_query') or ''} | {x.get('sfx') or ''} |")
    c = b.get("cta") or {}
    L += ["", f"**CTA:** spoken: {c.get('spoken') or '—'} · on-screen: {c.get('on_screen') or '—'} · end card: {c.get('end_card') or '—'}", "", "## Compliance"]
    L += [f"- {x}" for x in b.get("compliance", [])]
    s = b.get("sound") or {}
    L += ["", f"**Sound:** {s.get('vibe') or '—'} · energy {s.get('energy')} · {s.get('licence_rule')} (run /sound for the market plan)", ""]
    if b.get("assumptions"):
        L += ["## Assumptions"] + [f"- {x}" for x in b["assumptions"]]
    return "\n".join(L) + "\n"


def validate_brief(b, edit_dir):
    ids = {c["id"]: c for c in load_clips(edit_dir)}
    errs = []
    for x in b.get("beats", []):
        if x.get("clip") not in ids:
            errs.append(f"beat clip {x.get('clip')} not in ingest")
        elif not (0 <= float(x.get("t0", 0)) < float(x.get("t1", 0)) <= (ids[x["clip"]]["meta"].get("duration") or 1e9) + 0.5):
            errs.append(f"beat {x.get('beat')} has a bad range {x.get('t0')}-{x.get('t1')}")
    if b.get("goal") not in GOALS:
        errs.append(f"goal must be one of {GOALS}")
    return errs


def cmd_brief(a, edit_dir):
    brand, who, ctx = context_pack(a, edit_dir)
    if a.pack_only or a.llm == "pack":
        p = edit_dir / "brief_prompt.md"
        p.write_text(PROMPT.format(schema=json.dumps(SCHEMA, indent=1), context=ctx), encoding="utf-8")
        log(f"prompt pack -> {p} ({len(ctx) // 4} tokens approx). Write brief.json from it, then: editor.py brief --from-json brief.json")
        return
    if a.from_json:
        b = rjson(a.from_json)
    elif a.llm == "claude-cli":
        log(f"strategist: one claude -p call (~{len(ctx) // 4} input tokens)")
        b = parse_json(claude(PROMPT.format(schema=json.dumps(SCHEMA, indent=1), context=ctx), model=a.claude_model, step="brief"))
    else:
        b = heuristic_brief(a, edit_dir, brand)
    for k in ("platform", "aspect", "preset", "goal", "target_s"):
        if getattr(a, k, None):
            b[k] = getattr(a, k)
    errs = validate_brief(b, edit_dir)
    if errs:
        log("brief warnings: " + "; ".join(errs))
    b["brand"], b["brain"] = brand, who
    wjson(edit_dir / "brief.json", b)
    (edit_dir / "EDIT_BRIEF.md").write_text(render_md(b, brand), encoding="utf-8")
    log(f"brief -> {edit_dir / 'EDIT_BRIEF.md'}")
    return b
