# Genre research 2026-10: Class & status (§8), Cautionary / decision ladder (§12), Sci-fi / tech futurism (§16)

Overnight run on 2026-10-25. The goal was to ground, correct and extend three [draft] cards in `.claude/skills/higgsfield-creative-director/references/genre-playbooks.md`. I edited nothing in the playbook or the presets. Klaus decides what moves over.

## Method and caveats
- **Search.**
  - I used WebSearch for the press and research facts. Its `site:instagram.com/reel` queries returned nothing.
  - I used Firecrawl search for the reel URLs (8 calls). I made no Exa calls.
- **Downloads.**
  - I downloaded only public Instagram reels: `yt-dlp --write-info-json`, with one retry after 20 s.
  - Two reels failed. DYuUNQkz7Cp (Dhar Mann) is audience-restricted. Dak612IOzcL (@decisionsthefilm) returned a 429 again after the retry.
  - I used no YouTube, TikTok or Vimeo, no cookies and no workarounds.
  - Media and scripts are in `scratchpad/genreF/` only; nothing went into the repo.
- **Measurements.** Each measurement covers the first 120 s of the reel.
  - **Cuts:** `cropdetect` first, because reposts are letterboxed and an uncropped pass finds 0 cuts. Then `scale=320:-2,select='gt(scene,0.2)',showinfo`, with cuts within 150 ms merged.
    - Dark footage (ThaiHealth) needed a 0.08 threshold. That is marked where it applies.
    - Green-screen composites under-count, because the person layer stays constant.
  - **Loudness:** EBU R128 (integrated LUFS and LRA).
  - **Onsets:** spectral flux, reported as "cuts on onset" (the share of cuts with an onset within ±80 ms).
  - **Words/min:** faster-whisper `small` int8 on CPU, with audio piped from ffmpeg as 16 kHz s16le into numpy.
  - **Frame sheets:** 1 fps (0.5 fps for clips over 64 s). I looked at every sheet.
- **Caveats.**
  - Like counts are the uploader's own. Several reposts or personal accounts show "3 likes" against hundreds of comments, which means the like count is hidden. I treat those as unknown and use the comment count.
  - Loudness of about -14 LUFS is Instagram's normalisation, not the original mix.
  - The machine was shared and overloaded (load average 11-13). I transcribed speech only for the class reels (C1-C8).
  - For the K and S reels, words/min was **not measured**. Their cut and loudness figures come from a pass without transcription.

## Measured reference table

| id | what | URL (upload date, account) | reported performance | dur s | cuts / median shot s | shots by third (s) | other |
|---|---|---|---|---|---|---|---|
| C1 | "Arriving Rich vs Arriving Poor Pt2" (series) | https://www.instagram.com/reel/DYMfm95SuTF/ (2026-05-11, @alz_balaghe) | likes hidden, 16 comments | 11.8 | 1 / 5.9 | – | **two locked takes, same spot, same action** (step out of a car): a red G-wagon, then an old saloon; label "Arriving Rich:" / "Arriving Poor:" mid-frame; the punch is the last frame (the old car is parked beside the G-wagon); music only, LRA 1.2 |
| C2 | "When a rich person talks about their family" (two-hander) | https://www.instagram.com/reel/DWOhh_VCAb_/ (2026-03-23, @clairerammelkamp) | **5,690 likes, 153 comments** | 22.4 | 18 / **1.0** | 1.49 → 0.93 → 0.93 | shot-reverse-shot on the sofa; **same room, same light, same mugs**; class is carried by vocabulary only ("Gangan", "Mootie", "Tug"); persistent white box header at the top + small mid-frame sentence subs; **180 wpm**, words from 0.0 s; no music (LRA 3.9); the last frame is the partner's silent horrified face |
| C3 | "Garib Vs Amir ke bachhe" (Hindi classroom skit) | https://www.instagram.com/reel/DXreK7vDSvH/ (2026-04-28, @gabrusdwivedi) | 494 likes | 22.4 | 8 / 1.6 | 2.49 → 1.24 → 3.73 | the teacher treats the rich and the poor student differently for the same act (the target is the hypocrisy, not poverty); a two-colour bilingual header ("Garib" blue, "Amir" red); cuts on onset 0.75 (cut on the slap/line) |
| C4 | Two fathers, a bridge of money vs a bridge of books (wordless 3D parable) | https://www.instagram.com/reel/DRphLICDPkq/ (2025-11-29, @amjad_amyan__alqaisi) | **5,196 likes, 106 comments** | 52.0 | 9 / 3.6 (fade-heavy, under-counted) | 5.8 → 3.5 → 4.3 | **6 spoken words in 52 s**; a "Watch till the end" header; **locked framing per step** (the same pier and gap each time); close-up reaction inserts; the payoff (yacht vs rowing boat) is held for the last ~10 s; LRA 11.1 (the score swells) |
| C6 | Shabaz Says "I'm Rich, You're Poor: Ice Edition" | https://www.instagram.com/reel/ClEqw-1Arz6/ (2022-11-17, @shabazsays) | likes hidden, 155 comments | 57.5 | 15 / 3.1 | 3.8 → 2.4 → 3.8 | **side-by-side layout**: the creator's selfie on the left, the influencer's clip on the right; in-character satire voice at **171 wpm**, words from 0.0 s |
| C7 | Shabaz Says × **Channel 4** #ChangeClimate (brand collab) | https://www.instagram.com/reel/Czds85lsTIq/ (2023-11-10, @channel4) | **82,939 likes, 1,035 comments** (the top performer in this set) | 50.0 | 5 detected (the background swaps every ~4 s; green screen) / 8.6 | – | **green-screen persona**: the "rich" narrator sneers at "you, the poor" while stock-style rich-life clips play behind; the climate point lands through irony ("We don't care about our carbon footprint. That's for you to worry about. Why? Because you're a povvo."); lime sentence subs; 170 wpm |
| C8 | Shabaz Says "being an idiot for a trend" | https://www.instagram.com/reel/CuDFV_UorJb/ (2023-06-28) | likes hidden, **1,148 comments** | 14.6 | 4 / 3.0 | – | **254 wpm**; a waste-and-hunger contrast in one line |
| K4 | THINK! (UK DfT) 50th-anniversary drink-drive film, AMV BBDO 2014 | https://www.instagram.com/reel/DR_0wyCjFbM/ (2025-12-08, @marketingminutes repost) | repost 85 likes; trade press: "used to devastating effect" (https://www.gigwise.com/videos/95963/, https://lbb.lbbonline.com/news/amv-bbdos-harrowing-spot-marks-50-years-of-drink-driving-ads) | 61.1 | 13 / 2.45 (max 13.5) | 6.8 → 2.6 → 4.1 | **consequence ripple**: crash → fire crew → paramedics → hospital → police at a front door → a mother with a baby; the cast reluctantly sings Kool & the Gang's "Celebration" over it (an ironic tone clash); stat card "deaths fell from 1,640 to 230… but that's still 230 too many" (https://www.thedrum.com/news/think-celebrates-50-years-first-anti-drink-drive-ad); cold night blue → hospital white |
| K5 | ThaiHealth "Phone" anti-drink-drive PSA | https://www.instagram.com/reel/DY84J-VClM5/ (2026-05-30, @marketingmasalaa repost) | **10,585 likes, 45 comments** | 29.6 | 24 (threshold 0.08) / **0.7** | **1.98 → 0.76 → 1.10** | **a ladder of instructions**: a drunk driver phones a friend for directions; every "turn left… go straight" is a step, cross-cut driver ↔ friend, accelerating; the twist: the directions lead into a police checkpoint (the friend set him up); tag "Drink and drive and you will be caught for sure"; dialogue only, dark green sodium night |
| K6 | MCB Camp Pendleton "One decision can change everything" | https://www.instagram.com/reel/DaoKg6zS2K4/ (2026-07-10) | **1,994 likes**, 31 comments | 55.1 | 14 / **0.96** (max 30.1) | **1.8 → 3.1 → 18.4** | decision inserts (keys, phone, a breathalyser-like close-up, a rank chevron) → a **flash-forward crash insert at 6 s** → a 0.7-1 s cut burst at 12-25 s (the friend talks him into driving) → **a 30 s held wide** of the car pulling away under text: "Every day in the United States, 32 people die in drunk-driving accidents." → "Don't be a statistic."; LRA 19.9 |
| S1 | OpenAI "Introducing dots" launch film (official) | https://www.instagram.com/reel/Dd4RMfMJ7kO/ (2026-09-29, @openai) | **50,589 likes, 692 comments** | 147.8 | 59 / **1.71** | **2.0 → 1.74 → 2.11 (flat)** | **warm wood interiors, practical lamps, natural skin, dusk exteriors**; the product is UI on in-world screens and phones, plus playful mascot characters (a blob with a beret, a heart with sunglasses) on big screens; a magenta/blue accent; no cyan, no holograms; cuts on onset 0.37; -14.3 LUFS, LRA 5.5 |
| S2 | Anthropic "A Time and a Place" (Super Bowl 2026, Mother LA) | https://www.instagram.com/reel/DUXlgvHDeZD/ (2026-02-05, @marketingminutes repost) | repost 96 likes; context: the "Keep Thinking" platform, 120 M projected Super Bowl reach (https://www.thestable.com.au/super-bowl-mother-claude-want-you-to-wonder-where-advertising-shouldnt-be/) | 60.2 | 11 / 3.5 (max 14.4) | 3.4 → 6.7 → 4.0 | a comedy skit at a golden-hour park (a trainer and a teen): long held takes, a "VIOLATION" title card; **the product is never shown**; a terracotta end card "Claude / Keep thinking." |
| S3 | Apple "The Mighty Mac mini" (dir. @nicos_yesevil, prod. Blink Ink) | https://www.instagram.com/reel/DcvrOssO2nm/ (2026-09-01, @blink_ink) | 1,680 likes, 61 comments | 43.0 | 13 / – | **one continuous 30.6 s transformation shot**, then a 0.15 s burst, then the packshot | the product is the character: a chip drops in → it grows muscle arms → becomes a race car → an octopus of tools → a rocket; a white seamless void, playful 3D; the end card "The Mighty Mac mini with M6" |
| S4 | World (World.org) "proof of human", BBDO New York | https://www.instagram.com/reel/DYeJgJOzIQj/ (2026-05-18, @iconicads.in repost) | 257 likes (repost) | 60.2 | 27 / **2.0** | **2.87 → 2.01 → 1.54** (accelerates) | a human-history montage (cave painting, Sistine ceiling, the Wright brothers, surgery, a boxer, a flood rescue, an astronaut) → a modern office screen "Human or AI? It's getting harder to tell online." → the product (the Orb) in the last third → a white end card "In a world of AI, be human."; warm film grade |
| S5 | Higgsfield "Ad Multiplier in ChatGPT" launch | https://www.instagram.com/reel/DeM8HKhCQjy/ (2026-10-07, @higgsfield.ai) | 2,917 likes, **772 comments** (comment-to-DM CTA) | 62.9 | 13 / 1.69 (max 21.4) | 5.2 → 3.5 → 3.5 | a story cold open (a woman on a treadmill) → a big title card at 1.7 s → **floating UI cards on a white void** ("Ref video → Result") → CTR curves drawn on black with a **neon-lime** accent → dollar stat cards → back to the story; a CTA line over the final shot |
| S7 / S8 | "Humanoid robots by 2030" stock-montage explainers | https://www.instagram.com/reel/DYHmsbehW3m/ , https://www.instagram.com/reel/Deu3VZBlb2t/ | **1 like each** | 41 / 50 | S7 median 0.17 (stock bursts); S8 one static 50 s shot | – | **a negative control**: generic cyan-robot stock plus stat captions does not perform |

Researched only:
- **Fear-appeal meta-analysis.** Tannenbaum et al. 2015, *Psychological Bulletin* 141(6), 127 articles, N = 27,372, d ≈ 0.29 (https://pubmed.ncbi.nlm.nih.gov/26501228/).
  - Fear appeals work, and the authors found no conditions under which they backfired.
  - Effects are larger when the message includes **efficacy statements**, shows high susceptibility and severity, and recommends a **one-time** behaviour rather than a repeated one.
  - Effects were larger in East Asian samples (per a conference summary).
- **Meth Project "Not Even Once."** Graphic escalating ads.
  - The programme reported falls in use. Independent reviews (Erceg-Hurn 2008, *Prevention Science*) found that use was already falling and found some adverse effects (https://www.sciencedaily.com/releases/2008/12/081211081444.htm).
  - So: **graphic shock without efficacy is not a proven template.**
- **Shabaz Ali ("Shabaz Says").** A Blackburn chemistry teacher.
  - Audience: 1.2 M Instagram and 1.6 M TikTok followers (AFP, 2023); 4 M+ followers by the time of his BBC Three film "Shabaz Asks: Are Billionaires Bad?" (https://www.televisual.com/news/hello-mary-asks-are-billionaires-bad-for-bbc/).
  - The series became a book (PRH 2024) and a podcast.
  - He uses the satire for child-poverty campaigning (https://www.bigissue.com/news/activism/tiktok-shabaz-says-interview-christmas-child-poverty/).
  - This is proof that the persona format scales into brand and broadcaster deals (C7).
- **Anthropic "Keep Thinking" (Mother, Sept 2025).**
  - The hero film opens "There's never been a worse time" over global problems, then turns hopeful.
  - Campaign likened it to Apple's "Think Different" (https://campaignlive.com/article/ad-week-anthropic-hard-questions-mother/1964334; https://www.contentgrip.com/claude-ai-brand-campaign/).
- **Dhar Mann moral-choice shorts.** They report 45-60 B cross-platform views (self-reported; https://en.wikipedia.org/wiki/Dhar_Mann).
  - The structure: unfair judgement or a bad choice → consequence → moment of truth → reconciliation.
  - I couldn't measure one (audience-restricted).

---

### 8. Class & status [measured: C1 https://www.instagram.com/reel/DYMfm95SuTF/ , C2 https://www.instagram.com/reel/DWOhh_VCAb_/ , C3 https://www.instagram.com/reel/DXreK7vDSvH/ , C4 https://www.instagram.com/reel/DRphLICDPkq/ , C6 https://www.instagram.com/reel/ClEqw-1Arz6/ , C7 https://www.instagram.com/reel/Czds85lsTIq/ , C8 https://www.instagram.com/reel/CuDFV_UorJb/ ; deeper: class-status.md]
- **What changed:**
  - **No measured class reel uses split-screen or two colour grades.** The comparison lives in **wardrobe, props, vehicles and vocabulary inside one identical frame/room/light**.
  - The draft's "cut between wallets every 2-3 s, split at the punchline" matches nothing measured. Split-screen is now an option only for simultaneous comparison (an ad A/B), not the default.
  - The top performer (C7, 83 K likes, a Channel 4 brand collab) is a **persona satire**, not a two-wallet split.
- **Four spines** (pick one):
  - **A. Sequential A/B, "Arriving Rich: / Arriving Poor:"** (C1).
    - Two locked takes of 5-7 s, the same spot and the same action, with a label word mid-frame.
    - Punch in the last frame, where the two worlds meet in one shot.
    - Best for 8-15 s loops.
  - **B. Two-hander dialogue** (C2, 5.7 K likes).
    - Shot-reverse-shot, a **1.0 s median** at 180 wpm.
    - A persistent top header names the premise ("When a rich person…").
    - The poorer or normal character is the audience's proxy. End on their silent reaction.
  - **C. Persona satire / reaction** (C6-C8, the Shabaz Says model).
    - The creator plays the out-of-touch rich narrator at 170-250 wpm over a side-by-side or green-screen of real conspicuous consumption.
    - Close with the catchphrase sting.
    - Punch up at the behaviour; the viewer is on the "poor" side.
    - **Brands enter as the topic** (Channel 4 climate).
  - **D. Wordless parable** (C4, 5.2 K likes).
    - Two families or fathers make different choices in the same locked frame per step.
    - Reaction close-ups, then the payoff held ~10 s.
    - Under 10 words; the score carries it. Crosses into §12.
- **Pacing map (20 s, spine B; scale for A/C):**

| Beat | Time | Shot | What |
|---|---|---|---|
| Premise header | 0-2.8 s | the rich character's MCU, words from frame 0 | the header states the class premise; the first line is already absurd |
| Volley | 2.8-15 s | shot-reverse-shot, 0.9-1.0 s shots | each rich line escalates (names, prices, staff); each reply is 1-3 words of confusion |
| Topper | 15-19 s | MCU, a slightly longer hold (1.5-2.8 s) | the most absurd line, delivered casually |
| Reaction button | last 1-2 s | the proxy's face, held, no line | silent horror or the eye-twitch; loop back |

- **Shot grammar:**
  - Spine A: a locked wide from an identical position and height for both takes; the same action beat; a hard cut.
  - Spine B: matched MCU singles at the same lens and eye-line, both inside one real room.
  - Spine C: a 50/50 vertical side layout (creator left, evidence right) or a green-screen with the evidence behind the creator.
  - Spine D: one master framing repeated per step + close-up reaction inserts.
  - Mirrored framing still matters; it is just done sequentially, not split.
- **Look:**
  - One honest grade for both sides (natural or practical light).
  - Class shows in what is in the frame: the car, mugs, coats, the room's clutter, jewellery.
  - Equal dignity: the "poor" side gets the clean, well-lit framing too.
  - Spine D: a soft clay/3D style key.
- **genre_key:** `same camera position, lens and light for both lives, class shown only through wardrobe, props and setting, natural practical light, honest everyday texture, equal dignity for both sides, no glamour grade, no poverty-porn squalor`
- **Shot JSON (spine A):** `{"id":"S02","dur":6,"model":"seedance_2_5","mode":"omni_reference","camera":"locked wide, identical position and height to S01, 24mm","subject":"@DRIVER","action":"start: door opens -> end: steps out of the old saloon in the same slides as S01, nods to camera","environment":"the same hotel forecourt as S01, @LUXURY_CAR now parked beside","light":"identical to S01, night practicals","audio":"engine off, door creak, track continues","constraints":["frame must match S01 composition exactly","old car clean, not squalid"],"genre_key":"<§8 key>"}`
- **Sound:**
  - Spine A: a music track only (LRA 1.2), no VO.
  - Spine B: dialogue only, no bed, one room tone. The silence on the reaction is the punch.
  - Spine C: dense VO (170-250 wpm), with the evidence clip's audio ducked under it.
  - Spine D: a swelling score (LRA ~11), almost no words.
  - Accent stims are optional; ≤1 hit, on the reaction button.
- **Compliance:**
  - Punch at behaviour, systems and hypocrisy (C3's teacher, C7's carbon double standard), never at being poor.
  - The "poor" or normal side is the audience proxy and wins the last look.
  - Stats only from SOURCES.md.
  - Spine C reacts to real people's posts. Use only commentary/fair-dealing-safe clips on personal accounts (Remix/Stitch or written permission, §31 clip-jack rule). For brand accounts, **recreate the evidence with original actors**. No AI likeness of real influencers.
  - SG health brands: no testimonial framing; rich/poor jokes stay off patients and pricing inducements.
- **Preset:** `class-two-wallets` (new; spines A, B, D). `class-persona-satire` (new; spine C). `genz-header-skit` remains the fallback for raw selfie versions.

```json
{
  "name": "class-two-wallets",
  "label": "Class & status: same frame, two wallets (sequential A/B or two-hander)",
  "kind": "genre",
  "description": "Measured 2026-10-25 (C1, C2, C4): one room, one grade, class shown in props and lines. Persistent top header states the premise; small sentence subs; 1.0 s shot-reverse-shot for dialogue or two locked 5-7 s takes with a label word; no music under dialogue; silent reaction button at the end.",
  "reference": "research/genre-research-2026-10/class-cautionary-scifi.md#8",
  "structure": {"name": "class-ab", "target_s": [10, 25], "beats": ["premise header 0-2.8s", "volley / side A", "side B or topper", "silent reaction button"]},
  "pacing": {"remove_silence_over_s": 0.45, "pad_s": 0.06, "remove_fillers": "hard", "max_shot_s": 7.0, "drop_retakes": true},
  "captions": {"enabled": true, "max_words": 8, "animation": "fade", "size": 0.03, "position_y": 0.62, "uppercase": false, "keyword_caps": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "persistent": true, "position_y": 0.16, "size": 0.034, "uppercase": false, "max_words": 10},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0.4, "db": -16, "map": {"end": "boom"}},
  "music": {"energy": "none"},
  "grade": {"contrast": 1.03, "saturation": 1.0, "warmth": 0.0},
  "end_card": {"enabled": false},
  "split_compare_needs_feature": {"mode": "side", "same_timecode_both_halves": true, "note": "optional ad A/B version: both lives play in sync, left/right; B-roll mode side exists but has no synced two-clip compare yet"}
}
```

```json
{
  "name": "class-persona-satire",
  "label": "Class & status: in-character rich narrator over the evidence (side-by-side or green screen)",
  "kind": "genre",
  "description": "Measured 2026-10-25 (C6-C8, Shabaz Says; C7 Channel 4 collab 83K likes): creator speaks in character at 170-250 wpm from frame 0, evidence clip on the right half (side) or behind (greenscreen), lime sentence subs, catchphrase sting at the end. Brand accounts recreate the evidence with original actors.",
  "reference": "research/genre-research-2026-10/class-cautionary-scifi.md#8",
  "structure": {"name": "persona-react", "target_s": [15, 60], "beats": ["catchphrase open 0-2s", "evidence 1", "evidence 2 (escalate)", "the point (system / hypocrisy)", "catchphrase sting"]},
  "pacing": {"remove_silence_over_s": 0.25, "pad_s": 0.04, "remove_fillers": "hard", "max_shot_s": 11.0},
  "captions": {"enabled": true, "max_words": 6, "animation": "fade", "color": "#D7FF6B", "highlight": "#FFFFFF", "size": 0.03, "position_y": 0.66, "outline": 2},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "snap", "every_s": 0, "on_emphasis": false},
  "broll": {"every_s": 4.0, "max_dur_s": 11.0, "min_dur_s": 2.5, "mode": "side"},
  "sfx": {"density_per_10s": 0.5, "db": -16, "map": {"end": "pop"}},
  "music": {"energy": "none"},
  "grade": {"contrast": 1.02, "saturation": 1.0},
  "end_card": {"enabled": false}
}
```

### 8a. Wordless class parable (`class-two-wallets` + score) [measured: C4 https://www.instagram.com/reel/DRphLICDPkq/]
- **Use:** a values piece ("two fathers", "two habits") for a brand that wants to teach without lecturing. It crosses into §12.
- **Pacing:**
  - "Watch till the end" header;
  - 4-6 steps of 4-6 s each in the **same locked master frame**;
  - one close-up reaction per step;
  - the payoff (the two outcomes in one frame) held for 8-10 s.
- **Look:** soft clay/3D, a warm pastel sky, both families drawn with equal care.
- **genre_key:** `soft clay 3D parable, identical locked master frame each step, two families side by side, warm pastel sky, gentle reaction close-ups, wordless, equal dignity`
- **Compliance:** the moral must be about choices anyone can make (time, teaching, patience), never "poor people chose to be poor".

---

### 12. Cautionary / decision ladder [measured: K4 https://www.instagram.com/reel/DR_0wyCjFbM/ , K5 https://www.instagram.com/reel/DY84J-VClM5/ , K6 https://www.instagram.com/reel/DaoKg6zS2K4/ , C4 https://www.instagram.com/reel/DRphLICDPkq/ ; researched: Tannenbaum et al. 2015 https://pubmed.ncbi.nlm.nih.gov/26501228/ ; deeper: mature-edge.md §1]
- **What changed:**
  1. **The rungs accelerate. They don't sit at an even 3-5 s.**
     - K5: 1.98 → 0.76 s per shot as the instructions stack.
     - K6: a 0.7-1 s burst while the friend talks him into it.
     - The consequence is then **held long**: K6 holds 30 s, K4 holds 13.5 s, C4 holds 10 s.
  2. **None of the measured pieces uses on-screen step numbers or a clock-tick bed.** Steps are shown by repetition (the same phone call, the same frame) or by a chain of responders. Numbers stay optional for creator "one bad decision a day" series only.
  3. **The evidence says the ladder needs an efficacy rung.**
     - Fear appeals work best with an efficacy statement and a one-time action (Tannenbaum 2015).
     - The draft ended on "don't be him". Replace that with **one concrete, doable action** ("plan the ride", "get tested this week", "see a physio before week 3").
  4. **Three proven endings:**
     - the ironic ripple (K4, an upbeat song against the aftermath);
     - the comedic catch (K5, a proportionate consequence: caught, embarrassed);
     - the sober flash-forward (K6, a crash insert at 6 s, then a stat card).
- **Pacing map (30 s ad):**

| Beat | Time | Shot | What |
|---|---|---|---|
| Want + flash-forward | 0-3 s | an MCU of the protagonist; a 0.5-1 s insert of the consequence | the ordinary want + a glimpse of where this ends (K6 at 6 s; keep it ≤ 3 s in a reel) |
| Rung 1 (shortcut) | 3-9 s | the master frame, a 2-3 s shot | the first tempting choice, visible as a fork |
| Rungs 2-3 (escalate) | 9-20 s | the same frame or the same call, shots shrinking 1.5 → 0.7 s | each choice compounds; cross-cut the enabler (friend, group chat) |
| Consequence | 20-26 s | one held shot, 4-6 s (organic cut up to 30 s) | a realistic, proportionate cost, held without music hits |
| Efficacy + CTA | 26-30 s | a text card or the brand scene | one stat (sourced) + one one-time action; for brands, the calm brand space |

- **Shot grammar:**
  - Lock one master frame (the car seat, the phone screen, the pier) and return to it at every rung so the decay is visible.
  - Cross-cut the enabler in matched singles (K5).
  - Inserts for the props of each decision: keys, a phone, a glass.
  - The consequence is a static wide or a slow push, never handheld chaos.
- **Look:**
  - Night practicals: K6 is cold blue, K5 sodium green.
  - The grade cools and darkens across the rungs.
  - The consequence is cold and clean (hospital white, a blue-hour wide).
  - The efficacy end switches to the brand's warm, calm look.
- **genre_key:** `consistent locked master framing across every decision, grade cooling and darkening each step, realistic proportionate consequences, night practical light, no glamorising, sober documentary realism`
- **Shot JSON:** `{"id":"S05","dur":5,"camera":"locked wide from the car park lamp, same as S01","subject":"@DRIVER","action":"start: tail lights on -> end: the car pulls out of frame, empty bay remains","light":"blue hour, sodium practicals, cooler than S01","audio":"engine fades, wind; no music","constraints":["no crash shown in this shot","hold ≥4 s"],"genre_key":"<§12 key>"}`
- **Sound:**
  - Pick one bed:
    - **dialogue only** (K5);
    - **an ironic upbeat licensed song** sung or played against the aftermath (K4);
    - **a low drone** that drops to silence on the consequence (K6, LRA 19.9).
  - One low hit on the flash-forward insert only.
  - A clock tick is optional, not default.
- **Compliance:**
  - Stats are sourced and localised. K6's "32 a day" is a US figure; SG needs SPF/LTA numbers.
  - The consequence is proportionate, with no real victims.
  - No crime how-to (mature-edge hard lines).
  - In SG health: no fear-mongering diagnosis or outcome claims; the efficacy rung points to "see a professional", never a discount or free consult.
  - Check the ASAS SCAP clause on fear appeals before paid use (to verify; not checked tonight).
- **Preset:** `cautionary-ladder` (corrected below). Plus `cautionary-ripple` (12a) and `cautionary-twist` (12b).

```json
{
  "name": "cautionary-ladder",
  "label": "Cautionary / decision ladder",
  "kind": "genre",
  "description": "Corrected 2026-10-25 (K4-K6, C4): rungs shown by a repeated locked frame, shots accelerating 2-3 s -> 0.7 s, consequence HELD 4-30 s with no hits, then one sourced stat + one one-time action (efficacy). Grade cools per rung. Clock tick optional.",
  "reference": "research/genre-research-2026-10/class-cautionary-scifi.md#12",
  "structure": {"name": "decision-ladder", "target_s": [25, 60], "beats": ["want + flash-forward 0-3s", "rung 1", "rungs 2-3 accelerating", "consequence HELD", "efficacy stat + action"]},
  "pacing": {"remove_silence_over_s": 0.6, "pad_s": 0.12, "remove_fillers": "hard", "max_shot_s": 30.0},
  "captions": {"enabled": true, "max_words": 6, "animation": "fade", "size": 0.032, "uppercase": false},
  "hook_text": {"enabled": true, "max_words": 7, "uppercase": false, "size": 0.04},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.04, "on_hook": 1.0, "on_emphasis": false},
  "sfx": {"density_per_10s": 0.6, "db": -14, "map": {"hook": "boom", "end": "swell"}},
  "music": {"energy": "low", "db": -22, "duck": true},
  "grade": {"contrast": 1.08, "saturation": 0.85, "warmth": -0.05, "vignette": true},
  "broll": {"every_s": 0},
  "end_card": {"enabled": true, "dur_s": 3.5},
  "transitions": {"default": "dip", "on": "beats", "dur_s": 0.25, "strength": 0.6},
  "grade_ramp_per_beat_needs_feature": {"warmth_step": -0.02, "brightness_step": -0.015, "note": "cool/darken a little at each rung; today the grade is one value for the whole edit"},
  "hold_consequence_needs_feature": {"beat_role": "consequence", "min_hold_s": 4.0, "mute_sfx": true}
}
```

### 12a. Consequence ripple, ironic song (`cautionary-ripple`) [measured: K4 https://www.instagram.com/reel/DR_0wyCjFbM/]
- **Spine:** one bad decision happens off-screen. Then the consequence travels outward through people, each a 2-3 s shot (crash → first responders → hospital → the knock at the door → family). An upbeat licensed song plays straight through, sung by the cast if possible. End on a stat card + one action.
- **Pacing:** a slow open (6.8 s average in the first third), then 2.5 s through the chain, then a 13 s hold on the door/family.
- **Look:** cold night blue → clinical white → a domestic doorway at dawn.
- **genre_key:** `aftermath of one bad decision seen through responders and family, cold night blue to clinical white, restrained documentary realism, no gore`
- **Sound:** the tonal clash IS the device. Brand use needs a licensed track (`/sound`); no trending chart songs on brand accounts.

```json
{
  "name": "cautionary-ripple",
  "label": "Cautionary: consequence ripple with an ironic song",
  "kind": "genre",
  "description": "From THINK! 2014 (K4): aftermath chain through responders and family, ~2.5 s shots after a slow open, upbeat licensed song against it, 13 s hold on the family beat, stat card + action.",
  "reference": "research/genre-research-2026-10/class-cautionary-scifi.md#12a",
  "pacing": {"remove_silence_over_s": 99, "pad_s": 0.0, "remove_fillers": "none", "max_shot_s": 14.0},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "max_words": 8, "uppercase": false, "size": 0.032, "dur_s": 3.0},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.03},
  "sfx": {"density_per_10s": 0.0},
  "music": {"energy": "high", "db": -14, "duck": false},
  "grade": {"contrast": 1.1, "saturation": 0.8, "warmth": -0.06},
  "broll": {"every_s": 0},
  "end_card": {"enabled": true, "dur_s": 4.0}
}
```

### 12b. Comedy-twist ladder (`cautionary-twist`) [measured: K5 https://www.instagram.com/reel/DY84J-VClM5/ (10.6 K likes)]
- **Spine:** the rungs are a repeated exchange (a phone call, a group chat, a sat-nav). Each instruction pushes the protagonist one step further.
  - Cross-cut protagonist ↔ enabler, with shots shrinking from 2 s to 0.7 s.
  - The twist reveals that the enabler steered him into the consequence (caught, embarrassed, at the clinic door).
  - The tagline states the rule plainly.
- **Look:** the night in one practical colour; subtitles mid-frame.
- **genre_key:** `night interior car and bedroom cross-cut, sodium green practical light, naturalistic comic performance, proportionate consequence`
- **Sound:** dialogue only. One hit on the reveal.
- **Fit:** Physio Spot or men's health ("asks the group chat instead of a professional"). Thai/SEA comedic register (localisation.md TH pack).

```json
{
  "name": "cautionary-twist",
  "label": "Cautionary: comedy-twist ladder (cross-cut call, reveal)",
  "kind": "genre",
  "description": "From ThaiHealth 'Phone' (K5): cross-cut protagonist/enabler, shots 2 s -> 0.7 s, dialogue only, one hit on the reveal, plain-rule tagline card.",
  "reference": "research/genre-research-2026-10/class-cautionary-scifi.md#12b",
  "pacing": {"remove_silence_over_s": 0.3, "pad_s": 0.05, "remove_fillers": "hard", "max_shot_s": 5.0},
  "captions": {"enabled": true, "max_words": 7, "animation": "fade", "size": 0.028, "position_y": 0.68},
  "hook_text": {"enabled": true, "max_words": 6, "uppercase": false},
  "zoom": {"mode": "snap", "every_s": 0, "on_emphasis": true, "scale": 1.1},
  "sfx": {"density_per_10s": 0.4, "db": -10, "map": {"zoom": "impact", "end": "ding"}},
  "music": {"energy": "none"},
  "grade": {"contrast": 1.06, "saturation": 0.9, "warmth": -0.03},
  "end_card": {"enabled": true, "dur_s": 3.0}
}
```

---

### 16. Sci-fi / tech futurism (TITAN.AI) [measured: S1 https://www.instagram.com/reel/Dd4RMfMJ7kO/ , S2 https://www.instagram.com/reel/DUXlgvHDeZD/ , S3 https://www.instagram.com/reel/DcvrOssO2nm/ , S4 https://www.instagram.com/reel/DYeJgJOzIQj/ , S5 https://www.instagram.com/reel/DeM8HKhCQjy/ ; negative controls S7 https://www.instagram.com/reel/DYHmsbehW3m/ , S8 https://www.instagram.com/reel/Deu3VZBlb2t/]
- **What changed:**
  - **The draft's "cool cyan volumetric + holographic UI" appears in none of the five strong launch films.**
  - The best performer (S1, OpenAI, 50.6 K likes) uses warm wood rooms, practical lamps and real people, with the product as in-world screens and friendly mascots.
  - Anthropic (S2) and World (S4) use golden-hour, film-grain human scenes and show the product late or never.
  - Apple (S3) makes the product a playful character on a white void.
  - Only the 1-like stock explainers (S7, S8) look like the draft.
  - **Rule: futurism is shown through human benefit in a recognisable present, with one bold brand accent. The sci-fi look is now a sub-style (16c) for explicit concept pieces only.**
- **Three spines** (pick one):
  - **A. Human-day film** (S1). A person's ordinary day, helped; UI on real screens; median ~1.7 s, flat across thirds; the brand card at the end.
  - **B. Humanity montage → problem → product** (S4). Accelerating 2.9 → 2.0 → 1.5 s; the product enters in the final third; a white end card with one line.
  - **C. Product-as-character one-take** (S3). One continuous 20-30 s transformation, a 0.2 s burst, then the packshot. Also see the 16b UI-proof launch.
- **Pacing map (45 s, spine A):**

| Beat | Time | Shot | What |
|---|---|---|---|
| Cold open in the world | 0-3 s | a wide of a real space at dusk; the name card ≤1 s | no claim yet; a place and a person |
| Ask | 3-12 s | MCU, 1.5-2 s shots | the person asks the product for something ordinary |
| Product acts | 12-30 s | alternate screen inserts ↔ the human reaction, ~1.7 s | the product does the work in-world (screen, phone, a mascot); a reaction smile is the proof |
| Scale up | 30-40 s | wider, new locations | the same help, now bigger (a team, a city) |
| Brand card | last 3-5 s | a solid brand colour, logo + line | one line ("Keep thinking." / "be human."); no feature list |

- **Shot grammar:**
  - Eye-level 35-50 mm, gentle dolly or locked.
  - Screens are diegetic: in the room, not floating.
  - Shoot reactions in close-up.
  - Use symmetry only for the end card.
  - For spine C: a seamless white cyc, a slow orbit, transformations in one take.
- **Look:**
  - Warm practical light (wood, lamps, dusk windows) with natural skin.
  - One saturated brand accent on the UI or mascot (S1 magenta/blue, S5 neon lime, S2 terracotta end card).
  - Mild film grain; no cyan wash.
- **genre_key:** `warm near-present realism, real lived-in spaces with practical lamps and dusk windows, technology shown only on in-world screens and devices, one saturated brand accent colour on the interface, natural skin, gentle dolly, soft film grain, no holograms, no cyan wash`
- **Shot JSON:** `{"id":"S04","dur":2,"model":"seedance_2_5","mode":"omni_reference","camera":"50mm over-shoulder, slow push","subject":"@USER","action":"start: glances at the wall screen -> end: small surprised smile as @TITAN_MASCOT finishes the task on screen","environment":"warm wood studio office at dusk, lamps on","light":"warm practicals, cool dusk window fill","audio":"room tone, a soft UI chime","constraints":["UI shown on the physical screen only, no floating holograms","on-screen UI labelled simulated in post"],"genre_key":"<§16 key>"}`
- **Sound:**
  - An airy licensed score or near-silence with real room tone.
  - Soft UI chimes on product moments (not glitch ticks).
  - VO is optional and sparse. S4 and S3 are near-wordless; S2 is dialogue comedy.
  - A bass swell on the brand card only.
- **Compliance:**
  - Every capability shown must be real or labelled "simulated / concept". The FTC's Operation AI Comply (2024) targets deceptive AI claims; see the flags below.
  - No "replaces humans" fear angle; show augmentation.
  - Never borrow a competitor's mascots, end-card style, type or colours (OpenAI/Anthropic/Apple are references for grammar only).
  - Data and privacy claims need substantiation.
- **Preset:** `scifi-tech` (corrected below: warm grade, sparse SFX, a chime map). It covers spines A and B. Spine C uses it with `pacing.max_shot_s` 30. New: `ui-proof-launch` (16b).

```json
{
  "name": "scifi-tech",
  "label": "Tech launch / futurism (human-first)",
  "kind": "genre",
  "description": "Corrected 2026-10-25 (S1-S5): warm real spaces, product on in-world screens, ~1.7-2.0 s shots evenly paced (or accelerating 2.9 -> 1.5 for a montage), one brand accent, soft chimes, brand card with one line. The cyan sci-fi look moved to sub-style 16c.",
  "reference": "research/genre-research-2026-10/class-cautionary-scifi.md#16",
  "structure": {"name": "human-day-launch", "target_s": [30, 90], "beats": ["cold open in the world", "the ask", "product acts (screen <-> reaction)", "scale up", "brand card"]},
  "pacing": {"remove_silence_over_s": 0.5, "pad_s": 0.12, "remove_fillers": "hard", "max_shot_s": 6.5},
  "captions": {"enabled": true, "max_words": 6, "animation": "fade", "size": 0.03, "font": "Instrument Serif", "highlight": "#FFFFFF", "outline": 0, "shadow": 2},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "drift", "every_s": 0, "scale": 1.04},
  "sfx": {"density_per_10s": 0.5, "db": -18, "map": {"broll": "pop", "end": "swell"}},
  "music": {"energy": "low", "db": -20, "duck": true},
  "grade": {"contrast": 1.04, "saturation": 0.97, "warmth": 0.04},
  "broll": {"every_s": 3.5, "max_dur_s": 2.2, "mode": "full"},
  "transitions": {"default": "dip", "on": "beats", "dur_s": 0.2, "strength": 0.4},
  "end_card": {"enabled": true, "dur_s": 3.5},
  "sfx_chime_kind_needs_feature": {"kind": "chime", "note": "soft UI chime for product moments; today map to pop at -18 dB"}
}
```

### 16b. UI-proof launch (`ui-proof-launch`) [measured: S5 https://www.instagram.com/reel/DeM8HKhCQjy/ (2.9 K likes, 772 comments)]
- **Use:** SaaS or AI-tool launches where the proof is a number (TITAN.AI tools, Higgsfield-style features).
- **Spine:**
  - a story cold open (1.5 s);
  - a big title card at ~1.7 s;
  - floating UI cards on a white void ("input → result");
  - metric curves drawn on black in the brand accent (`tools/motion` stat-counter / compare-loop);
  - stat cards;
  - back to the story;
  - a comment-to-DM CTA over the last shot.
- **Pacing:** 1.7 s median; the story bookends allow long holds (max 21 s); a demo burst in the middle.
- **genre_key (generated plates only):** `clean white seamless void, floating rounded UI cards with soft shadows, single neon brand accent, crisp product interface, studio daylight`
- **Compliance:** the metric cards show real, dated campaign numbers or say "illustrative". Comment-to-DM is fine; no fake comment seeding.

```json
{
  "name": "ui-proof-launch",
  "label": "UI-proof launch (story bookends + floating UI cards + metric curves)",
  "kind": "genre",
  "description": "From Higgsfield Ad Multiplier (S5): story cold open, title card at ~1.7 s, input->result UI cards, motion metric curves on black in one neon accent, stat cards, story return, comment-to-DM CTA.",
  "reference": "research/genre-research-2026-10/class-cautionary-scifi.md#16b",
  "pacing": {"remove_silence_over_s": 0.35, "pad_s": 0.06, "max_shot_s": 8.0},
  "captions": {"enabled": true, "max_words": 4, "animation": "pop", "highlight": "#D4FF3A"},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "max_words": 4, "dur_s": 1.8, "size": 0.06},
  "zoom": {"mode": "snap", "every_s": 3.0, "scale": 1.06},
  "broll": {"every_s": 3.0, "max_dur_s": 3.5, "mode": "full"},
  "sfx": {"density_per_10s": 1.5, "db": -14, "map": {"broll": "whoosh", "title": "pop", "end": "riser"}},
  "music": {"energy": "mid", "db": -18, "duck": true},
  "grade": {"contrast": 1.05, "saturation": 1.04},
  "end_card": {"enabled": true, "dur_s": 2.5},
  "transitions": {"default": "flash", "on": "beats", "dur_s": 0.12, "strength": 0.5}
}
```

### 16c. Concept sci-fi (cyan look, opt-in) (`scifi-tech` + grade override) [researched: draft card; negative controls S7, S8]
- **Use:** only when the brief is literally a future-world concept (a film trailer, a "TITAN 2040" vision piece), not a product launch.
- **Look:** the old draft look (cool cyan volumetric, holographic UI, symmetry) with **one warm human anchor in every shot**.
- **Pacing:** 2-4 s smooth shots.
- **Rule:** stock-robot montages with stat captions (S7, S8: 1 like each) are not a format.
- **genre_key:** `sleek near-future concept world, cool cyan volumetric light with one warm human accent in frame, symmetrical composition, slow dolly, clean minimal surfaces, subtle holographic interface`

## Proposed §0 picker rows
| 8 | Class & status | rich vs broke, same problem two wallets, out-of-touch rich persona | recognition, both-sides | **1.0 s dialogue volley, or two locked 5-7 s takes; persona 3 s** | premise header → volley/side A → side B/topper → silent reaction button | **one grade, class shown in props/wardrobe/vocabulary** | dialogue only (no bed) or a track-only A/B; persona VO 170-250 wpm | class-two-wallets (new) + class-persona-satire (new) |
| 12 | Cautionary / decision ladder | bad choices escalate; PSA; "one decision" | dread → "I'll do the right thing" | **rungs 2-3 s shrinking to 0.7 s; consequence held 4-30 s** | want + flash-forward → accelerating rungs → held consequence → stat + ONE action | colder and darker per rung, brand-warm at the end | dialogue only, an ironic licensed song, or a drone → silence | cautionary-ladder (corrected) + cautionary-ripple, cautionary-twist (new) |
| 16 | Sci-fi / tech launch (TITAN.AI) | AI / product launch, future-of-work | wonder → "I want that help" | **~1.7-2.0 s, even (montage accelerating 2.9 → 1.5); one-take product transformation 20-30 s** | cold open in a real place → ask → product acts in-world → scale → one-line brand card | **warm practicals + one saturated brand accent; cyan only for concept pieces** | airy score or room tone, soft UI chimes, swell on the card | scifi-tech (corrected) + ui-proof-launch (new) |

## 3 core rules per module
- **Class & status:**
  1. One frame, one grade; class lives in props and lines.
  2. The normal or poor side is the audience proxy and gets the last look.
  3. Punch at behaviour and hypocrisy. The persona format (an out-of-touch rich narrator) is the proven brand-collab vehicle.
- **Cautionary:**
  1. Repeat one frame so the decay is visible.
  2. Accelerate the rungs, then hold the consequence.
  3. Always end with ONE doable, one-time action (efficacy), not just a warning.
- **Sci-fi / tech:**
  1. Show the future as help in a real present.
  2. Product on in-world screens or as a character, never floating cyan holograms by default.
  3. One accent colour and a one-line brand card; claims real or labelled simulated.

## Flags for Klaus
- **Class spine C reuses real people's clips.**
  - On TITAN or brand accounts, recreate the evidence with original actors.
  - Clip-reaction stays on personal accounts (Remix/Stitch) per §31.
- **ASAS fear clause.**
  - The SG Code of Advertising Practice reportedly has a fear-appeal clause.
  - I did not verify it tonight. Check it before any paid Physio Spot / heal360 cautionary ad.
- **FTC "Operation AI Comply" (Sept 2024).**
  - This is from memory, not searched tonight; verify before citing.
  - Relevant if TITAN.AI advertises to the US: label simulated UI, and substantiate capability claims.
- **OpenAI/Anthropic/Apple films are grammar references only.**
  - The playbook must not copy their mascots, type or end-card colours.
  - Note: this research agent is itself Claude (Anthropic). The S2 measurements are reported neutrally.
- **Presets proposed here use new keys.**
  - Keys suffixed `_needs_feature`: a synced split compare, a per-beat grade ramp, a hold for the consequence beat, and a chime SFX kind.
  - The engine ignores them until they're built.

## Sources
- Reels: the URLs in the measured reference table above (accessed 2026-10-25).
- Tannenbaum et al. 2015, Psychological Bulletin: https://pubmed.ncbi.nlm.nih.gov/26501228/
- Meth Project critique: https://www.sciencedaily.com/releases/2008/12/081211081444.htm ; https://www.montanakaimin.com/news/evaluating-the-effectiveness-of-the-montana-meth-project/article_39f61954-ac5a-11e6-b695-bfd686efc470.amp.html
- THINK! 2014: https://www.thedrum.com/news/think-celebrates-50-years-first-anti-drink-drive-ad ; https://lbb.lbbonline.com/news/amv-bbdos-harrowing-spot-marks-50-years-of-drink-driving-ads ; https://www.gigwise.com/videos/95963/
- Shabaz Says: https://busrep.co.za/news/feel-good/youre-a-povvo-the-tiktok-star-making-serious-points-about-poverty-and-ice-cubes-998f67a9-c6c3-49ed-8a10-1e6e4417898c ; https://www.bigissue.com/news/activism/tiktok-shabaz-says-interview-christmas-child-poverty/ ; https://www.televisual.com/news/hello-mary-asks-are-billionaires-bad-for-bbc/
- Dhar Mann: https://en.wikipedia.org/wiki/Dhar_Mann
- Anthropic Keep Thinking / Super Bowl: https://campaignlive.com/article/ad-week-anthropic-hard-questions-mother/1964334 ; https://www.contentgrip.com/claude-ai-brand-campaign/ ; https://www.thestable.com.au/super-bowl-mother-claude-want-you-to-wonder-where-advertising-shouldnt-be/
- OpenAI GPT-6 Astra / dots context: https://www.constellationr.com/insights/news/openai-launches-gpt-6-astra
