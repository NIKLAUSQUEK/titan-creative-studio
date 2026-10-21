# AI filmmaking + long-form (short film, series, movie)

Load this for short films, multi-scene ads, series and anything longer than one generation (more than 15 s).
Precedence: ledger > brand > Klaus's script (MASTER SPEC, never restage) > this file.

Tags: [HF-DIR] Higgsfield "Prompt Like a Director" (delivery-app ad) · [DAN-ADV] Dan Kieft "Master AI Filmmaking in 30 Min" · [LARRY] Larry Ulrich Higgsfield/Kling movie tutorial · [SIRIO] Sirio "Make AI copy emotions" · [DAN-TOOLS] Dan Kieft "3 Free Tools" · [DAN-REAL] Dan Kieft realism guide · [KAYE] kaye.creatives realism · [SD-DOCS] Seedance 2.5 official guide · [KLING] Kling 3.0 official guides · [SHOTCRAFT] Shotcraft defects reference.

---

## 1. Pre-production: the story bible (before a single credit)
**Organise first.** Create one Cinema Studio project per film, with folders and subfolders per asset type (characters / locations / props / scenes). "Two weeks and 400 generations later you'll be glad" ([HF-DIR], [KAYE]). Mirror it locally under `projects/<p>/assets/`.

**"Lazy prompting" mega-brief** ([KAYE]): give Claude ONE brief containing story, every character, every location, props, camera structure and the VO script, plus Pinterest/reference images. Claude returns every asset prompt and scene prompt in one pass. That beats 30 piecemeal messages that pollute context.

**Story bible file** (`projects/<p>/BIBLE.md`), built with the help of a guided story tool ([DAN-TOOLS] "AI World Builder" pattern: story → genre → hero → supporting cast → antagonist → world → acts → script PDF):
```
LOGLINE · GENRE/TONE · RUNTIME · ASPECT
CAST: name | role | want | look (locked wording) | voice description | ref sheet IDs
WORLD/LOCATIONS: name | master plate ID | anchors (3 landmarks) | light/time | grade block
PROPS: name | ref ID | owner | continuity notes (which hand, state: full/empty/broken)
ACTS → SCENES → SHOTS (shot list below)
VOICE BIBLE: per-character voice description (pitch, age, accent, texture) reused verbatim in every prompt
```
**Scope creep warning** ([DAN-ADV]): his planned 1-minute film became 3 minutes for lack of a shot list. Pros write the **shot list first** and generate down it.

## 2. Character consistency
- **Three references per lead character** ([DAN-ADV]): (1) a full-body turnaround sheet, (2) a front-facing identity close-up, (3) a close-up detail sheet for skin, hair, eyes and texture. One sheet alone drifts (hair colour, for example).
- **Mid-grey background, not white.** White bleeds overexposure into scenes ([DAN-ADV], [HF-DIR] "huge hack").
- **Neck-down crops on the outfit panels** so the model has only **one face** to learn from. The other panels carry clothes and proportions only ([HF-DIR]).
- Check for skin that looks too smooth or lighting that is too harsh, and fix it with an edit model (Seedream 5 Pro) rather than a full reroll ([HF-DIR]).
- Explore cheaply: Soul Cinema gives about 8 images for 1 credit, so generate many concepts, then lock one ([HF-DIR]). Final sheets go to GPT Image 2/2.5 at high/2K-4K ([DAN-ADV]). Seedream 5 Pro is also strong for ultra-real humans ([KAYE]).
- **Real people beat generated ones**: photograph the actual person (Klaus, staff) for references ([DAN-ADV]; matches CLAUDE.md).
- Creatures and props deserve close-up texture sheets too ([DAN-ADV] dinosaur).
- **Don't start a shot from the back of a head.** If the character turns round mid-shot, the face may not come back as your character. Start facing camera, have them turn away, then turn back, and cut the reveal in the edit ([LARRY]).
- Kling 3.0: define core subjects at the very start of the prompt and keep their wording **identical** whenever they recur ([KLING]). Bind elements (`@Element1…`) for 3+ characters ([KLING] / supercmo Kling guide).
- Seedance 2.5: put the lead character at the **lowest reference index**, because low indices hold identity best. Bind roles in prompt text ("the singer references @Image1"), never through names written on the image. Close with a preservation clause ([SD-DOCS] / Runware guide).

## 3. Location consistency + blocking
- **Lock layout, lighting and background before generating**, as on a live-action set ([HF-DIR]). Build a mood board / master location per set, then derive angles from it (PJ Accetturo's newsletter is the pro reference cited by [DAN-ADV]).
- **3/4-angle master plates**: the added depth gives camera moves something to grip, and renders better than a flat head-on plate ([HF-DIR]).
- **Edit the plate for the action**: shrink foreground clutter and clear the table where the delivery bags will land ([HF-DIR], Seedream 5 Pro edit, keeping light and texture).
- **Bake food and props into the location plate** when they are fixed per seat, so you don't need separate prop references ([HF-DIR]).
- **Extras as one group reference** (all four musicians in one image) ([HF-DIR]).
- **Seat-to-landmark anchoring**: tie every character position to a background landmark ("skylight behind Micah, shelves behind Jenny, red lamp behind Alex"). That gives you something to check as the camera moves ([HF-DIR]).
- **Open with a wide master in the same generation** to lock positions, then cut to close-ups. You may drop the wide from the edit later ([HF-DIR]).
- **Reverse angles**: describe exactly what is visible from the new camera position ("camera beside the building, pointing out toward the valley; band in foreground, table beyond, hills in distance"). Otherwise the model invents a wall ([HF-DIR]).
- **Colour-coded blocking map** for crowded or overhead shots: generate a top-down map (orange = Jenny left, blue = Alex top, green = Micah right; three plates, two shared dishes, phone beside Jenny) and attach it with the character refs. Tell the model the colours are labels only ([HF-DIR]; it fixed a 4th phantom seat).
- **Pose/camera blockout**: a 3D blockout or pose tool (Dan's free aicameracontrol.com) sets the exact angle and poses, then goes in as a pose reference with the character sheets ([DAN-TOOLS]). Seedance blockout rule: strip motion paths, axes and camera frustums, or they leak into the render ([SD-DOCS]).

## 4. Shot list, coverage, continuity
**Shot list row** (`projects/<p>/SHOTLIST.md`):
`# | scene | dur | size/angle | lens | camera move | action (1 verb) | dialogue (speaker) | refs (@) | continuity in/out | transition | audio`
- One action per shot that **completes inside it**. Change the shot size or angle between consecutive shots so cuts read. One camera move per shot; a second move means a second shot ([SHOTCRAFT]).
- Name the camera move OR name its absence ("locked-off tripod, no camera movement"). An unnamed camera drifts ([SHOTCRAFT]).
- Kling 3.0 Multi-Shot runs up to 6 shots per generation. Custom Multi-Shot sets per-shot duration, framing, action, dialogue and move. Attach dialogue to the named speaker ([KLING], fal guide).
- Seedance 2.5 timeline: continuous whole-second ranges. Too little content → it improvises; too much → it drops actions ([SD-DOCS]).
- Don't timestamp everything. "Shot 1 / Shot 2 / Shot 3" and letting Seedance pace often works ([DAN-ADV]). Add "24 fps" to the setting block to reduce laggy motion ([DAN-ADV]).
- **Transitions designed in the prompt** ([HF-DIR]):
  - *Match cut on action*: cut on a phone tap; keep framing and camera move identical; only the location changes.
  - *Body wipe*: the camera slides behind a character's back, which fills frame and hides the cut into the new place.
  - *Audio-first transition*: cut the music and bring in the next location's ambience **before** the visual reveal.
- **Continuity across generations** ([DAN-ADV]): screenshot the last good frame(s) of the previous clip, plus every prop present (the TV he jumped out of, the carcass), and pass them as references for the next angle. Missing prop refs = props vanish. If a detail is missing, edit the start frame ("add a small dead reptile carcass beside the man, keep everything else exactly the same") before animating.
- **Eye-line control** ([LARRY]): models love to tilt the eyes up. That reads as submissive and broke his "tough" lead. Put "She keeps looking straight ahead at eye level; her eye line never moves up or to the side" at the **start** of the prompt and repeat it. If that still fails, switch model.
- **Never mention off-screen people.** "He looks toward the two agents off camera" pulled them into frame. Delete every reference to anyone who must not appear ([LARRY]).
- Dialogue syntax: `<Character> says: "<line>"` in quotes, tone after ([LARRY]). Keep prompts under the platform cap (Larry: aim for 2,500 characters or fewer on Kling/Higgsfield; ask the LLM for that up front).

## 5. Prompt formats (pick per shot)
1. **Simple** ([DAN-ADV]): `[camera] + [subject @ref] + [action] + [subject 2 @ref] + [consequence]`.
2. **Timeline** ([DAN-ADV], [SD-DOCS]): SETTING block (location, realism, natural light, handheld energy, no music, 24 fps) → Shot 1…n → constraints.
3. **Labelled blocks** ([CONOR] in documentary-3d.md): ASSETS / BRIEF / STYLE (locked) / GRADE (locked) / SHOTS / SOUND / CONSTRAINTS.
4. **Chinese timeline for Seedance** ([DAN-ADV]): Seedance is a ByteDance model and sometimes follows Chinese better. Have Claude output the prompt in Chinese **plus** an English mirror for review; edit the English, regenerate the Chinese. Use it when an English prompt keeps failing.
5. **Official Seedance 4-part** ([SD-DOCS]): asset mapping → one-sentence brief → timeline → global constraints. Every asset answers "whose is it, and what exactly to take from it". State what must **not** be inherited.

**Director-skill pattern** ([HF-DIR]): a Claude skill turns a plain scene description into shots with dialogue timing and camera moves. Attach the refs labelled with the **same names** used in the prompt (for example `character Micah`, `location flat 2`). In Cinema Studio, refs named in the prompt auto-attach as Elements.

## 6. Emotional performance control
**Two-layer method** ([SIRIO]): split a performance into **movement** (expression, timing) and **identity** (face). Feed movement through a neutral grey **clay/matte-cap 3D face mask** video (Seedance 2.5 turns clay renders into real people well), and identity through your character photo/video. Open-source pipeline on Sirio's GitHub (MediaPipe + SPECTRE + FLAME + grayscale shading overlay). FLAME and SPECTRE are **non-commercial licences**, so it is **not for client ads**. Uploading a real actor's clip directly gets flagged.
- Debug rule ([SIRIO]): emotion missing from the mask → fix the mask; present in the mask but not on the face → fix the prompt. Prompt and mask must push together.
- The mask freezes when the actor turns away (no face to track). Note frozen spans in the prompt or avoid such clips. Keep other speakers' lines out of the prompt or your face mouths them too ([SIRIO]).
- **TITAN default**: Klaus films a phone reference and uses **Genjutsu motion transfer** (`hf_mult_motion_control`) or Seedance video-to-video. "Have @Image1 play the performance and dialogue of @Video1; replicate exact hand/body/head movements". Add environmental motion (leaves swaying), because static-shot backgrounds go stiff ([DAN-ADV]). Video-to-video also keeps **your real voice** ([DAN-ADV]).

**Write emotion as visible physiology, second by second** ([SD-DOCS], [SIRIO]). Have the agent describe eyes, brows and mouth per second from the reference, then check it against the footage yourself.

Acting-direction vocabulary (combine: *beat → visible change → breath → hold*):
| Emotion | Write this (visible) | Avoid |
|---|---|---|
| Grief building | grin fades to a tight smile, chin begins to tremble, eyes redden and glisten, one tear tracks down, breath catches | "sad", "crying dramatically" |
| Suppressed anger | jaw clenches, nostrils flare once, gaze holds without blinking, speaks quietly through teeth | "furious", shouting by default |
| Apprehension | eyes flick left then back, small swallow, shoulders rise slightly, weight shifts back | "nervous" alone |
| Relief | exhale through the mouth, shoulders drop, brow unknits, soft half-smile | "happy" |
| Curiosity + caution ([LARRY]) | head tilts slightly, brows lift a little, lips part, steady forward eye line | "confused" |
| Deep thought ([LARRY]) | turns away, pauses still for two seconds, slow turn back, softened expression | instant turn |
| Comic double-take | glance away, half-second freeze, snap back, eyes widen | "funny reaction" |
- Kill the mannequin look: specify **micro-behaviour** (blinks, swallows, breath, small weight shifts) and **restraint** ("subtle, understated, naturalistic, no exaggerated expressions").
- Pace big emotions over 4-8 s. Instant swings look fake.
- **Voice consistency** ([DAN-ADV]): describe each voice verbatim in every prompt ("rough, deep, guttural adult woman"; "young 12-year-old American boy"). Get a description of an existing voice by uploading the audio to Gemini. Attach your own audio file as a reference to have the character say exactly those lines. Use one good mic consistently, because mixed mic quality is audible.
- ElevenLabs v3 VO: Creative delivery mode, batch 4, pick the best ([KAYE]).

## 7. Generation economics + iteration
- **Draft at 480p first, then 1080p** (CLAUDE.md; [DAN-ADV] 840 vs 4,800 credits; [KAYE] verified-draft → 1080p first-try). The 1080p won't be identical, but a bad draft means a bad prompt.
- Reread the prompt before hitting generate. A paste error cost Larry 20 credits ([LARRY]).
- **Reuse "dead" footage**: the pre-line seconds of a take become a listening/reaction cutaway, so you don't need to generate one ([LARRY]).
- **Stitch the best segments from multiple takes**. Nobody gets a perfect one-shot ([DAN-ADV], [HF-DIR]).
- Speed clips up slightly (about 103%) in the edit for snappier, more natural motion ([LARRY]).
- Hold your reveals: cut before the character's face turns, to build intensity ([LARRY]).
- Learn camera vocabulary. Static shots everywhere kill story, because movement tells it ([LARRY]). See the camera table in realism.md and Dan's free aicameramovements.com cheat sheet ([DAN-TOOLS]).
- [HF-DIR]'s 30 s, 3-country ad cost about 2,100 credits including retries.

## 8. Hard-to-generate shots: composite instead
([DAN-ADV]) Film the real action (for example tapping a phone, with its UI legible), then **replace the background** with a VFX/background-replace tool, or **relight** (golden hour) an existing clip. Use Seedance `video_edit` / Kling edit in Higgsfield. That beats regenerating text-heavy screens.

## 9. Post-production
- Organise → trim → stitch → check for gaps → grade → SFX → fix flaws in the sound design (a weird scream gets replaced) ([DAN-ADV]).
- Don't butt 5-second clips end to end. Study normal film editing. Editors make the best AI filmmakers ([DAN-ADV]).
- Grade-match every clip to one reference; add grain/texture last (see realism.md).

## 10. Equip Claude (tools to build or use)
[DAN-TOOLS]: vibe-code small tools for repeated steps. The meta-prompt recipe has 3 questions: **What do I want to build? Why (what pain)? What features?** Have Claude write the build prompt, revise it, then build it in Claude Code.
- **World Builder** (story wizard → character sheets → location coverage, using Higgsfield MCP + Claude API key; GPT Image 2 for sheets, Soul Cinema for cheap location coverage, "full coverage" angle batches).
- **Camera/pose control** (aicameracontrol.com): free 3D blockout → pose reference + prompt.
- **Camera movement cheat sheet** (aicameramovements.com): copyable move prompts.
- **MD skill files**: Dan's filmmaking MD (character sheets, shot lists, timeline/Chinese prompts) ([DAN-ADV]). Turn any winning prompt + image into a reusable style `.md` ([DAN-REAL]).
- In this repo: the director-skill and blocking-skill equivalents live in `/plan` + `cinematic-ad-director.md`. Store reusable style MDs under `references/` or as Supabase StyleCards.

## Long-form assembly checklist
- [ ] BIBLE.md + SHOTLIST.md approved before any video credits
- [ ] Every lead: 3 refs (sheet / identity / detail) on grey, Gate 4 approved
- [ ] Every location: master 3/4 plate + 3 anchors + grade block
- [ ] Each shot prompt: assets mapped, one action, one move, eye line, speaker-tagged dialogue, no off-screen mentions
- [ ] Continuity refs (last frame + props) attached for every follow-on angle
- [ ] 480p draft QC'd (`scripts/qc_frames.py`, contact sheet) → Klaus OK → 1080p → 4K upscale of locked cut

## Sources
- Higgsfield AI, "How To Prompt Like a Director Using Opus 5.5 + Seedance 2.5" - youtube.com/watch?v=kFKpcCHkuPI
- Dan Kieft, "Master AI Filmmaking in 30 Minutes" - youtube.com/watch?v=e9ZupmL9BcM
- Larry Ulrich, "Higgsfield AI Tutorial | Cinematic AI Videos" - youtube.com/watch?v=8qfonxqvoSQ
- Sirio, "Make AI copy emotions from any scene (open source workflow)" - youtube.com/watch?v=AgLijG7t1QU
- Dan Kieft, "AI Filmmaking got 10x easier with Fable 5 - I Built 3 Free Tools" - youtube.com/watch?v=3YkMI7z_CWI
- kaye.creatives, "How I Get Perfect AI Realism on the First Try" - youtube.com/watch?v=w0R29uK3Hfk
- Seedance 2.5 Prompting Guide - docs.seedance.tv/en/seedance-2-5-prompting-guide ; Runware multi-reference guide - runware.ai/docs/models/bytedance-seedance-2-5/guides/multi-reference-production
- Kling 3.0 guides - kling.ai/quickstart/klingai-video-3-model-user-guide ; kling.ai/blog/kling-video-3-multi-shot-guide ; blog.fal.ai/kling-3-0-prompting-guide
- Shotcraft, "Why AI video looks wrong" - shotcraft.video/reference/video-defects/
