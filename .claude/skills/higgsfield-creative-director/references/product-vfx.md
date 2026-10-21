# Product VFX — assembly / exploded-view and other product reveals (image → video)
Researched 2026-10-21; link log in `research/sources-photo.md`. Still-image prompts (hand removal, relight, studio hero) are in `photo-effects.md` §6.

## Core principle: keyframes do the work, the motion prompt is a guardrail
Every reliable product reveal is **two (or more) approved stills + a first/last-frame video**. Without an end frame the video model invents both the destination geometry and the path (Masonry). The motion prompt is mostly a list of restrictions (Nim): identity lock → scene lock → ONE motion → failure bans → finish.

Higgsfield routing for start/end frames:
| Model | Call | When |
|---|---|---|
| Kling 3.0 first/last frame | `kling_o3_flf` (start + end image), 3-15 s, std draft → pro | default for assembly/explode — strong rigid-part interpolation |
| Seedance 2.5 | `generate_video` seedance_2_5 with first+last frame; draft 480p → 1080p, bitrate high | TITAN default stack; used by Somya Nayak (assembly) and Daniel Chiang (poster) |
| Minimax Hailuo 02 | 1080p, 6 s, start+end frame | what Daniel Chiang's original assembly reel used — use only with a stated reason |
| Kling single start frame | `kling3_0` + `start_image` | open-ended reveals (splash, orbit) where no end state is needed |
Always: same aspect ratio, framing, light and background in every keyframe (generate the end frame FROM the start frame as `image_references`). Draft cheapest first; QC the in-between with `scripts/qc_frames.py` contact sheet (look for parts appearing/disappearing mid-move).

---
## A. ASSEMBLY EFFECT (parts fly in and snap together) — src: IG DXt3ctpkepO (@danielchiang0620), prompts transcribed on-screen via vidIQ
Look: exploded parts float symmetrically along the product's main axis (shells, PCB, buttons, screws evenly spaced) on a dark teal/slate studio gradient with soft key + crisp rim → parts collapse inward along straight lines and lock in ~1-2 s, decelerating; camera static three-quarter; clean commercial grade.
1. **Shoot**: real product held by fingertips only, product unobstructed, plain background, 9:16.
2. **Hand removal** (`nano_banana_pro`, 9:16, 4K, photo in `image_references`) — creator's prompt (partly visible; completed as recon):
```
Remove only the two hands and all visible fingers from the photo. Everything else must stay exactly the same: the product's shape, colour, materials, label, logo, position, angle, lighting and background. Fill the areas where the hands were with a seamless continuation of the original background. The edit should be invisible and natural, with no blur patches, smudges, duplicated texture, or AI artifacts.
Result: a clean product photo of the [PRODUCT] floating in the same composition, with both hands completely removed.
```
3. **Exploded still** (`nano_banana_pro`, same settings, clean image as ref, **4 generations** → pick best):
```
Create a photorealistic exploded view of the [PRODUCT] shown in the reference image, where all components are cleanly disassembled and floating in mid-air, evenly spaced along one straight axis in a symmetrical arrangement, keeping the same camera angle, lighting and background. [Name 4-6 believable parts: e.g. cap, pump mechanism, inner tube, bottle body, label sleeve, base.]
Only the [PRODUCT] separates cleanly into parts. Do not add hands, arms, extra objects, labels, text, wires, or unrealistic components.
Photorealistic product photography style, seamless, no distortion, no warped parts, no messy artifacts.
```
4. **Video**: START = exploded still, END = clean assembled still (Daniel used the original unedited photo as end frame — the hand then "catches" it; use the clean one for a floating finish). 6 s, 1080p final. Motion prompt (verbatim tail + recon head):
```
The floating components move smoothly inward along straight lines and click together into the fully assembled [PRODUCT], decelerating into the final lock, with no warping, no morphing, and no distortion at any point. No new parts appear, no parts disappear, and no duplication. No rotations should occur. The camera angle, floating position, lighting, and background remain completely unchanged. Motion is clean, realistic, and cinematic, like a precision engineering assembly. End exactly on the fully assembled [PRODUCT] matching the final image. Do not change the lighting or background. No changes in lighting.
```
SFX (post): soft whoosh-in, staggered mechanical clicks on each lock, final low "thunk". 

## B. EXPLODED-VIEW REVEAL (assembled → apart) — src: masonry.so guide + YouTube tir7IcqEJ8k (Gaurav Bisen), somyanayak.com, sume.com
Exploded still (Masonry, Nano Banana 2/Pro):
```
Create a conceptual exploded-view marketing image from this product photo. Preserve the exact exterior shell, camera angle, lighting, background, logo, and visible details. Separate the product into five to eight broad, visually plausible layers along one straight axis with even spacing. Keep every layer parallel and aligned to the original body. Preserve the support or hand without changing its anatomy. Do not add labels, callouts, extra objects, loose debris, or technical claims. This is a concept visual, not an engineering diagram.
```
Text-to-image matched pair (Somya Nayak — the two prompts are identical except the state, which keeps the in-between clean):
```
START: High-end studio product photograph of [PRODUCT], fully assembled and intact, floating dead centre against a seamless matte [BACKGROUND COLOUR] studio background. Straight-on view, perfectly level camera, soft even studio lighting, one subtle soft shadow directly beneath the product, photorealistic, ultra sharp, high detail. Keep the product small enough in frame that there is generous empty space on every side. No text, no watermark, no hands, no props, no brand logos. [Aspect].
END: High-end studio product photograph of the same [PRODUCT] as a clean exploded view: the outer shell or casing lifted apart and every major part and layer separated and floating in an organised, evenly spaced arrangement along one axis, like a technical teardown render. Same straight-on view, same perfectly level camera, same soft even studio lighting, same seamless matte [BACKGROUND COLOUR] studio background, one subtle soft shadow beneath. The core body of the product stays in the exact centre at the same size, with the parts spreading outward around it. Photorealistic, ultra sharp, high detail. No text, no watermark, no hands, no props, no brand logos. [Aspect].
```
(For real packaging, feed the real product photo as reference for START, then START as reference for END.)
Motion prompt — Kling (Masonry, 5 s, locked camera):
```
Five-second locked-camera product reveal. Hold the fully assembled product unchanged for the first second. From one to four seconds, separate the visible layers smoothly along one straight axis until they match the supplied exploded end frame. All layers remain parallel, evenly spaced, and aligned; motion uses gentle ease-in and ease-out with no rotation, duplication, morphing, or new components. The hand, background, lighting, logo, camera angle, and exterior shell remain completely still. Hold the final exploded arrangement for the last second. No camera movement. Audio: one restrained mechanical separation sound and quiet room tone.
```
Motion prompt — Seedance short (Somya): `The product slowly comes apart into an exploded view: the casing separates and the internal parts spread outward smoothly and evenly. Camera locked in place, background unchanged, no cuts.`
Timing default: 1 s hold → 3 s separation → 1 s settle (5 s).

## C. EXPLODE → REASSEMBLE LOOP
- Option 1 (cleanest): render B (assembled→exploded) then A-style reverse clip (exploded→assembled), join in edit; seamless loop for Reels.
- Option 2 single clip (Nim): `Keep the exact product shown in the input image. Preserve the same camera angle, framing, perspective, lighting, background, composition, and visible hand position. Separate the product into evenly spaced components that move straight outward in a symmetric arrangement, then reassemble smoothly into the exact original product. No rotation, wobble, distortion, duplication, morphing, or camera movement. Keep all proportions realistic and keep the final frame identical to the input image.` (start = end = same still).
- Or simply reverse the B clip in post (free).

## D. MULTI-KEYFRAME PRODUCT STORY (chain of first/last-frame clips) — src: aitoolsforkids.com Kling 2.6 + NB Pro case study
Make 5 matched 9:16 stills, then 4 clips where each clip's end frame = next clip's start frame:
| Clip | Start → End | Prompt |
|---|---|---|
| 1 | hero floating product → extreme macro detail (e.g. cap/texture) | "Smooth cinematic zoom in onto the [detail]." |
| 2 | macro → exploded diagram | "Cinematic smooth explosion of the [product] into the diagram." |
| 3 | exploded → reassembled at new diagonal angle | "The [product] reassembles itself smoothly and the camera arcs out to reveal the completed product." |
| 4 | reassembled → in Klaus's hand / on clinic counter | "The [product] floats down into his hand." |
Lessons: say "no labels or annotations" explicitly on exploded stills; regenerate any odd-ratio still to the shared ratio before animating.

## E. POSTER BREAK-OUT ANIMATION — src: IG DcQ2IiJTDLj (@danielchiang0620; settings transcribed via vidIQ)
1. Poster still: Higgsfield **Layers** — full-body photo of Klaus + style reference → action movie-poster with bold headline (gpt_image_2_5 works too: quote exact title).
2. Layer Decomposition (1K, Standard, 8 layers) → edit one layer (e.g. prompt `Replace to a cool sunglasses` on the phone layer) → flatten/export.
3. Seedance 2.5, 1080p, 16:9, 6 s, bitrate high. Prompt (recon around the visible on-screen arrows):
```
Framed poster stands on the LEFT in a pure white digital studio space with soft floor shadows. 0-2s: the hero leaps out of the 2D poster into the 3D white space -> human now in the foreground. 2-4s: mid-air, the [sunglasses] fly in and are caught and worn. 4-6s: lands on the white floor to the right of the poster and settles into a final dynamic hero pose; slow push-in. The complete original poster remains visible on LEFT and unchanged, typography static. Same face and outfit throughout. Duration: 6 seconds. Aspect ratio matching the source poster.
```
TITAN use: Physio Spot "hero" poster where Klaus steps out holding a foam roller; TITAN.AI launch poster.

## F. STYLISED CHARACTER / OBJECT TRANSFORMS
- **Pixel-art from two photos** (IG DetquOiI5AD, @raoulvanmullem): NB 2.1 turns a person photo + an object photo (car) into pixel-art **character reference sheets** (front/side/back) → video model (Wan 3.0 in the post; for TITAN use `kling_o3_image_reference` or Seedance omni_reference) with a viral reference clip + the sheets to recreate the motion in pixel style. Sheet prompt (recon): `Turn the person in image 1 into a 16-bit pixel-art game character reference sheet: front, side and back views, idle pose, limited palette, crisp pixel edges, same hair/outfit colours, white background, no text.`
- **Minecraft / voxel food** (IG DeubOShqafl, @skaigenerated — caption only, reel not watchable; recon): still `Turn this [protein shake / meal] into a Minecraft-style voxel version: every element built from small cubes, same composition and colours, blocky pixel textures, soft daylight, on the same table.` → video start = real photo, end = voxel still: `The [meal] breaks into small cubes that rebuild it block by block into the voxel version; camera slow orbit 20°; satisfying pop sounds.` Good Power Protein hook.

## G. OTHER PRODUCT REVEALS (TITAN templates — not from a single source; built on the guardrail structure above)
| Effect | Keyframes | Motion prompt core | Camera |
|---|---|---|---|
| Levitation spin | start: product on plinth | "product lifts 10 cm, rotates one slow 360° on its vertical axis, settles back; label stays legible and undistorted" | locked or slow push-in |
| Ingredient orbit (Power Protein) | start: tub hero; end: tub with whey powder cloud, oats, berries orbiting | "ingredients drift in and orbit the tub in one smooth ring, then settle; tub unchanged" | slow 15° arc |
| Liquid splash | start: shaker bottle | "milk/protein splash erupts around the bottle in slow motion, freezes mid-air, droplets crisp" | locked, macro |
| Lid-lift unboxing | start: closed box; end: open box, product rising | "lid lifts off upward, product rises out with soft light spill from inside" | slight top-down tilt |
| Packaging dissolve to device | start: boxed device (heal360); end: device on clinic table | "box panels fold away and dissolve into light particles revealing the device in place" | push-in |
| Material transform | start: product in matte; end: same in chrome/glass | "surface material morphs smoothly from matte to polished chrome, shape fixed" | locked |
Camera vocabulary both Kling and Seedance parse: static tripod/locked-off, slow push-in, dolly out, 15-30° orbit/arc, top-down tilt, macro rack focus. Keep the camera **locked** for assembly/explode (moving parts already carry the energy); add camera moves only in A→B transitions between clips.

## H. Scroll-linked web sequence (bonus) — src: somyanayak.com
Render B with a locked camera → extract frames at 30 fps (Frames Extractor / ffmpeg `-vf fps=30`) → Claude Code builds a GSAP ScrollTrigger canvas sequence (pinned canvas, preload all frames, reduced-motion fallback to first/last frame). Good for TITAN.AI / product landing pages.

---
## Failure → fix (change one variable at a time)
| Failure | Fix |
|---|---|
| Parts spin / tumble | add "no rotation, parts move straight along one axis"; shorten duration |
| New or missing parts mid-move | tighten end frame (fewer, broader parts: 4-6); "no new parts appear, no parts disappear" |
| Logo/label warps | keep label face square to camera; regenerate end frame with label visible; reject and re-roll |
| Background/lighting shifts | repeat "background, lighting and camera completely unchanged" in prompt; same seed |
| Clip doesn't settle | ask for 1 s hold at start and end |
| Hand anatomy breaks | remove hand entirely (A step 2) or keep it fully static |

## Compliance & honesty
- Exploded views of products are **concepts**: invented internals are not a teardown (Masonry, Sume). Never imply a device's internal technology, mechanism or clinical effect that isn't verified — especially heal360/Physio Spot devices and supplements (SG health ad rules: no efficacy superlatives). If real internals matter, render the exploded still from CAD and let AI do only the motion.
- Real packaging must match the real product (label spelling, claims on pack). Don't generate new on-pack claims.
- QC: first and last frames match approved stills; parts move on one readable axis; no extra/missing parts; label legible; motion settles before the end.
