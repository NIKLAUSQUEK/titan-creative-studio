"""B-ROLL, token-cheap: local open_clip index over footage folders (incl. G:\\My Drive\\...), text query -> top-k, zero Claude tokens.
Claude only picks among the top 3 per beat, from compact text + ONE contact sheet for all beats.

Index: <index-dir>/broll.sqlite (clips + per-frame float16 embeddings). Default index dir: %LOCALAPPDATA%/TitanEditor (or ~/.titan-editor).
Consent: files/folders whose path contains a sensitive marker are flagged and excluded from search unless --allow-sensitive.
Also honoured: a `broll_flags.json` in any indexed root ({"glob": "flag"}) and Creator Brain analyses (sensitivity field) via --creator-brain-work.
"""
import fnmatch, hashlib, json, os, re, sqlite3, tempfile, time
from pathlib import Path

from .common import IMAGE, VIDEO, claude, ffmpeg, log, parse_json, probe, rjson, wjson

MODEL, PRETRAINED = "ViT-B-32", "laion2b_s34b_b79k"
SENSITIVE = re.compile(r"(^|[\\/ _\-.])(private|personal|no[-_ ]?use|do[-_ ]?not[-_ ]?use|patients?|clients?|minors?|kids|children|family|medical|nsfw|consent[-_ ]?pending)([\\/ _\-.]|$)", re.I)
_M = {}


def default_index_dir():
    base = os.environ.get("LOCALAPPDATA")
    return Path(base) / "TitanEditor" if base else Path.home() / ".titan-editor"


def db_open(index_dir):
    index_dir = Path(index_dir); index_dir.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(index_dir / "broll.sqlite")
    con.executescript("""
      create table if not exists clips(id text primary key, path text, root text, folder text, name text, kind text, duration real,
        width int, height int, mtime real, size int, tags text, flag text, indexed_at text, frames int, model text);
      create table if not exists frames(clip_id text, k int, t real, emb blob, primary key(clip_id, k));
    """)
    return con


def model(device="auto"):
    if "m" not in _M:
        import open_clip, torch
        dev = "cuda" if device == "auto" and torch.cuda.is_available() else ("cpu" if device == "auto" else device)
        m, _, pre = open_clip.create_model_and_transforms(MODEL, pretrained=PRETRAINED, device=dev)
        m.eval()
        _M.update(m=m, pre=pre, tok=open_clip.get_tokenizer(MODEL), dev=dev, torch=torch)
        log(f"open_clip {MODEL}/{PRETRAINED} on {dev}")
    return _M


def embed_images(paths):
    import numpy as np
    from PIL import Image
    M = model(); torch = M["torch"]
    with torch.no_grad():
        x = torch.stack([M["pre"](Image.open(p).convert("RGB")) for p in paths]).to(M["dev"])
        e = M["m"].encode_image(x)
        e = e / e.norm(dim=-1, keepdim=True)
    return e.cpu().numpy().astype(np.float16)


def embed_text(q):
    M = model(); torch = M["torch"]
    with torch.no_grad():
        e = M["m"].encode_text(M["tok"]([q]).to(M["dev"]))
        e = e / e.norm(dim=-1, keepdim=True)
    return e.cpu().numpy()[0]


def tags_for(p, root):
    rel = Path(p).resolve().relative_to(Path(root).resolve()) if str(Path(p).resolve()).startswith(str(Path(root).resolve())) else Path(p)
    toks = re.split(r"[\\/_\-. ]+", str(rel.with_suffix("")).lower())
    return sorted({t for t in toks if len(t) > 2 and not t.isdigit() and not re.match(r"^(img|vid|dsc|mov|pxl)\d*$", t)})


def flags_for(p, root, rules, cb_flags):
    if str(p) in cb_flags and cb_flags[str(p)] not in (None, "none"):
        return cb_flags[str(p)]
    rel = os.path.relpath(p, root)
    for g, f in rules.items():
        if fnmatch.fnmatch(rel.replace("\\", "/"), g) or fnmatch.fnmatch(Path(p).name, g):
            return f
    m = SENSITIVE.search(str(p))
    return m.group(2).lower() if m else None


def creator_brain_flags(work):
    out = {}
    if work and Path(work).exists():
        for ij in Path(work).glob("items/*/item.json"):
            an = ij.parent / "analysis.json"
            if an.exists():
                try:
                    out[json.loads(ij.read_text(encoding="utf-8"))["path"]] = json.loads(an.read_text(encoding="utf-8")).get("sensitivity")
                except Exception:
                    pass
    return out


def sample_frames(src, dur, n, tmp, kind):
    outs = []
    if kind == "image":
        o = tmp / "f0.jpg"
        ffmpeg(["-i", src, "-vf", "scale=320:-2", "-frames:v", 1, o], check=False)
        return [(0.0, o)] if o.exists() else []
    for k in range(n):
        t = dur * (k + 0.5) / n if dur else 0
        o = tmp / f"f{k}.jpg"
        ffmpeg(["-ss", f"{t:.2f}", "-i", src, "-vf", "scale=320:-2", "-frames:v", 1, "-q:v", 4, o], check=False)
        if o.exists():
            outs.append((round(t, 2), o))
    return outs


def cmd_index(a):
    con = db_open(a.index_dir)
    cbf = creator_brain_flags(a.creator_brain_work)
    seen, added, skipped = 0, 0, 0
    for root in a.roots:
        root = Path(root)
        if not root.exists():
            log(f"root not found: {root}"); continue
        rules = rjson(root / "broll_flags.json", {}) or {}
        files = [f for f in root.rglob("*") if f.is_file() and f.suffix.lower() in VIDEO | (IMAGE if a.images else set()) and not f.name.startswith(".")]
        log(f"{root}: {len(files)} media files")
        for f in files:
            seen += 1
            st = f.stat()
            cid = hashlib.sha1(f"{f.resolve()}".encode("utf-8", "replace")).hexdigest()[:16]
            row = con.execute("select mtime,size,model from clips where id=?", (cid,)).fetchone()
            flag = flags_for(str(f), str(root), rules, cbf)
            if row and abs(row[0] - st.st_mtime) < 1 and row[1] == st.st_size and row[2] == MODEL:
                con.execute("update clips set flag=? where id=?", (flag, cid)); skipped += 1; continue
            kind = "image" if f.suffix.lower() in IMAGE else "video"
            m = probe(f) if kind == "video" else {"duration": 0, "width": None, "height": None}
            if kind == "video" and (m.get("duration") or 0) < a.min_dur:
                continue
            with tempfile.TemporaryDirectory() as td:
                fr = sample_frames(f, m.get("duration") or 0, a.frames, Path(td), kind)
                if not fr:
                    log(f"  no frames: {f.name}"); continue
                embs = embed_images([p for _, p in fr])
            con.execute("delete from frames where clip_id=?", (cid,))
            con.executemany("insert into frames values(?,?,?,?)", [(cid, k, t, embs[k].tobytes()) for k, (t, _) in enumerate(fr)])
            con.execute("insert or replace into clips values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (cid, str(f.resolve()), str(root), str(f.parent), f.name, kind, m.get("duration") or 0, m.get("width"), m.get("height"),
                         st.st_mtime, st.st_size, " ".join(tags_for(f, root)), flag, time.strftime("%Y-%m-%d %H:%M"), len(fr), MODEL))
            added += 1
            if added % 25 == 0:
                con.commit(); log(f"  {added} indexed...")
    gone = [r[0] for r in con.execute("select id,path from clips").fetchall() if not Path(r[1]).exists() and any(r[1].startswith(str(Path(x).resolve())) for x in a.roots)]
    for g in gone:
        con.execute("delete from clips where id=?", (g,)); con.execute("delete from frames where clip_id=?", (g,))
    con.commit()
    n, nf = con.execute("select count(*), sum(flag is not null) from clips").fetchone()
    log(f"index: {added} new/changed, {skipped} unchanged, {len(gone)} removed; {n} clips total ({nf or 0} flagged sensitive) -> {Path(a.index_dir) / 'broll.sqlite'}")


_CACHE = {}


def load_index(index_dir):
    import numpy as np
    key = str(index_dir)
    if key not in _CACHE:
        con = db_open(index_dir)
        clips = {r[0]: dict(zip(["id", "path", "root", "folder", "name", "kind", "duration", "width", "height", "tags", "flag"], r))
                 for r in con.execute("select id,path,root,folder,name,kind,duration,width,height,tags,flag from clips")}
        rows = con.execute("select clip_id,k,t,emb from frames").fetchall()
        E = np.stack([np.frombuffer(r[3], np.float16).astype(np.float32) for r in rows]) if rows else np.zeros((0, 512), np.float32)
        _CACHE[key] = (clips, [(r[0], r[1], r[2]) for r in rows], E)
    return _CACHE[key]


def search(index_dir, query, k=5, min_dur=0.0, allow_sensitive=False, exclude=()):
    import numpy as np
    clips, refs, E = load_index(index_dir)
    if not len(E):
        return []
    sims = E @ embed_text(query).astype(np.float32)
    best = {}
    for (cid, fk, t), s in zip(refs, sims):
        if s > best.get(cid, (-9, 0))[0]:
            best[cid] = (float(s), t)
    qt = set(re.findall(r"[a-z]{3,}", query.lower()))
    out = []
    for cid, (s, t) in best.items():
        c = clips.get(cid)
        if not c or cid in exclude or (c["flag"] and not allow_sensitive):
            continue
        if c["kind"] == "video" and (c["duration"] or 0) < min_dur:
            continue
        tag_hits = len(qt & set((c["tags"] or "").split()))
        out.append({**c, "score": round(s + 0.02 * tag_hits, 4), "clip_sim": round(s, 4), "tag_hits": tag_hits, "best_t": t})
    return sorted(out, key=lambda x: -x["score"])[:k]


def cmd_search(a):
    for r in search(a.index_dir, a.query, a.k, a.min_dur, a.allow_sensitive):
        print(f"{r['score']:.3f}  {r['duration']:6.1f}s  {r['name']}  [{r['tags']}]  {'FLAG:' + r['flag'] if r['flag'] else ''}\n        {r['path']}")


def candidates_sheet(beats, out):
    """One image for Claude: one row per beat, its top-3 candidates (frame at best_t), labelled."""
    from PIL import Image, ImageDraw
    W, H = 240, 135
    rows = [b for b in beats if b["candidates"]]
    if not rows:
        return None
    sheet = Image.new("RGB", (W * 3 + 10, (H + 22) * len(rows)), "white")
    d = ImageDraw.Draw(sheet)
    with tempfile.TemporaryDirectory() as td:
        for i, b in enumerate(rows):
            y = i * (H + 22)
            d.text((4, y + 4), f"beat {b['beat_i']}: {b['query'][:70]}", fill="black")
            for j, c in enumerate(b["candidates"][:3]):
                f = Path(td) / f"{i}_{j}.jpg"
                ffmpeg((["-ss", f"{c['best_t']:.2f}"] if c["kind"] == "video" else []) + ["-i", c["path"], "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2", "-frames:v", 1, f], check=False)
                if f.exists():
                    sheet.paste(Image.open(f), (j * W, y + 20))
                d.text((j * W + 4, y + 22), f"{chr(65 + j)}", fill="yellow")
    sheet.save(out, quality=80)
    return out


CHOOSE = """Pick B-roll for an edit. For each beat choose A, B, C or none (none if no candidate truly fits the line, would mislead,
or shows a person/patient who may not have consented). Look at the contact sheet first with your Read tool: {sheet}
(one row per beat, candidates A/B/C left to right). Brand: {brand}. Return ONLY JSON: {{"picks": [{{"beat_i": 0, "pick": "A|B|C|none", "why": "<=10 words"}}]}}
{rows}"""


def cmd_match(a, edit_dir):
    brief = rjson(edit_dir / "brief.json")
    if not brief:
        raise SystemExit("No brief.json: run `brief` first")
    style = {}
    try:
        from .presets import load_preset
        style = load_preset(brief.get("preset") or "talking-head-punchy")
    except SystemExit:
        pass
    mind = (style.get("broll") or {}).get("min_dur_s", 1.0)
    beats, used = [], set()
    for i, b in enumerate(brief.get("beats", [])):
        q = b.get("broll_query")
        if not q:
            continue
        need = min(max(mind, (float(b["t1"]) - float(b["t0"])) * 0.6), (style.get("broll") or {}).get("max_dur_s", 2.5))
        cands = search(a.index_dir, q, a.k, min_dur=need, allow_sensitive=a.allow_sensitive, exclude=used)
        beats.append({"beat_i": i, "beat": b.get("beat"), "line": b.get("line"), "query": q, "need_s": round(need, 2),
                      "candidates": [{k: c[k] for k in ("id", "path", "name", "kind", "duration", "tags", "score", "best_t", "flag")} for c in cands]})
        if cands:
            used.add(cands[0]["id"])
    sheet = candidates_sheet(beats, edit_dir / "broll_sheet.jpg")
    picks = {}
    if a.llm == "claude-cli" and sheet:
        rows = "\n".join(f"beat {b['beat_i']} ({b['beat']}): line=\"{(b['line'] or '')[:120]}\" query=\"{b['query']}\" | " +
                         " | ".join(f"{chr(65 + j)}: {c['name']} [{c['tags']}] {c['duration']:.1f}s sim={c['score']:.2f}" for j, c in enumerate(b["candidates"][:3]))
                         for b in beats if b["candidates"])
        log("broll: one claude -p call to choose among top-3 per beat")
        res = parse_json(claude(CHOOSE.format(sheet=sheet, brand=brief.get("brand"), rows=rows), image_dir=edit_dir, model=a.claude_model))
        picks = {p["beat_i"]: p for p in res.get("picks", [])}
    for b in beats:
        p = picks.get(b["beat_i"])
        if p:
            b["pick"] = None if p["pick"] == "none" else "ABC".index(p["pick"]); b["why"] = p.get("why")
        else:  # local default: top match if it clears the similarity floor
            b["pick"] = 0 if b["candidates"] and b["candidates"][0]["score"] >= a.min_score else None
            b["why"] = "top local match" if b["pick"] == 0 else "no candidate above the similarity floor"
    wjson(edit_dir / "broll_candidates.json", {"index": str(a.index_dir), "sheet": str(sheet) if sheet else None, "beats": beats})
    n = sum(1 for b in beats if b["pick"] is not None)
    log(f"broll: {n}/{len(beats)} beats matched -> broll_candidates.json" + (f", sheet {sheet}" if sheet else ""))
