"""Code-motion cards (tools/motion): HTML templates rendered frame-exact by headless Chromium -> mp4 the editor uses as B-roll.

B-roll entry: {"kind": "motion", "template": "step-cards", "data": {...}, "dur": 4, "mode": "full|split|side|pip", "anchor": {...}}
"""
import hashlib, json, shutil, subprocess, tempfile
from pathlib import Path

from .common import REPO, log

MOTION = REPO / "tools" / "motion"


def templates():
    return sorted(p.stem for p in (MOTION / "templates").glob("*.html"))


def render_motion(template, data, out, w=1080, h=1920, fps=30, dur=None):
    node = shutil.which("node")
    if not node:
        raise SystemExit("code motion needs Node.js 18+ (winget install OpenJS.NodeJS.LTS), then in tools/motion: npm i playwright && npx playwright install chromium")
    tpl = MOTION / "templates" / f"{template}.html"
    if not tpl.exists():
        raise SystemExit(f"unknown motion template {template}; have: {', '.join(templates())}")
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(data or {}, f)
    args = [node, str(MOTION / "render.mjs"), str(tpl), str(out), "--data", f.name, "--w", str(w), "--h", str(h), "--fps", str(fps)] + (["--dur", f"{dur:.3f}"] if dur else [])
    r = subprocess.run(args, capture_output=True, text=True, timeout=1800)
    Path(f.name).unlink(missing_ok=True)
    if r.returncode != 0 or not Path(out).exists():
        raise SystemExit("motion render failed: " + (r.stderr or r.stdout)[-800:])
    return Path(out)


def cached(b, w, h, fps, cache):
    key = hashlib.sha1(json.dumps({"t": b["template"], "d": b.get("data"), "w": w, "h": h, "fps": fps, "dur": b.get("dur")}, sort_keys=True).encode()).hexdigest()[:16]
    out = Path(cache) / f"motion_{b['template']}_{key}.mp4"
    if not out.exists():
        log(f"  motion card {b['template']} {w}x{h}")
        render_motion(b["template"], b.get("data"), out, w - w % 2, h - h % 2, fps, b.get("dur"))
    return out


def cmd_motion(a):
    if a.list or not a.template:
        print("\n".join(templates())); return 0
    data = json.loads(Path(a.data).read_text(encoding="utf-8")) if a.data else {}
    out = render_motion(a.template, data, a.out or f"{a.template}.mp4", a.w, a.h, a.fps)
    print(out)
    return 0
