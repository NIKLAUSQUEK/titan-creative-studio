# Genre research: §24 Luxury / product reveal, §28 Event / retail / mall, §26 Before / after, §27 ASMR / satisfying

Overnight research run, 2026-10-25. Scope: ground, correct and extend genre-playbooks.md §24, §26, §27, §28 and their presets. This file is a proposal; genre-playbooks.md and tools/editor/presets/ are NOT edited. Klaus approves, then `/learn` and a normal edit apply it.

**Method.** 14 web searches (Firecrawl) plus 4 page reads. 22 public Instagram reels downloaded with yt-dlp (study only, kept in the session scratchpad, never in the repo, never re-uploaded). About 1 in 4 downloads hit HTTP 429 and was retried once, then dropped. 21 reels were measured locally:
- cuts: `ffmpeg select='gt(scene,0.2)'` on 320 px frames (0.3 also logged);
- shot lengths, loudness (ebur128), audio onsets (10 ms energy flux, adaptive threshold) and the share of cuts within 80 ms of an onset;
- words/min: faster-whisper small int8 with VAD; for clips over 90 s, only the first 90 s were transcribed;
- 1 fps sheets for every reel, plus 2 fps or last-40 s sheets for the key ones, all looked at.

YouTube, TikTok and Vimeo examples are cited from articles only.

**Caveats that apply to every number:**
- IG serves normalised audio. 15 of 21 reels read -14.0 to -14.5 LUFS, so loudness only tells us about outliers.
- yt-dlp returned no IG view counts. Likes and comments come from the info.json on 2026-10-25.
- A scene threshold of 0.2 under-counts dissolves and light sweeps, and over-counts flashes. Double cuts under 0.1 s apart are one transition.

---

## 0. Picker-table corrections (proposed rows for §0)
| # | Genre | Use when… | Feeling | Avg shot (measured) | Pace curve | Grade | Sound | Preset |
|---|---|---|---|---|---|---|---|---|
| 24 | Luxury / product reveal / new release | launches, premium products | desire | **narrative film 0.8-1.1 s median; object film 2.6-3.3 s; FOOH one take 7-8 s** | **brand flash ≤1.5 s → story or tease → hero packshot held 2-4 s at the end** | rich blacks, one brand colour | score/whoosh-led, sub hit on the packshot | luxury-reveal (+ new luxury-object-calm, fooh-oneshot) |
| 26 | Before / after transformation | change over time (home, car, hair, product) | proof, "wait for it" | **process 0.6 s median (detailing) or locked one-take time-lapse 7+ s (rug); reveal held to the last 3-5 s** | before shown at 0 s → process → split/wipe reveal at the end (or "part 2") | matched light, locked camera | real process foley, no VO; a whoosh/ding on the reveal | before-after-process (new) |
| 27 | ASMR / satisfying | process, pouring, building, cleaning | calm, completion | **top performer: one locked take (11-20 s) → completed state held 2-3 s; brand reels cut 0.7-1.5 s** | one continuous action → finished object → loop | clean, bright, macro | loud close foley (onsets 15-54 per 10 s), no music, no VO | asmr-satisfying (one-take default) + asmr-product-cut (new) |
| 28 | Event / retail / mall promo | openings, pop-ups, launches, mall events | FOMO, fun | **0.8-1.0 s median (music-only); 1.5 s when there is a VO** | storefront at 0 s → 1 s hero/product/activation inserts → bag-out or what-where-when | bright, natural store light | licensed upbeat track; ~140 wpm VO with dates for events | event-retail-promo (new) |

---

## §24 Luxury / product reveal / new release  [measured: lux_bleu_elordi, lux_missdior, lux_chanel_j12, lux_jacquemus; researched: Maybelline FOOH, Shot on iPhone]

### Evidence
| Ref | Creator / date | Public numbers | Measured |
|---|---|---|---|
| Bleu de Chanel L'Exclusif campaign cut, reposted by Elle Canada. https://www.instagram.com/reel/DY42Z6-ScTk/ | @ellecanada, 2026-05-28 (Chanel film) | 8,042 likes, 57 comments | 30.0 s; 27 cuts; mean 1.07 s, median 0.88 s, min 0.32 s, max 4.32 s. 52% of cuts land on an audio onset. Speech 4%. **Bottle packshot at 1.1-1.6 s, then the story, then the packshot again for the last ~2 s.** |
| Miss Dior (Natalie Portman) campaign. https://www.instagram.com/reel/DdBMVnJze7j/ | @marieclaireau, 2026-09-08 (Dior film) | 3 likes on the repost (the reach sits on Dior's own post) | 27.0 s, 16:9; 27 cuts; median 0.84 s; 24 wpm VO (speech share 0.91 = the music/VO bed) |
| Chanel J12 Bleu Tourbillon watch film. https://www.instagram.com/reel/DLN027ntJJV/ | @victorgueret (crew), 2025-06-22 | 161 likes | 30.0 s, 16:9; 8 cuts; **median 3.08 s, min 2.56 s**; no speech. The calm "object" film. |
| Jacquemus "Bags on wheels" FOOH (CGI). https://www.instagram.com/reel/CqqN8w6K3rL/ | @origiful, 2023-04-05 | 21,039 likes on this repost. Echo Poster cites ~2M likes (Dialect) for the campaign | **7.87 s, 0 cuts.** One handheld street take; bags roll past; the pink bag fills the frame at 6-7 s (the reveal is a pass-by, not a cut). -8.4 LUFS (loud), 29 onsets/10 s (traffic + music). |
| Maybelline Sky High "mascara tube" FOOH | Maybelline / London, July 2023 | 76M views (Beauty Packaging, via echoposter.com/en/amplification/fooh/); The Drum 2023-07-14 on the fake-OOH debate | not downloaded (researched) |
| Shot on iPhone (Apple, TBWA\Media Arts Lab) | Cannes Lions 2025 Creative Effectiveness Grand Prix (canneslions.com day-four winners) | platform proof, not a single film | researched |
| AI spec ads (for contrast). https://www.instagram.com/reel/Dbbd-2rAwRL/ and https://www.instagram.com/reel/DXwNmSUSa9t/ | @fiz_zstudio 2026-07-30, @dezinbydeepak 2026-04-30 | 8 and 3 likes | 6.9 s and 23.5 s, both 0 cuts (one-take AI reveal). The second has a 220 wpm VO "this is all AI". These show what the market is copying, not what performs. |

### What changed vs the draft card
1. **Withholding until 12 s is wrong for paid/social luxury.** Both real fragrance films show the product as a brand flash in the first 1.6 s. They run the story, then return to a held packshot at the end. Full withholding only works in a single-take FOOH, where the object itself is the hook and is visible from frame 1.
2. **There are two speeds, not one.** "Narrative luxury" (fragrance, fashion) cuts at a 0.8-0.9 s median with 4 s holds on faces or the bottle. "Object luxury" (watches, jewellery) holds about 3 s per shot. The old card's 1-3 s average blurred the two.
3. **FOOH / one-take spectacle is its own sub-style.** 7-8 s, no cut, the impossible object in a real recognisable place, loud real ambience. This is the highest-reach luxury format in the evidence (Maybelline 76M, Jacquemus ~2M likes).
4. Packshot end hold: 2-4 s, centred, dark ground, name only (no CTA text in the film; the CTA goes in the caption).

### Corrected card
### 24. Luxury / product reveal / new release [measured: DY42Z6-ScTk, DdBMVnJze7j, DLN027ntJJV, CqqN8w6K3rL]
- **Why it works:** a desire loop. A brand flash tells you whose world this is, the story makes you want to be in it, and the held packshot is the object you take away. Spectacle (FOOH) works when the product is impossible in a real place.
- **Pacing (30 s, narrative):**
  - 0-1.6 s: a brand flash (bottle or object, 0.5-1 s), then cut to the face/world;
  - 1.6-26 s: the story, median 0.85 s cuts, 3-4 s holds on the emotional peaks, ~50% of cuts on music onsets;
  - 26-30 s: a hero packshot held 2-4 s plus the name.
- **Pacing (30 s, object):** 8-10 shots of 2.5-3.5 s (macro detail → light sweep → wrist/hand → packshot); no cut under 2.5 s.
- **Pacing (FOOH, 6-10 s):** one take, the object visible from 0 s, the scale reveal at 60-85% of the runtime (a pass-by or camera move), no cut, no text until the final second.
- **Shot grammar:** a macro slider or a specular light sweep for the object; tight faces and hands for the narrative; a centred packshot with negative space; FOOH = handheld phone height in a real landmark street.
- **Look:** rich blacks (narrative) or neutral daylight (FOOH); one brand colour carried through wardrobe, light or set.
- **genre_key (narrative/object):** `premium fragrance commercial, cinematic shallow depth, rich deep blacks, controlled specular highlights on glass, one brand colour accent, slow deliberate camera, centred hero packshot`
- **genre_key (FOOH):** `handheld phone video on a real city street, natural daylight, photoreal CGI oversized product integrated with correct shadows and reflections, documentary realism, no text`
- **Shot JSON:**
  - `{"id":"s01","dur":0.8,"camera":"locked, 85mm, centred","subject":"@product bottle","action":"start: bottle in darkness -> end: a thin light sweep catches the cap","light":"single strip softbox","genre_key":"…"}`
  - FOOH: `{"id":"f01","dur":8,"camera":"handheld 24mm at chest height, slow pan right","action":"start: real street, the oversized @product drives in from the back -> end: it passes the lens and fills the frame","constraints":"one take, no cuts, real traffic sound"}`
- **Sound:** score- or whoosh-led; the whoosh peak on each fast cut; a sub/boom on the end packshot; no VO, or one whispered line. FOOH = real street ambience plus one musical sting.
- **Compliance:**
  - real prices, dates and terms; no fake scarcity (SG CCS enforcement, 18 May 2026);
  - FOOH must not be passed off as a real stunt in a factual claim. Caption "CGI" or "concept" and don't tag a transit operator or landmark as a partner without permission (The Drum, 2023-07-14, on the Maybelline backlash);
  - AI-made: label it AI per studio rules.
- **Preset:** luxury-reveal (narrative), luxury-object-calm (new), fooh-oneshot (new).

### Presets
```json
{
  "name": "luxury-reveal",
  "label": "Luxury narrative film (fragrance / fashion)",
  "kind": "genre",
  "description": "Measured 2026-10-25 (Bleu de Chanel, Miss Dior reels): brand flash <=1.6 s, story at ~0.85 s median cuts with 3-4 s peak holds, ~50% of cuts on music onsets, hero packshot held 2-4 s at the end. No talking, no subtitles.",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#24",
  "beat_sync": true,
  "structure": {"name": "lux-narrative", "target_s": [15, 30], "beats": ["brand flash 0-1.6s", "world/story", "peak hold", "story", "packshot hold 2-4s"]},
  "pacing": {"remove_silence_over_s": 0.6, "pad_s": 0.1, "remove_fillers": "none", "max_shot_s": 4.3},
  "captions": {"enabled": false},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.04, "on_hook": 1.0},
  "transitions": {"default": "dip", "on": "beats", "dur_s": 0.12, "strength": 0.4},
  "sfx": {"density_per_10s": 0.8, "db": -16, "cut_coverage": 0.3, "min_gap_s": 1.5, "map": {"broll": "whoosh", "end": "boom"}},
  "music": {"energy": "mid", "db": -12, "duck": false},
  "grade": {"contrast": 1.14, "saturation": 0.92, "brightness": -0.03, "vignette": true},
  "broll": {"every_s": 0.9, "max_dur_s": 4.3, "min_dur_s": 0.35, "mode": "full"},
  "end_card": {"enabled": true, "dur_s": 2.5, "_needs_feature": "end_card.style 'packshot': hold the last product shot with the name centred instead of the text card"}
}
```
```json
{
  "name": "luxury-object-calm",
  "label": "Luxury object film (watch / jewellery / premium device)",
  "kind": "genre",
  "description": "Measured 2026-10-25 (Chanel J12 film): 8-10 shots, median 3.1 s, never under 2.5 s; macro, light sweep, wrist, packshot; music only.",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#24",
  "beat_sync": true,
  "pacing": {"remove_silence_over_s": 1.0, "pad_s": 0.2, "remove_fillers": "none", "max_shot_s": 5.5},
  "captions": {"enabled": false},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "smooth", "every_s": 3, "scale": 1.05, "on_hook": 1.0},
  "transitions": {"default": "dip", "on": "cuts", "dur_s": 0.2, "strength": 0.5},
  "sfx": {"density_per_10s": 0.3, "db": -18, "map": {"end": "swell"}},
  "music": {"energy": "low", "db": -13, "duck": false},
  "grade": {"contrast": 1.12, "saturation": 0.9, "vignette": true},
  "broll": {"every_s": 3.0, "max_dur_s": 5.5, "min_dur_s": 2.5, "mode": "full"},
  "end_card": {"enabled": true, "dur_s": 3.0}
}
```
```json
{
  "name": "fooh-oneshot",
  "label": "FOOH / one-take product spectacle",
  "kind": "genre",
  "description": "Measured 2026-10-25 (Jacquemus bags, 7.9 s, 0 cuts): one handheld street take, impossible-scale product visible from 0 s, pass-by reveal at 60-85%, loud real ambience, no text until the last second. Label CGI/AI in the caption.",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#24",
  "structure": {"name": "fooh", "target_s": [6, 12], "beats": ["object in real street 0s", "approach", "scale reveal 60-85%", "brand mark last 1s"]},
  "pacing": {"remove_silence_over_s": 99, "pad_s": 0, "remove_fillers": "none", "max_shot_s": 15, "drop_retakes": false},
  "captions": {"enabled": false},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "snap", "every_s": 0, "on_hook": 1.0, "on_emphasis": false},
  "sfx": {"density_per_10s": 0.2, "db": -14, "map": {"end": "boom"}},
  "music": {"energy": "mid", "db": -16, "duck": false},
  "grade": {"contrast": 1.04, "saturation": 1.04},
  "broll": {"every_s": 0},
  "end_card": {"enabled": false},
  "_needs_feature": "loop seam check (shared with silent-loop-reaction) so the 8 s take replays cleanly"
}
```

### 3 core rules
1. Show the brand in the first 1.6 s and end on a held packshot (2-4 s); the story goes in between.
2. Choose the speed by category: narrative (fragrance/fashion) uses ~0.85 s median cuts; object (watch/jewellery/device) never cuts under 2.5 s.
3. Spectacle beats montage for reach. One impossible take in a real place (FOOH), clearly labelled CGI/AI, with no text until the end.

---

## §28 Event / retail / mall promo  [measured: mall_popmart, mall_grove_nb, mall_switch2, mall_jewel_poke, mall_lush_westquay, mall_wellbred]

### Evidence
| Ref | Creator / date | Public numbers | Measured |
|---|---|---|---|
| POP MART opening, Mall of America. https://www.instagram.com/reel/DQxooZQEaIl/ | @mallofamerica, 2025-11-08 | 627 likes (mall account) | 10.7 s; 10 cuts; **median 1.03 s, range 0.5-1.23 s**; music only. Storefront at 0 s → 7 product/character hero inserts → shopper walks out holding the bag. |
| New Balance store opening + pop-up, The Grove LA. https://www.instagram.com/reel/DbjPtUuyQyu/ | @thegrovela, 2026-08-02 | 492 likes, 15 comments | 26.9 s; 26 cuts; **median 0.83 s**, max 3.1 s; 50% of cuts on onsets; music only. Exterior → **hands doing the activation** (DJ pad, photo booth, free juice from an ice trough) → walk-through → shelves → hero jacket. Almost no identifiable faces. |
| Nintendo Switch 2 Experience at Jewel Changi (SG). https://www.instagram.com/reel/DLG_uWwh0qs/ | @bringyourkidout, 2025-06-20 | 97 likes | 22.7 s; 14 cuts; median 1.53 s; **VO 140 wpm, the first word at 1.36 s**, says the dates ("from now till 24 July 2025") and "FREE". The SG events-guide formula. |
| Jewel Changi school-holiday events. https://www.instagram.com/reel/C70QWlrSzmX/ | @jewelchangiairport, 2024-06-05 | 72 likes | 19.2 s; 8 cuts; median 1.48 s; one 7.6 s hold on the key-art/what-where-when card. |
| Lush ASMR at Westquay mall. https://www.instagram.com/reel/DYh60iMgIAz/ | @westquay, 2026-05-19 | 83 likes | 22.7 s; 21 cuts; median 0.98 s; no speech. A mall account using the ASMR format for a tenant (cross-genre). |
| WellBred Club pop-up, Funan SG. https://www.instagram.com/reel/DdlEbfezzJ9/ | @wellbredstore, 2026-09-22 | 3 likes | 24.4 s; 20 detected cuts, mostly flash-transition pairs; median 2.2 s. **The low performer: slow, offer-led ("10% off every $88").** |
| Context | Pop Mart revenue guidance >US$4bn (Reuters, 2025-08-20) explains why a toy opening outperforms; CCS SG 2026-05-18 dark-patterns enforcement (fake countdowns, rotating "flash sales", random "almost sold out") | | |

Honest note: mall and retailer accounts get hundreds of likes, not millions. Treat these reels as format references, not proof of virality. The engagement lift comes from the anchor product (Pop Mart, Nintendo, New Balance) more than from the edit.

### What changed vs the draft card
1. The pace is measured: **0.8-1.0 s median when music-only; ~1.5 s when a VO carries the dates**. The old "0.8-2 s" was right in range, but the two modes need different presets.
2. The best performers open on **the storefront or product at 0 s**, not a crowd. The middle is **hands interacting** (it reads as fun, needs no face consent) and the end is **a bag-out or what-where-when**.
3. Event promos that inform (SG events guides) use a fast VO with exact dates and "free". Brand/mall accounts go music-only with the info in the caption.
4. Offer-led openings (a discount as the hook) measured slowest and weakest.

### Corrected card
### 28. Event / retail / mall promo [measured: DQxooZQEaIl, DbjPtUuyQyu, DLG_uWwh0qs, C70QWlrSzmX]
- **Why it works:** a 10-25 s virtual walk-in. Seeing the door, touching the things and leaving with the bag lets the viewer rehearse the visit.
- **Pacing (15-25 s):**
  - 0-1 s: the storefront, logo or anchor product (no logo animation, no countdown);
  - 1-18 s: 1 s inserts on the beat in a fixed order: hero product → hands using the activation → freebie or photo moment → shelf walk-through;
  - the last 2-3 s: a bag-out or a what-where-when card (date, level/unit, hours), held at least 2 s.
- **Shot grammar:**
  - gimbal or handheld walk-in at eye level;
  - hands-only interaction close-ups;
  - product heroes centred;
  - crowds wide and unidentifiable;
  - faces only with consent (staff or creators).
- **Look:** natural store light, bright and saturated, white balance matched across clips.
- **genre_key:** `bright retail store opening, eye-level gimbal walk-in, hands interacting with product displays, clean saturated store lighting, shoppers unidentifiable, energetic`
- **Shot JSON:** `{"id":"r03","dur":1.0,"camera":"handheld close, 35mm, slight push","subject":"hands","action":"start: hand reaches into ice trough -> end: lifts @product bottle to lens","light":"store practicals"}`
- **Sound:**
  - a licensed upbeat track (brand accounts never use trending chart audio baked in);
  - cuts on the beat (~50% of cuts on onsets in the best one);
  - optional fast VO (~140 wpm) that states the dates within the first 3 s;
  - a pop on the what-where-when card.
- **Compliance:**
  - real dates, hours and unit numbers;
  - "while stocks last" only when stock is genuinely limited;
  - no fake countdowns, rotating "flash sales" or random "almost sold out" (CCS Singapore, 18 May 2026; SCAP bait-advertising clauses);
  - show the terms of a free gift;
  - crowd faces need consent or must stay unidentifiable;
  - mall property filming needs management permission.
- **Preset:** event-retail-promo (music-only) or event-guide-vo (with VO).

### Presets
```json
{
  "name": "event-retail-promo",
  "label": "Event / retail / mall opening (music-only walk-in)",
  "kind": "genre",
  "description": "Measured 2026-10-25 (POP MART MOA, New Balance The Grove): storefront at 0 s, 1 s beat-cut inserts (hero product -> hands on activation -> freebie -> shelf walk), bag-out or what-where-when card held >=2 s. No subtitles; info lives on one card + caption.",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#28",
  "beat_sync": true,
  "structure": {"name": "walk-in", "target_s": [10, 25], "beats": ["storefront 0-1s", "hero product", "hands on activation", "freebie / photo moment", "shelf walk", "bag-out or what-where-when 2s+"]},
  "pacing": {"remove_silence_over_s": 0.3, "pad_s": 0.03, "max_shot_s": 3.2},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "persistent": false, "dur_s": 1.6, "position_y": 0.22, "uppercase": false, "max_words": 6},
  "zoom": {"mode": "snap", "every_s": 0, "on_hook": 1.0},
  "transitions": {"default": "flash", "on": "beats", "dur_s": 0.06, "strength": 0.25},
  "sfx": {"density_per_10s": 0.5, "db": -14, "map": {"title": "pop", "end": "ding"}},
  "music": {"energy": "high", "db": -10, "duck": false},
  "grade": {"contrast": 1.05, "saturation": 1.12, "brightness": 0.02},
  "broll": {"every_s": 1.0, "max_dur_s": 1.3, "min_dur_s": 0.5, "mode": "full"},
  "end_card": {"enabled": true, "dur_s": 2.2, "_needs_feature": "end_card.fields {date, place, unit, hours} rendered as a what-where-when card"}
}
```
```json
{
  "name": "event-guide-vo",
  "label": "Event guide with VO (dates + free entry)",
  "kind": "genre",
  "description": "Measured 2026-10-25 (Switch 2 Experience @ Jewel, SG events guide): VO ~140 wpm starting by 1.4 s and naming the dates in the first sentence, ~1.5 s cuts, sentence captions.",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#28",
  "beat_sync": false,
  "pacing": {"remove_silence_over_s": 0.25, "pad_s": 0.05, "remove_fillers": "hard", "max_shot_s": 2.4},
  "captions": {"enabled": true, "max_words": 5, "animation": "pop", "uppercase": false, "keyword_caps": true},
  "hook_text": {"enabled": true, "max_words": 6, "uppercase": true},
  "zoom": {"mode": "snap", "every_s": 0},
  "sfx": {"density_per_10s": 0.6, "map": {"title": "pop"}},
  "music": {"energy": "mid", "db": -20, "duck": true},
  "grade": {"saturation": 1.1},
  "broll": {"every_s": 1.5, "max_dur_s": 2.0, "min_dur_s": 1.0, "mode": "full"},
  "end_card": {"enabled": true, "dur_s": 2.0}
}
```

### 3 core rules
1. Frame 1 is the door or the anchor product, never a discount. Offers go on the end card or in the caption.
2. The middle is hands on things at ~1 s per beat. This gives fun without needing face consent.
3. End on proof of a visit (the bag-out) or a what-where-when card held at least 2 s, with real dates and no fake urgency.

---

## §26 Before / after transformation  [measured: ba_rug1, ba_rug2, ba_car1, ba_hair1; compliance researched]

### Evidence
| Ref | Creator / date | Public numbers | Measured |
|---|---|---|---|
| Pink rug restoration. https://www.instagram.com/reel/DR4YtfODqnh/ | @mountainrugcleaning, 2025-12-05 | 18,775 likes, 70 comments | 179 s; only 10 cuts, **median shot 7 s**, longest 47.7 s. **Locked overhead camera for the whole video** (time-lapse speed changes, not cuts). The dirty rug is visible at 0 s. The last ~3 s: a cross-fade back to dirty, then a **wipe-split BEFORE \| AFTER card** with yellow italic labels. No speech, process foley. |
| "Impossible clean" rug. https://www.instagram.com/reel/DMz7w4FykvS/ | @mountainrugcleaning, 2025-08-01 | 2,794 likes | 177 s, **0 cuts** (one locked take, speed-ramped); LRA 12 LU (big quiet/loud swings in the process sound). |
| Car interior restoration. https://www.instagram.com/reel/DZ6xdQMvo1q/ | @meutrux, 2026-06-23 | 263 likes | 180.7 s; 187 cuts; **median 0.63 s**, first cut 0.7 s. **"Post-frame" layout: the video sits inside a fake X/Twitter post (avatar, handle, "This Car Was Hiding Under Years of Dirt") on black.** The reveal is the reassembled car in the last ~5 s. |
| Hair transformation, part 1. https://www.instagram.com/reel/DaqIzskRjC1/ | @tiffanyloe, 2026-07-11 | **24,172 likes, 6,513 comments** | 151.9 s; 42 cuts; median 2.87 s; **VO 154 wpm, speaking from 0.0 s**, sentence captions; top card "She gave me free reign… and I have one crazy idea 😏". **No "after" at all: it ends on "FOLLOW & COMMENT for part 2!!! 😱".** The consultation IS the content; the reveal is withheld to a sequel (a comment magnet: comments are 27% of likes). |
| Hair, part 2 style. https://www.instagram.com/reel/DS-lw_CEktQ/ | @tiffanyloe, 2026-01-01 | 6,106 likes, 1,337 comments | downloaded; the measurement didn't finish in time |

### Platform and legal rules (what is allowed)
| Where | Before/after rule | Source |
|---|---|---|
| **SG licensed healthcare (Physio Spot, any HCSA licensee)** | **Banned in any advertising medium**, including "after-only" images, with or without disclaimers, and even split across several ads. Allowed only in the clinic during a consultation. This covers the clinic's website and social accounts (Singapore-accessible). | Healthcare Services (Advertisement) Regulations 2021 reg 5(1)(d) (sso.agc.gov.sg/SL/HSA2020-S1033-2021); MOH HCS Advert Regs FAQ; xaviertan.co/hcsa-advertising-guidelines |
| **SG health (other)** | No unjustified expectations, no "results in N sessions", no superlatives (same regs 5(1)(c),(e)) | same |
| **Meta ads** | 18+ targeting for weight, diet and cosmetic. **Before/after IS allowed for general cosmetic products, procedures and surgeries at 18+** (policy page, change log Jul 22, 2026). Banned: pinch-fat close-ups, "statements of inferiority about appearance", permanent skin whitening, timeframe promises without qualifiers. Weight-loss before/after is risky: allowed only as "impact of use" with a clear timeframe, and frequently rejected. | transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/ |
| **TikTok ads** | Body image: no shaming, no "ideal body", no claims that appearance changes life or confidence. Weight claims 18+ only, via a healthy lifestyle. Cosmetic surgery (Mar 2026 update): no before/after that "exaggerates results, body shaming, or unsafe health claims". TikTok Shop: no before/after body comparisons for weight or muscle (exceptions: debloating, fitness equipment). | ads.tiktok.com weight-management policy; ads.tiktok.com update-to-cosmetic-surgery-na-march-2026; seller-us.tiktok.com health content requirements |
| **Snapchat / Pinterest** | Snapchat: no before/after in diet and fitness ads. Pinterest: no weight-loss imagery or before/after at all. | accelerateddigitalmedia.com 2026 matrix |
| **Non-health objects (rugs, cars, homes, shoes, gadgets, hair *styling*)** | Fine everywhere, provided the result is real and unedited (no filter on the "after" only). Hair *colour or cut* sits in beauty: fine on Meta/TikTok, but keep "no shaming" wording. | general misleading-ad rules (SCAP; ASA CAP 03) |

**What a SG physio CAN do instead (proposal for Physio Spot):**
- "Process, not outcome": show the method (assessment, mobility drill, taping) on a staff member or a consenting model, never a patient's result.
- Use an **object metaphor** for the transformation (a rusty hinge oiled, a tangled cable untangled, a stiff spring) in the before/after grammar.
- Make the before/after about **the space or tool** (new treatment room, new equipment), not a body.

All of these need Klaus's sign-off against the SG compliance pack.

### What changed vs the draft card
1. **The "snap switch on the beat" is not what the high performers do.** They show the "before" at 0 s, spend 90%+ of the runtime on a satisfying process, and land the reveal in the last 3-5 s. The reveal is often a **split/wipe BEFORE | AFTER comparison card**, not a hard cut.
2. **Two process grammars, both measured:**
   - (a) a locked one-take time-lapse (rug: a median 7 s shot or zero cuts);
   - (b) rapid 0.6 s detail cuts (car).
   In both, the camera position for before and after is identical.
3. **The "part 2" cliffhanger** (hair, 6.5K comments) is a strong organic format. It is not usable for ads, since it withholds the product result.
4. Most transformation reels are ASMR hybrids: no VO, process foley up. Hair is the exception (a talk-led consult).
5. Long runtime is normal: 150-180 s performed. The old card implied short.

### Corrected card
### 26. Before / after transformation [measured: DR4YtfODqnh, DMz7w4FykvS, DZ6xdQMvo1q, DaqIzskRjC1]
- **Why it works:** the before shown at 0 s opens a loop ("can they fix THAT?"). The process is satisfying on its own, and the side-by-side at the end closes the loop as proof.
- **Pacing (organic, 30-180 s):**
  - 0-1 s: the worst view of the "before" + a title card ("This rug was dumped");
  - process: locked one-take with speed ramps (median 7 s+) OR 0.6 s detail cuts on the steps;
  - last 3-5 s: return to the exact before framing → cross-fade or wipe to after → split BEFORE | AFTER card held at least 2 s.
- **Pacing (ad, 15-30 s):** before 0-1.5 s → 3-5 process beats → split card from ~70% → product/CTA.
- **Shot grammar:**
  - the before and after frames are locked identical (tripod mark, same lens, light and time of day);
  - overhead for flat objects, three-quarter for cars and rooms;
  - hands-only process;
  - no filter on the after only.
- **genre_key:** `locked overhead tripod, identical framing before and after, bright even studio light, real dirt and real result, satisfying cleaning process, no filters`
- **Shot JSON:** `{"id":"b05","dur":3,"camera":"locked overhead, 24mm, same mark as b01","subject":"@object","action":"start: grey matted pile -> end: squeegee pass reveals pink pile in one stripe","light":"same softbox as b01","constraints":"camera must not move between b01 and b05"}`
- **Sound:** real process foley up (brush, water, squeegee, vacuum). No VO for object restoration; a talk-led consult only for hair/people. A whoosh on the wipe and a ding/pop on the BEFORE | AFTER card.
- **Compliance:**
  - **SG healthcare: no before/after or after-only of people in any ad or social post.** Use process, object metaphors or space/tool upgrades only;
  - Meta: cosmetic before/after OK at 18+; no pinch-fat, no inferiority wording, no timeframe promises;
  - TikTok: no exaggerated or body-shaming before/after; weight claims 18+ via a healthy lifestyle;
  - every brand: an unedited after, and the same light. If the result took several sessions, say so.
- **Preset:** before-after-process (new; replaces ugc-try-on-demo for this genre), before-after-fast (car-style cuts).

### Presets
```json
{
  "name": "before-after-process",
  "label": "Before / after: locked process + split reveal",
  "kind": "genre",
  "description": "Measured 2026-10-25 (Mountain Rug Cleaning 18.8K likes; Meutrux car): before at 0 s, satisfying process (locked one-take with speed ramps, or 0.6 s detail cuts), last 3-5 s return to identical framing -> wipe to after -> BEFORE | AFTER split card held 2 s+. No VO, process foley up. Health brands in SG: NEVER on people (HCSA reg 5(1)(d)).",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#26",
  "structure": {"name": "before-after", "target_s": [20, 180], "beats": ["before 0-1s + title", "process step 1", "process step 2", "process step 3", "return to before framing", "wipe to after", "split card 2s+", "CTA (ads only)"]},
  "pacing": {"remove_silence_over_s": 99, "pad_s": 0.0, "remove_fillers": "none", "max_shot_s": 50, "drop_retakes": false},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "persistent": false, "dur_s": 2.5, "position_y": 0.2, "uppercase": false, "max_words": 8},
  "zoom": {"mode": "snap", "every_s": 0, "on_hook": 1.0},
  "transitions": {"default": "dip", "on": "beats", "dur_s": 0.3, "strength": 0.3},
  "sfx": {"density_per_10s": 0.2, "db": -14, "map": {"end": "ding", "title": "whoosh"}},
  "music": {"energy": "none"},
  "grade": {"contrast": 1.04, "saturation": 1.04},
  "broll": {"every_s": 0},
  "end_card": {"enabled": false},
  "reveal": {"type": "wipe_split", "labels": ["BEFORE", "AFTER"], "label_style": "yellow italic outline", "hold_s": 2.5, "_needs_feature": "before/after reveal: same-frame wipe + split card from two tagged frames (items with beat 'before' and 'after')"},
  "speed_ramp": {"_needs_feature": "per-item speed curve (items[].speed is constant today); needed for one-take time-lapse process"},
  "compliance": {"block_if_brand_industry": ["health-sg"], "_needs_feature": "QC block when a health-SG brand uses this preset on a person"}
}
```
```json
{
  "name": "before-after-fast",
  "label": "Before / after: rapid detail cuts (car / room restore)",
  "kind": "genre",
  "description": "Measured 2026-10-25 (Meutrux car, 187 cuts / 181 s, median 0.63 s): before at 0 s, rapid 0.4-1 s process cuts each completing one action, reassembled reveal in the last 5 s. Optional post-frame layout (fake social post header on black).",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#26",
  "pacing": {"remove_silence_over_s": 0.2, "pad_s": 0.02, "remove_fillers": "none", "max_shot_s": 1.2},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "persistent": true, "renderer": "card", "card_style": "outline", "uppercase": false, "max_words": 8, "position_y": 0.12},
  "zoom": {"mode": "snap", "every_s": 0},
  "sfx": {"density_per_10s": 1.0, "db": -16, "cut_coverage": 0.15, "map": {"end": "ding"}},
  "music": {"energy": "low", "db": -22, "duck": false},
  "broll": {"every_s": 0},
  "layout": {"type": "post_frame", "_needs_feature": "post_frame layout: video inset under a fake-post header (avatar, handle, title) on black"}
}
```

### 3 core rules
1. Show the worst "before" at 0 s, and make the "after" from the identical camera position and light. A moved camera breaks the proof.
2. Spend the runtime on the satisfying process. Put the reveal in the last 3-5 s as a wipe or split BEFORE | AFTER card held at least 2 s.
3. Never show people's health results for SG healthcare (reg 5(1)(d)), and nothing shaming or exaggerated anywhere. Transform objects, spaces and tools instead.

---

## §27 ASMR / satisfying  [measured: asmr_sandtagious, asmr_kinetic_off, asmr_bello, asmr_zip, asmr_horlicks, mall_lush_westquay; researched: Oddly IKEA, McDonald's Japan]

### Evidence
| Ref | Creator / date | Public numbers | Measured |
|---|---|---|---|
| "Ultimate Kinetic Sand Drop & Squish". https://www.instagram.com/reel/DaQQ9EuuNu4/ | @sand.tagious, 2026-07-01 | **44,732 likes, 355 comments** (30K in search two days earlier) | 21.8 s; **1 cut; one locked take of 19.7 s**, then a 2.2 s hold on the finished cone. **-17.9 LUFS with 53.6 onsets/10 s**: dense, close granular foley, no music, no VO, no text. The structure is "empty cone → layers drop in → pressed flat → topped → finished object". |
| Kinetic Sand official. https://www.instagram.com/reel/DePW2v6KrRO/ | @kineticsand, 2026-10-08 | 66 likes, 8 comments | 13.9 s; 2 cuts (3.3 s + 7.4 s shots). **-45.9 LUFS: practically silent.** The same product, a far weaker result. The likely cause: the brand cut the sound. |
| Bello Water concept. https://www.instagram.com/reel/C8xWr4mp4mL/ | @ansoatelier, 2024-06-28 | 84 likes | 10 s; 13 cuts; median 0.73 s; 33 onsets/10 s; 54% of cuts on onsets (pour, ice, cap). |
| "ZIP ASMR" (AI beauty). https://www.instagram.com/reel/DajMnknNOLF/ | @nikoxstudios, 2026-07-08 | 7 likes | 15 s; 8 cuts; median 1.46 s; first cut at 4.0 s. |
| Jackpot snacks "product-led ASMR". https://www.instagram.com/reel/DZujP64IbuB/ | @brandtalkindia, 2026-06-18 | 18 likes | 21.3 s; median 0.67 s; it opens on a 6 s billboard reveal before any crunch. **The ASMR promise is broken by the hook**, and the crunch arrives late. |
| Lush ASMR in a mall. https://www.instagram.com/reel/DYh60iMgIAz/ | @westquay, 2026-05-19 | 83 likes | 22.7 s; median 0.98 s; no speech. |
| Oddly IKEA (Ogilvy NY, 2017) | 25-min ASMR film + shorter cuts; ANA International ECHO Gold 2018 (Retail & Direct Sales) | ana.net 2018 ECHO winners; Adweek, Quartz, Fast Company coverage | researched |
| McDonald's Japan 500-yen-meal ASMR (Dentsu Japan) | Grand Prix, Best Innovation, TikTok Ad Awards Japan; "simple, minimal photography", sizzle sound | TikTok Creative Center "Creative Wins #AllAroundAPAC", 2024-05-14 | researched |

### What changed vs the draft card
1. **The top performer is one continuous take, not a string of 2-4 s shots.** A single locked 15-20 s action that builds to a finished object, then a 2-3 s hold, beat every multi-cut brand reel by about 500×. Cut-based ASMR (0.7-1.5 s) belongs to product ads, where the edit must show several textures.
2. **Loudness and onset density are the product.** The 44.7K-like reel has 53 audible onsets per 10 s. The official brand reel was nearly silent (-45.9 LUFS) and flopped. Add a QC check: foley under -24 LUFS integrated, or under ~10 onsets/10 s, fails.
3. **Never open with something that isn't the satisfying action** (the Jackpot billboard hook). The first second must already make the sound.
4. Text: none in the top performer. One small lowercase line at most for brand ads.

### Corrected card
### 27. ASMR / satisfying [measured: DaQQ9EuuNu4, DePW2v6KrRO, C8xWr4mp4mL, DZujP64IbuB]
- **Why it works:** the viewer wants to see the action complete, and dense close sound triggers the tingle. Both break the moment you cut away or go quiet.
- **Pacing:**
  - one-take (default, 12-25 s): the action starts by 0.5 s → continuous build in one locked shot → the finished object held 2-3 s → loops cleanly;
  - product-cut (ads, 10-20 s): 0.7-1.5 s shots, each completing one sound (pour, crack, click, peel), with about half the cuts on the sound's onset; the last shot holds 2 s on the product.
- **Shot grammar:** locked tripod, macro or tight top-down or side-on; a clean seamless background; one action per shot; hands only; symmetrical containers (glass shows the layers).
- **Look:** clean, bright, high-key, saturated product colours; no grade tricks.
- **genre_key:** `oddly satisfying macro process, locked tripod, seamless clean background, crisp texture detail, soft even high-key light, one continuous action, no text`
- **Shot JSON:** `{"id":"a01","dur":18,"camera":"locked side-on, 50mm macro, transparent cone centred","subject":"@product","action":"start: empty clear cone -> end: four coloured layers dropped, pressed and topped into a finished cone","audio":"close-mic granular foley only","constraints":"one take, no cut, no music"}`
- **Sound:**
  - close-mic foley at -16 to -18 LUFS integrated, dense (15-55 onsets/10 s);
  - no music, or a bed under -30 dB;
  - no VO;
  - never compress the transients away;
  - generated video needs a real foley pass (record the real product).
- **Compliance:** food: no health claims hidden in captions. Kids' products: no "buy now" pressure (child-directed advertising rules). AI-made textures: label AI.
- **Preset:** asmr-satisfying (one-take default) and asmr-product-cut (new).

### Presets
```json
{
  "name": "asmr-satisfying",
  "label": "ASMR / satisfying: one continuous take",
  "kind": "genre",
  "description": "Measured 2026-10-25 (@sand.tagious 44.7K likes: one 19.7 s locked take + 2.2 s finished hold, -17.9 LUFS, 53 onsets/10 s; vs official brand reel at -45.9 LUFS, 66 likes). No talking, no captions, no music, loud dense foley, loop ending.",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#27",
  "structure": {"name": "one-take", "target_s": [12, 25], "beats": ["action starts by 0.5s", "continuous build", "finished object hold 2-3s", "loop"]},
  "pacing": {"remove_silence_over_s": 99, "pad_s": 0.0, "remove_fillers": "none", "max_shot_s": 25, "drop_retakes": false},
  "captions": {"enabled": false},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "snap", "every_s": 0, "on_hook": 1.0, "on_emphasis": false},
  "sfx": {"density_per_10s": 0},
  "music": {"energy": "none"},
  "grade": {"contrast": 1.04, "saturation": 1.08, "brightness": 0.02},
  "broll": {"every_s": 0},
  "end_card": {"enabled": false},
  "audio_qc": {"min_lufs": -24, "min_onsets_per_10s": 10, "_needs_feature": "QC fail when the foley track is quieter or sparser than these"},
  "loop": {"_needs_feature": "loop seam finder (shared with silent-loop-reaction)"}
}
```
```json
{
  "name": "asmr-product-cut",
  "label": "ASMR product ad: one sound per cut",
  "kind": "genre",
  "description": "Measured 2026-10-25 (Bello Water concept, Lush @ Westquay): 0.7-1.5 s shots each completing one sound, ~50% of cuts on the sound onset, product hold 2 s at the end, no VO. The first frame must already make the sound (Jackpot reel opened on a billboard and lost the ASMR promise).",
  "reference": "research/genre-research-2026-10/luxury-retail-transform-asmr.md#27",
  "beat_sync": false,
  "pacing": {"remove_silence_over_s": 2, "pad_s": 0.05, "remove_fillers": "none", "max_shot_s": 2.0},
  "captions": {"enabled": false},
  "hook_text": {"enabled": true, "uppercase": false, "size": 0.03, "max_words": 5, "dur_s": 2.0},
  "zoom": {"mode": "snap", "every_s": 0},
  "sfx": {"density_per_10s": 0},
  "music": {"energy": "none"},
  "grade": {"contrast": 1.05, "saturation": 1.1, "brightness": 0.02},
  "broll": {"every_s": 1.0, "max_dur_s": 1.5, "min_dur_s": 0.6, "mode": "full"},
  "end_card": {"enabled": false},
  "cut_on_onset": {"source": "clip_audio", "_needs_feature": "snap cuts to onsets in the clip's own foley (beat_sync only reads the music track today)"}
}
```

### 3 core rules
1. The sound is the product. Keep the foley loud and dense (about -17 LUFS, 15+ onsets per 10 s) with no music or VO. A quiet ASMR reel is a dead reel.
2. Default to one locked continuous take that builds to a finished object held 2-3 s. Use cuts only for multi-texture product ads, one sound per cut.
3. Frame 1 already makes the satisfying sound: no logo, billboard or setup first.

---

## New sub-styles / ad formats proposed
1. **FOOH one-take** (preset fooh-oneshot, under §24): the impossible-scale product in a real place, about 8 s, no cut, labelled CGI/AI. It is the highest-reach evidence in this run (Maybelline 76M views; Jacquemus ~2M likes).
2. **Process + split reveal** (before-after-process, under §26): also the safe pattern for regulated brands when the object is a tool, room or product, not a body.
3. **Part-2 cliffhanger transformation** (organic only, §26): a talk-led consult, sentence captions, ends on "FOLLOW & COMMENT for part 2". Measured 24K likes / 6.5K comments. Needs an `end_card` "part 2" style (`_needs_feature`, or use end_card lines today).
4. **Post-frame restore** (before-after-fast layout): the video inside a fake social-post header. Flag for Klaus: it imitates an X/Twitter post UI. Fine for organic posts with your own handle; avoid in ads, where it can read as a platform impersonation.
5. **Mall-tenant ASMR** (§27 × §28): a mall account showing a tenant's product ASMR (Westquay × Lush). A low-cost format for mall/landlord clients.

## Engine features these presets assume (all marked `_needs_feature`)
- `reveal.wipe_split` before/after card;
- per-item speed ramps;
- `layout.post_frame`;
- `end_card` packshot and what-where-when styles;
- foley-onset cut snapping (`cut_on_onset`);
- the ASMR audio QC (`audio_qc`);
- the loop seam finder;
- a health-SG compliance block on before-after presets.

Every other key used (structure, pacing, captions, hook_text card/box/outline, zoom snap/smooth, transitions flash/dip, sfx map/cut_coverage/min_gap_s with boom/swell/ding/pop/whoosh, music, grade, broll, end_card) is listed in editor.md §2, §7, §7f.

## Flags for Klaus to judge
1. **Physio Spot and before/after:** my reading of HCSA reg 5(1)(d) is a total ban on person before/after or after-only in any Singapore-accessible ad or post, the clinic's own social accounts included. Object metaphors and process-only content look safe, but a clinic's "new treatment room" before/after should still be checked against the compliance pack.
2. **Luxury pace:** the 0.85 s median comes from two global fragrance films (big-budget coverage). For a Klaus-scale brand with fewer good shots, luxury-object-calm (3 s) may look better. Choose per brief.
3. **Engagement comparability:** mall/retailer reels have hundreds of likes. The pacing numbers are solid, but the "what performs" claims for §28 are weaker than for §26/§27.
4. **FOOH ethics:** the presets require a CGI/AI label. Klaus to confirm the house rule: label in the caption only, or also on screen.
5. **Hair "part 2" format:** withholding the reveal drives comments but can frustrate viewers. It works for organic; don't use it for paid.
6. **Measurement gaps:** no IG view counts (likes only). The hair part-2 reel (DS-lw_CEktQ) measurement did not finish. The Miss Dior repost's likes don't reflect the campaign's reach. Loudness is normalised for most reels.
7. **Kinetic Sand official vs creator:** I attribute the gap mostly to audio (-45.9 vs -17.9 LUFS). Account size and the algorithm also differ, so treat it as a strong hint, not proof.

## Sources (non-IG)
- Meta Health & Wellness ad standard: https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/ (change log Jul 22, 2026); https://www.facebook.com/business/help/2489235377779939
- TikTok weight management / body image: https://ads.tiktok.com/resources/help/article/tiktok-ads-policy-weight-management ; cosmetic surgery update Mar 2026: https://ads.tiktok.com/resources/help/article/update-to-cosmetic-surgery-na-march-2026 ; TikTok Shop health content: https://seller-us.tiktok.com/university/essay?knowledge_id=4545471832983342
- Platform matrix 2026: https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/
- SG HCS (Advertisement) Regulations 2021: https://sso.agc.gov.sg/SL/HSA2020-S1033-2021 ; MOH FAQ: https://isomer-user-content.by.gov.sg/7/a2d9019f-7617-40f1-8788-7e105b0a77e9/12-10-2023-advert-regs-faqs-%281%29.pdf ; summary: https://xaviertan.co/hcsa-advertising-guidelines/
- CCS SG false urgency enforcement, 18 May 2026: https://www.ccs.gov.sg/media-and-events/newsroom/announcements-and-media-releases/three-online-retailers-caught-using-false-urgency-tactics-and-misleading-claims-to-pressure-shoppers/ ; SCAP: https://asas.org.sg/Portals/0/SCAP%202008_1.pdf
- FOOH numbers: https://echoposter.com/en/amplification/fooh/ ; The Drum 2023-07-14: https://www.thedrum.com/opinion/fake-mascara-video-hoodwinked-the-public-it-outdoor-advertising ; Ellie Motion FOOH anatomy: https://elliemotion.com/journal/fake-out-of-home-campaigns-go-viral-the-anatomy-of-shareable-cgi-moments
- Cannes Lions 2025 Creative Effectiveness GP (Shot on iPhone): https://www.canneslions.com/news/lion-winners-announced-for-day-four-of-the-festival
- Oddly IKEA: https://www.adweek.com/brand-marketing/ikea-just-made-a-25-minute-asmr-video-and-its-one-of-the-most-satisfying-ads-ever/ ; ANA ECHO 2018: https://www.ana.net/content/show/id/pr-2018-echo-winners
- McDonald's Japan ASMR, TikTok Ad Awards Japan GP: https://ads.tiktok.com/business/creativecenter/quicktok/online/creative_wins_apac/pc/en
- Pop Mart revenue: https://www.reuters.com/business/retail-consumer/pop-mart-sees-revenue-hitting-over-4-bln-this-year-launch-mini-labubus-2025-08-20/
