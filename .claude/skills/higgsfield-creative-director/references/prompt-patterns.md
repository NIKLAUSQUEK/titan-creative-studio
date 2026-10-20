# Prompt patterns (research synthesis: Kling 3.0 guides incl. Higgsfield's Notion guide, Seedance 2.0 official + community guides, Higgsfield workflows)

## Universal grammar
`CAMERA (owner + size + lens + move) -> SUBJECT (cast tag + 1 trait) -> ACTION (verbs, start state -> end state) -> ENVIRONMENT (set-map anchor) -> LIGHT/LOOK (brand file) -> AUDIO (speaker-tagged line + tone + ambience) -> CONSTRAINTS (continuity + exclusions)`
- Models weight early tokens more: camera + identity first, quality tail last.
- Describe physics outcomes, not vibes: "bar bends slightly as he presses, elbows shake" > "struggling".
- Camera language that both Kling and Seedance parse: static tripod, slow push-in, handheld with subtle drift, whip-pan, tracking, low-angle POV, over-the-shoulder, macro close-up, shot-reverse-shot. Without camera direction Kling defaults to static.
- Avoid: "dynamic shot", "cool angle", "camera moves", "cinematic" alone.

## Kling 3.0 Omni multi-shot (dialogue skits)
```
multi_shots: true
multi_prompt: [
 "Shot 1 (0-2.5s) | WS neutral 3rd-person, 28mm, static tripod at the gym's E wall | A (lean 30s man, black tee, grey shorts, curly dark hair) lies supine on a flat bench, gripping a loaded barbell at lockout, arms trembling. B (huge muscular man, black stringer, grey shorts) stands behind A's head, eyes down on his phone, thumb scrolling. | Dim gym, warm amber tungsten practicals, haze. | Ambience: low gym hum, plates clink. | same characters, same wardrobe, no face morphing",
 "Shot 2 (2.5-6s) | CU, A-POV looking straight up, 24mm low angle | B looms upside-down-relative... "
]
```
Rules: label shots; introduce full character descriptions in Shot 1, then refer by tag; one camera owner per shot; dialogue bound to a visible action ("A's jaw clenches, he says flatly: ..."); keep the color grade line identical across shots.

## Seedance 2.5 / 2.0
- A prompt is a job assignment: Subject - Action - Camera - Style - Constraints.
- Use `@Image1`/`@Video1`/`@Audio1` refs: images lock identity/space/opening frame; video refs lock motion/timing/camera; audio refs lock rhythm/voice.
- Multi-shot with explicit "cut to" markers. Keep each spoken line short.
- Introduce the primary subject first; adding multiple subjects early splits attention and causes drift.
- Source images >= 1024 px short edge for stable long clips.
- `draft:true` -> review -> `draft_job_id` finalize.

## Cinema Studio 4.0
- Use creative-control ids (camera_model_id, camera_lens_id, aperture, pacing_id, genre_id, light/light_id, color_palette) instead of prose for look - it is deterministic and repeatable across a series. Save the id set per brand in the brand file once chosen.

## Images / start frames
- Slot order: composition + camera owner, identity (cast sheet verbatim), action/pose, set-map anchor, light, palette, realism module, quality tail, negative tail.
- Realism module (anti-AI): visible pores, natural asymmetry, matte skin, no beauty filter, no airbrushing, no plastic skin.
- For a new angle of an existing set: pass the master still as reference + "same room, same objects in same positions, camera now at <position> facing <direction>".

## Moderation-safe staging
- Bodily-fluid gags near genitals, "wet crotch", "leak" visuals -> NSFW blocks (2 wasted gens on 9 Oct). Restage: sweat drop from forehead onto the bar; reaction faces; on-screen caption carries the joke; for pelvic-floor education use a clean diagram/overlay, not a body close-up.

## Text on screen
- Prefer burning captions/overlays in post (video-montage workflow / CapCut) over generating text in video. For stills, gpt_image_2_5 or ideogram with exact quoted text and font description.
