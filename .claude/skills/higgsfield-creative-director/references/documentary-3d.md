# Documentary + 3D mannequin documentary: the workflow

Load this when Klaus asks for a documentary, a "Fern-style" or "Black Files-style" 3D explainer, true-story recreation, "how X actually works", or a narrated educational piece (for example "how the pelvic floor works", "the history of testosterone therapy").
Precedence still applies: ledger > brand file > Klaus's script > this file. Sources are listed at the bottom and in `research/sources-filmmaking.md`.

Tags used below: [CONOR] = Creating with Conor 3D doc tutorial · [CASH] = Cash-Coach free 3D doc guide · [DAVID] = David AI free doc tutorial (Spanish) · [DAN-ADV] = Dan Kieft advanced course · [SD-DOCS] = Seedance 2.5 official prompt guide · [VERSELY] = Versely finishing guide.

---

## 0. Why the 3D mannequin look suits TITAN
- A stylised matte mannequin or clay figure avoids real-person likeness entirely. That fits the CLAUDE.md rule against AI likenesses of real people, and it makes anatomy and medical topics read as diagrams, not gore or nudity. This is TITAN's own reasoning.
- The niche works on YouTube: [CASH] cites a 3D mannequin true-crime channel at roughly 400k subscribers, with US/UK/CA audiences and an estimated RPM of $10 or more. That is the tutorial author's estimate, not verified.
- **The brand's compliance pack still applies** (e.g. Singapore health: no testimonials, no superlatives, no inducements). Every factual claim gets a source in the project's `SOURCES.md` (see commentary-controversy.md for the fact-check layer).

## 1. Pipeline at a glance
```
Research + premise → script/narration (timed per clip) → STYLE KEY (base mannequin sheet)
→ character sheets (same paragraph, swap one line) → location plates (shared grade block)
→ composite stills (plate + character, lit by the room) → video per clip (Seedance 2.5, block prompts)
→ VO per clip (ElevenLabs v3) → music + SFX → edit (VO-first) → upscale 4K → thumbnail
```
All of the above is the [CONOR] spine. The "per clip" structure and the "type next" chatbot driver come from [CASH] and [DAVID].

## 2. Research + script
1. **Master-prompt driver** ([DAVID], [CASH]): a single chatbot session with a master prompt walks through a fixed sequence, advancing on "next": topic ideas → duration + aspect → audience → language → tone → premise + research → script → image prompts → video prompts → narration in one block → thumbnail prompts → channel branding. Reproduce this as a stepwise interrogation in `/ad` or `/brief`. Do not dump everything in one reply.
2. **Originality rule** ([CASH]): feed the model a *style* reference (pacing, hook pattern, transcript rhythm of the niche). Have it generate **new topics**. Never paraphrase another creator's script, because YouTube treats that as inauthentic/reused content and demonetises it.
3. **Script shape for a mystery doc** ([CONOR], heist example): cold open on a time-stamp ("3:00 a.m."), a short declarative line per beat, the contradiction stated plainly ("Nothing broken, nothing forced… That was the problem"), and one reveal line per clip. Roughly 1 minute = 5 clips.
4. **Word budget per clip**: each video clip only fits a set number of narration words. Write the narration *per clip*, not as one essay ([CONOR]). Rule of thumb: about 2.3 words per second for a measured doc VO. For example, a 12 s clip gets 25-28 words. This rate is TITAN's assumption; verify it against the real VO length.
5. Under each video prompt, list the narration line that must sync to it. This makes the edit trivial ([DAVID]).
6. **Visual flow** ([CASH]): before writing shot prompts, give the chatbot your own sequence of actions (enter frame → look right → exit → car → road). If you let it invent the flow, the result is generic. Klaus's creative input goes here.

## 3. Style key: generate it first, before any character
[CONOR] This is the single most important consistency trick.
- Generate a **plain base mannequin** as a 3-panel sheet (front, back, face close-up) on GPT Image 2/2.5, 16:9, quality high, **4K**, because everything downstream inherits this detail.
- The mannequin is **not a character**. Its only job is to define the render language: surface, geometry, proportions, lighting, background.
- Every character prompt then = **the same paragraph pasted verbatim** + **one rewritten line** describing who this person is (build, clothing, 1-2 props).
- Result: head shape, lighting, background and view layout stay identical across the cast.

**Style-key prompt template (GPT Image 2.5, 16:9, high, 4K)**
```
Character turnaround sheet, three panels side by side on a seamless mid-grey (#808080) studio background:
[1] full-body front view, [2] full-body back view, [3] head-and-shoulders close-up of the face.
Subject: a featureless 3D mannequin figure, smooth matte clay-like surface with faint micro-texture,
simplified rounded head with no hair, subtle sculpted brow/nose/lips only, realistic adult proportions,
neutral A-pose. Render language: high-end 3D documentary animation, soft large key light from camera-left,
gentle fill, faint rim light, soft contact shadow under the feet, no environment, no text, no logos.
CHARACTER LINE: none (base style reference).
```
**Character variant**: paste the identical paragraph and replace only `CHARACTER LINE:` with the person. Example:
`CHARACTER LINE: a broad, heavy-set security guard in plain black uniform, stylised utility belt, peaked cap, black sunglasses.`
Keep contrasts readable: [CONOR] made the guard big and dark and the manager thin in a monochrome suit with clear glasses, so silhouettes tell the characters apart.

**Background colour**: use mid-grey, not white. A white sheet bleeds overexposure into later generations ([DAN-ADV], credited to filmmaker "Joey"; also [HF-DIR] below).

## 4. Locations: a shared grade block holds consistency
[CONOR]
- Same model and settings as the characters. Only the prompt changes.
- **Every location prompt carries one identical GRADE block.** Example: "Whole image graded in two tones: steel blue for the scene, warm amber as the single motivated accent."
- Vary the **camera height/lens per location** deliberately, so the film has visual rhythm (for example: lobby low and wide, corridor at chest height on a medium lens).
- Give each room **one practical light source** (a desk lamp, a window shaft). Later, characters get lit by it.

```
GRADE (locked, paste in every location): Two-tone grade - steel blue dominates the scene, warm amber is the
only accent and is motivated by a visible practical source. Volumetric haze, deep but not crushed blacks,
3D documentary render language matching the style reference.
LOCATION: <room, time, architecture, 1 practical light source, camera height + lens, empty of people>.
```

## 5. Composite stills: put characters into plates
[CONOR] These are the frames the videos are built from. An empty plate (for example the establishing lobby) goes straight through as is.
- Upload **2 references**: image 1 = empty location plate, image 2 = character sheet.
- The prompt orders the model to **copy the plate exactly** (geometry, camera position, lighting) and insert the character.
- **Light the character with something already in the room** (amber backlight catching the shoulders, monitor glow on the face). A character who picks up the room's light looks like they belong in it.
- Scale for drama: a tiny figure in a vast foggy vault reads as "documentary".

```
Image 1 is the exact location plate: reproduce its geometry, camera position, lens, framing and lighting unchanged.
Image 2 is the character reference (use identity, build, clothing only; ignore its grey background).
Place the character <action/pose> at <position in frame>, scaled correctly to the room.
Light the character only with the room's existing sources: <amber backlight rims the shoulders / monitor glow on face>.
Keep the two-tone grade. No new props, no text.
```

## 6. Video: Seedance 2.5, written as labelled blocks
[CONOR] used Seedance 2.5 at 16:9 with the composite still pinned as first frame and the next location as a second reference, so the clip can **cut** into it. Durations ran 8-17 s per clip, about 1 minute total.
- **Write prompts in labelled blocks, not one paragraph.** Some blocks stay locked across every generation (STYLE, GRADE). Only SHOTS/ACTION change. Blocks give the model better context and let you fix one part without touching the rest ([CONOR]).
- Seedance invents coverage angles that were never in a reference while holding the look from the sheets. Let it, but end on the pinned frame or a planned move ([CONOR]).
- Clips come back with their own SFX. Keep the useful ones, such as the booming cut ([CONOR]).
- The official 4-part order is **asset mapping → one-sentence brief → timeline/shot order → global constraints**. Use whole-second continuous ranges (0-3, 3-7, 7-12) and match content density to duration ([SD-DOCS]).
- **Draft first** at 480p / draft mode, then re-render at 1080p (CLAUDE.md rule; [DAN-ADV] shows about 840 vs about 4,800 credits).

**Block template (Seedance 2.5 omni_reference)**
```
ASSETS: @Image1 = opening frame (composite still, use exactly). @Image2 = <next location plate>, used only for the
final cut destination. @Image3 = <character sheet>, identity/clothing only, ignore its background.
BRIEF: 3D documentary recreation, <subject> in <location>, tense investigative mood.
STYLE (locked): matte clay-mannequin 3D documentary render, no facial hair or skin pores, stylised but physically lit.
GRADE (locked): two-tone steel blue + motivated warm amber accent, volumetric haze.
SHOTS:
 0-4s  wide establishing, slow lateral dolly across <space>, nothing moves but dust in the light shafts.
 4-8s  medium, <character> <single clear action>, camera at chest height, slow push-in.
 8-11s insert close-up on <prop/clue>, rack focus from foreground to clue.
 11-12s hard cut to @Image2 (low wide), deep sub-bass boom on the cut.
SOUND: room tone, footsteps, distant HVAC hum; no music; no dialogue; no subtitles.
CONSTRAINTS: one character only, keep proportions and outfit identical to @Image3, no text, no morphing.
```

**Multi-shot chapters** ([CASH]): models cap at 8-15 s, so the chatbot splits the story into chapters. Each chapter = one multi-shot generation that uses the same character refs as ingredients. Generate chapter 1, pick the best, then move on. Label every download (`ch01_v3.mp4`), because unlabelled clips are hard to sort in the edit.

## 7. Voice-over
- ElevenLabs v3 inside Higgsfield's Audio tab ([CONOR] used the "Alistair" voice). Generate **one VO file per clip**, not one long file. That way the timing matches the word budget.
- In v3, inline tags such as `[whispers]` steer delivery ([CASH]). Set delivery mode to **Creative** for natural pauses and variation, batch 4, and pick the best take (kaye.creatives in the realism tutorial).
- Alternatives: Gemini TTS (narration style, no expressions needed for a serious doc) ([DAVID]). See voice-persona-audio.md for persona archetypes, and never clone a real person.

## 8. Music, SFX, edit, upscale
- Edit in CapCut/Premiere. Lay down **VO first**, each piece under its clip; SFX where they land; **one music bed across the whole film**, ducked under the voice ([CONOR], [CASH]).
- Leave deliberate **gaps between VO lines** and let the visuals breathe, because that builds suspense ([CASH]). Raise VO to about +7 dB relative to the bed in CapCut ([CASH]).
- Add **on-screen date/time cards** ("March 18, 1990") for the documentary feel ([CASH]). For a Singapore health doc, use the stat with its source citation instead.
- Mix in real archival screenshots (news headlines, papers) as montage ([CASH]). For TITAN, use licensed or own-source material only and cite it in SOURCES.md.
- Music: royalty-free from Pixabay or Mixkit, and **skip any track flagged with Content ID** ([CASH]). Prefer the `/sound` licensed flow.
- **Upscale the locked edit to 4K** (Topaz via Higgsfield Upscale) after export, since Seedance caps at 1080p ([CONOR]). Finishing order: deflicker/clean → upscale → grade match → grain/texture last ([VERSELY]).

## 9. Thumbnail + packaging
- The chatbot drafts 5 thumbnail concepts, which you render with the character refs attached so the cast stays consistent ([CASH]). Use the `higgsfield-youtube-thumbnail` skill for production.

## 10. Consistency checklist (QC before video spend)
- [ ] Base style-key sheet approved (Gate 4) and every character built from the same paragraph.
- [ ] Every location carries the identical GRADE block.
- [ ] Each composite still copies its plate exactly, and the character is lit by a source in the room.
- [ ] Every Seedance prompt has ASSETS mapped one-to-one, with exclusions ("ignore its background").
- [ ] Narration per clip fits its duration (word budget). Each video prompt lists its sync line.
- [ ] Draft at 480p passed `scripts/qc_frames.py` + contact sheet before the 1080p render.
- [ ] Facts and stats sourced in SOURCES.md. No SG-pack violations.

## Sources
- Creating with Conor, "How to Make 3D Documentary Videos with AI" - youtube.com/watch?v=DrsvFcPg8jY (prompt pack page creating-with-conor.kit.com/ea56987c72 is an email-gated opt-in; prompts not retrievable).
- Cash-Coach, "Create UNLIMITED 3D Documentary with AI | 100% FREE" - youtube.com/watch?v=Uofgx-ugrXc
- David AI, "GRATIS! Crea Documentales Largos de 20 Minutos con IA" - youtube.com/watch?v=Yf7T1VA83Gk
- Dan Kieft, "Master AI Filmmaking in 30 Minutes" - youtube.com/watch?v=e9ZupmL9BcM
- [HF-DIR] Higgsfield AI, "How To Prompt Like a Director…" - youtube.com/watch?v=kFKpcCHkuPI
- Seedance 2.5 Prompting Guide - docs.seedance.tv/en/seedance-2-5-prompting-guide
- Versely, "Grain, flare and vignette against the AI sheen" - versely.studio/blog/grain-flare-and-vignette-against-the-ai-sheen
