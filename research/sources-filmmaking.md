# Sources: AI filmmaking, documentary and realism research (fetched 2026-10-21)

Transcripts came from the vidIQ transcript tool (10 calls, 50 credits). Titles and creators came from YouTube oEmbed. These notes summarise the sources as data. The distilled guides are:
`.claude/skills/higgsfield-creative-director/references/documentary-3d.md`, `filmmaking-longform.md`, `realism.md`.

---

## 1. [Best practices overview] Yf7T1VA83Gk
**"GRATIS! Crea Documentales Largos de 20 Minutos con IA (Tutorial paso a paso)"** by David AI. Fetched: yes (Spanish transcript).
Note: despite the "best practices overview" label, this is a free AI **documentary** walkthrough.
- A master prompt in ChatGPT/Claude drives the whole flow: topic ideas → duration + aspect → audience → language → tone → summary/premise/research → script → image prompts → video prompts → narration, advancing with "next".
- 2-minute doc = 12 image prompts + 12 video prompts + one narration block.
- Images: Google Flow with Nano Banana 2 Lite. Batch all 12 through Flow's agent with a "generate the following images" instruction; outputs are numbered.
- Video: Veo 3.1 Lite (or Gemini Omni Flash) in Flow. Use the image as **start frame** if it's strong, or as an **ingredient** if the prompt should dominate.
- Free tier is about 50 credits/day, so one video at a time. Download at 720p.
- VO: Gemini TTS (narration style, no expressions for a serious doc) or ElevenLabs v4. About 1:40 of VO for a 2:00 film.
- Each video prompt carries its narration line, which makes VO-to-picture sync trivial in the edit. Add transitions and a music bed last.

## 2. [3D documentary tutorial] DrsvFcPg8jY
**"How to Make 3D Documentary Videos with AI"** by Creating with Conor. Fetched: yes.
- Story brainstormed with Claude (bank vault opened overnight, nothing forced, 1 of 400 boxes emptied). All visuals made in Higgsfield.
- Stills on GPT Image 2, 16:9, quality high, **4K**, because everything later is built from these images.
- **Style key first**: a plain 3D mannequin 3-panel sheet (front/back/face) defines surface, geometry, proportions and lighting. Each character = the same paragraph + one rewritten "who" line.
- Locations: the same settings, plus an identical grade block in every prompt (steel blue + warm amber motivated accent). Vary camera height and lens per location.
- Composites: 2 refs (empty plate + character sheet). The prompt says copy the plate exactly, then insert the character. **Light the character with the room's own sources.**
- Video: Seedance 2.5, 16:9, start-frame pinned plus the next location as a second ref so the clip can cut into it. Clips run 8-17 s, about 1 minute total.
- Video prompts are written as **labelled blocks**, with STYLE and GRADE locked across generations. Seedance invents angles while holding the look.
- VO: ElevenLabs v3 ("Alistair"), one file per clip, sized to each clip's word budget. Edit in CapCut: VO under each clip, SFX, one ducked music bed.
- Upscale the edit to 4K with Topaz in Higgsfield, since Seedance caps at 1080p.

## 3. [3D doc resource page] creating-with-conor.kit.com/ea56987c72
**"Grab 3D Documentary prompt Pack"**. Fetched: yes, but **content is email-gated**. The page is only a Kit opt-in form ("Create a complete 3D documentary with AI, from the first character sheet and location to the final narrated 4K edit"). The prompts themselves could not be retrieved without submitting an email, which was not done. The workflow was reconstructed from the video instead.

## 4. [Free documentary guide] Uofgx-ugrXc
**"Create UNLIMITED 3D Documentary with AI | 100% FREE Forever"** by Cash-Coach. Fetched: yes.
- Niche proof: a 3D-mannequin true-crime channel at about 400k subscribers; the creator estimates RPM at $10 or more (US/UK/CA). Unverified.
- Chatbot choice: ChatGPT / DeepSeek (free) / Grok / Qwen. Master prompt + a 45-page "model PDF" (branding, transcript style, thumbnail layout) is absorbed first.
- **Anti-demonetisation**: never paraphrase another creator's script. Use their *style* to generate brand-new topics.
- VO: ElevenLabs v3 with emotion tags like `[whisper]`. Free alternatives: Noise AI, DubDub, Clipchamp TTS (unlimited).
- Images tested on Meta AI (best for this look, no watermark), TikTok Symphony (action-figure look), Google Flow / Nano Banana 2.
- A **visual flow** (your own scene sequence) beats letting the AI design one. The chatbot splits the story into chapters sized to the model's 8-15 s cap.
- Video tested on Higgsfield Seedance 2.0 (best: multi-shot plus consistency from 2 refs), Flow ingredients (Veo 3.1 Lite, 10 credits each; got day/night wrong), Google Vids, Gemini, DGEN, Meta (no multi-shot).
- Music: Pixabay or Mixkit, avoiding tracks with Content ID. Suno is optional. CapCut: VO first, gaps for suspense, VO at about +7 dB, date cards.
- Label every clip. Mix in news/blog screenshots as montage. The chatbot also makes 5 thumbnail prompts, channel names, description and logo prompt. Canva banner within the YouTube safe zone.

## 5. [AI filmmaking guide] kFKpcCHkuPI
**"How To Prompt Like a Director Using Opus 5.5 + Seedance 2.5 (Full Workflow)"** by Higgsfield AI. Fetched: yes.
- Cinema Studio project with folders and subfolders per asset, set up before generating anything.
- Characters: Claude writes the sheet prompt. **Soul Cinema** for exploration (8 images for 1 credit). Sheet = face close-up + neck-down front/back outfit panels so there is only one face. **Plain grey background.**
- Seedream 5 Pro edits fix skin that is too smooth and harsh light, and declutter location plates (shrink the foreground cabinet, clear the table) while keeping light and texture.
- Locations: use image refs to lock lighting and layout. Always use a **3/4 angle** for depth. Bake food and props into the plate per seat. Generate extras as one group reference.
- A Claude "director skill" turns the scene into shots with dialogue timing and camera moves. Refs are labelled with the same names used in the prompt.
- Failures fixed by explicitness: assign seats, anchor each seat to a background landmark, add a wide master shot first; describe exactly what a **reverse angle** sees.
- A colour-coded **blocking map** (top-down, colour = character) fixed a phantom fourth seat.
- Transitions: match cut on a phone tap with identical framing and move; hide the cut behind a character's back; **audio-first** transition (new ambience before the reveal).
- 30 s, 3-location ad cost about 2,100 credits including retries. Use the best moments from multiple takes.

## 6. [AI filmmaking guide] e9ZupmL9BcM
**"Master AI Filmmaking in 30 Minutes - Advanced AI Video Course"** by Dan Kieft. Fetched: yes.
- Pre-production = characters, locations, objects. Use real photos of yourself when possible.
- **Grey-background sheets** (white overexposes; tip credited to "Joey"). **Three refs per character**: sheet, identity close-up, detail/skin sheet. GPT Image 2 high at 2K-4K over Nano Banana Pro.
- Missing object refs make props vanish (the TV disappeared). Add a reference for every object that must persist.
- A filmmaking MD file in Claude generates sheets, shot lists and prompts. Write the **shot list first**; his 1-minute plan grew to 3 minutes without one.
- Prompt formats: simple (camera + subject + action + refs), timeline (setting block + shots; "24 fps" reduced lag), and **Chinese timeline with an English mirror** for Seedance.
- Give Seedance lots of context. "Shot 1/2/3" can replace exact timestamps.
- **Draft at 480p** (about 840 vs 4,800 credits at 1080p).
- Continuity: screenshot previous frames plus props as refs for the next angle; edit the start frame to add missing details.
- Voice: video-to-video keeps your real voice; an audio-file ref makes the character say exact lines; describe voices in every prompt (Gemini can describe a voice from audio). Use one good mic consistently.
- Motion transfer: "have image 1 play the performance and dialogue of video 1", plus background motion so it doesn't go stiff. Phone UI shots are filmed for real, then the background is replaced. Relighting via OpenArt VFX.

## 7. [Long video / movie] 8qfonxqvoSQ
**"HIGGSFIELD AI TUTORIAL | CINEMATIC AI VIDEOS WITH LARRY ULRICH"** by Larry Ulrich. Fetched: yes.
- Workflow: ChatGPT writes image and action prompts → Nano Banana Pro stills (unlimited on his plan) → Kling 3.0 in Higgsfield at 1080p, 10 s → Final Cut Pro.
- Always reference both the scene image **and a close-up** of the lead, because models drift the face.
- Credit plans generate in about 1 minute; "unlimited" queues (Runway) can take about 10 minutes. He uses unlimited for retries to save credits.
- Ask the LLM to keep prompts **2,500 characters or fewer** (the platform cap; he hit it by 5 characters).
- Dialogue: `says: "<line>"` in quotes, followed by the tone.
- **Don't start on the back of a head.** Have him face forward, turn away, turn back, so the face is retained.
- Eye line kept drifting up (reads as submissive, 80 wasted credits). Front-load "eye line stays straight ahead" and repeat it.
- Mentioning off-camera agents pulled them into the frame. Remove every reference to unseen people.
- Edit craft: trim clips hard, speed up about 3%, hold reveals, reuse "dead" pre-line footage as listening cutaways, imply exits with footsteps SFX.
- Learn a list of 30-50 camera moves. Static shots kill story.

## 8. [Emotional control] AgLijG7t1QU
**"Make AI copy emotions from any scene (open source workflow)"** by Sirio. Fetched: yes.
- The problem: prompted emotion looks mannequin-like or overacted, and uploading an actor's clip gets flagged.
- The fix: split **movement** from **identity**. Build a grey clay/matte-cap 3D face mask that moves like the source, and give Seedance 2.5 the mask plus your photo/video.
- Pipeline: MediaPipe landmarks + SPECTRE (expression/jaw/pose) + FLAME 3D face + lip/eyelid outlines + grayscale light/shadow overlay (keeps muscle creases, drops colour identity) + synthetic lighting. Runs on CPU (M3 Mac). Free on GitHub.
- About 10 versions, about 3 hours, about $5; drafts at 480p.
- Two prompt modes: "copy the movement from the mask", or mask + written lines/timing/feelings. Have the agent describe eyes, brows and mouth **per second**.
- Rule: emotion missing from the mask → fix the mask; in the mask but not on the face → fix the prompt.
- Limits: the mask freezes when the actor turns away; keep other speakers' lines out of the prompt.
- **Licence**: FLAME and SPECTRE are non-commercial, so the workflow can't be sold or used commercially as is. Altering footage doesn't grant rights to it.

## 9. [Realistic video] 2hJsvDSPWYM
**"How I Make Realistic AI Videos with Seedance 2.5 - Full Guide"** by Dan Kieft. Fetched: yes.
- Image model choice "depends". Run the same prompt across about 6 models, since stills are cheap. GPT Image 2.5 Flare, Flux 2.0 Pro, Nano Banana Pro/2.1, Seedream 5.0 and Soul 2 all win sometimes. Flux 3 looked plastic.
- Video: Seedance 2.5 is best for realism. Flux 3 gets about 80-90% for much less. MiniMax H3 Max is weak without refs. The 480p draft can look *more* real.
- **CTLT prompt formula**: Camera, Tone, Lighting, Texture, plus subject/action/place. An LLM template fleshes out spoken ideas.
- Capture-style presets: skate cam, intimate doc, motion-blur photo dump, low curbside, disposable camera, concealed observation, phone snapshot, camcorder, iPhone selfie. Deliberately low resolution for low-fi looks.
- Turn a winning prompt + image into a reusable style `.md` skill.
- **Contrast levels** for scroll-stopping ideas: L0 none → L1 unexpected situation → L2 + unexpected styling → L3 + feeling.
- Human-camera moves: handheld, crash zoom, voyeuristic, whip pan, walking backwards, frame-blocking passer-by, exposure adjustment, focus hunting. Combine them.

## 10. [Realistic guide] w0R29uK3Hfk
**"How I Get Perfect AI Realism on the First Try in 2026"** by kaye.creatives. Fetched: yes.
- **"Lazy prompting"**: one massive Claude brief (story, 4 characters, locations, props, camera structure, VO script, plus Pinterest refs) returns every prompt in about 40 s.
- Cinema Studio project folder first.
- Spend 99% of effort perfecting **stills**; good stills mean the video doesn't glitch.
- Models as paintbrushes: Seedream 5.0 Pro for ultra-real humans and LEGO/plastic props; Soul Cinema for locations (fast, cheap). 16:9, 2K standard.
- Reuse 3 scene structures across 4 characters (ECU + slow dolly-out; full-body static wide with prop; macro on prop) and swap only the inputs.
- **480p draft → verify → 1080p first try** = zero wasted credits.
- Twist ending: Claude converts the human sheets to LEGO minifigure sheets that keep clothes, hair and accessories.
- VO: ElevenLabs v3 in Higgsfield (Arthur voice), **Creative delivery mode** for emotion and pauses, batch 4. Cut to the VO beat in Premiere/CapCut.

## 11. [Tools to equip Claude/ChatGPT] 3YkMI7z_CWI
**"AI Filmmaking got 10x easier with Fable 5 - I Built 3 Free Tools"** by Dan Kieft. Fetched: yes.
- Vibe-code tools for repeated steps. Meta-prompt with 3 answers (what to build, why, which features), have Claude write the build prompt, revise it, then build in Claude Code (Opus 5 is cheaper than Fable 5).
- **AI World Builder**: story wizard (idea → genre → hero → cast → antagonist → world with colour refs → acts) → script PDF → character sheets (GPT Image 2 via Higgsfield MCP; outfit-specific sheets suggested from the story) → locations (Soul 2 for about 1.5 credits each, "full coverage" angle batches, "surprise me", "detailed" switches to GPT Image 2). Uses your own Higgsfield + Claude API key.
- **AI Camera Control** (aicameracontrol.com): free 3D room with movable camera, shot-type presets, bird's-eye blocking, pose presets → prompt + pose reference image to use with character sheets in GPT Image 2.
- **AI Camera Movements** (aicameramovements.com): cheat sheet of camera-move prompts; builds a custom prompt from subject, location, action and mood.
- MCP-driven batch generation is faster but burns credits faster. Make sure the master reference image is good first.

---

## Supplementary web sources (gap-filling searches)
- **Seedance 2.5 Prompting Guide (official docs)**: docs.seedance.tv/en/seedance-2-5-prompting-guide
  - 4-part prompt: asset mapping → one-sentence brief → timeline/shot order → global constraints.
  - Up to 30 images / 10 videos / 10 audio clips (30 s total each); 1-8 subjects most reliable.
  - Whole-second continuous time ranges, with content density matched to duration.
  - Describe uncommon camera terms by what the viewer sees. Emotion as visible changes ("eyes redden, corners of the mouth lower, breathing quickens").
  - Blockouts: strip motion paths and axes. Separate keyframes align more strictly than storyboard grids.
- **fal "How to use Seedance 2.5"**: fal.ai/learn/devs/how-to-use-seedance-2-5. Formula Subject + Action + Scene + Style + Camera + Audio; `@Image1 defines…; do not use the image background` role template; multi-view = same object stated explicitly.
- **Runware Seedance 2.5 multi-reference**: runware.ai/docs/models/bytedance-seedance-2-5/guides/multi-reference-production. Role binding; lowest index holds identity best; never address unpassed slots; preservation clause; clean isolated refs; iterate a hero still, then animate.
- **Kling 3.0 official user guide + Multi-Shot guide**: kling.ai/quickstart/klingai-video-3-model-user-guide, kling.ai/blog/kling-video-3-multi-shot-guide. Multi-Shot vs Custom Multi-Shot (per-shot duration, framing, action, dialogue, move); element binding including voice; tie dialogue to the named speaker.
- **fal Kling 3.0 prompting guide**: blog.fal.ai/kling-3-0-prompting-guide. Up to 6 shots; anchor subjects early with identical wording; explicit motion over time.
- **Shotcraft defects reference**: shotcraft.video/reference/video-defects/. Unnamed camera = drift; camera-only motion = slideshow; one move per shot; define the end state.
- **Versely "Grain, flare and vignette against the AI sheen"**: real footage = errors; finishing order clean → upscale → grade → texture last; consistent texture across cuts.
- **media.io "How to make AI video look real"**: realism hierarchy; fake-signal table (morphing, floaty motion, plastic surfaces, impossible camera, audio mismatch).
- **WonderLens "Visual realism"**: too much perfection is the top failure; prompt specific hardware imperfections.

## Not fetched / limitations
- Conor's prompt pack (kit.com page) is email-gated, so the exact prompts weren't retrieved.
- Firecrawl was not used (out of credits). No other paid vidIQ tools were used.
- Model names and versions are quoted as spoken in the videos (for example "Cream 5 Pro" = Seedream 5.0 Pro, "Cedance/Seance" = Seedance, "deep fake field" = Higgsfield in the auto-captions).
