#!/usr/bin/env python3
"""Creator Brain extractor: videos/audio/photos -> transcripts + metadata -> Claude analysis -> Obsidian vault.

  python creator_brain.py extract --src "D:\\Videos" "G:\\My Drive\\mens_health_social" --work WORK
  python creator_brain.py sense   --work WORK [--llm claude-cli|api] [--model sonnet]
  python creator_brain.py vault   --work WORK --vault "C:\\Users\\me\\Obsidian\\Klaus Brain"

Every step is resumable: finished items are skipped, so re-running after adding files only processes the new ones.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile, time, urllib.request
from pathlib import Path

VIDEO = {".mp4", ".mov", ".m4v", ".webm", ".mkv", ".avi", ".3gp", ".mts", ".wmv"}
AUDIO = {".m4a", ".mp3", ".wav", ".aac", ".ogg", ".opus", ".flac"}
IMAGE = {".jpg", ".jpeg", ".png", ".heic", ".webp"}
ERAS = ["origin", "childhood", "teens", "young_adult", "builder", "future", "unknown"]
TYPES = ["klaus_talking", "klaus_life_footage", "client", "family_friends", "reference_creator", "broll", "event", "screen_recording", "photo", "other"]


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


def item_id(p: Path):
    st = p.stat()
    return hashlib.sha1(f"{p.resolve()}|{st.st_size}".encode("utf-8", "replace")).hexdigest()[:12]


def ffprobe(p: Path):
    r = run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", str(p)])
    try:
        return json.loads(r.stdout or "{}")
    except json.JSONDecodeError:
        return {}


def meta_from_probe(pr):
    fmt = pr.get("format", {}) or {}
    tags = {k.lower(): v for k, v in (fmt.get("tags") or {}).items()}
    for s in pr.get("streams", []) or []:
        for k, v in (s.get("tags") or {}).items():
            tags.setdefault(k.lower(), v)
    vs = next((s for s in pr.get("streams", []) if s.get("codec_type") == "video"), {})
    gps = tags.get("location") or tags.get("com.apple.quicktime.location.iso6709")
    return {
        "duration": round(float(fmt.get("duration") or 0), 1),
        "created": tags.get("com.apple.quicktime.creationdate") or tags.get("creation_time"),
        "gps": gps,
        "device": " ".join(x for x in [tags.get("com.apple.quicktime.make"), tags.get("com.apple.quicktime.model")] if x) or None,
        "width": vs.get("width"), "height": vs.get("height"),
        "has_audio": any(s.get("codec_type") == "audio" for s in pr.get("streams", [])),
    }


def image_meta(p: Path):
    m = {"duration": 0, "created": None, "gps": None, "device": None, "width": None, "height": None, "has_audio": False}
    try:
        from PIL import Image, ExifTags
        try:
            import pillow_heif  # optional HEIC support
            pillow_heif.register_heif_opener()
        except ImportError:
            pass
        with Image.open(p) as im:
            m["width"], m["height"] = im.size
            ex = im.getexif() or {}
            names = {ExifTags.TAGS.get(k, k): v for k, v in ex.items()}
            sub = ex.get_ifd(0x8769) if hasattr(ex, "get_ifd") else {}
            dto = sub.get(36867) or names.get("DateTimeOriginal") or names.get("DateTime")
            m["created"] = str(dto) if dto else None
            m["device"] = " ".join(str(names[k]) for k in ("Make", "Model") if names.get(k)) or None
    except Exception as e:  # unreadable/HEIC without plugin
        m["error"] = str(e)[:200]
    return m


def contact_sheet(src: Path, dur: float, out: Path):
    n = 9
    step = max(dur / (n + 1), 0.5) if dur else 1
    fps = f"fps=1/{step:.3f}" if dur else "fps=1"
    r = run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vf", f"{fps},scale=320:-2,tile=3x3", "-frames:v", "1", "-q:v", "4", str(out)])
    return out.exists() and out.stat().st_size > 0


def image_thumb(src: Path, out: Path):
    try:
        from PIL import Image
        try:
            import pillow_heif
            pillow_heif.register_heif_opener()
        except ImportError:
            pass
        with Image.open(src) as im:
            im = im.convert("RGB")
            im.thumbnail((1024, 1024))
            im.save(out, "JPEG", quality=82)
        return True
    except Exception:
        r = run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vf", "scale=1024:-2", "-frames:v", "1", str(out)])
        return out.exists()


_WHISPER = None


def whisper(model_name, device):
    global _WHISPER
    if _WHISPER is None:
        from faster_whisper import WhisperModel
        if device == "auto":
            device = "cuda" if shutil.which("nvidia-smi") else "cpu"
        compute = "float16" if device == "cuda" else "int8"
        log(f"loading whisper {model_name} on {device} ({compute})")
        _WHISPER = WhisperModel(model_name, device=device, compute_type=compute)
    return _WHISPER


def fmt_ts(s):
    h, rem = divmod(int(s), 3600)
    m, sec = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{sec:02d},{int((s - int(s)) * 1000):03d}"


def transcribe(src: Path, d: Path, model_name, device, language):
    wav = d / "audio.wav"
    r = run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-vn", "-ac", "1", "-ar", "16000", str(wav)])
    if not wav.exists():
        return None
    try:
        import wave, numpy as np  # feed numpy audio: avoids the PyAV version clash (ledger 2026-10-10)
        with wave.open(str(wav), "rb") as w:
            audio = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768.0
        segs, info = whisper(model_name, device).transcribe(audio, vad_filter=True, language=language or None, beam_size=5)
        segs = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in segs]
    finally:
        wav.unlink(missing_ok=True)
    (d / "transcript.srt").write_text("".join(f"{i}\n{fmt_ts(s['start'])} --> {fmt_ts(s['end'])}\n{s['text']}\n\n" for i, s in enumerate(segs, 1)), encoding="utf-8")
    (d / "transcript.txt").write_text("\n".join(f"[{int(s['start'])//60:02d}:{int(s['start'])%60:02d}] {s['text']}" for s in segs), encoding="utf-8")
    return {"language": info.language, "language_probability": round(info.language_probability, 2), "segments": len(segs), "words": sum(len(s["text"].split()) for s in segs)}


def cmd_extract(a):
    work = Path(a.work); (work / "items").mkdir(parents=True, exist_ok=True)
    files = []
    for root in a.src:
        rp = Path(root)
        if rp.is_file():
            files.append((rp, rp.parent)); continue
        for p in sorted(rp.rglob("*")):
            if p.is_file() and p.suffix.lower() in VIDEO | AUDIO | IMAGE and not p.name.startswith("."):
                files.append((p, rp))
    if a.limit:
        files = files[: a.limit]
    log(f"{len(files)} media files found")
    done = 0
    for i, (p, root) in enumerate(files, 1):
        try:
            iid = item_id(p)
        except OSError as e:
            log(f"skip unreadable {p}: {e}"); continue
        d = work / "items" / iid; d.mkdir(exist_ok=True)
        ij = d / "item.json"
        if ij.exists() and json.loads(ij.read_text(encoding="utf-8")).get("status") == "extracted":
            continue
        ext = p.suffix.lower()
        kind = "video" if ext in VIDEO else "audio" if ext in AUDIO else "image"
        log(f"[{i}/{len(files)}] {kind} {p.name}")
        item = {"id": iid, "path": str(p), "folder": str(p.parent), "source_root": str(root), "name": p.name, "kind": kind,
                "size_mb": round(p.stat().st_size / 1e6, 1), "mtime": time.strftime("%Y-%m-%d", time.localtime(p.stat().st_mtime))}
        try:
            item.update(image_meta(p) if kind == "image" else meta_from_probe(ffprobe(p)))
            if kind == "video":
                item["sheet"] = "sheet.jpg" if contact_sheet(p, item.get("duration") or 0, d / "sheet.jpg") else None
            elif kind == "image":
                item["sheet"] = "sheet.jpg" if image_thumb(p, d / "sheet.jpg") else None
            if kind in ("video", "audio") and item.get("has_audio", kind == "audio") and not a.no_transcribe:
                item["transcript"] = transcribe(p, d, a.model, a.device, a.language)
            item["status"] = "extracted"
        except Exception as e:
            item["status"] = "error"; item["error"] = str(e)[:500]
            log(f"  error: {e}")
        ij.write_text(json.dumps(item, indent=2, ensure_ascii=False), encoding="utf-8")
        done += 1
    log(f"extract finished: {done} new/updated items in {work / 'items'}")


SCHEMA = {
    "title": "short descriptive title (max 8 words)",
    "summary": "2-3 sentences: what this is and why it matters",
    "content_type": "|".join(TYPES),
    "owner": "me|client|reference|family|unknown (me = Klaus himself)",
    "era": "|".join(ERAS) + " (Klaus's life era this shows, if it is about his life)",
    "approx_year": "e.g. 2019 or null",
    "people": ["names or roles seen/mentioned (use roles like 'patient' for clients)"],
    "places": ["places"],
    "themes": ["identity|insecurity|barriers|growth|wins|losses|lessons|love|body|money|beliefs|mens_health|sexual_health|fitness|business|family|culture|faith|humour|education|other"],
    "emotions": ["love|grief|hope|tension|anger|joy|wonder|shame|pride|calm|fear"],
    "key_quotes": [{"t": "mm:ss", "quote": "verbatim line worth keeping"}],
    "story_seeds": [{"title": "", "what_happened": "", "lesson": "", "wisdom_note": "", "trope": "", "stance": "agree|challenge|subvert|flip|both"}],
    "hooks": ["5 hook lines a short video could open with, in Klaus's voice"],
    "values_beliefs_principles": [{"type": "value|belief|principle|contrarian_take", "text": "", "evidence_quote": ""}],
    "wisdom_notes": ["screenshot-worthy one-liners grounded in this material"],
    "content_ideas": [{"goal": "wise|expert|trust|sell|founder|entertain", "format": "", "idea": ""}],
    "reference_lessons": "if this is another creator's video: the hook, structure, edit and delivery techniques worth borrowing (never copy content); else null",
    "sensitivity": "none|personal|medical|minor_present|third_party — flag anything that must not be published without consent",
    "tags": ["lowercase-kebab tags"],
}

PROMPT = """You are the archivist for Klaus (Niklaus Quek), a men's health physiotherapist and founder in Singapore building a "Creator Brain": a structured memory of his life, values, stories and the reference content he studies.
Analyse ONE media item using its metadata, transcript and (if available) the contact-sheet image at {sheet}. Read that image with your Read tool if the path is not "none".
Rules: use only what is in the material; do not invent events, names or quotes; quotes must be verbatim from the transcript; if unsure use "unknown"/null/[]. Write in English (translate Chinese/Malay/Singlish meaning if needed, keep a short original snippet in quotes).
Return ONLY a JSON object (no prose, no code fence) with exactly these keys:
{schema}

METADATA:
{meta}

TRANSCRIPT ({words} words{trunc}):
{transcript}
"""


COURSE_SCHEMA = {
    "title": "lesson title (max 10 words)",
    "module": "module/section name if inferable from folder or file name, else null",
    "summary": "3-4 sentences: what this lesson teaches",
    "frameworks": [{"name": "", "steps": ["ordered steps"], "when_to_use": ""}],
    "key_points": ["the lesson's main teaching points, concrete"],
    "templates_prompts": ["any scripts, prompt templates, hook formulas, checklists or tool settings shown or spoken, verbatim where possible"],
    "tools": ["software/AI tools/models named, with what they are used for"],
    "examples": ["examples or case studies shown"],
    "key_quotes": [{"t": "mm:ss", "quote": "verbatim"}],
    "action_items": ["what a student should do after this lesson"],
    "apply_to_titan": "how this lesson improves Klaus's creative studio (which skill/command/reference file it should update and how)",
    "tags": ["lowercase-kebab tags"],
}

COURSE_PROMPT = """You are turning a paid course Klaus bought into private study notes and reusable workflows for his creative studio. Analyse ONE lesson video using its metadata, transcript and (if available) the contact-sheet image at {sheet} (read it with your Read tool if not "none"; slides and on-screen text matter).
Rules: only what the lesson actually teaches; quotes verbatim; do not invent steps. Notes are for private learning, not republishing.
Return ONLY a JSON object (no prose, no code fence) with exactly these keys:
{schema}

METADATA:
{meta}

TRANSCRIPT ({words} words{trunc}):
{transcript}
"""


def call_llm(prompt, a, sheet_path):
    if a.llm == "api":
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise SystemExit("ANTHROPIC_API_KEY not set (or use --llm claude-cli)")
        content = [{"type": "text", "text": prompt}]
        if sheet_path:
            import base64
            content.insert(0, {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": base64.b64encode(Path(sheet_path).read_bytes()).decode()}})
        body = json.dumps({"model": a.model or "claude-sonnet-5-5", "max_tokens": 4000, "messages": [{"role": "user", "content": content}]}).encode()
        req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
        with urllib.request.urlopen(req, timeout=300) as r:
            j = json.loads(r.read())
        return "".join(c.get("text", "") for c in j.get("content", []))
    cmd = [a.claude_bin, "-p", "--output-format", "json"]
    if sheet_path:
        cmd += ["--allowedTools", "Read", "--add-dir", str(Path(sheet_path).parent)]
    if a.model:
        cmd += ["--model", a.model]
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600)
    if r.returncode != 0:
        raise RuntimeError(f"claude CLI failed: {(r.stderr or r.stdout)[:400]}")
    try:
        return json.loads(r.stdout).get("result", "")
    except json.JSONDecodeError:
        return r.stdout


def parse_json(text):
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    m = re.search(r"\{.*\}", text, re.S)
    return json.loads(m.group(0) if m else text)


def cmd_sense(a):
    items = sorted((Path(a.work) / "items").glob("*/item.json"))
    todo = [p for p in items if not (p.parent / "analysis.json").exists() and json.loads(p.read_text(encoding="utf-8")).get("status") == "extracted"]
    if a.limit:
        todo = todo[: a.limit]
    log(f"{len(todo)} items to analyse ({len(items)} total)")
    for i, ij in enumerate(todo, 1):
        d = ij.parent; item = json.loads(ij.read_text(encoding="utf-8"))
        tpath = d / "transcript.txt"
        transcript = tpath.read_text(encoding="utf-8") if tpath.exists() else "(no speech / no transcript)"
        words = len(transcript.split()); trunc = ""
        if not a.max_words:
            a.max_words = 40000 if a.mode == "course" else 9000  # course lessons: keep the whole lesson
        if words > a.max_words:
            parts = transcript.split()
            half = a.max_words // 2
            transcript = " ".join(parts[:half]) + "\n[... middle omitted ...]\n" + " ".join(parts[-half:])
            trunc = f", truncated to {a.max_words}"
        sheet = str(d / "sheet.jpg") if (d / "sheet.jpg").exists() and not a.no_vision else None
        meta = {k: item.get(k) for k in ("name", "folder", "kind", "duration", "created", "mtime", "gps", "device", "width", "height", "transcript")}
        tmpl, sch = (COURSE_PROMPT, COURSE_SCHEMA) if a.mode == "course" else (PROMPT, SCHEMA)
        prompt = tmpl.format(sheet=sheet or "none", schema=json.dumps(sch, indent=1), meta=json.dumps(meta, ensure_ascii=False), words=words, trunc=trunc, transcript=transcript)
        log(f"[{i}/{len(todo)}] {item['name']}")
        for attempt in range(2):
            try:
                res = parse_json(call_llm(prompt, a, sheet))
                (d / "analysis.json").write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
                break
            except Exception as e:
                log(f"  attempt {attempt + 1} failed: {str(e)[:200]}")
                time.sleep(3)
    log("sense finished")


def slug(s, n=60):
    s = re.sub(r"[\\/:*?\"<>|#^\[\]]", "", str(s)).strip()
    return re.sub(r"\s+", " ", s)[:n] or "untitled"


def link(name):
    return f"[[{slug(name)}]]"


def yaml_list(xs):
    return "[" + ", ".join(json.dumps(str(x), ensure_ascii=False) for x in xs if x) + "]"


def cmd_vault(a):
    root = Path(a.vault) / a.folder
    for sub in ("Media", "Eras", "Themes", "People", "_attachments"):
        (root / sub).mkdir(parents=True, exist_ok=True)
    items = []
    for ij in sorted((Path(a.work) / "items").glob("*/item.json")):
        d = ij.parent; aj = d / "analysis.json"
        if not aj.exists():
            continue
        items.append((json.loads(ij.read_text(encoding="utf-8")), json.loads(aj.read_text(encoding="utf-8")), d))
    log(f"writing {len(items)} notes to {root}")
    by = {"era": {}, "theme": {}, "person": {}}
    quotes, hooks, seeds, vbp, wisdom, ideas, refs = [], [], [], [], [], [], []
    if getattr(a, "mode", "life") == "course":
        return course_vault(a, root, items)
    for item, an, d in items:
        date = (str(item.get("created") or "")[:10] or item.get("mtime") or "")
        title = an.get("title") or item["name"]
        note = slug(f"{date} {title}" if date else title, 90)
        att = None
        if (d / "sheet.jpg").exists():
            att = f"{item['id']}.jpg"; shutil.copy2(d / "sheet.jpg", root / "_attachments" / att)
        era = an.get("era") or "unknown"
        by["era"].setdefault(era, []).append(note)
        for t in an.get("themes") or []:
            by["theme"].setdefault(t, []).append(note)
        for p in an.get("people") or []:
            by["person"].setdefault(slug(p, 40), []).append(note)
        fm = ["---", f"id: {item['id']}", f"title: {json.dumps(title, ensure_ascii=False)}", f"date: {date or 'unknown'}", f"kind: {item['kind']}",
              f"content_type: {an.get('content_type')}", f"owner: {an.get('owner')}", f"era: {era}", f"approx_year: {an.get('approx_year')}",
              f"duration_s: {item.get('duration')}", f"source: {json.dumps(item['path'], ensure_ascii=False)}", f"people: {yaml_list(an.get('people') or [])}",
              f"places: {yaml_list(an.get('places') or [])}", f"themes: {yaml_list(an.get('themes') or [])}", f"emotions: {yaml_list(an.get('emotions') or [])}",
              f"sensitivity: {an.get('sensitivity')}", f"tags: {yaml_list(['creator-brain'] + (an.get('tags') or []))}", "---"]
        body = [f"# {title}", "", an.get("summary") or "", "",
                f"**Era:** {link('Era - ' + era)} · **Themes:** {', '.join(link('Theme - ' + t) for t in an.get('themes') or [])} · **People:** {', '.join(link('Person - ' + slug(p, 40)) for p in an.get('people') or [])}", "",
                f"Source: `{item['path']}`", ""]
        if att:
            body += [f"![[{att}]]", ""]
        if an.get("key_quotes"):
            body += ["## Key quotes"] + [f"- `{q.get('t', '')}` \"{q.get('quote', '')}\"" for q in an["key_quotes"]] + [""]
            quotes += [(q, note) for q in an["key_quotes"]]
        if an.get("story_seeds"):
            body += ["## Story seeds"]
            for s in an["story_seeds"]:
                body += [f"### {s.get('title', '')}", f"- What happened: {s.get('what_happened', '')}", f"- Lesson: {s.get('lesson', '')}",
                         f"- Wisdom note: {s.get('wisdom_note', '')}", f"- Trope: {s.get('trope', '')} ({s.get('stance', '')})"]
                seeds.append((s, note))
            body.append("")
        if an.get("hooks"):
            body += ["## Hooks"] + [f"- {h}" for h in an["hooks"]] + [""]
            hooks += [(h, note) for h in an["hooks"]]
        if an.get("values_beliefs_principles"):
            body += ["## Values, beliefs, principles (draft until Klaus confirms)"] + [f"- **{v.get('type')}:** {v.get('text')} — \"{v.get('evidence_quote', '')}\"" for v in an["values_beliefs_principles"]] + [""]
            vbp += [(v, note) for v in an["values_beliefs_principles"]]
        if an.get("wisdom_notes"):
            body += ["## Wisdom notes"] + [f"- {w}" for w in an["wisdom_notes"]] + [""]
            wisdom += [(w, note) for w in an["wisdom_notes"]]
        if an.get("content_ideas"):
            body += ["## Content ideas"] + [f"- **{c.get('goal')}** · {c.get('format')}: {c.get('idea')}" for c in an["content_ideas"]] + [""]
            ideas += [(c, note) for c in an["content_ideas"]]
        if an.get("reference_lessons"):
            body += ["## Techniques to borrow", str(an["reference_lessons"]), ""]
            refs.append((an["reference_lessons"], note))
        tp = d / "transcript.txt"
        if tp.exists():
            body += ["## Transcript", "> [!note]- Full transcript", *[f"> {l}" for l in tp.read_text(encoding="utf-8").splitlines()], ""]
        (root / "Media" / f"{note}.md").write_text("\n".join(fm + body), encoding="utf-8")

    def index(folder, prefix, groups, intro):
        for k, notes in groups.items():
            lines = [f"# {prefix}{k}", intro, "", *[f"- [[{n}]]" for n in sorted(set(notes))]]
            (root / folder / f"{slug(prefix + k)}.md").write_text("\n".join(lines), encoding="utf-8")

    index("Eras", "Era - ", by["era"], "Media from this era of Klaus's life.")
    index("Themes", "Theme - ", by["theme"], "Media touching this theme.")
    index("People", "Person - ", by["person"], "Media this person appears in or is mentioned in.")
    agg = {
        "Quotes": [f"- \"{q.get('quote', '')}\" — [[{n}]] `{q.get('t', '')}`" for q, n in quotes],
        "Hooks": [f"- {h} — [[{n}]]" for h, n in hooks],
        "Story Seeds": [f"- **{s.get('title', '')}**: {s.get('lesson', '')} — wisdom: _{s.get('wisdom_note', '')}_ — [[{n}]]" for s, n in seeds],
        "Values Beliefs Principles": [f"- **{v.get('type')}** {v.get('text')} — [[{n}]]" for v, n in vbp],
        "Wisdom Notes": [f"- {w} — [[{n}]]" for w, n in wisdom],
        "Content Ideas": [f"- **{c.get('goal')}** · {c.get('format')}: {c.get('idea')} — [[{n}]]" for c, n in ideas],
        "Reference Techniques": [f"- [[{n}]]: {str(r)[:300]}" for r, n in refs],
    }
    for name, lines in agg.items():
        (root / f"{name}.md").write_text("\n".join([f"# {name}", f"_{len(lines)} entries, auto-built from {len(items)} media items. Re-run the vault step to refresh; don't edit by hand._", ""] + lines), encoding="utf-8")
    home = ["# Creator Brain", f"_Built {time.strftime('%Y-%m-%d %H:%M')} from {len(items)} analysed media items._", "",
            "## Start here", *[f"- [[{n}]] ({len(agg[n])})" for n in agg], "",
            "## Eras", *[f"- [[{slug('Era - ' + e)}]] ({len(by['era'].get(e, []))})" for e in ERAS if e in by["era"]], "",
            "## Top themes", *[f"- [[{slug('Theme - ' + t)}]] ({len(v)})" for t, v in sorted(by["theme"].items(), key=lambda kv: -len(kv[1]))[:20]], "",
            "## Dataview (install the Dataview plugin)", "```dataview", f"TABLE date, era, content_type, owner, themes FROM \"{a.folder}/Media\" SORT date ASC", "```", "",
            "Sensitive items (`sensitivity` not none) need consent before any use.",]
    (root / "00 Home.md").write_text("\n".join(home), encoding="utf-8")
    log(f"vault ready: open {Path(a.vault)} in Obsidian → {a.folder}/00 Home")


def course_vault(a, root, items):
    (root / "Lessons").mkdir(exist_ok=True)
    mods, tmpls, actions, tools, applies = {}, [], [], [], []
    for item, an, d in sorted(items, key=lambda x: x[0]["path"]):
        title = an.get("title") or item["name"]; mod = an.get("module") or Path(item["folder"]).name
        note = slug(f"{mod} - {title}", 90); mods.setdefault(mod, []).append(note)
        att = None
        if (d / "sheet.jpg").exists():
            att = f"{item['id']}.jpg"; shutil.copy2(d / "sheet.jpg", root / "_attachments" / att)
        b = ["---", f"id: {item['id']}", f"title: {json.dumps(title, ensure_ascii=False)}", f"module: {json.dumps(mod, ensure_ascii=False)}",
             f"source: {json.dumps(item['path'], ensure_ascii=False)}", f"tags: {yaml_list(['course'] + (an.get('tags') or []))}", "---",
             f"# {title}", f"Module: [[{slug('Module - ' + mod)}]]", "", an.get("summary") or "", ""]
        if att: b += [f"![[{att}]]", ""]
        for fw in an.get("frameworks") or []:
            b += [f"## Framework: {fw.get('name', '')}", f"_When:_ {fw.get('when_to_use', '')}", *[f"{i}. {st}" for i, st in enumerate(fw.get("steps") or [], 1)], ""]
        for key, head in (("key_points", "Key points"), ("templates_prompts", "Templates & prompts"), ("tools", "Tools"), ("examples", "Examples"), ("action_items", "Action items")):
            if an.get(key): b += [f"## {head}", *[f"- {x}" for x in an[key]], ""]
        if an.get("key_quotes"): b += ["## Quotes", *[f"- `{q.get('t', '')}` \"{q.get('quote', '')}\"" for q in an["key_quotes"]], ""]
        if an.get("apply_to_titan"): b += ["## Apply to TITAN studio", str(an["apply_to_titan"]), ""]
        tp = d / "transcript.txt"
        if tp.exists(): b += ["## Transcript", "> [!note]- Full transcript", *[f"> {l}" for l in tp.read_text(encoding="utf-8").splitlines()]]
        (root / "Lessons" / f"{note}.md").write_text("\n".join(b), encoding="utf-8")
        tmpls += [(x, note) for x in an.get("templates_prompts") or []]; actions += [(x, note) for x in an.get("action_items") or []]
        tools += [(x, note) for x in an.get("tools") or []]
        if an.get("apply_to_titan"): applies.append((an["apply_to_titan"], note))
    (root / "Modules").mkdir(exist_ok=True)
    for m, notes in mods.items():
        (root / "Modules" / f"{slug('Module - ' + m)}.md").write_text("\n".join([f"# {m}", "", *[f"- [[{n}]]" for n in notes]]), encoding="utf-8")
    agg = {"Templates and Prompts": tmpls, "Action Items": actions, "Tools": tools, "Apply to TITAN": applies}
    for name, rows in agg.items():
        (root / f"{name}.md").write_text("\n".join([f"# {name}", ""] + [f"- {x} — [[{n}]]" for x, n in rows]), encoding="utf-8")
    home = ["# Course Brain", f"_{len(items)} lessons, built {time.strftime('%Y-%m-%d %H:%M')}._", "", *[f"- [[{n}]] ({len(agg[n])})" for n in agg], "", "## Modules",
            *[f"- [[{slug('Module - ' + m)}]] ({len(v)})" for m, v in mods.items()]]
    (root / "00 Home.md").write_text("\n".join(home), encoding="utf-8")
    log(f"course vault ready: {root / '00 Home.md'}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    e = sp.add_parser("extract"); e.add_argument("--src", nargs="+", required=True); e.add_argument("--work", required=True)
    e.add_argument("--model", default="small"); e.add_argument("--device", default="auto"); e.add_argument("--language", default=None)
    e.add_argument("--limit", type=int, default=0); e.add_argument("--no-transcribe", action="store_true")
    s = sp.add_parser("sense"); s.add_argument("--work", required=True); s.add_argument("--llm", choices=["claude-cli", "api"], default="claude-cli")
    s.add_argument("--model", default=None); s.add_argument("--claude-bin", default=shutil.which("claude") or "claude"); s.add_argument("--limit", type=int, default=0)
    s.add_argument("--max-words", type=int, default=0); s.add_argument("--no-vision", action="store_true")
    s.add_argument("--mode", choices=["life", "course"], default="life")
    v = sp.add_parser("vault"); v.add_argument("--work", required=True); v.add_argument("--vault", required=True); v.add_argument("--folder", default="Creator Brain"); v.add_argument("--mode", choices=["life", "course"], default="life")
    a = ap.parse_args()
    {"extract": cmd_extract, "sense": cmd_sense, "vault": cmd_vault}[a.cmd](a)


if __name__ == "__main__":
    main()
