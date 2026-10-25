# Genre research: §22 News / scam-expose, §20 Documentary / investigative, §21 Explainer / myth-buster (2026-10-25, overnight run C)

Scope: ground, correct and extend three cards in `.claude/skills/higgsfield-creative-director/references/genre-playbooks.md`. Builds on `research/refs-2026-10-25/editbymmh-sound.md` (the story-sfx-dense rulebook) and the presets news-expose, documentary, story-sfx-dense, mograph-metaphor-interview, illustrated-explainer-noir.
Nothing here is applied yet: Klaus approves, then the cards and presets get edited and `/learn` writes the rules.

## Method
- **Download:** public Instagram reels only, `yt-dlp --write-info-json`. No YouTube/TikTok/Vimeo, no cookies. Several reels hit 429 or "empty media" and were skipped. Media stays in the scratchpad (`scratchpad/genreC/dl/`), never in the repo; study only, nothing re-used.
- **Measure** (script `scratchpad/genreC/scripts/analyze.py`):
  - cuts: ffmpeg `select='gt(scene,0.2)'` at 320 px, merged within 150 ms;
  - loudness: ebur128 integrated LUFS;
  - level: 100 ms RMS percentiles and the share of time below -30 dBFS;
  - onsets: spectral-flux peaks (median×4 / median+3·MAD), and the share of cuts with an onset within ±250 ms;
  - words/min: faster-whisper small int8 with word timestamps. `wpm_speech` = words / summed word durations, `wpm_runtime` = words / runtime;
  - 1 fps 8×8 frame sheets, which I looked at for every reel cited as [measured].
- **Caveats (read before trusting a number):**
  - Scene detection misses dissolves, dark fades and in-frame layout changes. For one-take or PiP/green-screen reels the "shot length" is really the layout-change length. Where I counted from the sheet instead, the row says so.
  - Whisper auto-detected Singapore English as Malay ("ms") on 5 reels and returned a translation. Their wpm is approximate (±20 %) and marked ≈.
  - Chinese reels: whisper counts characters/tokens differently; wpm not comparable, marked n/a.
  - Likes are what yt-dlp returned on 2026-10-25. Instagram returned no view counts; views are quoted from press where available.

---

## A. Evidence tables

### A1. News / scam-expose (measured)
| # | Reel (creator, date) | Format | Likes / comments | Dur s | Cuts /10 s | Median / avg shot s | First word s | wpm speech / runtime | LUFS | time < -30 dBFS |
|---|---|---|---|---|---|---|---|---|---|---|
| N1 | [@serangoonnpc / Hougang NPC "Singa(pore) Inferno"](https://www.instagram.com/reel/DWkv0WID7gG/) 2026-04-01 | one-take trend parody (Netflix *Singles Inferno*), police officer to camera, the "reveal" is that the voice was pre-recorded and the man is a lookalike | **370,411 / 3,432**; CNA reported **5M+ views** ([CNA FB](https://www.facebook.com/ChannelNewsAsia/videos/a-22-second-video-posted-by-hougang-neighbourhood-police-centre-on-love-scams-qu/1311179780922017/)); [AsiaOne](https://www.asiaone.com/singapore/hougang-npc-love-scam-benjamin-cheah-viral-video), [MustShareNews](https://mustsharenews.com/hougang-police-love-scams-video/) | 22.1 | 0 hard cuts (1 hand-over-lens swap ~18 s) | one take | 0.0 | 220 / 152 | -14.1 | 6.8 % |
| N2 | [@singaporepoliceforce "Scam Alert: Deepfake Zoom Calls"](https://www.instagram.com/reel/DYZhomaFNjB/) 2026-05-16 | official advisory: 16:9 letterboxed footage + text slates + 4-point "Advisory to the Public" + crest outro | 544 / 4 | 66.1 | 2.0 | 3.5 / 4.7 | 7.6 | 172 / 83 | -14.3 | 42 % |
| N3 | [@singaporepoliceforce "If Netflix made a documentary about scams"](https://www.instagram.com/reel/DbwveVREWRt/) 2026-08-08 (SPF × China People's Police) | re-enactment doc: interviews + dramatised scenes, bilingual subs, big quoted scam lines ("TELL NO ONE", "REPORT DAILY") | 881 / 8 | 79.8 | 4.8 | **1.6 / 2.1** | 2.3 | n/a (zh) | -14.1 | 16 % |
| N4 | [@ica_singapore guardian-officer skit](https://www.instagram.com/reel/DejSVAmP2vV/) 2026-10-16 | comedy skit: victim on a scam call, an officer appears behind him at each bad decision | 359 / 6 | 96.0 | 2.4 | 2.9 / 4.0 | 0.0 | ≈175 / 88 | -14.5 | 26 % |
| N5 | [@singaporepoliceforce "Received a call from the police?"](https://www.instagram.com/reel/DajtXUcm9kl/) 2026-07-09 | long explainer, presenter-led | 231 / 4 | 247.4 | 1.5 | 5.7 / 6.7 | 0.0 | ≈162 / 142 | -14.2 | 8.6 % |
| N6 | [@mothershipsg "scammers, think twice" vox pop](https://www.instagram.com/reel/DP3m-09jxKk/) 2025-10-16 | street vox pop on caning for scammers: persistent yellow question header, news-article screenshot cards, comic "Sorry I paiseh" photo mask over people who declined to show their face | 2,149 / 32 | 83.9 | 4.8 | **1.7 / 2.1** | 0.0 | ≈208 / 174 | -14.3 | 11 % |
| N7 | [@mothershipsg "dw, you're on the real Mothership page"](https://www.instagram.com/reel/DdiccisGrWO/) 2026-09-21 | sit-down interview with an SPF Cyber Command officer, red kicker title + name/rank lower third, screenshots of fake posts, Anti-Scam Centre B-roll | 3,406 / 20 | 125.5 | 0.8 | 5.4 / 11.4 | 0.0 | ≈144 / 134 | -14.1 | 18 % |
| N8 | [@straits_times × SPF "toilet roll" e-commerce scam](https://www.instagram.com/reel/DUFJUMUluLA/) 2026-01-29 | **no voice**: text-on-stock case story (box captions), a yellow stat counter "3,237 e-commerce scam cases", "BUY AND PAY WISELY" checklist, partner logos | 3,873 / 33 | 52.4 | (dissolves; sheet count ≈ 9 shots) | ≈5.8 (sheet) | n/a | 0 (music only) | -14.0 | 1.1 % |
| N9 | [@mothershipsg MOS Goh Pei Ming podcast clip](https://www.instagram.com/reel/DVvfsnPD9OV/) 2026-03-11 | podcast clip with stat cards | 383 / 1 | 59.2 | 1.4 | 4.3 / 6.6 | 0.0 | 196 / 176 | -14.8 | 26 % |
| N10 | [@theonlinecitizen Google Meet "police" scam](https://www.instagram.com/reel/DXbW1g9CLjx/) 2026-04-22 | victim's phone recording of a fake officer + paragraph captions in red boxes, no music bed | 59 / 10 | 73.0 | 0.1 | one take | 9.8 | 217 / 47 | -15.1 | **76 %** |
| N11 | [@adrinmanohar commentary on a Mothership headline](https://www.instagram.com/reel/Dbp-N7QN2w7/) 2026-08-05 | creator talking head | 59 / 5 | 55.4 | 0.4 | 6.9 / 18.5 | 0.0 | 249 / 204 | -14.3 | 13 % |
| N12-15 | VTV "Toàn dân chống lừa đảo" ([1](https://www.instagram.com/reel/DYeMKoTkYV5/), [2](https://www.instagram.com/reel/DZ1CabYDiq3/), [3](https://www.instagram.com/reel/DamOVpBCKGn/)), [MB Bank](https://www.instagram.com/reel/DZmV19JjHVJ/) 2026-05..07 | VN "CẢNH BÁO" (WARNING) caps title + 🔴/🚨 kicker in caption, square news cut-downs | 0-1 likes each on IG (these are cross-posts; their home is Facebook/TikTok) | 59-140 | 0.4-2.0 | 4.0-7.1 median | 0-23 | 257-287 (VN) | -14.2..-14.5 | 6-25 % |

**What the numbers say**
- **Format beats polish.** The same institution (SPF family) gets 231-881 likes for advisories and docs, and 370k likes / 5M+ views for a 22 s one-take trend parody (about 400-1,600×). The parody does not explain a modus operandi at all. It *demonstrates the trick on the viewer* (the voice is pre-recorded, the man is a lookalike) and ends on one line: "Don't believe everything online."
- **Advisory grammar loses.** N2 and N5 (letterbox 16:9, 7.6 s before the first word, text slates, 42 % of runtime below -30 dBFS) are the weakest per follower.
- **News pages that do well** (N6-N8: 2.1-3.9k likes) use one of three spines:
  - a real face with a persistent question or kicker header (vox pop, interview);
  - a silent text-on-stock case story with ONE stat number.
- **Pacing.** In voiced news reels the median shot is 1.6-1.7 s when B-roll-led (N3, N6) and 4-6 s when interview-led (N7, N9). The card's "1.5-3 s" is right only for the B-roll-led spine.
- **Speech rate.** About 145-220 wpm of speech. Loudness is always -14..-15 LUFS.
- **The bed decides the floor.** Every reel above 2k likes keeps time below -30 dBFS ≤ 18 %; the two "silent bed" reels (N2 42 %, N10 76 %) are the weakest. This matches the editbymmh R1 "bed under everything".

### A2. Documentary / investigative (measured)
| # | Reel | Format | Likes / comments | Dur s | Cuts /10 s | Median / avg shot s | wpm speech / runtime | LUFS | < -30 dBFS |
|---|---|---|---|---|---|---|---|---|---|
| D1 | [@johnny.harris "American elections have more money…" (the scrubbed ad)](https://www.instagram.com/reel/DRfLDUfk4qJ/) 2025-11-25 | paper-trail investigation: silent cold open of him at the laptop + "Domain Not Claimed" / "This video isn't available" screens, the found ad, then printed FEC forms with a teal highlighter swiping the key words | 5,339 / 43 | 58.8 | 5.8 | **1.2 / 1.7** | 170 / 101 | -14.1 | 18 % |
| D2 | [@johnny.harris "The IRS briefcase heist"](https://www.instagram.com/reel/DZu1CrUEzge/) 2026-06-18 | true-crime reconstruction in 2.5D photo-collage (cut-out people on parallax plates), neon place-date stamp "Miami, 1973", producer called in through a CRT-framed video call | 3,517 / 58 | 171.6 | 2.0 | 3.2 / 4.8 | 216 / 175 | -14.5 | 13 % |
| D3 | [@johnny.harris "The UFO Evidence That's Hard to Ignore"](https://www.instagram.com/reel/DVM1PorDzKW/) 2026-02-26 | evidence review | 2,558 / 55 | 179.2 | 2.6 | 2.3 / 3.7 | 201 / 179 | -14.6 | 14 % |
| D4 | [@cnainsider #TalkingPoint recycling bins](https://www.instagram.com/reel/Cy8Es70hHLw/) 2023-10-28 | reporter explainer-investigation: **split layout** (evidence B-roll top, producer bottom), red headline box, **source tag on every evidence shot** ("Source: TODAY", "According to EcoBusiness, 2019"), yellow numbers in captions ("60%-70%", "9 times", "0%") | 861 / 8 | 66.4 | 4.7 | 1.8 / 2.1 | ≈171 / 159 | **-19.0** | 19 % |
| D5 | [@cnainsider "Myanmar: The Lost 5 Years"](https://www.instagram.com/reel/DUN1lSyE5qJ/) 2026-02-01 | correspondent VO + archive | 382 / 6 | 94.9 | 5.8 | 1.6 / 1.7 | 197 / 163 | -14.3 | 12 % |
| D6 | [@cnainsider Inside the Police Coast Guard](https://www.instagram.com/reel/DQ3zcuzE8cJ/) 2025-11-10 | observational + investigator interview | 1,381 / 6 | 93.4 | 5.6 | 1.5 / 1.8 | ≈178 / 156 | -14.1 | 0.6 % |
| D7 | [@cnainsider Beyond Maximum Security](https://www.instagram.com/reel/CmQ3JlxB9AR/) 2022-12-17 | observational, natural sound | 658 / 3 | 52.1 | 2.9 | 2.9 / 3.3 | ≈129 / 76 | **-20.5** | 66 % |
| D8 | N3 above (SPF "Netflix documentary") | re-enactment doc | 881 | 79.8 | 4.8 | 1.6 / 2.1 | n/a | -14.1 | 16 % |

**What the numbers say**
- **The card's "3-6 s avg shot" is wrong for short-form docs.** Measured medians are 1.2-3.2 s (avg 1.7-4.8). The VO-led cut-down cuts like an explainer; long holds survive only in observational moments (D7, which is also the quietest and weakest per follower).
- **Words.** 170-216 wpm of speech. Runtime wpm drops in cold opens (D1: 101 wpm overall, because the first ~9 s are near-wordless screen action).
- **Loudness.** -14..-14.6 LUFS, except CNA's broadcast-sourced D4/D7 at -19/-20.5 (TV masters reposted without a platform loudness pass).
- **Johnny Harris's three devices** (the top performers) are all *process on screen*:
  - searching/browsing (dead links);
  - paper (printing, highlighter swipe on the key words);
  - a stylised reconstruction (collage, neon date stamp) instead of photoreal re-enactment.
- **CNA's best device for trust is the source tag.** A small top-right "Source: X" or "According to X, year" sits on every evidence shot.

### A3. Explainer / myth-buster (measured)
| # | Reel | Format | Likes / comments | Dur s | Cuts /10 s | Median / avg shot s | wpm speech / runtime | LUFS | < -30 dBFS |
|---|---|---|---|---|---|---|---|---|---|
| E1 | [@drkaranrajan "The great toilet roll conspiracy"](https://www.instagram.com/reel/CxkzKPFs6Dx/) 2023-09-24 | myth-buster: the viral claim plays first (stitch of the claimant, small word-by-word captions), then he appears PiP bottom-right over evidence (microscope photos of new vs used needles, labelled, red circle/arrow), then talking head at the bookcase, ends on the screenshot of the original Facebook post where the myth started | **74,969 / 790** | 67.3 | 1.5 (layout changes; shots 4.8 / 6.1) | 4.8 / 6.1 | **239 / 219** | -14.7 | 13.5 % |
| E2 | [@drkaranrajan period myth ("WATCH TIL THE END")](https://www.instagram.com/reel/CRWkCiEoTIj/) 2021-07-15 | 15 s stitch-and-answer | 14,195 / 208 | 15.2 | 2 shots | 7.6 | 231 / 218 | -15.0 | 9.9 % |
| E3 | [@veritasium_daily "How gravity really works"](https://www.instagram.com/reel/DFWIQ4_CxLY/) 2025-01-27 | 6.7-min long-form cut-down (presenter + animation) | 26,414 / 296 | 401.8 | 1.3 | 5.6 / 7.7 | 185 / 152 | -14.1 | 18 % |
| E4 | [@veritasium_daily "How End-to-End Encryption Works"](https://www.instagram.com/reel/DbDwKfHCU7G/) 2026-07-21 | **physical-metaphor demo**: two presenters mix coloured dyes on a bar top to show a key exchange (public colour + private colours = shared secret), then an "attacker" cut-in and a node diagram; serif subtitles mid-frame | 7,712 / 41 | 123.3 | 2.9 | 2.1 / 3.3 | 234 / 206 | -14.1 | 25 % |
| E5 | D4 (CNA reporter split explainer) | see D4 | 861 | | 4.7 | 1.8 / 2.1 | ≈171 | -19.0 | |
| E6 | [@princecourtmc "5 dangerous cancer myths"](https://www.instagram.com/reel/DcNUyEVP6n-/) 2026-08-19 | hospital doctor list explainer (a low-performer control) | 30 / 1 | 77.9 | 3.3 | 2.4 / 2.9 | ≈160 / 104 | -14.2 | 19 % |

**What the numbers say**
- **Myth-busters talk fast.** Top myth-busters speak at 230-240 wpm with zero dead air (word at 0.0 s, runtime wpm ≈ speech wpm). That is faster than news (≈145-220) and docs (170-216).
- **Long shots, constant visual change.** E1's "shots" are long (4.8 s median), but the visual never sits still: the layout flips between claim stitch → evidence + PiP → face → source screenshot, about every 5 s.
- **Structure that wins (E1, 75k likes):**
  1. the myth, shown as the viral artefact itself;
  2. "look closely" (the bait is the claim's own evidence);
  3. the mechanism, with labelled evidence images;
  4. why it's harmful ("dehumanises");
  5. the origin receipt (the original post);
  6. a one-line verdict ("stop listening to idiocy online").
- **The second winning grammar is the physical-metaphor demo** (E4: dyes = encryption keys, 234 wpm, 2.1 s median). Every abstract step is a hand doing something to a prop on a table, so the shot changes with each clause.
- **Length is not the problem.** The long-form cut-down (E3: 6.7 min, 185 wpm, 5.6 s median) still drew 26k likes; a big topic carries length.
- **The control shows what loses.** E6 (30 likes) cuts *faster* (2.4 s median) but talks slowly with gaps: 160 wpm of speech, only 104 wpm over the runtime, first word at 2.4 s. Dead air, not shot length, separates the losers.

### A4. Vietnam scam-warning reels (researched + light measure)
VTV's anti-scam page ("Toàn dân chống lừa đảo") and MB Bank post square or 9:16 news cut-downs with a "🔴 CẢNH BÁO KHẨN" (URGENT WARNING) caps kicker and numbered "1. Không bấm link lạ…" (don't tap unknown links) steps in the caption. Their IG copies get 0-1 likes because their audience is on Facebook/TikTok/Zalo. So treat them as a **language and convention reference only** (Vietnamese first, the CẢNH BÁO kicker, the numbered do/don't list), not as a performance benchmark.

Measurements:
- **VTV [DZ1CabYDiq3](https://www.instagram.com/reel/DZ1CabYDiq3/):** 59 s, 1:1, a stacked layout.
  - The top half is the broadcast segment: anchor, hooded-hacker stock B-roll, red news ticker.
  - The bottom half is a **persistent green campaign card** with the CAPS headline "GIA TĂNG LỪA ĐẢO TRỰC TUYẾN DO TỘI PHẠM DÙNG A.I" (online scams rising as criminals use AI).
  - The outro slogan card reads "Bình tĩnh nhận diện · Chủ động xác minh · Quyết liệt ngăn chặn" (calmly recognise · proactively verify · resolutely block).
  - Median shot 7.1 s, 284 wpm, -14.2 LUFS.
- **VTV [DYeMKoTkYV5](https://www.instagram.com/reel/DYeMKoTkYV5/):** 140 s, median 6.5 s, 257 wpm.
- **VTV [DamOVpBCKGn](https://www.instagram.com/reel/DamOVpBCKGn/):** 81 s, median 4.0 s, 287 wpm.
- **MB Bank [DZmV19JjHVJ](https://www.instagram.com/reel/DZmV19JjHVJ/):** 104 s, first word at 23.4 s (animated intro), 0.4 cuts/10 s.

Vietnamese is monosyllabic, so wpm runs about 1.2-1.3× English; compare only within the language. The convention to keep is the stacked "news segment over a persistent campaign title card" and the 3-verb slogan close. The convention to avoid is hooded-hacker stock: it's a cliché, and it shows nothing the viewer will actually see. SnapSaigon-type pages could not be opened in this run (the ref #2 gap remains).

### A5. Carousels (researched; IG image posts don't download without login)
- **Benchmarks:** Socialinsider 2026 benchmarks put carousels at the top engagement rate (≈0.50 %) of IG formats ([Socialinsider](https://www.socialinsider.io/social-media-benchmarks/instagram)). Carousels earn more saves but less non-follower reach than reels ([Blck Alpaca summary](https://blckalpaca.at/en/knowledge-base/social-media/social-media-algorithms-distribution/reels-vs-carousel-instagram-formats)). Socialinsider also reports >10 slides getting more reach ([blog](https://www.socialinsider.io/blog/instagram-carousel/)).
- **Live scam-carousel convention** (seen in Oct 2026 posts: [1](https://www.instagram.com/p/DecEKFOEY1i/), [2](https://www.instagram.com/p/De1zkXsEW9W/), [3](https://www.instagram.com/p/DejI4taG-KY/), [4](https://www.instagram.com/p/DelSLxlGxB5/)):
  - a 3-5-word CAPS title built as threat + command ("FAKE QR, REAL LOSS", "BANK SMS? DON'T TAP", "INSTANT LOAN? THINK TWICE");
  - a repeated series line ("Scammers are getting smarter every day. This carousel breaks down the trick…");
  - a "save this" CTA. A recurring series name is the format.

---

## B. Corrected cards (exact genre-playbooks.md layout)

### 22. News / scam-expose (video + carousel) [measured: N1 https://www.instagram.com/reel/DWkv0WID7gG/ , N6 https://www.instagram.com/reel/DP3m-09jxKk/ , N7 https://www.instagram.com/reel/DdiccisGrWO/ , N8 https://www.instagram.com/reel/DUFJUMUluLA/ ; controls N2, N10]
- **Pick the spine first.** There are three proven spines plus the advisory, which is the control and loses:
  - (a) **face + persistent kicker header**: interview or vox pop. 4-6 s shots when interview-led, 1.7 s when vox-pop-led.
  - (b) **silent case story**: text-on-stock, no VO, ONE stat counter.
  - (c) **trick-on-the-viewer remix**: see 22b.
  - Never lead with the advisory slate.
- **Pacing map (30-60 s, voiced):**
  - **0-1 s:** the kicker card ("⚠️ SCAM ALERT" / "CẢNH BÁO") with a 6-word claim over the evidence (fake SMS, fake page), and a voice from frame 0. Measured first word at 0.0 s on every reel above 2k likes; the advisories open on 7-10 s of slates.
  - **1-8 s:** what the victim sees, the real artefact (screenshot, recreated call), labelled "Example" or "Dramatisation".
  - **8-35 s:** "how it works" in 3-5 numbered beats, one idea each, 4-6 s per beat. B-roll or screenshot cuts every 1.7-2.5 s inside a beat.
  - **35-45 s:** ONE number (stat counter) with its source line.
  - **Last 5-8 s:** "what to do": 3-4 numbered actions plus the official helpline (SG ScamShield 1799; VN: the bank's hotline or local police). Then a 1-2 s logo.
- **Pacing map (silent case story, 45-55 s):** a 1-line loss hook ("He lost $700 ordering toilet rolls") → 5-7 text-on-stock cards of 4-6 s each, one sentence per card → a stat counter → a "BUY AND PAY WISELY:" bold-verb checklist (Check / Verify / Use / Avoid) held 6-8 s → partner logos.
- **Carousel (see 22c for the full card):**
  - slide 1 = a CAPS 3-5-word "threat? command" title over the evidence image;
  - slides 2-6 = numbered steps, one idea each;
  - a stat slide with its source;
  - the last slide = what to do + who to call + "save this".
  - 7-10 slides.
- **Shot grammar:**
  - interview mid-shot at desk height with the name/rank lower third in the first 3 s;
  - screenshots full-width on a blurred copy of themselves, with a red circle or arrow on the tell;
  - B-roll of the scam surface (phone in hand, laptop), never a victim's face;
  - vox pop: people who decline get a comic photo mask (Mothership's "Sorry I paiseh") or a blur, never shown.
  - **VN variant:** a 1:1 or 4:5 stack, with the news segment on top and a persistent campaign title card below (Vietnamese CAPS headline). Close on a 3-verb slogan card. Vietnamese text comes first and is largest.
- **Look:**
  - high clarity, real daylight, the brand logo as a small pill top-right;
  - ONE warning accent: red kicker bar, or yellow for numbers and the persistent question;
  - captions as 3-5-word sentence chunks in a clean sans, white with a soft shadow;
  - no meme fonts, no letterbox (letterboxed 16:9 = the losing advisory look).
- **genre_key:** `credible photojournalistic style, real daylight, clear evidence framing, phone screens legible, neutral natural colour, no dramatisation, documentary handheld steadiness`
- **Shot JSON:**
  ```
  {"camera":"locked 35mm desk-height mid-shot, subject 1/3 left, screen-safe headroom for kicker","subject":"spokesperson or presenter in work clothes","action":"start: looks at phone showing a fake message -> end: turns phone to lens, taps the tell","light":"soft daylight, clean office","constraints":"screen content added in post, not generated; no real logos generated","genre_key":"…"}
  ```
- **Sound:**
  - a continuous low bed at -20..-22 dB under the voice (keep time below -30 dBFS ≤ 15 %);
  - a news sting or impact on the kicker;
  - a tick on each numbered step and on each screenshot slam;
  - a swell + impact on the stat counter;
  - silence only before the "what to do" turn (≤ 0.3 s);
  - silent case story: music-only, mid-tempo, at -16..-18 dB (it IS the voice);
  - -14 LUFS.
- **Compliance:**
  - Describe patterns, not people. Name or show a person or business only when an official source has, and link it (compliance-packs.md "Media, publishers").
  - Blur faces, plates, phone numbers and account numbers; scam numbers stay partly masked (show the prefix only).
  - Every fact carries a source + date line on screen (CNA-style tag) and in SOURCES.md.
  - **SG:** POFMA can order a correction for a false statement of fact in the public interest ([POFMA Office](https://www.pofmaoffice.gov.sg/media-centre/); [Act](https://sso.agc.gov.sg/Act/POFMA2019)), so quote SPF/ScamShield wording for numbers and modus operandi and never round or extrapolate a statistic. Defamation risk is higher than in the US (commentary-controversy.md).
  - Never imitate police/government branding, crests, uniforms or a ".gov" look on a brand account. Even a parody can read as impersonation, the very thing the scam does.
  - **VN:** Vietnamese first, foreign text ≤ 3/4 size; Decree 15/2020 Art. 101 fines false or slanderous posts; phone-verified accounts only (Decree 147/2024); no political or state content.
  - Paid: keep scam creative calm or run it organically (sensational crime creative gets rejected).
- **Preset:** news-expose (corrected below); expander: carousel-text with the kicker card.

### 22b. Trick-on-the-viewer remix ("police-advisory remix") [measured: N1 https://www.instagram.com/reel/DWkv0WID7gG/ ; N4 https://www.instagram.com/reel/DejSVAmP2vV/ as the skit cousin] (NEW sub-style)
- **Use when:** a brand or community page wants a warning to spread; the trick can be performed on the viewer (fake voice, lookalike, fake link, deepfake).
- **Pacing map (15-25 s, one take):**
  - **0 s:** a direct address, mid-action, with a mystery prop ("you must be wondering what I'm drinking");
  - **2-12 s:** three "you think X, but Y" reveals, each 3-4 s, each breaking an assumption the viewer just made (the cup is empty → the hands are elsewhere → the voice is pre-recorded);
  - **14-18 s:** the lesson line ("Don't believe everything online");
  - **18-22 s:** the final reveal (lens covered, a swap to a different person: "is not even the real me");
  - **end:** no CTA card; the caption carries the advice and the helpline.
- **Shot grammar:** one locked or handheld take, waist-up, a plain bright location. The only "cut" is a physical wipe (a hand over the lens). Captions are 2-4 words in a serif beside the head (not under the chin), with the punch word in the accent colour. The parodied show's title type sits persistent at the top.
- **Look:** bright, natural, flat office light; the show-parody title in the trend's own colour (pink here).
- **genre_key:** `bright natural office daylight, flat even light, clean white walls, casual direct-to-camera, phone-shot realism`
- **Sound:**
  - the trend's dating-show-style bed (personal/creator accounts: in-app trending audio only; brand accounts: an original sound-alike, never the show's music);
  - voice from frame 0 at 220 wpm;
  - no SFX needed (measured 0 cuts, 14.5 onsets/10 s are all speech and bed);
  - -14 LUFS.
- **Compliance:**
  - Only real staff, or a consenting creator, as "the lookalike". Never an AI likeness of a real officer or public figure.
  - On brand accounts don't wear a uniform you are not entitled to.
  - Health brands (SG): no patient, no outcome; the "reveal" can only be about the scam.
- **Preset:** `scam-remix-onetake` (new, below).

### 22c. News-card carousel (`news-card-carousel`) [researched: Socialinsider benchmarks, Oct-2026 live scam carousels listed in A5] (NEW sub-style)
- **Slides (8-10, 4:5):**
  1. **Kicker** ("⚠️ SCAM ALERT", or "CẢNH BÁO" for VN) + a CAPS 3-5-word "THREAT? COMMAND" title + the evidence image, masked;
  2. "What you see": the artefact with a red circle on the tell;
  3-6. "How it works": numbered steps 1-4, one sentence each, one icon or crop each;
  7. **The number**: one stat + "Source: SPF, mid-year 2026";
  8. **What to do**: 3-4 bold-verb lines (Check / Verify / Call / Report);
  9. **Who to call**: the helpline, plus "Save this · Send to your parents".
- **Look:** a recurring series name in the top-left on every slide (it IS the brand), and the same colour bar on every slide. Slide 1 has the evidence photo full-bleed; slides 2-9 are clean off-white or dark cards. Type: one sans, the keyword in the accent colour.
- **Compliance:** as in card 22. The source line on the stat slide is mandatory; never put a real scammer's full number or a victim's name on a slide.
- **Preset:** the expander's `carousel-text` with `card_style: kicker`; slide-plan rules go to thumbnail-carousel-design.md (thumbnail-designer agent).

### 20. Documentary / investigative [measured: D1 https://www.instagram.com/reel/DRfLDUfk4qJ/ , D2 https://www.instagram.com/reel/DZu1CrUEzge/ , D4 https://www.instagram.com/reel/Cy8Es70hHLw/ , D5 https://www.instagram.com/reel/DUN1lSyE5qJ/ , N3 https://www.instagram.com/reel/DbwveVREWRt/]
- **Pacing map (60-90 s short; scale up for long form):**
  - **0-9 s:** a cold open of *process*, not a talking head: the investigator searching, dead links, a document coming out of the printer. Near-wordless ambient + one line ("I've been looking for a video that has almost entirely disappeared from the internet").
  - **9-15 s:** the question, said plainly ("So why did someone scrub it?").
  - **15-70 s:** evidence beats of 6-10 s each, cut inside at a **1.2-2 s median** (measured 1.2-1.8 s on D1/D4/D5/N3). Each beat = a document or archive image + a source tag + one VO sentence.
  - **~65 %:** the turn: the paper trail names the payer / the twist.
  - **Last 5-10 s:** what it means + "full video" CTA.
- **Shot grammar:**
  - macro on paper with a highlighter swiping the key words (D1);
  - screen captures of searches and dead pages;
  - interview at 1/3 framing with name/role lower thirds in the first 3 s of each speaker;
  - the reporter split (evidence top, presenter bottom) when the presenter explains numbers (D4).
  - **Reconstructions are stylised** (2.5D photo-collage with parallax, neon place-date stamp "Miami, 1973" (D2), or labelled re-enactment "Dramatisation" (N3)), never photoreal AI of real people.
- **Look:** neutral daylight grade for the present; archival texture (b/w, film grain) for the past. Caption: small CAPS white text in a black box at the lower third (D1), or sentence captions with yellow numbers (D4). Source tag top-right on every evidence shot.
- **genre_key:** `documentary realism, natural available light, observational camera, macro detail on paper and screens, archival texture for past events, sober composition`
- **Shot JSON:**
  ```
  {"camera":"overhead 50mm macro, slow 3% push","subject":"printed government filing on a desk","action":"start: page lands -> end: teal highlighter swipes across the key line","light":"warm desk lamp, soft falloff","constraints":"text added in post from the real document; no generated text","genre_key":"…"}
  ```
- **Sound:**
  - VO first;
  - a bed under everything at -20..-22 dB (time below -30 dBFS 12-18 % measured; the -66 % observational outlier D7 underperforms);
  - paper/foley on documents (print, slap, highlighter squeak), a typing tick on the search screens;
  - a swell → impact on the turn;
  - -14 LUFS (never post a -19/-20 broadcast master; re-normalise).
- **Compliance:**
  - Every fact goes in SOURCES.md plus an on-screen source tag.
  - Real people's names only from public records or reputable press.
  - Archive clips: short, transformative, credited.
  - Re-enactments are labelled "Dramatisation" and use actors or stylised collage (no AI likeness of real people; commentary-controversy.md).
  - SG POFMA / defamation and VN Decree 15 apply as in card 22.
- **Preset:** documentary (corrected below); `doc-paper-trail` (new) for investigation pieces.

### 21. Explainer / myth-buster [measured: E1 https://www.instagram.com/reel/CxkzKPFs6Dx/ , E2 https://www.instagram.com/reel/CRWkCiEoTIj/ , E4 https://www.instagram.com/reel/DbDwKfHCU7G/ , E5/D4 https://www.instagram.com/reel/Cy8Es70hHLw/ ; control E6]
- **Pacing map (45-70 s):**
  - **0-4 s:** the myth itself, shown as the artefact (a recreated viral post or clip, or the claim read in its own words), with a provocation ("If your toilet paper looks like this…, get out");
  - **4-12 s:** "look closely": the claim's own evidence, zoomed;
  - **12-35 s:** the mechanism, with labelled evidence images (microscope, diagram, chart) and the expert PiP in a corner pointing at it; the layout changes every 4-6 s;
  - **35-55 s:** back to the face: why the myth is harmful or who it hurts;
  - **55-65 s:** the origin receipt (where the myth started: the first post, dated) and a one-line verdict;
  - voice from 0.0 s at 220-240 wpm, no pauses over 0.3 s.
- **Shot grammar:**
  - the expert in a real setting (bookcase, clinic) mid-shot;
  - the green-screen or PiP expert in the bottom-right (about 35 % width) over evidence;
  - evidence images labelled in small type on the image ("New needle", "Used 6 times"), with a red circle or arrow on the tell;
  - 2-4 word captions centred mid-screen.
  - Our version: the CNA reporter split (B-roll top, expert bottom) is the editor's ready-made layout (`mode: split`).
  - **Alternative spine (E4), the physical-metaphor demo:** the presenter's hands act out each abstract step with tabletop props (dyes, cups, coins, a resistance band for a muscle). Cut on each clause at about a 2 s median, then one node diagram (tools/motion) for the summary. For Physio Spot this is the natural grammar: a band, a spine model, a sponge.
- **Look:** bright and clean, real location rather than a seamless studio; the evidence images keep their own colour; one accent (red) for the circles and arrows.
- **genre_key:** `bright clean educational look, real location background, clear subject, natural soft light, evidence-friendly composition with negative space for a PiP`
- **Shot JSON:**
  ```
  {"camera":"locked 35mm mid-shot, subject right third, left two-thirds clear for evidence overlay","subject":"expert in work clothes","action":"start: squints at off-screen claim -> end: points down-left at where the evidence will appear","light":"soft window light","genre_key":"…"}
  ```
- **Sound:**
  - voice-led with a low bed at -22 dB;
  - a light whoosh on each layout change (evidence in / out);
  - a "pop" on each label or arrow;
  - one impact under the verdict line;
  - -14 LUFS.
- **Compliance:**
  - Claims are sourced. Show the myth as a recreation or a quote card, not the original poster's face, unless it's a public figure or platform-native Stitch/Remix (personal accounts only).
  - Mask private names on the origin screenshot (E1 does).
  - Health brands in SG: no superlatives, no "cure", no patient stories; a myth-buster is education, not an inducement (compliance-sg.md).
- **Preset:** `myth-buster-stitch` (new, replaces talking-head-punchy as the card's default); talking-head-punchy stays the fallback when there's no evidence footage.

---

## C. Corrected and new presets (schema of tools/editor/presets/*.json)
Engine keys used only from editor.md §2, §7, §7b, §7f. Anything else sits under `_needs_feature`.

### C1. news-expose (corrected)
```json
{
  "name": "news-expose",
  "label": "News / scam-expose (face + kicker spine)",
  "kind": "genre",
  "description": "Measured on SPF/Mothership/Straits Times scam reels (research/genre-research-2026-10/news-doc-explainer.md A1). Voice from frame 0, persistent kicker header, 3-5 numbered steps of 4-6 s with cuts every ~1.7-2.5 s inside a step, one stat counter with source, numbered 'what to do' + helpline, logo. Continuous bed (time below -30 dBFS <= 15%), sting on the kicker, ticks on steps and screenshot slams.",
  "reference": "research/genre-research-2026-10/news-doc-explainer.md",
  "structure": {
    "name": "news-short",
    "target_s": [30, 60],
    "beats": ["kicker + claim 0-1s", "what you see (artefact)", "how it works 1", "how it works 2", "how it works 3", "the number + source", "what to do + helpline", "logo"]
  },
  "pacing": {"remove_silence_over_s": 0.3, "pad_s": 0.06, "remove_fillers": "hard", "max_shot_s": 6.0, "drop_retakes": true},
  "captions": {"enabled": true, "max_words": 5, "animation": "fade", "size": 0.036, "position_y": 0.72, "uppercase": false, "keyword_caps": false, "highlight": "#FFC400", "outline": 0, "shadow": 1},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "kicker", "persistent": true, "position_y": 0.16, "size": 0.034, "uppercase": false, "max_words": 10},
  "lower_third": {"size": 0.026, "box": "#C62828", "box_alpha": 0.9, "position_y": 0.62},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.06, "on_hook": 1.0, "on_emphasis": true},
  "broll": {"every_s": 2.5, "max_dur_s": 2.5, "min_dur_s": 1.2, "mode": "full"},
  "sfx": {
    "density_per_10s": 2.5, "db": -15,
    "map": {"hook": "sting", "zoom": "click", "broll": "whoosh", "title": "tick", "end": "swell"},
    "stacks": {"reveal": [{"type": "swell", "db": -16}, {"type": "impact", "db": -11}]},
    "cut_coverage": 0.35, "min_gap_s": 0.25, "reveal_every_s": 0
  },
  "music": {"energy": "low", "db": -21, "duck": true},
  "grade": {"contrast": 1.04, "saturation": 1.0, "warmth": 0.0, "vignette": false},
  "transitions": {"default": "dip", "on": "beats", "dur_s": 0.12, "strength": 0.3},
  "end_card": {"enabled": true, "dur_s": 1.5},
  "_needs_feature": {
    "source_tag": {"position": "top_right", "size": 0.018, "text_from": "beat.source", "on": "every_broll_and_screenshot"},
    "stat_counter_beat": "beat role 'number' -> B-roll kind motion template stat-counter with a source line, plus the reveal stack",
    "numbered_steps": "beat role 'step' auto-prefixes 1/2/3 on the hook/kicker card or a step-cards motion insert",
    "screenshot_slam": "full-width screenshot on a blurred copy of itself with a red circle annotation; sfx 'paper'",
    "redact": "auto-blur faces of unknown people, plates and phone/account digits in B-roll (QC already flags unknown faces)",
    "helpline_card": "end card line from brand.compliance.helpline (SG ScamShield 1799)",
    "logo_pill": "small brand pill top-right, persistent"
  }
}
```

### C2. news-silent-case (new: the Straits Times spine)
```json
{
  "name": "news-silent-case",
  "label": "Silent case story (text on stock, no VO)",
  "kind": "genre",
  "description": "From N8 (@straits_times x SPF, 3.9k likes): a one-line loss hook, 5-7 text-on-B-roll cards of 4-6 s with one sentence each, a stat counter, a bold-verb checklist held 6-8 s, partner logos. Music is the voice.",
  "reference": "research/genre-research-2026-10/news-doc-explainer.md#A1",
  "structure": {"name": "silent-case", "target_s": [40, 55], "beats": ["loss hook", "who/what", "what happened", "the twist", "the number", "checklist", "logos"]},
  "pacing": {"remove_silence_over_s": 0, "max_shot_s": 6.0},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "persistent": false, "position_y": 0.62, "size": 0.03, "uppercase": false, "max_words": 18, "dur_s": 5.0},
  "zoom": {"mode": "smooth", "every_s": 5.0, "scale": 1.05, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 5.0, "max_dur_s": 6.0, "min_dur_s": 4.0, "mode": "full"},
  "sfx": {"density_per_10s": 0.6, "db": -18, "map": {"hook": "riser", "broll": "whoosh", "title": "tick", "end": "swell"}},
  "music": {"energy": "mid", "db": -16, "duck": false},
  "grade": {"contrast": 1.06, "saturation": 0.9, "warmth": -0.03, "vignette": true},
  "transitions": {"default": "dip", "on": "cuts", "dur_s": 0.4, "strength": 0.6},
  "end_card": {"enabled": true, "dur_s": 2.0},
  "_needs_feature": {
    "text_per_broll": "a text card per B-roll item from beat.text (box style, bottom-left third), replacing captions",
    "crossfade": "real dissolves between B-roll (dip is a brightness pulse, not a crossfade)",
    "stat_counter_beat": "motion stat-counter in the accent colour (#FFD54F) with a one-line source",
    "checklist_card": "a bold-verb list card (Check / Verify / Use / Avoid) held 6-8 s"
  }
}
```

### C3. scam-remix-onetake (new: 22b)
```json
{
  "name": "scam-remix-onetake",
  "label": "Trick-on-the-viewer remix (one take, trend parody)",
  "kind": "genre",
  "description": "From N1 Hougang NPC 'Singa(pore) Inferno' (370k likes, 5M+ views): one 15-25 s take, direct address from frame 0 at ~220 wpm, three 'you think X but Y' reveals, the lesson line, the final physical reveal (hand over lens / swap). Persistent parody title on top, 2-4 word serif captions beside the head with the punch word in the accent colour. No SFX, trend bed only.",
  "reference": "research/genre-research-2026-10/news-doc-explainer.md#22b",
  "structure": {"name": "remix-onetake", "target_s": [15, 25], "beats": ["direct address + mystery prop 0s", "reveal 1", "reveal 2", "reveal 3", "lesson line", "final reveal"]},
  "pacing": {"remove_silence_over_s": 0.0, "remove_fillers": "none", "max_shot_s": 30.0, "drop_retakes": true},
  "captions": {"enabled": true, "font": "Instrument Serif", "bold": false, "size": 0.034, "max_words": 4, "animation": "pop", "position_y": 0.42, "uppercase": false, "keyword_caps": false, "highlight": "#E0218A", "outline": 0, "shadow": 1},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "outline", "persistent": true, "position_y": 0.06, "size": 0.045, "uppercase": true, "max_words": 3},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0, "map": {}},
  "music": {"energy": "mid", "db": -20, "duck": true},
  "grade": {"contrast": 1.0, "saturation": 1.02},
  "end_card": {"enabled": false},
  "_needs_feature": {
    "captions.beside_face": "place the caption block next to the head (face box from YuNet), alternating sides when the head moves",
    "music.in_app_only": "personal accounts: trending sound added in-app, recorded in PUBLISH.md; brand accounts: original sound-alike only"
  }
}
```

### C4. documentary (corrected)
```json
{
  "name": "documentary",
  "label": "Documentary / investigative (short-form)",
  "kind": "style",
  "description": "Measured on Johnny Harris + CNA Insider + SPF doc reels: VO-led, cuts at a 1.2-2 s median inside 6-10 s evidence beats, a near-wordless process cold open, small boxed caps captions, source tag on every evidence shot, a continuous bed (time below -30 dBFS 12-18%), paper/foley SFX, swell+impact on the turn, -14 LUFS.",
  "reference": "research/genre-research-2026-10/news-doc-explainer.md#20",
  "structure": {"name": "doc-short", "target_s": [60, 100], "beats": ["process cold open 0-9s", "the question", "evidence 1", "evidence 2", "evidence 3", "turn by ~65%", "what it means", "full-video CTA"]},
  "pacing": {"remove_silence_over_s": 0.4, "pad_s": 0.1, "remove_fillers": "hard", "max_shot_s": 4.0},
  "captions": {"enabled": true, "max_words": 6, "animation": "static", "keyword_caps": false, "uppercase": true, "size": 0.024, "position_y": 0.76, "outline": 0, "shadow": 0, "highlight": "#FFFFFF"},
  "hook_text": {"enabled": false},
  "lower_third": {"size": 0.026, "box": "#000000", "box_alpha": 0.7, "position_y": 0.7},
  "zoom": {"mode": "smooth", "every_s": 3.0, "scale": 1.04, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 2.0, "max_dur_s": 2.5, "min_dur_s": 1.0, "mode": "full"},
  "sfx": {
    "density_per_10s": 2.0, "db": -17,
    "map": {"hook": "riser", "broll": "whoosh", "title": "tick", "end": "swell"},
    "stacks": {"reveal": [{"type": "swell", "db": -15}, {"type": "impact", "db": -10}, {"type": "boom", "db": -12}]},
    "cut_coverage": 0.3, "min_gap_s": 0.3, "reveal_every_s": 25
  },
  "music": {"energy": "low", "db": -21, "duck": true},
  "grade": {"contrast": 1.04, "saturation": 0.95, "warmth": 0.0, "vignette": false},
  "end_card": {"enabled": true, "dur_s": 1.5},
  "_needs_feature": {
    "captions.box": "caps caption in a black box (box_alpha 0.75), lower third",
    "source_tag": {"position": "top_right", "size": 0.018, "text_from": "beat.source"},
    "highlighter_swipe": "animated highlighter stroke over a word region on a document still (teal #2EC4B6)",
    "archival_texture": "per-B-roll b/w + grain when beat.era == 'past'",
    "sfx kinds paper, print, typing": "foley kinds for documents and search screens",
    "loudness_renormalise_inserts": "normalise broadcast inserts (-19..-21 LUFS) before the mix"
  }
}
```

### C5. doc-paper-trail (new: investigation spine)
```json
{
  "name": "doc-paper-trail",
  "label": "Investigation / paper trail (Johnny Harris-style grammar)",
  "kind": "style",
  "description": "From D1 (5.3k likes): a near-wordless cold open of searching and dead links, the question, then printed documents with highlighter swipes, cut at a ~1.2 s median; small boxed caps captions; foley-led sound. Use for 'who paid for this', 'where did this come from'.",
  "reference": "research/genre-research-2026-10/news-doc-explainer.md#A2",
  "structure": {"name": "paper-trail", "target_s": [45, 90], "beats": ["silent search cold open", "the find", "the question", "document 1", "document 2", "the name/turn", "what it means"]},
  "pacing": {"remove_silence_over_s": 0.5, "pad_s": 0.1, "max_shot_s": 3.0},
  "captions": {"enabled": true, "max_words": 6, "animation": "static", "uppercase": true, "size": 0.022, "position_y": 0.78, "outline": 0},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "smooth", "every_s": 2.0, "scale": 1.05, "on_hook": 1.0},
  "broll": {"every_s": 1.4, "max_dur_s": 2.0, "min_dur_s": 0.6, "mode": "full"},
  "sfx": {"density_per_10s": 3.0, "db": -16, "map": {"hook": "click", "broll": "paper", "title": "tick", "end": "boom"}, "cut_coverage": 0.4, "min_gap_s": 0.2, "reveal_every_s": 20,
          "stacks": {"reveal": [{"type": "swell", "db": -15}, {"type": "impact", "db": -10}]}},
  "music": {"energy": "low", "db": -22, "duck": true},
  "grade": {"contrast": 1.06, "saturation": 0.9, "warmth": 0.04, "vignette": true},
  "end_card": {"enabled": false},
  "_needs_feature": {
    "captions.box": "black-box caps captions",
    "highlighter_swipe": "see documentary",
    "screen_capture_beat": "beat.visual.type 'screen' = a screen recording at 100% legibility with a cursor",
    "cold_open_wordless": "allow the first 5-9 s with no captions and only foley + ambient"
  }
}
```

### C6. myth-buster-stitch (new: §21 default)
```json
{
  "name": "myth-buster-stitch",
  "label": "Myth-buster: claim -> look closely -> evidence with PiP -> face -> origin receipt",
  "kind": "genre",
  "description": "From E1 Dr Karan Rajan toilet-roll myth (75k likes): voice from 0.0 s at 230-240 wpm, the myth shown as its artefact, labelled evidence images with the expert as a PiP (or the editor's split layout), a layout change every 4-6 s, the origin post as the receipt, a one-line verdict.",
  "reference": "research/genre-research-2026-10/news-doc-explainer.md#21",
  "structure": {"name": "myth-buster", "target_s": [30, 70], "beats": ["myth artefact 0-4s", "look closely", "mechanism 1 (evidence)", "mechanism 2 (evidence)", "why it matters", "origin receipt", "verdict"]},
  "pacing": {"remove_silence_over_s": 0.25, "pad_s": 0.04, "remove_fillers": "hard", "max_shot_s": 6.0, "drop_retakes": true},
  "captions": {"enabled": true, "max_words": 4, "animation": "pop", "size": 0.034, "position_y": 0.5, "uppercase": false, "keyword_caps": false, "outline": 0, "shadow": 1, "highlight": "#FFFFFF"},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "snap", "every_s": 4.0, "scale": 1.06, "on_hook": 1.1, "on_emphasis": true},
  "broll": {"every_s": 5.0, "max_dur_s": 6.0, "min_dur_s": 3.0, "mode": "split"},
  "sfx": {"density_per_10s": 1.5, "db": -15, "map": {"hook": "impact", "zoom": "whoosh", "broll": "whoosh", "title": "pop", "end": "impact"}, "min_gap_s": 0.3},
  "music": {"energy": "low", "db": -22, "duck": true},
  "grade": {"contrast": 1.04, "saturation": 1.04},
  "end_card": {"enabled": false},
  "_needs_feature": {
    "broll.mode pip_corner": "expert PiP bottom-right at ~35% width over full-frame evidence (today: split top/bottom or pip default position)",
    "annotate": "red circle / arrow on an evidence still at a given xy and time; sfx 'pop'",
    "evidence_labels": "small label text placed on the evidence image (from beat.label)",
    "myth_card": "the claim recreated as a social-post card (name masked) when the original can't be shown"
  }
}
```

---

## D. Three core rules per module

**§22 News / scam-expose**
1. Voice (or the kicker card) at frame 0 and a face or a real artefact by 1 s. Never open on an advisory slate, crest or letterbox: the advisories measured 7.6-9.8 s to the first word and got about 0.1-0.2 % of the remix's likes.
2. Teach one trick per post, and if you can, *perform it on the viewer* (22b). Then give 3-4 numbered actions plus the official helpline. Keep exactly one statistic, shown with its source and date.
3. Pattern, not people: no private names or faces, masked numbers, a source tag on every claim, "Dramatisation" on recreations, no police/government look-alike branding. For SG (POFMA) and VN (Decree 15), quote official wording; never extrapolate a number.

**§20 Documentary / investigative**
1. Open on process, not opinion: 5-9 s of the investigator doing something (searching, printing, opening a box) before the question.
2. Cut inside beats at a 1.2-2 s median while the VO holds 6-10 s per evidence point. Every evidence shot carries a source tag; documents get a highlighter or circle on the exact line.
3. Reconstruct in a style nobody can mistake for footage (collage, neon date stamps, labelled dramatisation). No photoreal AI of real people. Bed under everything; -14 LUFS.

**§21 Explainer / myth-buster**
1. Show the myth as its own artefact first, then "look closely". The claim's evidence is the hook.
2. Talk at 220-240 wpm with no dead air (the control E6 cut faster but spoke at 104 wpm runtime and got 30 likes). Change the layout every 4-6 s (claim → evidence + PiP → face → receipt), or act each step out with a prop (E4), rather than just cutting faster.
3. End on the origin receipt (where the myth started, dated, private names masked) and a one-line verdict. Every mechanism line has a source in SOURCES.md.

---

## E. For Klaus to judge (unsure / decisions)
1. **The remix sub-style (22b) wins on numbers but carries brand risk.** It worked because a real police officer did it. A brand or clinic doing "trick the viewer" could feel like a bait-and-switch, and on SG health accounts any "reveal" must stay off outcomes. Is it allowed for Physio Spot / heal360, or personal accounts only?
2. **The advisory format is our current draft's spirit** (kicker → steps → source line), and it was the weakest measured. I kept the kicker and steps but moved them *behind* a face or artefact. Agree?
3. **Trend audio:** N1 rides a TV show parody. Using the show's title type/colour is parody of a format, not its footage. Confirm the line: no show music on brand accounts, original sound-alike only.
4. **Doc pacing correction (3-6 s → 1.2-2 s median)** is from VO-led cut-downs of long docs (JH, CNA). A native long-form doc (YouTube 16:9, 10+ min) is slower; the card now targets short-form. Should long form get its own row?
5. **Loudness:** CNA posts some reels at -19/-20.5 LUFS. I set "always re-normalise to -14". OK?
6. **Carousel:** no IG image posts could be downloaded logged-out, so 22c is [researched], not measured. SnapSaigon-type VN pages (ref #2) are still not seen; VN IG mirrors (VTV/MB Bank) get 0-1 likes there because their audience is on FB/TikTok/Zalo.
7. **Whisper language:** 5 Singapore-English reels were auto-detected as Malay. Their wpm is approximate. The engine's ingest should force `language` from the brand file (`en` for SG), or it will mistranscribe Singlish.
8. **Legal items not verified in primary text this run:** SG Online Criminal Harms Act (scam-content directions) and the Online Safety (Relief and Accountability) Act may also touch scam pages. Worth a compliance-pack line after a legal check.

## Appendix: raw numbers
Per-reel JSON: `scratchpad/genreC/dl/<group>/<id>.analysis.json`; sheets: `<id>.sheet.jpg`; logs: `scratchpad/genreC/*_analysis.log`.
