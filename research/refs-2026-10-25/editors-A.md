# Editor reference study, batch A (2026-10-25)

Refs: ed01 mahdiology.edit · ed02 editvibez12 · ed03 ruth.the.crafter · ed10 getclayhook
Source packs: `scratchpad/refs/b2/pack/<id>/` (meta.json, transcript, 1 fps sheet, 4 fps hook). Extra frames pulled with ffmpeg (inner-frame crops for ed01/ed02, 4 fps for ed03 3-9 s, colour sampling on 8 stills).
Studied for technique only. No reference footage gets cut into our edits.

Note: ed01, ed02 and ed03 are editor portfolio reels. ed01 and ed02 show a small "Before" (raw) window next to a large "After" window on a branded backdrop. I analysed the **After** window, because that is the style Klaus wants. The portfolio wrapper is a technique in its own right, covered in §5 (F10).

## Measured numbers (from meta.json + frame checks)

| ref | dur s | detected cuts | median shot | words/min | LUFS | what really changes (by eye) |
|---|---|---|---|---|---|---|
| ed01 | 23.8 | 2 (4.00, 7.47) | 4.0 s | 247 | -14.4 | 2 full-screen 3D-illustration inserts (4.0-~6.3 s and 7.47-~13.8 s, so ~36 % of runtime), 1 colour-wash transition (~19 s), 1 tight punch-in from ~19.8 s to the end |
| ed02 | 15.4 | 11 (they fall in 3 flash clusters: 1.43-1.57, 9.0-9.07, 11.87-12.0, 14.3-14.43) | 0.07 (artefact) | 199 | -14.5 | 5 segments: face 0-1.43 · motion-graphic cards 1.5-9.0 · face 9.07-11.87 · illustration card 12.0-14.3 · face 14.43-end. Face is on screen ~34 %, designed cards ~66 %. Every transition is a 2-4 frame glow flash |
| ed03 | 22.4 | 22 | 0.5 s | 38 (music-led, one VO line) | -14.1 | Intro 0-5.73 is one composited animation with 3 background swaps (~2.9 s, ~4.6 s, ~5.0 s) the detector missed. Showreel 5.73-22.4 has 21 cuts in 16.7 s, about 0.8 s average |
| ed10 | 56.5 | 0 | 56.5 | 178 | -14.1 | Fully animated, with no hard cuts. Scenes change through camera moves and morphs about every 2-4 s. Subtitle chunks change every ~2.2 s (26 transcript lines / 56.5 s) |

All four are mastered at about -14 LUFS (IG/TikTok normalisation target). Our `music.db`/master should land in the same place.

---

## ed01 · mahdiology.edit: "talking head → 3D metaphor motion graphics" (interview/podcast clip)

**Hook, first 3 s (After window, 4 fps):**
- 0.0-0.25 s: a medium-close interview shot of a man on a dark teal set. The first word "We w…" fades in at chest height. It is small, light weight and partly transparent.
- 0.25-1.0 s: the payoff words "on videos" build up letter by letter with a **blur-to-sharp + glow** reveal. They sit under the small setup words "We work". The font is a bold serif, pale yellow (~#F2E15A) with a soft yellow outer glow.
- 1.25-2.0 s: the caption clears. The next line, "probably three or four months / **in advance**", appears **top-right beside his head** (about 25 % down the frame, right-aligned). "in advance" is the payoff in orange (~#F5A623).
- 2.75 s: "but **Before** that like". "Before" is a larger blue-grey word inside a lighter sentence, which is per-word emphasis inside the line.

**Layout/framing:** single-camera 16:9 interview reframed to 9:16 at chest-up. Bottom ~30 % is a dark gradient (clothes plus a probable added gradient) that holds the captions. At ~19.8 s the frame punches in to a tight face crop, about 1.35x [inferred from face size], for the money line "1.5 million a video".

**Captions:** a two-tier system.
- Setup words: small (~0.022 H), light-weight sans, white at ~85 % opacity, sentence case.
- Payoff/keyword: 2-4 words, about 2x larger (~0.045 H), bold sans or serif, coloured (yellow ~#F2E15A, orange ~#F5A623 or white bold) with a glow. It sits directly under the setup words.
- Each group runs 3-6 words. Words reveal one by one with a blur/fade-in.
- Position moves between chest height (y ≈ 0.62-0.69 of the frame) and beside the head (y ≈ 0.25, right side) to avoid the face and hands.

**Graphic elements:**
- Full-screen photoreal 3D "desk" metaphor scenes in a warm cream top-down still life with soft window-shadow light: a brain, then a lightbulb pops on above it, then sticky notes ("concept / story / style") and a coffee cup.
- A storyboard pile with a dotted arrow animating to a phone showing a play button and an "UPLOAD" tag.
- Big lightbulb with "three to four months / **working on the idea**".
- Elements build on one at a time (scale-pop, roughly every 0.5 s). Captions keep running inside the insert in the same two-tier style.

**Transitions:** hard cuts into the inserts. One **colour-gradient wash** (magenta→violet over the footage, ~0.5 s) on "from start to finish". The sheet also shows a warm orange light-flare at about 16 s.

**Zoom/camera:** a slow drift and punch on the footage [inferred: subtle scale changes between frames]. The hard punch-in for the finale is described under Layout.

**Grade:** natural and slightly crushed. Teal set against warm skin, the default "YouTube interview" look. Inserts are warm and cream.

**Pacing:** 247 wpm, a very dense source. Only 2 hard cuts on the face; the illustration inserts provide the visual change instead of jump cuts.

**Sound [inferred]:** soft ambient/lo-fi bed under the voice. A whoosh on each insert entry, a pop on each element build-on, a "ding" on the lightbulb, a shimmer/riser under the colour wash.

**Persona:** podcast/interview clippers, coaches, experts and founders with sit-down interview footage who want "premium documentary-explainer" polish (MrBeast-business-talk aesthetic). Fits TITAN.AI and Klaus founder clips.

**Steal this:**
1. Two-tier captions: small light setup words with a big glowing coloured payoff word under them.
2. Captions that move beside the head when the hands or face would collide.
3. 3D "desk still-life" metaphor inserts for abstract nouns (idea → lightbulb, brainstorm → brain, process → storyboard → upload). Elements pop on in sync with the words.
4. One colour-wash transition on the line that summarises the process.
5. A hard punch-in to a tight face for the final number.

---

## ed02 · editvibez12: "neon mograph cards" talking head (Alight Motion)

**Hook, first 3 s:**
- 0.0-0.75 s: a selfie talking head (blonde woman, warm bedroom). "My name is" reveals word by word at y ≈ 0.69 of the frame in small white bold sans.
- 0.75-1.25 s: "AVA JUERGENS" slams in under it in a wide black-weight sans, all caps, cyan (#00E0F0) with a cyan glow. The name is the payoff line.
- 1.43-1.57 s: a white-cyan glow flash (3-4 frames).
- 1.5-2.75 s: a full-screen designed card. Dark teal-black background with a vertical cyan light beam, and a **cut-out of the speaker** (pro photo, arms crossed) rising into frame.
- Behind her, a huge condensed "CEO" (Bebas/Anton-like, cyan with glow) fades and scales up, with a small "I AM A" kicker flanked by thin lines. The text sits **behind the cut-out subject** (depth text).
- 2.75 s: a 3D phone mockup showing her Instagram profile swings in from the lower right.

**Layout:** 9:16 selfie with designed full-screen cards between the face sections. Cards have a radial/beam glow and cyan corner swooshes (top-right and bottom-left rounded light shapes).

**Captions:** the same two-tier logic as ed01, louder.
- Lead words: white bold sans, ~0.03 H.
- Keyword: wide, heavy, ALL CAPS, cyan with outer glow, ~0.07 H ("EDIT", "CONTENT", "RIGHT NOW", "GOOD LUCK").
- 1-3 words per group, word-by-word pop with a short scale overshoot.
- Accent words such as "short-form" appear in italic script.
- Position y ≈ 0.65-0.75. On the last line the keyword is above the small words ("GOOD LUCK / By the way").

**Text/graphic elements:**
- Headline cards: "PERSONAL / BRAND LAUNCH" in condensed caps with letter-by-letter wipe-on, plus a small "Social media marketing agency" kicker.
- A list card: "CURRENTLY / We are looking for", then a diamond-bullet list (Talented · Hard working · Committed) that types on one word at a time and is synced to the VO.
- An illustration card: a cyan monochrome illustration of a person at a laptop, with "You are doing / EDITING TASK / *for the application*" (sans + condensed caps + script).
- A sticker icon (yellow clapperboard) pops next to "CONTENT".

**Transitions:** every segment change is a 2-4 frame glow/flash (white→cyan bloom). Card elements scale-in with overshoot.

**Zoom:** a tighter punch-in on the face for the last line, about 1.3x by eye.

**Grade:** footage is natural and warm. Cards are monochrome teal (#001020 base, #00E0F0 accent; sampled).

**Pacing:** 199 wpm. Face segments last 1.4-2.8 s, and a card or face swap happens every ~2.5-7.5 s.

**Sound [inferred]:** an upbeat tech/EDM bed, a glow "shing" on each flash, a typewriter tick per bullet, a bass hit on the CEO slam.

**Persona:** female founder, agency CEO, coach or recruiter. "Tech-premium / personal-brand agency" look. Good for TITAN.AI recruiting and hiring reels, and client agencies.

**Steal this:**
1. Depth text: a giant condensed word behind a subject cut-out.
2. A bulleted list card that types on in sync with the spoken list.
3. A phone mockup showing the brand's own profile or app as social proof.
4. Glow-flash transitions of 2-4 frames.
5. Keyword captions in a wide black-weight font with a monochrome brand accent and glow.

---

## ed03 · ruth.the.crafter: "girly scrapbook + bobblehead mascot" showreel

**Hook, first 3 s:**
- 0.0-0.25 s: a white screen.
- 0.25-0.5 s: a **pixel-grid reveal**. Blue squares build outward around a tiny head cut-out while a **pixel-art hand cursor clicks** on it.
- 0.5-1.0 s: the scene resolves into a dreamy sky with pink 3D clouds over green hills and flowers. The cursor drags the head down.
- 1.0-1.75 s: the head lands on a small body (pink hoodie, jeans), making a **bobblehead**: a real face cut-out about 2x scale on a doll body, with face stickers (hearts, flowers). The word "hey", then "there", appears one word at a time, top-centre (y ≈ 0.16), in heavy rounded white sans (~0.06 H) with a soft shadow.
- 1.75-2.5 s: "I'm Ruth" in **handwritten arched/curved text** above the head.
- 2.75 s: background swaps to blue vertical stripes with floating **soap-bubble icons** (camera, clapper, mic, notebook). Each word now sits on a **white paper sticker label** in handwriting ("and", "this", "is", "my", "application"). A yellow starburst sits behind the bobblehead, and a MacBook rises in front of her.

**Then:**
- ~4.6 s: a pink heart-tunnel background with a film camera and studio light. "video editor" appears in lime-green heavy lowercase.
- A **magic-wand wipe** with a sparkle trail transitions into the showreel at about 5.7 s.

**Showreel layout (5.73-22.4 s):**
- Patterned backgrounds: cream/pink stripes, green gingham, pink stars, pink plaid. They change about every 2-4 s.
- A centred **rounded card window** (~65 % W × 75 % H) plays client clips, cut every ~0.5-0.8 s.
- The bobblehead mascot stays in the **bottom-left corner behind a laptop**, as a persistent cut-out PIP.
- Kinetic stat stack inside a clip: "**3** Brand Trips / **5** Countries / **12** Brand events". Numbers are big yellow (~#F5F000) with small white labels and appear one per beat.
- Clips show the client's own captions (typewriter "#1 place enough bets", serif "Salary Progression"), which shows range.

**Captions:** one word per group, swapped in sync with the VO, and the type style changes per scene (rounded sans → handwriting arc → sticker labels → lime display). Always lowercase or sentence case. No outline.

**Transitions:** pixel-grid build, cursor drag, background swaps on the beat, wand wipe, hard cuts on the beat in the showreel.

**Grade:** high-key, saturated pastel. Pink #E06090 and lime #90B020 accents on sky blue #6090C0 (sampled).

**Pacing:** the intro is fast (a new word every ~0.25-0.4 s). The showreel cuts about every 0.8 s on the beat.

**Sound [inferred]:** 38 wpm means a music-led cute pop/hyperpop bed. Click SFX on the cursor, pops on each sticker word, a sparkle on the wand, and cuts on the beat.

**Persona:** Gen Z girl creators, female freelancers, beauty/lifestyle/fashion/"girlboss" brands, and playful DTC (PeachForm). The "divas" audience.

**Steal this:**
1. A bobblehead mascot (face cut-out on a small body) as a recurring host and corner PIP.
2. One-word captions whose type style changes per scene, including sticker-label words and handwritten arched text.
3. Patterned scrapbook background with a rounded card window for B-roll or clips.
4. Kinetic stat stack (big number + small label) built per beat.
5. Fun transitions: a pixel-cursor reveal and a magic-wand wipe.

---

## ed10 · getclayhook: "illustrated noir explainer" (faceless startup/founder)

**Hook, first 3 s:**
- 0.0-0.25 s: a macro of a cartoon egg sitting on a dark track ring. Dark aubergine-black background (#101010-#302020, sampled) with a radial spotlight.
- 0.25 s: the title "Here's a *paradox.*" appears top-centre (y ≈ 0.19). "Here's a" is white bold serif (DM Serif/Playfair-like); "*paradox.*" is italic serif in lime (#C0F000).
- 1.0-1.5 s: a **continuous camera pull-back**. The egg shrinks and the ring becomes a loop with an infinity symbol behind it. A chicken appears, and the title fades out.
- 1.25 s: the subtitle "You need users" fades in at y ≈ 0.81, in small white semibold sans (~0.028 H), sentence case.
- 2.0-3.0 s: as "to sell your app" is said, the ring **fills with lime chevrons** from chicken to egg, and lime speech-bubble icons (people, app) pop over each character.

**Layout:** 100 % 2.5D vector illustration and no face. A small round brand logo watermark sits top-left. Scenes use recurring "museum" devices: "EXHIBIT A / a book" paper tags, pedestals with spotlights and plaques ("a book, 2021 / Andrew Chen"), a party room, a "COMING SOON" marquee, crowds, a "TRUTH" paper note, and a phone UI with "building…" progress bars.

**Captions:**
- Subtitles: 2-5 words, white sans, bottom, always on, centred, no outline (they sit on the dark background).
- Inline emphasis words switch to *italic serif lime* ("starts at zero.", "problem.", "a promise.", "honest").
- Scene titles in the serif + italic-lime pair appear at the top only on chapter beats ("the cold start *problem.*", "which comes *first?*", "something that *doesn't exist?*").

**Transitions:** no cuts. Camera pushes, pulls and pans between connected scenes, plus morphs (Tesla car silhouette → "NOT FOR SALE yet" → crowd), stamp-ins ("RESERVED", "AVAILABLE NOW" stamped then struck through), and a cross-dissolve to a phone UI.

**Grade:** low-key noir. Near-black warm background, a single lime accent, warm spotlight pools.

**Pacing:** 178 wpm, calm and authoritative VO. A visual beat every ~2.2 s matches the subtitle chunks. A loop ending returns to the egg macro, so the first and last frames match for rewatch.

**Sound [inferred]:** a soft cinematic/lo-fi piano or pluck bed, a whoosh on camera moves, a stamp thud on "RESERVED"/"AVAILABLE NOW", a party-horn and crowd murmur in the party scene, mechanical clicks on the ring fill.

**Persona:** startup founders, build-in-public, B2B/SaaS educators, finance/strategy explainers. Faceless brand accounts (TITAN.AI, the "explain a business concept" pillar).

**Steal this:**
1. A serif title with an italic accent-colour keyword, paired with plain sans subtitles: two fonts, one accent colour.
2. Inline emphasis words in italic accent inside the subtitles.
3. A one-continuous-camera explainer: push and pull between connected illustrations instead of cutting.
4. Recurring "Exhibit A / B" museum-plaque device for citing sources (book, year, author), which builds credibility.
5. A loop ending that lands on the opening frame.

---

## 4. Can our editor do it today?

Editor today has: jump-cut pacing, snap/smooth punch-ins, ASS captions (pop/karaoke/fade/static, highlight colour, emphasis words), PNG text cards (outline/box/label/kicker, emoji), B-roll full/pip/split/greenscreen, persistent header, lower thirds, grade eq/warmth/teal/vignette/LUT, beat sync, SFX by role, end card, iMessage chat cutaways. Fonts bundled: DejaVu Sans/Serif only (plus `assets/fonts/<brand>/`).

| technique | ed | today? | notes |
|---|---|---|---|
| Keyword colour + emphasis captions | 01 02 10 | YES (partial) | highlight colour + emphasis words exist. No glow, no size jump, no font switch |
| Word-by-word reveal | all | YES (pop/karaoke) | the blur-to-sharp variant is missing |
| Punch-in on final line | 01 02 | YES | `zoom.on_emphasis` / snap scale |
| Full-screen B-roll insert (illustration still) | 01 02 | YES (static) | `broll mode: full` with a PNG/clip. Element build-on is missing |
| Corner PIP | 03 | YES (rectangular) | needs a cut-out (alpha) PIP for the mascot |
| Text cards with kicker | 02 10 | YES (static PNG) | no animated type-on, no bullets |
| Persistent header | 10 | YES | usable for chapter titles |
| Beat-synced cuts | 03 | YES | showreel section |
| Grade (teal / warm / vignette) | all | YES | |
| SFX by role (whoosh/pop/impact/riser) | all | YES | needs `flash`, `typewriter`, `stamp`, `click`, `sparkle` roles |
| Two-tier caption (small setup + big payoff line) | 01 02 | **NO** | F1 |
| Glow on text | 01 02 | **NO** | F1 |
| Captions that avoid the face (beside head) | 01 | **NO** | F2 (faces.py exists, so reuse it) |
| Subject cut-out / text behind subject / bobblehead | 02 03 | **NO** | F3 |
| Animated mograph scene cards (bg + layers + type-on + bullets + device mockup) | 02 (01, 10) | **NO** | F4 |
| Flash / colour-wash / light-leak / wipe transitions | 01 02 03 | **NO** | F5 (no xfade in render.py) |
| Style font pack (condensed, wide black, serif italic, handwriting, rounded) | all | **NO** | F6 |
| Sticker-label words, arched text, per-scene caption style switch | 03 | **NO** | F7 |
| Kinetic stat stack / counter | 03 | **NO** | F8 |
| Patterned background + rounded card window ("framed" layout) | 03 (01/02 wrapper) | **NO** | F9 |
| Illustrated still-sequence explainer with continuous camera | 10 | **NO** | F10 (stills from Higgsfield via the studio gates, then the local editor animates them) |

## 5. New features, specified so they can be built

**F1. Two-tier + glow captions** (`captions.tiers`, `captions.glow`)
- Each caption group splits into `setup` (non-emphasis words) and `payoff` (emphasis/keyword words, from the existing emphasis detector or the last 1-3 words of a clause).
- Render as two stacked ASS events at the same timestamp.
  - setup: `size × tiers.setup_scale` (0.5), `tiers.setup_alpha` (0.15 transparency), weight regular.
  - payoff: `size × tiers.payoff_scale` (1.0), colour = highlight, its own font (`tiers.payoff_font`).
  - `tiers.order`: `"setup_first"` or `"payoff_first"`.
- Glow: duplicate the payoff event on a lower layer with `\bord{glow.radius}\blur{glow.blur}\3c{glow.color}\3a{glow.alpha}` and no fill (`\1a&HFF&`).
- Add a new animation `"blur_in"`: per word `\fad(0,0)`, `\t(0,{ms},\blur0)` starting from `\blur8`, plus a 6 px `\move` rise.

**F2. Face-aware caption placement** (`captions.avoid_face: true`, `captions.alt_positions: [[x,y],…]`)
- Use faces.py boxes (sample every 0.5 s).
- If the caption box at `position_y` overlaps the face box or the hands (approximate with a body box under the face), move to the first free alt position, e.g. `[0.72, 0.25]` right-aligned beside the head.
- Align text `\an6` when x > 0.6.

**F3. Subject cut-out** (`cutout` module, local `rembg`/MediaPipe selfie segmentation, CPU OK at 480p drafts)
- (a) `texts[].behind_subject: true` composites text between the background plate and the matted subject (ed02 "CEO").
- (b) `stickers[]`: `{src: still|frame@t, matte: true, scale, x, y, anim:"rise|pop|drag", body: "assets/mascot/body-*.png", head_scale: 2.0}` builds the bobblehead (ed03). The face crop comes from faces.py; the body PNG is chosen from a small library.
- (c) `broll mode: "pip_cutout"` gives an alpha PIP, persistent with `persistent: true`.
- Matte edges get a 2 px feather and an optional white sticker outline (`outline_px`).

**F4. Mograph scene cards** (`scenes[]` in edit.vN.json, rendered by PIL to an RGBA PNG sequence at 30 fps, then overlaid; VO audio continues underneath)
```
{"id":"s01","start":1.5,"end":4.2,
 "bg":{"type":"radial|beam|gradient|image|pattern","colors":["#001020","#00E0F0"],"pattern":"stripes|gingham|stars|plaid"},
 "layers":[
  {"type":"text","text":"CEO","font":"condensed","size":0.16,"color":"#00E0F0","glow":true,"y":0.30,"in":"scale_up","at_word":"CEO","behind_subject":true},
  {"type":"kicker","text":"I AM A","lines":true,"y":0.22,"in":"fade"},
  {"type":"bullets","items":["Talented","Hard working","Committed"],"bullet":"diamond","sync":"words","in":"typewriter"},
  {"type":"device","frame":"iphone","src":"assets/brand/profile.png","tilt":-12,"in":"swing_up"},
  {"type":"image","src":"…/brain.png","in":"pop","at_word":"brainstorm"},
  {"type":"stamp","text":"RESERVED","in":"stamp","angle":-6}]}
```
- `at_word` is resolved from the transcript word timings.
- In-animations: fade, rise, scale_up (overshoot 1.08), pop, typewriter, swing_up, stamp (scale 1.6→1.0 in 4 frames + `stamp` SFX). Each lasts 6-10 frames.
- The `{scene}` role in sfx.map fires on every layer entry.

**F5. Transitions** (`transitions[]` or `transition.default`)
- Types: `flash` (2-4 frames, white→`color` bloom: ffmpeg `xfade=fadewhite` or overlay a radial glow PNG with alpha ramp); `color_wash` (gradient overlay with `colors`, 0.4-0.6 s, blend screen); `light_leak` (bundled leak clip, screen blend); `wipe` (xfade wipe/circlecrop/pixelize); `wand` (sparkle sprite path + wipe).
- Placed at segment boundaries (face↔scene↔broll), with SFX roles `flash`/`whoosh`/`sparkle`.

**F6. Style font pack** (`tools/editor/fonts/style/`, OFL only)
- Bebas Neue / Anton (condensed caps), Montserrat Black or Archivo Black (wide heavy), Playfair Display + Italic / DM Serif Display Italic (serif accent), Inter / Manrope SemiBold (subtitles), Nunito Black / Fredoka (rounded), Caveat / Patrick Hand (handwriting).
- Presets refer to aliases (`condensed`, `wide_black`, `serif_italic`, `clean_sans`, `rounded`, `hand`), so brand fonts can override them.

**F7. Per-word sticker labels, arched text and scene-dependent caption style** (`captions.styles_by_scene`, `captions.label`)
- `label`: each word on a white rounded paper rectangle (radius 0.2 × h, ±4° random tilt, 3 px drop shadow), handwriting font, black text.
- `arc`: text on an arc (`arc_deg: 40`) rendered via PIL per glyph.
- Each caption group takes the style of the scene it falls in.

**F8. Kinetic stat stack** (`layers[].type:"stat"`)
- `{"items":[["3","Brand Trips"],["5","Countries"],["12","Brand events"]],"num_color":"#F5F000","count_up":true}`
- Number ~0.08 H with label ~0.025 H to its right. Each line enters on the next beat and counts up from 0 over 8 frames.

**F9. Framed layout** (`layout: {"type":"card","bg":{…pattern…},"rect":[0.17,0.12,0.66,0.76],"radius":0.04,"shadow":true,"bg_cycle_s":2.5}`)
- Footage is scaled into a rounded card over a patterned or designed background. The background changes on the beat every `bg_cycle_s`.
- The same mechanism covers the "Before/After" portfolio wrapper: two cards plus `Before`/`After` pill labels. That is useful for Klaus selling TITAN editing services.

**F10. Stills explainer mode** (`mode: "stills_explainer"`)
- Input is a VO (or TTS) plus an ordered list of illustration stills (generated under the studio gates with one style key, or supplied).
- Each still gets a continuous `camera` move (`push`, `pull`, `pan_l/r`, from/to rect) eased in-out. Consecutive stills join by a `zoom_through` (end-scale of A = start of B, 8-frame cross-dissolve) so there are no visible cuts.
- Optional 2-3 depth layers per still (PNG with alpha) for parallax.
- Also: `loop_end: true` ends on the first still's opening framing, plus the serif-title + subtitle captions and F4 stamps.
- Real character animation stays a Higgsfield job (Seedance i2v per still). The editor only assembles it.

## 6. Proposed presets (JSON, schema of tools/editor/presets; new keys marked `_needs_feature`)

### mograph-metaphor-interview (ed01)
```json
{
  "name": "mograph-metaphor-interview",
  "label": "Interview → 3D metaphor motion graphics (two-tier glow captions)",
  "kind": "style",
  "description": "From ref ed01 mahdiology.edit: sit-down interview clip; two-tier captions (small light setup words + big glowing yellow/orange payoff) that move beside the head; full-screen warm 3D 'desk still-life' metaphor inserts (~36% of runtime) with elements popping on per keyword; one colour-wash transition; hard punch-in for the final number.",
  "reference": "research/refs-2026-10-25/editors-A.md#ed01",
  "pacing": { "remove_silence_over_s": 0.35, "pad_s": 0.08, "remove_fillers": "hard", "max_shot_s": 8.0 },
  "captions": {
    "enabled": true, "font": "DejaVu Sans", "bold": true, "size": 0.045, "color": "#FFFFFF", "highlight": "#F2E15A",
    "outline": 0, "shadow": 0, "position_y": 0.66, "max_words": 5, "animation": "pop", "uppercase": false, "keyword_caps": false,
    "_needs_feature": {
      "tiers": { "setup_scale": 0.5, "setup_alpha": 0.15, "payoff_scale": 1.0, "payoff_font": "serif_italic", "order": "setup_first", "alt_highlight": "#F5A623" },
      "glow": { "color": "#F2E15A", "blur": 6, "radius": 4, "alpha": 0.45 },
      "animation": "blur_in",
      "avoid_face": true, "alt_positions": [[0.74, 0.25]]
    }
  },
  "hook_text": { "enabled": false },
  "zoom": { "mode": "smooth", "every_s": 4.0, "scale": 1.05, "on_hook": 1.0, "on_emphasis": true, "_needs_feature": { "final_punch_scale": 1.35 } },
  "broll": { "every_s": 6.0, "max_dur_s": 6.3, "min_dur_s": 2.3, "mode": "full",
    "_needs_feature": { "source": "metaphor_stills", "style_key": "photoreal 3D still life, top-down cream desk, soft window-shadow light, warm", "build_on": "pop_per_keyword" } },
  "sfx": { "density_per_10s": 2.0, "db": -14, "map": { "hook": "pop", "zoom": "whoosh", "broll": "whoosh", "title": "pop", "end": "riser" },
    "_needs_feature": { "map": { "transition": "shimmer", "element": "pop" } } },
  "music": { "energy": "low", "db": -21, "duck": true },
  "grade": { "contrast": 1.06, "saturation": 1.0, "warmth": 0.0, "vignette": true, "_needs_feature": { "bottom_gradient": 0.3 } },
  "end_card": { "enabled": false },
  "_needs_feature": { "transitions": [{ "type": "color_wash", "colors": ["#E040A0", "#8040E0"], "dur_s": 0.5, "on": "summary_line" }] }
}
```

### neon-mograph-cards (ed02)
```json
{
  "name": "neon-mograph-cards",
  "label": "Neon mograph cards (CEO / agency talking head)",
  "kind": "style",
  "description": "From ref ed02 editvibez12: selfie talking head ~34% / designed cards ~66%; dark teal cards with cyan glow, depth text behind a cut-out of the speaker, type-on bullet list synced to the spoken list, phone mockup of the brand profile; captions = small white lead words + huge wide-black cyan glowing keyword; 2-4 frame glow-flash transitions.",
  "reference": "research/refs-2026-10-25/editors-A.md#ed02",
  "pacing": { "remove_silence_over_s": 0.3, "pad_s": 0.06, "remove_fillers": "hard", "max_shot_s": 3.0 },
  "captions": {
    "enabled": true, "font": "DejaVu Sans", "bold": true, "size": 0.07, "color": "#FFFFFF", "highlight": "#00E0F0",
    "outline": 0, "shadow": 0, "position_y": 0.69, "max_words": 3, "animation": "pop", "uppercase": false, "keyword_caps": true,
    "_needs_feature": {
      "tiers": { "setup_scale": 0.43, "payoff_scale": 1.0, "payoff_font": "wide_black", "order": "setup_first" },
      "glow": { "color": "#00E0F0", "blur": 8, "radius": 5, "alpha": 0.4 },
      "accent_font": "hand"
    }
  },
  "hook_text": { "enabled": false },
  "zoom": { "mode": "snap", "every_s": 0, "scale": 1.3, "on_hook": 1.0, "on_emphasis": true },
  "broll": { "every_s": 0 },
  "sfx": { "density_per_10s": 3.0, "db": -12, "map": { "hook": "bass", "zoom": "impact", "broll": "whoosh", "title": "pop", "end": "riser" },
    "_needs_feature": { "map": { "transition": "flash", "bullet": "typewriter", "element": "pop" } } },
  "music": { "energy": "high", "db": -20, "duck": true },
  "grade": { "contrast": 1.05, "saturation": 1.05, "warmth": 0.0 },
  "end_card": { "enabled": false },
  "_needs_feature": {
    "scenes": { "every_s": 3.5, "palette": { "bg": "#001020", "accent": "#00E0F0" }, "bg": "beam",
      "layer_kinds": ["condensed_headline_behind_subject", "bullets_typewriter", "device_iphone", "mono_illustration"], "corner_swoosh": true },
    "transitions": [{ "type": "flash", "color": "#9FF8FF", "frames": 3, "on": "segment_change" }],
    "cutout": true,
    "fonts": { "headline": "condensed", "keyword": "wide_black", "accent": "hand" }
  }
}
```

### scrapbook-bobblehead (ed03)
```json
{
  "name": "scrapbook-bobblehead",
  "label": "Girly scrapbook + bobblehead mascot (Gen Z / divas)",
  "kind": "style",
  "description": "From ref ed03 ruth.the.crafter: music-led; a bobblehead mascot (face cut-out ~2x on a small body) hosts the intro then lives bottom-left as a persistent cut-out PIP; one-word captions whose look changes per scene (rounded sans, arched handwriting, white sticker labels); pastel pattern backgrounds (stripes/gingham/stars/plaid) swapping on the beat with a rounded card window cutting clips every ~0.8 s; yellow kinetic stat stack; pixel-cursor reveal and magic-wand wipe.",
  "reference": "research/refs-2026-10-25/editors-A.md#ed03",
  "pacing": { "remove_silence_over_s": 0.4, "pad_s": 0.06, "remove_fillers": "hard", "max_shot_s": 0.9 },
  "captions": {
    "enabled": true, "font": "DejaVu Sans", "bold": true, "size": 0.06, "color": "#FFFFFF", "highlight": "#9ACD32",
    "outline": 0, "shadow": 2, "position_y": 0.16, "max_words": 1, "animation": "pop", "uppercase": false, "keyword_caps": false, "emoji": false,
    "_needs_feature": { "font": "rounded", "styles_by_scene": ["rounded", "arc_hand", "label_hand", "display_lime"], "label": { "bg": "#FFFFFF", "text": "#111111", "tilt_deg": 4 }, "arc_deg": 40 }
  },
  "hook_text": { "enabled": false },
  "zoom": { "mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false },
  "broll": { "every_s": 0.8, "max_dur_s": 0.9, "min_dur_s": 0.4, "mode": "full", "_needs_feature": { "mode": "card_window" } },
  "sfx": { "density_per_10s": 4.0, "db": -12, "map": { "hook": "pop", "zoom": "whoosh", "broll": "whoosh", "title": "pop", "end": "riser" },
    "_needs_feature": { "map": { "cursor": "click", "transition": "sparkle", "label": "pop" } } },
  "music": { "energy": "high", "db": -14, "duck": true, "_needs_feature": { "beat_sync_cuts": true, "genre_hint": "cute pop / hyperpop" } },
  "grade": { "contrast": 1.04, "saturation": 1.15, "brightness": 0.02, "warmth": 0.05 },
  "end_card": { "enabled": false },
  "_needs_feature": {
    "layout": { "type": "card", "rect": [0.17, 0.12, 0.66, 0.76], "radius": 0.04, "shadow": true, "bg_cycle_s": 2.5,
      "patterns": ["stripes_pink_cream", "gingham_green", "stars_pink", "plaid_pink"] },
    "mascot": { "type": "bobblehead", "head_scale": 2.0, "persistent_corner": "bottom_left", "prop": "laptop" },
    "stat_stack": { "num_color": "#F5F000", "count_up": true },
    "transitions": [{ "type": "pixelize", "on": "intro" }, { "type": "wand", "on": "intro_to_reel" }]
  }
}
```

### illustrated-explainer-noir (ed10)
```json
{
  "name": "illustrated-explainer-noir",
  "label": "Illustrated noir explainer (faceless founder / startup)",
  "kind": "style",
  "description": "From ref ed10 getclayhook: faceless VO over 2.5D vector illustrations on near-black with spotlight pools and ONE lime accent; continuous camera push/pull between scenes, no hard cuts; serif chapter titles with italic lime keyword at top, small white sans subtitles at bottom with italic-lime emphasis words; Exhibit A/B museum plaques for sources; stamps; loop ending on the first frame.",
  "reference": "research/refs-2026-10-25/editors-A.md#ed10",
  "pacing": { "remove_silence_over_s": 0.45, "pad_s": 0.1, "remove_fillers": "hard", "max_shot_s": 4.0 },
  "captions": {
    "enabled": true, "font": "DejaVu Sans", "bold": true, "size": 0.028, "color": "#FFFFFF", "highlight": "#C0F000",
    "outline": 0, "shadow": 0, "position_y": 0.81, "max_words": 5, "animation": "fade", "uppercase": false, "keyword_caps": false,
    "_needs_feature": { "font": "clean_sans", "emphasis_font": "serif_italic" }
  },
  "hook_text": {
    "enabled": true, "max_words": 5, "font": "DejaVu Serif", "bold": true, "size": 0.04, "color": "#FFFFFF", "outline": 0,
    "position_y": 0.19, "dur_s": 1.0, "uppercase": false,
    "_needs_feature": { "accent_last_word": { "font": "serif_italic", "color": "#C0F000" }, "chapter_titles": true }
  },
  "zoom": { "mode": "smooth", "every_s": 2.2, "scale": 1.15, "on_hook": 1.0, "on_emphasis": false,
    "_needs_feature": { "hook_move": "pull_back", "hook_from_scale": 2.2, "join": "zoom_through" } },
  "broll": { "every_s": 0 },
  "sfx": { "density_per_10s": 1.5, "db": -14, "map": { "hook": "whoosh", "zoom": "whoosh", "broll": "whoosh", "title": "pop", "end": "riser" },
    "_needs_feature": { "map": { "stamp": "stamp", "element": "pop" } } },
  "music": { "energy": "low", "db": -22, "duck": true },
  "grade": { "contrast": 1.05, "saturation": 1.0, "vignette": true },
  "end_card": { "enabled": false },
  "_needs_feature": {
    "mode": "stills_explainer",
    "palette": { "bg": "#1A1416", "spot": "#302020", "accent": "#C0F000" },
    "style_key": "2.5D flat vector illustration, near-black warm background, soft spotlight pools, single lime #C0F000 accent, rounded cute props",
    "devices": ["exhibit_plaque", "stamp", "marquee"],
    "watermark": { "corner": "top_left", "shape": "circle_logo" },
    "loop_end": true
  }
}
```

Notes on the numbers:
- Sizes are fractions of frame height, measured from the inner After window and normalised to a full 9:16 frame.
- Colours are sampled from frames, except ed01 yellow/orange, which were read by eye from the glow text [inferred ±10 %].
- Zoom scales of 1.3/1.35 come from face-size ratios by eye [inferred].
- Music dB levels are [inferred] from the LUFS and voice density. ed03 music is louder because it is music-led at 38 wpm.

## 7. Build order (impact ÷ effort)

1. **F6 font pack + F1 two-tier/glow captions + blur_in.** These touch ed01, ed02 and ed10 and are pure ASS/PIL work.
2. **F5 transitions** (flash, color_wash, wipe/pixelize via xfade). Cheap ffmpeg work used by three refs.
3. **F4 scene cards** (text/kicker/bullets/stat/device/image/stamp layers with `at_word`). This is the core of the "mograph" look and absorbs F8.
4. **F3 cut-out** (behind-subject text, alpha PIP, bobblehead).
5. **F9 framed layout** (also gives us the Before/After portfolio wrapper for selling TITAN editing).
6. **F2 face-aware placement.**
7. **F10 stills explainer** (needs generated illustration stills through the normal Higgsfield gates first).
