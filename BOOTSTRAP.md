# Bootstrap — paste this into Claude Code from inside this folder

```
You are setting up my creative studio repo (this folder). I only click logins/consents.
1. git init; create PRIVATE GitHub repo NIKLAUSQUEK/titan-creative-studio; push.
2. Read CLAUDE.md, BOOTSTRAP.md, .claude/settings.json, .mcp.json, the skill at .claude/skills/higgsfield-creative-director/SKILL.md.
3. Verify .claude/settings.json hooks against the CURRENT Claude Code hooks docs (docs.claude.com → Claude Code → Hooks). Fix the schema only if it differs; keep the behaviour (PreToolUse cost gate, PostToolUse logging). Then test: pipe a fake generate_video event into scripts/hooks/cost_gate.py → must exit 2; with get_cost true → exit 0.
4. MCP: confirm .mcp.json servers load (/mcp). I will sign in to higgsfield, supabase, vidiq when prompted. Run Supabase query: select count(*) from style_creators → expect 56.
5. Install Higgsfield's official CLI+skills: `npx skills add higgsfield-ai/skills` then `higgsfield auth login` (I click).
6. Local deps: ffmpeg, python3 pillow, faster-whisper (pip install --break-system-packages if needed). Run python scripts/compile_shots.py validate projects/physio-spot-spotting/spec.v2-draft.json → should PASS.
7. Smoke test the routing: run /status and /style Jun Yuh, show me results.
8. Commit "studio: bootstrap verified". Print a 6-line how-to-use summary.
```

## Daily use (no heavy prompting)
- Just talk: "make a Physio Spot skit where…", "edit it like Jun Yuh", "QC that", "that's wrong because…".
- Claude routes it via CLAUDE.md → agents → commands. Corrections become ledger rules automatically (/learn).
- On your phone: open this project in Claude Code from the Claude mobile app (remote session) — same repo, same rules.
- In claude.ai chat: install the higgsfield-creative-director.skill file; it reads the same Supabase style library. Repo stays the source of truth — say "add to ledger" in chat and paste into the repo later.
