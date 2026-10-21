# Motion design: ads, trailers, product videos, explainers, Vox-style docs

Motion design means editable graphics built in code (text, UI, charts, maps, shapes, particles, 3D-in-code), combined with generated footage only where real-looking people, products or places are needed. The split is the point: graphics stay editable and cheap to change, and only the footage spends credits. [HF-Motion]
Source tags are explained in `research/sources-editing.md`. Product assembly and exploded-view reveals are covered in product-vfx.md.

## 1. Tool choice
| Need | Tool | Notes |
|---|---|---|
| Quick animated explainer, chart or walkthrough, MP4 out | **Claude Motion** (artifact "Motion" template) | Beta on Team/Enterprise plans. Code-built with no video model, so no AI people. Edit any word, number or timing, export MP4, "open in" Adobe, Higgsfield, HeyGen, Runway and others. [Anthropic-Motion] |
| Full control in Claude Code, React | **Remotion** | `npx create-video@latest --yes --blank my-video && cd my-video && npx remotion skills add && npm run dev`, then run `claude` in the folder. Check the Remotion license for company use. [Remotion-docs] |
| Full control, plain HTML/GSAP, no build step | **HyperFrames** (HeyGen, Apache-2.0) | `npx hyperframes init my-video && npx hyperframes preview && npx hyperframes render`. Needs Node 22+ and FFmpeg. Claude plugin: `claude plugin marketplace add heygen-com/hyperframes && claude plugin install hyperframes@hyperframes`. [HyperFrames] |
| Generated footage inside the motion piece | Higgsfield MCP (Seedance 2.5 / Kling 3.0 / Nano Banana) | Generate only the shots, then composite. [HF-Motion] |
| Finishing by a human or in a pro tool | After Effects or Blender | Ask Claude to "transfer the project with editable layers into After Effects", or rebuild a 3D sequence in Blender. The presenter got it working, slowly. [HF-Motion] See claude-editing.md for AE MCP. |
| Precise 3D camera timing (product hero, hyper-motion) | Blender gray-box via Higgsfield Bridge → Seedance | See credit-saving.md §2. [HF-Blender] |

## 2. Core workflow (works with any tool above)
1. **Reference first.** Upload 1-6 reference videos or Instagram links. "Giving references to Claude is easily the single best thing you can do." Say exactly what to match: motion, transitions, palette, pacing. [HF-Motion] For motion examples that come with their prompts, see promptmotion.com. [Duncan]
2. **Teach the style before the job:** upload 15-20 images in one consistent style (from Pinterest or Cosmos), then "Describe the style. Don't edit yet." Approve the description. [100x]
3. **Style test:** "Make 3 static frames in this style from 3 lines of my script." [100x]
4. **Animation test:** "Animate frame 1 according to its script line." [100x]
5. **Storyboard / beat map:** list every sentence with what's on screen while it's said. Either Claude drafts it and you cut it, or you draft it and Claude critiques it. [100x] [Duncan]
6. **Build in scenes.** Each scene goes to its own sub-agent, in parallel (6 at once worked), using Opus to plan and Sonnet to build. [Duncan] [HF-Motion]
7. **Design sheet before export:** screenshots of every scene for approval. Then render a half-size draft, then full size. [Joseph-YT] [Duncan]
8. **Iterate with specific notes**, e.g. "she hangs in the air, make it one grounded step" or "the clipboard paper faces us but the cat writes on the back, flip it". [HF-Motion]
9. **Sound pass last** (whooshes → textures → risers; see claude-editing.md §5). [UE-Sound]

Briefing rule: **be specific about how things move and how scenes connect.** The clearer the brief, the less the model guesses. [HF-Motion]

## 3. Kinetic typography rules
- One idea per card, 1-5 words, keyword in the accent colour, and **readable dwell of at least 0.3 s per word plus 0.5 s**. "Text that shows up too late to read" is a QC fail. [Duncan]
- Text follows speech. Words appear on the word they're spoken (word timestamps from faster-whisper), never before.
- Use one sans plus one script or serif font pair at most. The UE caption system uses "a sans font and a script font". [UE-Prompts]
- Use motion verbs: slide up and settle (ease-out), pop with 5-10% overshoot, letter-by-letter write-on, mask reveal, scale punch on the beat.
- **Text can sit behind the subject** (person segmentation / matte) for a premium look. [100x]
- Darken and blur the background behind on-screen UI cards so they read. [UE-Prompts]
- **Responsive layout:** when a word changes, connected elements resize and the scenes re-time with the music still in sync. Ask for this explicitly so the piece stays editable. [HF-Motion]

**Prompt (Remotion/HyperFrames/Claude Motion):**
```
Build a 9:16, 15 s kinetic-type sequence from this VO + word timestamps (attached JSON).
Style: [paste approved style description]. Fonts: <sans> + <script>. Palette: <hex list>.
Each phrase = one card; keyword highlighted in <accent>; entrance = slide-up 12px + fade, 220 ms ease-out;
exit = 120 ms fade; one beat-synced scale punch (1.0→1.06→1.0) per sentence. Text must appear on the spoken word,
minimum read time 0.3 s/word + 0.5 s. Keep it fully editable: every string, colour, duration as a prop.
Give me a design sheet (screenshot per card) before rendering.
```

## 4. Product reveals and launch videos
- **Launch-video recipe** (the Higgsfield viral launch format): UI and motion in code, product and lifestyle shots generated, fast and smooth, 20-30 s. Mixing 3 reference videos into a new film worked. [HF-Motion]
- **3D product ad in code:** "rebuild this reference shot in 3D, keep the rhythm, editable". Then iterate with "smoother camera, richer textures, more going on in 3D", and add your fonts and logo. **Product swap** is one line: "replace the truck with this bicycle". [HF-Motion]
- **Hyper-motion / beverage-style ad** (can bursts, fruit splits, ice freezes mid-air): block it with primitives (cylinder can, cube ice, sphere fruit), cut in the blockout, add a **speed ramp** (slam in, hold a beat, accelerate into the next cut), reveal the logo one letter at a time, and use one text line telling the model which colour = which flavour. [HF-Blender]
- **Physio/health products** (PeachForm, Power Protein): no "best" or "#1" claims and no before/after miracle framing (SG pack). Lead with the mechanism, the texture or the ritual instead.

**Prompt (generated hero shot, Seedance 2.5 draft first):**
```
Studio product hero, <product> on a seamless <colour> sweep. 0-1.5 s: macro push-in across the logo emboss,
shallow DOF; 1.5-2.0 s: snap speed-ramp into a 180° orbit; 2.0-3.5 s: product rises 10 cm and freezes, droplets/ingredients
hang mid-air around it; 3.5-4 s: settle to centred packshot, soft top light, clean shadow. Brand colours <hex>.
No text in frame (text added in post). Camera locked to blocking reference video (attached).
```

## 5. Trailer and teaser structure
**30-60 s trailer, three acts:**
1. **World and hook (0-20%):** an establishing image plus one intriguing line. Quiet.
2. **Escalation (20-75%):** shots shorten (3 s → 1 s). Use title cards between beats ("THIS SUMMER" / "ONE CHOICE"), a riser under the cuts, and one false calm.
3. **Peak and button (75-100%):** the fastest montage hits the drop, then **silence**, then a button line or gag, then the title and logo, then the date or CTA.
- **Teaser (15-30 s)** = hook plus withheld payoff. "Work out what to reveal and where to leave you hanging." [HF-Clip]
- **Sound map:** riser into each act break with an impact hit underneath. Whooshes peak on the fastest frame. **One impact per scene.** [UE-Sound]

**Prompt:**
```
Write a 45 s trailer cut-list for <project> from the attached footage/script. Output a table:
timecode | shot (source or "GEN: <prompt>") | on-screen text card | VO/dialogue | SFX family (whoosh/texture/riser/hit) | music cue.
Act 1 0-9 s, Act 2 9-34 s (shot length shrinking 3 s→1 s), Act 3 34-45 s with a 1 s silence before the button line.
Then build title cards in code (style: <description>) and list only the shots that need generating.
```

## 6. SaaS / app demo and explainer
- Use UI mock animation (cursor types, clicks, panels slide), camera zooms into the UI, and annotation pointers ("hook the viewer" on the hook line). It's the "highest demand style" of motion right now. [HF-Motion] [Joseph-YT]
- **Hybrid explainer with a cartoon:** characters and voices generated through Higgsfield, with documents, text and map routes animated in code. That took about 2 h for the presenter, and only the broken shots get regenerated. [HF-Motion]
- For TITAN.AI demos, screen-record the real product and have Claude animate around it (zoom-ins, highlights, callouts) rather than faking the UI.

## 7. Vox-style documentary motion (paper texture, choppy frame rate)
Joseph's method uses three "brains" (skills): [Joseph-Vox]
1. **Editor brain:** transcribe ~10 reference docs (timestamps), have Claude study what is said versus what is shown, and deduce why. The output is a scene-planning skill. Feed it the script and it plans scenes per phrase (year counter → character + text → clock, map → global map with circles, graph with circled year, pie chart around a character, quote card).
2. **Design brain:** collect ~100 style references in one Figma/PDF board and have Claude extract the design system (colours, shapes, type, textures, macro and micro details). The output is design guidelines. Generate scene designs as stills (Higgsfield) and approve them.
3. **Animator brain:** describe the 5 asset layers per scene: **text** (minimal pop), **main object** (paper-unfold or position pop), **background** (static), **secondary objects** (subtle jitter) and **camera** (slow zoom or pan). Animate the approved stills in Seedance, prompting for the rough, choppy, jittery look and transitions between designs.
- VO: an ElevenLabs narrator voice at medium speed. Score with a mysterious synth bed. Assembled in Premiere. Cost was about $20 of Higgsfield credits for 60 s including tests. [Joseph-Vox]
- Higgsfield also ships an "Editorial Motion Graphics" preset (`/vox-mixed-media`) and a stickman explainer preset. [HF-MCP-page]
- Every stat needs a source in `SOURCES.md` (commentary-controversy.md fact-check layer).

## 8. QC for motion pieces (add to qc-rubric)
Check at 10 fps, not 1 fps [Duncan]: an animation playing twice, a graphic flashing for one frame, text too late or too short to read, a graphic covering a face, a repeated word, lip drift, two of the same person on screen, music under graphics, and whoosh peaks off the fastest frame.
