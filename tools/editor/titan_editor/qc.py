"""QC: scripts/qc_frames.py contact sheet + local measurable checks + optional Claude self-review against the brief and preset.
Writes <edit>/qc/QC_v<N>.md + qc_v<N>.json. Always LOOK at the contact sheets before calling anything done (studio rule).
"""
import json, re, subprocess, sys
from pathlib import Path

from .common import REPO, claude, ffmpeg, log, parse_json, rjson, run, wjson
from .ingest import load_clips
from .recipe import at_of, item_starts, load
from .render import caption_words

FORBID_HEALTH = ["best", "no.1", "no. 1", "#1", "number one", "leading", "most trusted", "guarantee", "guaranteed", "cure", "cured", "cures",
                 "miracle", "free consult", "free consultation", "discount", "% off", "promo", "testimonial", "100%", "permanent fix"]


def loudness(path):
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"])
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r.stderr)
    return (float(i[-1]) if i else None), (float(tp[-1]) if tp else None)


def silences(path, until):
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-t", f"{until:.2f}", "-af", "silencedetect=noise=-38dB:d=0.7", "-f", "null", "-"])
    return [float(x) for x in re.findall(r"silence_duration: ([\d.]+)", r.stderr)]


def black_start(path):
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-t", "1.5", "-i", str(path), "-vf", "blackdetect=d=0.2:pix_th=0.08", "-an", "-f", "null", "-"])
    return bool(re.search(r"black_start:0(\.0+)?\b", r.stderr))


def hook_sheet(path, out, secs=4, fps=2):
    ffmpeg(["-t", secs, "-i", path, "-vf", f"fps={fps},scale=180:-2,tile={secs * fps}x1", "-frames:v", 1, out], check=False)
    return out if Path(out).exists() else None


def full_sheet(path, out, dur, n=16):
    step = max(dur / n, 0.25)
    ffmpeg(["-i", path, "-vf", f"fps=1/{step:.3f},scale=180:-2,tile=8x2", "-frames:v", 1, out], check=False)
    return out if Path(out).exists() else None


def keyword_spoken(kw, words, until=3.0):
    """Start time of the first spoken occurrence of the phrase kw (all its tokens, in order) before `until`, else None."""
    norm = lambda t: re.sub(r"[^\w]", "", t.lower())
    toks = [norm(t) for t in kw.split() if norm(t)]
    ws = [(norm(w["w"]), w["t0"]) for w in words if w["t0"] < until]
    for i in range(len(ws) - len(toks) + 1):
        if toks and all(ws[i + j][0] == toks[j] for j in range(len(toks))):
            return round(ws[i][1], 2)
    return None


def compliance_scan(r, clips, brand_text):
    words = list((r["style"].get("compliance") or {}).get("forbid_words", []))
    if re.search(r"health|clinic|physio|medical", brand_text or "", re.I):
        words += FORBID_HEALTH
    if not words:
        return []
    text_parts = [("caption", " ".join(w["w"] for w in caption_words(r, clips)))] + [(t["type"], t["text"]) for t in r.get("texts", [])] + \
                 [("end card", " ".join(r["end_card"].get("lines") or []) + " " + (r["end_card"].get("cta") or ""))]
    hits = []
    for where, txt in text_parts:
        low = " " + txt.lower() + " "
        for w in set(words):
            if re.search(r"(?<![\w])" + re.escape(w.lower()) + r"(?![\w])", low):
                hits.append(f"{where}: '{w}'")
    return sorted(set(hits))


def run_qc(edit_dir, version=None, quality="draft", llm="none", claude_model=None):
    r = load(edit_dir, version)
    man = [x for x in rjson(edit_dir / "renders" / "renders.json", []) if x["version"] == r["version"] and x["quality"] == quality]
    if not man:
        raise SystemExit(f"No {quality} render for v{r['version']}: run `render` first")
    seen = {}
    for x in man:
        seen[x["aspect"]] = x
    man = list(seen.values())
    brief = rjson(edit_dir / "brief.json", {})
    clips = {c["id"]: c for c in load_clips(edit_dir)}
    brand_file = REPO / "brands" / f"{r.get('brand')}.md"
    brand_text = brand_file.read_text(encoding="utf-8") if brand_file.exists() else ""
    qd = edit_dir / "qc"
    qd.mkdir(exist_ok=True)
    starts, body = item_starts(r)
    st = r["style"]
    checks, sheets = [], []

    def chk(name, ok, detail=""):
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    for x in man:
        p = Path(x["path"])
        tag = f"v{r['version']}_{x['aspect'].replace(':', 'x')}"
        subprocess.run([sys.executable, str(REPO / "scripts" / "qc_frames.py"), str(p), "--out", str(qd / tag), "--frames", "3,20,40,60,80,97"],
                       capture_output=True, text=True)
        sheets += [str(s) for s in [qd / tag / "contact_sheet.jpg", hook_sheet(p, qd / f"{tag}_hook.jpg"), full_sheet(p, qd / f"{tag}_full.jpg", x["duration"])] if s and Path(s).exists()]
        I, TP = loudness(p)
        chk(f"[{x['aspect']}] loudness ≈ {r['audio'].get('loudness', -14)} LUFS", I is not None and abs(I - r["audio"].get("loudness", -14)) <= 2.0, f"I={I} LUFS, TP={TP} dBFS")
        chk(f"[{x['aspect']}] true peak ≤ -1 dBTP", TP is not None and TP <= -0.8, f"TP={TP}")
        long_sil = [s for s in silences(p, body) if s > 0.7]
        chk(f"[{x['aspect']}] no dead air > 0.7 s (before end card)", not long_sil or st["pacing"].get("remove_silence_over_s", 0.35) >= 0.7, f"{len(long_sil)} gap(s): {long_sil[:5]}")
        chk(f"[{x['aspect']}] first frame not black", not black_start(p))
    tgt = brief.get("target_s")
    total = man[0]["duration"]
    if tgt:
        chk("duration within target (+/-35%)", 0.5 * float(tgt) <= total <= 1.35 * float(tgt), f"{total:.1f} s vs target {tgt} s")
    cw = caption_words(r, clips)
    first_word = cw[0]["t0"] if cw else None
    chk("speech starts within 0.5 s (no throat-clearing)", first_word is not None and first_word <= 0.5, f"first word at {first_word}")
    hook = next((t for t in r["texts"] if t["type"] == "hook"), None)
    hat = at_of(r, hook["anchor"], starts) if hook else None
    chk("hook lands in first 0.5 s (text overlay or spoken line)", (hat is not None and hat <= 0.3) or (first_word is not None and first_word <= 0.5),
        f"overlay '{hook['text']}' at {hat}" if hook else f"spoken hook, first word at {first_word}")
    kw = (brief.get("search_keyword") or "").strip()
    if kw:
        said = keyword_spoken(kw, cw, until=3.0)
        chk("search keyword spoken in first 3 s (auto-captions + search; platform-signals.md §3)", said is not None, f"'{kw}' at {said} s" if said is not None else f"'{kw}' not heard before 3.0 s")
    sz = st.get("safe_zone", {})
    for nm, y in (("captions", st["captions"].get("position_y", 0.7)), ("hook text", st["hook_text"].get("position_y", 0.2))):
        chk(f"{nm} inside 9:16 safe zone", sz.get("top", 0.14) <= y <= 1 - sz.get("bottom", 0.2), f"y={y} (UI zones: top {sz.get('top')}, bottom {sz.get('bottom')})")
    flagged = [b["path"] for b in r["broll"] if b.get("flag")]
    chk("no consent-flagged B-roll", not flagged, "; ".join(flagged))
    from .render import music_ok
    ok, why = music_ok(r)
    chk("music licence OK for this account (or no music)", ok or not r["audio"]["music"].get("path"), why)
    hits = compliance_scan(r, clips, brand_text)
    chk("compliance word scan (brand pack)", not hits, "; ".join(hits))
    sfx_n = len(r["audio"].get("sfx", []))
    dens = st["sfx"].get("density_per_10s", 1)
    chk("SFX density matches preset", sfx_n <= max(2, dens * (total / 10) * 1.5 + 2), f"{sfx_n} cues for {total:.1f} s (preset {dens}/10 s)")
    review = None
    if llm == "claude-cli":
        prompt = (f"Self-review this draft edit against its brief and preset. LOOK at these images with your Read tool first: {', '.join(sheets)} "
                  f"(red = platform UI zones). Brief: {json.dumps({k: brief.get(k) for k in ('goal', 'platform', 'aspect', 'target_s', 'hooks', 'cta', 'compliance')}, ensure_ascii=False)[:3500]}\n"
                  f"Preset: {r['preset']} ({st.get('description', '')}). Measured checks: {json.dumps(checks)}\n"
                  "Return ONLY JSON: {\"verdict\": \"PASS|FIX\", \"score\": 0-10, \"issues\": [\"...\"], \"revisions\": [\"plain-English revision instructions the editor can apply, e.g. 'cut first 1.5 s', 'punchier captions'\"]}")
        try:
            review = parse_json(claude(prompt, image_dir=qd, model=claude_model))
        except Exception as e:
            review = {"verdict": "n/a", "issues": [f"self-review failed: {str(e)[:200]}"]}
    fails = [c for c in checks if not c["ok"]]
    verdict = "PASS" if not fails and (not review or review.get("verdict") == "PASS") else "FIX"
    L = [f"# QC v{r['version']} ({quality}) — {verdict}", "", f"Renders: " + ", ".join(f"{x['aspect']} {x['W']}x{x['H']} {x['duration']} s → `{x['path']}`" for x in man), "",
         "| check | ok | detail |", "|---|---|---|"] + [f"| {c['check']} | {'✅' if c['ok'] else '❌'} | {c['detail']} |" for c in checks]
    L += ["", "**Contact sheets (look at them):**"] + [f"- `{s}`" for s in sheets]
    if review:
        L += ["", f"## Self-review: {review.get('verdict')} ({review.get('score')}/10)"] + [f"- {i}" for i in review.get("issues", [])]
        if review.get("revisions"):
            L += ["", "Suggested revisions (apply with `revise`):"] + [f"- {x}" for x in review["revisions"]]
    L += ["", "Next: show Klaus the draft → his verdict + biggest miss → `/learn`. Revise with `revise \"...\"`; when approved: `approve` then `render --final`."]
    md = qd / f"QC_v{r['version']}_{quality}.md"
    md.write_text("\n".join(L) + "\n", encoding="utf-8")
    wjson(qd / f"qc_v{r['version']}_{quality}.json", {"verdict": verdict, "checks": checks, "sheets": sheets, "review": review})
    log(f"QC {verdict}: {len(fails)} failing check(s) -> {md}")
    return verdict, md


def cmd_qc(a, edit_dir):
    return run_qc(edit_dir, a.version, "final" if a.final else "draft", a.llm, a.claude_model)


def handoff(edit_dir, version=None):
    """Write HANDOFF.md for /publish: final files per aspect, brief, QC, music/licence notes."""
    r = load(edit_dir, version)
    finals = [x for x in rjson(edit_dir / "renders" / "renders.json", []) if x["version"] == r["version"] and x["quality"] == "final"]
    brief = rjson(edit_dir / "brief.json", {})
    m = r["audio"].get("music") or {}
    L = [f"# Edit handoff → /publish (v{r['version']}, approved {r.get('approved_at')})", "",
         "| aspect | file | duration |", "|---|---|---|"] + [f"| {x['aspect']} | `{x['path']}` | {x['duration']} s |" for x in finals]
    qc_md = edit_dir / "qc" / ("QC_v%d_final.md" % r["version"])
    L += ["", f"Brief: `{edit_dir / 'EDIT_BRIEF.md'}` · QC: `{qc_md}`",
          f"Hook used: {next((t['text'] for t in r['texts'] if t['type'] == 'hook'), '—')} · CTA: {(brief.get('cta') or {}).get('spoken') or '—'}",
          f"Music: {m.get('path') or 'none'} (licence: {m.get('licence') or '—'}). In-app sounds (personal accounts) are added at posting: see SOUND.md.",
          "", "Next: `/publish` (distributor agent) → per-platform package; never auto-posts."]
    p = edit_dir / "HANDOFF.md"
    p.write_text("\n".join(L) + "\n", encoding="utf-8")
    log(f"handoff -> {p}")
    return p
