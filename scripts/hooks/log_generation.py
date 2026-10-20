#!/usr/bin/env python3
"""PostToolUse hook: appends every Higgsfield generation call to registry/generations.csv."""
import json, sys, os, csv, pathlib, datetime
ROOT = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR", ".")).resolve()
d = json.load(sys.stdin); inp = d.get("tool_input", {}) or {}; p = inp.get("params", inp) if isinstance(inp, dict) else {}
if isinstance(p, dict) and p.get("get_cost"): sys.exit(0)
ap = ROOT / ".studio" / "active_project"; proj = ap.read_text().strip() if ap.exists() else ""
resp = json.dumps(d.get("tool_response", ""))[:300]
summary = json.dumps({k: p.get(k) for k in ("model", "mode", "duration", "aspect_ratio", "resolution") if isinstance(p, dict) and k in p})
with open(ROOT / "registry" / "generations.csv", "a", newline="") as f:
    csv.writer(f).writerow([datetime.datetime.now().isoformat(timespec="seconds"), d.get("tool_name"), (p or {}).get("model", "") if isinstance(p, dict) else "", proj, "", summary, resp])
sys.exit(0)
