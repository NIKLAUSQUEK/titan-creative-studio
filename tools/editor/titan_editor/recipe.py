"""EDIT RECIPE: the video is data. edit.v1.json, edit.v2.json ... Claude edits ONLY this; render.py turns it into pixels.

Recipe keys (times in seconds):
  version, parent, note, created, approved, brand, preset, project
  outputs:   [{"aspect": "9:16"}, {"aspect": "1:1"}, ...]          first = master aspect
  style:     merged preset + StyleCard + brand guide (captions, hook_text, zoom, grade, sfx, music, end_card, safe_zone, logo)
  beats:     [{"i", "beat", "clip", "t0", "t1"}]                     source ranges from the brief (re-cut rebuilds items from these)
  items:     [{"id": "c01", "clip": <ingest id>, "in", "out", "beat", "speed": 1, "zoom": [{"at", "scale", "ease"}], "focus_x": 0.5}]
  broll:     [{"id": "b01", "path", "src_in", "dur", "anchor": {"item", "offset"}, "mode": "full|pip|greenscreen", "flag"}]
  texts:     [{"type": "hook|title|lower_third", "text", "anchor": {"item", "offset"}, "dur"}]
  captions:  {"enabled", "replace": {"word": "fix"}, "emphasis": ["words"], "hide": [[t0, t1] output time]}
  audio:     {"music": {"path", "licence": "original|licensed:<source>|in-app", "db", "duck"}, "sfx": [{"type", "anchor", "db"}], "loudness": -14}
  end_card:  {"enabled", "dur", "lines": [], "cta": ""}
Captions are derived at render time from ingest word timestamps of each item's range, so trims never break caption sync.
"""
import copy, json, re
from pathlib import Path

from .common import claude, log, now, parse_json, rjson, studio, wjson
from .ingest import load_clips
from .presets import apply_brand, brand_guide, deep_merge, load_preset

ASPECTS = {"9:16", "1:1", "16:9", "4:5", "2.39:1"}


# ---------------- versions ----------------
def versions(edit_dir):
    return sorted(int(m.group(1)) for p in edit_dir.glob("edit.v*.json") if (m := re.match(r"edit\.v(\d+)\.json$", p.name)))


def load(edit_dir, v=None):
    vs = versions(edit_dir)
    if not vs:
        raise SystemExit("No recipe yet: run `assemble` first")
    v = vs[-1] if v in (None, "latest") else int(v)
    r = rjson(edit_dir / f"edit.v{v}.json")
    if r is None:
        raise SystemExit(f"edit.v{v}.json not found (have: {vs})")
    return r


def save_new(edit_dir, r, note, parent=None):
    vs = versions(edit_dir)
    n = (vs[-1] + 1) if vs else 1
    r = copy.deepcopy(r)
    r.update({"version": n, "parent": parent if parent is not None else (vs[-1] if vs else None), "note": note, "created": now(), "approved": False})
    r.pop("approved_at", None)
    errs = validate(r, edit_dir)
    if errs:
        raise ValueError("recipe invalid: " + "; ".join(errs[:8]))
    p = wjson(edit_dir / f"edit.v{n}.json", r)
    log(f"saved {p.name}: {note}")
    return r


# ---------------- build ----------------
def resolve_style(preset, brand, overrides=None):
    style = load_preset(preset)
    guide, _ = brand_guide(brand)
    style = apply_brand(style, guide)
    return deep_merge(style, overrides or {})


def spans_for(words, t0, t1, pacing):
    """Keep-spans inside [t0, t1]: drop fillers and gaps longer than the silence threshold, pad each span."""
    gap_max, pad, fill = pacing.get("remove_silence_over_s", 0.35), pacing.get("pad_s", 0.08), pacing.get("remove_fillers", "hard")
    ws = [w for w in words if w["t1"] > t0 and w["t0"] < t1]
    if fill in ("hard", "all"):
        ws = [w for w in ws if w.get("filler") != "hard" and not (fill == "all" and w.get("filler"))]
    if not ws:
        return [(t0, t1)]
    spans, cur = [], [max(t0, ws[0]["t0"]), min(t1, ws[0]["t1"])]
    for w in ws[1:]:
        if w["t0"] - cur[1] > gap_max:
            spans.append(cur); cur = [w["t0"], min(t1, w["t1"])]
        else:
            cur[1] = min(t1, w["t1"])
    spans.append(cur)
    out = []
    for i, (a, b) in enumerate(spans):
        lo = max(max(0.0, t0 - pad) if i == 0 else spans[i - 1][1], a - pad)  # pad may reach just outside the beat so first/last phonemes survive
        hi = min(t1 + pad if i == len(spans) - 1 else spans[i + 1][0], b + pad)
        if out and lo - out[-1][1] < 0.04:
            out[-1] = (out[-1][0], hi)
        elif hi - lo > 0.12:
            out.append((round(lo, 3), round(hi, 3)))
    return out


def place_zooms(items, style):
    z = style.get("zoom", {})
    every, scale, mode = z.get("every_s", 0) or 0, z.get("scale", 1.08), z.get("mode", "snap")
    for k, it in enumerate(items):
        d = (it["out"] - it["in"]) / it.get("speed", 1)
        keys = []
        if mode == "drift":
            # alternate wide / close framing per shot, each drifting slowly the opposite way (premium moving talking head)
            wide = k % 2 == 0
            a, b = (z.get("wide", [1.04, 1.10]) if wide else z.get("close", [1.16, 1.22]))
            x0, x1 = (0.35, 0.65) if k % 4 in (0, 3) else (0.65, 0.35)
            keys = [{"at": 0.0, "scale": a, "x": x0, "y": 0.38 if wide else 0.3}, {"at": round(d, 3), "scale": b, "x": x1, "ease": "drift"}]
            it["zoom"] = keys
            continue
        if mode == "smooth" and every:
            keys = [{"at": 0.0, "scale": 1.0}, {"at": round(d, 3), "scale": scale, "ease": "linear"}]
        elif every:
            base = 1.0 if k % 2 == 0 else scale  # jump-cut punch: alternate framing on every cut
            keys = [{"at": 0.0, "scale": base}]
            t = every
            while t < d - 0.6:
                base = scale if base == 1.0 else 1.0
                keys.append({"at": round(t, 3), "scale": base}); t += every
        if k == 0 and z.get("on_hook", 1.0) not in (None, 1.0):
            keys = [{"at": 0.0, "scale": z["on_hook"]}] + [x for x in keys if x["at"] > 0]
        it["zoom"] = keys
    return items


def build_items(beats, clips_by_id, style):
    items = []
    for b in beats:
        c = clips_by_id[b["clip"]]
        dur = c["meta"].get("duration") or 1e9
        for a, z in spans_for(c["words"], float(b["t0"]), float(b["t1"]), style.get("pacing", {})):
            z = min(z, dur)
            items.append({"id": f"c{len(items) + 1:02d}", "clip": b["clip"], "in": a, "out": z, "beat": b["i"], "speed": 1.0, "focus_x": 0.5})
    return place_zooms(items, style)


def auto_sfx(r):
    """SFX cues by priority, spread over the edit, capped by the preset's density budget (editbymmh rulebook,
    research/refs-2026-10-25/editbymmh-sound.md): hook > reveal stacks (riser peaking on the cut + impact + sub, with a bed dip)
    > B-roll in > a share of cuts > titles/labels > punch-ins > the end. Gains vary +-2 dB so repeats don't sound stamped."""
    st = r["style"].get("sfx", {})
    mp, dens, db = st.get("map", {}), st.get("density_per_10s", 1.0), st.get("db", -12)
    total = sum((i["out"] - i["in"]) / i.get("speed", 1) for i in r["items"])
    budget = max(1, round(dens * total / 10)) if dens > 0 else 0
    starts, _ = item_starts(r)
    jitter = lambda k: ((k * 7919) % 5) - 2                    # deterministic -2..+2 dB
    pri = []                                                    # (priority, cue)

    stacks = st.get("stacks", {})

    def cue(kind, item, off, d, why, p):
        """A kind that names a stack (preset sfx.stacks) fires every member: own dB, optional probability p, optional pre-lap."""
        if kind in stacks:
            for j, m in enumerate(stacks[kind]):
                if m.get("p", 1) < 1 and ((len(pri) * 7 + j * 13) % 100) / 100 >= m["p"]:
                    continue
                pri.append((p, {"type": m["type"], "anchor": {"item": item, "offset": round(max(0.0, off + m.get("pre_lap_ms", 0) / 1000), 3)},
                                "db": m.get("db", d), "why": f"{why} [{kind} stack]"}))
            return
        pri.append((p, {"type": kind, "anchor": {"item": item, "offset": round(max(0.0, off), 3)}, "db": d, "why": why}))
    if r["items"] and mp.get("hook"):
        cue(mp["hook"], r["items"][0]["id"], 0.0, db + 2, "hook", 0)
    r["audio"]["dips"] = []
    every = st.get("reveal_every_s", 0)
    if every:                                                   # reveal stacks on beat turns, at most one per `every` seconds
        last, prev = -1e9, None
        for it in r["items"]:
            t = starts[it["id"]]
            turn = prev is not None and it.get("beat") != prev.get("beat") and (r["beats"][it["beat"]].get("beat") in ("turn", "lesson", "payoff", "reveal", "proof", "cta")
                                                                               if isinstance(it.get("beat"), int) and it["beat"] < len(r["beats"]) else True)
            if turn and t - last >= every and t > 2.0:
                if "reveal" in stacks:
                    cue("reveal", it["id"], 0.0, db, "reveal", 1)
                else:
                    cue("riser", it["id"], 0.0, db - 3, "reveal: riser peaks on the cut", 1)
                    cue("impact", it["id"], 0.0, db + 3, "reveal: impact", 1)
                    cue("bass", it["id"], 0.0, db + 1, "reveal: sub", 1)
                r["audio"]["dips"].append(round(t, 3)); last = t
            prev = it
    for b in r["broll"]:
        if mp.get("broll"):
            cue(mp["broll"], b["anchor"]["item"], b["anchor"]["offset"], db - 2, "broll in", 2)
    cov = st.get("cut_coverage", 0)
    if cov and mp.get("cut", mp.get("broll")):
        cuts = [it for it in r["items"][1:]]
        step = max(1, round(1 / cov))
        for k, it in enumerate(cuts[::step]):
            cue(mp.get("cut", mp.get("broll")), it["id"], 0.0, db - 4 + jitter(k), "cut", 3)
    if mp.get("title"):
        for k, t in enumerate(x for x in r["texts"] if x["type"] in ("title", "label")):
            cue(mp["title"], t["anchor"]["item"], t["anchor"].get("offset", 0), db - 3 + jitter(k), "title", 4)
    if mp.get("zoom"):
        for k, (i, at) in enumerate((it["id"], z["at"]) for it in r["items"] for z in it.get("zoom", []) if z["at"] > 0 and z.get("ease") != "linear"):
            cue(mp["zoom"], i, at, db - 2 + jitter(k), "punch-in", 5)
    if mp.get("end") and r["items"]:
        li = r["items"][-1]
        cue(mp["end"], li["id"], (li["out"] - li["in"]) / li.get("speed", 1) - 0.02, db - 2, "end", 1)
    # keep the best cues within budget, never two within min_gap of each other (stack members share a time on purpose)
    gap = st.get("min_gap_s", 0.12)
    chosen, times = [], []
    for p, c in sorted(pri, key=lambda x: x[0]):
        if len(chosen) >= budget:
            break
        t = starts.get(c["anchor"]["item"], 0) + c["anchor"]["offset"]
        stack = c["why"].startswith("reveal") or "stack]" in c["why"]
        if not stack and any(abs(t - u) < gap for u in times):
            continue
        chosen.append(c); times.append(t)
    return sorted(chosen, key=lambda c: starts.get(c["anchor"]["item"], 0) + c["anchor"]["offset"])


def assemble(edit_dir, preset=None, aspects=None, music=None, music_licence=None, note="assembled from brief"):
    brief = rjson(edit_dir / "brief.json")
    if not brief:
        raise SystemExit("No brief.json: run `brief` first")
    clips = {c["id"]: c for c in load_clips(edit_dir)}
    brand = brief.get("brand") or studio("active_brand")
    preset = preset or brief.get("preset") or "talking-head-punchy"
    style = resolve_style(preset, brand)
    beats = [{"i": i, "beat": b.get("beat"), "clip": b["clip"], "t0": float(b["t0"]), "t1": float(b["t1"])} for i, b in enumerate(brief.get("beats", [])) if b.get("clip") in clips]
    if not beats:
        raise SystemExit(f"brief.json has no beats that point at an ingested clip (known ids: {', '.join(clips) or 'none'}). Fix the clip ids in brief.json, then: brief --from-json brief.json")
    items = build_items(beats, clips, style)
    master = brief.get("aspect") or "9:16"
    outs = [master] + [x for x in (aspects or brief.get("extra_aspects") or []) if x != master]
    r = {"project": edit_dir.parent.name, "brand": brand, "preset": preset, "outputs": [{"aspect": a} for a in outs], "style": style,
         "beats": beats, "items": items, "broll": [], "texts": [], "chats": [], "captions": {"enabled": style["captions"].get("enabled", True), "replace": {}, "emphasis": [], "hide": []},
         "audio": {"music": {"path": music, "licence": music_licence, "db": style["music"].get("db", -19), "duck": style["music"].get("duck", True)},
                   "sfx": [], "loudness": -14},
         "end_card": {"enabled": style.get("end_card", {}).get("enabled", True), "dur": style.get("end_card", {}).get("dur_s", 2.0),
                      "lines": [x for x in [(brief.get("cta") or {}).get("end_card")] if x], "cta": (brief.get("cta") or {}).get("on_screen") or ""}}
    hook = next((h for h in brief.get("hooks", []) if h.get("rank") == 1), None)
    ht = style.get("hook_text", {})
    if items and ht.get("enabled"):
        text = (brief.get("headers") or [None])[0] or (brief.get("beats") or [{}])[0].get("on_screen_text")
        if not text and hook and hook.get("source") != "footage":
            text = hook.get("text")  # text-overlay / new-vo hooks go on screen; a spoken footage hook is already captioned
        if text:
            if "\n" not in text:
                words = text.split()
                text = " ".join(words[: ht.get("max_words", 7)]) + ("…" if len(words) > ht.get("max_words", 7) else "")
            _, body0 = item_starts({"items": items})
            persistent = ht.get("persistent")
            r["texts"].append({"type": "header" if persistent else "hook", "text": text, "anchor": {"item": items[0]["id"], "offset": 0.0},
                               "dur": round(body0, 2) if persistent else ht.get("dur_s", 2.6)})
    for bi, b in enumerate(brief.get("beats", [])):
        if b.get("label"):
            first = next((it for it in items if it["beat"] == bi), None)
            if first:
                r["texts"].append({"type": "label", "text": b["label"], "style": "label", "anchor": {"item": first["id"], "offset": 0.0},
                                   "dur": round(sum(it["out"] - it["in"] for it in items if it["beat"] == bi), 2)})
    for bi, b in enumerate(brief.get("beats", [])):
        ch = b.get("chat")                       # "what someone said" beat -> texting cutaway (chatanim.py)
        first = next((it for it in items if it["beat"] == bi), None)
        if ch and ch.get("messages") and first:
            r["chats"].append({"id": f"chat{len(r['chats']) + 1}", "anchor": {"item": first["id"], "offset": float(ch.get("offset", 0.3))},
                               "style": ch.get("style", "dark"), "dur": ch.get("dur"), "messages": ch["messages"]})
    for b in brief.get("beats", [])[1:]:
        if b.get("on_screen_text"):
            first = next((it for it in items if it["beat"] == brief["beats"].index(b)), None)
            if first:
                r["texts"].append({"type": "title", "text": b["on_screen_text"], "anchor": {"item": first["id"], "offset": 0.0}, "dur": 2.0})
    bc = rjson(edit_dir / "broll_candidates.json", {"beats": []})
    br = style.get("broll", {})
    last_at = -1e9
    web_used = []
    for b in bc["beats"]:
        if b.get("pick") is None:
            continue
        c = b["candidates"][b["pick"]]
        its = [it for it in items if it["beat"] == b["beat_i"]]
        if not its or (c.get("flag") and not b.get("allow_flagged")):
            continue
        start = sum((x["out"] - x["in"]) for x in items[: items.index(its[0])])
        if br.get("every_s") and start - last_at < br["every_s"] * 0.6:
            continue
        beat_len = sum(x["out"] - x["in"] for x in its)
        dur = round(min(br.get("max_dur_s", 2.5), max(br.get("min_dur_s", 1.0), beat_len * 0.6), c["duration"] or 99), 2)
        off = round(min(0.4, max(0.0, beat_len - dur) / 2), 2)
        src_in = max(0.0, min(c["best_t"] - dur / 2, (c["duration"] or 0) - dur)) if c["kind"] == "video" else 0.0
        r["broll"].append({"id": f"b{len(r['broll']) + 1:02d}", "path": c["path"], "kind": c["kind"], "src_in": round(src_in, 2), "dur": dur,
                           "anchor": {"item": its[0]["id"], "offset": off}, "mode": br.get("mode", "full"), "flag": c.get("flag"), "query": b["query"],
                           "people": list(c.get("people") or {}), "unknown_faces": c.get("unknown_faces") or 0,
                           "credit": c.get("credit"), "licence": c.get("licence"), "real_person": bool(c.get("real_person"))})
        if c.get("credit") and not str(c.get("licence", "")).lower().startswith(("cc0", "public")):
            r["texts"].append({"type": "credit", "text": c["credit"], "anchor": {"item": its[0]["id"], "offset": off}, "dur": dur})
        if c.get("credit"):
            web_used.append(c)
        last_at = start
    r["audio"]["sfx"] = auto_sfx(r)
    if style.get("transitions", {}).get("default") == "flicker":
        seen_b = set()
        for it in r["items"]:
            if it["beat"] not in seen_b:
                seen_b.add(it["beat"]); it["fx"] = ["flicker"]
    if style.get("music", {}).get("energy") == "drone" and not music:
        r["audio"]["sfx"].insert(0, {"type": "drone", "anchor": {"at": 0.0}, "db": -24, "why": "tension bed (synth, original)"})
    if style.get("beat_sync") and music:
        beat_sync(r, music)
    if web_used:
        from .webimg import attribution
        log(f"image credits -> {attribution(edit_dir, web_used)} (add to the caption)")
    return save_new(edit_dir, r, note, parent=None)


def music_onsets(path, min_gap=0.25):
    """Beat/onset times (s) of a music file: positive jumps in short-time energy, peak-picked. Local, no libraries beyond numpy."""
    import numpy as np
    from pathlib import Path as P
    from .ingest import load_audio
    a = load_audio(str(path), P(path).parent)
    if a is None or not len(a):
        return []
    hop = 160  # 10 ms at 16 kHz
    fr = a[: len(a) // hop * hop].reshape(-1, hop)
    e = np.log10((fr ** 2).mean(1) + 1e-9)
    flux = np.maximum(0, np.diff(e, prepend=e[0]))
    thr = flux.mean() + 1.5 * flux.std()
    out = []
    for i in range(1, len(flux) - 1):
        if flux[i] > thr and flux[i] >= flux[i - 1] and flux[i] >= flux[i + 1] and (not out or i * 0.01 - out[-1] >= min_gap):
            out.append(round(i * 0.01, 3))
    return out


def beat_sync(r, music, window=0.3):
    """Snap B-roll starts, label texts and SFX to the nearest music onset (beat-switch edits). Stores the onsets in the recipe."""
    onsets = music_onsets(music)
    r["audio"]["onsets"] = onsets[:400]
    if not onsets:
        return r
    starts, _ = item_starts(r)
    for coll in (r["broll"], [t for t in r["texts"] if t["type"] in ("label", "title")], r["audio"]["sfx"]):
        for x in coll:
            a = x["anchor"]
            if "item" not in a or a["item"] not in starts:
                continue
            t = starts[a["item"]] + a.get("offset", 0)
            near = min(onsets, key=lambda o: abs(o - t))
            if abs(near - t) <= window:
                a["offset"] = round(max(0.0, a.get("offset", 0) + near - t), 3)
    return r


# ---------------- timeline maths (shared with render) ----------------
def item_starts(r):
    t, out = 0.0, {}
    for it in r["items"]:
        out[it["id"]] = t
        t += (it["out"] - it["in"]) / it.get("speed", 1.0)
    return out, t


def at_of(r, anchor, starts=None):
    starts = starts or item_starts(r)[0]
    if "at" in anchor:
        return float(anchor["at"])
    return starts[anchor["item"]] + float(anchor.get("offset", 0)) if anchor.get("item") in starts else None


def validate(r, edit_dir):
    errs = []
    clips = {c["id"]: c for c in load_clips(edit_dir)}
    ids = set()
    if not r.get("items"):
        errs.append("no items")
    for it in r.get("items", []):
        if it["id"] in ids:
            errs.append(f"duplicate item id {it['id']}")
        ids.add(it["id"])
        c = clips.get(it.get("clip"))
        if not c:
            errs.append(f"{it['id']}: unknown clip {it.get('clip')}"); continue
        dur = c["meta"].get("duration") or 0
        if not (0 <= it["in"] < it["out"] <= dur + 0.05):
            errs.append(f"{it['id']}: in/out {it['in']}-{it['out']} outside 0-{dur}")
        if not 0.25 <= it.get("speed", 1) <= 4:
            errs.append(f"{it['id']}: speed out of range")
    for o in r.get("outputs", []):
        if o.get("aspect") not in ASPECTS:
            errs.append(f"bad aspect {o.get('aspect')}")
    for k in ("broll", "texts", "chats"):
        for x in r.get(k, []):
            a = x.get("anchor", {})
            if "at" not in a and a.get("item") not in ids:
                errs.append(f"{k} {x.get('id') or x.get('text', '')[:20]}: anchor item {a.get('item')} missing")
    for x in r.get("audio", {}).get("sfx", []):
        a = x.get("anchor", {})
        if "at" not in a and a.get("item") not in ids:
            errs.append(f"sfx anchor item {a.get('item')} missing")
    return errs


def prune_anchors(r):
    ids = {it["id"] for it in r["items"]}
    for k in ("broll", "texts", "chats"):
        r[k] = [x for x in r.get(k, []) if "at" in x["anchor"] or x["anchor"].get("item") in ids]
    r["audio"]["sfx"] = [x for x in r["audio"]["sfx"] if "at" in x["anchor"] or x["anchor"].get("item") in ids]
    return r


# ---------------- quick revisions (zero tokens) ----------------
def trim_start(r, secs):
    left = secs
    while r["items"] and left > 1e-6:
        it = r["items"][0]
        d = (it["out"] - it["in"]) / it.get("speed", 1)
        if d <= left + 0.05:
            left -= d; r["items"].pop(0)
        else:
            cut = left * it.get("speed", 1)
            it["in"] = round(it["in"] + cut, 3)
            for k in ("broll", "texts", "chats"):
                for x in r.get(k, []):
                    if x["anchor"].get("item") == it["id"]:
                        x["anchor"]["offset"] = round(max(0.0, x["anchor"]["offset"] - left), 3)
            for x in r["audio"]["sfx"]:
                if x["anchor"].get("item") == it["id"]:
                    x["anchor"]["offset"] = round(max(0.0, x["anchor"]["offset"] - left), 3)
            it["zoom"] = [dict(z, at=round(max(0.0, z["at"] - left), 3)) for z in it.get("zoom", [])]
            left = 0
    prune_anchors(r)
    if r["items"]:
        b0 = r["items"][0]["beat"]
        r["beats"] = [b for b in r["beats"] if b["i"] >= b0]
        for b in r["beats"]:
            if b["i"] == b0:
                b["t0"] = r["items"][0]["in"]
        if not any(t["type"] == "hook" for t in r["texts"]) and r["style"].get("hook_text", {}).get("enabled"):
            log("note: the hook text was on the trimmed part; add a new one with `revise \"hook text: ...\"`")
    return r


def trim_end(r, secs):
    left = secs
    while r["items"] and left > 1e-6:
        it = r["items"][-1]
        d = (it["out"] - it["in"]) / it.get("speed", 1)
        if d <= left + 0.05:
            left -= d; r["items"].pop()
        else:
            it["out"] = round(it["out"] - left * it.get("speed", 1), 3); left = 0
    return prune_anchors(r)


def recut(r, edit_dir):
    clips = {c["id"]: c for c in load_clips(edit_dir)}
    old_first = {}
    for it in r["items"]:
        old_first.setdefault(it["beat"], it["id"])
    r["items"] = build_items(r["beats"], clips, r["style"])
    new_first = {}
    for it in r["items"]:
        new_first.setdefault(it["beat"], it["id"])
    remap = {old_first[b]: new_first[b] for b in old_first if b in new_first}
    for coll in (r["broll"], r["texts"], r["audio"]["sfx"]):
        for x in coll:
            if x["anchor"].get("item") in remap:
                x["anchor"]["item"] = remap[x["anchor"]["item"]]
    return prune_anchors(r)


QUICK = [
    (r"(?:cut|trim|remove|drop)\s+(?:the\s+)?first\s+(\d+(?:\.\d+)?)\s*(?:s|sec|secs|seconds)\b", "trim_start"),
    (r"(?:cut|trim|remove|drop)\s+(?:the\s+)?last\s+(\d+(?:\.\d+)?)\s*(?:s|sec|secs|seconds)\b", "trim_end"),
    (r"(?:go\s+back|revert|roll\s*back|back)\s+to\s+v(?:ersion\s*)?(\d+)", "revert"),
    (r"\b(punchier|bigger|larger)\s+captions?\b", "captions_punchier"),
    (r"\bsmaller\s+captions?\b", "captions_smaller"),
    (r"\b(no|remove|kill|turn off)\s+captions?\b|\bcaptions?\s+off\b", "captions_off"),
    (r"\b(no|remove|kill)\s+music\b", "music_off"),
    (r"\bmusic\s+(louder|up)\b|\blouder\s+music\b", "music_up"),
    (r"\bmusic\s+(quieter|down|lower)\b|\bquieter\s+music\b", "music_down"),
    (r"\bmore\s+zooms?\b|\bmore\s+punch[- ]?ins?\b", "zoom_more"),
    (r"\b(fewer|less)\s+zooms?\b", "zoom_less"),
    (r"\bno\s+zooms?\b", "zoom_off"),
    (r"\b(no|fewer|less)\s+(sfx|sound effects|stims|whooshes)\b", "sfx_less"),
    (r"\bmore\s+(sfx|sound effects|stims|whooshes)\b", "sfx_more"),
    (r"\b(tighter|faster|snappier)\b(?:\s+(pace|pacing|cuts?))?", "tighter"),
    (r"\b(slower|breathe|more breathing room|keep (the )?pauses)\b", "looser"),
    (r"\bhook\s+text\s*[:=]\s*[\"“]?(.+?)[\"”]?\s*$", "hook_text"),
    (r"\b(?:only|just)\s+(9:16|1:1|16:9|4:5)\b", "only_aspect"),
    (r"\badd\s+(9:16|1:1|16:9|4:5)\b", "add_aspect"),
]


def quick_revise(r, instruction, edit_dir):
    """Apply every recognised phrase; returns (recipe, [applied ops], leftover_text)."""
    r = copy.deepcopy(r)
    applied, text = [], instruction
    for pat, op in QUICK:
        m = re.search(pat, text, re.I)
        if not m:
            continue
        arg = m.group(1) if m.groups() else None
        st = r["style"]
        if op == "revert":
            return load(edit_dir, int(arg)), [f"revert to v{arg}"], ""
        if op == "trim_start":
            trim_start(r, float(arg))
        elif op == "trim_end":
            trim_end(r, float(arg))
        elif op == "captions_punchier":
            c = st["captions"]; c["size"] = round(c["size"] * 1.15, 4); c["max_words"] = max(1, c.get("max_words", 3) - 1)
            c["animation"] = "pop" if c.get("animation") in ("static", "fade") else c["animation"]; c["keyword_caps"] = True
        elif op == "captions_smaller":
            st["captions"]["size"] = round(st["captions"]["size"] * 0.87, 4)
        elif op == "captions_off":
            r["captions"]["enabled"] = False
        elif op == "music_off":
            r["audio"]["music"]["path"] = None
        elif op == "music_up":
            r["audio"]["music"]["db"] += 3
        elif op == "music_down":
            r["audio"]["music"]["db"] -= 3
        elif op in ("zoom_more", "zoom_less", "zoom_off"):
            z = st["zoom"]
            z["every_s"] = 0 if op == "zoom_off" else round(max(1.0, (z.get("every_s") or 4) * (0.6 if op == "zoom_more" else 1.6)), 2)
            place_zooms(r["items"], st)
        elif op in ("sfx_less", "sfx_more"):
            st["sfx"]["density_per_10s"] = round(st["sfx"].get("density_per_10s", 1) * (0.4 if op == "sfx_less" else 1.8), 2)
            r["audio"]["sfx"] = auto_sfx(r)
        elif op in ("tighter", "looser"):
            p = st["pacing"]; f = 0.7 if op == "tighter" else 1.6
            p["remove_silence_over_s"] = round(max(0.15, p.get("remove_silence_over_s", 0.35) * f), 3)
            p["pad_s"] = round(max(0.02, p.get("pad_s", 0.08) * f), 3)
            recut(r, edit_dir); r["audio"]["sfx"] = auto_sfx(r)
        elif op == "hook_text":
            r["texts"] = [t for t in r["texts"] if t["type"] != "hook"]
            r["texts"].insert(0, {"type": "hook", "text": arg.strip(), "anchor": {"item": r["items"][0]["id"], "offset": 0.0}, "dur": st["hook_text"].get("dur_s", 2.6)})
        elif op == "only_aspect":
            r["outputs"] = [{"aspect": arg}]
        elif op == "add_aspect":
            if all(o["aspect"] != arg for o in r["outputs"]):
                r["outputs"].append({"aspect": arg})
        applied.append(op + (f"({arg})" if arg else ""))
        text = text[: m.start()] + " " + text[m.end():]
    leftover = re.sub(r"[\s,.;&]+|\band\b|\bthen\b|\balso\b|\bplease\b", " ", text, flags=re.I).strip()
    return r, applied, leftover


REVISE = """You are TITAN's editor. Apply Klaus's revision to this edit recipe and return the FULL new recipe as ONE JSON object (no prose).
Rules: change only what the revision asks; keep ids stable where possible; items reference ingest clip ids and SOURCE times (in/out within the clip);
overlays/sfx/texts anchor to an item id + offset in output seconds; captions are derived from word timestamps automatically (use captions.replace
/ captions.emphasis / captions.hide to adjust them). Never invent footage lines: only use lines from the footage list. Keep brand + compliance rules.
Recipe format notes:
{doc}

REVISION: {instruction}

FOOTAGE LINES AVAILABLE (clip id, source range, text):
{lines}

CURRENT RECIPE (v{v}):
{recipe}
"""


def footage_lines(edit_dir, r):
    used = {it["clip"] for it in r["items"]}
    L = []
    for c in load_clips(edit_dir):
        for s in c["an"]["sentences"]:
            if c["id"] in used or s.get("best"):
                L.append(f"{c['id']} [{s['t0']:.2f}-{s['t1']:.2f}]{'' if s.get('best') else ' (retake)'} {s['text']}")
    return "\n".join(L[:400])


def claude_revise(r, instruction, edit_dir, model=None):
    slim = {k: v for k, v in r.items() if k not in ("style",)}
    slim["style_summary"] = {k: r["style"].get(k) for k in ("captions", "hook_text", "zoom", "sfx", "music", "grade", "pacing", "broll")}
    prompt = REVISE.format(doc=__doc__.split("Recipe keys")[1], instruction=instruction, lines=footage_lines(edit_dir, r), v=r["version"], recipe=json.dumps(slim, ensure_ascii=False))
    for attempt in range(2):
        new = parse_json(claude(prompt, model=model, step="revise"))
        if "style_summary" in new:
            st = copy.deepcopy(r["style"])
            for k, v in new.pop("style_summary").items():
                if isinstance(v, dict):
                    st[k] = deep_merge(st.get(k, {}), v)
            new["style"] = st
        new.setdefault("style", r["style"])
        errs = validate(new, edit_dir)
        if not errs:
            return new
        prompt += f"\n\nYour last answer was invalid: {errs[:6]}. Fix and return the full recipe JSON again."
    raise ValueError(f"Claude revision invalid after retry: {errs}")


def cmd_assemble(a, edit_dir):
    assemble(edit_dir, a.preset, a.aspects.split(",") if a.aspects else None, a.music, a.music_licence)


def cmd_revise(a, edit_dir):
    r = load(edit_dir, a.base)
    new, applied, left = quick_revise(r, a.instruction, edit_dir)
    if left and len(left) > 3:
        if a.llm == "claude-cli":
            log(f"quick ops: {applied or 'none'}; sending the rest to Claude: '{left}'")
            new = claude_revise(new, a.instruction if not applied else left, edit_dir, a.claude_model)
            applied.append("claude")
        else:
            raise SystemExit(f"Not a quick op: '{left}'. Use --llm claude-cli, or (in a Claude Code session) edit the newest edit.v*.json by hand "
                             f"via `fork` then `validate`. Quick ops understood: trim first/last N s, go back to vN, punchier/smaller captions, "
                             f"captions off, music off/up/down, more/fewer/no zooms, more/less sfx, tighter/slower, hook text: ..., only/add <aspect>.")
    if not applied:
        raise SystemExit("Nothing changed.")
    parent = new["version"] if applied and applied[0].startswith("revert") else r["version"]
    save_new(edit_dir, new, f"{a.instruction}  [{', '.join(applied)}]", parent=parent)


def cmd_fork(a, edit_dir):
    r = load(edit_dir, a.base)
    save_new(edit_dir, r, a.message or f"fork of v{r['version']} for hand edit", parent=r["version"])


def cmd_validate(a, edit_dir):
    r = load(edit_dir, a.version)
    errs = validate(r, edit_dir)
    starts, total = item_starts(r)
    print(f"v{r['version']}: {len(r['items'])} items, {len(r['broll'])} B-roll, {len(r['texts'])} texts, {len(r['audio']['sfx'])} sfx, {total:.2f} s"
          + (f" + {r['end_card']['dur']} s end card" if r["end_card"].get("enabled") else ""))
    print("OK" if not errs else "ERRORS:\n- " + "\n- ".join(errs))
    if errs:
        raise SystemExit(1)


def cmd_versions(a, edit_dir):
    for v in versions(edit_dir):
        r = rjson(edit_dir / f"edit.v{v}.json")
        _, total = item_starts(r)
        print(f"v{v:<3} parent={str(r.get('parent')):4} {'APPROVED ' if r.get('approved') else ''}{total:6.2f}s  {r.get('created')}  {r.get('note')}")


def cmd_approve(a, edit_dir):
    r = load(edit_dir, a.version)
    r["approved"], r["approved_at"] = True, now()
    wjson(edit_dir / f"edit.v{r['version']}.json", r)
    log(f"v{r['version']} approved for final render")
