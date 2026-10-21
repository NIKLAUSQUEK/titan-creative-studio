# 3D feature-animation ("Disney/Pixar-style") and cartoon workflow

Source tags are explained in `research/sources-editing.md`. The main source is Dan Kieft's Kling 3.0 animation guide [Kieft], plus the Higgsfield Blender and Motion workflows [HF-Blender] [HF-Motion].
Studio rules still apply: original characters only (character-design.md, no lookalikes of real people or of existing studio characters), Gate 4 visual approval before any video, drafts at the lowest quality first.

**Prompt wording:** describe the look rather than naming studios. Write "stylised 3D feature-animation look, soft subsurface skin, large expressive eyes, rounded appealing shapes, warm cinematic lighting". Studio names can trip IP filters and break the brand-safe-prompt rule. "Pixar-style" is fine in conversation with Klaus but avoid it in generation prompts unless a draft proves it's needed.

## 1. Pipeline (4 steps) [Kieft]
1. **Story → characters → character sheets → storyboard stills.** Stills are cheap, so make many.
2. **Image-to-video** with Kling 3.0 (start/end frame, scene continuation, Omni multi-shot) or Seedance 2.5 omni_reference.
3. **Audio sync:** one consistent voice per character via a voice changer, then lip-sync fixes.
4. **Edit:** order, transitions, SFX and music.

## 2. Characters and style key
- **Generate every character with the same style phrase** (e.g. "3D animated"), or you get a mix of 3D and photoreal people in one frame, which looks broken unless that mix is the concept. [Kieft]
- **Style key** (paste at the end of every image and video prompt for the project and save it in `spec.json` as `style_key`):
  ```
  STYLE KEY: stylised 3D feature-animation render, soft subsurface skin, slightly oversized heads and eyes,
  rounded appealing silhouettes, painterly textured fabrics, warm key light + cool rim, gentle bloom,
  shallow depth of field, rich saturated but soft palette <hex list>, 2.39:1 or 16:9 cinematic framing.
  Every character and prop in the same 3D animated style; no photoreal humans.
  ```
- **Lighting words matter.** Always state the light source (soft window light, street lanterns at night). Leaving it out drifts the style. [Kieft]

### Character sheet prompt (Nano Banana Pro / Nano Banana 2, 16:9, 4K, character image attached) [Kieft, structure; wording ours]
```
Character turnaround sheet of the attached character, same 3D animated style. Row 1: full body front, 3/4 left,
profile left, back, 3/4 right. Row 2: head close-ups - neutral, happy, sad, surprised, angry - plus a 3/4 head and a
profile head. Neutral light-grey background, even soft studio lighting, identical outfit, proportions and colours
in every view, no text, no extra characters.
```
Then register each approved sheet as an **Element** (`manage_reference_elements`) and inject it with `<<<element_id>>>` (model-routing.md). Use the Higgsfield `character-sheet` workflow when Klaus explicitly asks for a sheet.

## 3. Storyboard stills
- Upload the character sheet(s) and prompt with the four parts: **subject + details + action + style**. Example: "3D animated man in a dark suit, loose tie, messenger bag on his shoulder, standing inside a warmly lit apartment, hand on the door as if just walking in, looking into the room. [STYLE KEY]". [Kieft]
- **Multi-reference scenes:** attach character sheet A, character sheet B and the prop image, then write in plain words what happens ("father holds a stack of flyers, the boy holds a smaller stack, a woman reaches out and the dad hands her one; both look tired and sad; street-lantern light"). [Kieft]
- **Reference a previous still by tag** (`@image2`) to build derivative shots, e.g. a selfie still that later appears as a printed photo in his hands. [Kieft]
- **Multi-shot angles** from one still ("open in multishot") give alternate coverage cheaply. Upscale only the keepers. [Kieft]
- Lay the frames out in order (Figma or `scripts/qc_frames.py`-style contact sheet) and get Klaus's approval before any video.

## 4. Image-to-video techniques [Kieft]
1. **Start + end frame (most-used):** make the end-state still, then edit it into the start-state ("remove the man and close the door"). Kling 3.0 start/end frame prompt: "He grips the doorknob, turns it, pushes through the door while saying 'I'm home.' He steps inside, slides his hand from the knob to the door edge, looking into the room." Set the duration to fit the line (3 s or more).
2. **Scene continuation:** the last frame of clip A becomes the start frame of clip B, and a new still is B's end frame ("man closes the door, camera turns slowly and pans to the kid on the couch"). Stitch them for one continuous take.
   `ffmpeg -sseof -0.1 -i A.mp4 -frames:v 1 -update 1 A_last.png`
3. **Kling 3.0 Omni multi-shot:** upload elements (scene stills plus the character sheet so clothes stay consistent), enable multi-shot, and write each shot separately with its own duration (e.g. 3 shots in 9 s: tuck-in / stands, lights off, exits / slides down the wall outside the door). It's less exact per shot but fast. Generate separately when you need control.
- **Precise camera or blocking for animation:** block in Blender (Higgsfield Bridge), then generate. The same blocking file can be re-skinned **2.5D, full 2D ink-on-paper, or 3D toy-box** with identical camera and cuts. [HF-Blender]
- **Cartoon explainer hybrid:** generate the characters and voices in Higgsfield, and animate documents, text and maps in code (Claude Motion / Remotion). [HF-Motion]

## 5. Voices and lip-sync
- **Each generated clip gives a slightly different voice for the same character, and prompting doesn't fix it.** Run every line of a character through **one** voice: Higgsfield `voice_change` (Audio → Change voice) or ElevenLabs voice changer (more voices, custom voice). [Kieft]
- Keep the voice IDs in `cast/registry.md`. Use voice-persona-audio.md archetypes and never clone a real person.
- **Lip drift fix:** slide the audio about 2-4 frames earlier than the picture. [Kieft]
  `ffmpeg -i clip.mp4 -itsoffset -0.08 -i clip.mp4 -map 0:v -map 1:a -c copy clip_sync.mp4`
- Dialogue-heavy scenes: prefer Kling 3.0 Omni native multi-shot dialogue (model-routing.md), then voice-change in post.
- **Performance reference:** Klaus films himself acting the beat on a phone, then Genjutsu motion transfer (`hf_mult_motion_control`) onto the animated character. This is the studio default for performance-critical shots.

## 6. Edit
Order the clips to the storyboard, then add flashback treatments (film burn, cross-fade), SFX (generated or licensed) and music (licensed or AI-generated). Use any editor: CapCut, DaVinci or Premiere, or the ffmpeg/Remotion route in claude-editing.md. [Kieft] Run QC on the contact sheet.

## 7. Movie-quote sites as timing and acting references (NOT as footage)
| Site | What it gives you | How we use it |
|---|---|---|
| **getyarn.io** | Short clips searchable by quote, with **clip length shown** (e.g. "2.7 s") | Measure how long a delivery takes, its pause placement and its reaction beat. Use it to set shot duration and line timing in the spec. [Yarn] |
| **clip.cafe** | 5M+ clips and 82M phrases from 20k films. Filter by actor, character, genre, year and **clip length**. Watch the scene around the line. [ClipCafe] | Study the staging, the cut point and the reaction shot pattern of a comedic or dramatic beat. |
| **playphrase.me** | Type a phrase and see many films saying it back-to-back. English (39M+ phrases), French, Spanish, Japanese, Italian and German. [PlayPhrase] | Compare 10 deliveries of the same line (sarcastic, tender, angry), pick the read and describe it in the prompt or to the voice actor. |
| **aimoviequotes.com** | AI quote finder by title, **theme or mood** across books, films, TV and lyrics. [AIMQ] | Find the archetypal line for a mood, then **write an original line** that hits the same beat. |

**Rules (copyright and brand safety):**
- **Never download quote clips into project folders or outputs.** View them in the browser only, and log the reference as text: `film / timecode / what we learned (duration, pause, eyeline, cut)`.
- **Never recreate recognisable characters, costumes, sets or actors' likenesses**, and never use a real actor's voice. Describe the *acting* ("deadpan 1.2 s pause, eyes slide to camera, half-smile on the button word") instead.
- **Don't quote famous lines verbatim in ads.** Short quotation may be fair use or fair dealing in commentary, but rules vary by country, and for commercial ads assume no. Write an original line with the same rhythm. [AIMQ FAQ]
- For a reaction or GIF-style beat in our own animation, recreate the *timing* with our characters: the anticipation pose, the hold, the take and the settle.

**Reference prompt pattern:**
```
Acting/timing reference (do not copy footage): line lasts 2.6 s, 0.4 s silent beat before the last word,
eyes move off-partner to camera on the beat, small head tilt on the button. Apply to <<<char_dad>>> saying
"<original line>". Medium close-up, static camera, 4 s clip, hold 1 s reaction after the line.
```

## 8. Animation QC add-ons
Check that the style is consistent across every character (no photoreal intruders), outfits match the sheet, the voice is the same across clips, lips sit within 2 frames, eyelines hold across cuts, and character scale doesn't drift between shots. [HF-Blender] [Kieft]
