"""TITAN auto-editor CLI. Every step is resumable and runs locally; Claude (`claude -p`, your Claude Code login) is used only for decisions.

  editor.py check
  editor.py ingest  --project P <files/folders...>            word timestamps, silences, fillers, scenes, best takes, hooks, sheets
  editor.py brief   --project P [--goal sell --platform tiktok --ask "..."] [--llm claude-cli|none] [--pack-only]
  editor.py broll-index <roots...>                            local open_clip index (G:\\My Drive\\... works), incremental
  editor.py broll-search "query"                              zero-token text -> top-k
  editor.py broll-match --project P [--llm claude-cli|none]   per beat top-k; Claude only picks among top 3
  editor.py assemble --project P [--preset X --aspects 9:16,1:1,16:9 --music file --music-licence original]
  editor.py revise  --project P "cut first 2 s, punchier captions"     -> new edit.vN.json (quick ops cost 0 tokens)
  editor.py revert  --project P 3 | fork | validate | versions | approve
  editor.py render  --project P [--final] [--aspects 9:16]    draft = lowest quality; final needs an approved version
  editor.py qc      --project P [--final] [--llm claude-cli]
  editor.py run     --project P <footage...>                  ingest -> brief -> broll -> assemble -> draft -> qc
  editor.py chat    --project P                               revision loop: type a note, get a new draft
  editor.py export  --project P [--version N] [--fps 30]      CMX3600 EDL of the cut (A-roll + B-roll on V2) for Premiere/Resolve finishing
  editor.py preset  list | show NAME | from-stylecard NAME [--file card.json]
  editor.py selftest                                          synthetic end-to-end test
"""
import argparse, shutil, sys

from .common import have, log, project_dir, studio


def add_llm(p, default="claude-cli"):
    p.add_argument("--llm", choices=["claude-cli", "none"], default=default, help="claude-cli = `claude -p` on your Claude Code login; none = local heuristics only")
    p.add_argument("--claude-model", default=None, help="e.g. sonnet (cheaper) or opus; default = your Claude Code default")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="editor.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", default=None, help="projects/<name> (default: .studio/active_project)")
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("check")
    p = sp.add_parser("ingest"); p.add_argument("footage", nargs="+")
    p.add_argument("--whisper-model", default="auto"); p.add_argument("--device", default="auto"); p.add_argument("--language", default=None); p.add_argument("--force", action="store_true")
    p = sp.add_parser("brief"); add_llm(p)
    for k in ("goal", "platform", "aspect", "preset", "ask", "brand", "brain", "course-brain", "from-json"):
        p.add_argument("--" + k, default=None)
    p.add_argument("--target-s", type=float, default=None); p.add_argument("--pack-only", action="store_true")
    from .broll import default_index_dir
    p = sp.add_parser("broll-index"); p.add_argument("roots", nargs="+"); p.add_argument("--index-dir", default=str(default_index_dir()))
    p.add_argument("--frames", type=int, default=4); p.add_argument("--min-dur", type=float, default=0.8); p.add_argument("--images", action="store_true")
    p.add_argument("--creator-brain-work", default=None, help="Creator Brain work folder: reuse its sensitivity flags")
    p = sp.add_parser("broll-search"); p.add_argument("query"); p.add_argument("--index-dir", default=str(default_index_dir())); p.add_argument("-k", type=int, default=5)
    p.add_argument("--min-dur", type=float, default=0); p.add_argument("--allow-sensitive", action="store_true")
    p = sp.add_parser("broll-match"); add_llm(p); p.add_argument("--index-dir", default=str(default_index_dir())); p.add_argument("-k", type=int, default=5)
    p.add_argument("--min-score", type=float, default=0.2); p.add_argument("--allow-sensitive", action="store_true")
    p = sp.add_parser("assemble"); p.add_argument("--preset"); p.add_argument("--aspects"); p.add_argument("--music"); p.add_argument("--music-licence")
    p = sp.add_parser("revise"); p.add_argument("instruction"); p.add_argument("--base", default=None); add_llm(p)
    p = sp.add_parser("revert"); p.add_argument("to", type=int)
    p = sp.add_parser("fork"); p.add_argument("--base", default=None); p.add_argument("-m", "--message", default=None)
    p = sp.add_parser("validate"); p.add_argument("--version", default=None)
    sp.add_parser("versions")
    p = sp.add_parser("approve"); p.add_argument("--version", default=None)
    p = sp.add_parser("render"); p.add_argument("--version", default=None); p.add_argument("--final", action="store_true"); p.add_argument("--aspects"); p.add_argument("--force", action="store_true")
    p = sp.add_parser("qc"); p.add_argument("--version", default=None); p.add_argument("--final", action="store_true"); add_llm(p, "none")
    p = sp.add_parser("handoff"); p.add_argument("--version", default=None)
    p = sp.add_parser("export"); p.add_argument("--version", default=None); p.add_argument("--fps", type=int, default=30)
    p = sp.add_parser("run"); p.add_argument("footage", nargs="*"); add_llm(p)
    for k in ("goal", "platform", "aspect", "preset", "ask", "brand", "brain", "course-brain", "music", "music-licence", "aspects"):
        p.add_argument("--" + k, default=None)
    p.add_argument("--target-s", type=float, default=None); p.add_argument("--whisper-model", default="auto"); p.add_argument("--device", default="auto")
    p.add_argument("--language", default=None); p.add_argument("--index-dir", default=str(default_index_dir())); p.add_argument("--broll-roots", nargs="*", default=[])
    p.add_argument("--no-broll", action="store_true")
    p = sp.add_parser("chat"); add_llm(p)
    p = sp.add_parser("preset"); p.add_argument("action", choices=["list", "show", "from-stylecard"]); p.add_argument("name", nargs="?")
    p.add_argument("--file"); p.add_argument("--base", default="talking-head-punchy")
    p = sp.add_parser("selftest"); p.add_argument("--keep", action="store_true"); p.add_argument("--whisper-model", default="tiny"); p.add_argument("--no-clip", action="store_true")
    a = ap.parse_args(argv)
    if getattr(a, "whisper_model", None) == "auto":
        a.whisper_model = "large-v3" if have("nvidia-smi") else "small"

    if a.cmd == "check":
        return check(a.project)
    if a.cmd == "preset":
        from .presets import cmd_preset
        return cmd_preset(a)
    if a.cmd == "broll-index":
        from .broll import cmd_index
        return cmd_index(a)
    if a.cmd == "broll-search":
        from .broll import cmd_search
        return cmd_search(a)
    if a.cmd == "selftest":
        from .selftest import selftest
        return selftest(a)
    ed = project_dir(a.project)
    if a.cmd == "ingest":
        from .ingest import cmd_ingest
        return cmd_ingest(a, ed)
    if a.cmd == "brief":
        from .brief import cmd_brief
        return cmd_brief(a, ed)
    if a.cmd == "broll-match":
        from .broll import cmd_match
        return cmd_match(a, ed)
    from . import recipe
    if a.cmd == "assemble":
        return recipe.cmd_assemble(a, ed)
    if a.cmd == "revise":
        return recipe.cmd_revise(a, ed)
    if a.cmd == "revert":
        r = recipe.load(ed, a.to)
        return recipe.save_new(ed, r, f"revert to v{a.to}", parent=a.to)
    if a.cmd == "fork":
        return recipe.cmd_fork(a, ed)
    if a.cmd == "validate":
        return recipe.cmd_validate(a, ed)
    if a.cmd == "versions":
        return recipe.cmd_versions(a, ed)
    if a.cmd == "approve":
        return recipe.cmd_approve(a, ed)
    if a.cmd == "render":
        from .render import cmd_render
        return cmd_render(a, ed)
    if a.cmd == "qc":
        from .qc import cmd_qc
        return cmd_qc(a, ed)
    if a.cmd == "export":
        from .checks import export_edl
        from .ingest import load_clips
        r = recipe.load(ed, a.version)
        return export_edl(r, {c["id"]: c for c in load_clips(ed)}, ed / f"edit_v{r['version']}.edl", a.fps)
    if a.cmd == "handoff":
        from .qc import handoff
        return handoff(ed, a.version)
    if a.cmd == "run":
        return pipeline(a, ed)
    if a.cmd == "chat":
        return chat(a, ed)


def pipeline(a, ed):
    from .brief import cmd_brief
    from .ingest import cmd_ingest
    from .qc import run_qc
    from .recipe import assemble
    from .render import render
    if a.footage:
        a.force = False
        cmd_ingest(a, ed)
    a.pack_only, a.from_json = False, None
    cmd_brief(a, ed)
    if not a.no_broll:
        if a.broll_roots:
            from .broll import cmd_index
            cmd_index(argparse.Namespace(roots=a.broll_roots, index_dir=a.index_dir, frames=4, min_dur=0.8, images=False, creator_brain_work=None))
        from .broll import cmd_match, db_open
        con = db_open(a.index_dir)
        if con.execute("select count(*) from clips").fetchone()[0]:
            cmd_match(argparse.Namespace(index_dir=a.index_dir, k=5, min_score=0.2, allow_sensitive=False, llm=a.llm, claude_model=a.claude_model), ed)
        else:
            log("no B-roll index yet (run broll-index on your footage folders); continuing without B-roll")
    assemble(ed, a.preset, a.aspects.split(",") if a.aspects else None, a.music, a.music_licence)
    render(ed, None, "draft")
    verdict, md = run_qc(ed, None, "draft", a.llm, a.claude_model)
    log(f"draft ready. Brief: {ed / 'EDIT_BRIEF.md'} | QC: {md} | renders: {ed / 'renders'}")


def chat(a, ed):
    from . import recipe
    from .qc import run_qc
    from .render import render
    log("Revision chat. Type a note (e.g. 'cut first 2 s, punchier captions'), 'versions', 'approve', 'final', or 'quit'.")
    while True:
        try:
            note = input("\nrevision> ").strip()
        except EOFError:
            break
        if note in ("", "quit", "exit", "q"):
            break
        try:
            if note == "versions":
                recipe.cmd_versions(a, ed); continue
            if note == "approve":
                recipe.cmd_approve(argparse.Namespace(version=None), ed); continue
            if note == "final":
                render(ed, None, "final"); run_qc(ed, None, "final", "none")
                from .qc import handoff
                handoff(ed); continue
            recipe.cmd_revise(argparse.Namespace(instruction=note, base=None, llm=a.llm, claude_model=a.claude_model), ed)
            _, res = render(ed, None, "draft")
            run_qc(ed, None, "draft", "none")
            log("new draft: " + ", ".join(x["path"] for x in res))
        except (SystemExit, ValueError, RuntimeError) as e:
            log(f"! {e}")


def check(project=None):
    ok = True
    for c in ("ffmpeg", "ffprobe"):
        print(f"{c:14} {'ok' if have(c) else 'MISSING (winget install Gyan.FFmpeg)'}"); ok &= have(c)
    print(f"{'claude':14} {'ok' if have('claude') else 'missing: npm install -g @anthropic-ai/claude-code, then run claude once to sign in'}")
    for mod, hint in (("faster_whisper", "pip install faster-whisper"), ("numpy", "pip install numpy"), ("PIL", "pip install pillow"),
                      ("torch", "pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu"), ("open_clip", "pip install open_clip_torch")):
        try:
            __import__(mod); print(f"{mod:14} ok")
        except Exception:
            print(f"{mod:14} MISSING ({hint})"); ok &= mod not in ("torch", "open_clip")
    print(f"{'gpu':14} {'nvidia' if have('nvidia-smi') else 'cpu only (fine; whisper small + CLIP on CPU)'}")
    print(f"{'project':14} {project or studio('active_project') or '(none: pass --project)'}  brand={studio('active_brand')}  brain={studio('active_brain')}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
