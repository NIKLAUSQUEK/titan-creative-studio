# Photo-effects prompt library (stills: relight, film looks, edits, viral trends, product)
Researched 2026-10-21. Sources per entry; full link log in `research/sources-photo.md`. Many viral posts gate the exact prompt behind "comment X" DMs — where the creator's prompt was not public, the template below is a **TITAN reconstruction** (marked "recon") built from the visible result (vidIQ watch) plus public prompt libraries. Video/product-motion effects live in `product-vfx.md`.

## 0. How to run any edit (read first)
**Golden rule (Zemith, OpenAI image guide, fal GPT Image 2 guide): say what to KEEP before what to CHANGE.** Image models redraw the whole frame; anything not locked drifts (face first).

Universal edit template (paste, fill brackets):
```
Using the uploaded photo as the reference, keep [the person's face, facial features, identity, skin tone, body shape, hairstyle, expression, outfit, pose, camera angle, crop, background objects] exactly the same. Do not slim, smooth, age or beautify the face. Change only this: [ONE change — light / grade / angle / background / outfit / style]. Photorealistic, natural skin texture with pores, no extra people, no text, no watermark, no distorted hands.
```
Rules: one change per pass (outfit, then background, then grade); name features, not "keep my face"; if the face drifts reply "the face changed — keep the face exactly as in the reference and redo". Multi-image prompts: refer to "image 1 / image 2" in upload order.

**Edit-from-reference flow in Higgsfield (`generate_image`):**
| Need | Model | How |
|---|---|---|
| Faithful edit of a real photo (Klaus, staff, clinic, product) | `nano_banana_pro` (2k/4k) or `nano_banana_2_1` | put the photo in `image_references`; prompt = template above; same aspect ratio as source unless reframing |
| Edit + exact on-image text, posters, covers, UI mockups | `gpt_image_2_5` | photo in `image_references`; quote exact copy in "double quotes" with placement; `quality: low` draft → `high/max` final |
| Masked/local fix (remove one object, fix a hand) | `nano_banana_2` / `seedream_v5_pro` with mask | smaller region = less identity drift |
| Pure relight of an existing still/clip with a light gimbal | Higgsfield **Relight** app (`relight_image`, or Apps → Relight for video) | direction preset + soft/hard + brightness + colour + optional prompt (§1) |
| Same face across many stills | Soul ID (`text2image_soul_v2`) or an Element `<<<id>>>` | never for real people without consent |
Cost discipline (CLAUDE.md): draft at lowest quality → QC contact sheet → Klaus approves → re-render high. Real photos of real staff beat generated ones. No AI likeness of real people who haven't consented; never "make me look like <celebrity>".

**Slash "codes" are not ChatGPT commands** — they are shorthand the model interprets (Arjav Jain, DesignPrompting). In Higgsfield, expand them to full sentences (below). Optional chat primer (John Savage PDF): *"From now on, when I upload a photo and type a /code, re-shoot the SAME photo in the style the code describes. Keep the same person (face, hair, skin tone, body), outfit and place unless the code changes them. Photorealistic, natural skin texture, no text or watermarks. Only change what the code asks for."*

---
## 1. Relighting / lighting effects
Describe light in this order (QuestStudio): **source → direction → quality (soft/hard) → balance (fill/contrast) → colour**. Name patterns (Rembrandt, butterfly, rim) — models know them.

**1.1 Higgsfield Relight app (video or still)** — src: YouTube 4EV2HRZTPuY (Higgsfield Relight demo), IG DcqabXsiM3o (@declann golden hour).
UI: Upload media → Quick select direction (Top/Front/Right/Left/Back/Bottom or drag the sphere) → Soft | Hard → Brightness % → Colour hex → (optional) Preset + Prompt.
Golden-hour recipe (Declann): Preset **Contre Jour** → Custom: light directly behind (backlit) or in front of subject → Colour orange/`#FFD800`, Brightness 100%, Diffusion 10% → prompt:
```
Transform the entire scene into a dramatic, photorealistic golden hour environment. Replace the existing sky with a rich golden sunset sky filled with warm amber, orange and soft yellow tones.
Create strong directional sunlight coming from a low angle, blasting naturally across the scene. The sunlight should interact with the buildings and structures to create beautiful streaks and geometric patches of golden light.
Preserve the original composition, perspective, subjects, objects and structural details exactly. Do not add or remove anything from the scene. Only transform the sky, lighting, shadows, reflections and overall atmosphere.
Make the final result look like it was originally photographed during golden hour with a high-end cinema camera, featuring realistic lens flare, natural light wrap, and rich color depth throughout the entire image.
```
(verbatim, transcribed on-screen via vidIQ). TITAN use: rescue grey Singapore-monsoon B-roll of the clinic exterior; Hard + warm back = hero; Soft + front = natural fill on Klaus's talking head.

**1.2 Identity-safe portrait relight (Nano Banana Pro / GPT Image)** — src: QuestStudio cheatsheet.
```
Edit the uploaded photo only. Preserve the person's recognizable identity, facial proportions, expression, skin tone, hair, clothing, pose, camera angle, crop, and background objects. Change only the lighting: add one large diffused key light 45 degrees camera-left and slightly above eye level, restrained fill from camera-right, natural catchlights, controlled skin highlights, soft-edged shadows, and gentle falloff into the background. Keep the result photographic and unretouched; do not reshape the face or replace scene details.
```
Swap the bold light clause for any of these (sources: Morphed, PhotoWorkout, Chase Jarvis, Imgstyler, nanobananapro.photo):
| Look | Light clause | TITAN use |
|---|---|---|
| Golden-hour rim | "relight so it is sunset, low warm sun behind the subject camera-right as rim light on hair and shoulders, soft sky fill on the face, restrained flare, natural skin tone" | warm founder/lifestyle |
| Rembrandt | "single key light high from upper-left, triangle of light on the shadow-side cheek, deep shadows on the right, warm rim from behind right, cinematic, background unchanged" | serious men's-health talk, doc tone |
| Low-key rim (athlete) | "dark studio, strong rim light behind subject, clean edge highlights on shoulders and arms, minimal spill, subtle haze, moody contrast" | PeachForm / Power Protein athlete |
| Soft window | "soft window light from the left, natural indoor fill, gradual shadow transition, warm colour temperature" | clinic consult room, trust |
| Fix harsh midday | "soften harsh midday light, gentle ambient fill, reduce contrast, remove hard shadows under eyes and chin" | phone shots from outdoor events |
| Clean high-key | "high-key white studio, large frontal soft key, balanced fill both sides, background one stop brighter, clean whites without clipped skin" | heal360 wellness |
| Neon two-colour | "neon signs casting magenta and cyan light, coloured rim, soft bloom, wet reflections, realistic skin tones, max two colours" | night/edgy hooks |
| Butterfly beauty | "butterfly lighting from directly above camera, soft shadow under nose and chin, pure white sweep" | headshots |
| Studio backdrop swap + match | "replace background with a mottled charcoal-grey canvas backdrop; relight subject to match: softbox 45° camera-left, subtle fill right, soft falloff" | staff headshots, consistent set |
Tips: work from the highest-res source (4K gives the model more geometry — Chase Jarvis); "too flat → reduce fill, add rim; too harsh → more diffusion, softer wrap". Check eye colour, face shape and shadow direction against the original at the same size.

**1.3 Product relight** — src: QuestStudio.
```
Relight the uploaded product photo without changing the product shape, label, logo, color, camera angle, crop, or background layout. Use a broad softbox key from upper-left, a subtle white-card fill from the right, a clean contact shadow, restrained edge highlights, and reflections that follow the material. Change illumination only; preserve all approved packaging details.
```

**1.4 "Shadow Lift" (recon)** — src: @skaigenerated Deq7GWciiv5 (Nano Banana 2; prompt gated, carousel not watchable). Likely the shadow-recovery / dappled-light portrait trend:
```
Using the uploaded photo as the reference, keep the person, face, pose, outfit and composition exactly the same. Lift the crushed shadows and recover detail in the dark areas of the face and clothing, balance exposure like a professional raw edit, then add soft dappled sunlight through leaves falling across the face and shoulders with crisp natural shadow shapes. Warm natural skin tones, no HDR halo, photorealistic.
```
Split into two passes if it over-cooks (exposure fix first, then dappled shadows).

---
## 2. Colour filters & film / camera looks
All as edits of an uploaded photo; prepend the keep-clause from §0. Before→after descriptions from vidIQ watches of IG DeG80_sTYnY (@sherlynheon, ChatGPT) unless noted.
| Code | Prompt (change clause) | Source |
|---|---|---|
| /ccd | "Restyle into an early-2000s CCD compact digital camera photo: saturated punchy colours, rich blues and greens, high contrast, harsh direct sunlight, visible digital noise, slight JPEG softness, orange retro date stamp 'OCT 5 2026' in the bottom-left corner." | DeG80 |
| /ricohflash | "Re-shoot as a Ricoh GR street photo with hard direct on-camera flash: bright specular highlights on skin and fabric, fast exposure falloff into deep dark background, crisp micro-contrast, slight wide-angle 28mm feel." | DeG80 |
| /goldenhour | "Golden-hour sunset: replace the sky with orange-pink clouds, brilliant sunburst backlight through background foliage, warm golden rim on hair and skin, elevated contrast." | DeG80 |
| /disposableflash | "Grainy point-and-shoot disposable camera flash, party-snapshot look, slight vignette, warm cast." | John Savage PDF |
| /35mmfilm | "35mm film photograph: natural grain, softer contrast, slight halation on highlights, true-to-film colour." | Arjav Jain |
| Expired film | "Expired colour film: muted greens, warm yellowed highlights, visible grain, slight old-lens blur, soft white printed border." | Zemith #17 |
| 1970s snapshot | "Warm consumer film, faded orange-brown tones, soft edges, small light leak in one corner." | Zemith #2 |
| /polaroid | "Instant-film colour, soft contrast, slight lens character, clean white border." | leadwithzoe presets |
| /noir | "Sculpted monochrome, deep blacks, luminous highlights, classic hard side light." | leadwithzoe |
| /cinematic | "Controlled contrast, teal-and-orange colour separation, dimensional light, subtle film grain, 2.39 framing feel." | leadwithzoe |
| iPhone blurry / motion blur (recon) | "Re-shoot as an ordinary iPhone photo taken mid-movement: slight motion blur from hand shake, subject softly smeared but recognisable, light streaks from lamps, mild overexposure, uneven mixed lighting, digital sensor noise, typical iPhone warm colour science, awkward casual framing. Keep face, outfit and setting." | @skaigenerated DeuZwBDqKT9 (Gemini; prompt gated, reel not watchable) + PromptHero/SweetPrompt "mediocre iPhone selfie" prompts |
| Flash selfie at night | "Standard iPhone selfie with the flash, casual rough snapshot, slight motion blur, somewhat overexposed, awkward angle, as if taken pulling the phone from a pocket. Do not alter the face." | PromptHero d998d037392 |
TITAN note: the "anti-polish" iPhone/CCD/flash looks are the native UGC texture for Physio Spot hooks — they read as real, not ad. Still: never use them to fake a patient photo or testimonial (SG health ad rules).

---
## 3. Camera "re-shoot" codes (same photo, new lens/angle/shutter)
Src: IG DeSJCWHDF-d (@charliehills; looks verified by vidIQ) + charliehills.substack "22 photo commands"; IG Dd6k910Ch6n (@skaigenerated "camera-angle cheat codes", carousel — caption only). Tip from Charlie: fill the frame with the subject, plain even light, send the code alone, re-run if the face drifts.
| Code | Expanded change clause |
|---|---|
| /fisheye /wormseye | "Extreme low-angle worm's-eye view through an ultra-wide fisheye lens, curved barrel distortion, ceiling/sky geometry towering above." |
| /fisheye (selfie) | "Extreme fisheye, circular barrel distortion, subtle black corner vignette, expanded field of view, original lighting kept." (DeG80) |
| /panning /motionblur /slowshutter | "Subject mid-stride and sharp; background streaked horizontally from a slow-shutter camera pan." |
| /zoomburst /longexposure | "Radial zoom-burst streaks exploding outward from the centre, subject stays in focus." |
| /topdown /overhead /90degrees | "Direct 90° overhead view looking straight down at the subject, floor pattern and shadows visible." |
| /crowdblur /longexposure /tripod | "Tripod long exposure: ghostly motion-blurred pedestrians stream past; subject perfectly still and sharp." |
| /multipleexposure /incamera | "In-camera multiple exposure: 3 translucent overlapping copies of the subject in different head angles, room unchanged." |
| /tinyplanet | "360° stereographic tiny-planet projection, ground wrapped into a sphere beneath the subject." |
| /droneview | "High aerial drone view from above, subject small in the scene." |
| /0.5selfie | "0.5x ultra-wide arm's-length selfie, exaggerated near-hand perspective." |
| /85mm /f1.4 /shallowdof | "85mm portrait lens at f/1.4, tighter crop, creamy background blur." |
| /telephoto /200mm | "Long lens from far away, compressed background pulled close." |
| back view / speed shot | "Same person seen from behind, walking away" / "speed shot: subject sharp, environment streaked with forward motion." (Dd6k910Ch6n caption) |
Stack max two codes (e.g. /droneview /goldenhour). TITAN use: one real Klaus photo → 6 angle variants = instant carousel or B-roll start frames for Seedance.

---
## 4. Photo-edit transforms
Prepend §0 keep-clause to each.
- **Remove people** (DeG80): "Seamlessly remove all background people, pedestrians and tourists; rebuild the stairs and architecture behind them; subject and foreground untouched; identical exposure and white balance." Use mask on Nano Banana 2 for precision.
- **Remove one object** (TechPilot): "Remove [the person in the red jacket on the right] and fill the area with [the beach behind them]. Change only that area. Keep everything else exactly the same, including lighting."
- **Restore old photo** (Limor Markman /PhotoRestore): "Restore this old photo: repair tears, scratches, dust and fading; recover natural contrast; keep faces, expressions and clothing exactly as they are; no colourising unless asked; no beautifying."
- **Enhance / /hdreal**: "Sharpen and clean this low-resolution photo to high-definition, recover fine detail, reduce noise, keep everything identical." (or `upscale_image`)
- **Background swap** (Morphed): "Replace background with [deep black seamless studio], dramatic rim lighting separating subject from background, clean edge separation" / "[golden-hour beach], warm backlight on subject, natural environmental integration, soft horizon". Always relight the subject to match the new background.
- **Outfit swap**: "Change only the outfit to [navy blazer over a plain white tee]; keep body shape, pose, hands, face and background exactly the same; realistic fabric folds and fit." One garment per pass.
- **Professional headshot** (Zemith #9): "...don't slim, smooth or age the face. Plain light-grey studio background, soft even front light with gentle fill, navy blazer over a plain shirt, head-and-shoulders, centred, eye-level camera, natural skin texture, no retouching beyond tidy hair."
- **Speaker/author photo** (Zemith #11): dark softly-lit background with warm gradient, single soft side key, half-length, empty space on one side for text.
- **Natural retouch** (Imgstyler): "Retouch like a professional photo editor: correct underexposure, neutral white balance, reduce temporary blemishes and under-eye shadows slightly, keep real skin texture and pores. No plastic skin, no face reshaping, no makeup changes."
- **Style transfer** (Zemith #4-8): 1920s B&W silver-gelatin · 1980s yearbook · 1990s mall glamour · hand-drawn anime film still · watercolour · 3D animated movie character · classical oil portrait. Pattern: "keep the person recognizable: same face shape, eyes, nose, hairstyle, skin tone, expression... Redraw/repaint as [style details + light]." Avoid naming living artists/studios in brand work.
- **Magazine cover** (Zemith #16, TikTok @fashionbyally): use `gpt_image_2_5`; "glossy fashion magazine cover, bold solid studio colour, crisp beauty light, masthead reading "[MADE-UP NAME]" top, two short cover lines down the side". Never real mastheads (Vogue etc.) — fashionbyally used a Picsart "Vogue" sticker; that is trademark use, not for client work.
- **Movie poster** (Zemith #19): orange-and-teal light, vast backdrop, dust, short made-up title at bottom, no other text.

---
## 5. Viral photo-effect trends (ready templates)
| Trend | Template | Source / notes |
|---|---|---|
| **Frame Break / IG pop-out** | `gpt_image_2_5` or NB Pro, photo in refs: "Photorealistic upper-body shot of the person in the reference (keep face, hair, outfit exactly). Subject is framed inside a centred white Instagram-style post border on a soft [colour matching outfit] background. Thin top/left/right borders; thicker bottom panel with heart, comment, share and bookmark icons, text "[1,204 likes]", username "[physiospot.sg]", caption "[caption]... more". 3D pop-out: head and arms physically break OVER the top and side borders, hands gripping the outer edges of the frame. Soft studio light casting real drop shadows from the frame and the protruding hands/head onto the flat background. Solid 3D figure, detailed fabric texture." Pose alts: blowing kiss / resting on bottom panel / arms reaching to lens in L-frame. | @skaigenerated Deq7nKICjKX (GPT Image 2; prompt gated) — template from BigPromptHub "Instagram Pop-Out" + YouMind "Screen Breakout" |
| **Background Sketch** (recon) | "Keep the person exactly as in the photo, fully photorealistic and in colour. Redraw ONLY the background as a loose graphite pencil sketch on off-white paper, same layout and perspective, visible hatching and construction lines; the boundary where the real person meets the sketch is clean, with the person casting a soft real shadow onto the drawn ground." Variant (trompe-l'oeil): sketchbook on a desk with the person drawn in graphite while a real hand with a pencil draws them. | @skaigenerated DeuXGRkiiUx (prompt gated) + gptimgprompts "Trompe L'oeil Sketchbook" |
| **Loading Me** (recon) | `gpt_image_2_5`: "Keep the person exactly as in the reference. The image is split vertically: the left [60%] is the finished photorealistic person; the right part dissolves into an unrendered state — grey 3D wireframe/clay, then pixel blocks, then empty transparency checkerboard. Overlay a sleek progress bar near the bottom reading "Loading [Klaus]... 60%". Clean studio light, 4:5." | @skaigenerated Del1RmKijNL (prompt gated). Fits TITAN.AI "building your body/AI" hooks |
| **Block Print poster** (recon) | `gpt_image_2_5`: "Turn the person in the photo into an editorial linocut / woodblock print poster: bold carved black lines, 2-3 flat ink colours [deep red, cream, black] on textured paper, slight ink mis-registration and paper grain, keep the face recognisable and the pose; bold headline "[TEXT]" set in hand-carved letterforms at the top." | @skaigenerated DeuXgJwihLh (prompt gated) |
| **Camera-angle cheat codes** | §3 table | Dd6k910Ch6n |
| **Action figure in blister pack** | Zemith #18: figure keeps face/outfit at toy scale, 3 accessories in slots (e.g. foam roller, protein shaker, resistance band), name "[NAME]" printed on box, clean product light. | Zemith; good PeachForm/Physio merch gag |
| **Meeting younger self** | Zemith #20 (two refs: recent + childhood) | consent required |
| **Pixel / voxel character** | NB 2.1: turn subject photo + prop photo (e.g. car) into pixel-art character reference sheets → video (see product-vfx §F) | IG DetquOiI5AD (@raoulvanmullem) |
| **Minecraft / voxel food** | see product-vfx §F (reel not watchable; caption only) | @skaigenerated DeubOShqafl |
| **Poster animation** | still: hero poster with you as lead (Higgsfield Layers), video in product-vfx §E | IG DcQ2IiJTDLj (@danielchiang0620) |

---
## 6. Product shots (stills that feed product-vfx)
- **Hand removal → floating product** (Daniel Chiang assembly step 1, NB Pro 9:16 4K; recon of gated prompt): "Remove the fingers and hand holding the product completely. Keep the product's exact shape, colour, label text, logo, angle and lighting. The product now floats in mid-air in the same position with a soft natural shadow below; rebuild the background behind where the hand was."
- **Clean studio hero** (Somya Nayak): "High-end studio product photograph of [PRODUCT], fully assembled, floating dead centre against a seamless matte [COLOUR] background. Straight-on, perfectly level camera, soft even studio light, one subtle soft shadow directly beneath, photorealistic, ultra sharp. Generous empty space on every side. No text, no hands, no props." (Use the real product photo as reference so packaging stays real.)
- **Exploded concept still** → product-vfx §A/§B.
- **Higgsfield native**: `higgsfield-product-photoshoot` skill (modes product_shot, conceptual_product levitating/splash) and Marketing Studio product-shot presets (`get_presets source:'marketing_studio' category:'product-shot'`) beat freehand prompts for catalogue work.
- Product QC: label spelling, logo shape, cap/pump geometry, colour vs real pack — compare side by side.

## Compliance & QC (all sections)
- SG health ads (localisation.md SG pack): no before/after body or symptom "results", no fake patient/testimonial photos, no superlatives on-image. Relight/grade/angle edits of Klaus, consenting staff, the clinic and products are fine.
- Faces: compare result vs source at same size (eyes, jaw, skin tone); reject any beautification Klaus didn't ask for.
- Text: GPT Image 2.5 for anything with words; still proof-read every letter.
- Log every keeper prompt + model + seed into the project's spec/generation log so the look is repeatable.
