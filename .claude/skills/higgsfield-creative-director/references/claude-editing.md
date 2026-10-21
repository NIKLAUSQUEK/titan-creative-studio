# Editing with Claude: ffmpeg pipelines, code video, After Effects / Premiere, Higgsfield

Source tags are explained in `research/sources-editing.md`.
**Environment note:** this studio repo runs in a Linux cloud container, which can run ffmpeg, faster-whisper, Remotion and HyperFrames (Node 22 + Chrome). After Effects and Premiere run only on Klaus's Mac or Windows machine, so their MCP servers must be installed there and used from Claude Code or Claude Desktop on that machine.

## 1. The six jobs: give Claude one job at a time [Duncan]
Asking for a finished video in one go gives a cheap "AI look". Split the work into jobs, each with a way to check itself ("loop engineering"):
1. **Research and script.** Mine hooks from outlier videos in the niche (more than 3x the channel's normal views) into a hook library. Every fact must be checked against a real file or web page, and an unproven line is cut.
2. **The cut.** A word-level transcript, keep the last clean take of each line, cut retakes and long pauses (≈80% retake catch rate early on), and measure and fix **AV offset** (camera picture lagging the mic).
3. **The plan.** A beat map: every sentence → what's on screen (140 beats for a long video). Use references, never let Claude guess the look. Plan every graphic against the beat map before building any.
4. **Graphics.** Split into sections and use parallel sub-agents (6 worked) building in code (HyperFrames / Remotion). Use Opus or Fable to plan and Sonnet to build. Queue renders one at a time, motion blur off, half-size drafts.
5. **Checking.** Look at **10 frames per second**, not 1, and check for six failure types: double-played animation, a one-frame flash, text too late to read, a graphic over the face, a repeated word, and lip drift.
6. **Learning.** Every note from Klaus goes into the rule that would have prevented it. Rewrite the old rule rather than stacking a new one, which stops drift and bloat. This maps to the studio's `/learn` + `ledger/learnings.md`.
Duncan's 2026 numbers: ~12 h Claude time and ~1.4B tokens (≈$445 at API prices, or covered by a Max 20x plan) versus 3-7 days for a human editor. [Duncan]

## 2. Six-step checkpoint workflow for a talking-head reel [100x]
1. Prerequisites: a Claude plan plus the starting assets (footage, script, VO). Use Claude Code in the desktop app, which has local file access.
2. **Style training:** 15-20 consistent reference images → "describe the style, don't edit yet" → approve.
3. **Style test:** 3 static frames from 3 script lines.
4. **Animation test:** animate frame 1.
5. **Storyboard:** Claude drafts and you cut, or you draft and Claude critiques.
6. **Edit:** "Using the storyboard, my script and the art style, create the final video." Opus at medium effort (high sometimes helps). Expect 20-90 min. **Feed footage in 1-2 min chunks.** Iterate, because the first draft is only a draft.
Their result: a 60 s reel in under 30 min for under $2. [100x]

## 3. Training Claude on a house style (long form) [Joseph-YT]
- Pick ~10 of the brand's best videos. Prompt (Opus, extra-high effort): "Study my editing style. Transcribe all 10, cut out every animation and break it down frame by frame, study when and why each visual was chosen against what I'm saying, and study the design: composition, colours, fonts, objects, style." → 458 animations were catalogued into data, an inspiration guide (A-roll, media frames, numbers, objects, text, UI) and a style-board web page → a long-form editing skill for Remotion.
- **Cost control:** loading every reference cost ~4.5M tokens per run, so have Claude build an **index** that picks only the refs each planned scene needs (<100K tokens) and offers options.
- **Long-form pipeline:** cut (silences and bad takes, padding under 20 ms, script as reference; slow in Claude, ~1.5 h for 30 min of raw footage, so a dedicated cutter is faster) → human scene plan in Figma (dictated, 1.5-2 h for 18 min) → Claude recommends design refs per scene → build the intro only and send a **design sheet** → revise → build the body in phases, with a design sheet per phase → sound design → music. That took ~12 h total with ~1.5 h of human work.
- The short-form training prompt from the shared Drive (paraphrased) reads a full brief board: caption system (sans + script font, placement, colour, animation), caption inspiration board, **hook psychology doc**, an on-screen animation guide with 4 categories (**text-centric, object-centric, character-centric, video-centric**), "how to create animations" (background → placement → effects → stylise), a UI and graph inspiration board, and the on-screen card rule (darken and blur behind). [UE-Prompts]
- **Do this for Klaus:** build `style_cards` entries the same way (the Supabase `titan-os` style library already exists), with one index file per creator style so runs load only what they need.

## 4. Local pipeline: Claude Code + ffmpeg (runs in this repo)
```bash
# Proxy for fast review (half-size draft rule)
ffmpeg -i master.mp4 -vf scale=-2:540 -c:v libx264 -crf 28 -preset veryfast -c:a aac -b:a 96k proxy.mp4

# Word transcript (see clipping-podcast.md §6 for the faster-whisper snippet) -> words.json

# Find dead air
ffmpeg -i master.mp4 -af silencedetect=noise=-35dB:d=0.35 -f null - 2> silences.txt

# Claude writes keep.txt from words.json + silences (last clean take per line), as an ffconcat list:
#   ffconcat version 1.0
#   file master.mp4
#   inpoint 3.120
#   outpoint 9.480
#   file master.mp4        <- repeat the file line for every kept segment
#   inpoint 11.020
#   outpoint 15.300
ffmpeg -f concat -safe 0 -i keep.txt -c:v libx264 -crf 18 -c:a aac -b:a 192k cut.mp4

# AV-offset fix (picture lags audio by N ms -> delay audio by N ms)
ffmpeg -i cut.mp4 -itsoffset 0.067 -i cut.mp4 -map 0:v -map 1:a -c copy cut_synced.mp4

# Overlay a rendered graphic (ProRes 4444 / WebM with alpha) from 12.5 s to 16 s
ffmpeg -i cut_synced.mp4 -i card.mov -filter_complex \
 "[1:v]setpts=PTS-STARTPTS+12.5/TB[g];[0:v][g]overlay=enable='between(t,12.5,16)'" -c:a copy comp.mp4

# Burn captions, normalise, QC
ffmpeg -i comp.mp4 -vf "ass=captions.ass" -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v libx264 -crf 18 final.mp4
python3 scripts/qc_frames.py final.mp4
```
Ask Claude to keep every decision as data (`edl.json`: clips, in/out, overlays, captions, SFX cues) so changes are re-runs, not re-edits.

## 5. Sound design pass (any route) [UE-Sound]
The Drive training doc "UE-Sound-Design-Claude-Training-COMPLETE.md" boils down to:
- **Three families with three jobs:** whooshes for movement, textures for events that don't slide (pop, click, reveal, write-on), and risers plus hits for anticipation.
- **Order is fixed:** analyse the whole video first (classify each moment as MOVEMENT, EVENT or BUILD, with a timecoded cue sheet) → ask 2-3 questions → Pass 1 whooshes → Pass 2 textures → Pass 3 risers and hits → Pass 4 music only after approval.
- **Placement:** a whoosh **peak on the fastest frame** of the motion, a texture exactly on the event frame, a riser **ending** on the transition frame with a hit under it, and transition sounds leading picture by 2-3 frames.
- **Levels:** whooshes -12 dB (max -10), textures -6 to -7 dB, risers -5 dB, music -19 dB **under the talking head only, never under graphics**. Voice is king, so if the loudest stack would clip, pull the hit, not the voice.
- **Rules:** one family per track, mute rather than delete original audio, audition every variation in a folder before choosing, a riser about 5 s after the hook, at least 2 sharp-bass and 2 metallic risers per video, one impact per scene, sound scale matches shot scale, and diegetic sounds first.
- Joseph's version: give Claude the sound-design doc plus SFX library folder access. It runs an audio audit and does the intro first for revisions, with fixes like "align the whoosh peak to where the animation hands back to raw footage" and "cash-register SFX whenever money is mentioned". About 1.5 h for 18 min. [Joseph-YT]
- In this studio, `/sound` (licensed SFX and trending audio) feeds these cue rules.

## 6. Code video: Remotion vs HyperFrames
| | Remotion | HyperFrames |
|---|---|---|
| Authoring | React components | Plain HTML/CSS + GSAP/Lottie/Three.js, no build step |
| Setup | `npx create-video@latest --yes --blank my-video && cd my-video && npx remotion skills add && npm run dev`, then `claude` | `npx hyperframes init my-video && cd my-video && npx hyperframes preview` / `render` (Node 22+, FFmpeg) |
| Claude plugin | `claude plugin marketplace add remotion-dev/claude-code-plugin && claude plugin install remotion@remotion` | `claude plugin marketplace add heygen-com/hyperframes && claude plugin install hyperframes@hyperframes` |
| Skills | `/remotion-best-practices`, `/remotion-captions`, `/remotion-maps`, `/remotion-render`, … | `/hyperframes` router (core skills) |
| License | Source-available Remotion License (check company terms) | Apache-2.0, no per-render fees |
| Used by | Joseph (long-form style, sound design in Remotion Studio) [Joseph-YT] | Duncan (word-by-word captions, sub-agent graphics) [Duncan] |
Sources: [Remotion-docs] [HyperFrames]. **Pick HyperFrames by default for this studio** (license-clean, plain HTML suits agents). Use Remotion when reusing UE-style Remotion skills.

## 7. Claude inside After Effects (MCP / ExtendScript)
**Why:** full creative control. Claude builds editable comps, layers, keyframes, expressions and effects, and you can study how a complex animation was built by asking Claude to construct it and then inspecting the layers. [HF-Motion] [100x]
Options (all community, MIT; read the code before installing):
- **`a-y-ibrahim/after-effects-mcp`** has 57 tools, including `see-frame` (renders a frame back so Claude can see its work), `contact-sheet`, `match-reference`, `animate-to-audio`, background `aerender` and `execute-script` (arbitrary ExtendScript).
  ```bash
  git clone https://github.com/a-y-ibrahim/after-effects-mcp.git && cd after-effects-mcp
  npm install && npm run install-bridge
  # AE: Settings > Scripting & Expressions > "Allow Scripts to Write Files and Access Network"; restart AE
  # AE: Window > mcp-bridge-auto.jsx (keep open)
  claude mcp add AfterEffectsMCP node /absolute/path/to/after-effects-mcp/build/index.js
  # test: "check the After Effects bridge"
  ```
- **`23d1/after-effects-mcp`** needs no panel (osascript / AfterFX.exe dispatch), has `npm run doctor`, one undo group per tool, and `ae_save_frame` for visual checks. `claude mcp add --scope user after-effects -- node /path/dist/index.js`
- **`JUNKDOGE-JOE/after-effects-mcp` (ae-mcp)** is a CEP panel with an HTTP MCP (`claude mcp add --transport http ae http://127.0.0.1:11488/mcp`), checkpoints and recovery, and saves successful scripts as reusable tools.
- Also `Dakkshin/after-effects-mcp` (the original) and `shibin0/mcp-ae` (AppleScript/COM/aerender).
- **Claude Motion → AE:** "transfer the project with editable layers into After Effects" worked, slowly. [HF-Motion] 100x shares an "AEU" skill that converts Claude MP4 outputs into editable AE files (link in their video description; not verified here). [100x]
**Safe-use rules:** work on a duplicate `.aep`, enable undo groups, have Claude render a frame (`see-frame`) after each step, and never run downloaded `.jsx` without reading it.

**Prompt to learn a complex animation:**
```
In After Effects, build <describe effect, e.g. "a liquid-mask text reveal with a trailing glow"> as a fully
editable comp: named layers, nulls for control, expressions commented. After each step render a frame with
see-frame and check it. Then write me a numbered explanation of every layer, keyframe and expression so I can
rebuild it by hand.
```

## 8. Claude inside Premiere Pro (MCP)
- **`leancoderkavy/premiere-pro-mcp`** installs as a Claude Code plugin: `/plugin marketplace add leancoderkavy/premiere-pro-mcp` → `/plugin install premiere-pro@premiere-pro-mcp` → `npx -y premiere-pro-mcp@1.24.1 --install-cep`. It covers timeline insert and overwrite, ripple, roll, slide and slip, and split and trim. Note: Premiere's APIs can't set clip speed, and some 26.3 builds silently ignore QE edits, which the tools verify.
- **`quadlzzz/premiere-mcp`** does transcript-driven editing: "take out filler words and long pauses", `ppro_apply_cutlist` (a 30 s cut assembled from named soundbites in about 25 s), `ppro_find_phrase`, and frame grabs to verify. It **works on a duplicate sequence and snapshots the `.prproj`**. `claude mcp add premiere -- node "$(pwd)/mcp/server.js"`
- **`compimprove/adobe-premiere-mcp`** has 284 tools (CEP), `--doctor`, and a UXP helper for reading Premiere Speech-to-Text.
- **`mhadifilms/prpr`** is a Python CLI and MCP over UXP (`pip install prpr`, `prpr plugin install`, `prpr mcp install-claude`).
- **`CaYatur/PremiereProMCP`** is UXP-first and Windows Setup.bat based, handling titles, audio mix, grade and export.
- 100x simply asked Claude Code to "create a custom MCP that connects Claude Code to my Premiere Pro", then drove it: new project, import, captions, levels. [100x]
**Use Premiere MCP for** assembling a rough cut from a transcript, filler removal, B-roll on upper tracks and caption tracks. Keep creative graphics in code or AE.

## 9. Higgsfield inside Claude
- **Connector:** Claude Settings → Connectors → Add custom connector → `https://mcp.higgsfield.ai/mcp` (paid plan, no API key). Claude Code uses the Higgsfield CLI or skills. [HF-Help]
- **Katana (`/katana`)** recreates a reference edit (shot order, pacing, cuts on music, typography) with up to 5 photos of your characters or products, and only affected shots are regenerated on correction. Use only references you own or have rights to, including the music. Instagram and TikTok profile links aren't accepted, so upload the file. [HF-Katana-blog]
- **Blender Bridge** `bridge.higgsfield.ai/mcp` gives scene blocking → Seedance (credit-saving.md). [HF-Blender]
- Presets worth knowing (from the MCP page): Genjutsu (remake a reference with your characters, keeping the motion), `/ugc-flow`, `/marketing-adapt-video` (Ad Recreator), `/marketing-hook-variants` (Hook Multiplier), `/vox-mixed-media`, and the stickman explainer. [HF-MCP-page]

## 10. Setup checklist for Klaus (one-time)
```
Container (this repo):  ffmpeg, python3 + faster-whisper, Node 22 + npx hyperframes (or Remotion), scripts/qc_frames.py
Klaus's Mac/PC:         Claude Code/Desktop; Higgsfield connector; Higgsfield Blender add-on + Bridge (optional);
                        AE MCP (a-y-ibrahim or 23d1) with scripting permission on; Premiere MCP (quadlzzz for transcript cuts)
Skills to add:          remotion-dev/skills or heygen-com/hyperframes; studio sound-design rules (§5) as a skill file
House style:            build per-creator style index (§3) into Supabase style_cards; every Klaus note -> /learn
```
