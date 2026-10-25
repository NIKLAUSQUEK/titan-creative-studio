# TITAN auto-editor (Windows, local)
Turns raw footage into finished edits in any brand's style: a strategist brief first, then a versioned edit recipe, a cheap draft, chat revisions and 1080p finals in every aspect ratio.
Everything runs on your PC. The heavy work (transcription, B-roll search, rendering) is local and free. Claude is used only for decisions, through your Claude Code login (`claude -p`), so there are no API keys and no API credits.

## How it works
1. **Ingest** (local): word-level transcript (faster-whisper), fillers, silences, scene cuts, retakes grouped with the best take picked, a hook shortlist and a contact sheet per clip. Output: `projects/<p>/autoedit/ingest/summary.md`, the compact text Claude reads instead of raw transcripts.
2. **Brief** (strategist first, 1 Claude call): goal, audience, platform/aspect, 5 ranked hooks, beats with source ranges, CTA, compliance notes and a preset pick. It is built from the brand file, the brain profile, `story-engine.md`, the brand's compliance packs, the marketing strategy and your Course Brain notes if they exist. Output: `EDIT_BRIEF.md` + `brief.json`.
3. **B-roll** (local, 0 tokens to search): an open_clip index of your footage folders, including `G:\My Drive\...`. Each beat's B-roll query is matched locally; Claude only picks among the top 3, using one contact sheet for all beats.
4. **Recipe**: `edit.v1.json` holds the clips and trims, word-timed captions, punch-ins, B-roll windows, hook/title/lower-third text, SFX cues, music, the end card and the output aspects. Every revision writes a new version (`edit.v2.json`, ...), and nothing is ever overwritten.
5. **Render** (deterministic ffmpeg + libass): the draft is the lowest quality (360 px short edge). The final is 1080 px, high quality, for the approved version only. Segments are cached, so a revision re-renders only the clips it changed.
6. **QC**: the studio's `scripts/qc_frames.py` contact sheet, hook and full-video frame strips, plus loudness, true peak, dead air, safe zones, the brand compliance word scan, the B-roll consent check and the music licence check. An optional Claude self-review checks the draft against the brief and the preset.

## One-time setup
1. Install Claude Code and sign in (the same as for the Creator Brain tool): install Node.js LTS, run `npm install -g @anthropic-ai/claude-code`, then run `claude` once.
2. If Windows blocks scripts, allow them once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
3. Run the selftest. The first run installs ffmpeg and Python via winget, then faster-whisper, PyTorch (CPU, or CUDA if `nvidia-smi` exists) and open_clip into `%LOCALAPPDATA%\TitanEditor\venv`. That is a 1-3 GB download, once.
```powershell
cd C:\path\to\titan-creative-studio\tools\editor
.\Run-Editor.ps1 -SelfTest
```
It ends with `SELFTEST 26/26 passed`. It uses Windows' built-in voice to make a test clip.

## Daily use
```powershell
cd C:\path\to\titan-creative-studio\tools\editor

# 1) Index B-roll once (re-run any time; only new or changed files are processed)
.\Run-Editor.ps1 -BrollRoots "G:\My Drive\clinic_broll","D:\Footage\B-roll" -Steps broll-index

# 2) Footage -> brief -> B-roll -> recipe -> draft (all aspects) -> QC
.\Run-Editor.ps1 -Project back-pain-myth -Footage "D:\Shoots\2026-10-24" -Brand physio-spot `
  -Goal expert -Platform tiktok -Ask "myth-bust for men 30-45, end on booking via WhatsApp"

# 3) Revise in plain words: each note makes a new recipe version + a new draft
.\Run-Editor.ps1 -Project back-pain-myth -Revise "cut first 2 s, punchier captions"
.\Run-Editor.ps1 -Project back-pain-myth -Revise "go back to v3"
.\Run-Editor.ps1 -Project back-pain-myth -Chat          # type notes one after another

# 4) Approve the draft you like, then render 1080p finals of every aspect + QC + handoff for /publish
.\Run-Editor.ps1 -Project back-pain-myth -Approve -Final
```
Outputs go to `projects\<p>\autoedit\`: `EDIT_BRIEF.md`, `edit.vN.json`, `renders\vN_9x16_draft.mp4` (and 1x1, 16x9), `qc\QC_vN_draft.md` + contact sheets, and `HANDOFF.md`.

| Option | Default | Notes |
|---|---|---|
| `-Preset` | from the brief | `.\Run-Editor.ps1 -Presets` lists them: 6 styles + 8 UGC formats, plus `style-<creator>` presets you make from StyleCards |
| `-Aspects` | brief's platform + others | e.g. `"9:16,1:1,16:9"`; all come from the same recipe |
| `-Music` / `-MusicLicence` | none | brand accounts: `original` or `licensed:<source>` only; `in-app` sounds are never baked in (see `/sound`) |
| `-Llm none` | `claude-cli` | zero-token heuristics (best takes in order, top hook first); good for testing |
| `-ClaudeModel sonnet` | your default | Sonnet is cheaper and plenty for briefs and revisions |
| `-WhisperModel` | `large-v3` with a GPU, else `small` | use `medium` for Singlish/Chinese on a fast CPU |
| `-IndexDir` | `%LOCALAPPDATA%\TitanEditor` | where the B-roll index (`broll.sqlite`) lives |

## Revision phrases that cost zero tokens
These revision phrases are applied locally, with no Claude call:
- trim: `cut first 2 s`, `trim last 1.5 s`
- versions: `go back to v3`
- captions: `punchier captions`, `smaller captions`, `captions off`
- music: `no music`, `music up`, `music down`
- zooms: `more zooms`, `fewer zooms`, `no zooms`
- SFX: `more sfx`, `less sfx`
- pacing: `tighter`, `slower`
- hook text: `hook text: STOP STRETCHING`
- aspects: `only 9:16`, `add 1:1`

You can combine them: `"cut first 2 s, punchier captions, music down"`. Anything else ("swap the B-roll on beat 3 for the gym clip", "move the CTA earlier") goes to one `claude -p` call that returns the full new recipe, which is validated before saving.

## B-roll consent and privacy
- Files or folders whose path contains `private`, `personal`, `no-use`, `patient(s)`, `client(s)`, `minor(s)`, `kids`, `children`, `family`, `medical`, `nsfw` or `consent-pending` are **flagged and never suggested** unless you pass `--allow-sensitive` and decide it yourself.
- For finer control, put a `broll_flags.json` in any indexed root, e.g. `{"2024 wedding/*": "family", "*_ok.mp4": null}`.
- If the Creator Brain extractor has run, its per-file `sensitivity` flags are reused automatically.
- **Google Drive for desktop:** indexing reads only 4 frames per clip, but streamed files download on first read, so mark B-roll folders "Available offline" for speed.

## Style presets from StyleCards
```powershell
# from Supabase titan-os (needs $env:SUPABASE_URL + $env:SUPABASE_SERVICE_ROLE_KEY in this window only)
& "$env:LOCALAPPDATA\TitanEditor\venv\Scripts\python.exe" editor.py preset from-stylecard "Jun Yuh"
# or from the Style Lab export, no keys needed
& "$env:LOCALAPPDATA\TitanEditor\venv\Scripts\python.exe" editor.py preset from-stylecard "Jun Yuh" --file "$env:LOCALAPPDATA\CreatorBrain\stylelab\style_cards_export.json"
```
This writes `presets\style-jun-yuh.json`, which maps `avg_shot_s`, captions, sound, lighting and energy to concrete edit parameters. Use it with `-Preset style-jun-yuh`.

## Brand guide
The editor reads the ```` ```edit-brand ```` JSON block in `brands/<brand>.md` (see Physio Spot §6b): fonts, colours, caption and hook placement, end card, grade and the brand's forbidden words. Without the block it guesses from §6 (hex colours, font names). Put brand font files in `assets\fonts\<brand>\`; the bundled DejaVu fonts are the fallback.

## Time and cost
- **Ingest:** about real time on a CPU with `small`, and much faster on a GPU.
- **B-roll indexing:** about 0.3-1 s per clip on CPU, once.
- **Rendering:** a 30 s draft in all 3 aspects takes about 20 s; finals take about 1-2 min.
- **Claude:** about 1 call per brief, 1 per B-roll pick, 1 per free-text revision and 1 per optional self-review, each using a few thousand tokens, all counted against your Claude usage.

## Linux/macOS (and the cloud container)
```bash
python3 -m venv ~/.titan-editor/venv && . ~/.titan-editor/venv/bin/activate
pip install faster-whisper pillow numpy "opencv-python-headless<5" rembg   # opencv = face-occlusion QC
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu && pip install open_clip_torch
python tools/editor/editor.py selftest          # needs espeak-ng for the synthetic voice
python tools/editor/editor.py --project P run /path/to/footage --brand physio-spot --goal expert --platform tiktok
```
