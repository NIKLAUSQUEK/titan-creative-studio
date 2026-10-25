# Thumbnail, cover and carousel design (stills that stop the scroll)

Knowledge base for the `thumbnail-designer` agent (draft at the end of this file). Researched 2026-10-25.
It builds on, and does not replace:
- `higgsfield-creative-director/references/playbook-carousel.md` (the 5-rule carousel playbook),
- `higgsfield-youtube-thumbnail/SKILL.md` + its `references/thumbnail-frameworks.md` (16 concept frameworks, truthfulness law) and `references/text-overlay-bake.md` (5 overlay presets),
- `higgsfield-creative-director/references/photo-effects.md` (image-edit prompts and film/texture looks),
- `distribution.md` (packaging, captions, alt text) and `compliance-sg.md` / `compliance-packs.md` (claims rules).

**Evidence labels.** Each non-obvious claim has a source and access date. **RoT** = practitioner rule of thumb with no published data behind it. **[inferred]** = our own reasoning. **[to verify from Klaus's screenshots]** = something we could not see, because Instagram blocks downloads here. We do not log in to Instagram, scrape it or bypass it. Platform UI changes often, so re-check specs in-app before a big batch.

---
## 0. The reference accounts: what public sources show

| Account | What public sources confirm | Look (not verified) |
|---|---|---|
| @theobsession | Probably the media arm of **OBSN ("Obsession")**, Steven Bartlett's Steven.com + Authentic venture, launched Sep 2026. It is described as "news, analysis and live experiences focused on the creator economy", with "more than one million followers on Instagram" (pulse2.com, 2026-09-15). The handle-to-OBSN match is **[inferred]**: the article names no handle. The example hook Klaus quoted ("Jeff Nippard entered 2026 expecting it to be the biggest year of his career…") is a narrative, past-tense, expectation→twist opening. | Cover layout, type, colour, texture **[to verify from Klaus's screenshots]**. Working hypothesis from the brief: one large portrait of the subject plus a 1-2 sentence story headline. This is pattern P5 below. |
| @builtwithscience | Jeremy Ethier's brand. Its stated mission is to cut through "bro-science" with research-backed training (builtwithscience.com/about-us, accessed 2026-10-25). About 1.3M IG followers (iqfluence.io, accessed 2026-10-25). Its own site shows the "myth" topic Klaus quoted. In a 30-day experiment, one arm was trained daily vs twice weekly. The site itself notes the confound: about 35 vs 10 hard sets a week (builtwithscience.com/fitness-tips/train-a-muscle-every-day, accessed 2026-10-25). | Myth→"WRONG!" reversal structure from Klaus's quote = pattern P1. Fonts, colours and slide count **[to verify from Klaus's screenshots]**. |
| @dr.longevity | No public source ties to the handle. The study Klaus cited is real: Laukkanen et al., *JAMA Internal Medicine* 2015, KIHD cohort, **2,315 Finnish men aged 42-60**, median follow-up ~20.7 y. Compared with 1 session a week, SCD risk was 22% lower at 2-3 sessions and 63% lower at 4-7. Fatal CHD was 23% and 48% lower. All-cause figures were not in the summaries we read, so check the paper before quoting them. The study is observational (men only, Finnish dry sauna) (ScienceDaily 2015-02-23; ACC.org 2015-02-23). | "Study-receipt" structure = pattern P2. Exact card styling **[to verify from Klaus's screenshots]**. |
| "Explore page thumbnail hook" post | Not retrievable. | **[to verify from Klaus's screenshots]**. Ask Klaus for 3-5 screenshots of each account's covers and slides 2-3, then run `editor.py study`-style notes on them. Refs are for study only and are never reused. |

**Lesson the three share [inferred from the hooks Klaus quoted]:**
- Slide 1 is a complete thought that opens a gap: an expectation set up to break, a belief set up to be reversed, or a striking number with its source.
- The design serves that one sentence.
- Trust signals sit inside the design: study name, n, year.

---
## 1. Hook science for a still

### 1.1 The 0.5-second read
- People pull the gist of an image extremely fast. In MIT's Potter lab study, viewers identified an image's concept after seeing it for **13 ms** (MIT News, 2014-01-16). So the picture's *concept* lands almost at once. Text takes longer, which is why words must be few and huge **[inferred]**.
- The rules below are working rules, not proven laws (RoT unless cited).
  1. **One idea.** One focal subject, one headline, one emotion. The existing thumbnail skill uses the same rule: one clear focal subject, no clutter, reads in under a second at ~120 px.
  2. **3-6 words on covers** (2-4 on YouTube, per `text-overlay-bake.md`). Story covers like @theobsession can carry 1-2 sentences, but only if a 3-5-word **anchor phrase** is set 1.5-2x larger. The anchor is the line that reads in 0.5 s.
  3. **Contrast first.** Figure and ground must separate in a grayscale squint. Text needs ≥4.5:1 contrast. Large display text needs ≥3:1, the WCAG 1.4.3 floor for "large" (18 pt / 14 pt bold) (W3C Understanding SC 1.4.3, accessed 2026-10-25). At thumbnail scale every headline is small on screen, so aim for **≥7:1** on covers **[inferred]**.
  4. **Face + emotion when a person is the story.** The Kapwing × NeoMam 2024 count of top creators' thumbnails found surprise and happiness each in ~27% of faces (Tubefilter, 2024-10-24). That is how often they appear, **not** a measured CTR lift. We found no published data proving that "faces raise CTR". Vendor blogs claim it without data, so we test faces instead of assuming.
  5. **Curiosity gap that the content pays off.** This is the truthfulness law in `thumbnail-frameworks.md`. YouTube's own A/B tool picks winners by **watch-time share, not CTR**, because CTR-only winners can mislead (YouTube Help 13861714, accessed 2026-10-25). Bait that loses watch time loses the test.
  6. **Specificity beats adjectives.** Write "2,315 men, 20 years", not "huge study"; "Day 30", not "a while" **[inferred]**. In SG health it is also the compliant route: specific + sourced instead of superlative.
  7. **Numbers** are processed as one glyph-cluster and signal "list / data / receipt" (RoT). Use numerals, not words ("7", not "seven").
- **Truth gate.** No invented outcomes, quotes, screenshots or stats. Same law as the thumbnail skill.

### 1.2 Surface differences

| Surface | What the viewer sees | Design consequence |
|---|---|---|
| IG **Explore grid** | Small tiles in a mixed grid. Some reels tiles are taller **[to verify in-app; layout changes]** | The cover must read as a *tile*: one subject, ≤5 huge words, a strong colour block. The tile is ~1/3 of screen width (~125 px on a 375-pt phone) **[inferred]** |
| IG **feed** | Full width at the post's ratio. 4:5 gives the most height (sources below) | Can carry a longer story headline. People decide whether to swipe from slide 1 *and* the caption's first line |
| IG **profile grid** | Center-cropped to **3:4 (1080×1440)** since the 2025 grid change (Planoly; Kapwing; Hopper HQ 2026-09-18). Sources disagree on the exact rollout date | A 4:5 post loses side strips: keep key content inside the **centered ~1012×1350** area (Planoly / O'Brien Media). A 9:16 reel cover loses **240 px top and 240 px bottom** (Hopper HQ 2026-09-18) |
| IG **Reels cover** | 1080×1920 in the Reels tab, 3:4 crop on the grid | Design the cover for the **1080×1440 middle band**, then check that the 9:16 full frame still looks intentional |
| **TikTok** cover / photo mode | 9:16 full screen. Caption, sidebar and CTA overlays are bottom and right | TikTok says the safe zone depends on caption length and add-ons. Use its downloadable safe-zone files and preview tool (TikTok Business Help "TopView", accessed 2026-10-25). Keep text in the upper-middle (RoT) |
| **YouTube** long-form | 16:9 next to the title, often at small sizes. The duration badge sits bottom-right (third-party guides; not stated on the Help page) | Thumbnail and title must **say different things that add up** (distribution.md). Never put text bottom-right. Make 3 variants for Test & Compare |
| **YouTube Shorts** | 9:16 thumbnail supported (YouTube Help 72431) | Same as the TikTok cover: faces and text in the upper two-thirds (thumbnail skill) |
| **LinkedIn** PDF carousel | Each page shown at the doc ratio in the feed | 4:5 or 1:1 pages. Denser text is OK, but the 1-idea-per-page rule still holds **[inferred]** |

### 1.3 Aspect ratios, pixel sizes and safe zones

| Deliverable | Canvas | Safe zone (keep text + faces inside) | Source |
|---|---|---|---|
| IG carousel slide | **1080×1350 (4:5)** | Center **1012 px** wide band for the grid crop on slide 1. Margins **≥80 px** sides (≈7.4%) and ≥90 px top/bottom (house rule, playbook-carousel.md: 80 px). Third-party guides suggest 150-200 px from the edges for share-to-Stories clipping (Decktopus): use that for slide 1 only | Planoly; Kapwing 2026; Decktopus |
| IG native 3:4 post | 1080×1440 | Full frame survives the grid; feed shows 3:4 | Kapwing 2026; Planoly |
| IG Reel cover / TikTok cover | **1080×1920 (9:16)** | Text and face inside **y = 270…1250 px** (top 14%, bottom 35% reserved), x = 65…850 px (right ~21% rail). The 3:4 grid band is y = 240…1680, so the overlap where text survives *both* is **y 270-1250** | Hopper HQ 2026-09-18 (Meta % safe zones) |
| YouTube thumbnail | **1280×720 minimum target, 3840×2160 max** (16:9). Min width 640. JPG/PNG. **2 MB on mobile upload**, 50 MB desktop | Keep the bottom-right ~20% × 15% clear (duration badge, RoT). Faces on a power third | YouTube Help 72431, fetched 2026-10-25 |
| YouTube Shorts thumbnail | 2160×3840 max (9:16), min height 640 | Faces in the upper two-thirds | YouTube Help 72431 |
| IG carousel length | 1-**20** frames (raised from 10 in Aug 2024) | Our default arcs below are 6-12 | Social Media Today / TechRadar, 2024-08 |

### 1.4 Text-size minimums for mobile
A 1080-px canvas shown on a 375-pt-wide phone is scaled ×0.347. In a 3-column grid tile it is ×~0.116 **[inferred arithmetic]**. Cap height is the visible size, so we size by it. The numbers are house minimums: Krumzi's vendor guide suggests body 28-36 px and headers 40-55 px on 1080 (krumzi.com, accessed 2026-10-25). We set ours higher because covers must also survive the grid.

| Element | At 1080 wide (px) | % of canvas width | On a 375-pt phone (feed) | Note |
|---|---|---|---|---|
| Cover anchor headline (3-6 words) | **≥96 px** font size (cap ≈ 70 px); 110-160 preferred | ≥9% | ≥33 px | Still ~11 px in the Explore tile |
| Cover secondary/story line | ≥56 px | ≥5.2% | ≥19 px | @theobsession-style sentence |
| Inner-slide headline | 64-80 px | 6-7.5% | 22-28 px | |
| Inner-slide body | **≥40 px** (44-48 preferred), ≤40 words/slide | ≥3.7% | ≥14 px | Krumzi: 30-40 words max |
| Source / footer line | ≥26 px, 70% opacity of the text colour but still ≥4.5:1 | ≥2.4% | ≥9 px | A receipt, read on zoom |
| Handle / page number | 26-30 px | | | Fixed position every slide |
| YouTube headline | cap height **12-18% of frame height** (86-130 px cap at 720 h) | | | text-overlay-bake.md |
| Reel/TikTok cover | ≥ 0.05 × 1920 = **96 px** | | | matches textcard `size=0.05` default |

Test: export, view the PNG at **375 px wide** and at **125 px wide**. If the anchor can't be read at 125 px, it fails (QC §5).

---
## 2. Cover / thumbnail pattern library (20 patterns)

**Format of each entry:**
- **Use:** when to use it.
- **Layout:** the layout in words, on a 1080×1350 canvas unless noted.
- **Type:** type treatment, using fonts in `tools/editor/fonts/` (all OFL, except Permanent Marker, which is Apache 2.0, per `tools/editor/fonts/FONTS.md`).
- **Colour/texture.**
- **Examples:** one headline per brand.

**Brand guardrails for the examples:**
- Physio Spot and heal360 are SG health (compliance-sg.md): no testimonials, superlatives, guarantees or inducements. Never assert the viewer's condition: write "ED is common", never "Do you have ED?" (Meta personal-attributes rule, compliance-sg §3).
- PeachForm is fitness/body image: no before/after miracle framing.
- Power Protein is VN food: confirm local claim rules.
- Stats only with a source line.

**P1. Myth → "WRONG!" reversal** (@builtwithscience structure)
- **Use:** a widely held belief that the evidence contradicts. It makes the best slide 1 for education. Use it only when you have a source.
- **Layout:** top 55% is the belief as a quote ("We all know…, right?"), centred. Bottom 45% is a huge stamp, "WRONG." or "NOT QUITE.", rotated -6°, overlapping the quote's last line.
- **Type:** quote in Poppins Bold 64 px, sentence case. Stamp in Anton 220-280 px CAPS, letter-spacing -1%.
- **Colour/texture:** off-white paper (#F4EFE6) with grain. Stamp red #C8102E: 5.14:1 on that paper, passes. Optional halftone dot overlay on the stamp's edges (ink-stamp feel).
- **Examples:**
  - Physio Spot: "Kegels are only for women, right?" → **NOT QUITE.**
  - heal360: "Rest it until the pain is gone?" → **NOT ALWAYS.**
  - Power Protein: "Protein after 9pm turns to fat?" → **MYTH.**
  - PeachForm: "Squats alone build glutes?" → **NOT ALONE.**
  - TITAN.AI: "AI content all looks the same?" → **ONLY IF YOU LET IT.**
  - Klaus: "You need a big team to scale?" → **WRONG.**

**P2. Study-receipt card** (@dr.longevity structure)
- **Use:** one study with a striking, honest number. Health brands' strongest cover, because evidence replaces superlatives.
- **Layout:** top band (12%) is a kicker label ("NEW-ISH STUDY" / "20-YEAR STUDY"). Middle is the big number, 40% of the canvas height. Under it, a 2-line plain-language result. Bottom 10% is a receipt strip: journal, year, n, design ("JAMA Intern Med 2015 · n=2,315 men · observational").
- **Type:** number in Archivo Black 300-420 px. Result line in Instrument Serif 60 px. Receipt in Space Grotesk 26-28 px, monospaced feel, letter-spaced +4%.
- **Colour/texture:** a dark warm field (#1A1410) with a paper "receipt" card at 92% opacity, a torn/perforated top edge and a faint drop shadow.
- **Examples:**
  - heal360: "**2,315 men. 20 years.** What regular sauna use was linked to." (sauna, observational wording)
  - Physio Spot: "**1 in 3?** How common pelvic floor issues are in men" (fill only with a sourced figure, else cut)
  - Power Protein: "**1.6 g/kg**: where muscle gains plateaued in one meta-analysis" (source required)
  - PeachForm: "**10 weeks, ~200 lifters**: 3 vs 6 days a week" (Built With Science experiment, credit them)
  - TITAN.AI: "**[n] posts tested**: what actually lifted saves" (own data only)
  - Klaus: "**I tracked 365 days of posting.** Here's the curve."

**P3. Before → after split** (process, not miracle)
- **Use:** a change in technique, setup, edit or design. For health and fitness brands it shows a *process* (posture cue, form fix, workspace), **never a patient or body result**.
- **Layout:** a vertical split 50/50. On 16:9 use left/right. On 4:5 use top/bottom, which reads better at phone scale **[inferred]**. Labels "BEFORE / AFTER" or "WRONG / RIGHT" sit in the corner pills. An arrow crosses the seam.
- **Type:** labels in Bebas Neue 64 px in white pills (box style).
- **Colour/texture:** left half desaturated −60% with a cool cast; right half full colour. A 6-px seam in the brand accent.
- **Examples:**
  - Physio Spot: "How you sit vs how you should" (posture)
  - heal360: "Desk setup: wrong / right"
  - Power Protein: "Same calories, 2× protein" (meal swap)
  - PeachForm: "Hip hinge: wrong / right" (form, not body)
  - TITAN.AI: "Raw footage → our edit"
  - Klaus: "My 2019 office vs today"

**P4. Big-number stat**
- **Use:** one number that is the whole story (time, money, count).
- **Layout:** the numeral fills ≥50% of the width, centred-left. A 3-5-word unit line under it. The subject's photo is cut out, small, bottom-right, looking at the number.
- **Type:** Archivo Black or Anton at 400-600 px. Unit in Poppins Bold 72 px.
- **Colour/texture:** a solid brand field with the number in high-contrast ink; or the number filled with an image (P13).
- **Examples:**
  - Physio Spot: "**6 weeks**: a typical pelvic-floor programme length" (sourced/clinic-protocol wording, no outcome claim)
  - heal360: "**8 hrs** sitting. 3 moves."
  - Power Protein: "**40 g** protein. 1 bowl."
  - PeachForm: "**12 sets** a week. Enough?"
  - TITAN.AI: "**1 shoot → 47 posts**"
  - Klaus: "**$0 → 6 brands**"

**P5. Story-portrait with headline** (the @theobsession hypothesis, to verify)
- **Use:** stories about a person (founder, creator, staff, Klaus): expectation → twist.
- **Layout:** a full-bleed portrait. The face sits in the top 55%, eyes on the upper third. A bottom gradient goes from 0% to 85% black over the lower 45%. Headline: 1-2 sentences, left-aligned in the bottom 35%. The **anchor phrase** is bold or highlighted, the rest regular.
- **Type:** Instrument Serif 64-72 px for the sentence, with the anchor in Poppins ExtraBold or the same serif in italic, 1.4× size. Or all sans: Poppins Regular plus ExtraBold for the anchor.
- **Colour/texture:** a muted, slightly warm grade with light grain (3-4%). The anchor gets a highlighter colour or white on a thin accent underline. The handle is small, top-left.
- **Examples:**
  - Physio Spot: "Nik spent 8 years treating athletes. **Then men started asking the question nobody asks.**"
  - heal360: "She thought a sprained ankle heals itself. **Six months later it still clicked.**" (generic composite, labelled dramatisation, no real patient)
  - Power Protein: "He opened a protein café in Saigon. **Nobody ordered protein.**"
  - PeachForm: "She trained glutes 5 days a week. **They stopped growing.**"
  - TITAN.AI: "An agency with no editors. **It ships 300 videos a month.**" (only if true)
  - Klaus: "I entered 2026 expecting my biggest year. **Then I closed the clinic for a month.**" (only if true)

**P6. Cut-out subject over texture**
- **Use:** a person or product as hero with a graphic, editorial feel. It does well in Explore because it is not "just a photo" **[inferred]**.
- **Layout:** the subject is cut out (rembg or Higgsfield `remove_background`) and placed on a textured field. A 10-14 px white "sticker" stroke plus a hard drop shadow (offset 12 px, blur 0, 35%). The headline sits *behind* the head (image-in-front-of-text depth trick), with ≤30% of the letters hidden.
- **Type:** Anton 200+ px CAPS behind the subject. A secondary line in front, in Poppins Bold.
- **Colour/texture:** paper, risograph or halftone field in 1-2 brand colours.
- **Examples:**
  - Physio Spot: Nik cut-out, "**PELVIC FLOOR**" behind, "men have one too" in front
  - heal360: "**RECOVERY**" behind a physio cut-out
  - Power Protein: a bowl cut-out, "**40G**" behind
  - PeachForm: an athlete cut-out mid-hinge, "**HINGE**" behind
  - TITAN.AI: a laptop cut-out, "**AUTOPILOT**" behind
  - Klaus: Klaus cut-out, "**FOUNDER MODE**" behind

**P7. Paper / grain / halftone / risograph**
- **Use:** to make digital content feel printed, human and premium. A counter-trend to glossy AI looks **[inferred]**. Combine it with any other pattern.
- **Layout:** any. The texture sits on top of everything (the multiply/overlay layer).
- **Type:** serif (Instrument Serif or DM Serif Display Italic) for editorial; Bebas Neue for zine.
- **Colour/texture:** risograph = 2 spot inks (e.g. fluorescent pink #FF48B0 and blue #0078BF on cream), mis-registration offset 3-6 px, grain 6-8%. Halftone = 45° dots, cell 8-14 px on 1080.
- **Examples:**
  - Physio Spot: beige risograph, "the muscle men forget"
  - heal360: "your back isn't weak" on newsprint
  - Power Protein: teal/black riso menu card, "eat your macros"
  - PeachForm: peach/plum riso, "glute myths, debunked"
  - TITAN.AI: a black zine, "the AI agency manifesto"
  - Klaus: "notes from year 7" on paper

**P8. Transparency / glass overlay**
- **Use:** a text panel over a busy photo without killing the photo. Also good for the "app UI" premium look.
- **Layout:** a rounded panel (radius 36-48 px) over the lower or middle third. The backdrop is blurred 24-40 px under the panel only. Fill white at 14-22% (or dark at 35-55%), a 1.5-px inner stroke at 35% white, and a soft shadow.
- **Type:** Poppins Bold, or Space Grotesk for TITAN.AI.
- **Colour/texture:** check the text's contrast against the *blurred* backdrop at its worst pixel. Raise the panel opacity until it is ≥4.5:1.
- **Examples:**
  - Physio Spot: the existing end-card panel #EFE3D3 at 88%, "Book an assessment"
  - heal360: a frosted card, "3 signs your desk is the problem"
  - Power Protein: glass over a food shot, "macros: 40P / 55C / 18F"
  - PeachForm: a gym photo with a glass card, "4 cues for your hip thrust"
  - TITAN.AI: a dashboard glass, "what our agents did today"
  - Klaus: a city at night with a glass quote

**P9. Highlighter / scribble annotations**
- **Use:** to point out the one thing in a screenshot, chart or sentence. It adds a human hand to tidy design.
- **Layout:** a highlighter swipe behind 1-3 words: a slightly skewed rectangle, ±2°, rough ends, multiply blend, about 55% opacity. A hand-drawn circle or underline, an arrow, and a margin note in a marker font.
- **Type:** marker = Permanent Marker or Caveat Brush, 54-72 px.
- **Colour/texture:** highlighter yellow #FFE600 (14.9:1 behind #111 text), lime #D4FF3F, or brand peach #FFB38A behind plum text (8.5:1).
- **Examples:**
  - Physio Spot: "common" highlighted in "ED is common and treatable"
  - heal360: a circled line in a posture study
  - Power Protein: a nutrition label with "PROTEIN 42g" circled
  - PeachForm: "progressive overload" underlined three times
  - TITAN.AI: one KPI circled on a client report (own data, client consent)
  - Klaus: "this sentence changed my business" scribbled beside a book quote

**P10. Newspaper / headline mock**
- **Use:** "news" energy for a real development: a guideline change, a study, a company milestone.
- **Layout:** a masthead (a generic invented name, *never a real paper*), a date line, a big headline, a deck, a column-rule photo, and newsprint.
- **Type:** headline DM Serif Display or Instrument Serif 120 px; deck in Poppins Regular 40 px; masthead in blackletter-free serif CAPS.
- **Colour/texture:** newsprint #ECE7DD, halftone photo, ink 90% black, slight paper fold shadow.
- **Truth gate:** the headline must be true and not pose as a real outlet (compliance and Artifact rule: no impersonating real organisations).
- **Examples:**
  - heal360: "**The Sitting Report**: what 8 hours does to your hips"
  - Physio Spot: "**MEN'S HEALTH BULLETIN**: the physio most men don't know exists"
  - Power Protein: "**SAIGON DAILY PROTEIN**: café opens 6am"
  - PeachForm: "**GLUTE GAZETTE**"
  - TITAN.AI: "**AGENTS ARE HIRING**"
  - Klaus: "**LOCAL PHYSIO BUILDS AI AGENCY**"

**P11. Notes-app / tweet screenshot**
- **Use:** confessional, contrarian or founder-voice lines. It reads as native and unpolished.
- **Layout:** a generic notes or post UI card (no real platform logo) centred on a blurred photo or a flat colour. Avatar plus name **of the brand's own person**, the text, small fake-free metadata (no invented likes/views).
- **Type:** system-like sans: Poppins Regular 44 px for the body, Bold 36 px for the name.
- **Colour/texture:** light mode #FFFFFF card on #F2F2F7, or dark #1C1C1E card; soft shadow.
- **Never:** fabricate a third-party tweet, review or DM (the CLAUDE.md "never publish fabricated records" rule and SG testimonial rules).
- **Examples:**
  - Klaus: "Unpopular opinion: your first 100 posts are for you, not them."
  - TITAN.AI: "We fired our editing software. Here's what replaced it."
  - Physio Spot (Nik's note): "Things men tell me only after the door closes:" (no patient detail)
  - heal360: "3 things I check before any back exercise"
  - PeachForm: "Note to self: rest days build glutes too"
  - Power Protein: "Menu idea: what if the bowl came with its macros?"

**P12. Arrow-and-circle callout**
- **Use:** an image with one detail people would miss: a form fault, a label, a UI element.
- **Layout:** the photo full-bleed. A 10-14 px red or yellow circle (an imperfect ellipse) around the detail. A curved arrow from the headline to the circle. The headline sits in the opposite third.
- **Type:** Anton CAPS, or Permanent Marker for a casual tone.
- **Colour/texture:** circle colour picked to contrast the photo. Default #FF2D2D, or #FFE600 on dark photos.
- **Examples:**
  - PeachForm: a knee caving in, "WATCH THE KNEE"
  - heal360: "this is why your shoulder clicks" (generic demo model)
  - Physio Spot: "the muscle under here" (anatomy diagram, not a body photo)
  - Power Protein: "the hidden sugar line" on a label
  - TITAN.AI: "the setting nobody turns on"
  - Klaus: "the line in my contract I'd change"

**P13. Image-in-text / text-as-window**
- **Use:** a bold single word with photographic meaning.
- **Layout:** a giant word (Anton 380+ px) used as a mask over a photo, on a solid field.
- **Colour/texture:** field in a brand colour; the photo inside keeps texture.
- **Examples:**
  - Power Protein: "FUEL" filled with a bowl
  - PeachForm: "STRONG" filled with a gym
  - heal360: "MOVE"
  - Physio Spot: "SPOT IT" filled with the clinic interior
  - TITAN.AI: "SHIP" filled with a timeline
  - Klaus: "2026"

**P14. "X vs Y" comparison**
- **Use:** two options the audience genuinely confuses. Not "us vs competitor": that is a comparative claim, banned for SG health.
- **Layout:** two equal columns or halves, a "VS" roundel at the seam (160 px circle), each side with an icon or photo, a label and a 1-line verdict under it.
- **Type:** labels in Bebas Neue 96 px, VS in Anton.
- **Colour/texture:** two contrasting colours from the palette (e.g. teal vs black for Power Protein).
- **Examples:**
  - heal360: "Heat vs ice"
  - Physio Spot: "Kegels vs reverse Kegels"
  - Power Protein: "Whey vs tofu bowl"
  - PeachForm: "Hip thrust vs squat"
  - TITAN.AI: "Agency vs AI agency"
  - Klaus: "Clinic vs agency: which taught me more"

**P15. Checklist**
- **Use:** save-bait utility content: steps, signs, a packing list.
- **Layout:** title at the top (2 lines), 3-5 rows with tick boxes, one or two rows ticked in the accent, plus "save this" in the corner.
- **Type:** title in Archivo Black 88 px; rows in Poppins Bold 52 px; ticks drawn as vectors, not emoji, for crispness.
- **Colour/texture:** paper or a clean white card; the ticks in the accent.
- **Examples:**
  - heal360: "Desk check: 5 things"
  - Physio Spot: "4 signs it's worth asking a physio" (neutral, educational)
  - Power Protein: "Your 30 g protein breakfast list"
  - PeachForm: "Glute day warm-up ✓"
  - TITAN.AI: "Before you hire an agency: 5 questions"
  - Klaus: "My Sunday reset"

**P16. Timeline**
- **Use:** story carousels (the @theobsession genre): a career, a company or a study history.
- **Layout:** a horizontal or vertical line with 3-5 dated nodes. The current node is enlarged and in the accent; the cover shows the line fading into "?".
- **Type:** years in Space Grotesk Bold 72 px; labels in Poppins 40 px.
- **Examples:**
  - Klaus: "2016 physio → 2021 clinic → 2024 AI → 2026 ?"
  - TITAN.AI: "Week 1 → week 12 of one client"
  - Physio Spot: "How men's pelvic physio became a thing" (sourced history)
  - heal360: "Your ankle: day 1 → week 6" (general rehab phases, not a patient)
  - Power Protein: "Café day 1 → day 100"
  - PeachForm: "12-week block, mapped"

**P17. Question hook**
- **Use:** when the audience already has the question (search intent) or a genuinely open one.
- **Layout:** the question huge, the left 70%; a thinking or curious face, or a prop, on the right third; a question mark as a 600 px graphic, 15% opacity, behind.
- **Type:** Poppins ExtraBold 110 px, sentence case. Never more than 8 words.
- **Compliance:** third person or general for health ("Why do so many men…", not "Do you…").
- **Examples:**
  - Physio Spot: "Why do men avoid this physio?"
  - heal360: "Should it still hurt after 6 weeks?"
  - Power Protein: "How much protein is too much?"
  - PeachForm: "Why aren't my glutes growing?"
  - TITAN.AI: "Can AI really run an agency?"
  - Klaus: "Would I start a clinic again?"

**P18. Kicker / news label** (maps to textcard `kicker`)
- **Use:** an alert or update tone: "⚠️ COMMON MISTAKE", "NEW STUDY", "PART 3".
- **Layout:** a coloured bar (Bebas Neue 56 px) above a 2-3-line headline.
- **Examples:** works with any brand. "PART 2", series covers.

**P19. Repetition / grid of many**
- **Use:** volume or variety ("I tested 12 protein bars"). From thumbnail framework 13.
- **Layout:** a 3×4 or 4×5 grid of the objects with one item highlighted (circled, in colour while the rest are grey).
- **Examples:**
  - Power Protein: "12 bowls, ranked by protein"
  - TITAN.AI: "30 hooks we tested"
  - PeachForm: "16 glute exercises, 1 winner?"
  - heal360: "9 desk stretches"
  - Physio Spot: "6 pelvic floor positions"
  - Klaus: "52 weeks of posting"

**P20. Size difference / scale**
- **Use:** to make an abstract quantity physical (thumbnail framework 14).
- **Layout:** a giant object next to a tiny person or object; the headline names the comparison.
- **Examples:**
  - Power Protein: a giant egg beside a bowl, "1 bowl = 6 eggs of protein" (verify the macros)
  - TITAN.AI: a tiny team next to a mountain of footage
  - heal360: a giant chair, "you sit 8 hrs"
  - PeachForm: a giant dumbbell
  - Physio Spot: an oversized anatomy model
  - Klaus: a tiny Klaus beside a huge to-do list

**Pairing rules [inferred].**
- Combine at most **one layout pattern** (P1-P5, P10-P20) with **one surface treatment** (P6-P9: cut-out, texture, glass, scribble).
- Example combinations: "P2 + P7" (study receipt on paper), "P5 + P9" (portrait + highlighted anchor).
- Three treatments on one cover = clutter.

---
## 3. Carousel storytelling

### 3.1 Why carousels, and the slide-2 rule
- In the 2025 Socialinsider benchmarks, carousels had the highest average IG engagement rate (0.50%), ahead of Reels (0.45%) and images (0.40%) (socialinsider.io, accessed 2026-10-25). An older 22M-post Socialinsider study found 10-slide carousels highest and mixed image+video carousels best. The method and era differ, so don't compare the absolute numbers (Search Engine Journal, 2020 data).
- **Second chance:** per secondhand reports of Adam Mosseri's remarks, a carousel someone didn't swipe can be shown to them again, opening on **slide 2**. It is reported as happening once (Planoly; Jenn Herman via RouteNote, accessed 2026-10-25; no primary Mosseri post found).
- Therefore **slide 2 is a second cover**. It must stand alone as a hook and must not read "continued…".
- **Slide-2 re-hook rules:**
  1. It restates the gap in a new form. A picture if slide 1 was text, a number if slide 1 was a claim.
  2. It carries its own anchor headline at cover size (≥96 px).
  3. It never just repeats slide 1.
  4. It never needs slide 1 to make sense.
  5. It gives a reason to keep swiping ("the 3rd one surprised me", or a partial reveal).
- **Music:** reports say adding music at posting can make a carousel eligible for the Reels tab (Planoly; verify in-app). Brand accounts use licensed/original music only (`/sound`).
- **Originality:** Instagram's 2026 policy extends non-recommendation of accounts that mainly repost others' content to the whole platform. Transform or credit (PetaPixel, 2026-04-30). Our carousels are original builds. A reference creator's slides are never re-posted.

### 3.2 Arcs (slide by slide)

**Story carousel, 8-12 slides** (@theobsession genre: person, expectation, twist, lesson)
1. **Cover**: P5 portrait plus a sentence; expectation set up to break.
2. **Re-hook**: the twist teased in a new form (a P4 number or a P11 note). "Then [event] happened."
3. **Context**: who they are and the stakes. Image-led.
4. **The rising beat**: what they did, with a specific date or number.
5. **Complication**: what went wrong, or the counter-intuitive choice.
6. **Receipt**: the evidence (a quote they said publicly, a public number, a screenshot of *public* material, credited).
7. **Turn**: the decision.
8. **Result**: outcome (true, sourced).
9. **Lesson**: the takeaway in Klaus's voice (Creator Brain).
10. **Apply it**: 1-3 actionable lines for the reader.
11. **Sources** slide (if the story uses facts about a real person; commentary-controversy.md receipts rules; no AI likeness of real people).
12. **CTA**: follow for part 2 / save / comment a word.

**Myth-buster, 6-8 slides** (@builtwithscience genre)
1. **Cover**: P1 myth → WRONG.
2. **Re-hook**: "Here's what the research actually found" with a P2 number teased.
3. **Why people believe it**: steelman the myth (fair, short).
4. **The evidence**: study card (P2 receipt strip).
5. **What it means**: plain language plus a diagram or illustration.
6. **How to apply**: a P15 checklist.
7. **Caveat**: limits of the evidence (observational? small n? who it applies to).
8. **CTA + source list.**

**Study breakdown, 7-10 slides** (@dr.longevity genre)
1. **Cover**: P2, with the number plus who and how long ("2,315 men, 20 years").
2. **Re-hook**: the most surprising sub-finding (e.g. the dose-response: 4-7 sessions vs 1).
3. **Who was studied**: population, n, age, country, design.
4. **What they measured.**
5. **Finding 1**: a chart (bar or dose-response, built per the `dataviz` skill palette rules).
6. **Finding 2.**
7. **What it doesn't prove**: association ≠ causation, population limits. **Mandatory for health brands.**
8. **What to do**: a safe, general action ("talk to a professional if…").
9. **Full citation slide.**
10. **CTA.**

### 3.3 Rhythm of text-heavy vs image slides
- Alternate density: **heavy → light → heavy**. Never more than 2 text-heavy slides in a row.
- Text-heavy slide: ≤40 words. Image slide: ≤12 words (the house values in `expand.py`: `clean(line, 26 or 12)`).
- Every 3rd-4th slide is a **visual reward**: an illustration, a photo, a chart or a big number (RoT).
- The swipe cue on slide 1 and slide 2: a small "→" or a partial element bleeding off the right edge. The continuous-panorama trick (one image spanning slides 1-2) is a strong cue but conflicts with "slide 2 must stand alone". Use it only when slide 2 still reads alone **[inferred]**.
- Page numbers ("2/9") in a fixed spot, which the renderer already does top-right.

### 3.4 Sourcing slide and source footers
- Any slide with a stat gets a **footer line**: `Source: Laukkanen et al., JAMA Intern Med 2015 (observational, n=2,315 men)`. Space Grotesk 26-28 px, bottom-left, inside the margin.
- The penultimate or last slide lists the full citations (author, year, journal, DOI/URL). The same list goes to `projects/<p>/SOURCES.md` and the caption or pinned comment.
- Health wording: "was linked to", "associated with", "evidence suggests", "for some people". Never "proves", "cures", "guaranteed" (compliance-sg.md §2).

### 3.5 CTA slide
- One action only, matched to the funnel (distribution.md): **save** (utility), **share** ("send to someone who…"), **comment a word**, **follow for part 2**, or a neutral book step for clinics ("WhatsApp us to ask about an assessment").
- No free consults, discounts or "limited slots" on SG health brands.
- Layout:
  - the brand field colour;
  - the CTA verb huge (Anton or Archivo Black 120 px);
  - one sub-line;
  - the handle and logo;
  - the same visual motif as slide 1, which closes the loop.

### 3.6 Consistent visual system (decide before slide 1; store in `brands/<brand>.md` edit-brand block)

| Token | Default (4:5, 1080×1350) | Notes |
|---|---|---|
| Grid | 12 columns, gutter 24 px, margins 80 px L/R, 90 px top, 110 px bottom | 1012-px centre band for slide 1 |
| Baseline | 8-px grid; line-height 1.15 display / 1.35 body | |
| Type scale (ratio ~1.33) | 28 / 40 / 52 / 72 / 96 / 128 / 170 / 228 px | Use ≤3 sizes per slide |
| Fonts | max 2 families plus 1 accent (marker or italic) | |
| Colour roles | `bg`, `ink` (text), `accent` (≤10% area: highlights, numbers), `muted` (footers), `alert` (WRONG stamp) | Every text/bg pair ≥4.5:1 |
| Motif | one repeated element (a highlighter swipe, a paper texture, a corner tab) | Same on every slide |
| Fixed furniture | handle top-left or bottom-left, page number top-right, source footer bottom-left | Never move between slides |
| Imagery | same model, seed and refs for every illustration; same grade and grain on all photos | playbook-carousel.md rule 3 |

### 3.7 Making "engaging graphics" with our tools
- **Illustrations, textures and backgrounds: generate them *without text*** (playbook-carousel.md rule 3):
  - `gpt_image_2_5` is best for diagrams, posters and exact text when needed. Draft at `quality: low` and finalise at `high`.
  - `nano_banana_pro` is best for faithful edits of real photos (Klaus, staff, product) and cut-out-friendly portraits (photo-effects.md §0).
  - Generate one master style key, then pass it as an `image_references` style ref on every later slide for consistency.
  - Texture plates (grain, paper, risograph and halftone sheets) are generated **once per brand** at 2048×2560, saved to `assets/textures/<brand>/`, and reused at zero cost.
- **Type always goes on in Pillow** (`tools/editor/titan_editor/textcard.py` + `expand.py` `slide()`). AI-rendered text drifts between slides, and the exact strings matter for compliance.
- **Charts** follow the `dataviz` skill rules (one series colour plus a highlight, direct labels, no legend if avoidable). Render them in matplotlib with the brand fonts, export a transparent PNG and composite it.
- **Cut-outs**: Higgsfield `remove_background` (credits) or local `rembg` (free, needs install) **[verify rembg availability on Klaus's PC]**.
- Prompt starters (fill the brackets; add the brand `genre_key` or style key last):
```
TEXTURE PLATE: "Seamless [cream risograph paper / newsprint / recycled kraft] texture, subtle fibres and speckles, even lighting, no folds, no text, no objects, flat top-down scan, 4:5."
HALFTONE ILLUSTRATION: "Editorial halftone illustration of [subject], 2 spot colours [#hex, #hex] on cream paper, visible 45-degree dot screen, slight misregistration, bold simple shapes, generous empty space in the [top 40%] for a headline, no text, no logos."
CUT-OUT-READY PORTRAIT (edit of a real photo, nano_banana_pro): "Using the uploaded photo, keep [face, identity, hair, outfit, expression] exactly the same. Change only the background to a flat seamless [mid-grey] studio wall, soft key light from camera left, clean hair edges, no text."
DIAGRAM (gpt_image_2_5): "Clean flat medical-education diagram of [the male pelvic floor muscles, side view], soft beige and brown palette [#EFE3D3, #6B5544], simple labelled-ready shapes with NO text, white margins, textbook clarity, non-explicit."
STORY BACKDROP: "Moody editorial photo of [empty clinic room at dusk / Saigon street at 6am], shallow depth of field, warm practical light, 35mm film grain, negative space in the lower half for text, no people, no text."
```

---
## 4. Typography, colour and texture recipes

### 4.1 Font pairings (all in `tools/editor/fonts/`, free for commercial use per FONTS.md)

| Recipe | Display | Body / secondary | Accent | Use |
|---|---|---|---|---|
| **Hype** | Anton (CAPS, tracking −1%, line-height 0.9) | Poppins Bold | Permanent Marker | WRONG stamps, YouTube, PeachForm, Klaus |
| **Evidence** | Archivo Black (numbers) | Space Grotesk (receipt), Poppins Regular | Caveat Brush note | Study cards, TITAN.AI, heal360 |
| **Editorial story** | Instrument Serif / Italic | Poppins Regular + ExtraBold anchor | DM Serif Display Italic keyword | @theobsession-style story covers, Klaus founder |
| **Zine** | Bebas Neue | Space Grotesk | Permanent Marker | Risograph, checklists, kicker labels |
| **Friendly** | Fredoka | Poppins | Caveat Brush | Lighter heal360 tips, kids/edu |
| **Physio Spot house** | Playfair Display Italic (brand) | Cormorant Garamond (brand) | none | Brand fixed (brands/physio-spot.md). These fonts are **not in the font pack yet**: install them from Google Fonts into `assets/fonts/physio-spot/`, which `expand.font()` already searches |

Rules:
- ≤2 families plus 1 accent per piece.
- Display weight ≥700, or a naturally heavy face (Anton, Archivo Black), for anything under 80 px.
- Never set body in CAPS.
- Sentence case for story lines; CAPS for 1-3-word stamps.
- Serif for trust and story, condensed sans for urgency **[inferred]**.

### 4.2 Palettes: checked contrast ratios (WCAG formula, computed 2026-10-25)

| Pair (text on bg) | Ratio | Verdict |
|---|---|---|
| Physio Spot #4E3B2E on #EFE3D3 | 8.35 | ✓ all text |
| Physio Spot #6B5544 on #EFE3D3 | 5.52 | ✓ body/footers |
| **White on #EFE3D3** | 1.27 | ✗ never |
| Power Protein black on teal #2ED3C7 | 11.26 | ✓ |
| **White on teal #2ED3C7** | 1.87 | ✗ never put white text on teal |
| PeachForm plum #3B1F2B on peach #FFB38A | 8.52 | ✓ |
| PeachForm plum on cream #FFF4EC | 13.69 | ✓ |
| **Coral #FF6F59 on cream** | 2.53 | ✗ coral = shapes and highlights only, never text |
| **White on coral #FF6F59** | 2.74 | ✗ |
| Ink #111111 on paper #F4EFE6 | 16.49 | ✓ |
| Stamp red #C8102E on paper #F4EFE6 | 5.14 | ✓ |
| Textcard kicker red #E53935 with white text | 4.23 | large text only (≥3:1); fine for ≥56 px bold kickers |
| Lime #D4FF3F on #0B0B0F | 17.0 | ✓ (YouTube Neon Lime preset) |
| Highlighter #FFE600 behind #111 text | 14.9 | ✓ |
| White on electric blue #1F4BFF | 5.99 | ✓ (TITAN.AI suggestion [draft]) |
| Grey #7A7A7A on white | 4.29 | ✗ for small footers. Use #6B6B6B or darker |

Suggested palettes for brands whose palette is still CONFIRM (mark [draft] until Klaus approves):
- **heal360** [draft]: sage #6E8B74, cream #F6F2EA, ink #1E2A24, accent warm sand #D9B98C (shapes only).
- **TITAN.AI** [draft]: near-black #0B0B0F, white, electric blue #1F4BFF, lime #D4FF3F accent.

Run the contrast check before use; the agent computes it with the same formula as above.

### 4.3 Texture overlays (exact settings for the renderer)

| Texture | How | Strength on 1080×1350 |
|---|---|---|
| **Film grain** | Gaussian mono noise σ = 18-28 (of 255), blended overlay or soft-light | 3-5% for photos (story covers); 6-8% for zine/riso. Never on small text: apply it *under* the type layer, or keep type ≥40 px |
| **Paper** | Scanned or generated paper plate, multiply blend | 60-100% opacity on a flat bg; 15-25% over photos |
| **Halftone** | Convert the layer to dots at 45°, cell 8-14 px (fine) / 18-24 px (pop-art) | Use on images or shapes, never on text |
| **Risograph** | 2 spot colours, each layer offset 3-6 px (misregistration), grain 6-8%, slight ink-density noise | Whole slide |
| **Glass panel** | Gaussian blur 24-40 px of the backdrop under the panel, fill white 14-22% or black 35-55%, 1.5 px inner stroke white 35%, radius 36-48 px, shadow 0/12/40 px at 25% | Check the worst-pixel contrast ≥4.5:1 |
| **Gradient scrim** | Linear black 0%→85% over the bottom 40-50% (the current `expand.slide` image kind uses 0→82% over the bottom 50%) | Lets white text sit on any photo |
| **Vignette** | Radial darken to 20-30% at the corners | Pulls the eye to the centre subject |

### 4.4 Transparency rules
1. Text never sits on raw photo detail. It goes on a scrim, a panel, a solid colour or an out-of-focus area.
2. Panel opacity is set by contrast, not taste: raise it until the worst pixel passes 4.5:1.
3. Text-behind-subject: hide ≤30% of each glyph and never the first letter. The word must still be readable in a squint.
4. Max 2 translucent layers stacked. More muddies the image at thumbnail scale **[inferred]**.
5. Logos are never semi-transparent below 80%, and never over faces.

---
## 5. QC checklist (run on every cover, thumbnail and carousel before `/publish`)
```
READ
[ ] 0.5 s test: show the cover for half a second (or glance at the contact sheet); say the idea out loud. If you can't, it fails
[ ] Squint test: blur 8 px / view at 15% size: one focal subject and the anchor words still separate from the background
[ ] 125 px test: the anchor is readable with the cover resized to 125 px wide (Explore tile); YouTube readable at 120 px wide (thumbnail skill)
[ ] 375 px test: every text element is readable at 375 px wide; body ≥40 px and footers ≥26 px on the 1080 master
[ ] Contrast: every text/bg pair ≥4.5:1 (≥7:1 for cover anchors); computed, not eyeballed
CROP / SAFE ZONES
[ ] 4:5 slide 1: key content inside the centre 1012×1350 (grid 3:4 crop)
[ ] 9:16 cover: text/face inside y 270-1250, x 65-850 (Reels UI + 3:4 grid band)
[ ] 16:9: nothing in the bottom-right ~20%×15% (duration badge); faces sharp
[ ] TikTok: checked against TikTok's safe-zone file / in-app preview with the real caption length
STORY
[ ] Slide 2 works as a standalone cover (re-hook rule)
[ ] ≤2 text-heavy slides in a row; one idea per slide; ≤40 words body, ≤12 image slides
[ ] Same grid, margins, fonts, colour roles, motif, handle/page positions on every slide (contact sheet)
[ ] CTA: one action, funnel-matched
TRUTH + COMPLIANCE
[ ] The cover's promise is paid off inside (truthfulness law); no invented stats, quotes, screenshots, UI metrics
[ ] Every stat has a source footer + full citation in SOURCES.md / caption
[ ] SG health (Physio Spot, heal360, any clinic promo): no testimonials, reviews, patient photos or before/after results;
    no superlatives (best, leading, No.1, most trusted); no guarantees (cure, permanent, 100%, "in 3 sessions");
    no free-consult/discount/limited-slot inducements; never assert the viewer's condition; observational studies worded as "linked to"
[ ] Fitness / body image (PeachForm): no before/after miracle framing; form/process only
[ ] Brand forbid_words list (brands/<brand>.md edit-brand compliance) = 0 hits (expand.compliance_hits)
[ ] No real-outlet mastheads, platform logos or fake third-party posts; no AI likeness of real people without consent
[ ] Alt text written per image (distribution.md)
LOOK
[ ] Ran scripts/qc_frames.py / opened the contact sheet and LOOKED at every slide before calling it done (CLAUDE.md)
```
If any line fails, return FIX with the slide number, the exact rule it breaks and the fix. Klaus's version stays A.

---
## 6. Renderer feature list (what `tools/editor` needs), ordered by impact

What exists today:
- `textcard.card()`: 4 styles (outline, box, label, kicker), colour emoji, wrapping, for transparent overlay PNGs on video.
- `expand.slide()`: 2 kinds ("text" = brand colour field + big words + an optional photo strip; "image" = full-bleed photo + bottom gradient + stroked text), page numbers, brand fonts from `assets/fonts/<brand>/`.
- It does **not** yet do: rich text, textures, cut-outs, panels, annotations, masks, footers, or layout templates.

| # | Feature | Why it matters | Spec |
|---|---|---|---|
| 1 | **Layout templates per pattern** (`layout: myth / receipt / story-portrait / bignum / checklist / vs / notes / timeline / question / cta / sources`) | Turns this library into one-command output; today there are only 2 generic kinds | JSON slide spec (§7 step 6) → template function; all positions in % of canvas on the §3.6 grid |
| 2 | **Multi-font rich text** (inline runs: `**bold**`, `*italic*`, `==highlight==`, `[accent]colour[/]`, size step-ups) | The anchor-phrase treatment (P5, P2, P9) needs mixed weight/size/colour in one paragraph | Extend `textcard.runs()` beyond text/emoji to styled spans; line-break aware; baseline-aligned |
| 3 | **Source footer + citation slide** | Compliance: every stat sourced; trust signal for the study genre | `footer: "Source: …"` per slide, Space Grotesk 26-28 px, muted colour checked ≥4.5:1; auto-built sources slide from SOURCES.md |
| 4 | **Contrast + safe-zone + legibility auto-QC** | Catches the failures in §5 before Klaus sees them | Compute WCAG ratio per text box against the sampled bg (worst pixel under the box); flag text outside the safe zones per aspect; render 125 px and 375 px previews into the contact sheet |
| 5 | **Gradient / glass panels** | Text on photos without killing them | Rounded rect, backdrop Gaussian blur under the panel, fill RGBA, inner stroke, shadow; opacity auto-raised until contrast passes |
| 6 | **Cut-out with sticker stroke + drop shadow** | P6, the strongest Explore treatment | Input an RGBA cut-out (rembg local or Higgsfield remove_background); dilate alpha by N px for the white stroke; hard or soft shadow; position by subject bbox |
| 7 | **Texture overlays** (grain, paper, halftone, risograph misregistration, vignette) | The "texturing and colours" Klaus asked for; brand signature | Blend modes multiply / overlay / soft-light on numpy; texture plates from `assets/textures/<brand>/`; per-layer target (under-type by default) |
| 8 | **Highlighter / scribble annotations** | P9 and P12; humanises the design | Skewed rough-edged highlight behind word spans (via rich-text span bboxes); hand-drawn ellipse (jittered Bézier, 10-14 px); curved arrow with an arrowhead; marker-font notes |
| 9 | **Image-behind / in-front-of-text masks** | Text-behind-subject depth (P6) and text-as-window (P13) | Layer order: bg → text → cut-out subject; text glyph mask filled with the image |
| 10 | **Stamp / sticker element** | P1 WRONG stamp, P18 kicker variants | Rotated text block, rough ink-edge mask (noise threshold), optional halftone edge |
| 11 | **Chart compositing** | Study-breakdown slides | matplotlib with brand fonts → transparent PNG → placed in the grid; dataviz palette rules |
| 12 | **UI-card mocks** (generic notes / post card, no real logos) | P11 native look | Rounded card, avatar circle from a brand photo, name, body text, light/dark themes |
| 13 | **Grid crop + multi-aspect export** | One design → 4:5 + 9:16 cover + 16:9 thumb | Re-flow the template per aspect (not a naive crop); export the 3:4 grid preview |
| 14 | **Fonts pack additions** | Brand fonts missing | Add Playfair Display + Cormorant Garamond (OFL) to `assets/fonts/physio-spot/`; keep FONTS.md licences |
| 15 | **Swipe cue / panorama bleed** | Signals "there's more" | Element spanning slides 1→2 split at x = 1080; optional "→" glyph |

---
## 7. Sources (accessed 2026-10-25 unless dated)
- MIT News, "In the blink of an eye" (Potter, 13 ms), 2014-01-16: https://news.mit.edu/2014/in-the-blink-of-an-eye-0116
- W3C, Understanding SC 1.4.3 Contrast (Minimum): https://w3c.github.io/wcag/understanding/contrast-minimum.html
- YouTube Help, Add video thumbnails (specs, fetched 2026-10-25): https://support.google.com/youtube/answer/72431
- YouTube Help, Test & compare thumbnails (watch-time share): https://support.google.com/youtube/answer/13861714
- Hopper HQ, Instagram Reel size 2026 (safe zones as Meta %; 3:4 grid crop), 2026-09-18: https://www.hopperhq.com/blog/instagram-reel-size/
- Planoly, Guide to Instagram's new vertical grid: https://planoly.com/blog/guide-to-instagrams-new-vertical-grid
- Kapwing, Instagram's new grid layout size (2026): https://www.kapwing.com/resources/instagrams-new-grid-layout-size-and-dimensions-2025/
- O'Brien Media, Instagram's Jan 2025 image size change: https://obrienmedia.co.uk/?p=145850
- Decktopus, Instagram carousel size: https://www.decktopus.com/blog/instagram-carousel-size-dimensions
- Krumzi, Instagram carousel size guide (font sizes): https://www.krumzi.com/blog/instagram-carousel-size-guide
- Social Media Today, Instagram expands carousels to 20 frames (2024-08): https://www.socialmediatoday.com/news/instagram-expands-carousels-to-20-frames/723792/
- Planoly, Instagram carousels are making a comeback (slide-2 resurfacing, music → Reels tab): https://planoly.com/blog/instagram-carousels-are-making-a-comeback
- RouteNote, Carousels perform better than single photos (Mosseri remarks, secondhand): https://routenote.com/blog/instagram-carousels-perform-better-than-single-photos-according-to-the-head-of-instagram/
- Socialinsider, Instagram benchmarks (2025 engagement by format): https://socialinsider.io/blog/igtv
- Search Engine Journal, Socialinsider carousel study (22M posts, 2020 data): https://www.searchenginejournal.com/instagram-carousels/379311/
- PetaPixel, New Instagram policies target reposted content, 2026-04-30: https://petapixel.com/2026/04/30/new-instagram-policies-target-reposted-content/
- TikTok Business Help, TopView (safe zone depends on caption length / add-ons): https://ads.tiktok.com/help/article/tiktok-reservation-topview
- Tubefilter, Kapwing emotion-in-thumbnails study, 2024-10-24: https://www.tubefilter.com/2024/10/24/emotion-in-thumbnails-ai-study-kapwing/
- Tubefilter, MrBeast leaked production guide key points, 2024-09-17: https://www.tubefilter.com/2024/09/17/mrbeast-internal-production-guide-leaked-key-points/
- HubSpot, Facebook text overlay (20% rule no longer enforced; low-text ads perform best per Facebook): https://blog.hubspot.com/marketing/facebook-text-overlay
- Pulse 2.0, Steven.com and Authentic launch OBSN, 2026-09-15: https://pulse2.com/steven-com-and-authentic-launch-obsn/
- Built With Science, about: https://builtwithscience.com/about-us/ · train a muscle every day: https://builtwithscience.com/fitness-tips/train-a-muscle-every-day/
- ScienceDaily, Sauna bathing and reduced risk (Laukkanen 2015), 2015-02-23: https://sciencedaily.com/releases/2015/02/150223122602.htm · ACC.org summary: https://acc.org/latest-in-cardiology/articles/2015/02/23/16/10/is-sauna-use-associated-with-reduced-risk-of-cv-events

Gaps (not found publicly; don't cite as fact):
- an official Meta pixel spec for Reels safe zones (only % via third parties);
- an official minimum font size for social graphics;
- any published CTR lift for faces or emotions;
- the visual style of @theobsession, @builtwithscience and @dr.longevity carousels.

---
## Agent draft

Proposed file: `.claude/agents/thumbnail-designer.md` (not yet created; Klaus approves first).

```markdown
---
name: thumbnail-designer
description: Designs scroll-stopping covers, thumbnails and carousels for any brand (IG Explore/feed/Reels covers, TikTok covers and photo mode, YouTube and Shorts thumbnails, LinkedIn PDF carousels): 3 cover concepts from the pattern library, the chosen spec, a slide-by-slide carousel plan, text-free generation prompts, Pillow type specs and a QC pass. Use for "make a thumbnail / cover / carousel", "design slide 1", "story carousel like @theobsession", "myth-buster carousel", "study breakdown carousel", or after /publish asks for a cover brief. Never posts, never spends credits without the cost gate.
tools: Read, Write, Edit, Grep, Glob, WebSearch, Bash
---
Follow `.claude/skills/marketing-engine/references/thumbnail-carousel-design.md` (this playbook), with `.claude/skills/higgsfield-creative-director/references/playbook-carousel.md`, `photo-effects.md`, `.claude/skills/higgsfield-youtube-thumbnail/SKILL.md` (+ `references/thumbnail-frameworks.md`, `text-overlay-bake.md`) for YouTube, `distribution.md` and the brand's compliance pack (`compliance-sg.md` / `compliance-packs.md`).

1. **Read first:** `ledger/learnings.md`; `brands/<brand>.md` (palette, fonts, edit-brand block, compliance pack, forbid_words; CONFIRM fields stay CONFIRM); `brains/<who>/identity/profile.md` when founder-led; the piece itself (`projects/<p>/` BRIEF.md, SCRIPT.md, spec.json, edit recipe or transcript); any existing cover or slides. Ask once: "Is there an existing brief, cover or final cut?" — prior work is the master spec (version A).
2. **Inputs to lock (ask only what's missing, max 3 tappable questions):** the piece's hook and the truthful promise it pays off; platform + surface (Explore/feed/Reels cover/TikTok/YouTube/Shorts/LinkedIn) → aspect and safe zone (§1.3); format (single cover, thumbnail set, or carousel + arc type: story 8-12 / myth-buster 6-8 / study 7-10); who/what appears (real photos of real staff beat generated; consent; no AI likeness of real people); sources for any stat.
3. **Compliance pre-check at idea stage:** apply the brand pack (SG health: no testimonials, superlatives, guarantees, inducements, viewer-condition assertions; fitness: no before/after miracle framing). Every stat must have a source in `projects/<p>/SOURCES.md` or it is cut. Use WebSearch only for public sources; cite URL + date; never log in to, scrape or bypass Instagram or other platforms. Reference creators' posts are studied, never reused.
4. **Three cover concepts:** brainstorm ≥6 internally across the pattern library (§2, P1-P20; YouTube also the 16 frameworks), pick 3 that differ in pattern, not just wording. For each: pattern + treatment (≤1 of each), anchor headline (3-6 words; YouTube 2-4), secondary line, layout in words with % positions, fonts from the pack, colour roles with computed contrast ratios, texture, image source (real photo / generated / cut-out), why it opens a truthful gap, compliance note. Recommend one.
5. **Chosen spec (after Klaus picks, or the recommended one if he says "go"):** write `projects/<p>/design/COVER.md` + `cover.json`: canvas, grid, every element (type, text, font, size px, colour, position %, layer order, effects), safe-zone and crop notes for every export aspect (4:5 + 3:4 grid, 9:16 + grid band, 16:9).
6. **Carousel slide plan (if a carousel):** `projects/<p>/design/SLIDES.md` + `slides.json` — one row per slide: n | role (cover / re-hook / … / sources / CTA) | layout template | headline | body (≤40 words; image slides ≤12) | image/illustration | source footer | density (heavy/light). Enforce: slide 2 stands alone as a second cover; ≤2 heavy slides in a row; a visual reward every 3-4 slides; fixed furniture; one CTA; sources slide when facts are used.
7. **Generation prompts:** text-free image prompts per slide/cover (§3.7 starters; `gpt_image_2_5` for diagrams/posters, `nano_banana_pro` for faithful edits of real photos; one style key reused as reference; texture plates generated once per brand). Type is always set in Pillow (`tools/editor/titan_editor/textcard.py`, `expand.py`) unless Klaus explicitly orders baked text. For YouTube, hand off to the higgsfield-youtube-thumbnail skill flow with the chosen concept.
8. **Cost gate:** never call a generation tool yourself unless the project has an approved spec (`"approved": true`) and a cost quote (get_cost) — the cost-gate hook enforces it. Drafts at the lowest quality first; finals at high only after Klaus approves the draft.
9. **Render + QC:** once assets exist, render with the local renderer (Bash: `tools/editor` commands), build the contact sheet with `scripts/qc_frames.py` and LOOK at it. Run every line of the QC checklist (§5): 0.5 s, squint, 125 px and 375 px tests, computed contrast, crop/safe zones per aspect, slide-2 standalone, consistency, truth + compliance, alt text. Return PASS or FIX (slide n, rule, fix). Where the renderer lacks a feature (§6), say which and offer the nearest available treatment.
10. **Output and hand-off:** end with the 3 concepts (one-line each), the chosen spec path, slide plan path, prompts, QC result, alt text per image, and the next command (`/publish` for packaging; `/draft` if generation is pending). Never post, schedule or reply. After delivery ask Klaus's verdict + biggest miss → `/learn`.
```
