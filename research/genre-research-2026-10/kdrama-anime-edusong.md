# Genre research 2026-10: K-drama (§17), Anime-inspired (§18), Edu-song / mnemonic (§29)

Overnight run, 2026-10-25. Scope: ground, correct and extend three [draft] cards in
`.claude/skills/higgsfield-creative-director/references/genre-playbooks.md`. Nothing in the playbook, the presets or any other repo file was edited. Klaus decides what moves over.

## Method and caveats
- **Search:** WebSearch for context and figures. firecrawl_search was used 6 times, only to find public Instagram reel URLs. Exa was not used (no credits).
- **Downloads:** public Instagram reels only, via yt-dlp. There was one retry after 20 s on a 429: C064YKqLshP and DYXvT8iNLjg needed it, and both then downloaded. No YouTube, TikTok or Vimeo downloads, no cookies, no workarounds. Media and scripts stay in `scratchpad/genreG/` (never in the repo).
- **Measures:** every measure is capped at the first 120 s.
  - **Cuts:** `scale=320:-2,select='gt(scene,0.2)',showinfo`, merging cuts that fall within 150 ms of each other.
    - Several reposts sit on a **white** letterbox, which cropdetect misses; the first pass found only 4 cuts in a 2-s-cut ad. I re-ran those reposts with a crop to the moving picture band (`recut.py`).
    - Animation that changes inside one camera take (a phone filming a screen) does not count as a cut. For those reels I report the frame-sheet changes instead.
  - **Loudness:** EBU R128 (`ebur128`). Most reels read -14.1 LUFS, which is Instagram's normalisation, not the original mix.
  - **Onsets:** spectral flux. **BPM** is an autocorrelation of the onset envelope (70-180 BPM window). It is rough: it can land on half or double time, so I note when that is likely.
  - **Words/min:** faster-whisper small int8 on CPU. Korean wpm counts space-separated words (eojeol), so it is not comparable with English wpm. Whisper fails on dense sung Latin anatomy terms (E2), so I give no wpm there.
  - **Syllables:** an English vowel-group count over the transcript. Syllables per beat = syllables / (sung span × BPM / 60).
  - **Flash frames:** a jump of more than 40 luma that lasts 5 frames or fewer at 30 fps (`flash.py`).
  - **Frame sheets** at 1 fps were viewed for every reel cited below as measured.
- **Engagement:** like counts are the repost's own, not the original film's. "Likes 3" next to hundreds of comments means the likes are hidden.

---

## 0. Measured reference table

| id | what | URL (date, account) | reported performance | dur s | cuts | avg / median shot s (p90, max) | by third (s) | other measures |
|---|---|---|---|---|---|---|---|---|
| K1 | Wacky Willy (KR fashion) "rejection" ad, Go Kyung-pyo + Kang Hye-won, repost with a white header "The reason why I'm traumatized about approaching women:" | https://www.instagram.com/reel/DSRr7PTkc3E/ (2025-12-15, @korea.replay) | 4,050 likes, 34 comments; a Korean marketing blog calls it self-deprecating "B-grade" humour (https://letter.wepick.kr/post/1648) | 79.5 | 32 | 2.41 / **1.97** (5.0, 5.8) | 2.2 → 2.2 → 2.4 | ~64 Korean words/min with long pauses; a silence gag at 10-20 % (decile RMS -43.6 dB); bilingual subs (KR + EN) small at the bottom; three escalating rejections (rule of three) → the final umbrella-in-autumn-rain scene played straight romantic → a twist (grandma's memorial rite) → he walks off alone |
| K2 | same ad, the 49 s cut ("Rejection at the highest level") | https://www.instagram.com/reel/DTuIUuuiNF9/ (2026-01-20, @_aj_valentine_) | 1,438 likes | 49.0 | 26 | 1.81 / **1.53** (3.0, 5.3) | 1.5 → 1.8 → 1.8 | 59 Korean words/min; first word 0.5 s; holds of 3-5 s only on the umbrella beat |
| K3 | National Geographic Apparel (KR), Heo Nam-jun + Go Youn-jung: a car confession, she jumps out and runs | https://www.instagram.com/reel/Ddo6qjHg2Fh/ (2026-09-23, @thv.djyjmj fan repost) | likes hidden; covered by Sports Khan 2026-09-23 (https://sports.khan.co.kr/en/article/202609231145007) | 24.9 | 7 | 3.11 / **3.33** (4.6, 5.7) | 2.8 → 2.1 → 2.8 | **LRA 13.0** (a near-silent confession, then a scream/run); night, low-key tungsten + car-dash light, the product (a fleece jacket) worn in every shot |
| K4 | Compose Coffee × V (BTS) "That Night, Our Decaf" short-film ad, **fan edit** | https://www.instagram.com/reel/DW8SWRzjaRM/ (2026-04-10, @kitto_.editz) | 1,187 likes; the official ad passed 1 M YouTube views in one day (https://sportskeeda.com/pop-culture/news-the-main-character-you-fans-awe-taehyung-s-influence-compose-coffee-s-ad-youtube-surpassed-1m-views-just-one-day) | 28.2 | 36 | 0.76 / **0.63** (1.4, 2.3) | 1.0 → 0.63 → 0.63 | **cuts on onset 0.47** (beat-synced); no dialogue; a persistent header "POV: you meet your high school love after years 🥹✨"; soft cream/blue grade, school-uniform flashbacks, a teddy-keyring prop motif, store-front open and close |
| K5 | "No one does placement ads like K-dramas" (Kopiko PPL commentary) | https://www.instagram.com/reel/DYXvT8iNLjg/ (2026-05-15, @oluwaseyiclassic) | **1,834 comments** (likes hidden) | 73.1 | 2 | one 55 s take | – | 170 wpm talking head; "I'm going to count down and you say the name… Kopiko" → comment bait; the trope is "the friend hands over the product out of nowhere" |
| A1 | Nissin Cisco "Gorogura" granola TV CM (animated by coalowl, aired 2025-03-08), anime-OP meme song | https://www.instagram.com/reel/DayFKseMzpH/ (2026-07-14, @japan_ad_archive) | 2,603 likes; the meme OP it parodies ("Shikairo Days", My Deer Friend Nokotan) got 14 M+ views in 2 weeks (https://knowyourmeme.com/memes/shikanoko-nokonoko-koshitantan-opening-edits) | 30.1 | 38 | 0.77 / **0.53** (p10 0.17, max 4.5) | **0.53 → 0.84 → 1.0** (slows into the packshot) | ~91 BPM; LRA 2.7; **0 flash frames**; flat hand-drawn 2D girls on solid pastel fields; a big chanted katakana label on every shot (ごろグラ ごろごろ / 具がでっかい!); one stat card ("約9割 YES" pie); packshot + logo for the last ~4 s |
| A2 | "Anime Openings Be Like" trope-list parody | https://www.instagram.com/reel/C064YKqLshP/ (2023-12-16, @dude.dans_) | **513,548 likes, 2,461 comments** | 20.8 | 12 | 1.60 / **1.53** (max 3.3) | 1.4 → 1.0 → 2.3 | -12.2 LUFS; a Japanese OP-style song under the whole thing; **a white label box per shot naming the trope** ("Main Character Falling…", "Serious Face", "Insanely Complex Fight Scene", "Unrelated Cute Scene", "Running…", "Waifu Defies the Laws of Physics"); the creator's stick-figure mascot is dropped into lush anime-style plates; 0 flashes; ends on a sunset hold |
| A3 | "If DNF Duel had an anime opening" (real OP craft, control for grammar) | https://www.instagram.com/reel/CflwSqeDh_z/ (2022-07-04, @otg33k) | 4 likes (craft reference, not a performer) | 90.4 | 204 | **0.44 / 0.27** (p10 0.17, max 5.9) | 0.54 → 0.35 → 0.46 | **-7.8 LUFS** (brick-walled J-rock); **10 flash frames in 90 s, mostly in pairs** (10.03/10.43, 22.33/22.50, 62.33/63.07); a quiet dark credit intro 0-6 s → the title-logo card at ~26-30 s → character intros with staff-credit text → a full-speed fight montage |
| A4 | One Punch Man live-action fan concept trailer (control) | https://www.instagram.com/reel/Dc9MHZLkfeC/ (2026-09-06, @fandomtopicsofficial) | 238 likes (low) | 120 cap | 22 | 5.22 / 4.84 | 3.3 → 6.7 → 5.7 | trailer pacing with no anime grammar, and it underperforms; also named IP, so it's a "don't" |
| E1 | AsapSCIENCE mitosis song (creator parody), a teacher filming her monitor | https://www.instagram.com/reel/C6LnMbiiLuT/ (2024-04-25, @biologywitholivia) | **302,311 likes, 761 comments** | 42.8 | 17 (+ animation changes ~every 1-2 s) | 2.38 / 1.73 | 1.4 → 2.4 → 3.6 | **singing from 0.0 s, no spoken hook**; header "If you study biology and you don't know this song you're missing out on a treat" for ~11 s, then **a persistent step label** ("Mitosis 1. Prophase" → "2. Metaphase" → "3. Anaphase" → "4. Telophase then cytokinesis" → "2 genetically identical daughter cells"); ~92 BPM; 141 wpm; **3.4 syll/s ≈ 2.2 syllables per beat**; -14.7 LUFS |
| E2 | studysongz "Skeletal Bones Re-Mix" (original song, sold on study-songz.com) | https://www.instagram.com/reel/C3J3vLDuHKo/ (2024-02-10, @studysongz) | **141,766 likes, 708 comments** | 32.4 | 1 | one 3D-animation take | – | ~130 BPM; -11.1 LUFS, LRA 1.8 (a dense, loud song mix); **a dancing 3D skeleton; the named bone flies in enlarged and colour-tinted on the line that names it**; spotlights on black ↔ a white bubble background per verse; a constant small title "Skeletal Bones Re-Mix"; CTA in the caption "Send this to someone who has bones" |
| E3 | SimpleNursing cardio-pulmonary rap (original) | https://www.instagram.com/reel/DImv5FFt773/ (2025-04-18, @simplenursing.com_) | **51,455 likes**, 92 comments | 59.0 | 0 | one phone take of a laptop playing the animated diagram | – | header "PSA: this is how you get As in nursing school"; rap at 136 wpm, **3.2 syll/s** (≈ 2.6 syllables per beat at ~75 BPM half-time, i.e. 150 BPM double-time feel); the animated heart/lung diagram labels each structure as it is rapped; mnemonic metaphors ("pull it back like a slingshot… that's preload"); -14.2 LUFS |
| E4 | Tarsal-bones song | https://www.instagram.com/reel/DeXXrE9PV2Y/ (2026-10-11, @my.anatomy.teacher) | 714 likes | 19.2 | 0 | one take | – | ~98 BPM; **3.0 syll/s**; 7 names in 19 s, ending on the count line "These are the tarsal bones, seven bones total" |
| E5 | kids' science song controls: MRS GREN (https://www.instagram.com/reel/DUdsT_hgZEs/, 2026-02-07, 4 likes), Water Cycle (https://www.instagram.com/reel/Denvh2gCKae/, 2026-10-18, 3 likes), Planet Song (https://www.instagram.com/reel/DWedzSdDZ87/, 2026-03-29, 34 likes) | – | all low | 118 / 35.5 / 21.5 | 47 / 6 / 0 | 2.46/1.78 · 5.08/5.03 · one shot | – | **1.1-2.0 syll/s (≈ 0.6-1.9 per beat)**; the Water Cycle's first word comes at 4.6 s (an instrumental intro); kids-TV 3D cartoon look; nothing for an adult to save |

Researched, not measured (no public IG reel, or YouTube/TikTok only):
- **K-drama brand series:**
  - Colgate Optic White Purple, "The Purple Café" (June 2026): a 6-part TikTok K-drama series across TH/PH/MY, led by influencers. The product is a character, and viewers "one-up" AI-generated antagonists. No views were published. Sources: https://www.contentgrip.com/colgate-purple-cafe-campaign/ , https://www.marketing-interactive.com/colgate-turns-toothpaste-into-a-k-drama-plot-twist
  - The Venti × Park Ji-hoon: 15 M combined YouTube + IG views, a brand-reported figure (https://sports.khan.co.kr/en/article/202610082311007, 2026-10-08).
  - Marithé François Girbaud × Go Youn-jung / Cha Eun-woo: 1.9 M views (https://www.sportskeeda.com/us/shows/the-chemistry-chemistrying-fans-cheer-go-youn-jung-cha-eun-woo-s-marithe-commercial-goes-mega-viral-garnering-1-9m-views).
  - TikTok-native K-drama "In The Name Of Beauty": 300 M views in 12 days (https://sbsstar.net/article/N1008699988/shortform-kdrama-in-the-name-of-beauty-surpasses-300-million-views-on-tiktok).
- **K-drama PPL research:** small and qualitative. Fan "fanaticism raises purchase intention, more for hedonic products" (https://journal.untar.ac.id/index.php/jmieb/article/view/7717/5195). Placement aids recognition (https://burjcdigital.urjc.es/handle/10115/35559). No sales numbers.
- **Anime collabs:**
  - Popeyes × One Piece (April 2026, timed to AnimeCons): https://www.ypulse.com/newsfeed/2026/04/14/popeyes-is-launching-a-collaboration-with-one-piece/
  - Adidas commissioning **independently made anime-style imagery instead of licensing Japanese IP** (Animenomics, May 2026): https://bsky.app/profile/animenomics.com/post/3mksff33bts2y
  - Nissin's meme-parody CM habit, with another Nissin parody at 2.8 M YouTube views: https://automaton-media.com/en/news/20230725-20270/
  - The "me and the gang if we were in an anime" format: 776 K likes, and a follow-up at 10.6 M views in 5 days (https://amp.knowyourmeme.com/memes/people/playboianto-me-and-the-gang-if-we-were-in-an-anime).
  - AI "world leaders as an anime OP" (Shiro AI) reels circulate widely, but they use real-person likeness, so they are a hard-line "don't" for us.
- **Edu-song / PSA:**
  - **Metro Trains "Dumb Ways to Die"** (McCann Melbourne, 2012): an **original** song by members of The Cat Empire and Tinpan Orange. 5 Cannes Grand Prix (2013), 50 M YouTube views by mid-2013, 200+ covers and parodies, and charted in 28 countries. A "21 % fewer accidents" claim is company-reported. Sources: https://www.warc.com/content/article/cannes/metro-trains-dumb-ways-to-die/en-gb/101929 , https://mumbrella.com.au/?p=161258 , https://www.smartcompany.com.au/marketing/metro-s-dumb-ways-to-die-campaign-awarded-at-cannes-advertising-festival/
  - **"Ghen Cô Vy"** (Vietnam NIOEH, 2020-02-23): composer Khắc Hưng **re-lyricised his own hit "Ghen"** with the original singers. It became a TikTok hand-wash dance (Quang Đăng), which UNICEF joined. Re-lyricising was clean because the rights holder did it. Sources: https://en.wikipedia.org/wiki/Ghen_C%C3%B4_Vy , https://www.cbsnews.com/amp/news/coronavirus-prevention-vietnam-song-ghen-co-vy-tik-tok-challenge-about-washing-hands-quang-dang-john-oliver
  - "The Antibody Song" (Raven Baxter, 2021): taught immunology to ~3 M listeners, but on a Megan Thee Stallion melody, so creator-only (https://news.uci.edu/2021/06/22/these-videos-could-boost-covid-vaccination-rates).
  - AsapSCIENCE: 10.8 M subscribers; "Lab Rules" (Dua Lipa parody) 17 M+ views (https://en.wikipedia.org/wiki/AsapScience). These are creator parodies on copyrighted melodies, so they are **not** a brand template.
- **Memory science:**
  - Wallace 1994, J. Exp. Psych. LMC 20:1471-85: an easily learned, repeated melody improves text recall. Secondary sources only, e.g. https://scholarlycommons.pacific.edu/researchday/2015/events/13
  - Purnell-Webb & Speelman 2008: rhythm alone also helps, and familiarity helps more (https://ro.ecu.edu.au/ecuworks/1212).
  - The Ms Rachel "pause for response" is ~3 s of silent, smiling wait time. The evidence is clinical practice, not a controlled study of the show (https://screenwiseapp.com/media/miss-rachel-youtube).

---

## 3 core rules (one line each per module)
- **K-drama:**
  1. In 2025-26 brand ads K-drama is a **rom-com subversion**: play the romance grammar dead straight (umbrella, rain, held look, OST), then puncture it with a rejection, a twist or a PPL gag. Brands buy self-deprecation, not swooning.
  2. Cut at 1.5-2 s and save the 3-5 s holds for the one romantic beat. Holding every shot is wrong.
  3. The product is worn or held in-scene the whole time (PPL logic), and the logo comes only at the end.
- **Anime:**
  1. Reels that win are **anime-OP grammar used as a joke or a jingle**: trope labels per shot (A2) or a chanted label per shot (A1). They are not straight action pastiches (A4 flopped).
  2. Real OP cadence is 0.27 s median with paired white flashes every ~10-12 s and a title card at ~25-30 s. Reels borrow the energy but cut at 0.5-1.5 s and use **labels instead of flashes**.
  3. Original characters and an original or licensed song only. Commission original anime-style art (Adidas route), and never a named studio, series or real-person likeness.
- **Edu-song:**
  1. **The header is the hook and the song starts at 0.0 s.** The winners (E1-E3) open on a value-promise header ("If you study X and don't know this song…", "PSA: this is how you get As…"). There is no spoken intro and no count-in, while the kids' channels with instrumental intros flopped.
  2. **Adult study songs are dense:** 3.0-3.4 syllables/s (≈ 2-2.6 per beat at 90-100 BPM). Kids'-tempo songs (1-2 syll/s) read as "for toddlers" and don't get saved by adults. Use nursery-tempo tunes only for the do-along or comedy-clash format.
  3. **One diagram that changes on every line**, with the named part highlighted on the word that names it and a persistent step label. A one-take phone shot of a screen is enough; production polish didn't matter (E1 and E3 are phone-at-monitor).

---

### 17. K-drama [measured: K1 https://www.instagram.com/reel/DSRr7PTkc3E/ , K2 https://www.instagram.com/reel/DTuIUuuiNF9/ , K3 https://www.instagram.com/reel/Ddo6qjHg2Fh/ , K4 https://www.instagram.com/reel/DW8SWRzjaRM/ , K5 https://www.instagram.com/reel/DYXvT8iNLjg/ ; researched: Colgate "The Purple Café" (contentgrip.com), The Venti × Park Ji-hoon 15 M (sports.khan.co.kr 2026-10-08)]
- **What changed and why:**
  - Shots were "held looks of 3-5 s". Measured brand ads run at a **1.5-2.0 s median** (K1, K2) or 3.3 s (K3), with only the romantic beat held 4-6 s.
  - The look was "pastel, soft bloom". The 2025-26 ads are **warm golden autumn daylight or low-key tungsten night**, filmic and low-contrast; pastel is one option, not the default.
  - The structure gains a **subversion button**: every measured brand ad ends on a comic puncture, not a swoon.
- **Two modes:**
  - **17 Rom-com mini-film (brand)**: K1-K3. Sincere K-drama grammar, then a twist. Preset `kdrama-soft` (corrected).
  - **17a Fan-edit montage**: K4, see below.
- **Pacing map (30-45 s ad; 60-80 s film in brackets):**

| Beat | 30-45 s | Film | Shots |
|---|---|---|---|
| Hook header + setup | 0-3 s | 0-8 s | top header naming the premise ("Why I'm scared to talk to girls"); a wide of the lead hesitating; the product worn and visible |
| Attempt × 2-3 (rule of three) | 3-20 s | 8-45 s | shot-reverse-shot close-ups at 1.5-2 s; each attempt fails faster; a 1-2 s silence before each rejection line |
| The real K-drama moment | 20-30 s | 45-65 s | rain/umbrella or a car at night: a wide two-shot 4-6 s → CU → CU, a slow push-in, the OST enters, a held look of 3-5 s (the ONLY long holds) |
| Twist / button | 30-40 s | 65-75 s | one line breaks the spell (a phone call, she flees, the PPL product appears "out of nowhere"); hard cut, the music stops |
| Brand | last 3-4 s | last 4-5 s | logo card on a soft field, or the product in the final frame |

- **Shot grammar:**
  - two-shot → CU → CU for dialogue, eye-level, 50-85 mm, shallow depth of field;
  - an umbrella frame (two people under one umbrella, a wide from across the street) or a car interior (dash light on faces, K3);
  - a lingering back-of-head or over-the-shoulder shot before the confession;
  - one slow push-in (≤ 4 %) on the held look;
  - a macro "PPL insert" of the product in a hand: comic when it comes out of nowhere (K5 trope).
- **Look:**
  - warm low-contrast film: lifted blacks, golden-hour autumn trees or tungsten street lamps at night (K1, K3);
  - clean, bright, soft skin;
  - an optional pastel/cream variant for spring and morning scenes (K4);
  - never crushed or teal (that is horror/thriller).
- **genre_key:** `Korean drama cinematography, warm low-contrast film grade, soft golden-hour or tungsten street-lamp light, shallow depth of field, gentle slow push-in, rain and umbrella romance framing, clean luminous skin, quiet held glances`
- **Shot JSON (the real moment):** `{"id":"S9","dur":5,"camera":"wide two-shot across the street, 85mm, then locked; push-in 3% over the shot","subject":"@LEAD and @CRUSH under one clear umbrella, @LEAD wearing @PRODUCT jacket","action":"start: she looks up at him -> end: he holds her gaze, says nothing","environment":"autumn campus path, wet leaves, light rain","light":"soft overcast golden hour, warm","audio":"rain room tone, OST piano enters at 1.5 s","constraints":"adults 25+, no school uniforms, no real actor likeness","genre_key":"<17 key>"}`
- **Sound:**
  - room tone and **real silences** for the comedy (a K1 silence beat measured at -43 dB);
  - an OST-style piano/strings cue only under the real moment, cut dead on the twist;
  - no SFX except one comic sting or record-scratch on the button (optional);
  - original or licensed OST only (`/sound`).
- **Compliance:**
  - no real-actor lookalikes, ever (character-design.md);
  - romance = adults 25+; avoid school uniforms in romantic beats, and flashback "high school" scenes need cast who clearly read as adults or non-romantic staging (mature-edge.md hard lines);
  - PPL in organic posts still carries #ad / a paid-partnership label;
  - SG health brands: the twist may not be a treatment outcome, and the clinic appears as the setting or the staff, not as a cure.
- **Preset:** `kdrama-soft` (corrected):
```json
{
  "name": "kdrama-soft",
  "label": "K-drama rom-com mini-film (sincere grammar, comic button)",
  "kind": "genre",
  "description": "Measured on Wacky Willy 'rejection' ad (median 1.97 s, 1.53 s in the 49 s cut, holds 5-6 s only on the umbrella beat, real silences before each rejection line) and National Geographic Apparel KR (median 3.3 s, night tungsten, LRA 13: whisper confession then a scream). 1.5-2 s storytelling cuts, one held romantic beat with a slow push, small bilingual-style subtitles low in frame, a top premise header, warm low-contrast film grade, OST only under the real moment, a hard cut to the button and the logo.",
  "reference": "research/genre-research-2026-10/kdrama-anime-edusong.md#17",
  "structure": {
    "name": "kdrama-romcom",
    "target_s": [30, 80],
    "beats": ["premise header + setup", "attempt 1", "attempt 2", "attempt 3 (optional)", "the real moment (held)", "twist / button", "logo"]
  },
  "pacing": {"remove_silence_over_s": 1.6, "pad_s": 0.3, "remove_fillers": "light", "max_shot_s": 6.0, "keep_pause_before_punch_s": 1.2},
  "captions": {"enabled": true, "font": "Poppins", "bold": false, "size": 0.03, "max_words": 8, "animation": "fade", "uppercase": false, "keyword_caps": false, "outline": 0, "shadow": 2, "position_y": 0.86},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "persistent": true, "font": "Instrument Serif", "size": 0.032, "position_y": 0.12, "uppercase": false, "max_words": 12},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.03, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0.1, "db": -16, "map": {"end": "ding"}},
  "music": {"energy": "low", "db": -20, "duck": true},
  "grade": {"contrast": 0.92, "saturation": 0.92, "brightness": 0.02, "gamma": 1.03, "warmth": 0.05, "vignette": false},
  "transitions": {"default": "dip", "on": "beats", "dur_s": 0.35, "strength": 0.25},
  "end_card": {"enabled": true, "dur_s": 3.0},
  "reveal_hold": {"min_s": 3, "max_s": 6, "push_in": 1.03, "_needs_feature": "beat role 'moment' exempt from the median pace, gets the only push-in"},
  "music_arc": {"start_db": -30, "end_db": -18, "_needs_feature": "OST enters on the 'moment' beat and hard-stops on the 'button' beat (music.stop_at_beat exists only as a single stop)"}
}
```

### 17a. K-drama fan-edit montage (`kdrama-fan-edit`) [measured: K4 https://www.instagram.com/reel/DW8SWRzjaRM/]
- **Use:** a brand already has K-drama-style film footage (its own long ad or BTS) and wants a reel recut, or a creator account edits "POV" romance montages.
- **Pacing:**
  - median 0.63 s, max 2.3 s;
  - cuts on beat (47 % of cuts within 80 ms of an onset);
  - the opening store-front/meet shot is held ~1.5 s, then the montage of memories, then a return to the present and a last held look.
- **Text:** one persistent POV header ("POV: you meet your high school love after years 🥹✨"). No subtitles, no dialogue.
- **Look:** soft cream/blue-washed, slightly desaturated, flashbacks a touch brighter.
- **Sound:** one licensed song (an original OST for brands, a trending sound in-app for personal accounts), not ducked.
- **Compliance:** brands recut **their own** footage only, never another brand's ad or a drama's footage. Fans editing celebrity ads (K4) is fan culture, not something we copy. School-uniform flashbacks follow the adults-only rule above.
```json
{
  "name": "kdrama-fan-edit",
  "label": "K-drama POV fan-edit montage (beat-synced)",
  "kind": "style",
  "description": "Measured on a Compose Coffee x V ad fan edit: median shot 0.63 s, 47 % of cuts on a music onset, no dialogue, one persistent 'POV: ...' header with emoji, soft cream/blue grade, present -> flashback memories -> present held look. Music-led; recut of the brand's OWN K-drama-style film footage only.",
  "reference": "research/genre-research-2026-10/kdrama-anime-edusong.md#17a",
  "beat_sync": true,
  "pacing": {"remove_silence_over_s": 0.2, "pad_s": 0.0, "remove_fillers": "none", "max_shot_s": 1.4},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "outline", "persistent": true, "size": 0.032, "position_y": 0.1, "uppercase": false, "max_words": 12},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.02, "on_hook": 1.0},
  "broll": {"every_s": 0.7, "max_dur_s": 1.4, "min_dur_s": 0.4, "mode": "full"},
  "sfx": {"density_per_10s": 0},
  "music": {"energy": "medium", "db": -8, "duck": false},
  "grade": {"contrast": 0.94, "saturation": 0.86, "brightness": 0.03, "warmth": -0.02},
  "end_card": {"enabled": false}
}
```

### 17b. Self-aware PPL gag (`kdrama-soft`, button variant) [measured: K5 https://www.instagram.com/reel/DYXvT8iNLjg/ ; researched: K-drama PPL studies (journal.untar.ac.id; burjcdigital.urjc.es)]
- **Why:** viewers love spotting K-drama product placement. K5 drew 1,834 comments by asking viewers to shout the brand name ("3, 2, 1… Kopiko").
- **Use:** the brand **parodies its own placement**. In the big romantic moment a character hands over the product "out of nowhere", with a slow-mo close-up and a sparkle, while the other character stares at the camera. Use it as the 17 twist beat or as a 10-15 s standalone.
- **Rules:**
  - make the gag about our own brand only;
  - never mock a named competitor's placement;
  - SG health clinics avoid the "fixes everything" implication: the product can be a heat pack or a water bottle, not a cure.

---

### 18. Anime-inspired [measured: A1 https://www.instagram.com/reel/DayFKseMzpH/ , A2 https://www.instagram.com/reel/C064YKqLshP/ , A3 https://www.instagram.com/reel/CflwSqeDh_z/ (grammar control), A4 https://www.instagram.com/reel/Dc9MHZLkfeC/ (control); researched: Popeyes × One Piece (ypulse 2026-04-14), Adidas original anime-style art (Animenomics 2026-05)]
- **What changed and why:**
  - "Impact frames" are real OP craft: A3 has 10 two-to-five-frame flashes in 90 s, mostly in pairs. The reels that perform (A1 brand CM, A2 at 513 K likes) use **zero flashes**. Their energy comes from **a label on every shot** and a song that drives the cut.
  - Flashes become optional seasoning (≤ 1 pair per 10 s), not the default.
  - "Power-up holds 1-2 s" survive only as the last-shot hold (A1 packshot 4.5 s, A2 sunset ~3 s).
  - A straight live-action pastiche with trailer pacing (A4, 4.8 s median) underperformed. Keep it comedic or jingle-led.
- **Two modes:**
  - **18 Anime CM / jingle (brand)**: A1. Flat 2D original characters, a chanted label per shot, one stat card, packshot last.
  - **18a Anime-OP parody / trope list**: A2. See below.
- **Pacing map (30 s):**

| Beat | Time | Shots |
|---|---|---|
| Cold open | 0-1 s | a white/pastel field, the first chant word slams in, the character pops in |
| Chant verse | 1-12 s | 0.3-0.6 s cuts on the beat, each with ONE big label (the product's 2-4 sound/benefit words, repeated); character poses alternate with macro product-texture plates |
| Proof card | 12-16 s | one stat or fact card ("9 in 10 …" only if it is substantiated), pie or counter animating in, held ~2.5 s |
| Chorus / group shot | 16-25 s | all characters together, a sky or fruit-field background, the chant repeated; cuts slow to ~1 s |
| Packshot | last 4-5 s | product + logo held, the final chant line sung once |

- **Real-OP grammar (only when you need a full "anime opening", e.g. a brand-mascot OP; from A3):**
  - a dark, quiet credit intro of 4-6 s;
  - the title-logo card on the first chorus hit (~25-30 s of a 90 s OP);
  - character intros with name or credit text;
  - fight montage cuts at 0.17-0.3 s;
  - flash pairs on the chorus hits.
- **Shot grammar:**
  - extreme low angle for the hero pose;
  - a frontal "camera-bow" pose with hand gestures to the lens (A1);
  - a falling-through-sky shot and a running-at-sunset shot (the A2 tropes everyone recognises);
  - a split panel or manga frame for the reaction;
  - speed lines behind a static character for motion (cheap in AI).
- **Look:**
  - **flat hand-drawn 2D** on solid pastel fields (A1), or lush painted backgrounds with a simple mascot dropped in (A2);
  - saturated but not neon;
  - live action uses hard coloured gels plus a speed-line overlay.
- **genre_key:** `original anime-inspired 2D illustration, clean confident line art, flat cel shading, solid pastel background fields, dynamic low-angle hero pose, speed lines, saturated cheerful palette, Japanese TV commercial energy` (original characters only; never a named studio, series or artist)
- **Shot JSON (chant shot):** `{"id":"S3","dur":0.5,"camera":"locked frontal medium, slight low angle","subject":"@MASCOT_GIRL original character in brand-colour hoodie","action":"start: arms down -> end: both hands framing the product bowl, wink","environment":"solid pastel yellow field with the product bowl","light":"flat even cel light","audio":"chant word on the downbeat","constraints":"original character, no IP, label added in post","genre_key":"<18 key>"}`
- **Sound:**
  - **the song is the ad**: an original chant-style jingle of 2-4 words repeated, at 90-100 BPM (A1 ~91 BPM);
  - one impact or whoosh only on the title or packshot;
  - a licensed J-pop/anime OP only with written licence (Nissin's spot is an official tie-in parody of a hit OP; treat that as licensed, never as a precedent for using an OP freely).
- **Compliance:**
  - original characters and art (the Adidas route) or a properly licensed collab (the Popeyes × One Piece route);
  - no AI lookalikes of real people (the Shiro AI-style political OPs are out);
  - anime-style characters who could read as minors never appear in suggestive or romantic beats (mature-edge.md);
  - stat cards need a source (SG health: no superlatives, no outcome claims).
- **Preset:** `anime-energy` (corrected):
```json
{
  "name": "anime-energy",
  "label": "Anime CM / jingle (chant label per shot)",
  "kind": "genre",
  "description": "Measured on Nissin Cisco 'Gorogura' anime CM (median 0.53 s, slows 0.53 -> 0.84 -> 1.0 s into a 4.5 s packshot, a big chanted label on every shot, one stat card, 0 flash frames) with real-OP grammar from a DNF Duel OP (median 0.27 s, paired white flashes ~every 10-12 s, -7.8 LUFS) as an optional seasoning. Song-led, labels instead of subtitles, flat saturated grade.",
  "reference": "research/genre-research-2026-10/kdrama-anime-edusong.md#18",
  "beat_sync": true,
  "structure": {"name": "anime-cm", "target_s": [15, 30], "beats": ["cold open chant", "chant verse", "proof card", "chorus group shot", "packshot"]},
  "pacing": {"remove_silence_over_s": 0.25, "pad_s": 0.03, "remove_fillers": "aggressive", "max_shot_s": 1.2},
  "captions": {"enabled": false},
  "labels": {"style": "outline", "font": "Archivo Black", "size": 0.075, "position_y": 0.78, "uppercase": true, "_needs_feature": "labels.style/font/position per beat (beat 'label' exists; styling keys not yet)"},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "outline", "dur_s": 1.2, "position_y": 0.5, "size": 0.07, "uppercase": true, "max_words": 3},
  "zoom": {"mode": "snap", "every_s": 1.0, "scale": 1.12, "on_hook": 1.2},
  "broll": {"every_s": 0.6, "max_dur_s": 1.0, "min_dur_s": 0.3, "mode": "full"},
  "sfx": {"density_per_10s": 1.0, "db": -12, "map": {"hook": "impact", "title": "whoosh", "end": "impact"}, "min_gap_s": 3.0},
  "music": {"energy": "high", "db": -6, "duck": false},
  "grade": {"contrast": 1.08, "saturation": 1.22, "brightness": 0.03},
  "transitions": {"default": "flash", "on": "beats", "dur_s": 0.07, "strength": 0.8, "_needs_feature": "flash only on role 'title' and chorus hits, max 1 pair per 10 s (now fires on every beat change)"},
  "end_card": {"enabled": true, "dur_s": 4.0}
}
```

### 18a. Anime-OP parody / trope list (`anime-op-parody`) [measured: A2 https://www.instagram.com/reel/C064YKqLshP/ (513,548 likes)]
- **Use:** comedy on brand or personal accounts: "Physio appointments be like (anime opening)", "Every gym bro's anime opening", "Your lower back's anime OP".
- **Pacing:**
  - 15-25 s, median 1.5 s per trope;
  - a 1.4 s "<X> be like:" setup card, then 9-12 trope shots;
  - the last shot is a ~3 s hold (sunset, field, freeze).
- **The engine is a white label box per shot naming the trope** in plain English, top third. Each trope is one shot; the mascot or the creator is dropped into each scene.
- **Trope bank** (all public-domain clichés, no IP): falling through the sky · serious side-profile face with wind · "Their future love interest" · huge rival with a huge weapon · "insanely complex fight" · unrelated cute scene with petals · running for no reason · floating heroine "defying physics" · group pose on a hill · title card with fake katakana.
- **Physio version:** "Main character's knee clicks" · "Serious stretching face" · "The rival: Desk Chair" · "Training arc (2 reps)" · "Unrelated cute scene: the clinic cat". The comedy is the label; the clinical content stays true.
- **Sound:** an **original** J-rock-style OP pastiche (a Suno/original track with a commercial licence noted, or a commissioned one). A2 used an OP-style song: fine for a creator, not for a brand unless licensed.
```json
{
  "name": "anime-op-parody",
  "label": "Anime-OP parody / trope list (label per shot)",
  "kind": "style",
  "description": "Measured on 'Anime Openings Be Like' (513 K likes): 20.8 s, median 1.53 s, a '<X> be like:' setup card then one trope per shot, each with a white rounded label box naming the trope at the top, a creator mascot dropped into lush anime-style plates, OP-style song under the whole thing (-12 LUFS), no subtitles, no flash frames, last shot held ~3 s.",
  "reference": "research/genre-research-2026-10/kdrama-anime-edusong.md#18a",
  "beat_sync": true,
  "structure": {"name": "trope-list", "target_s": [15, 25], "beats": ["'<X> be like:' setup", "trope 1-10 (one shot each, labelled)", "final held tableau"]},
  "pacing": {"remove_silence_over_s": 0.3, "pad_s": 0.05, "remove_fillers": "none", "max_shot_s": 2.2},
  "captions": {"enabled": false},
  "labels": {"style": "box", "size": 0.034, "position_y": 0.2, "uppercase": false, "_needs_feature": "labels.style/font/position per beat (beat 'label' exists; styling keys not yet)"},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "dur_s": 1.4, "position_y": 0.2, "size": 0.036, "uppercase": false, "max_words": 6},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.04, "on_hook": 1.0},
  "broll": {"every_s": 1.5, "max_dur_s": 2.2, "min_dur_s": 0.8, "mode": "full"},
  "sfx": {"density_per_10s": 0.3, "db": -14, "map": {"title": "whoosh"}},
  "music": {"energy": "high", "db": -6, "duck": false},
  "grade": {"contrast": 1.04, "saturation": 1.15, "brightness": 0.03},
  "end_card": {"enabled": false}
}
```

---

### 29. Edu-song / mnemonic / musical explainer (`edu-song`) [measured: E1 https://www.instagram.com/reel/C6LnMbiiLuT/ , E2 https://www.instagram.com/reel/C3J3vLDuHKo/ , E3 https://www.instagram.com/reel/DImv5FFt773/ , E4 https://www.instagram.com/reel/DeXXrE9PV2Y/ ; controls E5 DUdsT_hgZEs, Denvh2gCKae, DWedzSdDZ87; researched: Dumb Ways to Die (warc.com), Ghen Cô Vy (wikipedia), Wallace 1994]
Full guide: edu-songs-mnemonics.md. Tool: `editor.py song`.
- **What changed and why:**
  - The old map opened with a **spoken hook (0-3 s) then a count-in (3-5 s)**. All three high performers (302 K, 142 K, 51 K likes) **start singing at 0.0 s** and put the hook in a **value-promise header** on screen. The low-performing kids' channels open on an instrumental intro (first word at 4.6 s). Drop the count-in from published cuts; keep it only on the guide track for recording.
  - "One syllable per note" is right for nursery re-lyrics, but **adult study songs run 3.0-3.4 syllables/s (≈ 2-2.6 per beat)**, rap-adjacent. The kids' controls sat at 1.1-2.0 syll/s and got no saves. Pick the density for the audience.
  - Winners are **one-take "proof" shots** (a phone filming a monitor or laptop, E1/E3) or one continuous 3D animation (E2). The "cut" happens inside the diagram: a new label or part on every line, ~every 1-2 s. Production polish did not predict performance.
  - The **step label** is persistent and changes per section (E1 "Mitosis 1. Prophase" → "2. Metaphase"), the visual twin of the chorus.
- **Formats now ranked by evidence:**
  1. **Study / mnemonic song** (measured winner): 20-60 s, dense lyric, a diagram per line.
  2. **Brand PSA original song** (researched winner: Dumb Ways to Die, Ghen Cô Vy): original melody, a character or dance, the safety message as the chorus.
  3. **Do-along routine** (physio): still a hypothesis, unmeasured. Test it against format 1.
- **Pacing map (30-45 s study song):**
  - 0 s: the song starts AND the header is on screen ("If you treat backs and don't know this song…", "PSA: how to remember the 4 rotator cuff muscles"), held 8-12 s;
  - 0-30 s: one fact per line; the diagram or animation changes on every line (1-2 s); the named part is highlighted as it's sung; a persistent step label per section;
  - last 5-10 s: the recap chorus or the count line ("Four muscles: that's your SITS"), with all labels on screen at once;
  - CTA in the caption, not in the video ("Send this to someone who has bones", E2; "save for your exam"). An end card is optional (≤ 1.5 s).
- **Shot grammar:**
  - **A (proof screen):** a phone at the monitor or laptop playing the animated diagram, a bit of desk visible, a slow handheld drift; header top, subtitle-style lyrics optional.
  - **B (3D mascot):** a dancing skeleton or mascot on black with spotlights; the named body part flies in enlarged and colour-tinted; the background changes per verse.
  - **C (host do-along):** locked frontal medium, the host mirrors the viewer; one gesture per line, the same gesture every time.
- **Look:**
  - A: whatever the screen shows, with high-contrast labels;
  - B: black with RGB spotlight cones ↔ a white bubble field;
  - C: bright high-key;
  - all: labels in one bold sans and one accent colour per section.
- **genre_key (B, 3D mascot):** `stylised 3D anatomical character dancing on a black stage under coloured spotlight cones, clean glossy materials, the highlighted body part enlarged and colour-tinted, crisp educational clarity, playful music-video energy`
- **Shot JSON (B, one lyric line):** `{"id":"L4","dur":1.6,"camera":"locked full-body, eye level","subject":"@SPINEY 3D skeleton mascot","action":"start: dancing -> end: points at the enlarged glowing @SUPRASPINATUS floating beside it","environment":"black stage, three coloured spotlight cones","light":"spot-lit, rim light","audio":"sung line 'supraspinatus lifts your arm'","constraints":"anatomy must be correct, label added in post","genre_key":"<29 key>"}`
- **Sound:**
  - the song is the mix: vocal over an original or public-domain backing, not ducked, at -11 to -14 LUFS (E2 -11.1, LRA 1.8);
  - **90-100 BPM** for study songs (E1 ~92, E4 ~98) or a half-time 130-150 BPM rap feel (E2, E3);
  - no SFX except a pop per label (optional);
  - no pop-song melodies on brand accounts (§5 copyright: E1 and the Antibody Song are creator parodies of copyrighted melodies, so they are creator-only patterns).
- **Compliance:**
  - every lyric is a clinical claim, so run the compliance pack line by line;
  - accuracy beats rhyme;
  - SG health: no outcomes, superlatives or testimonials;
  - stat or count lines must be true ("seven bones total").
- **Preset:** `edu-song` (corrected):
```json
{
  "name": "edu-song",
  "label": "Edu-song / study song / mnemonic (header hook, song from 0 s)",
  "kind": "style",
  "description": "Measured on AsapSCIENCE mitosis song repost (302 K likes), studysongz Skeletal Bones (142 K) and SimpleNursing cardio rap (51 K): singing starts at 0.0 s, the hook is a value-promise HEADER on screen ('If you study X and don't know this song...'), no spoken intro or count-in; 3.0-3.4 syllables/s at 90-100 BPM; one diagram change per lyric line (1-2 s) with the named part highlighted; a persistent step label per section; recap or count line last; CTA in the caption. Kids-tempo songs (1-2 syll/s, instrumental intros) flopped. Music = the original song mix, not ducked.",
  "reference": "research/genre-research-2026-10/kdrama-anime-edusong.md#29",
  "beat_sync": true,
  "structure": {"name": "study-song", "target_s": [20, 60], "beats": ["song + header (0 s)", "section 1 (label)", "section 2 (label)", "section 3 (label)", "recap / count line", "optional end card"]},
  "pacing": {"remove_silence_over_s": 0.6, "pad_s": 0.05, "remove_fillers": "none", "max_shot_s": 2.0},
  "captions": {"enabled": true, "size": 0.045, "max_words": 3, "animation": "karaoke", "uppercase": true, "highlight": "#FFD23F", "outline": 6, "position_y": 0.7, "emoji": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "persistent": false, "dur_s": 10.0, "position_y": 0.12, "size": 0.032, "uppercase": false, "max_words": 18},
  "labels": {"style": "box", "size": 0.034, "position_y": 0.12, "uppercase": false, "_needs_feature": "persistent per-section step label that replaces the header after it ends (beat 'label' shows only on its own clip)"},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.05, "on_hook": 1.0},
  "broll": {"every_s": 1.6, "max_dur_s": 2.0, "min_dur_s": 0.8, "mode": "full"},
  "sfx": {"density_per_10s": 0.6, "db": -16, "map": {"broll": "pop", "end": "ding"}, "min_gap_s": 1.2},
  "music": {"energy": "high", "db": -4, "duck": false},
  "grade": {"contrast": 1.06, "saturation": 1.12, "brightness": 0.02, "warmth": 0.02},
  "end_card": {"enabled": false, "dur_s": 1.5},
  "audio_qc": {"min_lufs": -15, "_needs_feature": "warn when the sung span is < 2.8 syll/s for an adult study song or > 2.2 for a do-along"}
}
```

### 29a. Proof-screen study song, one take (`edu-song-screen`) [measured: E1 https://www.instagram.com/reel/C6LnMbiiLuT/ , E3 https://www.instagram.com/reel/DImv5FFt773/ , E4 https://www.instagram.com/reel/DeXXrE9PV2Y/]
- **What it is:** the physio films a laptop or clinic monitor playing the brand's own animated diagram (tools/motion step-cards, or a Higgsfield explainer clip) while the original song plays. It's the cheapest winner in this set: one take, no on-camera talent.
- **Rules:**
  - header from frame 1 (value promise plus who it's for);
  - the step label changes per section;
  - no cuts (or one), 20-60 s;
  - the diagram must change on every line;
  - the song mix is loud and clear;
  - lyrics as small subtitles or none.
- **Physio seeds:**
  - "If you treat shoulders and don't know this song…" (SITS rotator cuff);
  - "PSA: the 3 ankle-sprain grades in 20 seconds";
  - "The 7 tarsal bones, sung" (anatomy for students: an audience-building pillar, not a patient pitch).
```json
{
  "name": "edu-song-screen",
  "label": "Proof-screen study song (one take of a screen + header)",
  "kind": "style",
  "description": "Measured on AsapSCIENCE mitosis repost (302 K likes: phone filming a monitor, header 'If you study biology and you don't know this song...' ~11 s, then a step label per phase) and SimpleNursing (51 K likes: one 59 s take of a laptop playing an animated heart diagram, header 'PSA: this is how you get As in nursing school', 136 wpm rap). One take, the cut lives inside the animation, header first, song from 0 s, CTA in the caption.",
  "reference": "research/genre-research-2026-10/kdrama-anime-edusong.md#29a",
  "structure": {"name": "proof-screen-song", "target_s": [20, 60], "beats": ["header + song", "sections (step label each)", "recap"]},
  "pacing": {"remove_silence_over_s": 99, "pad_s": 0.0, "remove_fillers": "none", "max_shot_s": 60},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "persistent": true, "position_y": 0.66, "size": 0.03, "uppercase": false, "max_words": 16},
  "zoom": {"mode": "drift", "every_s": 0, "wide": [1.02, 1.05]},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0},
  "music": {"energy": "high", "db": -4, "duck": false},
  "grade": {"contrast": 1.04, "saturation": 1.05},
  "end_card": {"enabled": false},
  "labels": {"style": "box", "position_y": 0.12, "_needs_feature": "per-section step label from lyrics.json section markers"}
}
```

### 29b. Brand PSA original song (`edu-song`, PSA variant) [researched: Dumb Ways to Die https://www.warc.com/content/article/cannes/metro-trains-dumb-ways-to-die/en-gb/101929 ; Ghen Cô Vy https://en.wikipedia.org/wiki/Ghen_C%C3%B4_Vy]
- **Why:** the biggest edu-song brand wins are **original songs with a recurring character set or a dance**, where the message is the chorus. Dumb Ways to Die: 5 Cannes Grand Prix, 50 M views in about 7 months, 200+ covers. Ghen Cô Vy: the composer re-lyricised his own hit, and it became a TikTok dance challenge.
- **Structure:** one cute character per verse doing a "dumb" thing (comedy), the chorus repeats the title phrase, and the message comes only in the last 10 s.
- **Rules:**
  - a fully original melody, or a re-lyric **by the rights holder**;
  - a dance or hand move simple enough to copy (the challenge mechanic);
  - the brand only on the end card.
- **Physio adaptation:** "Dumb ways to hurt your back" (lifting with a twist, phone neck, the weekend-warrior sprint). Run the compliance pack: no fear claims, and no "only we can fix it".
- **Status:** researched only. Draft it with `editor.py song --beat` plus an original melody, then test.

---

## Proposed §0 picker rows
| 17 | K-drama | rom-com mini-film, crush or confession, a romance played straight then punctured; PPL gags | tenderness → laugh | 1.5-2 s median; holds of 3-6 s only on the one romantic beat | premise header → attempts × 3 → the real moment (held) → twist → logo | warm low-contrast film, golden autumn or tungsten night (pastel optional) | real silences, OST only under the moment, hard stop on the twist | kdrama-soft (+ kdrama-fan-edit for beat-synced POV recuts of own footage) |
| 18 | Anime-inspired | a product jingle, mascot chant, "<X> be like" trope parody, hype | intensity, delight | 0.5 s (chant CM) to 1.5 s (trope list); real OP 0.27 s | chant verse → proof card → chorus → packshot held 4 s; or setup card → one trope per shot → held tableau | flat 2D cel on pastel fields, saturated | the song is the ad (original chant 90-100 BPM); flash pairs optional | anime-energy (+ anime-op-parody) |
| 29 | Edu-song / mnemonic / musical explainer | anatomy, steps, checklists, red flags; study content; PSA songs | "I can't unhear it", save-for-later | the diagram changes every 1-2 s inside one take | song + header at 0 s → labelled sections → recap/count line; CTA in the caption | whatever the screen shows, plus bold labels; 3D mascot on black | the original song, not ducked, -11 to -14 LUFS; adults 3.0-3.4 syll/s | edu-song (+ edu-song-screen) |

## Flags for Klaus
1. **The K-drama card's look was wrong for current ads.** Real 2025-26 Korean brand ads (Wacky Willy, NatGeo Apparel KR) are warm filmic rom-com *subversions*, not pastel swooning. Do you want a pastel variant kept as the default for "soft" briefs?
2. **Anime songs:** the Nissin CM parodies a hit anime OP and is, by all signs, licensed. Our brand anime spots need an original chant jingle (or a paid licence). For personal accounts, the trope-list parody can ride an in-app sound.
3. **The edu-song do-along format for physio is unproven.** Every measured winner is a dense study song for students or nurses, not a slow follow-along routine. I suggest an A/B: "SITS rotator cuff study song" (29a) vs "desk-stretch do-along" (29 format C), both original melodies.
4. **Engine gaps (`_needs_feature`):** a persistent per-section step label; labels styling; flash only on title/chorus hits; an OST that enters on a beat and hard-stops on another; a syllables/s QC warning.
5. **School-uniform romance:** fan edits like K4 use high-school flashbacks. Our hard line (adults 25+, nothing romantic that reads as minors) rules that framing out for generated characters. Use "college" or "first job" flashbacks instead.
6. **Measurement limits:** K-drama wpm is Korean eojeol; whisper could not transcribe E2's sung Latin; BPM is ±2× uncertain. White-letterbox reposts needed a manual re-crop, and the first-pass cut counts for K1/K2 (4 and 7 cuts) were wrong and are superseded by 32 and 26.

## Sources (all accessed 2026-10-25)
- Reels: K1-K5, A1-A4, E1-E5 as listed in table 0 (Instagram, dates and accounts there).
- https://www.contentgrip.com/colgate-purple-cafe-campaign/ · https://www.marketing-interactive.com/colgate-turns-toothpaste-into-a-k-drama-plot-twist · https://sports.khan.co.kr/en/article/202610082311007 · https://sports.khan.co.kr/en/article/202609231145007 · https://sportskeeda.com/pop-culture/news-the-main-character-you-fans-awe-taehyung-s-influence-compose-coffee-s-ad-youtube-surpassed-1m-views-just-one-day · https://www.sportskeeda.com/us/shows/the-chemistry-chemistrying-fans-cheer-go-youn-jung-cha-eun-woo-s-marithe-commercial-goes-mega-viral-garnering-1-9m-views · https://sbsstar.net/article/N1008699988/shortform-kdrama-in-the-name-of-beauty-surpasses-300-million-views-on-tiktok · https://letter.wepick.kr/post/1648 · https://journal.untar.ac.id/index.php/jmieb/article/view/7717/5195 · https://burjcdigital.urjc.es/handle/10115/35559
- https://www.ypulse.com/newsfeed/2026/04/14/popeyes-is-launching-a-collaboration-with-one-piece/ · https://bsky.app/profile/animenomics.com/post/3mksff33bts2y · https://knowyourmeme.com/memes/shikanoko-nokonoko-koshitantan-opening-edits · https://automaton-media.com/en/news/20230725-20270/ · https://amp.knowyourmeme.com/memes/people/playboianto-me-and-the-gang-if-we-were-in-an-anime
- https://www.warc.com/content/article/cannes/metro-trains-dumb-ways-to-die/en-gb/101929 · https://mumbrella.com.au/?p=161258 · https://www.smartcompany.com.au/marketing/metro-s-dumb-ways-to-die-campaign-awarded-at-cannes-advertising-festival/ · https://en.wikipedia.org/wiki/Ghen_C%C3%B4_Vy · https://www.cbsnews.com/amp/news/coronavirus-prevention-vietnam-song-ghen-co-vy-tik-tok-challenge-about-washing-hands-quang-dang-john-oliver · https://news.uci.edu/2021/06/22/these-videos-could-boost-covid-vaccination-rates · https://en.wikipedia.org/wiki/AsapScience · https://scholarlycommons.pacific.edu/researchday/2015/events/13 · https://ro.ecu.edu.au/ecuworks/1212 · https://screenwiseapp.com/media/miss-rachel-youtube
