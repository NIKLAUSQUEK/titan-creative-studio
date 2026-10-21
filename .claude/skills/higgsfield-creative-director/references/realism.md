# Realism checklist: photo + video

Load this whenever the brief says "make it look real", for photoreal ads, UGC, documentary inserts, and Klaus/staff-based shots. Run the pre-prompt checklist, write with the vocabulary, then QC against section 6.

Tags: [DAN-REAL] Dan Kieft "Realistic AI Videos with Seedance 2.5" · [KAYE] kaye.creatives "Perfect AI Realism First Try" · [DAN-ADV] Dan Kieft advanced course · [HF-DIR] Higgsfield director tutorial · [SD-DOCS] Seedance 2.5 guide · [SHOTCRAFT] Shotcraft defects · [VERSELY] Versely finishing · [MEDIAIO] media.io realism guide · [WONDER] WonderLens realism.

---

## 1. Core principle
- **Real footage is defined by its errors, not its sharpness.** Generated frames are evenly lit, clean in the shadows and sharp to the edges. No camera produces that ([VERSELY]). Generic "realistic, cinematic" prompting returns the statistical average, which looks like AI ([WONDER]).
- **Realism hierarchy** ([MEDIAIO]): 1 believable action/physics → 2 stable identity and geometry → 3 coherent camera/light/material → 4 human timing and sound → 5 resolution and grain. Fix the higher tiers first.
- **Perfect the still before animating.** "99% of the effort on the stills": a flawless base frame means the video doesn't glitch ([KAYE]; also Runware: iterate a hero still, then animate).
- **Imperfect is more real.** Deliberately lower resolution or compression for phone/camcorder looks ([DAN-REAL]: 1K output on purpose). The Seedance 480p draft can itself read *more* real for found-footage styles ([DAN-REAL]).

## 2. Model notes (October 2026, per sources)
| Job | Pick | Notes |
|---|---|---|
| Realistic stills | **Test several models every time**, since stills are cheap | [DAN-REAL] ran 6 models per prompt. GPT Image 2.5 "Flare" often best; Flux 2.0 Pro still excellent for photographic realism (weak on text); Nano Banana Pro sometimes beats 2.1; Seedream 5.0 Pro good; Soul 2 gives an iPhone-sunrise candid look; Flux 3 looked plastic. |
| Ultra-real human character sheets | Seedream 5.0 Pro ([KAYE]) or GPT Image 2/2.5 high ([DAN-ADV]) | Mid-grey background. Fix over-smooth skin with a Seedream 5 Pro edit ([HF-DIR]). |
| Locations / wide architecture | Soul Cinema / Soul 2 | Fast, cheap, cinematic ([KAYE], [HF-DIR]) |
| Realistic video | **Seedance 2.5** (top). Flux 3 video gets about 80-90% of that for far less ([DAN-REAL]) | MiniMax H3 Max was much worse with no references. Kling 4 is untested by Dan; it first looked less real to him. |
| Plastic / toy objects (LEGO) | Seedream 5.0 Pro ([KAYE]) | Micro-reflections, studs |
"There is no best model. Models are paintbrushes" ([KAYE]). Draft at 480p, verify, then go to 1080p, which hits first try when the draft was verified ([KAYE]).

## 3. Still prompt formula: CTLT (Camera · Tone · Lighting · Texture) + subject
From [DAN-REAL]. Order: **Camera → Tone → Subject/action/place → Lighting → Texture.**
```
CAMERA: candid 35mm film photograph, 12mm fisheye, slightly elevated side view, wide full-body framing,
        tilted horizon, slight motion blur.
TONE: frantic, absurd, darkly comic - an unexpected moment caught by a passer-by.
SUBJECT: <who> <doing what> <where, when>.
LIGHTING: harsh direct on-camera flash on the subject, background falls to ambient sodium streetlight.
TEXTURE: <material detail that interacts with the scene: matte, glossy, frayed, wet, dust, sweat>.
```
**Capture-style presets** (swap the CAMERA + TONE lines; [DAN-REAL] "7 ways to capture an idea"):
- *Phone snapshot*: smartphone photo, deep focus, HDR-flat tones, slight computational sharpening, mild noise in the shadows (also opendirector camera list).
- *iPhone selfie*: arm's-length front camera, slight wide-angle distortion, face off-centre, uneven window light.
- *Disposable camera + flash*: on-camera flash falloff, red-orange date stamp, slight vignette, warm cast, grain.
- *Low-quality camcorder*: 4:3, interlaced softness, compression blocking, blown highlights, timestamp OSD, low resolution on purpose.
- *Skate photo*: very low curbside angle, 12mm fisheye, crooked, visible film grain.
- *Intimate documentary*: 50mm, available light, shallow focus, subject unaware of camera.
- *Concealed observation*: long lens through foreground foliage or glass, partly occluded, voyeuristic.
- *Motion-blur photo dump*: slow shutter, smeared movement, flash-freeze on the subject.
Turn any winning image + prompt into a reusable style `.md` (ask Claude to "turn this camera style into a reusable markdown file") ([DAN-REAL]).

## 4. Vocabulary
**Camera / lens**: 24mm/35mm/50mm/85mm/135mm, anamorphic (oval bokeh, horizontal flare), fisheye, macro, tilt-shift; shallow vs deep focus; f/1.8 bokeh; eye-level / low / high / overhead; Dutch tilt; locked-off tripod vs handheld breathing.
**Light (always name ONE motivated source)**: window key, practical lamp, on-camera flash, overcast soft, hard noon sun, golden hour backlight, sodium streetlight, fluorescent office flicker, monitor glow, neon spill, bounce from a white wall; rim/kicker; negative fill.
**Texture**: skin pores, fine vellus hair, slight redness around the nose, under-eye texture, sweat sheen, fabric weave and pilling, wrinkles at the elbows, dust motes, fingerprints on glass, chipped paint, scuffed floor.
**Sensor / lens errors** ([VERSELY], [WONDER]): fine monochrome grain mostly in the shadows, 16mm/35mm film grain, gentle lens vignette, corner softness, slight chromatic aberration at the edges, motivated flare only, shutter-correct motion blur, slight focus breathing.
**Video realism moves** ([DAN-REAL]; make it look like a human filmed it):
| Move | Prompt it as |
|---|---|
| Handheld | small natural shakes, camera reacts to the action |
| Crash zoom | sudden fast zoom-in as if surprised by the event |
| Voyeuristic | partly hidden viewpoint, as if the moment shouldn't be filmed |
| Whip pan | quick turn toward an unexpected event |
| Walking backwards | operator walks backward with uneven step bob |
| Frame block | a passer-by crosses close to the lens, briefly blocking the frame |
| Exposure adjust | auto-exposure hunts when moving from indoors to bright outdoors |
| Focus hunt | autofocus struggles, breathes, then locks |
Combine 2-3 per clip (Dan's "office" clip). Seedance accepts standard terms directly. For unusual ones, describe what the viewer sees ([SD-DOCS]).

## 5. What breaks realism (avoid it or prompt it out)
- **Morphing / identity drift**: faces, clothes and props change. Fix: refs with roles, a preservation clause, the lead at @Image1 ([SD-DOCS], [MEDIAIO]).
- **Floaty motion / no weight**: feet slide, nothing makes contact. Fix: describe contact and weight transfer ("heel strikes, weight shifts, cup rocks when set down") ([MEDIAIO]).
- **Plastic skin / over-smoothing**: from the source image or an upscaler. Fix: texture terms, a Seedream edit, careful upscaling ([HF-DIR], [VERSELY]).
- **Unnamed camera drift** or two competing moves ([SHOTCRAFT]). Name one move, or "locked-off, no movement".
- **Slideshow**: only the camera moves. Give every shot a subject action ([SHOTCRAFT]).
- **Abrupt end**: describe the end state and "settle and hold" ([SHOTCRAFT]).
- **Even, sourceless lighting** and perfect focus everywhere ([VERSELY]).
- **Unmotivated flare / sticker grain**, or grain that differs between cuts ([VERSELY]).
- **Audio mismatch**: wrong room size or mic distance. Footsteps and cloth sell weight ([MEDIAIO]).
- **Wrong eye line / uncanny stare** ([LARRY] in filmmaking-longform.md). Overacting: specify restraint and micro-behaviour.
- **Text, UI, screens**: shoot the real phone and composite ([DAN-ADV]).
- **Low contrast idea**: realism alone doesn't stop the scroll. Add **contrast levels**: L1 subject in an unexpected place, L2 + unexpected styling/attitude, L3 + feeling ([DAN-REAL]). Keep this brand-safe for TITAN.

## 6. Realism QC (run on the contact sheet from `scripts/qc_frames.py`)
- [ ] One visible motivated light source; shadows agree with it in every frame
- [ ] Skin and material texture present at 100% crop; no waxy skin
- [ ] Identity stable first frame to last (face, hair, wardrobe, props, logo)
- [ ] Hands and fingers count correctly; contact points (feet, hands on objects) hold
- [ ] Camera behaves like a real rig (one move, plausible speed, no passing through objects)
- [ ] Motion has weight and cause → effect; hair and cloth lag slightly
- [ ] No morph or flicker between frames; background geometry fixed
- [ ] Eye line correct; expressions restrained and timed
- [ ] Audio room/scale matches the image; no extra voices
- [ ] Across the cut: grade, black level and grain match between clips

## 7. Finishing order (after Klaus approves the draft)
([VERSELY]) 1 clean/deflicker → 2 upscale in steps (1080p → 4K; check a still at full size for invented detail) → 3 grade-match all clips to one reference → 4 texture LAST: fine monochrome grain, shallow vignette, motivated flare only, almost no chromatic aberration. Same texture on every clip. Generating at 24-30 fps flickers less than at 60 ([VERSELY]; [DAN-ADV] adds "24 fps" to the prompt).

## Sources
- Dan Kieft, "How I Make Realistic AI Videos with Seedance 2.5 - Full Guide" - youtube.com/watch?v=2hJsvDSPWYM
- kaye.creatives, "How I Get Perfect AI Realism on the First Try in 2026" - youtube.com/watch?v=w0R29uK3Hfk
- Dan Kieft, "Master AI Filmmaking in 30 Minutes" - youtube.com/watch?v=e9ZupmL9BcM
- Higgsfield AI, "How To Prompt Like a Director…" - youtube.com/watch?v=kFKpcCHkuPI
- Seedance 2.5 Prompting Guide - docs.seedance.tv/en/seedance-2-5-prompting-guide
- Shotcraft - shotcraft.video/reference/video-defects/ · Versely - versely.studio/blog/grain-flare-and-vignette-against-the-ai-sheen · media.io - media.io/video-tips/ai-video-looks-real.html · WonderLens - wonderlens.ai/blog/what-is-visual-realism-in-ai-videos-for-filmmakers · OpenDirector camera types - opendirector.co/learn/camera-types-for-ai-video/
