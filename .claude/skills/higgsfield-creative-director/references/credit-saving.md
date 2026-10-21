# Credit-saving playbook (Higgsfield + Claude tokens + local render time)

Studio law still applies first: approved `spec.json` + `get_cost` quote, then a **draft at the LOWEST quality/resolution the model offers**, then QC and Klaus's approval, and only then a re-render at the HIGHEST quality, 1080p, followed by a 4K upscale of the locked final. Everything below is about spending fewer credits *inside* that loop.
Source tags such as [HF-Blender] are explained in `research/sources-editing.md`.

## 0. The one rule behind most savings
**Lock structure for free, then pay only for pixels.** Camera, timing, staging, cuts and design should all be decided in cheap media (stills, gray-box 3D, code animation, text plans) before any video credit is spent. [HF-Blender] [Kieft] [Duncan] [100x]

## 1. Ladder of cost: climb it in order
| Step | Medium | Cost | What gets locked here |
|---|---|---|---|
| 1 | Text: beat map / shot list / storyboard plan | Claude tokens only | Story, lines, who does what, shot count |
| 2 | Stills (Nano Banana / GPT Image 2.5), 1K or 2K draft quality | Low | Character look, set, composition, key poses ("images are cheap, video is expensive", so iterate here) [Kieft] |
| 3 | Gray-box blocking in Blender (Higgsfield Bridge) or 3D Jutsu → playblast MP4 | ~0 credits (local render) | Camera path, lens, timing, blocking, eyelines, 180° rule [HF-Blender] |
| 4 | Code motion (Claude Motion / Remotion / HyperFrames) for graphics, text and UI | Tokens + local CPU | All graphics, so only the *footage* gets generated [HF-Motion] [Joseph-YT] |
| 5 | Video **draft** (Seedance 2.5 `draft:true` 480p; Kling `std`; Cinema Studio 480p) | Medium | Motion and performance |
| 6 | Final at 1080p, highest quality, **only the PASS shots** | High | - |
| 7 | 4K upscale of the locked, trimmed edit | High | - |

## 2. Tactics, with sources

### Pre-vis / blocking (largest saving on camera-heavy shots)
- **Gray-box the shot in Blender before you generate it.** Connect the Higgsfield Bridge (`bridge.higgsfield.ai/mcp`) as a connector, install the Higgsfield Blender add-on, and ask Claude to "build a corridor, one figure walking, camera following behind". Iterate the camera in Blender ("add texture to walls, vary framings, animate the lens"). Then Output Properties → 1920x1080, 24 fps, MPEG-4 → View → Viewport Render → playblast. [HF-Blender]
- **Get Claude to write the prompt from the playblast:** "Write a 30-second Seedance prompt from this blocking video. Read the input video and write the prompt second by second to match the camera moves in the clip." Set the generation duration to the blocking length. [HF-Blender]
- The presenter reports burning **~5,000 credits** on a 6-person dialogue scene with raw prompts and never getting a usable take (seats swapped, 180° rule broken). With blocking it worked in about 3 iterations. [HF-Blender]
- **Give Claude a real shot list, not "cinematic camera":** rails, targets, number of cuts, then "add subtle handheld sway". [HF-Blender]
- **The gray box carries camera and timing; reference images carry the look.** Attach the blocking render, the character sheet and the asset refs together. [HF-Blender]
- **Leave what AI does well blank in the blockout** (liquid, smoke, splashes). Block only the geometry that needs to land on cue. [HF-Blender]
- **Make client and Klaus revisions in the blockout, not in regenerations.** "The opening is boring / show the flavours / where's the logo" means re-cutting the Blender timeline (free) and generating once. [HF-Blender]
- **One blocking file can carry many looks.** Every prompt has two halves: the structural layer (the reference video: cuts, camera, timing, which never changes) and the style layer (2.5D, 2D ink, 3D toy box, photoreal). You can pitch three worlds in a day on the same approved edit. [HF-Blender]
- No Blender? Use **3D Jutsu** (browser-based blocking and previz in Higgsfield) via `get_preset_instructions {preset:"/3d-jutsu"}`. [HF-3DJutsu]
- In the Blender add-on the **cost is shown on the Generate button** before you press it. Treat it like `get_cost`. [HF-Blender-blog]

### Stills-first storyboarding
- Build **character sheets** (multi-angle, close-ups) first, then generate every storyboard frame from the sheet. Lay the frames out in order (Figma or a contact sheet) before animating. [Kieft]
- **Use start and end frames rather than letting the model guess.** Edit the still (e.g. "remove the man, close the door") to make the start frame and use the original as the end frame, then run Kling 3.0 start/end frame. You get fewer re-rolls. [Kieft]
- **Scene continuation:** the last frame of clip A becomes the start frame of clip B, which gives one seamless "take" without generating a 15 s monster. Grab it locally:
  `ffmpeg -sseof -0.1 -i clipA.mp4 -frames:v 1 -update 1 clipA_last.png` [Kieft]
- **Multi-shot angles from one image** (Higgsfield "open in multishot") give alternate angles without hand-writing camera prompts. Upscale only the ones you keep. [Kieft]
- **Kling 3.0 Omni multi-shot:** several camera angles in one 9 s generation from elements and character sheets is cheaper than three separate generations, though you get slightly less control per shot. [Kieft]

### Hybrid edits: generate only footage
- **Do text, UI, charts, maps and logos in code** (Claude Motion / Remotion / HyperFrames) and generate only the shots that need real footage or characters. When a fix is needed, **regenerate only that shot** instead of the whole video. [HF-Motion]
- **Katana corrections regenerate only the affected shots.** A cost card is shown before each generation. Keep iterating in the same chat so each version starts from the last one. [HF-Katana-blog]
- **Make design mock-ups as images first, then animate only the approved designs.** A whole 60 s Vox-style piece cost about $20 of Higgsfield credits including tests. [Joseph-Vox]

### Draft discipline (matches studio rules)
- Seedance 2.5: `draft:true` (480p) → QC → finalize with `draft_job_id`. Kling: `std` for drafts, `pro`/`4k` only for finals. Use the lowest image `quality` for storyboard stills. (model-routing.md)
- **Duration:** generate the shortest duration that covers the beat plus about 0.5 s of handle, and trim the rest in ffmpeg. Exception: spoken lines need 3 s or more on Kling (model-routing.md).
- **Trim before you upscale.** Never upscale handles you will cut:
  `ffmpeg -ss 2.40 -to 7.90 -i shot.mp4 -c:v libx264 -crf 14 -preset slow -c:a copy shot_trim.mp4`
- **Fix one thing with an edit model** (`kling_video_edit`, `seedance_2_5 mode:video_edit`) instead of a full regen.
- **Batch size 1 for video.** Only batch stills.
- **Fix voices in post, not by re-rolling.** Each AI clip gives a slightly different voice, so run them all through one voice (`voice_change` in Higgsfield or ElevenLabs voice changer) instead of regenerating for a better voice. [Kieft]
- **Small lip-sync drift is an edit fix, not a regen:** nudge the audio about 2-4 frames earlier. [Kieft]
  `ffmpeg -i clip.mp4 -itsoffset -0.08 -i clip.mp4 -map 0:v -map 1:a -c copy clip_sync.mp4`

### Claude token and local-render savings
- **One job at a time with checkpoints:** style understanding → 3 static test stills → 1 animation test → storyboard → full build. Feedback before the token-heavy build saves the most. [100x]
- **Feed Claude 1-2 minute chunks**, not whole long videos. [100x]
- **Plan before you build:** a graphic plan mapped to the beat map is cheap to change, and a finished graphic isn't. [Duncan]
- **Use Opus for planning and directing and Sonnet sub-agents for building.** Duncan's edit used ~1.4B tokens: ~500M Opus and ~900M Sonnet. [Duncan]
- **Index your references.** Don't load 458 reference animations (4.5M tokens). Build an index and load only the refs each scene needs (<100K tokens). [Joseph-YT]
- **Send a design sheet (screenshots) before any export.** Exporting is the expensive step. [Joseph-YT]
- **Local render speed:** queue renders one at a time (parallel renders crashed each other), turn off motion blur (≈3x faster), and render review drafts at half size, full size only after approval. Run long renders overnight. [Duncan]

## 3. Pre-spend checklist (paste into the job log)
```
[ ] spec.json approved:true            [ ] get_cost quote shown to Klaus
[ ] Stills / character sheets approved (Gate 4)
[ ] Camera locked (blocking playblast or start/end frames) for any moving-camera or multi-person shot
[ ] Graphics/text/UI moved to code, not generation
[ ] Draft settings: lowest res/quality, batch 1, shortest duration that covers the beat
[ ] After draft QC: re-render ONLY PASS shots at 1080p highest quality; trim; then 4K upscale
```
