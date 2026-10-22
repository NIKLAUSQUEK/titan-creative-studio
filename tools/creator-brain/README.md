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
- **Use the vault with the studio:** open Claude Code in the vault folder, or copy the notes you want into `brains/<who>/` in the studio repo once that repo is private. Then `/story`, `/journal` and `/storyboard` can build on them.

## Linux/macOS
```bash
pip install faster-whisper pillow numpy
python3 creator_brain.py extract --src ~/Videos --work ~/.creatorbrain
python3 creator_brain.py sense --work ~/.creatorbrain
python3 creator_brain.py vault --work ~/.creatorbrain --vault ~/Obsidian/KlausBrain
```

---
# Style Lab: build the creator style library for free
`Run-StyleLab.ps1` does what the vidIQ-based style-runner does, on your PC, without vidIQ credits:
1. **Download:** yt-dlp fetches each creator's top short-form videos (or the exact URLs you paste in).
2. **Measure:** ffmpeg counts the cuts, average shot length and cuts in the first 3 s, and grabs hook frames (first 3 s) and a contact sheet; faster-whisper transcribes and gives words per minute.
3. **Break down:** Claude looks at the frames, metrics and transcript and writes the style breakdown using the same headings as the runner.
4. **StyleCard:** one card per creator, uploaded to Supabase `style_cards` or exported for import.

```powershell
# creators from Supabase batch 4 (needs $env:SUPABASE_URL and $env:SUPABASE_SERVICE_ROLE_KEY in this PowerShell window only)
.\Run-StyleLab.ps1 -Batch 4 -Per 3 -Browser chrome
# or your own list: copy creators.example.json, add creators + exact video URLs
.\Run-StyleLab.ps1 -Creators .\creators.example.json -Browser chrome
```
- **Getting blocked?** `-Browser chrome` (or `edge`/`firefox`) uses your logged-in browser cookies, so YouTube's "are you a bot" check and Instagram/TikTok logins pass. Close the browser first if cookie reading fails.
- **No Supabase key on the PC?** The `push` step exports `stylelab\style_cards_export.json`. Open Claude Code in the studio repo and say "import that file into style_cards".
- **Disk space:** `-DeleteVideos` deletes each video right after analysis.
- **Cost and use:** no vidIQ credits; it uses your Claude usage (about one call per video plus one per creator). Downloads are for private style analysis only: never re-upload another creator's video.

## Course mode (paid courses → study notes + workflows)
`-Mode course` turns lesson videos into notes with frameworks (ordered steps), key points, templates and prompts, tools, examples, quotes, action items, and "Apply to TITAN" (which studio skill or command each lesson should improve). Output goes to `Course Brain/`: `00 Home`, `Modules/`, `Lessons/`, plus rolled-up `Templates and Prompts`, `Action Items`, `Tools` and `Apply to TITAN`. Zip files in `-Source` are unzipped automatically. Notes are for private study; never republish course content.
