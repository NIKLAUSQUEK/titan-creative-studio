#!/usr/bin/env python3
"""PreToolUse hook: blocks paid Higgsfield generations unless the active project's spec is approved.
Allows cost quotes (get_cost: true) and anything Klaus explicitly unlocks via .studio/allow_once.
Exit 2 = block (stderr is shown to Claude)."""
import json, sys, os, pathlib
ROOT = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR", ".")).resolve()
data = json.load(sys.stdin)
inp = data.get("tool_input", {}) or {}
params = inp.get("params", inp)
if isinstance(params, dict) and params.get("get_cost"):
    sys.exit(0)  # quotes are free
allow = ROOT / ".studio" / "allow_once"
if allow.exists():
    allow.unlink(); sys.exit(0)
ap = ROOT / ".studio" / "active_project"
proj = ap.read_text().strip() if ap.exists() else ""
spec = ROOT / "projects" / proj / "spec.json"
try:
    ok = json.loads(spec.read_text()).get("approved") is True
except Exception:
    ok = False
if not ok:
    print(f"BLOCKED by cost gate: projects/{proj}/spec.json is missing or not approved. Run /plan, show Klaus the cost quote, and set \"approved\": true only after he says yes. (One-off exception: Klaus can ask you to create .studio/allow_once.)", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
