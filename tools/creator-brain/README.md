# Creator Brain extractor (Windows)
Turns your folders of videos, voice notes and photos into an Obsidian vault Claude can work from.

## What you get
Your vault gets a `Creator Brain/` folder:
- `00 Home`: counts, eras, top themes, and a Dataview table of everything.
- `Media/`: one note per video or photo, containing:
  - a summary, era, people, places, themes and emotions;
  - verbatim quotes with timestamps;
  - story seeds (lesson, wisdom note, trope stance) and 5 hooks;
  - values, beliefs and principles (draft until you confirm);
  - content ideas, and techniques to borrow when it's another creator's video;
  - a sensitivity flag, the contact sheet, and the full transcript in a folded section.
- `Eras/`, `Themes/` and `People/`: index notes linking back to the media.
- `Quotes`, `Hooks`, `Story Seeds`, `Values Beliefs Principles`, `Wisdom Notes`, `Content Ideas` and `Reference Techniques`: everything rolled up across all media.

## One-time setup
1. **Copy this folder** (`tools/creator-brain/`) to your PC, or clone the repo.
2. **Install Claude Code**, so the analysis runs on your Claude subscription with no API key:
   - install Node.js LTS;
   - in PowerShell, run `npm install -g @anthropic-ai/claude-code`;
   - run `claude` once to sign in.
3. **Allow scripts once**, if Windows blocks them: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
4. **Let the script install the rest.** On the first run it installs ffmpeg and Python via winget if they're missing, then faster-whisper into its own environment under `%LOCALAPPDATA%\CreatorBrain`.

## Run
```powershell
cd path\to\tools\creator-brain
# test on 5 files first
.\Extract-CreatorBrain.ps1 -Source "D:\Creator Brain" -Limit 5
# then everything (several folders allowed, incl. Google Drive for desktop paths)
.\Extract-CreatorBrain.ps1 -Source "D:\Creator Brain","G:\My Drive\mens_health_social","G:\My Drive\pelvic_videos_2"
```
Then open Obsidian, choose **Open folder as vault**, and pick `Documents\Obsidian\Klaus Brain` (or your `-Vault`). Start from `Creator Brain/00 Home`. The Dataview community plugin is optional and adds a sortable table.

| Option | Default | Notes |
|---|---|---|
| `-Vault` | `Documents\Obsidian\Klaus Brain` | point it at an existing vault to merge |
| `-WhisperModel` | auto: `large-v3` with an NVIDIA GPU, else `small` | use `medium` on a fast CPU for better Singlish/Chinese |
| `-Language` | auto per file | `en`, `zh`, `ms` to force one language |
| `-ClaudeModel` | your Claude Code default | `sonnet` (cheaper/faster) or `opus` (deeper) |
| `-Llm api` | off | uses `$env:ANTHROPIC_API_KEY` instead of Claude Code |
| `-Steps` | extract, sense, vault | e.g. `-Steps vault` to rebuild notes only |
| `-Limit` | 0 (all) | process N new files per step |

**Time and cost:**
- **Transcription is free and local.** On a CPU with `small`, it runs at roughly real time to 3× real time per video; a GPU is far faster.
- **Analysis is one Claude call per file,** which counts against your Claude usage limits. Run big libraries overnight; if you hit a limit, just run again later and finished files are skipped.

## Privacy
- **Everything stays on your PC** except the transcript text and contact sheet sent to Claude for analysis.
- **Keep the vault private.** It may contain family, minors and clients. Don't put it in a public GitHub repo; `sensitivity` flags what needs consent before use.
- **Use the vault with the studio:** open Claude Code in the vault folder, or copy the notes you want into `brain/` in the studio repo once that repo is private. Then `/story`, `/journal` and `/storyboard` can build on them.

## Linux/macOS
```bash
pip install faster-whisper pillow numpy
python3 creator_brain.py extract --src ~/Videos --work ~/.creatorbrain
python3 creator_brain.py sense --work ~/.creatorbrain
python3 creator_brain.py vault --work ~/.creatorbrain --vault ~/Obsidian/KlausBrain
```
