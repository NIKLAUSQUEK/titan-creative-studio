# higgsfield-creative-director - install & use

## Claude.ai / Desktop (chat + Higgsfield MCP connector)
Upload `higgsfield-creative-director.skill` in Claude's Skills settings. It triggers on any Higgsfield / Kling / Seedance / "generate a video/carousel" request.

## Claude Code (recommended for heavy production)
```bash
# 1. Higgsfield MCP at user scope (one OAuth for every session)
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
#    then inside Claude Code: /mcp  -> sign in

# 2. Higgsfield's official CLI + skills (generate, soul, product-photoshoot)
npx skills add higgsfield-ai/skills
higgsfield auth login

# 3. This skill
mkdir -p ~/.claude/skills && unzip higgsfield-creative-director.skill -d ~/.claude/skills/
pip install pillow   # ffmpeg must be on PATH (brew install ffmpeg)
```
In Claude Code, `references/learnings-ledger.md` is appended after every feedback round, so the skill literally gets smarter on disk. Commit the folder to a private repo so Hermes / TITAN OS agents share the same ledger.

## Harnesses
- `scripts/compile_shots.py validate spec.json` - lints a shot spec (geography, camera owner, line length vs shot length, model duration limits, moderation-risk words, negative phrasing).
- `scripts/compile_shots.py compile spec.json --model kling_o3_image_reference` - emits a multi-shot payload.
- `scripts/qc_frames.py <urls...>` - contact sheet + metadata + TikTok/Reels safe-zone overlay.
