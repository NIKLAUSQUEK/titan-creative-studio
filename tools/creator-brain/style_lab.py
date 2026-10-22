#!/usr/bin/env python3
"""Style Lab: build the creator Style DNA library for FREE on your own PC (no vidIQ credits).

  python style_lab.py creators --out creators.json [--batch 4]       # list from Supabase (or edit the JSON by hand)
  python style_lab.py fetch    --creators creators.json --work W --per 3
  python style_lab.py analyse  --work W                               # cuts/pacing/hook frames + transcript + Claude breakdown
  python style_lab.py cards    --work W                               # Claude synthesises one StyleCard per creator
  python style_lab.py push     --work W                               # upsert into Supabase style_cards (env vars) or export JSON

Downloads: yt-dlp (YouTube/Shorts, TikTok, Instagram). Instagram/TikTok may need --cookies-from-browser chrome.
Analysis: ffmpeg scene detection + faster-whisper + `claude -p` (your Claude Code login). Every step is resumable.
Videos are kept only for analysis; delete the work folder's videos/ any time. Never re-upload other creators' videos.
"""
import argparse, json, os, re, shutil, subprocess, sys, time, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import creator_brain as cb  # reuse ffprobe, transcription, claude helpers

EXTRACT = ("Break this video down for a style library. Use these headings: HOOK (first 2 seconds: what is seen, heard, written); "
           "STRUCTURE (beats with timestamps); PACING (average shot length, number of cuts, jump cuts, pauses removed or kept); "
           "CAMERA (who holds it, angle, shot sizes, movement, POV); LIGHTING & GRADE (key light quality, colour temperature, contrast, saturation); "
           "CAPTIONS & TEXT (font style, position, animation, word-by-word or static, emoji use); SOUND (music genre/energy, SFX types and where they hit, voice processing); "
           "VOICE & DELIVERY (speed, rhythm, accent, energy, persona); EDIT EFFECTS (zooms, transitions, shakes, freezes, overlays, memes); PEOPLE & SETTING; "
           "TARGET AUDIENCE (likely age band and who it is for, and why); SIGNATURE MOVE. Describe only what is on screen.")
log = cb.log
SUPA_REF = "qdikcsxinpyfnljszvay"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:50]


def supa(path, method="GET", body=None):
    url, key = os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not (url and key):
        return None
    req = urllib.request.Request(f"{url}/rest/v1/{path}", method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json",
                                          "Prefer": "resolution=merge-duplicates,return=representation"})
    with urllib.request.urlopen(req, timeout=60) as r:
        t = r.read()
    return json.loads(t) if t else None


def cmd_creators(a):
    rows = None
    try:
        q = "style_creators?select=id,name,category,country,batch,long_form,status&order=batch,id"
        if a.batch:
            q += f"&batch=eq.{a.batch}"
        rows = supa(q)
    except Exception as e:
        log(f"Supabase read failed ({e}); writing a template instead")
    if rows is None:
        rows = [{"id": None, "name": "Jun Yuh", "category": "Yapping", "country": "USA", "long_form": False}]
        log("No SUPABASE_URL/SUPABASE_SERVICE_ROLE_KEY env vars: wrote a one-row template. Add creators by hand.")
    for r in rows:
        r.setdefault("urls", [])        # paste exact video URLs here for best results
        r.setdefault("search", f"{r['name']} #shorts" if not r.get("long_form") else r["name"])
    Path(a.out).write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    log(f"{len(rows)} creators → {a.out}  (edit 'urls' or 'search' per creator, then run fetch)")


def ytdlp(args):
    exe = shutil.which("yt-dlp") or [sys.executable, "-m", "yt_dlp"]
    return cb.run(([exe] if isinstance(exe, str) else exe) + args)


def cmd_fetch(a):
    work = Path(a.work)
    creators = json.loads(Path(a.creators).read_text(encoding="utf-8"))
    base = ["--no-warnings", "--no-write-playlist-metafiles", "-f", "bv*[height<=720][ext=mp4]+ba[ext=m4a]/b[height<=720]/b", "--merge-output-format", "mp4",
            "--write-info-json", "--restrict-filenames"]
    if shutil.which("deno") is None and shutil.which("node"):
        base += ["--js-runtimes", "node", "--remote-components", "ejs:github"]  # YouTube needs a JS runtime
    if a.cookies_from_browser:
        base += ["--cookies-from-browser", a.cookies_from_browser]
    for c in creators:
        d = work / "creators" / slug(c["name"]); (d / "videos").mkdir(parents=True, exist_ok=True)
        (d / "creator.json").write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding="utf-8")
        have = len(list((d / "videos").glob("*.mp4")))
        if have >= a.per:
            continue
        log(f"{c['name']}: fetching {a.per - have} video(s)")
        out = ["-o", str(d / "videos" / "%(extractor)s_%(id)s.%(ext)s")]
        urls = c.get("urls") or []
        if urls:
            r = ytdlp(base + out + urls[: a.per])
        else:
            maxdur = "duration < 1200" if c.get("long_form") else "duration < 181"
            r = ytdlp(base + out + ["--match-filter", maxdur, "--max-downloads", str(a.per - have), f"ytsearch{a.search_depth}:{c.get('search') or c['name']}"])
        if "not a bot" in (r.stderr or ""):
            log("  YouTube wants a signed-in browser: re-run with --cookies-from-browser chrome (or edge/firefox)")
        if r.returncode not in (0, 101):  # 101 = max-downloads reached
            log(f"  yt-dlp: {(r.stderr or r.stdout)[-300:]}")
        time.sleep(a.sleep)


def cuts(path):
    r = cb.run(["ffmpeg", "-hide_banner", "-i", str(path), "-vf", "select='gt(scene,0.3)',showinfo", "-an", "-f", "null", "-"])
    return [float(m) for m in re.findall(r"pts_time:([\d.]+)", r.stderr)]


def hook_sheet(path, out):
    r = cb.run(["ffmpeg", "-y", "-v", "error", "-t", "3", "-i", str(path), "-vf", "fps=2,scale=320:-2,tile=6x1", "-frames:v", "1", str(out)])
    return out.exists()


def cmd_analyse(a):
    for vid in sorted(Path(a.work).glob("creators/*/videos/*.mp4")):
        d = vid.parent.parent / "analysis" / vid.stem; d.mkdir(parents=True, exist_ok=True)
        if (d / "analysis.md").exists():
            continue
        c = json.loads((vid.parent.parent / "creator.json").read_text(encoding="utf-8"))
        log(f"{c['name']}: {vid.name}")
        meta = cb.meta_from_probe(cb.ffprobe(vid)); dur = meta["duration"] or 0
        cut_t = cuts(vid)
        info = {}
        ij = vid.with_suffix(".info.json")
        if ij.exists():
            j = json.loads(ij.read_text(encoding="utf-8"))
            info = {k: j.get(k) for k in ("title", "uploader", "view_count", "like_count", "comment_count", "upload_date", "webpage_url", "description")}
            info["description"] = (info.get("description") or "")[:600]
        metrics = {"duration_s": dur, "width": meta["width"], "height": meta["height"], "cuts": len(cut_t),
                   "avg_shot_s": round(dur / (len(cut_t) + 1), 2) if dur else None, "cuts_first_3s": sum(1 for t in cut_t if t < 3),
                   "cut_times": [round(t, 2) for t in cut_t[:60]]}
        cb.contact_sheet(vid, dur, d / "sheet.jpg"); hook_sheet(vid, d / "hook.jpg")
        tr = cb.transcribe(vid, d, a.model, a.device, None) if meta["has_audio"] else None
        if tr and dur:
            metrics["words_per_min"] = round(tr["words"] / (dur / 60), 1)
        (d / "metrics.json").write_text(json.dumps({"info": info, "metrics": metrics, "transcript": tr}, indent=2, ensure_ascii=False), encoding="utf-8")
        transcript = (d / "transcript.txt").read_text(encoding="utf-8") if (d / "transcript.txt").exists() else "(no speech)"
        prompt = (f"{EXTRACT}\n\nCreator: {c['name']} ({c.get('category')}, {c.get('country')}).\n"
                  f"Use your Read tool to look at these images first: hook frames (first 3 s, 2 per second, left→right) at {d / 'hook.jpg'}, "
                  f"and a 3x3 contact sheet across the whole video at {d / 'sheet.jpg'}.\n"
                  f"Measured facts (trust these over impressions): {json.dumps(metrics)}\nPost metadata: {json.dumps(info, ensure_ascii=False)}\n"
                  f"Transcript:\n{transcript[:12000]}\n\nAnswer in markdown with exactly those headings.")
        try:
            ns = argparse.Namespace(llm="claude-cli", model=a.claude_model, claude_bin=a.claude_bin)
            text = cb.call_llm(prompt, ns, str(d / "sheet.jpg"))
            (d / "analysis.md").write_text(text, encoding="utf-8")
        except Exception as e:
            log(f"  analysis failed: {str(e)[:200]}")
        if a.delete_videos:
            vid.unlink(missing_ok=True)


CARD_PROMPT = """You are building a StyleCard for a creator style library used by a creative studio (Higgsfield video models: Seedance 2.5, Kling 3.0; GPT Image 2.5).
Creator: {name} ({category}, {country}). Below are per-video breakdowns with measured cut/pacing data. Base everything ONLY on them.
Return ONLY a JSON object: {{"card_md": "<markdown with sections: Vibe, Energy (1-5), Hook pattern, Structure, Pacing & edit, Camera & framing, Lighting & grade, Captions & text, Sound & SFX, Voice & delivery, Signature moves, Target audience, Higgsfield translation (concrete prompt phrases, camera moves, model notes), How a brand could borrow it (technique only, never copy content), Sources>", "dna": {{"vibe": "", "energy": 0, "hook": "", "pacing": "", "camera": "", "lighting": "", "captions": "", "sound": "", "voice": "", "signature": "", "audience": "", "avg_shot_s": 0, "higgsfield_prompt_snippet": "", "sources": []}}}}

{breakdowns}"""


def cmd_cards(a):
    for cdir in sorted(Path(a.work).glob("creators/*")):
        out = cdir / "card.json"
        if out.exists() and not a.force:
            continue
        an = sorted(cdir.glob("analysis/*/analysis.md"))
        if not an:
            continue
        c = json.loads((cdir / "creator.json").read_text(encoding="utf-8"))
        parts = []
        for p in an:
            m = json.loads((p.parent / "metrics.json").read_text(encoding="utf-8"))
            parts.append(f"### {m['info'].get('webpage_url') or p.parent.name}\nMetrics: {json.dumps(m['metrics'])}\n{p.read_text(encoding='utf-8')}")
        log(f"card: {c['name']} ({len(an)} videos)")
        ns = argparse.Namespace(llm="claude-cli", model=a.claude_model, claude_bin=a.claude_bin)
        try:
            card = cb.parse_json(cb.call_llm(CARD_PROMPT.format(name=c["name"], category=c.get("category"), country=c.get("country"), breakdowns="\n\n".join(parts)), ns, None))
            card["creator"] = {k: c.get(k) for k in ("id", "name", "category", "country")}
            out.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception as e:
            log(f"  card failed: {str(e)[:200]}")


def cmd_push(a):
    cards = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(Path(a.work).glob("creators/*/card.json"))]
    export = Path(a.work) / "style_cards_export.json"
    export.write_text(json.dumps(cards, indent=2, ensure_ascii=False), encoding="utf-8")
    if not (os.environ.get("SUPABASE_URL") and os.environ.get("SUPABASE_SERVICE_ROLE_KEY")):
        log(f"No Supabase env vars. Exported {len(cards)} cards to {export}. Import: open Claude Code in the studio repo and say "
            f"'import {export} into style_cards'.")
        return
    n = 0
    for c in cards:
        cr = c["creator"]
        cid = cr.get("id")
        if not cid:
            rows = supa("style_creators?on_conflict=name", "POST", [{"name": cr["name"], "category": cr.get("category") or "Other", "country": cr.get("country"), "batch": 99}])
            cid = rows[0]["id"]
        supa("style_cards?on_conflict=creator_id", "POST", [{"creator_id": cid, "card_md": c["card_md"], "dna": c["dna"]}])
        supa(f"style_creators?id=eq.{cid}", "PATCH", {"status": "done", "notes": "built locally by style_lab.py"})
        n += 1
    log(f"pushed {n} StyleCards to Supabase")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("creators"); p.add_argument("--out", default="creators.json"); p.add_argument("--batch", type=int)
    p = sp.add_parser("fetch"); p.add_argument("--creators", required=True); p.add_argument("--work", required=True); p.add_argument("--per", type=int, default=3)
    p.add_argument("--search-depth", type=int, default=15); p.add_argument("--cookies-from-browser"); p.add_argument("--sleep", type=float, default=3)
    for name in ("analyse", "cards"):
        p = sp.add_parser(name); p.add_argument("--work", required=True); p.add_argument("--claude-model"); p.add_argument("--claude-bin", default=shutil.which("claude") or "claude")
        if name == "analyse":
            p.add_argument("--model", default="small"); p.add_argument("--device", default="auto"); p.add_argument("--delete-videos", action="store_true")
        else:
            p.add_argument("--force", action="store_true")
    p = sp.add_parser("push"); p.add_argument("--work", required=True)
    a = ap.parse_args()
    {"creators": cmd_creators, "fetch": cmd_fetch, "analyse": cmd_analyse, "cards": cmd_cards, "push": cmd_push}[a.cmd](a)


if __name__ == "__main__":
    main()
