"""Shared helpers: paths, ffmpeg/ffprobe, Claude CLI, JSON IO. Reuses tools/creator-brain where it can."""
import json, os, re, shutil, subprocess, sys, time
from pathlib import Path

PKG = Path(__file__).resolve().parent
TOOL = PKG.parent                      # tools/editor
REPO = TOOL.parent.parent              # repo root
sys.path.insert(0, str(REPO / "tools" / "creator-brain"))
import creator_brain as cb  # noqa: E402  (ffprobe, contact sheets, claude -p wrapper, JSON parsing)

VIDEO = cb.VIDEO
IMAGE = cb.IMAGE
AUDIO = cb.AUDIO
log = cb.log
run = cb.run
parse_json = cb.parse_json


def repo_path(*p):
    return REPO.joinpath(*p)


def studio(name, default=""):
    f = REPO / ".studio" / name
    return f.read_text(encoding="utf-8").strip() if f.exists() else default


def project_dir(project=None):
    project = project or studio("active_project")
    if not project:
        raise SystemExit("No project: pass --project <name> or set .studio/active_project")
    d = REPO / "projects" / project / "autoedit"  # (projects/<p>/edit/ is kept for hand-made edit scripts)
    d.mkdir(parents=True, exist_ok=True)
    return d


def rjson(p, default=None):
    p = Path(p)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def wjson(p, obj):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
    return p


def probe(path):
    pr = cb.ffprobe(Path(path))
    m = cb.meta_from_probe(pr)
    vs = next((s for s in pr.get("streams", []) if s.get("codec_type") == "video"), {})
    rot = 0
    for sd in vs.get("side_data_list", []) or []:
        if "rotation" in sd:
            rot = int(sd["rotation"])
    if abs(rot) in (90, 270) and m.get("width"):
        m["width"], m["height"] = m["height"], m["width"]
    fr = vs.get("avg_frame_rate") or vs.get("r_frame_rate") or "30/1"
    try:
        n, d = fr.split("/")
        m["fps"] = round(float(n) / float(d), 3) if float(d) else 30.0
    except Exception:
        m["fps"] = 30.0
    return m


def ffmpeg(args, cwd=None, check=True):
    cmd = ["ffmpeg", "-hide_banner", "-v", "error", "-y"] + [str(a) for a in args]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=cwd)
    if check and r.returncode != 0:
        raise RuntimeError("ffmpeg failed: " + (r.stderr or "")[-1500:] + "\nCMD: " + " ".join(cmd)[:1500])
    return r


def have(cmd):
    return shutil.which(cmd) is not None


def claude(prompt, image_dir=None, model=None, claude_bin=None):
    """One `claude -p` call on Klaus's Claude Code login (no API key). Returns the text result."""
    import argparse
    ns = argparse.Namespace(llm="claude-cli", model=model, claude_bin=claude_bin or shutil.which("claude") or "claude")
    sheet = None
    if image_dir:
        sheet = str(Path(image_dir) / "_")  # creator_brain only uses the parent dir for --add-dir
    return cb.call_llm(prompt, ns, sheet)


def slug(s, n=50):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:n] or "x"


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S")
