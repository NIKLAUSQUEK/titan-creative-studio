# Genre research: §2 Comedy skit / deadpan, §5 POV / relatable, §6 Absurdist / meme chaos

Overnight run 2026-10-25 (agent genreA). Scope: ground, correct and extend genre-playbooks.md §2, §5 and §6 and their presets (deadpan-comedy, ugc-pov, genz-chaos). This file is a proposal; the main session merges. Nothing else in the repo was edited.

**Method.**
- Web research: Firecrawl search (rate-limited, shared), WebSearch and WebFetch. Exa was out of credits.
- Measurement: 10 public Instagram reels downloaded with yt-dlp, analysis only. Media stays in the scratchpad (`.../scratchpad/genreA/media`) and nothing was re-uploaded. Two reels hit the 429 rate limit twice and were skipped: Scott Seiss `CdRqwZyroqT` and kallmekris `ClMK0ogDCEE`.
- Tools: ffmpeg scene cuts (`scale=320:-2,select='gt(scene,0.2)'`), ebur128 loudness, 20 ms RMS-flux onsets, silence runs ≥ 0.4 s below -45 dB, and faster-whisper `small` int8 word timings. I made a 1 fps contact sheet and a 4 fps hook sheet for every reel and looked at each one.
- Caveats:
  - Instagram re-encodes every reel to about -14 LUFS, so loudness numbers describe the platform target, not the creator's mix.
  - The scene detector misses wipes and slides (duo2); those cut counts were corrected by eye from the sheets.
  - Like counts come from yt-dlp metadata or Instagram's own page title on 2026-10-25. Instagram returns no view counts without a login.

## 0. Measured reference set

| id | Link | Creator · date | Public stats | Dur | Shots (s) | Median shot | Words / wpm | Loudness | What it is |
|---|---|---|---|---|---|---|---|---|---|
| khaby1 | https://www.instagram.com/reel/DceEuVnii0u/ | @khaby00 · 2026-08-25 | 9.70 M likes, 49.7 K comments | 30.7 s | 1.6 / 4.7 / 0.7 / 2.5 / 2.9 / **18.4** | 2.7 | 0 words | -14.5 LUFS, LRA 13.8 | Over-complicated "hack" trigger clip (12.3 s, 5 shots, music onsets every ~1.14 s), then ONE locked wide of Khaby's silent fix (18.4 s) |
| khaby2 | https://www.instagram.com/reel/C5bLa77NFDa/ | @khaby00 · 2024-04-06 | 7.86 M likes, 61.8 K comments | 33.2 s | 5.7 / **27.5** | 16.6 | 1 word ("Alright.") | -11.2 LUFS, TP +3.3 | Trigger 5.7 s, then one 27.5 s take of escalating slapstick; three 0.4-0.5 s silences at 6.1 / 12.7 / 21.0 s between attempts |
| corp1 | https://www.instagram.com/reel/DNNv34yR8oE/ | @corporatenatalie · 2025-08-11 | 233 K likes, 1.47 K comments | 10.9 s | **10.9 (0 cuts)** | 10.9 | 4 words, 27 wpm | -15.0 LUFS, LRA 3.7 | Quote header ("We need you in the office to experience the company culture" / "The culture:") over ONE static wide; she walks into an empty office: "Good morning… hello? Where is everybody?" |
| pov1 | https://www.instagram.com/reel/Dd9hI51P_aw/ | @amitmizrachix · 2026-10-01 | 406 K likes, 499 comments | 30.4 s | 8.3 / 10.1 / 12.0 | 10.1 | 113 words, **223 wpm** | -14.6 LUFS, LRA 6.3 | "POV: the friend who can't show affection": 3 vignettes in 3 locations, each one locked take to the lens; the longest pause (1.72 s) comes before the punch word "Emily?" at 20.3 s (67 %) |
| pov3 | https://www.instagram.com/reel/DW9oL7zAQXW/ | @kylezhengg · 2026-04-10 | 15.5 K likes | 26.5 s | 4.8 / 8.8 / 1.7 / 9.6 / 1.6 | 4.8 | (dialogue, fast) | -14.1 LUFS | "POV: that one friend that's socially self aware": the same grammar as pov1, 3 vignettes, short reverse-angle inserts inside a vignette |
| duo1 | https://www.instagram.com/reel/DFttLM7ATju/ | @duolingo · 2025-02-06 | 253 K likes, 1.0 K comments | 16.1 s | 5.8 / 5.1 / 5.2 | 5.2 | sung track only | -14.1 LUFS | "never not annoying": a year-evolution meme with big year labels 2023 → 2024 → 2025, each a weirder Duo image, all on one song |
| duo2 | https://www.instagram.com/reel/C764VubMXTL/ | @duolingo · 2024-06-07 | 89 K likes, 2.33 K comments | 5.7 s | ~2.3 / ~3.4 (a wipe) | — | 0 | -14.2 LUFS | "rating things duo has done 🥰" (mascot suit) → "die -1000000/10 what the flip duo." (a skeleton Duo render) |
| ryan1 | https://www.instagram.com/reel/DWb_vEDDzzd/ | @ryanair · 2026-03-28 | 7.3 K likes (IG; Ryanair's scale is on TikTok) | 6.9 s | 1.6 / 1.8 / 2.5 / 1.0 | 1.7 | 0 | -14.1 LUFS | Stitch of a customer's "POV when u don't pay for seats…" clip (3.4 s) → plane-face reply with one-word caps "NICE. / NOW / FOR" → a fake fee card "Boogie Fee 49.00" (1.0 s) |
| brain1 | https://www.instagram.com/reel/DH4Mk9ORXzA/ | @fabianmosele · 2025-03-31 | 445 K likes, 1.1 K comments | 28.0 s | 4.5 / 3.5 / 2.7 / 2.3 / 1.0 / 2.8 / **11.2** | 2.7 | chanted names, 123 wpm | -14.2 LUFS, LRA 15.2 | AI "Italian brainrot" roll-call in a fake-1998-cartoon style: one character per shot with a name tag top-right, chanted name on each cut, last character held 11 s |
| brain2 | https://www.instagram.com/reel/DIM2e7JgSwW/ | @yuripomo · 2025-04-08 | 691 K likes, 1.5 K comments | 8.3 s | 2.6 / 1.5 / 4.2 | 2.6 | sound only | -14.1 LUFS | "Other people lives:" (a glossy wedding, 2 shots) → "Me:" (a phone-lit face in bed, held 4.2 s) on the Tralalero sound |

**Cross-cutting findings (what the numbers say against the current cards):**
1. **Top-performing comedy reels are NOT fast-cut.**
   - The medians are 2.7-16.6 s for deadpan, 4.8-10.1 s for POV, and 1.7-5.2 s for meme chaos.
   - The current §0 table (1.5-3 s / 1-2.5 s / 0.5-1.5 s) and the presets (`ugc-pov` max_shot 2.2, `genz-chaos` max_shot 1.8 with a punch-in every 1.5 s) are 2-5× too fast for these genres.
   - The speed lives in the **dialogue** (pov1 at 223 wpm) or the **image** (the absurd picture itself), not in the edit.
2. **The joke is carried by a persistent top header** in 7 of 10 reels: a POV line, a quote + "The culture:", "Other people lives: / Me:", year labels, "rating things…". Captions underneath are small. This is already how `genz-header-skit` works; §2/§5/§6 should reuse it.
3. **Pause before the punch.**
   - Measured: pov1's longest gap (1.72 s) sits right before the punch word; khaby2 has 0.4-0.5 s dead-air beats between escalations; corp1 holds a silent walk.
   - Researched: pauses lengthen before high-surprise punchlines, and lower body motion predicts more laughter (r = -0.75): arXiv 2603.21803, "Timing In stand-up Comedy… TIC-TALK" (2026), https://arxiv.org/abs/2603.21803, plus the related preprint https://papers.cool/arxiv/2605.00143.
   - So `remove_silence` must NOT eat the pre-punch pause.
4. **Loudness:** every measured reel sits at -14 ± 0.5 LUFS integrated (Instagram's normalisation), so deliver at -14 LUFS / ≤ -1 dBTP. LRA is high (14-20 LU) only where silence and slapstick alternate (Khaby, brainrot). That is the dynamic shape to keep for deadpan.
5. **Very short works for brand memes:** duo2 5.7 s and ryan1 6.9 s. The researched Ryanair rule is "funny, captioned, mostly under 10 seconds" (whito.co.uk / namecheap.com, below).

---

## §2. Comedy skit / deadpan: corrected card

### 2. Comedy skit / deadpan [measured: khaby1 https://www.instagram.com/reel/DceEuVnii0u/ , khaby2 https://www.instagram.com/reel/C5bLa77NFDa/ , corp1 https://www.instagram.com/reel/DNNv34yR8oE/ ; deeper rules: playbook-skit.md]
- **Why it works:** the viewer is shown the absurd premise first, so the laugh is anticipation. The deadpan performer is **still** while everything around them is ridiculous, and stillness before the punch measurably predicts laughter (TIC-TALK, r = -0.75 kinetic energy vs laughter rate). The best performers are silent or nearly so: Khaby Lame's wordless format took him to the most-followed TikTok account (142.8 M, Guinness, June 2022), because "the best way [to reach the most people] was not to speak" (CNN quote via the coverage below).
- **Pacing map (measured; 30 s):**

| Beat | Time | Shot | Sound | Measured from |
|---|---|---|---|---|
| Trigger / premise | 0-6 s (up to 12 s if it's itself funny) | the problem or the over-complicated "normal" way; can be several 1-3 s shots | its own audio/music (khaby1 onsets every ~1.14 s) | khaby1 0-12.3 s, khaby2 0-5.7 s |
| or: Quote header | 0 s → end | a persistent top header: the claim in quotes + "The reality:" label | room tone | corp1 |
| Deadpan answer | one locked wide, **10-28 s, 0 cuts** | the performer does the simple or absurd thing; escalation happens INSIDE the take | near-silence; 0.4-0.5 s dead-air beats between escalations | khaby1 18.4 s, khaby2 27.5 s, corp1 10.9 s |
| Punch | ~60-70 % of runtime | the reveal (the empty office, the obvious fix) | the longest pause right before it (0.5-1.7 s), then ONE hit or none | corp1, pov1 |
| Button | last 1-3 s | the signature gesture (the Khaby hands), a deadpan look to the lens, or a walk-off | silence or a single sting | khaby1 end, khaby2 walk-off |
| Brand turn (ads) | +3-5 s | cut to the brand world | calm VO | (studio rule) |

- **Shot grammar:**
  - A static, locked wide (full body or 3/4) at eye level; the performer occupies the centre third.
  - Cut only between "their way" and "our way", never inside the deadpan answer.
  - **No crash zoom by default:** none of the measured deadpan reels uses a zoom; the current card's "crash zoom + 0.5 s freeze" belongs to the absurdist §6, not to deadpan. Keep at most one snap zoom ×1.1 for a brand ad if Klaus wants it (a proposal B).
  - Hide the gag until the reveal (hard_rules).
- **Look:** phone-natural, flat daylight or office fluorescent, no grade tricks. The comedy comes from staging and the header.
- **Header type:** quote header in a white rounded box, sentence case, centred at y ≈ 0.07-0.10, two lines max, plus a short label line ("The culture:") in a second box (corp1). The Khaby format has no text at all.
- **genre_key (unchanged in spirit, tightened):** `naturalistic deadpan comedy, locked-off tripod wide, eye level, flat even everyday light, performer perfectly still and expressionless, no mugging, realistic skin and clothing, ordinary real location, phone-camera look`
- **Shot JSON:**
```json
{"id":"S02","dur":10,"model":"seedance_2_5","mode":"omni_reference",
 "camera":"locked tripod wide, 24mm, eye level, from behind a desk toward the office door",
 "subject":"@LEAD (office outfit, tote bag) enters through the far door",
 "action":"start: @LEAD walks in smiling, 'good morning' -> 4 s: slows, looks left and right at empty desks -> end: stops centre frame, deadpan stare toward the lens",
 "environment":"@SET_OFFICE: open-plan, every desk empty, monitors off, one yellow sticky note",
 "light":"flat overhead fluorescent, no accent light",
 "audio":"room tone, footsteps, her two lines only",
 "constraints":"no camera move, no cuts, nobody else visible anywhere in frame",
 "genre_key":"<§2 genre key>"}
```
- **Sound:**
  - Live room tone, with no music under the deadpan take (khaby1 drops its music when Khaby enters).
  - Keep the 0.4-1.7 s pause before the punch.
  - At most ONE hit on the punch: a vine-boom-style meme hit only on personal accounts, in-app; brands use an original or licensed impact.
  - Deliver at -14 LUFS.
- **Ad template:** quote header with the industry's cliché ("'Just stretch it out,' they said") / "The reality:" → one take of the deadpan truth → hard cut to the brand world.
- **Compliance:**
  - Dramatised skits never pose as patient testimony (SG health).
  - The "their way vs our way" structure must not disparage a named competitor or real person; Khaby-style trigger clips are **third-party footage**, so brand accounts recreate the trigger (format-jack, genre §31).
- **Preset:** deadpan-comedy (corrected below); new sub-presets deadpan-silent-rebuttal and quote-reality-oneshot.

**Corrected `deadpan-comedy.json`:**
```json
{
  "name": "deadpan-comedy",
  "label": "Deadpan comedy",
  "kind": "style",
  "description": "Measured 2026-10-25 (khaby00 DceEuVnii0u 9.7M likes, C5bLa77NFDa 7.9M; corporatenatalie DNNv34yR8oE 233K): a trigger/premise (0-12 s, may be several short shots) then ONE locked take of the deadpan answer (10-28 s, 0 cuts), the escalation inside the take, the longest pause right before the punch, at most one hit. Optional persistent quote header. No zooms, no music under the take, -14 LUFS.",
  "reference": "research/genre-research-2026-10/comedy-pov-absurd.md#2",
  "structure": {"name": "deadpan", "target_s": [10, 35],
    "beats": ["trigger or quote header 0-6s", "deadpan take (one shot)", "pause >=0.5s", "punch at ~65%", "button / walk-off"]},
  "pacing": {"remove_silence_over_s": 1.8, "pad_s": 0.35, "remove_fillers": "none", "max_shot_s": 30, "drop_retakes": true,
    "keep_pause_before_punch_s": 0.6, "_needs_feature": "pacing.keep_pause_before_punch_s: protect the gap before a beat marked role=punch from silence removal"},
  "captions": {"enabled": true, "animation": "static", "max_words": 6, "keyword_caps": false, "size": 0.032, "position_y": 0.62, "uppercase": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "box", "persistent": true, "position_y": 0.08, "size": 0.03, "uppercase": false, "max_words": 16},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0},
  "transitions": {"default": "none"},
  "sfx": {"density_per_10s": 0.3, "db": -12, "map": {"hook": "impact", "end": "impact"}},
  "music": {"energy": "none"},
  "grade": {"contrast": 1.0, "saturation": 1.0, "warmth": 0.0, "vignette": false},
  "end_card": {"enabled": false}
}
```
Changes vs the current preset:
- max_shot_s 8 → 30, so the one-take answer isn't chopped;
- silence removal 1.2 → 1.8 s, plus a protected pre-punch pause (`_needs_feature`);
- a persistent quote-header box (existing `hook_text.persistent` + `card_style: box`);
- the crash zoom on the hook removed;
- smaller static captions;
- no end card (none of the refs has one; the brand turn is a cut, not a card).

**3 core rules (§2):**
1. **One take for the answer.** Cut between the premise and the deadpan answer, never inside the answer; escalate inside the shot.
2. **The pause is the punchline's runway.** Keep 0.5-1.7 s of stillness and silence right before the reveal; never let silence removal eat it.
3. **The header or the trigger tells the joke; the performer never explains it.** No mugging, no music under the take, at most one hit.

**Unsure, for Klaus:**
- **Is the measured "one-take" grammar right for HIS skits?** Klaus's ledger skit entries (e.g. "BUFF BOY" reveal) may need the crash zoom; I kept it out of the default and suggest it as proposal B.
- **Brand use of the Khaby structure:** it needs a recreated trigger clip (a staged over-complicated method). Is it OK to parody generic "bad advice" in a physio context without reading as health misinformation? Compliance-check per piece.
- **khaby2 loudness:** it measured -11.2 LUFS / +3.3 dBTP (clipped by the platform). Don't copy it; target -14 / -1.

### 2a. NEW sub-style: Silent over-complication rebuttal (`deadpan-silent-rebuttal`) [measured: khaby1, khaby2]
- **What:** a "life hack" or "expert" method that is absurdly over-complicated (0-12 s) → the performer, silent, does the obvious thing in one locked take → the signature open-palm "it's that easy" gesture.
- **Why:** it's wordless, so it is language-free and works in every market. Khaby Lame built 142.8 M+ TikTok followers on it (Guinness 2022) and 7.9-9.7 M likes per IG reel in 2024-26 (measured above).
- **Brand version:** "How people think you fix a stiff neck (17-step gadget routine)" → the physio silently does one simple, safe cue → the gesture → the brand card.
  - The rebuttal must be **safe general education**, never a treatment claim.
  - Never mock a real creator's clip: recreate a generic version.
- **Preset JSON:**
```json
{"name":"deadpan-silent-rebuttal","label":"Silent over-complication rebuttal","kind":"style",
 "description":"Measured khaby00 DceEuVnii0u / C5bLa77NFDa: trigger montage 5-12 s (several 0.7-4.7 s shots, music-led), hard cut to ONE locked wide 18-28 s of the silent fix, 0.4-0.5 s dead-air beats between attempts, ends on the signature gesture. 0-1 spoken words.",
 "reference":"research/genre-research-2026-10/comedy-pov-absurd.md#2a",
 "structure":{"name":"rebuttal","target_s":[20,35],"beats":["trigger (their way)","hard cut","silent fix one take","gesture button"]},
 "pacing":{"remove_silence_over_s":99,"pad_s":0.0,"remove_fillers":"none","max_shot_s":30,"drop_retakes":true},
 "captions":{"enabled":false},
 "hook_text":{"enabled":false},
 "zoom":{"mode":"snap","every_s":0,"scale":1.0,"on_hook":1.0,"on_emphasis":false},
 "broll":{"every_s":0,"mode":"split","_needs_feature":"optional duet layout (trigger top, performer bottom) for the reaction variant"},
 "sfx":{"density_per_10s":0.0},
 "music":{"energy":"mid","db":-16,"duck":false,"stop_at_beat":"fix","_needs_feature":"music.stop_at_beat: hard-stop the bed when the beat with role=fix starts"},
 "grade":{"contrast":1.0,"saturation":1.0},
 "end_card":{"enabled":false}}
```

### 2b. NEW sub-style: Quote vs reality, one shot (`quote-reality-oneshot`) [measured: corp1; also brain2 "Other people lives: / Me:"]
- **What:** a persistent two-part header: the quote or claim ("We need you in the office to experience the company culture"), then the label ("The culture:"). Under it, ONE static take that contradicts it. 8-12 s.
- **Measured:** corp1 is 10.9 s, 0 cuts, 4 words. brain2 is 8.3 s: "Other people lives:" for 2.6 s, then "Me:" held for 4.2 s.
- **Brand use:** corporate satire (TITAN.AI: "'AI will do it all for you' / The AI:"); for SG health, "'Just rest it' / Your desk setup:" (no outcome claims).
- **Preset JSON:**
```json
{"name":"quote-reality-oneshot","label":"Quote vs reality (one shot)","kind":"style",
 "description":"Measured corporatenatalie DNNv34yR8oE (233K likes, 10.9 s, 0 cuts, 4 words) and yuripomo DIM2e7JgSwW (691K, 8.3 s): a persistent white-box quote header + label line, one static take that contradicts it, sparse live lines as small captions, no music or the trend sound in-app.",
 "reference":"research/genre-research-2026-10/comedy-pov-absurd.md#2b",
 "structure":{"name":"quote-reality","target_s":[7,14],"beats":["quote + label header (persistent)","contradicting take","deadpan line or hold"]},
 "pacing":{"remove_silence_over_s":99,"pad_s":0.0,"remove_fillers":"none","max_shot_s":15},
 "hook_text":{"enabled":true,"renderer":"card","card_style":"box","persistent":true,"position_y":0.08,"size":0.026,"uppercase":false,"max_words":18,
   "second_line_box":true,"_needs_feature":"hook_text.second_line_box: render the label line ('The culture:') as its own smaller box under the quote"},
 "captions":{"enabled":true,"animation":"static","max_words":4,"size":0.028,"position_y":0.55,"uppercase":false},
 "zoom":{"every_s":0,"on_hook":1.0,"on_emphasis":false},
 "sfx":{"density_per_10s":0.0},
 "music":{"energy":"none"},
 "end_card":{"enabled":false}}
```

---

## §5. POV / relatable: corrected card

### 5. POV / relatable [measured: pov1 https://www.instagram.com/reel/Dd9hI51P_aw/ (406 K likes), pov3 https://www.instagram.com/reel/DW9oL7zAQXW/ ; brand stitch ryan1 https://www.instagram.com/reel/DWb_vEDDzzd/]
- **Why it works:** the camera IS the viewer ("POV: the friend who…"), so every line lands as if said to you. The hook is not "funny", it is **recognised**: a specific social type everyone has met (async.com reels-format guide; contentstudio / brandwatch POV glossaries). Three escalating examples of the same trait turn recognition into a laugh, and the last one is the punch.
- **Pacing map (measured; 25-30 s):**

| Beat | Time | Shot | Text | Sound | Measured |
|---|---|---|---|---|---|
| Header | 0 s → end | — | **persistent** "POV: the friend who …" top, y ≈ 0.06-0.10, white with a black outline, 1-2 lines | — | pov1, pov3 |
| Vignette 1 (establish the trait) | 0-8 s | one locked handheld/tripod mid-full shot, actor talking into the lens; location A | small centred subtitles on the chest, y ≈ 0.35-0.40 | live dialogue, first word at 0.0 s | pov1 8.3 s, pov3 4.8 s |
| Vignette 2 (bigger) | 8-18 s | new location B, same framing | subs | dialogue at 200-225 wpm | pov1 10.1 s, pov3 8.8 s |
| Vignette 3 (the punch) | 18-30 s | location C; the punch word comes after the longest pause (pov1: 1.72 s gap → "Emily?" at 67 % of runtime) | subs | the pause, then the line | pov1 12.0 s, pov3 9.6 s |
| Button | last 2 s | the actor's last petty line, no CTA card | — | — | pov1 "give me your phone, I'm gonna change it" |

- **Shot grammar:**
  - Lens = the viewer: the actor looks straight into the lens, eye level, a mid-full or medium shot.
  - One take per vignette; a vignette may include a 1.5 s reverse or insert (pov3).
  - Change the **location** per vignette (it signals "another time this happened"). No zooms; outdoor daylight, car, hallway.
  - The off-camera "you" is either silent or voiced off-screen. Klaus to confirm which he wants; pov1's transcript contains both sides.
- **Look:** phone-natural, bright daylight; wardrobe stays the same across vignettes (continuity = "same friend").
- **genre_key:** `first-person point of view, the camera is the viewer, subject talks and reacts directly into the lens at eye level, medium shot, natural phone-camera daylight, everyday real locations, candid relatable performance, no camera movement`
- **Shot JSON:**
```json
{"id":"S03","dur":10,"model":"seedance_2_5","mode":"omni_reference",
 "camera":"handheld-steady medium shot at eye level, 26mm phone lens, subject looks straight into the lens as if at the viewer",
 "subject":"@LEAD (same white tee and denim as S01-S02) in a parked car passenger seat, phone in hand",
 "action":"start: scrolls her phone, asks 'wait, what do you have me saved as?' -> 2 s pause, she reads it, flat face -> end: deadpan look up into the lens",
 "environment":"@SET_CAR interior, daylight through the windscreen",
 "light":"soft natural daylight, no grade",
 "audio":"car interior room tone, her dialogue only",
 "constraints":"no cuts, same wardrobe as earlier shots, keep the phone screen unreadable",
 "genre_key":"<§5 genre key>"}
```
- **Sound:**
  - Dialogue-led and fast (pov1: 223 wpm); NOT trend-music-led as the old card said.
  - No music bed under dialogue POV. The trend sound only for silent POV variants, on personal accounts in-app.
  - One sting max, on the punch, or none (both refs have none). Deliver at -14 LUFS.
- **Ad template (corrected):** "POV: the friend who [has the problem the brand solves]" → 3 vignettes escalating the trait → the 3rd vignette's punch is the brand-relevant moment → a short tag line in the caption, not on screen.
  - **Brand-reply variant (ryan1):** Stitch/Remix a customer's POV clip (where the platform permits it) and reply in-character in ≤ 7 s.
- **Compliance:**
  - SG health: a POV skit about a "type" is fine; the "friend" must not be a patient, no outcome or cure lines, no "my physio fixed me".
  - Stitch replies only use the platform's own Stitch/Remix, with the original enabled (§31 rights rules).
- **Preset:** ugc-pov (corrected below).

**Corrected `ugc-pov.json`:**
```json
{
  "name": "ugc-pov",
  "label": "UGC: POV (three vignettes)",
  "kind": "ugc",
  "description": "Measured 2026-10-25 (amitmizrachix Dd9hI51P_aw 406K likes, kylezhengg DW9oL7zAQXW): a persistent 'POV: the friend who…' header the whole video, 3 vignettes in 3 locations, each one locked take to the lens (5-12 s), dialogue at ~200-225 wpm with small centred subtitles, the longest pause before the punch in vignette 3 (~65% of runtime), no music under dialogue, no zooms, no end card.",
  "reference": "research/genre-research-2026-10/comedy-pov-absurd.md#5",
  "structure": {
    "name": "pov",
    "target_s": [15, 32],
    "beats": ["POV header (persistent)", "vignette 1: establish the trait", "vignette 2: bigger", "vignette 3: pause -> punch", "petty button"]
  },
  "pacing": {"remove_silence_over_s": 0.6, "pad_s": 0.1, "remove_fillers": "hard", "max_shot_s": 12.5,
    "keep_pause_before_punch_s": 0.8, "_needs_feature": "pacing.keep_pause_before_punch_s"},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "outline", "persistent": true, "position_y": 0.08, "size": 0.032, "uppercase": false, "max_words": 12},
  "captions": {"enabled": true, "animation": "static", "max_words": 5, "size": 0.026, "position_y": 0.38, "uppercase": false, "keyword_caps": false},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0.0},
  "music": {"energy": "none"},
  "grade": {"contrast": 1.02, "saturation": 1.04},
  "end_card": {"enabled": false}
}
```
Changes vs the current preset:
- max_shot 2.2 → 12.5;
- SFX 1.5/10 s → 0;
- music high → none;
- the 3 s hook text becomes a persistent header;
- small static subtitles at y 0.38;
- a 3-vignette structure.

**3 core rules (§5):**
1. **A header names a TYPE, not a situation.** "POV: the friend who can't show affection" beats "POV: you're at lunch". It stays on screen the whole time.
2. **Three vignettes, three locations, one locked take each, looking into the lens.** Escalate the same trait; the third has the punch.
3. **Dialogue is the speed.** ~200+ wpm and no music bed, but the one long pause (≈ 1-1.7 s) sits right before the punch line.

**Unsure, for Klaus:**
- **Who voices "you"?** pov1's transcript includes the other side's lines (an off-camera voice or the creator dubbing). For brand POVs, is a silent "you" (actor reacts to unheard lines, captions show them) preferred? It reads better for SG compliance (no second fake person).
- **Both POV refs are personal-creator accounts.** I found no high-like *brand* POV skit on IG; the brand evidence is Ryanair's Stitch replies (TikTok-scale; only 7.3 K likes on IG). Treat brand POV performance as unproven on IG.
- **Silent music-led POVs** (a one-line POV over a trend sound, e.g. ryan1's customer clip) are a different format. If Klaus wants that, use silent-loop-reaction or the brand-reply preset (§6a) rather than ugc-pov.

---

## §6. Absurdist / meme chaos: corrected card

### 6. Absurdist / meme chaos [measured: duo1 https://www.instagram.com/reel/DFttLM7ATju/ , duo2 https://www.instagram.com/reel/C764VubMXTL/ , ryan1 https://www.instagram.com/reel/DWb_vEDDzzd/ , brain1 https://www.instagram.com/reel/DH4Mk9ORXzA/ , brain2 https://www.instagram.com/reel/DIM2e7JgSwW/]
- **Why it works:** an escalating non-sequitur, with the brand or mascot as an unhinged character that "shouldn't" behave this way.
  - The chaos lives in the **picture and the text**, not in cut speed: measured medians are 1.7-5.2 s and the brand memes are 5.7-16 s long.
  - Researched brand evidence:
    - Duolingo grew from 50 K TikTok followers (Sept 2021) to ~16-17 M by 2025 with the "unhinged" owl (The Drum 2025-02-25; Contagious; digitalsummit speaker bio for Zaria Parvez). Its first owl video got ~800 K views, 3× its previous best, and the next 3.5 M (marketingmag.com.au). Parvez: "anything over a million views, we'll see an uptick in users" (Marketplace 2022-01-17).
    - Ryanair's TikTok has ~2.9 M followers (Social Blade), built on the plane-face filter, self-deprecation, trend speed over polish, "mostly under 10 seconds", and snark aimed at itself, never at customers in distress (namecheap / whito / Travel Weekly; head of social Michael Corcoran).
- **Pacing map (measured; three shapes, pick one):**

| Shape | Length | Grammar | Measured |
|---|---|---|---|
| A. Meme reply (brand) | 5-8 s | a customer/trend clip or setup line (2-3.5 s) → the mascot's in-character reply, one-word CAPS captions per beat ("NICE. / NOW / FOR") → a fake product card punch (1.0 s) | ryan1: 1.6 / 1.8 / 2.5 / 1.0 s |
| B. Label escalation | 6-16 s | 2-3 shots, each with a big label (years, ratings, "Other people: / Me:"), each image weirder; the final image is the most absurd and held | duo1: 3 × ~5.3 s; duo2: ~2.3 / 3.4 s; brain2: 2.6 / 1.5 / 4.2 s |
| C. Roll-call / lore parade | 20-30 s | one absurd character per shot (1-4.5 s) with a name tag top-right, a name chanted on each cut, the last character held 8-11 s | brain1: median 2.7 s, last hold 11.2 s |

- **Shot grammar:**
  - Centred single subject, frontal, filling the frame (plane face, owl, creature).
  - A hard cut or a quick wipe between beats. Crash zoom / Dutch angle are optional accents, not the base grammar: they appear in none of the 5 measured reels.
  - End on the most absurd image and either hard-cut (A) or hold (B, C).
- **Look:** saturated and clean for brand mascots; or a consistent "found media" style (a fake-1998-cartoon in brain1, a cheap 2000s clip-art collage in duo1). The style consistency is what makes the nonsense read as a world.
- **Text:**
  - Shape A: one word at a time, white heavy-sans caps with a black outline, centred at y ≈ 0.62.
  - Shape B: big labels (years) at the bottom (y ≈ 0.72) or a small sentence header top.
  - Shape C: a small name tag top-right.
- **genre_key:** `absurdist meme comedy, single bizarre subject centred and frontal filling the frame, saturated clean colours, deadpan straight-faced presentation of an impossible situation, consistent illustration style across shots, no extra text in frame`
- **Shot JSON:**
```json
{"id":"S02","dur":2.5,"model":"seedance_2_5","mode":"omni_reference",
 "camera":"locked frontal close-up, centred, eye level with the subject's face",
 "subject":"@MASCOT (brand-original character from the asset bible) stares into the lens",
 "action":"start: neutral stare -> 1 s: slow exaggerated smile spreads -> end: holds the too-wide smile, unblinking",
 "environment":"plain bright brand-colour backdrop",
 "light":"flat bright key, no shadows",
 "audio":"none (the edit adds the beat)",
 "constraints":"same mascot design as the sheet, no text in frame, no real-person likeness",
 "genre_key":"<§6 genre key>"}
```
- **Sound:**
  - The track or trend sound IS the rhythm (all 5 refs are music- or sound-led, 0-1 spoken lines). Cut on its onsets; one hit on the final image.
  - The old "stim every 1.5 s" rule is not supported by the refs (none uses SFX stacks); keep it only for the genz-chaos *talking* edit.
  - Brands: licensed or original sound only. A trend sound only on personal accounts, in-app.
- **Ad template:** shape A as a reply to a real comment or trend (the brand mocks itself, e.g. a fake "Boogie Fee") or shape B "rating things [brand] did".
- **Compliance:**
  - Self-deprecation only; never punch down at customers, patients or real people (Ryanair's own boundary, whito.co.uk).
  - No fake fees or prices that could be read as real offers: label them clearly as jokes, and never add an inducement in SG health.
  - Brainrot-style characters must be original (no lookalikes of existing IP or real people; Gate 4).
  - Kids' audiences: the Italian-brainrot wave drew parent-safety coverage (Instagram DJWSQ2yCRl_), so avoid violent or slur-laden "lore".
- **Preset:** genz-chaos stays for the *talking-head chaos edit* (archetype #6). New preset meme-chaos-short for this card (below); plus brand-meme-reply (6a) and lore-rollcall (6b).

**New `meme-chaos-short.json` (the default for §6; genz-chaos stays as is):**
```json
{
  "name": "meme-chaos-short",
  "label": "Absurdist meme (label escalation, 6-16 s)",
  "kind": "style",
  "description": "Measured 2026-10-25 (duolingo DFttLM7ATju 253K, C764VubMXTL 89K; yuripomo DIM2e7JgSwW 691K): 2-3 shots of 1.5-5.8 s, each with a big label, each image more absurd, sound-led (no VO, no SFX stack), last image held, hard end, no end card. -14 LUFS.",
  "reference": "research/genre-research-2026-10/comedy-pov-absurd.md#6",
  "structure": {"name": "meme-escalation", "target_s": [5, 16], "beats": ["label 1 + image", "label 2 + weirder image", "label 3 + most absurd image (hold)"]},
  "pacing": {"remove_silence_over_s": 99, "pad_s": 0.0, "remove_fillers": "none", "max_shot_s": 6.0},
  "captions": {"enabled": false},
  "labels": {"style": "outline", "font": "Archivo Black", "size": 0.06, "position_y": 0.72, "uppercase": true, "_needs_feature": "labels.style/font/position per beat (beat 'label' exists; styling keys not yet)"},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "outline", "persistent": true, "position_y": 0.1, "size": 0.026, "uppercase": false, "max_words": 8},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0},
  "beat_sync": true,
  "transitions": {"default": "none"},
  "sfx": {"density_per_10s": 0.5, "db": -12, "map": {"end": "impact"}},
  "music": {"energy": "high", "db": -14, "duck": false},
  "grade": {"contrast": 1.06, "saturation": 1.15},
  "end_card": {"enabled": false}
}
```
**`genz-chaos.json` correction (small):** the description claims "[measured]" in style-archetypes #6, but no reel in this run supports a punch-in every 1.5 s or 4 SFX per 10 s for *meme* content. Keep the preset for a fast talking-head edit only, and relabel it in §0 row 6 → meme-chaos-short. If Klaus wants it calmer: `zoom.every_s` 1.5 → 3.0 and `sfx.density_per_10s` 4 → 2. **Flag for Klaus: I did not measure a talking-head chaos reel, so I'm not changing genz-chaos numbers myself.**

**3 core rules (§6):**
1. **Chaos is in the image, not the cut.** One bizarre, centred, frontal subject per shot, held long enough to read (1.5-5 s); the last, most absurd image gets the longest hold.
2. **Label every beat.** A year, rating, "Me:", a name tag or a one-word caps line: the label turns nonsense into a pattern the viewer can follow.
3. **The brand mocks itself, fast and short.** 5-16 s, sound-led, a reply to something the audience already said, never punching down.

**Unsure, for Klaus:**
- **Is "brainrot" style on-brand for any of his brands?** It is huge (445-691 K likes on single reels) but polarising, with child-safety press. I'd keep it to TITAN.AI or personal accounts.
- **Fake product cards** ("Boogie Fee 49.00") are a strong punch for Power Protein / PeachForm, but a fake price can read as an advertised price; it needs a "joke" signal. Not for SG health at all.
- **Plane-face-style "mascot face" effects need a mascot.** Which brands have one? A Gate 4 character-design job may come first (character-design.md).

### 6a. NEW sub-style: Brand meme reply (`brand-meme-reply`) [measured: ryan1]
- **Format:** platform Stitch/Remix of a customer or trend clip (≤ 3.5 s) → the brand mascot/face replies in-character (one word per caption beat) → a 1 s fake-card or product punch. 5-8 s in total.
- **Researched:** Ryanair reports 111 M organic impressions in a month from low-fi memes and reactive posts (podcast summary via WebSearch; unverified). The team posts within days of a trend, and speed beats polish.
```json
{"name":"brand-meme-reply","label":"Brand meme reply (Stitch + mascot)","kind":"style",
 "description":"Measured ryanair DWb_vEDDzzd (6.9 s, shots 1.6/1.8/2.5/1.0): platform Stitch of a customer clip, mascot-face reply with one-word white caps outline captions, 1 s fake product card punch, no end card. Brand self-deprecation only.",
 "reference":"research/genre-research-2026-10/comedy-pov-absurd.md#6a",
 "structure":{"name":"reply","target_s":[5,9],"beats":["their clip (platform Stitch only)","mascot reply word by word","1 s punch card"]},
 "pacing":{"remove_silence_over_s":99,"max_shot_s":3.0,"remove_fillers":"none"},
 "captions":{"enabled":true,"max_words":1,"uppercase":true,"font":"Archivo Black","size":0.06,"outline":7,"position_y":0.62,"animation":"pop"},
 "hook_text":{"enabled":false},
 "zoom":{"every_s":0,"on_hook":1.0},
 "broll":{"kind":"motion","template":"kinetic-quote","_needs_feature":"a 'fake-card' motion template (product/fee card pop-in, 1 s)"},
 "sfx":{"density_per_10s":1.5,"db":-12,"map":{"broll":"pop","end":"impact"}},
 "music":{"energy":"high","db":-14,"duck":false},
 "end_card":{"enabled":false}}
```
Rights: the opening clip comes in only through the platform's Stitch/Remix, or with written permission (genre §31). Never downloaded and re-uploaded.

### 6b. NEW sub-style: Lore roll-call / character parade (`lore-rollcall`) [measured: brain1]
- **Format:** 5-8 original AI characters, one per shot (1-4.5 s, median 2.7 s), each with a name tag top-right and a chanted name; the final character is held 8-11 s while the chant loops.
- **Why:** each character is a collectible and a comment prompt ("which one are you?"). It fits a studio that already builds character sheets (Gate 4).
- **Brand use:** TITAN.AI "meet the agents" or a Power Protein flavour-creature roster, built from original characters only.
- **genre_key for the set:** `vintage 1990s cel-animated TV cartoon look, warm sunlit forest background, one hybrid creature centred full body, soft film grain, consistent character design style across shots, no text`
```json
{"name":"lore-rollcall","label":"Lore roll-call (character parade)","kind":"style",
 "description":"Measured fabianmosele DH4Mk9ORXzA (445K likes, 28 s, 7 shots median 2.7 s, last hold 11.2 s, chanted names ~123 wpm): one original character per shot with a small name tag top-right, a cut on each new name, final character held, no end card.",
 "reference":"research/genre-research-2026-10/comedy-pov-absurd.md#6b",
 "structure":{"name":"rollcall","target_s":[18,30],"beats":["character 1..N (1-4.5 s each)","final character hold 8-11 s"]},
 "pacing":{"remove_silence_over_s":99,"max_shot_s":12,"remove_fillers":"none"},
 "captions":{"enabled":false},
 "labels":{"position":"top_right","size":0.022,"style":"plain","_needs_feature":"labels.position top_right + per-beat name tag"},
 "hook_text":{"enabled":false},
 "zoom":{"mode":"smooth","every_s":0,"scale":1.03},
 "beat_sync":true,
 "sfx":{"density_per_10s":0.0},
 "music":{"energy":"mid","db":-14,"duck":false},
 "end_card":{"enabled":false}}
```

---

## Proposed §0 picker rows (replace rows 2, 5, 6)
| # | Genre | Use when the script is… | Feeling | Avg shot | Pace curve | Grade | Sound | Editor preset |
|---|---|---|---|---|---|---|---|---|
| 2 | Comedy skit / deadpan | a joke with a reveal; "their way vs the obvious way"; quote vs reality | anticipation → laugh | premise 1-5 s, then ONE 10-28 s take | premise → still take → pause → punch at ~65 % | natural / brand | room tone, no music under the take, ≤ 1 hit | deadpan-comedy (+ deadpan-silent-rebuttal, quote-reality-oneshot) |
| 5 | POV / relatable | "POV: the friend who…", a recognisable type | recognition | 5-12 s per vignette | 3 vignettes, escalating; pause before the punch | phone-natural | dialogue-led (~200+ wpm), no bed | ugc-pov |
| 6 | Absurdist / meme chaos | brand self-mockery, escalating nonsense, mascot lore | shock-laugh | 1.5-5 s (memes 5-16 s in total) | label escalation → hold the most absurd image | saturated, one consistent style | the sound/track is the rhythm, one hit at the end | meme-chaos-short (+ brand-meme-reply, lore-rollcall); genz-chaos for chaos talking-head edits |

## Engine features this research asks for (all marked `_needs_feature` above)
1. `pacing.keep_pause_before_punch_s`: protect the gap before a beat with role=punch from silence removal (§2, §5).
2. `music.stop_at_beat`: hard-stop the bed at a named beat (§2a).
3. `hook_text.second_line_box`: a quote box + label box header (§2b).
4. `labels` styling (font, size, position incl. top_right) per beat (§6, §6b).
5. A fake product/fee card motion template, 1 s (§6a).

## Sources (researched, not measured)
- **Khaby Lame:**
  - Guinness World Records, 2022-06: most-followed TikTok, 142.8 M. https://www.guinnessworldrecords.com/news/2022/6/khaby-lame-overtakes-charli-damelio-as-most-followed-person-on-tiktok-708392
  - Business Insider, 2021-07 (updated 2022-06): deadpan reaction format. https://www.businessinsider.com/khaby-lame-tiktok-most-popular-creator-charli-damelio-2021-7
- **Comedic timing:**
  - TIC-TALK (CHum 2026, arXiv 2603.21803): kinetic energy vs laughter r = -0.75. https://arxiv.org/abs/2603.21803
  - Pause lengthening before punchlines, 828 Chinese stand-up performances (preprint). https://papers.cool/arxiv/2605.00143
- **Duolingo:**
  - The Drum 2025-02-25 (50 K → 16 M+ followers). https://www.thedrum.com/news/2025/02/25/duolingo-s-tiktok-mastermind-its-unhinged-social-strategy-and-killing-its-mascot
  - marketingmag.com.au (first owl video ~800 K views, next 3.5 M). https://www.marketingmag.com.au/news/duolingo-gets-massive-tiktok-following-thanks-to-passive-aggressive-owl/
  - Marketplace 2022-01-17 (>1 M views → user uptick). https://www.marketplace.org/story/2022/01/17/the-creative-force-behind-a-viral-corporate-tiktok-account
  - Contagious. https://www.contagious.com/news-and-views/duolingo-social-media-marketing
- **Ryanair:**
  - Social Blade (~2.9 M TikTok followers). https://socialblade.com/tiktok/user/ryanair
  - Travel Weekly (Michael Corcoran quote). https://www.travelweekly.com.au/article/ryanair-has-overseas-fans-desperate-to-fly-with-it-after-blowing-up-on-tik-tok/
  - Skift 2024-03-22. https://skift.com/2024/03/22/ryanair-ceo-shares-social-media-strategy/
  - namecheap "Mastering the short video: Ryanair & Duolingo". https://namecheap.com/blog/mastering-the-short-video-ryanair-duolingo
  - CBS thesis on memetic marketing (six meme categories). https://research.cbs.dk/en/studentProjects/the-strategic-use-of-memetic-marketing-as-a-communication-tool-to/
  - The 111 M impressions/month figure comes from a podcast summary surfaced by WebSearch and is unverified.
- **POV format:**
  - async.com "5 Instagram Reels formats to try in 2026". https://async.com/blog/instagram-reels-formats/
  - Brandwatch POV glossary. https://brandwatch.com/social-media-glossary/pov-video
- **Scott Seiss (deadpan retail, not measured, download blocked):**
  - IG "At this job, we're a family." 1 M likes, 2022-05-07. https://www.instagram.com/reel/CdRqwZyroqT/
  - TikTok book post, 666.9 K likes. https://www.tiktok.com/@scottseiss/video/7412039965250424094
