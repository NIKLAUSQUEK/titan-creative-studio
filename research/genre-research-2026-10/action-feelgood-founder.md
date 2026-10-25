# Genre research 2026-10: Action / sport hype (§15), Feel-good / emotional (§9), Founder / comeback (§11)

Overnight run, 2026-10-25. Scope: ground, correct and extend three [draft] cards in
`.claude/skills/higgsfield-creative-director/references/genre-playbooks.md`. Nothing in the playbook or the presets was edited. Klaus decides what moves over.

**Method.** I searched with Firecrawl. Exa ran out of credits after the first call, so all citations come from Firecrawl results or scraped pages. Only public Instagram reels were downloaded (yt-dlp, one retry after 20 s on a 429). Two reels stayed 429-blocked after the retry: DYP9MVAtHVW (Ben Francis, YouTube story) and DUkc_iIDzfm (PETRONAS CNY 2026 "Shop of Wonders"). Others needed the retry. I used no YouTube, TikTok or Vimeo downloads and no cookies. Media and scripts stay in the session scratchpad (`scratchpad/genreD/`), never in the repo.

**Measurements** (my own ffmpeg + numpy, scripts in `scratchpad/genreD/scripts/`):
- **Cuts:** `crop=<cropdetect>` (reposts are letterboxed; without the crop, scene scores fall below threshold and zero cuts are found), then `scale=320:-2,select='gt(scene,0.2)',showinfo`. Cuts within 150 ms are merged. Soft punch-ins/reframes and dissolves are under-counted, so read "avg shot" as an upper bound.
- **Thirds:** average shot length per third of the runtime, which shows whether the edit accelerates or slows.
- **Audio:** EBU R128 integrated LUFS, LRA and true peak (`ebur128=peak=true`). Spectral-flux onsets use median + 6·MAD. "Cuts on onset" is the share of cuts with an onset within ±60 ms, compared with the same test on 500 random times (chance).
- **RMS by decile:** the mean dB of each tenth of the runtime, which shows the loudness arc.
- **Words/min:** faster-whisper `small`, int8, CPU, from audio piped through ffmpeg to 16 kHz s16le.
- **Frame sheets** at 1-2 fps were viewed for every measured reel.

**Caveats.**
- Most brand films were measured from Instagram reposts (aggregator accounts), not the brands' own uploads. Their loudness (-14.1 LUFS almost everywhere) is Instagram's normalisation, not the original mix. Cut timing and structure are preserved.
- Like counts are the repost's own, not the film's. Several personal reels show "3 likes" with dozens of comments, which looks like hidden like counts. I treat those as unknown.
- My kick-drum detector failed (a threshold bug). I report only broadband onsets, and tempo estimates are rough.

---

## 0. Measured reference table

| id | what | source URL (date, account) | reported performance | dur s | cuts | avg / median shot s | shots by third (s) | other measures |
|---|---|---|---|---|---|---|---|---|
| A1 | Nike "You Can't Stop Us" (W+K Portland, dir. Oscar Hudson, 2020) | https://www.instagram.com/reel/Cy-JFIkyqgM/ (2023-10-29, @goodadsmatter repost) | ~60 M YouTube views; Cannes Lions 2021 Film winner (Contagious https://www.contagious.com/en/article/news-and-views/cannes-lions-film-winners-2021); 72 clips from 4,000 searched, 36 split-screen pairs (It's Nice That https://www.itsnicethat.com/news/oscar-hudson-wieden-kennedy-nike-you-cant-stop-us-advertising-060820); repost 169,294 likes, 1,205 comments | 90.0 | 38 | 2.31 / 2.04 (p10 1.2, p90 4.2) | 2.50 → 2.31 → 1.88 (accelerates) | VO 113 words, 91 wpm while speaking, first word at 2.3 s; RMS by decile -27.9 → -19.7 dB (the mix rises ~8 dB to the end); cuts on onset 0.05 vs chance 0.07 (cuts follow motion matches, not beats) |
| A2 | Nike "Winning Isn't for Everyone" anthem (W+K, dir. Kim Gehrig, Willem Dafoe VO, Paris 2024) | https://www.instagram.com/reel/C9po_ojpF6t/ (2024-07, repost) | One Show 2025 Gold Pencil, Writing; "12B+ impressions, 4B+ views, reached 90% of US Gen Z & Millennials, +18% message memorability" (https://www.oneclub.org/awards/theoneshow/-award/58222/winning-isnt-for-everyone/) | 90.1 | 47 | 1.88 / **1.0** (p10 0.4, p90 4.8, max 9.6) | **3.75 → 2.31 → 1.04** (strong acceleration) | -14.1 LUFS, LRA 6.9; classical bed (Berlin/Vienna Phil credits); sheet: extreme close-ups of faces/eyes on dark backgrounds, slow push-ins, slow-motion effort shots |
| A3 | Gymshark Conditioning Club recap (Regent St, London) | https://www.instagram.com/reel/Dd4VcGmoFYN/ (2026-09-29, @alexrennie) | 53 comments; likes hidden | 37.9 | 55 | 0.68 / **0.44** (p10 0.16) | 1.05 → 0.74 → 0.44 (accelerates) | cuts on onset 0.33 vs chance 0.21 (partly beat-synced); LRA 10.1; sheet: low wide-angle handheld into running crowds, red neon gym, small centred typewriter-mono captions, 2-up stacked split screens, 3 s logo card on black at the end |
| A4 | Gymshark Essentials spec ad (creator) | https://www.instagram.com/reel/Da2Tou0o9c5/ (2026-07-16, @ridgwayimagery__) | 32 likes (low) | 10.2 | 6 | 1.46 / 1.30 | flat 1.13 | **cuts on onset 0.83 vs chance 0.25** (hard beat-sync) |
| A5 | Powerlifting "GIVE ME MY THEME MUSIC" edit | https://www.instagram.com/reel/DbS6it8t1fj/ (2026-07-27, @bless_pwrlftz) | 54 likes (low) | 22.2 | 35 | **0.62 / 0.62** (p10 0.42, p90 0.80) | 0.67 → 0.67 → 0.46 | metronomic: one cut per beat-pair at ~0.62 s; music LRA 0.8 (brick-walled); word-by-word yellow CAPS title in the first 1.4 s; federation logos flash in |
| A6 | Powerlifting 300 kg | https://www.instagram.com/reel/DZ7owTXN8Yp/ (2026-06-23, @powerlifts_varun) | 35 comments, likes hidden | 33.7 | 8 | 3.75 / 1.75 (max 12.5) | 2.8 → 2.8 → 3.75 | **the full lift is held uncut (12.5 s)**; quick cuts only around it |
| A7 | Gym edit "pure power" | https://www.instagram.com/reel/DY6Hu34Kk0-/ (2026-05-29, @mightyraj83) | likes hidden, 11 comments | 16.5 | 9 | 1.65 / 1.76 | 0.92 → 1.83 → 1.83 | burst of 0.2-0.3 s cuts in the first 2 s, then ~2 s holds |
| F1 | Thai Life Insurance "Unsung Hero" (Ogilvy & Mather Bangkok, 2014) | https://www.instagram.com/reel/DWXnBo1DMbN/ (2026-03-27, @vacations repost) | "6 M views in the first week, 17 M in 232 countries within a month, 117 M+ on the original upload"; spawned "try not to cry" reaction videos (https://www.selfstorming.com/tools/libraries/campaigns/thai-life-insurance-unsung-hero; Business Insider 2014 https://www.businessinsider.com/thai-life-tearjerker-ad-2014-4); repost 19,408 likes, 234 comments | 177.9 | 68 | **2.58 / 2.10** (p10 1.16, p90 3.82, **max 10.6**) | 2.2 → 2.7 → 2.7 (slows after the midpoint) | **no dialogue for the first 37 s**; only 120 spoken words in 178 s (51 wpm while speaking), mostly in the last third; quiet hole at ~107-125 s (decile 7 RMS -34.6 dB vs ~-20 around it) before the payoff swell; warm, washed, low-contrast beige grade; a persistent small text header on the repost |
| F2 | PETRONAS "My Son" (Leo Burnett Malaysia, CNY 2006, Yasmin Ahmad era) | https://www.instagram.com/reel/DU2O_tWEZf8/ (2026-02-17, @planetofads repost) | repost 221 likes (low); the brand series is famous (Campaign Asia, LBB coverage) | 131.9 | 54 | 2.40 / 1.83 (max 9.7) | 1.76 → 3.14 → 2.44 | dialogue-led: aunties trade brags over a festive lunch in shot-reverse-shot over-the-shoulder close-ups with burned-in subtitles; the warmth comes from the people, not the score; -14.2 LUFS, LRA 8.6 |
| F3 | PETRONAS "Once More" (Season's Greetings / New Year 2026, 20 s cutdown) | https://www.instagram.com/reel/DSrCoZ4EYfo/ (2025-12-25, @petronas official) | 180 likes | 20.1 | 5 | **3.35 / 2.93** | 2.2 → 2.2 → 3.35 | warm practical fairy lights, mauve/rose grade, macro on a baby's fist, a group embrace, lantern night wide, handwritten title card for the last ~4 s; logo persistent top-right |
| C1 | Sara Blakely (Spanx) at Hello Sunshine "Shine Away", the Neiman Marcus story | https://www.instagram.com/reel/DC47FDWxlpv/ (2024-11-27, @hellosunshine) | **11,059 likes, 178 comments** | 76.5 | 16 (+ uncounted punch-ins) | 4.5 / 4.4 (max 9.8) | 3.6 → 3.6 → 5.1 | big white CAPS header "THE MOMENT SARA BLAKELY REVOLUTIONIZED CLOTHING" for the first ~7 s; close-up ↔ wide-with-audience every 3-5 s; small sentence subs; one specific scene told in dialogue ("Can I have 15 minutes…", "come with me to the bathroom"); **218 wpm** while speaking, words from 0.0 s |
| C2 | Ben Francis (Gymshark founder), "original ambition: sell one thing online" | https://www.instagram.com/reel/DRnBLsXDQE-/ (2025-11-28, @benfrancis) | 2,382 likes, 47 comments | 29.5 | 2 (+ split-layout switches) | 9.9 / 8.1 | – | **234 wpm** (probably sped up ~1.15-1.2×); words from 0.0 s; podcast clip; 2-line white captions with a yellow keyword; from 18 s a 2-up layout (close-up top, wide bottom); LRA 2.9 |
| C3 | Jack Khorsandi street interview "how did you make your first million" | https://www.instagram.com/reel/DehjfyxRDu2/ (2026-10-15) | 116 likes (low) | 80.3 | 11 | 6.7 / 5.5 | – | 153 wpm; Q&A format; words from 0.0 s |
| C4 | "Spare bedroom" founder (@poweredbysage) | https://www.instagram.com/reel/DdSIhiAiMJC/ (2026-09-14) | 17 likes (low) | 43.9 | 4 | 8.8 / 9.9 | – | 235 wpm; walk-and-talk |

Researched only (not downloadable here):
- **Dollar Shave Club "Our Blades Are F***ing Great" (2012).** A one-take founder rant by Michael Dubin. It cost $4,500 and "drew 12,000 orders in 48 hours" (https://echai.ventures/videos/dollar-shave-club-dollarshaveclub-com-our-blades-are-f-ing-great). Unilever bought the company for $1 B in 2016 (WSJ, https://www.wsj.com/articles/funny-video-led-to-1-billion-deal-for-dollar-shave-club-1469055206).
- **System1 on emotion.** "Happiness is the emotion most strongly associated with long-term brand growth." "The most effective journey is one where negative emotions bring tension to the middle of the storyline, then find a resolution by the end." The average UK TV ad leaves 52% of viewers neutral. Sport ads "typically struggle to resonate with mass audiences". The 2025 top-10 included a sport ad with +48% happiness vs sport-themed ads. Sources: https://system1group.com/blog/the-important-role-of-emotion-in-advertising, https://lbbonline.com/news/System1-Reveals-the-10-Brands-that-Cut-Through-in-2025.
- **Founder-led ad performance.** MHI Media reports "2.7× CTR, 31% lower CPA vs UGC, 67% vs 43% completion" over 1,200+ campaigns (https://mhigrowthengine.com/blog/what-is-founder-led-advertising-complete-guide/). **This is a vendor claim with no published method; don't quote it in client decks.** Cybertize (2026) adds: shoot in the founder's real workspace, natural light, a single take per topic, and don't cut out the "imperfect pause" (https://cybertizemedia.com/blog/founder-led-ads/).
- **Unruly via Business Insider:** SE-Asian brands use tear-jerkers because "those are the kinds of ads people in South-East Asia are most likely to share".

---

## 1. Action / sport hype (§15), corrected card

### What changed and why
- **The old card said "0.5-1.5 s cuts on the beat" for the whole genre. The evidence splits it in two:**
  - **Sport anthem / brand film (A1, A2).**
    - Median shot 1.0-2.0 s. Long holds up to 5-10 s on faces.
    - **The cut rate accelerates across the piece** (A2: 3.75 → 2.31 → 1.04 s per third; A1: 2.50 → 1.88).
    - Cuts follow the VO lines and motion matches, **not** the beat (A1 cut-on-onset 0.05 = chance).
    - VO is sparse: 90-ish wpm and only about 110-150 words in 90 s.
    - The mix gets louder toward the end (A1 +8 dB).
  - **Creator gym / event hype (A3-A5).**
    - Median shot 0.44-0.62 s, cut on the beat (A4 0.83 vs 0.25 chance; A5 metronomic ~0.62 s).
    - Accelerating into the drop (A3 1.05 → 0.44).
    - A brick-walled music bed (LRA 0.8-1.6) with no VO.
- **New rule from A6: show the full lift or play uncut.** The rep from unrack to lockout is the proof, so the edit cuts around it, never inside it. Cutting mid-rep reads as fake. The same goes for a goal, a sprint finish or a PB.
- **Speed ramps and freeze frames** were in the old card. I could not measure them (no detector), and I did not see a clear freeze frame on the sheets. They stay as a craft option, not a rule. **Flagged for Klaus.**
- **The grade is not always "crushed + desaturated".**
  - A2 is dark and contrasty with skin rendered rich. A1 is natural archival colour.
  - A3 is saturated red neon + daylight. The common thread is **one dominant colour world per film**, not a fixed desaturation.
- **Type** is small and quiet in brand work: A3 uses small typewriter-mono captions and A2 has no captions. Big caps type is the creator style (A5's word-by-word yellow title).

### 15. Action / sport hype (two modes) [measured: A1 https://www.instagram.com/reel/Cy-JFIkyqgM/, A2 https://www.instagram.com/reel/C9po_ojpF6t/, A3 https://www.instagram.com/reel/Dd4VcGmoFYN/, A4 https://www.instagram.com/reel/Da2Tou0o9c5/, A5 https://www.instagram.com/reel/DbS6it8t1fj/, A6 https://www.instagram.com/reel/DZ7owTXN8Yp/]
- **Why it works:**
  - The anthem mode makes a provocation (a question or a "we will…" vow) and then proves it with faces and effort.
  - The edit speeds up as the argument builds, so the viewer's pulse follows the cut rate.
  - The creator mode is pure rhythm: one action per beat, then the payoff rep held in full.
- **Pick a mode:**
  - **15a Anthem** for brand films and ads with a message (Power Protein, TITAN.AI "we don't quit");
  - **15b Gym / event hype** for training reels, event recaps and launches (Physio Spot return-to-sport day, Power Protein gym collab).
- **Pacing map, 15a Anthem (30 s ad, scaled from the 90 s measurements):**

| Beat | 30 s | Shot length | What happens |
|---|---|---|---|
| Provocation | 0-4 s | one 3-4 s hold | a face in extreme close-up, eyes to lens or just off; the VO asks the question or names the doubt |
| Build 1 | 4-12 s | 2-3 s | effort details (breath, chalk, a grip, a sweat drop) in slow motion; VO line, beat, VO line |
| Build 2 | 12-22 s | 1-1.5 s | more athletes and sports, match-cut on motion (a jump continues into another jump) |
| Peak | 22-26 s | 0.4-1 s burst | 5-8 fast impacts; the music peaks; the mix is at its loudest |
| Payoff + brand | 26-30 s | one 3-4 s hold | a held face or the full action, then the line and the logo on black |

- **Pacing map, 15b Gym / event hype (15-30 s):**
  - 0-1.5 s: a word-by-word title or the heaviest moment;
  - 1.5 s → drop: 1-2 beats per shot (~0.6-1.0 s);
  - after the drop: one shot per beat (0.4-0.65 s), with bursts of 0.15-0.3 s;
  - **the money rep / finish is held uncut (3-12 s)**;
  - a 2-3 s logo or end card.
- **Shot grammar:**
  - **15a:**
    - 85-135 mm extreme close-ups of faces and eyes on dark, clean backgrounds;
    - slow push-ins;
    - 50-100 fps slow motion on effort;
    - match-cuts on motion direction across different sports or people (A1's split-screen pairs are the extreme version);
    - one hero wide at the payoff.
  - **15b:**
    - 14-24 mm low-angle handheld at knee height running with the group;
    - over-the-shoulder lifts;
    - 2-up stacked split screens to show two moments at once (A3);
    - a federation, venue or brand logo flashed on a beat;
    - phone footage is fine.
- **Look:**
  - One colour world per piece.
  - 15a: dark contrasty skin-rich, or archival natural.
  - 15b: venue light (neon, gym fluorescents, daylight) pushed for saturation.
  - Brand accent: one colour (the brand's), carried by set dressing or kit, not by a grade trick.
- **genre_key 15a:** `high-end sports anthem film, extreme close-up portraits on dark clean backgrounds, rich skin tones, hard side light, slow motion effort detail, sweat and breath visible, shallow depth of field, deliberate slow push-in`
- **genre_key 15b:** `raw high-energy fitness event footage, low wide-angle handheld at knee height, motion blur, venue neon and daylight, saturated, crowd energy, authentic phone-camera texture`
- **Shot (15a):** `{"id":"S01","dur":3.5,"camera":"locked 100mm extreme close-up, slow push-in 3%","subject":"@ATHLETE face, eyes just off lens","action":"start: exhales through the nose -> end: eyes lift to lens, jaw sets","light":"single hard side key, black background, rim on sweat","audio":"breath, low room tone; VO line 1 starts at 0.8 s","genre_key":"<15a key>"}`
- **Shot (15b):** `{"id":"S07","dur":6,"camera":"low 18mm handheld, side-on, no cut","subject":"@LIFTER deadlift","action":"start: grips bar -> end: lockout and roar, plates settle","constraints":"full rep in one take; do not speed up the rep","genre_key":"<15b key>"}`
- **Sound:**
  - **15a:**
    - an orchestral or cinematic bed that grows ~6-8 dB from start to end;
    - VO sparse (≤ 100 wpm), each line followed by a breath of picture;
    - SFX are foley (breath, impact, crowd) rather than whooshes;
    - one sub-hit on the peak burst; silence of ≤ 0.5 s before the payoff line.
  - **15b:**
    - the music carries it (licensed or original for brands, phonk/trend on personal accounts only);
    - cut on onsets (aim ≥ 60% of cuts within 60 ms of an onset);
    - impact on the lockout;
    - the crowd or a roar is kept live.
- **Compliance (fitness pack):**
  - no unrealistic transformations or "X kg in Y days";
  - no body shaming;
  - age-gate weight-loss content.
  - SG health brands (Physio Spot, heal360): sport hype is fine for return-to-sport *stories*, but never as an outcome promise ("back on court in 2 weeks"), and never a patient as the athlete.
  - Real athletes need image rights. No AI likeness of real athletes.
- **Preset:**
  - 15a `sport-anthem` (new, below);
  - 15b `action-hype` (corrected, below).

### Preset: `action-hype` (corrected, = 15b gym / event hype)
```json
{
  "name": "action-hype",
  "label": "Action / sport hype: gym & event edit (15b)",
  "kind": "genre",
  "description": "Measured on Gymshark Conditioning Club recap (median 0.44 s, accelerating 1.05->0.44 s by third), Gymshark spec (83% of cuts on onsets) and powerlifting edits (metronomic ~0.62 s; the full lift held uncut up to 12.5 s). Music-led, no VO, cut on onsets, word-by-word title in the first 1.5 s, small or big type depending on account, one held money-rep, logo card at the end.",
  "reference": "research/genre-research-2026-10/action-feelgood-founder.md#1",
  "beat_sync": true,
  "structure": {"name": "hype", "target_s": [15, 35], "beats": ["title / heaviest moment 0-1.5s", "build to drop (1-2 beats per shot)", "drop: one shot per beat", "money rep held uncut", "logo card"]},
  "pacing": {"remove_silence_over_s": 0.2, "pad_s": 0.03, "max_shot_s": 1.0, "remove_fillers": "hard"},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "font": "Anton", "uppercase": true, "size": 0.07, "position_y": 0.12, "max_words": 5, "dur_s": 1.5, "color": "#FFE14D", "outline": 0},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.08, "on_hook": 1.12, "on_emphasis": false},
  "broll": {"every_s": 0.6, "max_dur_s": 0.9, "min_dur_s": 0.3, "mode": "full"},
  "sfx": {"density_per_10s": 2, "db": -12, "cut_coverage": 0.15, "min_gap_s": 0.8, "map": {"hook": "impact", "broll": "whoosh", "end": "boom"}},
  "music": {"energy": "high", "db": -8, "duck": false},
  "grade": {"contrast": 1.12, "saturation": 1.1, "vignette": false},
  "transitions": {"default": "flash", "on": "beats", "dur_s": 0.06, "strength": 0.35},
  "end_card": {"enabled": true, "dur_s": 2.5},
  "hold": {"money_rep": {"min_s": 3, "max_s": 12, "uncut": true}, "_needs_feature": "mark one beat as a protected uncut hold that max_shot_s and beat-sync must not split (brief beat role 'proof_hold')"},
  "pacing_curve": {"by_third_s": [1.0, 0.7, 0.45], "burst": {"len_s": [0.15, 0.3], "count": [3, 6], "where": "before_drop"}, "_needs_feature": "per-third shot-length targets + burst cuts; today max_shot_s is one number"},
  "_needs_feature_split": "broll mode 'split' exists (top/bottom); A3 uses 2-up stacked clips of the SAME energy (two B-rolls, no speaker). Needs broll mode 'stack2'."
}
```

### Preset: `sport-anthem` (new, = 15a)
```json
{
  "name": "sport-anthem",
  "label": "Sport anthem film (15a, Nike-style VO manifesto)",
  "kind": "genre",
  "description": "Measured on Nike 'Winning Isn't for Everyone' (median 1.0 s, 3.75->2.31->1.04 s by third, holds to 9.6 s) and 'You Can't Stop Us' (median 2.0 s, 2.5->1.9 s, cuts on motion not beats, mix +8 dB start->end). Sparse VO manifesto (~90 wpm), extreme close-ups on dark grounds, slow motion effort, peak burst, held payoff and logo on black. No captions in the films; burn sentence subs only for mute-first placements.",
  "reference": "research/genre-research-2026-10/action-feelgood-founder.md#1",
  "beat_sync": false,
  "structure": {"name": "anthem", "target_s": [30, 90], "beats": ["provocation hold", "build 1 (2-3 s)", "build 2 (1-1.5 s, match cuts)", "peak burst (0.4-1 s)", "payoff hold + line + logo"]},
  "pacing": {"remove_silence_over_s": 0.6, "pad_s": 0.15, "max_shot_s": 4.0, "remove_fillers": "hard"},
  "captions": {"enabled": true, "font": "Space Grotesk", "bold": false, "size": 0.03, "max_words": 6, "animation": "fade", "uppercase": false, "keyword_caps": false, "outline": 0, "shadow": 2, "position_y": 0.8},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "smooth", "every_s": 3, "scale": 1.04, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 2.0, "max_dur_s": 3.0, "min_dur_s": 0.4, "mode": "full"},
  "sfx": {"density_per_10s": 1.2, "db": -16, "cut_coverage": 0.1, "min_gap_s": 1.5, "map": {"hook": "swell", "broll": "whoosh", "end": "boom"}, "reveal_every_s": 0},
  "music": {"energy": "mid", "db": -16, "duck": true},
  "grade": {"contrast": 1.15, "saturation": 0.92, "warmth": 0.02, "vignette": true},
  "transitions": {"default": "cut"},
  "end_card": {"enabled": true, "dur_s": 2.5},
  "pacing_curve": {"by_third_s": [3.5, 2.2, 1.0], "_needs_feature": "per-third shot-length targets (acceleration)"},
  "music_arc": {"start_db": -24, "end_db": -14, "_needs_feature": "bed gain ramp across the piece (measured +8 dB on A1)"},
  "speed": {"slowmo_on": "effort", "factor": 0.5, "_needs_feature": "per-item speed exists (constant 0.25-4); ramps 1.0->0.3 within one item do not"}
}
```

### 3 core rules (action)
1. **Pick the mode first.** An anthem accelerates (≈3.5 → 2 → 1 s per third) and cuts on VO lines and motion. A gym/event hype cuts on the beat (0.4-0.65 s). Never mix the two grammars in one piece.
2. **Show the proof uncut.** The money rep, the finish or the goal plays from start to completion in one shot (3-12 s). The fast cutting lives around it.
3. **Build the loudness and the cut rate together.** The last third is the fastest and loudest. End on a held face or action, the line, and the logo on black.

### Flags for Klaus (action)
- Speed ramps and freeze frames: keep them as optional craft or drop them? I found no measured evidence either way.
- Is splitting into `sport-anthem` (new) + `action-hype` (creator) acceptable, or should one preset carry a `mode` switch?
- A3's typewriter-mono captions need a mono font (e.g. Space Mono, OFL). There is none in `tools/editor/fonts/` yet.
- All creator gym references here are low-engagement accounts or hidden likes. A3 is the only one with a real brand behind it. A higher-performing gym edit (≥100k likes) still needs measuring; ask Klaus for 2-3 links.

---

## 2. Feel-good / emotional (§9), corrected card

### What changed and why
- **Average shot length: the old card said 3-5 s. Measured 2.1-2.9 s median (F1 2.10, F2 1.83, F3 2.93).**
  - Emotion here comes from **one long hold (9-11 s) at the reveal** (F1 max 10.6 s, F2 9.7 s) set against otherwise brisk 2-ish-second storytelling. It is not slow everywhere.
- **Pace curve:** F1 slows after the midpoint (2.2 → 2.7 s). The film settles down as it moves toward the payoff.
- **Words:** F1 has no dialogue for the first 37 s and only 51 wpm while speaking, with most words in the last third.
  - The hook is a **visual act with a header**, not a spoken line. The "why" is spoken late.
  - F2 is the counter-model: dialogue-led ensemble comedy that turns. Both work. The card now names both structures.
- **Sound:** F1 has a measured quiet hole (~18 s, about 15 dB under its surroundings) right before the payoff, then a swell. The old card's "let silence breathe 1-2 s" undersells this. **Drop the bed into near-silence for several seconds before the reveal.**
- **Structure:** System1 says tension in the middle and a resolution to a peak at the end beats steady positivity. That matches F1 (people mock the hero, the hero gives his money away) and Thai Life's model generally.
- **The 30 s timing in the old card is unrealistic for the genre.** Every high-performing reference is 90-180 s and runs as a web film. On social, the 15-30 s piece is a **cutdown** (F3) that keeps the hold, the macro detail and the title card.

### 9. Feel-good / emotional [measured: F1 https://www.instagram.com/reel/DWXnBo1DMbN/, F2 https://www.instagram.com/reel/DU2O_tWEZf8/, F3 https://www.instagram.com/reel/DSrCoZ4EYfo/]
- **Why it works:**
  - a repeated small act the viewer doesn't understand yet (curiosity);
  - others doubting it (tension);
  - the reveal of what it gave back, held long enough to land;
  - one wisdom line;
  - the brand only at the end. SE-Asian audiences share these (Unruly).
- **Two structures:**
  - **9a Quiet hero** (Thai Life model): wordless repetition → doubt → near-silence → reveal hold → VO wisdom.
  - **9b Ensemble turn** (PETRONAS model): warm, funny dialogue among family or friends → a line that turns it → a held reaction.
- **Pacing map (hero film 90-180 s; 30 s cutdown in brackets):**

| Beat | Film | 30 s cutdown | Shots |
|---|---|---|---|
| Hook: the act | 0-10 s | 0-3 s | the kind act with a small header ("He does this every day. Why?"); no dialogue |
| Repetition + details | 10-60 s | 3-12 s | the same act on different days; hands, coins, a plant, a dog; 2-2.5 s shots |
| Doubt / tension | 60-100 s | 12-17 s | someone mocks, shakes their head, or he loses something; 2.5-3 s |
| Quiet hole | 100-120 s | 17-20 s | the bed drops ~15 dB to room tone; slower shots |
| Reveal hold | 1 shot, 8-11 s | 20-25 s (one 4-5 s hold) | the payoff (the girl in school uniform, the mother's face); push-in 3-5% |
| Wisdom + brand | last 15-25 s | 25-30 s | the VO line, the title card (handwritten or serif), the logo |

- **Shot grammar:**
  - observational handheld that is steady but alive;
  - mid-shots for the act, macro for hands and objects (F3's baby fist);
  - over-the-shoulder shot-reverse-shot for dialogue (9b);
  - a single push-in only on the reveal;
  - 35-50 mm, natural eye level, nothing showy.
- **Look:**
  - warm, washed, low contrast;
  - beige/golden daylight (F1) or tungsten practicals and fairy lights at night (F3);
  - lifted blacks, never crushed;
  - skin warm.
- **genre_key:** `warm natural light, washed low-contrast film look, lifted shadows, observational handheld, everyday streets and homes, genuine understated emotion, small tactile details, golden beige tones` (night variant: replace the first item with `tungsten practicals and fairy lights`).
- **Shot (reveal):** `{"id":"S14","dur":9,"camera":"locked 50mm mid-shot, push-in 4% over the shot","subject":"@GIRL in a school uniform, @HERO sees her","action":"start: he stops on the pavement -> end: he smiles, eyes wet, says nothing","light":"warm late-afternoon daylight, soft","audio":"room tone only for 2 s, then piano re-enters","constraints":"no dialogue, no music swell before 3 s","genre_key":"<9 key>"}`
- **Sound:**
  - a single instrument bed (piano, guitar or strings) that carries the first half;
  - **a 5-15 s quiet hole (bed -12 to -15 dB, room tone up) before the reveal**;
  - the swell enters 2-3 s into the reveal hold, not on the cut;
  - the VO is spoken slowly (≤ 60 wpm) in the last part;
  - no SFX except diegetic foley;
  - a festive original song works as the bed and the title track (PETRONAS 2026 commissioned "Seindah Kasih", https://www.instagram.com/reel/DV0xuA_Gc6s/).
- **Compliance:**
  - the brand is the enabler, never the saviour of real hardship;
  - no exploiting real people's grief; consent for anyone real;
  - insurance and health brands make no claims inside the story;
  - SG health (Physio Spot/heal360): no patient stories as testimonials, so stage the act around staff or family, not a treated patient's outcome;
  - festive films respect each festival's customs (localisation.md).
- **Preset:** `feelgood-emotional` (corrected, below); the cutdown uses the same preset with `target_s` [15, 30].

### Preset: `feelgood-emotional` (corrected)
```json
{
  "name": "feelgood-emotional",
  "label": "Feel-good / emotional (quiet hero + reveal hold)",
  "kind": "genre",
  "description": "Measured on Thai Life 'Unsung Hero' (median 2.1 s, slows 2.2->2.7 s, 10.6 s reveal hold, no dialogue for 37 s, ~18 s quiet hole before the payoff), PETRONAS 'My Son' (median 1.8 s, dialogue shot-reverse-shot) and PETRONAS 'Once More' cutdown (median 2.9 s, macro detail, title card). Brisk 2-2.5 s storytelling, one long reveal hold, the bed drops out before the reveal, slow VO wisdom line, warm washed grade, small header, title card + logo.",
  "reference": "research/genre-research-2026-10/action-feelgood-founder.md#2",
  "structure": {"name": "feelgood", "target_s": [60, 180], "beats": ["act + header (no dialogue)", "repetition + details", "doubt / tension", "quiet hole", "reveal hold", "wisdom line + title card + logo"]},
  "pacing": {"remove_silence_over_s": 1.2, "pad_s": 0.3, "max_shot_s": 3.5, "remove_fillers": "light"},
  "captions": {"enabled": true, "font": "Poppins", "bold": false, "size": 0.032, "max_words": 7, "animation": "fade", "uppercase": false, "keyword_caps": false, "outline": 0, "shadow": 2, "position_y": 0.8},
  "hook_text": {"enabled": true, "font": "Instrument Serif", "bold": false, "uppercase": false, "size": 0.045, "position_y": 0.16, "max_words": 8, "dur_s": 3.5, "outline": 0},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.04, "on_hook": 1.0, "on_emphasis": true},
  "broll": {"every_s": 2.5, "max_dur_s": 3.0, "min_dur_s": 1.5, "mode": "full"},
  "sfx": {"density_per_10s": 0},
  "music": {"energy": "low", "db": -18, "duck": true},
  "grade": {"contrast": 0.92, "saturation": 0.9, "brightness": 0.02, "gamma": 1.04, "warmth": 0.06, "vignette": false},
  "transitions": {"default": "dip", "on": "beats", "dur_s": 0.4, "strength": 0.3},
  "end_card": {"enabled": true, "dur_s": 4.0},
  "reveal_hold": {"min_s": 4, "max_s": 11, "push_in": 1.04, "_needs_feature": "brief beat role 'reveal' that is exempt from max_shot_s and gets the only push-in"},
  "music_hole": {"before": "reveal", "len_s": [5, 15], "drop_db": -14, "swell_after_s": 2.5, "_needs_feature": "bed automation: drop before the reveal beat, re-enter after the cut (sfx.silence / music.drop_before_reveal are specced in story-sfx-dense but only for 0.2-0.3 s holes)"}
}
```

### 3 core rules (feel-good)
1. **Tell the story briskly (2-2.5 s shots) and give the reveal one long hold (5-11 s).** The contrast is the tear.
2. **Take the music away before the payoff:** several seconds of room tone, and the swell only after the reveal lands.
3. **Show first, say last.** The hook is an act with a small header, and the meaning (the "why", the wisdom line, the brand) is spoken only in the final fifth.

### Flags for Klaus (feel-good)
- The old card's 30 s pacing map is replaced by a film map plus cutdown. Do SG brands even want 2-3 min web films, or only cutdowns?
- F2's emotional turn (the end of "My Son") was not transcribed: I stopped whisper to save CPU. Watch the last 30 s before citing what the turn is.
- The 9b ensemble-turn structure overlaps with comedy (§2). Keep it here or move it to a "festive film" card? A `festive-film` sub-card is proposed below.

### NEW sub-card: 9c Festive film / cutdown (`festive-film`) [measured: F2, F3; researched: Campaign Asia Hari Raya 2025 round-up https://aws1.campaignasia.com/article/hari-raya-2025-the-apac-campaigns-you-need-to-see/501374]
- **Use for:** CNY, Hari Raya, Deepavali, Christmas and National Day pieces for SG/MY brands.
- **Pacing:** the hero film is 90-180 s on YouTube/Facebook. Social gets 15-30 s cutdowns (F3: 5 shots in 20 s, then a title card for the last 4 s).
- **Shot grammar:**
  - an ensemble round a table in over-the-shoulder shot-reverse-shot;
  - one macro symbol (hands, food, a baby's fist);
  - one wide of the festive night (lanterns, fireworks).
- **Look:** tungsten and fairy-light practicals, rose/mauve or gold grade, the logo small and persistent top-right.
- **Sound:** a commissioned original song (PETRONAS 2026 "Seindah Kasih") that becomes the campaign's audio asset, mixed with dialogue.
- **Compliance:** cultural accuracy per festival (localisation.md); no religious ritual as a product prop.
- **Preset:** `feelgood-emotional` with the overrides `{"structure":{"target_s":[15,30]},"pacing":{"max_shot_s":4},"end_card":{"dur_s":4},"hook_text":{"enabled":false}}`, plus a persistent logo (brand `edit-brand` block).

---

## 3. Founder / comeback / inspirational (§11), corrected card

### What changed and why
- **The old card describes a cinematic documentary arc:** desaturated past → warm present, 2-4 s shots, a grind montage.
  - **Every high-engagement founder reel I could measure is talk-led instead (C1 11k likes, C2 2.4k likes):**
    - a podcast, stage or interview clip;
    - 4-10 s average shots (C1 4.5 s, C2 9.9 s, C3 6.7 s, C4 8.8 s);
    - the first word at 0.0 s;
    - 150-235 wpm (fast, often sped up);
    - a big header for the first ~7 s;
    - framing changes (close ↔ wide-with-audience, or a 2-up stack) instead of B-roll montages.
  - The cinematic arc is still the right grammar for a **produced founder ad film**. It is unmeasured here (no downloadable example), so it stays [researched].
- **The winning content is ONE specific scene, not the whole life story.**
  - C1 doesn't summarise Spanx's rise; she re-enacts one 15-minute meeting with dialogue ("Can I have 15 minutes?", "come with me to the bathroom").
  - The DSC ad is one take, one rant, one product truth.
  - A "from bedroom to millions" summary (C3, C4) gets low engagement.
- **The header carries the claim:** "THE MOMENT SARA BLAKELY REVOLUTIONIZED CLOTHING". The founder doesn't have to say it.
- **The old card's "grade progression sat 0.6 → 1.05"** is untested and the engine can't do it today. It stays a `_needs_feature` for 11b only.

### 11. Founder / comeback (two modes) [measured: C1 https://www.instagram.com/reel/DC47FDWxlpv/, C2 https://www.instagram.com/reel/DRnBLsXDQE-/, C3 https://www.instagram.com/reel/DehjfyxRDu2/; researched: Dollar Shave Club 2012 https://echai.ventures/videos/dollar-shave-club-dollarshaveclub-com-our-blades-are-f-ing-great]
- **Why it works:**
  - a real person retelling one scene where it could have gone wrong, in their own words and with the specific details only they know;
  - the viewer gets the founder's nerve rather than a CV.
  - A header frames the stakes; the payoff is a line of dialogue.
- **Modes:**
  - **11a Founder clip** (default, organic + Thought-Leader/Spark ads): a podcast, stage, interview or walk-and-talk;
  - **11b Founder film** (produced ad): the cinematic arc from the old card, used when there's budget and real archive.
- **Pacing map 11a (45-80 s):**

| Beat | Time | Shot | What |
|---|---|---|---|
| Header + cold start | 0-7 s | close-up, words from frame 0 | the header states the stakes ("The moment…" / "I had $800 and a desk"); the founder is mid-sentence in the scene |
| Set the scene | 7-20 s | alternate close ↔ wide every 3-5 s | where, who, what was at risk; one concrete number or object |
| The ask / the risk | 20-45 s | close-ups, punch-in on the key line | the dialogue of the moment, quoted ("I said…", "she said…") |
| The turn | 45-60 s | a reaction wide (the audience or the interviewer) | the line that changed everything, then a beat |
| Payoff + lesson | last 10-15 s | a close-up hold | one-sentence lesson; the brand appears only as the result, no hard CTA in organic |

- **Pacing 11b (30-60 s film):**
  - 0-3 s: the lowest moment, or archival proof;
  - 3-15 s: the wound in archive or recreation;
  - 15-30 s: the decision, then the grind;
  - 30-45 s: proof;
  - then the invitation.
  - Shots 2-4 s (unmeasured).
- **Shot grammar 11a:**
  - two cameras, a 50-85 mm close-up and a wide that includes the host or audience;
  - punch-in (×1.15-1.3) for the key line;
  - an optional 2-up stack (close-up on top, wide below) for podcast clips;
  - B-roll only for real proof (the first product, the garage, the receipt), never stock.
- **Shot grammar 11b:** past = static and archival; present = steady tracking and low-angle hero.
- **Look 11a:**
  - the real room (office, stage, warehouse) with natural or practical light;
  - no heavy grade (contrast 1.0-1.05).
  - Cybertize: shoot in the founder's own workspace; a studio set reads as "production".
- **genre_key (11a, for generated inserts only):** `real founder workspace, natural practical light, documentary two-camera interview coverage, candid unpolished moment, honest texture, no stock-footage gloss`
- **genre_key (11b):** `documentary-style cinematic realism, archival texture for the past, natural light, intimate framing, earned optimism, no stock-footage gloss`
- **Shot (11a):** `{"id":"S03","dur":4,"camera":"85mm close-up, punch-in to 1.2 on the quoted line","subject":"@FOUNDER","action":"start: leans in -> end: delivers 'Can I have fifteen minutes?' to camera-left","light":"soft practical key, real office behind","audio":"clean lav, room tone; no music under the quote","genre_key":"<11a key>"}`
- **Sound 11a:**
  - the voice is everything (enhance first);
  - the music bed is low or absent (C1, C2 have none: LRA 2.9 = speech only);
  - one soft riser or swell into the turn line at most;
  - audience laughter or reaction kept live.
- **Sound 11b:** a build-up score, with silence becoming the swell (old card, unchanged).
- **Compliance:**
  - every number must be substantiable (revenue, customers, "first in SG");
  - no humble-brag "overnight" myths;
  - in SG health the founder speaks about their own journey, never patient outcomes;
  - speeding up speech is fine but never changes words; keep the original as version A.
- **Presets:**
  - 11a `founder-clip` (new, below);
  - 11b `founder-inspire` (corrected, below);
  - dense-SFX documentary retellings stay `story-sfx-dense`.

### Preset: `founder-clip` (new, = 11a)
```json
{
  "name": "founder-clip",
  "label": "Founder clip: one scene, talk-led (11a)",
  "kind": "genre",
  "description": "Measured on Sara Blakely @hellosunshine (11k likes; 4.5 s avg shot, close<->wide-with-audience every 3-5 s, 7 s CAPS header, small sentence subs) and Ben Francis @benfrancis (2.4k likes; 234 wpm, 2-line captions with a yellow keyword, 2-up close/wide stack). Words from frame 0, header carries the stakes, no music under speech, punch-in on the quoted line, proof B-roll only.",
  "reference": "research/genre-research-2026-10/action-feelgood-founder.md#3",
  "structure": {"name": "founder-scene", "target_s": [40, 80], "beats": ["header + cold start mid-scene", "set the scene", "the ask / the risk (quoted dialogue)", "the turn (reaction wide)", "lesson line"]},
  "pacing": {"remove_silence_over_s": 0.3, "pad_s": 0.06, "remove_fillers": "hard", "max_shot_s": 6.0, "drop_retakes": true},
  "captions": {"enabled": true, "font": "Poppins", "bold": true, "size": 0.034, "color": "#FFFFFF", "highlight": "#FFE14D", "outline": 2, "shadow": 1, "position_y": 0.72, "max_words": 6, "animation": "fade", "uppercase": false, "keyword_caps": false},
  "hook_text": {"enabled": true, "font": "Poppins", "bold": true, "uppercase": true, "size": 0.05, "position_y": 0.42, "max_words": 7, "dur_s": 7.0, "outline": 0},
  "zoom": {"mode": "snap", "every_s": 4.0, "scale": 1.15, "on_hook": 1.0, "on_emphasis": true},
  "broll": {"every_s": 12, "max_dur_s": 2.5, "min_dur_s": 1.2, "mode": "full"},
  "sfx": {"density_per_10s": 0.2, "db": -20, "map": {"hook": "swell"}},
  "music": {"energy": "low", "db": -30, "duck": true},
  "grade": {"contrast": 1.03, "saturation": 1.0, "warmth": 0.02, "vignette": false},
  "end_card": {"enabled": false},
  "framing": {"plan": "per_sentence", "cycle": ["close", "wide"], "min_hold_s": 3.0, "_needs_feature": "sentence-aligned framing plan (same as premium-moving-talking-head B.3 #3); zoom snap every 4 s approximates it"},
  "layout": {"stack2": {"top": "close", "bottom": "wide"}, "_needs_feature": "speaker-only 2-up stack from two camera angles (broll mode split puts B-roll top, speaker bottom)"},
  "speed": {"talk_speedup": 1.1, "_needs_feature": "global speech speed-up with pitch kept (expand has --speeds; base render does not)"}
}
```

### Preset: `founder-inspire` (corrected, = 11b produced film)
```json
{
  "name": "founder-inspire",
  "label": "Founder film / comeback (11b, produced arc)",
  "kind": "genre",
  "description": "Produced founder ad film: archival/recreated past -> decision -> grind -> proof -> invitation. VO in the founder's real voice, build-up score, proof B-roll. Unmeasured (researched); for organic founder content use founder-clip.",
  "reference": "research/genre-research-2026-10/action-feelgood-founder.md#3",
  "structure": {"name": "founder-arc", "target_s": [30, 60], "beats": ["lowest moment / archival proof 0-3s", "wound", "decision + grind", "proof", "invitation"]},
  "pacing": {"remove_silence_over_s": 0.5, "pad_s": 0.12, "max_shot_s": 4.0},
  "captions": {"enabled": true, "font": "Space Grotesk", "bold": false, "size": 0.032, "max_words": 5, "animation": "fade", "keyword_caps": false, "outline": 0, "shadow": 2},
  "hook_text": {"enabled": true, "font": "Instrument Serif", "bold": false, "uppercase": false, "size": 0.05, "dur_s": 3.0},
  "zoom": {"mode": "smooth", "every_s": 5, "scale": 1.05},
  "broll": {"every_s": 3, "max_dur_s": 3, "min_dur_s": 1.2, "mode": "full"},
  "sfx": {"density_per_10s": 0.5, "db": -18, "map": {"hook": "riser", "end": "swell"}},
  "music": {"energy": "mid", "db": -19, "duck": true},
  "grade": {"contrast": 1.04, "saturation": 0.95},
  "end_card": {"enabled": true, "dur_s": 2.0},
  "grade_progression": {"from": {"saturation": 0.6, "contrast": 0.95}, "to": {"saturation": 1.05, "contrast": 1.06}, "by": "beat", "_needs_feature": "per-beat grade override (grade is global today)"}
}
```

### 3 core rules (founder)
1. **Tell one scene, not the whole journey.** Name the room, the person, the sentence said and the number at stake. Summaries ("from my bedroom to millions") underperform.
2. **Words from frame 0, with a header that carries the stakes for ~7 s.** The founder never has to say "this is my story".
3. **Real voice, real room, no music under the quote.** Change framing (close ↔ wide, punch-in) instead of laying stock B-roll. B-roll appears only as proof.

### Flags for Klaus (founder)
- I'm proposing to split 11 into 11a (clip, measured) and 11b (film, unmeasured). Klaus's own TITAN.AI and Physio Spot founder content would mostly be 11a.
- C2's 234 wpm looks sped up (~1.15-1.2×). Does Klaus want a default speed-up on his own talking clips?
- The founder-led performance stats (2.7× CTR etc.) come from an agency blog. Use them as a hunch, not as evidence.
- No high-engagement Asian or SG founder reel was measured. Ask Klaus for 2-3 SG founder references (e.g. local podcast clips) to localise.
- C1 measured 218 wpm (addendum). Fast delivery is normal for this format, not a defect.

---

## 4. Proposed new ad formats (cards for Klaus to approve)

### N1. "The question" sport/brand anthem (from A2)
- **Structure:** a provocative question repeated as a refrain ("Am I a bad person?") over a list of "flaws" that turn out to be the virtues of a champion. The answer is the brand line.
- **Works for any brand with a stance:** Power Protein ("Am I obsessive?"), TITAN.AI ("Is it cheating to use AI?").
- **Pacing:** the `sport-anthem` acceleration.
- **Rule:** the refrain returns every 8-12 s, and each return comes after a faster section.
- **Compliance:** the "flaws" must not mock the audience.

### N2. Event recap hype (from A3)
For brand community events (Gymshark Conditioning Club; Physio Spot run clinic; Power Protein gym takeover).
- **Grammar:**
  - low wide handheld in the crowd;
  - 2-up stacks;
  - a typewriter-mono line per section ("for those that choose…", "we do gym.");
  - the group photo as the final shot;
  - the logo on black.
- **Pace:** accelerate 1.0 → 0.45 s.
- **Preset:** `action-hype` with captions enabled in a mono font (needs the font).

### N3. Quiet-hero cutdown for SG health
Feel-good 9a staged around a physio's small repeated act, e.g. a physio staying late to adjust a kid's football boots (staff, not a patient outcome).
- 30 s cutdown;
- the reveal hold on the kid playing (no claim);
- the wisdom line, then the clinic.
- **SG-compliant by design:** no testimonial, no outcome promise.

---

## 5. Addendum: late whisper results (finished before hand-off)

| id | words | wpm while speaking | first word | RMS dB by decile (start → end) | reading |
|---|---|---|---|---|---|
| A2 Nike WIFE | 123 | **86** | 0.53 s | -28.6, -26.0, -24.4, -20.1, -19.0, -18.4, -18.4, -23.8, -18.3, -18.9 | confirms the sparse-VO anthem (≤ 100 wpm) and the **+10 dB build** with one dip before the final section (the `music_arc` + quiet-beat rule) |
| C1 Sara Blakely | 273 | **218** | 0.0 s | -29.5 … -18.7 (peak at decile 6 = the bathroom moment, laughter) … -29.2 | stage storytelling is fast. The loudest moment is the audience reaction at the turn, which supports "keep the reaction live" |
| F3 PETRONAS Once More | 22 | 72 | 0.0 s | rises to -15.2 at decile 8, then the title card drops to -28 | song-led cutdown; the music peaks just before the title card |

All three founder clips with real engagement sit at 150-235 wpm with zero lead-in silence. Both anthems and the quiet-hero film sit at 50-90 wpm. Speech rate is the clearest single dial between the founder and anthem/feel-good grammars.
