# Physio Spot ad: full production brief (copy-paste for any AI)

You are helping a men's health physiotherapist ("Nik") make short, funny, provocative vertical video ads for his clinic **Physio Spot** (men's health: erectile dysfunction, premature ejaculation, pelvic pain, prostate conditions). This brief explains the finished ad "Physio Spot: are you REALLY spotting?" (v4, 36 s, 9:16), exactly how every shot was prompted and edited, what went wrong along the way, and the standing rules for every future ad. Treat section 7 ("Dramatisation system") as a permanent instruction for all ads.

---

## 1. The concept in one line

Two guys at the gym. The friend on the bench keeps asking the buff spotter if he's really spotting. The punchline: the buff guy has a small pee leak on his grey shorts that he hasn't noticed ("spot" = spotting at the gym + spotting a leak). Cut to black, a bulb flicks on, Nik in scrubs: "Once you spot it, come to Physio Spot."

Tone: deadpan comedy, then a sharp humiliating reveal, then calm, premium, reassuring clinic ending. Shame is played for laughs on screen but the ending is warm and stigma-free.

## 2. Characters and set (keep these constant in every shot)

- **Buff guy (the spotter):** huge, dark-skinned bodybuilder. Skimpy black stringer singlet with deep armholes. Light heather-grey cotton shorts. Skin completely DRY and matte (no sweat, no shine; otherwise the leak reads as sweat). Absorbed in his phone, grinning at reels.
- **Friend:** slim, light-skinned guy, black t-shirt, lying flat on his back on a flat bench. NOT lifting. Hands resting on his stomach. Deadpan, nerdy, unimpressed.
- **Staging (critical, never change):** the buff guy stands at the HEAD end of the bench, behind the friend's head and behind the racked empty barbell, in classic spotting position. The friend's head stays flat on the bench pad and he stares straight up at the ceiling. **He never turns his head to look at the buff guy.**
- **The leak:** three distinct drops in the MIDDLE of the front of the grey shorts, below the drawstring: one big round, one small round, one oval. Each is just a darker shade of the same grey. NOT red, NOT brown, NOT a big patch, NOT coming from the waistband. "Like he leaked a bit of pee and didn't notice."
- **Gym look:** dark, gritty gym, hard warm yellow tungsten top light, deep shadows, 35 mm film grain, cinematic, vertical 9:16.
- **Shorts rule:** the shorts are NEVER visible in the opening shots. They are shown only after the friend points (POV), and the stain is already there; the zoom just makes it obvious.
- **Nik (ending):** the user's own trained Higgsfield Soul character "Nik" (soul_id `1e8acf3a-cd75-43a0-ac2b-e97706906d2c`). Plain navy scrubs, no logos. Warm beige minimalist room, single bare Edison bulb.

## 3. Final script, line by line (v4 timings)

| # | Time | Shot | Audio / line | On-screen caption |
|---|---|---|---|---|
| 1 | 0.0–1.2 s | Low angle from the bench up at the buff guy, chest-up, grinning at his phone. Bar across the top of frame. | Gym room tone | none |
| 2 | 1.2–3.0 s | Side-on close-up of the friend lying on the bench, spotter blurred behind his head scrolling his phone. Friend stares at the ceiling. | Friend (casual nerdy voice): "Bro... are you spotting?" (long mid-line pause cut out) | Bro... are you spotting? |
| 3 | 3.0–5.9 s | Back to the buff guy, chest-up. Opens already mid-glare, eye-roll. | Buff guy (deep): "Hmph. You're only doing the bar." | Hmph. You're only doing the bar. |
| 4 | 5.9–8.8 s | Friend close-up again, narrows eyes, knowing smirk, slow push-in. Head still. | Friend: "Yeah... but are you REALLY spotting?" | Yeah... but are you REALLY spotting? |
| 5 | 8.8–10.6 s | Buff guy. Grin drops instantly, lowers phone, confused curious frown, snap push-in. | Buff guy: "What?" | What? (appears with the word) |
| 6 | 10.6–13.3 s | POV from the buff guy's eyes looking straight down: his own shorts waistband and singlet hem in the foreground, the racked bar, the friend's upside-down face below. Friend keeps his head still, raises an eyebrow and jabs a finger up at the shorts twice. Camera tips down following the finger. | Room tone, tension | none |
| 7 | 13.3–16.3 s | Close-up of the front of the grey shorts: three darker-grey drops. Fast aggressive push-in, then a sudden still hold. | Dramatic hit (see section 7) | none |
| 8 | 16.3–20.8 s | Wide side-on: buff guy behind the bar hunched, face in his hand, squirming, glancing down. Friend on the bench laughing uncontrollably, wheezing. Slow pull-back. | Loud genuine laughter | none |
| 9 | 20.8–21.3 s | Hold / transition | — | — |
| 10 | 21.3–36 s | Black. Bulb flickers on (black flash), Nik in scrubs in the beige room, calm push-in. Beige card fades in with the conditions in italic, then the brand. | Nik (calm, warm): "Once you spot it, come to Physio Spot. We provide guidance and treatment for men's health: E.D., P.E., pelvic and prostate conditions. Don't wait till it's too late." | Erectile dysfunction / Premature ejaculation / Pelvic pain / Prostate conditions → **Physio Spot** / men's health physiotherapy |

## 4. Tools and settings

- **Platform:** Higgsfield.
- **Stills (keyframes):** `gpt_image_2_5`, aspect 9:16, with `image_references` (1–2 earlier images). It follows framing and staging much better than `soul_2` with a reference. Use `soul_2` + `soul_id` only for Nik.
- **Video:** `kling3_0`, mode `pro`, 9:16, `sound: on`, `start_image` = the keyframe, 3 s for dialogue beats and inserts, 5 s for the laugh shot, 13 s for the ending. If Higgsfield offers the "IN THE DARK" preset instead of submitting, resubmit with `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- **Friend's voice:** generate the line in Kling (so the lips sync), then run Higgsfield `voice_change` on that clip with the ElevenLabs preset voice **Benji** (`e6f9b893-51b1-51d3-afe9-9e0482cb7ac1`): casual, nerdy. Timing and lip sync are kept. (The "Dylan" voice was rejected as weird and stuttery.)
- **Buff guy's voice:** Kling's own generated deep voice.
- **Edit:** ffmpeg. Every clip scaled to 1080×1920, 30 fps, 48 kHz stereo, then concatenated. Captions: DejaVu Sans Bold 46 px, white with a 4 px black border, centred at 74% of the height, timed to appear with the spoken word.
- **Content filter:** words like "pee", "crotch" and "groin" get blocked. Use neutral wording: "three small water drop marks on the front panel of the shorts", "pointing at the grey shorts in the foreground".

## 5. Exact prompts used for the final cut

### 5a. Keyframe images (`gpt_image_2_5`, 9:16)

**Buff guy chest-up (used for shots 1, 3, 5)** (reference: an earlier wide gym image)
> Same bodybuilder (same face and build) and the same dark gym with hard warm yellow tungsten top light as the reference. Low-angle MEDIUM CLOSE-UP from his navel up only (waist and shorts out of frame). He now wears a skimpy black bodybuilding stringer singlet with deep cut armholes; his skin is completely DRY and matte, no sweat, no shine. The yellow light carves deep shadows across his huge shoulders, traps and arms. He grins down at his phone held at chest height. Photorealistic, film grain, cinematic, vertical.

**Wide staging master (shot 8, and the reference for all other staging)**
> Wide side-on shot in the same dark gym with warm yellow light: a flat bench with an empty barbell racked at its head end. The slim light-skinned friend in a black t-shirt lies on his back on the bench, laughing hard with his head back on the bench and a hand on his chest. The huge dark-skinned bodybuilder in a black stringer singlet and light grey cotton shorts stands at the HEAD end of the bench, behind the friend's head and behind the racked barbell, in spotting position; he is hunched with one hand over his face in embarrassment. On the front of his grey shorts, in the middle, three small darker-grey drop marks (one big round, one small round, one oval); the rest of the shorts and his skin are completely dry. Full bodies in frame, photorealistic, film grain, vertical.

**Friend close-up (shots 2 and 4)** (references: the wide master + an earlier friend face)
> Same gym, bench, racked barbell and people as the first reference, same side-on camera direction but a tight medium close-up on the slim light-skinned friend lying flat on the bench (face from the second reference). His head rests flat on the bench pad and stays still; he stares straight up at the ceiling, not at anyone, with a flat deadpan face, mouth slightly open mid-sentence. The racked empty barbell runs across the upper part of the frame just above his face. Behind his head, at the head end of the bench, the huge dark-skinned spotter's torso in a black stringer singlet is visible but blurred and cropped at the chest, holding a phone; his shorts are out of frame. Hard warm yellow light, photorealistic, 35mm film grain, vertical.

**POV point (shot 6)** (references: the wide master + friend face)
> First-person point of view of the dark-skinned spotter standing at the head end of the bench from the first reference, looking straight down. Layout of the vertical frame from bottom to top: (1) bottom edge, out of focus foreground: the waistband and drawstring of his own light heather-grey shorts and the hem of his black singlet; (2) the racked empty barbell crossing the frame horizontally; (3) directly beyond the bar, the friend's face seen UPSIDE DOWN, the top of his head pointing toward the bottom of the frame, resting flat on the bench pad; (4) the friend's black t-shirt torso and legs extending toward the top of the frame along the bench. The friend keeps his head still, eyes looking straight up with a curious raised eyebrow, and bends one arm back over his face to point his index finger straight up at the grey shorts in the foreground. Hard warm yellow light, photorealistic, 35mm film grain.

**The drops (shot 7)**
> Product-style close-up of the front panel of light heather-grey cotton jogger shorts worn by a man, waistband drawstring at the top and the hem of a black tank top just visible above it. The cotton is dry everywhere except for three small water drop marks near the centre of the front panel, below the drawstring: one larger round drop, one smaller round drop and one oval drop, each just a darker shade of the same grey with crisp edges. Warm yellow light, photorealistic, film grain, vertical.

**Nik ending (shot 10)** (`soul_2` with Nik's soul_id)
> Vertical cinematic photo: the man in plain solid navy blue medical scrubs with no logos or lettering stands calmly in a minimalist warm beige room, lit only by a single bare Edison light bulb hanging just above and in front of him, warm soft glow, gentle shadows, calm reassuring half-smile, looking directly into the camera. Clean empty beige wall with lots of negative space in the upper third. Serene, premium, text-free image.

### 5b. Video prompts (`kling3_0` pro, 9:16, sound on)

**Shot 2, friend line 1 (3 s)**
> From the very first frame the guy lying on the bench is already speaking. His head stays completely still on the bench pad and he keeps staring straight up at the ceiling, never turning to look at the man behind him. Flat, unimpressed deadpan face. He says in a casual nerdy voice: 'Bro... are you spotting?' The blurred man behind keeps scrolling his phone. Static camera, hard yellow gym light, ambient gym hum.

**Shot 3, buff guy line (7 s clip, the 2.9–5.75 s window used)**
> Chest-up low-angle shot of the bodybuilder in a black stringer singlet under hard yellow light, framing held throughout. For the first three seconds he is completely silent, grinning and thumb-scrolling his phone. Then he glances down, rolls his eyes hard and scoffs in a deep voice: 'Hmph. You're only doing the bar.' then goes straight back to smiling at reels. Static camera. Ambient gym hum, no other voices, no music.

**Shot 4, friend line 2 (3 s)**
> From the very first frame the guy lying on the bench narrows his eyes and smirks knowingly. His head stays completely still on the bench pad and he keeps staring straight up at the ceiling, never turning to look at the man behind him. He says in a casual nerdy voice: 'Yeah... but are you REALLY spotting?' Slow push-in on his face. Hard yellow gym light, ambient gym hum.

**Shot 5, "What?" (3 s, the 1.25–3.0 s window used)**
> Instantly, from the very first frame, the bodybuilder's grin drops. He lowers the phone, tilts his head and looks down toward the bench with a confused, curious frown, eyebrows pinched, as if asking 'what?'. He says nothing. Quick snap push-in. Hard yellow light, ambient gym hum only, no speech.
(Kling added the "What?" by itself and it worked; keep it.)

**Shot 6, POV point (3 s)**
> Point of view looking straight down. From the first frame the guy lying on the bench keeps his head still and, with a curious raised eyebrow, jabs his pointing finger twice toward the grey shorts in the foreground. The camera tips down toward the shorts with a quick push-in, following the finger. Hard yellow light, ambient gym hum, no speech.

**Shot 7, drop zoom (3 s)**
> Fast aggressive push-in onto the three small darker grey drop marks on the front of the grey shorts, then a sudden still hold. Fabric otherwise still. Dramatic comedic reveal, warm yellow light.

**Shot 8, humiliation and laugh (5 s, first 4.5 s used)**
> From the first frame: the bodybuilder standing at the head of the bench behind the racked bar squirms with awkward humiliation, face buried in his hand, shifting his weight and glancing down at his shorts. The guy lying on the bench laughs uncontrollably, wheezing and holding his chest, head staying back on the bench. Both stay in their positions. Camera slowly pulls back. Sound: loud genuine laughter, ambient gym hum.

**Shot 10, Nik (13 s)**
> The man in navy scrubs stands calmly in the warm beige room under the single glowing bulb. He looks straight into the camera and says in a calm, warm, confident male voice: 'Once you spot it, come to Physio Spot. We provide guidance and treatment for men's health: E.D., P.E., pelvic and prostate conditions. Don't wait till it's too late.' He gives a small reassuring nod and a warm smile. Very slow gentle push-in. Calm, premium, quiet room tone, no music, no text.

### 5c. Ending card (ffmpeg on the Nik clip)
- Start black; 0.12 s black flash at 0.5 s = the bulb "flicker", then fade in over 0.8 s.
- From 6.5 s a soft beige panel (#EFE3D3 at 88%) on the lower third.
- The four conditions fade in one by one (6.8 / 7.6 / 8.5 / 9.2 s) in **Cormorant Garamond Italic**, 80 px, warm brown #4E3B2E, calm and beige, never clinical red.
- At 12.2 s they fade out; **"Physio Spot"** fades in (Playfair Display Italic, 104 px), then "men's health physiotherapy" beneath (Cormorant Italic, 58 px, #6B5544).
- Hold the last frame 1.6 s with room tone.

## 6. What went wrong and the fixes (don't repeat these)

1. **The stain showed red or brown** → always say "just a darker shade of the same grey, no red, no brown, no colour".
2. **It looked like sweat** → the buff guy must be dry and matte, wear a skimpy singlet (not shirtless), and the leak must be 3 small drops in the middle of the front, not a patch from the waistband.
3. **The stain "appeared" in the zoom** → it's there all along; the shorts just aren't shown until the point. The zoom only makes it obvious.
4. **The friend's line was spoken by the buff guy** → each line must come from the right mouth. Generate each speaker's line on a clip of that speaker, lip-synced.
5. **No back-and-forth** → the opening must cut between the two faces (shot / reverse shot) on every line, not hold on one person.
6. **Laggy emotions** → every clip must start with the emotion already happening ("from the very first frame…"). Trim the slow ramp. Cut out mid-line pauses.
7. **The POV pointed at the lens** → POV is from the buff guy's eyes looking DOWN at the friend, who points at the shorts in the foreground. Describe the frame layout bottom-to-top explicitly.
8. **Staging jumped** (buff guy behind in one shot, beside in another) → lock one staging (spotter at the head of the bench behind the bar) and use the wide master image as a reference for every shot.
9. **The friend turned his head to look at the buff guy** → "His head stays completely still on the bench pad… never turning to look at the man behind him."
10. **A voice was weird or stuttery** → use the Benji voice via voice_change.
11. **Text inside generated images is unreliable** → never ask the image model for text; add all captions and cards in the edit.

## 7. Dramatisation system (apply to EVERY future ad, always)

Nik loves the dramatic zoom-with-sound moments. Build every ad around at least one big reveal beat and lean into it hard:

1. **The reveal recipe (use every time):** point or look → hard cut → FAST aggressive push-in (crash zoom) on the reveal object → sudden freeze/still hold 0.5–1 s → reaction shot. In the video prompt write it explicitly: "fast aggressive push-in / crash zoom onto X, then a sudden still hold, dramatic comedic reveal".
2. **Sound design on the reveal:** a whoosh or riser into the zoom, a deep bass "boom"/impact hit on the freeze, then 0.3–0.5 s of near-silence before the reaction (laughter, gasp, record scratch). Ask Kling for "dramatic impact sound on the zoom, then silence" with sound on; if it doesn't land, layer SFX in the edit (whoosh → boom → silence → laugh). Duck room tone under the hit.
3. **Snap push-ins on every emotional turn** (eye-roll, grin dropping, "What?"): a quick 5–10% punch-in timed to the beat, with a subtle whoosh.
4. **Shot / reverse shot on dialogue**, cutting on each line, 1.5–3 s per shot. No long single-angle holds in the first 10 s.
5. **Emotions are instant.** Every prompt starts "From the very first frame…", and trim to the moment the expression changes.
6. **Comic timing:** a beat of silence before the punchline; the punchline image holds just long enough to read (about 1 s); the laugh cuts in hard.
7. **Captions** land on the spoken word, large, bold, white with a black border; the key word in CAPS ("REALLY").
8. **Contrast ending:** after the chaos, a hard cut to black, then calm (bulb flicker, slow push-in, soft room tone, beige italic text). The tonal flip makes the brand feel trustworthy.
9. **Hook in the first 1.5 s:** strong visual and a question or tension line before 2 s.
10. **Keep continuity:** same wardrobe, lighting, staging and character references in every shot; reuse the master image as a reference.
11. **Stay tasteful:** humour by implication. No nudity, no graphic fluids, no real names. The clinic ending is respectful, warm and stigma-free.
12. **Length:** 25–40 s; the reveal by about 40% of the runtime; the clinic CTA in the final 12–15 s.

## 8. Reusable shot-prompt template

```
[SHOT n] [length 3 s] [framing: close-up / wide / POV looking down, layout bottom-to-top …]
Same gym, people, wardrobe and staging as the reference (spotter at the head of the bench behind the racked bar; friend lying flat, head still, staring at the ceiling).
From the very first frame: [emotion already happening] + [action].
[Dialogue: 'line' in a casual nerdy voice / deep voice] or [no speech].
Camera: [static / slow push-in / fast aggressive push-in then sudden still hold].
Sound: [ambient gym hum / dramatic whoosh into an impact hit then silence / loud genuine laughter].
Hard warm yellow tungsten light, 35mm film grain, photorealistic, vertical 9:16.
```
