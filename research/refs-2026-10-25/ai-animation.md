# AI animation and narration styles Klaus likes (refs anim1-anim3, 2026-10-25)

Klaus: "ai animation and narration styles I like". This file adds to animation-3d-cartoon.md (3D feature look, character sheets, Kling start/end frames, voice consistency), documentary-3d.md (mannequin style key, words-per-clip budget), motion-design.md (Claude Motion / Remotion / HyperFrames table, kinetic-type rules, Vox method) and genre-playbooks.md §19 (Pixar → pace as comedy/feel-good) and §21 (explainer / myth-buster). It does not repeat them. It covers three formats those guides don't have yet:

1. **anim1: absurd "how to cook" survival recipe** (narrated, photoreal-3D character on a blank grid void).
2. **anim2: code-made motion graphics + screen tutorial** (Claude writes the animation as code).
3. **anim3: side-by-side stick-figure progression loop** (no narration, counters + one changing variable).

Method: analysis packs (meta.json, transcript.txt, sheet.jpg, hook.jpg) plus close-up frames pulled with ffmpeg into the agentC scratchpad. Measurements come from the packs (cut detection, words/min, LUFS) plus my own sentence counts and frame reads. Anything marked **[inferred]** is a guess from the frames, not something the creator stated.

---

## anim1: @storygoaten "How to Cook a Carnotaurus Leg" (140K likes, 1,773 comments, 38.7 s, 9:16)

### Format concept (why it hooks)
- **The first frame is already absurd mid-action.** An old caveman is sawing a cleaver into the thigh of a whole dinosaur lying on the floor. There is no intro and no title card. The caption "How to Cook a Carnotaurus Leg 😳" is the whole premise.
- **It borrows a familiar format.** It's a recipe or cooking-tutorial voice ("First…, then…, pack…, splash…") applied to an impossible ingredient. The familiar grammar makes the absurd thing easy to follow. Viewers stay to see the process finish (salt-crust roasting is satisfying ASMR-style process content), not for a joke.
- **It opens a loop in sentence 2.** "This is our **last** recipe, so it needs a lot more rock salt than ever." It sounds like a cooking aside, but it plants the ending.
- **The twist ending has no words.** He bites the leg ("final salted meat"), a T-rex rises behind him, and the last frame is a tombstone reading **"CAVEMAN 1 RIP"**. "Last recipe" pays off and the "1" implies a franchise (Caveman 2). That's why there are so many comments: people theorise, mourn and ask for part 2.
- **Series branding is baked into the character.** "STORYGOAT" is tattooed across his chest, so the watermark survives reposts.

### Narration voice and script structure
- **Transcript (8 sentences, 138 words, 38.7 s):**
  1. Step + contrarian warning: "First, cut off the whole leg, **but don't just** throw it into a bowl of hot water."
  2. Open loop: "This is our last recipe, so it needs a lot more rock salt than ever."
  3. "Instead," the correct method: "spread a thick bed of rock salt onto a flat stone and place the whole leg right on top."
  4-7. Process verbs, one step per sentence: "Then, keep pouring…", "Pack the salt tightly…", "Splash a little water… hardens into a solid crust", "Then, roast… until the meat cooks inside its salt shell."
  8. Sensory payoff: "When the crust turns dry and solid, crack it open, pull out the hot leg, and **bite straight into** the final salted meat."
  - Then about 3 s of picture with no words: the T-rex, then the tombstone.
- **Measured:** **214 wpm** (fast); mean sentence **17.3 words** (max 24); a new imperative verb roughly every 2 s; no pauses (no silence over 0.4 s below -40 dB in the whole clip).
- **Persona:** a calm, flat, confident instructor. It is a TTS-like read with no jokes in the voice. The narrator never acknowledges that it's insane, and that deadpan is the comedy. It is second person ("you"), with "our" used once.
- **Captions:** **one word at a time**, white heavy sans in caps with a soft dark shadow, centred at about 78% of frame height. Each word appears on the spoken word.

### Visual style
- **Render look:** photoreal-leaning 3D, like a high-end game cinematic or an AI still. The character is a wiry elderly caveman with a long white beard, fur loincloth, visible veins and a chest tattoo. The dinosaur, salt, coals and stone slab have tactile macro detail.
- **Set:** a **"3D viewport void"**: an infinite saturated cobalt-blue floor (≈ #1F6FE6) with a thin white grid, fading to a lighter blue horizon. There are no walls and no props except the recipe items. **This is the consistency trick:** with no environment there is nothing to drift between clips, and the grid gives scale and a "simulation / tutorial" feel.
- **Camera:** mostly one **high 3/4 overhead angle** (~40-50° down, like a cooking top-shot), locked or with a slow push. There are 3-4 close inserts (salt pouring from cupped hands, hands packing the crust, the bite) and one low hero angle (the T-rex reveal).
- **Shot lengths (measured from 16 cuts):** 2.33 / 2.17 / 1.47 / 2.16 / 3.04 / 2.13 / 2.33 / 2.30 / 2.07 / 2.03 / 1.60 / 2.57 / 4.37 / 2.30 / 2.00 / 3.53 s. **Median 2.17 s**, which is about one shot per sentence-half. The longest shot (4.4 s) is the roast, when the steam rises.
- **Continuity:** the state carries across cuts (the salt bed persists, then the crust, then the cracked shell). Each shot equals one recipe step.
- **Palette:** cobalt blue + bone white (salt) + warm meat browns + ember orange (coals). Food reads warm against the cold background.

### How it was likely made [inferred]
1. Lock the character with one reference image (a Nano Banana / GPT Image / Midjourney-style still), then generate a **keyframe still per step** with that reference and the same "blue grid void" sentence.
2. Image-to-video each still for 5 s (Kling or Seedance class, judging by the micro-motion and steam). Each clip is trimmed to ~2 s on the best motion.
3. A TTS narrator (ElevenLabs-class) at high speed, with the script written to fit about 2.2 s per step.
4. Auto one-word captions (CapCut-style) and a quiet bed or foley. Loudness is -14.5 LUFS integrated with peaks near 0 dBFS, which suggests a social-normalised export.

### Sound
VO-first with an unbroken audio bed (silencedetect found no gaps). Foley sells the process: salt crunch, sizzle, crust crack. **[inferred]** The ending is a stomp/roar for the T-rex. For our version: VO at -14 LUFS, foley at stim density "story" (structural beats only), and one impact on the tombstone.

### Recipe for our stack
**Style key (paste LAST in every Higgsfield prompt):**
```
STYLE KEY: hyper-detailed 3D character render on an infinite saturated cobalt-blue studio floor with a thin white
perspective grid fading to a pale-blue horizon, no walls, no other props, soft overhead key light with gentle
contact shadows, tactile macro textures (skin, salt, stone, fur), warm food tones against the cold blue, clean
tutorial staging, same character design and outfit in every shot, no text in frame
```
**Shot JSONs** (shots[] in spec.json; Nano Banana Pro still → Seedance 2.5 omni_reference, 5 s draft at 480p, trimmed to 2-2.5 s):
```json
{"id":"S01","dur":2.3,"camera":"high three-quarter overhead, 35mm, locked, slight push-in","action":"start: @CAVEMAN braces one bare foot on the mammoth tusk's base -> end: he heaves the tusk free and it thuds onto the grid floor","light":"soft overhead key, contact shadow under tusk, cold blue bounce"}
```
```json
{"id":"S06","dur":2.0,"camera":"macro insert, 85mm, top-down, locked","action":"start: @CAVEMAN's cupped hands full of rock salt -> end: salt pours through his fingers onto the stone slab, grains bouncing","light":"hard overhead key catching each salt crystal, blue grid floor visible at frame edges"}
```
**Narration / VO spec:**
- Persona: **Deadpan British** (voice-persona-audio.md) pushed to ~200 wpm, flat and certain, no laugh. Do not use the Posh Nature-Doc archetype here; that one is slow and reverent.
- Structure: "First, X, but don't just Y" → open-loop aside ("This is our last…") → "Instead," → one imperative step per 2-2.5 s → sensory verb payoff → wordless visual twist.
- Budget: **~7-8 words per shot** at ~3.4 words/s. A 35-40 s piece is ~130-140 words and 15-17 shots.
- Voice source: Higgsfield preset or ElevenLabs library voice, one voice ID per series (cast/registry.md). Never clone anyone.

**Edit spec (draft preset `absurd-howto-3d`, schema of tools/editor/presets/*.json):**
```json
{
  "name": "absurd-howto-3d",
  "label": "Absurd how-to / survival recipe (narrated 3D, one word per caption)",
  "kind": "genre",
  "description": "From ref anim1 (@storygoaten, 140K likes, measured 2026-10-25): deadpan imperative VO at ~210 wpm, one recipe step per 2-2.5 s shot on a blue-grid void, single-word centred captions, foley on every process verb, a wordless twist ending (callback to an open-loop line) and a series tombstone/end card.",
  "reference": "research/refs-2026-10-25/ai-animation.md#anim1",
  "pacing": {"remove_silence_over_s": 0.3, "pad_s": 0.05, "remove_fillers": "hard", "max_shot_s": 4.5},
  "captions": {"enabled": true, "size": 0.05, "max_words": 1, "animation": "pop", "uppercase": true, "keyword_caps": false, "outline": 0, "shadow": 3, "position_y": 0.78, "color": "#FFFFFF", "highlight": "#FFFFFF"},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.03, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0, "mode": "full"},
  "sfx": {"density_per_10s": 0.8, "db": -14, "map": {"hook": "impact", "title": "pop", "end": "impact"}},
  "music": {"energy": "low", "db": -24, "duck": true},
  "grade": {"contrast": 1.05, "saturation": 1.08, "warmth": 0.0},
  "end_card": {"enabled": false}
}
```
(Foley comes from the generated clips' own audio or a `/sound` cue sheet. The "end card" is the in-world tombstone or sign shot, not a brand card.)

**Example concepts using the format:**
- **Physio Spot (education, SG health pack): "How a caveman lifts a mammoth tusk (properly)."** Steps: "First, roll the tusk close to your shins, but don't just bend over and yank it." → "Instead, push your hips back like you're closing a cave door with your butt…" → brace, grip, push the floor away, stand tall, set it down the same way. Twist: the tusk is still attached to a living mammoth, which walks off carrying him. Wordless; the end card is "CAVEMAN 2: SHOULDER DAY". Compliance: it's a technique demo only, with no outcome claims ("never hurt again"), no testimonials, no "best clinic". Caption CTA: "Back feels off? Get it assessed: Physio Spot", with no free-consult inducement.
- **Power Protein: "Prehistoric protein shake."** A caveman cracks a giant egg, grinds roasted seeds, shakes it in a hollow gourd, and the twist is a pterodactyl stealing the gourd. Compliance: no "build muscle fast" or superlatives; the product only appears as the modern cut-in at the end.
- **Founder (TITAN.AI, personal account): "How to build a startup with stone tools."** Same deadpan steps: carve the logo into rock, hire a mammoth, pitch to a cave council. Twist: an asteroid ("Series A"). Klaus's voice persona stays out of it; it's the brand's deadpan narrator.

---

## anim2: @miftahul_islam_efaz "Opus 5.5 made these animations. Here's what I actually told it", Tutorial 2/3 (1,667 likes, **2,040 comments**, 143.6 s, 16:9)

### Format concept (why it hooks)
- **Comments outnumber likes (1.22 : 1).** That comes from the CTA "Comment SKILL for the file, comment TUTORIAL for part 3 in your DMs". It's a comment-keyword lead magnet (ManyChat-style auto-DM [inferred]), and the comment velocity drives reach. "Part 2 of 3" adds a series hook.
- **Contrast open:** "This is what AI motion usually looks like, and this is the same AI with the skill" over two monitors labelled **"AI SLOP"** vs **"VIRAL / HIGH QUALITY"**. Then a price hook: "Higgsfield-level motion without the Higgsfield price tag."
- **Proof in the middle:** a 15 s showreel at 62-76 s, cut at 0.03-0.13 s intervals. It's kinetic-type cards: "CAMERA. 0 cameras / 0 lights / 0 crew", "depth, drawn.", "nothing here was filmed.", "f(t) every pixel is a function of time", "ONE PROMPT.", "KEYFRAMES.", "MOTION", "NO". The claim gets proven visually before the how-to.

### Narration and script structure
- **Measured:** **120 wpm**, 287 words, mean sentence **7.6 words** (38 sentences), and 27 silences over 0.4 s (breathing room while the screen recordings play).
- **Structure:** series tag ("Part 2") → contrast claim → price hook → compatibility list ("Claude Code, Codex, Cursor, VS Code, Claude Desktop, even Google Antigravity. It runs almost anywhere you work.") → "Alright, now let's cook." (a chef mascot card) → objection-handling ("No, you don't need a paid subscription… here's the secret") → 3 steps (give Claude the skill → "Now watch." → showreel) → part-2 method (find inspiration → download the reference → "make my animation in this exact style… then tell it your topic. That's it.") → "Claude breaks the reference down, frame by frame." → keyword CTA.
- **Persona:** a casual peer-to-peer tutorial voice, slightly hyped ("here's the secret", "let's cook"), using short declaratives. **[inferred]** It's the creator's own voice or a clean TTS.
- **Caveat for us:** the tutorial tells viewers to download other creators' videos with "video downloader" sites and copy "the exact style, same effects, same motion, everything". For us, references are **study-only** (`editor.py study`, research/style-studies); we never cut them into edits or clone a specific creator's piece. Some of the free/paid model claims in the video may not hold; don't repeat them.

### Visual style
- **Mixed-media 16:9.** There's a **voxel/pixel-art 3D room** (a desk with two monitors, a chalkboard with app cards, a voxel host character with a fedora and coffee, and a voxel chef mascot over flames for "NOW LET'S COOK"). Then dark-UI **screen recordings of claude.ai** with kinetic captions laid over the empty right side ("It already knows the **PLAYBOOK.**", "DROP the file", "10 SECONDS.", "PLAN."). Then the showreel cards. Then a **painted anime-style landscape** used as a background plate for the part-2 steps ("Videos like mine?", "Inspiration.", "Same process. Every platform.", "Frame by frame.", "Your style. Understood.").
- **Type system:** a heavy grotesk in caps for punch words (CAMERA., ONE PROMPT.), an italic serif for poetic lines ("depth, drawn.", "nothing here was filmed."), and mono HUD micro-text (frame counters "0256 / 0458", coordinates "X 1544 Y 8446", "03 - TERRAIN") that sells a "motion-design engine" feel. Accents are mint (#5EEBC0-ish) on the title, orange-red (#F05A28-ish) for keywords, and cream/black.
- **Shot lengths (measured):** the 61 detected cuts are **clustered**. There are 6 at 0.5-1.1 s (a glitch intro), 9 at 21.3-21.6 s (the "let's cook" stutter), about 40 between 61.8 and 69 s (the showreel, 0.03-0.13 s apart) and 3 at 76.5 s. Everything else is long screen-recording segments of 3-20 s with smooth transitions the detector doesn't count. So the pack's "median 0.1 s" is misleading. The real rhythm is **long calm explanation, then a 15 s burst of proof, then calm again**.

### How it was likely made
- **The showreel cards [inferred, consistent with the caption]:** HTML/CSS/JS (GSAP, canvas or SVG) or React/Remotion generated by Claude from a "motion-video-director" skill (the skill name is visible in the claude.ai screenshot: "/motion-video-director … make me a motion graphics video … 15s landscape"), then rendered to MP4 in the browser or with a headless renderer. The HUD counters ("0256 / 0458") are frame counters, which is typical of a frame-stepped code renderer.
- **The voxel room [inferred]:** a voxel 3D scene (MagicaVoxel/Blender, or AI-generated voxel stills animated). The screen recordings are real captures. The anime landscape is an AI-generated plate. Assembly is in an NLE.

### How Claude-made code animation actually works
1. **A video is a function of time.** Claude writes a page (HTML/CSS/JS, SVG, canvas or three.js/WebGL) or a React component (Remotion) where **every visual property is computed from `t`** (seconds or frame number). No wall clock, no `Date.now()`, no free-running `requestAnimationFrame`, and randomness is seeded. A GSAP timeline is created **paused** and set with `tl.seek(t)`.
2. **A renderer steps time deterministically.** For frame i = 0…N, set `t = i / fps`, wait for layout and fonts, screenshot the viewport in headless Chromium, and pipe each PNG to ffmpeg (`-f image2pipe … -c:v libx264 -pix_fmt yuv420p`). Audio (VO, SFX, music) is muxed afterwards or by the editor. Because frames are captured, not recorded in real time, a slow frame can't drop. 60 fps or 4K just takes longer.
3. **Frameworks that package this:** Remotion (`npx remotion render`, React, licence check for company use), HyperFrames (HTML + GSAP, `npx hyperframes render`, Apache-2.0), and Claude Motion (artifact, MP4 export). These are already listed in motion-design.md §1. The "skill" in anim2 is a prompt/playbook file (plan → scene list → animate → sound) that makes the model use these patterns consistently.
4. **Why it beats AI video for this job:** exact text, exact numbers, brand fonts and hex colours, and infinite cheap revisions ("make the keyword orange, hold 0.2 s longer"). It costs 0 credits per render, has no hallucinated letters, and re-renders to every aspect ratio from one source. It is weak at people, organic motion and photoreal, so those stay in Higgsfield and get composited in.

**Verified here:** a 30-line seekable HTML scene plus a 15-line Node renderer (`playwright` from the global `/opt/node22/lib/node_modules`, Chromium, ffmpeg) rendered **120 frames at 1080×1920 in 17 s** (≈7 fps render speed). It's a stick-figure month counter with a glowing head (the anim3 mechanic). Files are in the agentC scratchpad, `poc/scene.html` and `poc/render.mjs`. Contract: the page exposes `window.seek(t)` and `window.DURATION`. The renderer loops seek → screenshot → ffmpeg pipe.

### What we would add to our pipeline (proposal; nothing in the repo was changed)
| Add | What | Why |
|---|---|---|
| `tools/motion/render.mjs` | The PoC renderer, hardened: args for size/fps/duration, `--draft` (half size, 15 fps), a `document.fonts.ready` wait, a `--frames` range for re-rendering one scene, and output to `projects/<p>/motion/<scene>.mp4` | It's a code-animation renderer that needs only what we already have (Node 22, global Playwright + Chromium, ffmpeg); no Remotion licence question |
| `tools/motion/templates/` | Seekable HTML scene templates matching our formats: kinetic-type card, HUD/counter card, split-compare (anim3), chat card, chart/stat card, title/series card. Each reads a JSON of strings/colours/timings | Claude edits JSON or one template instead of writing from zero; brand tokens come from `brands/<brand>.md` |
| A motion-director skill/playbook (`references/code-motion.md`) | plan (beat list per VO line) → design sheet (screenshot frame at each beat's mid-point → Klaus approves) → draft render → full render → hand to the editor | Same gates as Higgsfield work: a design sheet replaces Gate 4 for code-made graphics; drafts first |
| Editor hook | Code-rendered clips enter `edit.vN.json` as B-roll items (`mode: full`, `pip` or `split`), the same way `chatanim.py` cards do now; word timestamps from faster-whisper drive the `t` of each text card | Text lands on the spoken word (motion-design.md §3 rule) |
| QC | `scripts/qc_frames.py` at 10 fps on code renders (one-frame flashes, late text) | motion-design.md §8 |
| Optional | `pip install playwright` if we'd rather drive it from Python inside `titan_editor` (only the Node package is installed now) | One language inside the editor |

**Edit spec (draft preset `code-motion-tutorial`):**
```json
{
  "name": "code-motion-tutorial",
  "label": "Code-made motion + screen tutorial (calm explain, burst proof, keyword CTA)",
  "kind": "genre",
  "description": "From ref anim2 (@miftahul_islam_efaz, measured 2026-10-25): 16:9 or 9:16, ~120 wpm conversational VO, screen recordings with kinetic keyword captions in the empty half of the frame, code-rendered showreel burst (cards 0.1-0.6 s) as proof mid-video, series tag up front, comment-keyword CTA at the end.",
  "reference": "research/refs-2026-10-25/ai-animation.md#anim2",
  "pacing": {"remove_silence_over_s": 0.5, "pad_s": 0.12, "remove_fillers": "hard", "max_shot_s": 12.0},
  "captions": {"enabled": true, "size": 0.04, "max_words": 3, "animation": "pop", "uppercase": false, "keyword_caps": true, "highlight": "#F05A28", "outline": 0, "shadow": 2, "position_y": 0.5},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "dur_s": 2.0, "position_y": 0.35, "size": 0.06, "uppercase": true, "max_words": 3},
  "zoom": {"mode": "smooth", "every_s": 6, "scale": 1.12, "on_hook": 1.0, "on_emphasis": true},
  "broll": {"every_s": 0, "mode": "full"},
  "sfx": {"density_per_10s": 1.0, "db": -15, "map": {"hook": "whoosh", "zoom": "click", "title": "pop", "broll": "whoosh", "end": "riser"}},
  "music": {"energy": "mid", "db": -20, "duck": true},
  "grade": {"contrast": 1.03, "saturation": 1.0},
  "end_card": {"enabled": true, "dur_s": 4.0}
}
```
(The showreel burst is one pre-rendered code clip placed as a full B-roll item. The editor does not cut 0.1 s itself. Smooth zooms push into the UI region being discussed.)

**Narration / VO spec:** about 120 wpm, sentences of 5-10 words, peer tone, one "here's the secret" turn, steps numbered by verb ("Drop… Now watch… Copy…"). Persona: **Laid-back West Coast Smooth** (voice-persona-audio.md) at ~120 wpm, or Klaus's own voice for TITAN.AI (founder authenticity beats a persona here).

**Higgsfield side (for the non-code layers: the mascot room and plates).** Style key:
```
STYLE KEY: cosy voxel-art 3D diorama, chunky cube-built characters and furniture, soft warm desk-lamp key with
cool window fill, muted sage-green walls, wooden desk, gentle depth of field, clean readable silhouettes, no text
```
```json
{"id":"R01","dur":5,"camera":"slow dolly-in, 35mm, eye level toward the desk","action":"start: @VOXEL_HOST sips coffee in the armchair beside two dark monitors -> end: both monitors flick on and the host leans forward","light":"warm desk lamp key, cool window fill, monitor glow on the host's face"}
```
```json
{"id":"R02","dur":4,"camera":"locked medium, 50mm, straight-on","action":"start: @VOXEL_CHEF holds a wok over voxel flames -> end: he flips the wok, cube vegetables arc into the air, flames flare","light":"orange fire key from below, dark kitchen behind"}
```

**Example concepts:**
- **TITAN.AI (founder, Klaus's voice): "I don't hire motion designers. I write them."** Open: "AI SLOP" vs "TITAN" monitors in a voxel office. Burst: 15 s of code-rendered cards made for Physio Spot and Power Protein (real outputs). Steps: brief → design sheet → render. CTA: "Comment STUDIO and I'll send the template." (Use a real auto-DM; never promise what we can't send.)
- **Physio Spot (SG health): "Your back, explained in code."** A code-animated spine with discs as stacked cards and HUD labels ("L4-L5", "load: sitting 8 h"). Clean kinetic VO, no outcome claims, every anatomy line sourced in SOURCES.md, no free-consult hook.

---

## anim3: @stickmaxx "Same gym. Only one added weight." (14.6K likes, 76 comments, 14.6 s, 9:16)

### Format concept (why it hooks)
- **Two identical figures, one variable.** Left: "SAME WEIGHT, SQUAT: 60 KG". Right: "+10 KG A MONTH", with the number counting up. The header ticks "MONTH 1 >> … MONTH 7". The viewer instantly runs the comparison in their head. There is nothing to read beyond the counters, so it works muted and in any language.
- **Escalating visual exaggeration:** each month the right figure's plates change colour (blue → green → yellow → red → rainbow), the **head glows brighter** (bloom, which reads as "aura"), and the **legs swell** to cartoonish tree trunks while the left figure stays the same.
- **The punchline is typed text:** "SAME SQUATS. DIFFERENT LEGS." appears with a typing cursor as the camera pushes into the giant legs, then it **hard-loops back to MONTH 1** (it ends on the start frame), so replays are seamless. That loop drives completion rate past 100%.
- **There's almost no narration** (21 wpm, which is song lyrics: "Call me, I could phone…"). The track is a trending song, so it's music-led.

### Visual style
- **Render:** minimal 3D. White capsule-limb stick figures with round heads stand on **emissive warm tiles** (yellow → orange → red gradient squares) in a **black void with a glossy reflective floor**. There's a single bar stool between them as a "same gym" prop, and the barbells have coloured bumper plates. Bloom on the glowing head and the tiles is the only glamour.
- **Type:** a rounded pixel/monospace display font. The header is white, the right stats amber (#FFC266-ish), the left stats grey, and the "+0 KG / +10 KG" deltas pop under the stats each month.
- **Camera:** **one continuous shot, 0 cuts** (measured). It's a locked wide two-shot, then a slow push-in to the legs for the punchline, then a hard reset.
- **Timing:** ~7 months in ~11 s, so **~1.5 s per month**. Each month has one squat rep by both figures (synced), a plate swap on the right, and a counter tick. The typed punchline takes about 2.5 s and the loop reset is instant.

### How it was likely made [inferred]
3D animation in Blender/C4D or three.js: rigged capsule figures, a shape-key/scale ramp on the right figure's legs, and emissive tiles with bloom (Eevee-style). The text counters were done in AE or code; the deterministic counters and typed cursor point to motion software, not AI video. AI video would struggle to keep the numbers and the symmetry exact. Our best route is a **hybrid**: the counters, type and loop in code (tools/motion), and the figures either in code (three.js capsules are trivial; see the PoC) or as Higgsfield start/end-frame morphs when we want a richer render.

### Recipe for our stack
**Style key:**
```
STYLE KEY: minimal 3D render, two identical white matte stick figures with capsule limbs and round heads, black
void with a glossy reflective floor, glowing warm emissive floor tiles (yellow to orange to red), soft bloom,
perfectly symmetrical side-by-side composition, locked camera, no background detail, no text in frame
```
**Shot JSONs** (Seedance 2.5 start/end frame from Nano Banana stills; counters and text added in the edit or the code layer, never generated):
```json
{"id":"M01","dur":1.5,"camera":"locked wide two-shot, 35mm, slightly high, perfectly centred","action":"start: both @STICK_A and @STICK_B stand with barbells on their backs -> end: both complete one synced squat and stand; @STICK_B's legs are 15% thicker and his head glows slightly brighter","light":"warm emissive tiles under each figure, faint bloom, black void"}
```
```json
{"id":"M08","dur":2.5,"camera":"slow push-in from wide to low mid-shot on @STICK_B's legs, 50mm","action":"start: @STICK_B stands with hands on hips, legs enormous and rounded -> end: frame filled by the legs, @STICK_A visible only at the left edge","light":"strong head glow with bloom, tiles flaring orange-red"}
```
**Narration / VO spec:** none. Music-led, with one pop per counter tick, a soft whoosh on each plate swap, and keyboard ticks on the typed punchline. If a voice variant is tested, use **Sports Play-by-Play** at broadcast pace for the month calls only ("Month five… still sixty.").
**Sound:** brand accounts use a licensed CML track (`/sound`, tiktok_music_trending by country) or an original beat. The trending chart song goes on personal accounts in-app only.

**Edit spec (draft preset `stick-compare-loop`):**
```json
{
  "name": "stick-compare-loop",
  "label": "Side-by-side stick-figure progression loop (one variable, counters, typed punchline)",
  "kind": "genre",
  "description": "From ref anim3 (@stickmaxx, measured 2026-10-25): one continuous 12-16 s shot, two identical figures, one changes a variable each period (~1.5 s per tick), counters top-left/right, typed punchline over a push-in, hard loop to frame 1. Music-led, no VO, pop per tick.",
  "reference": "research/refs-2026-10-25/ai-animation.md#anim3",
  "beat_sync": true,
  "pacing": {"remove_silence_over_s": 99, "pad_s": 0.0, "remove_fillers": "none", "max_shot_s": 20.0, "drop_retakes": false},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "kicker", "persistent": true, "position_y": 0.06, "size": 0.03, "uppercase": true, "max_words": 4, "font": "DejaVu Sans"},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0, "mode": "full"},
  "sfx": {"density_per_10s": 6.0, "db": -18, "map": {"hook": "pop", "title": "click", "end": "whoosh"}},
  "music": {"energy": "high", "db": -10, "duck": false},
  "grade": {"contrast": 1.1, "saturation": 1.05, "vignette": true},
  "end_card": {"enabled": false},
  "safe_zone": {"top": 0.05, "bottom": 0.2, "right": 0.12}
}
```
(Counters and the typed punchline are better built in the code layer (tools/motion "split-compare" template) and placed as one full-frame clip. The preset then only mixes music and ticks.)

**Example concepts:**
- **TITAN.AI / Klaus personal (founder): "Same founder. Only one automates one task a week."** Counters: "TASKS AUTOMATED: 0" vs "+1 A WEEK: 26". Hours at the desk shrink on the right, the right figure's desk empties and his head glows, and the left drowns in paper stacks. Punchline: "SAME HOURS. DIFFERENT LIFE." No health claims needed.
- **Power Protein (light compliance): "Same lunch. Only one added protein."** Counters: "PROTEIN: 18 G" vs "+25 G". The visual is the figure carrying shopping bags more easily, not body change (no body-transformation claims). Add the label "illustration".
- **Physio Spot (SG health, careful): "Same desk. Only one gets up every 30 min."** This is education about a *behaviour*, not an outcome. Counters show "BREAKS TODAY: 0" vs "16"; the right figure stretches each tick and the left slowly curls into a C-shape (a cartoon exaggeration, labelled "dramatised illustration"). Never show "pain-free" numbers, never use before/after patients, and add no inducement. Run this past the compliance pack before posting. If in doubt, post it from Klaus's personal account, not the clinic's ad account.

---

## Cross-cutting lessons (for /learn if Klaus agrees)
1. **Blank-void sets beat built sets for AI consistency.** A grid floor (anim1) or a black reflective void (anim3) removes environment drift and makes the character and prop the whole story.
2. **Deadpan + absurd premise + familiar format = shareable.** The narrator never winks; the twist is wordless and calls back an early "throwaway" line.
3. **Put exact things in code, organic things in Higgsfield.** Numbers, type, HUDs, loops and charts go in code. Creatures, food, texture and performance go in Higgsfield. Composite them in the editor.
4. **Loops:** end on the first frame (anim3) or on a series card ("CAVEMAN 1 RIP"). Both make people watch again or watch the next one.
5. **Comment-keyword CTAs inflate comments (anim2: 1.22 comments per like).** Use them only when we can really deliver the file/DM, and never on SG health posts as an inducement.

---

## Genre module cards (draft, for genre-playbooks.md; Klaus to approve before they are merged)

### 32. Absurd how-to / survival recipe, narrated 3D (`absurd-howto-3d`) [draft; measured: ref anim1]
- **Why it works:** an impossible ingredient or task explained in a calm, familiar tutorial voice. The process is satisfying, an early aside opens a loop, and a wordless twist pays it off and sets up the next episode.
- **Pacing map (35-40 s):**
  - 0-2.5 s: the absurd action is already happening (no intro); VO "First, X, but don't just Y."
  - 2.5-5 s: the open-loop aside ("This is our last recipe…").
  - 5-30 s: one step per shot, 2-2.5 s each, with an imperative verb on each cut and state carried across cuts.
  - 30-34 s: the sensory payoff (crack, pour, bite) and the longest hold (3.5-4.5 s).
  - 34-38 s: the wordless twist (threat appears / it backfires), then an in-world series card ("CAVEMAN 1 RIP").
- **Shot grammar:** one master angle (a high 3/4 overhead, cooking-show top shot) for most steps; 3-4 macro inserts on hands and material; one low hero angle saved for the twist. A locked camera or slow push. The character's outfit and markings never change.
- **Look:** a hyper-detailed 3D character on an infinite cobalt-blue grid void; warm food and material tones against cold blue; soft overhead key light.
- **genre_key:** `hyper-detailed 3D character render on an infinite saturated cobalt-blue studio floor with a thin white perspective grid fading to a pale-blue horizon, no walls, no other props, soft overhead key light with gentle contact shadows, tactile macro textures, warm food tones against the cold blue, clean tutorial staging, same character design in every shot, no text in frame`
- **Shot:** `{"camera":"high three-quarter overhead, 35mm, locked, slight push-in","action":"start: @CAVEMAN packs rock salt around the leg -> end: only the bone end pokes out of a smooth white mound","light":"soft overhead key, contact shadows, cold blue bounce"}`
- **Sound:** a deadpan VO at ~200-210 wpm (~7-8 words per shot); one-word captions; foley on every process verb (crunch, sizzle, crack); a low bed at -24 dB; one impact on the twist; no meme sounds on brand accounts.
- **Compliance:** for a health brand, the "recipe" must be safe technique or education, with no outcome or cure claims, no testimonials and no superlatives. The twist can be slapstick but never a medical injury scare. Food or supplement versions make no nutrition claims beyond the label.
- **Preset:** absurd-howto-3d (JSON in research/refs-2026-10-25/ai-animation.md).

### 33. Code-made motion + screen tutorial (`code-motion-tutorial`) [draft; measured: ref anim2]
- **Why it works:** the contrast hook ("slop vs this"), then proof (a 10-15 s burst of code-rendered cards), then a calm, doable how-to. The series tag and comment-keyword CTA drive comments and follows.
- **Pacing map (60-145 s; 16:9 YouTube/LinkedIn or 9:16):**
  - 0-3 s: series tag plus a glitch-in title ("PART 2").
  - 3-12 s: the contrast claim on two screens ("AI SLOP" vs "WITH THE SKILL") and the price or effort hook.
  - 12-25 s: who it's for / where it runs (a chalkboard or card list), then "now let's cook" (a mascot card).
  - 25-60 s: steps over screen recordings, with keyword captions in the empty half of the frame and smooth push-ins on the UI.
  - 60-76 s: the PROOF BURST, a code-rendered showreel with cards at 0.03-0.6 s and one idea per card.
  - 76-130 s: the second method or part, over a painted plate background.
  - Last 8 s: the keyword CTA ("Comment X") plus "part 3".
- **Shot grammar:** real screen recordings for UI (never faked UI). A voxel or illustrated host room for the bookends. Code cards for claims and numbers. The camera is a smooth digital push in the edit.
- **Look:** dark UI + cream/black type cards, a heavy grotesk for punch words, an italic serif for poetic lines, mono HUD micro-text (frame counters, coordinates); accents in mint and orange-red, or the brand's hex.
- **genre_key (non-code layers only):** `cosy voxel-art 3D diorama, chunky cube-built characters and furniture, soft warm desk-lamp key with cool window fill, muted sage-green walls, gentle depth of field, clean readable silhouettes, no text`
- **Shot:** `{"camera":"slow dolly-in, 35mm, eye level toward the desk","action":"start: @VOXEL_HOST beside two dark monitors -> end: left monitor flickers on showing cluttered slop, right shows a clean card, host leans in","light":"warm desk lamp key, monitor glow on the host"}`
- **Sound:** a conversational VO at ~120 wpm with 5-10 word sentences; a mid-energy bed at -20 dB ducked under the VO; clicks and whooshes on UI moves; the burst cut to a beat-synced track with one hit per card.
- **Compliance:** only claim what our real outputs show (no "Higgsfield-level for free" claims we can't back). Reference videos are study-only and never downloaded and re-cut. A keyword CTA must deliver what it promises, and it is never an inducement on SG health posts. Show real client work only with permission.
- **Preset:** code-motion-tutorial; the burst comes from tools/motion (proposed) as one full B-roll clip.

### 34. Side-by-side progression loop, stick figures (`stick-compare-loop`) [draft; measured: ref anim3]
- **Why it works:** two identical figures and ONE variable. Counters tick on screen and the difference compounds visually (glow, size, colour) until a typed punchline lands. Then it loops to frame 1, so it reads muted and in any language.
- **Pacing map (12-16 s):**
  - 0-1.5 s: Month/Week 1, both figures equal, counters visible (the persistent header "SAME X. SAME Y.").
  - 1.5-11 s: 6-7 ticks at ~1.5 s each; per tick, a synced action rep, the variable changes on the right only, the delta pops ("+0" grey / "+10" amber) and the exaggeration grows.
  - 11-14 s: the typed punchline with a cursor ("SAME SQUATS. DIFFERENT LEGS.") over a slow push-in on the changed feature.
  - 14 s: a hard cut back to the first frame (seamless loop).
- **Shot grammar:** one continuous shot, zero cuts; a locked, perfectly symmetrical wide; a single shared prop between the figures as the "same" anchor; only the final push-in moves the camera.
- **Look:** white capsule stick figures, a black reflective void, warm emissive floor tiles, bloom on the "winning" figure's head, a pixel/mono display font, white header + amber winner stats + grey control stats.
- **genre_key:** `minimal 3D render, two identical white matte stick figures with capsule limbs and round heads, black void with a glossy reflective floor, glowing warm emissive floor tiles, soft bloom, perfectly symmetrical side-by-side composition, locked camera, no background detail, no text in frame`
- **Shot:** `{"camera":"locked wide two-shot, 35mm, slightly high, centred","action":"start: both figures stand with barbells -> end: both finish one synced squat; @STICK_B's legs are slightly thicker and his head glows brighter","light":"warm emissive tiles, faint bloom, black void"}`
- **Sound:** music-led (a licensed CML track or an original for brands; a trending chart song only on personal accounts, in-app); a pop per counter tick; a whoosh on each prop swap; keyboard ticks on the typed punchline; no VO.
- **Compliance:** this is a comparison format, so in SG health it is close to before/after. Show behaviours and inputs (breaks taken, protein added, tasks automated), not guaranteed body or pain outcomes. Label exaggeration as "dramatised illustration", use no patients and no "results" numbers. Counters and type are built in code so the numbers are exact and checkable.
- **Preset:** stick-compare-loop; the counters, type and loop come from the tools/motion split-compare template (proposed). The figures come from code (three.js capsules) or Seedance start/end morphs.
