# Genre research, Oct 2026: Drama / Mystery / Thriller / Romance (§7, §14, §13, §10)

Overnight run of 2026-10-25. It grounds, corrects and extends four [draft] modules of `.claude/skills/higgsfield-creative-director/references/genre-playbooks.md` with real examples. It also proposes two new sub-styles: **§7a micro-drama episode** and **§10a slow-burn texting romance**.

**Klaus approves before anything moves into the playbook or the presets.** This file does not edit genre-playbooks.md, the presets, or any other repo file.

## Method (read before trusting a number)
- **Downloads:** public Instagram reels only, via yt-dlp. There were no logins or cookies, and no workarounds for YouTube, TikTok or Vimeo. Media stays in the scratchpad (`.../scratchpad/genreE/dl/`), never in the repo. Like and comment counts come from the yt-dlp info JSON on 2026-10-25 (IG hides views).
- **What was measured locally:**
  - **Cuts:** ffmpeg scene detection, `select='gt(scene,0.2)'` on a 320 px proxy. Handheld whip-pans and flashes can add false cuts, and a static two-shot can hide a real one, so read the median before the mean.
  - **Loudness:** `ebur128` (integrated LUFS, LRA, true peak).
  - **Audio hits:** spectral-flux onsets (median + 3σ, 0.3 s minimum gap). This counts SFX, door slams, music hits and hard consonants alike, so treat it as "busy-ness", not as an SFX count.
  - **Words per minute:** faster-whisper `small` int8.
  - **Silences:** stretches ≥ 0.5 s below -45 dBFS.
- **Window:** the first 120 s of each reel (the ASR window is ≤ 90 s). The shared container was at load 15-27, so long episodes were cut down to fit the time limit.
- **Frame sheets:** 1 fps (or keyframe) contact sheets were made and LOOKED at for every reel quoted below.
- **Tags:** [measured] = at least one example measured here. [researched] = web sources only.

## Evidence table
| ID | Module | Reel / source | Creator · date | Public signal | Measured (first ≤120 s) |
|---|---|---|---|---|---|
| d6 | §7 drama | https://www.instagram.com/reel/Da9ltsbPQAf/ "Girl Finds Out Whole Life's A REALITY SHOW" | @dharmannstudios · 2026-07-19 | **238,298 likes**, 178 comments | 89.5 s · 30 cuts · avg 2.9 s / **median 1.5 s** · cuts by thirds 17 / 11 / 2 · **first word 0.11 s** · **137 wpm** · no silence ≥ 0.5 s · -14.3 LUFS, LRA 4.9, TP -0.3 |
| d4 | §7 drama | https://www.instagram.com/reel/DU7YHpGD2Rr/ "Model Fired For Being Too Short" | @dharmannstudios · 2026-02-19 | 3,316 likes | see "late results" below |
| d3 | §7 drama (clip-account repost of a TV drama) | https://www.instagram.com/reel/DVM_VTjlKMH/ "The Slap – Part 1" | @reelshufflex · 2026-02-26 | 4,854 likes, 64 comments | 49.6 s · 32 cuts · avg 1.5 s / **median 1.17 s** · thirds **7 / 12 / 13** (accelerates into the hit) · 43 wpm (action, not talk) · silences 1.0 s and 1.3 s right after the violence · -14.3 LUFS, LRA 11.3 |
| d1 | §7a micro-drama | https://www.instagram.com/reel/Ddt9waGtvbS/ "Episode 2 of FAME" | @tales_of_abena · 2026-09-25 | 3,366 likes, 78 comments | 278.7 s episode (see late results) |
| d7 | §7a micro-drama | https://www.instagram.com/reel/DZCnMOLjhWL/ "Your Love Broke My Heart" | @reelshortapp · 2026-06-01 | 2,239 likes | see late results |
| d2 | §7a (parody signal) | https://www.instagram.com/reel/DVqMjhFEaQs/ "reacting to low budget short form dramas pt 15" | @amandalpaca · 2026-03-09 | **10,169 likes**, 80 comments | reaction PIP over micro-drama clips (sheet viewed) |
| r1 | §10 romance (micro-drama) | https://www.instagram.com/reel/DewJSY9AquY/ "Irresistible Young Love, Episode 1" | @iqiyi.shortdrama · 2026-10-21 | 1,534 likes | 284 s (see late results); sheet viewed |
| r4 | §10a texting romance | https://www.instagram.com/reel/C8MfUipINoB/ "Scenes From a Love Story – Ep 2" | @molshriii (with @dearmol) · 2024-06-14 | 1,260 likes | see late results; sheet viewed |
| r6 | §10 romance | https://www.instagram.com/reel/DCWDXxsMURB/ ReelShort "EP 1" | @reelshortapp · 2024-11-14 | 661 likes | see late results |
| t2 | §13 thriller / heist (studio promo) | https://www.instagram.com/reel/DUJOUnrj2cU/ "Crime 101 – the rules of the heist" | @crime101film · 2026-01-30 | 641 likes | 49.0 s · 38 cuts · avg 1.26 s / **median 0.83 s** · thirds 10 / 14 / 14 · 142 wpm · no silence · -14.1 LUFS, **LRA 3.8** (wall-to-wall) |
| t4 | §13 heist (comedy) | https://www.instagram.com/reel/Csyv74MAu-e/ "The heist (short film)" | @alloramomo · 2023-05-28 | 3,442 likes | see late results |
| t3 | §13 heist (AI film) | https://www.instagram.com/reel/DD5hcfgSTxB/ "The Heist", dir. Jason Zada, all text-to-video | @secret____level · 2024-12-22 | 430 likes, 39 comments | see late results |
| t1 | §13 heist (AI, 38 s) | https://www.instagram.com/reel/DbIx9btvZ5v/ | @wonderlustt36 · 2026-07-23 | 3 likes (control: AI heist with no audience) | see late results |
| m2 | §14 mystery | https://www.instagram.com/reel/Dc-RntLBfcK/ "The Lampshade Evidence" (micro-fiction) | @_chillexplore · 2026-09-07 | 352 likes | see late results |
| m5 | §14 mystery puzzle | https://www.instagram.com/reel/DbYOd-HD7E3/ "man found dead… spot the contradiction" | @namanjain_sleuths · 2026-07-29 | 81 likes, **78 comments** (comment ratio ≈ 1:1, the puzzle format pulls answers) | see late results |
| R1 | §7a / §13 | Issa Rae / Hoorae "Screen Time" (TikTok + PineDrama, ~1-min episodes, thriller) | nofilmschool.com/issa-rae-vertical (2026-05-27) | **~75 M views in week 1; Ep 1 26 M views, 840 K likes**; final Act 1 episodes still 2-3 M each; 55 episodes | researched |
| R2 | §7a | Crocs "Charmed to Meet You" (ReelShort, 5 eps, 45 s-2 min), "nearly 10 M views", sequel; "Déjà Shoe" 7-part shoppable TikTok series | marketingdive.com; ypulse.com (2026-02-19); easternprogress.com | ~10 M views (Marketing Dive) | researched |
| R3 | §10 | ReelShort "The Double Life of My Billionaire Husband": 419 M+ views; 75 % female audience (company figure) | rollingstone / AOL profile of ReelShort | 419 M views | researched |
| R4 | §7 | Dhar Mann Studios: 60 B cross-platform views (WNYC); format = unfair treatment → turning point → reversal/lesson | wnyc.org/story/dhar-mann-studios-dhar-mann | 60 B views | researched |
| R5 | §7a | SocialPeta 2026 short-drama ranking: darker revenge + family-search themes overtaking sweet romance; ads end on a freeze-frame cliffhanger to drive the install | socialpeta.com/blog/Short-Drama-Weekly-Ranking:Family-Search-Revenge-Romance-Soars | ranking | researched |

**Engagement caveat:** IG likes are not views. Most micro-drama pages on IG are clip funnels for apps, so their like counts sit far below their TikTok numbers. The strongest *measured* example is d6 (238 K likes). The strongest *researched* example is "Screen Time" (26 M views on Ep 1).

## Cross-module findings (what changed vs the drafts)
1. **The drafts are too slow for vertical drama.** Every high-signal drama/thriller reel measured here cuts at a **0.8-1.5 s median**, not 2-4 s.
   - d6 Dhar Mann: 1.5 s. d3 The Slap: 1.17 s. t2 Crime 101: 0.83 s.
   - The long holds are rare and deliberate. One of them is the aftermath/evidence beat: d6 holds a single two-shot for ~30 s while the evidence plays out on a laptop.
   - **Correction:** "avg shot 2-4 s" becomes **median 1-1.5 s in the conflict, with ≤ 2 held beats of 4-8 s (the aftermath, the evidence)**.
2. **Dialogue starts in the first frame.** d6's first word is at 0.11 s, t2's at 0.0 s. The hook is the conflict line itself, mid-scene: "Sophie?! Get in this house NOW!" Nobody sets the scene first.
3. **Talk density is high.** 137-142 wpm for dialogue-led drama and promo, roughly talking-head pace. Action drama (d3) drops to ~43 wpm because the shots carry it.
4. **Loudness:** everything sits at ≈ -14 LUFS integrated.
   - Dialogue drama and promo are compressed: LRA 3.8-4.9 and **no silences**.
   - Only the action drama keeps dynamics (LRA 11.3), with 1.0-1.3 s silences *right after* the violent beat. That confirms the "cold sound after cruelty" rule with real numbers.
5. **The vertical drama "frame" is a format, not an accident** (d6, the strongest example, sheet viewed):
   - the 16:9-ish picture sits inside a **white 9:16 frame**;
   - a **one-line persistent header** sits above it in black text plus one emoji ("Her parents couldn't trust her 😑");
   - **bold condensed ALL-CAPS captions** (Anton/Bebas-like) are burned low in the picture;
   - the brand bug sits top-left inside the picture.

   d3 uses the same header grammar with black bars and a POV header ("Me in future. If I ever had a daughter 😭"). The editor has no frame/letterbox layout yet (`_needs_feature`).
6. **Evidence inserts turn the scene.** d6's reversal is a phone video ("Watch this.") then a laptop CCTV insert. The micro-drama r1 cuts to a pregnancy-scan document, and r4 uses chat bubbles. This ties §7 and §14 to the existing `chats[]` cutaway and B-roll inserts.
7. **Romance on Reels splits into two very different products:**
   - (a) **C-drama/ReelShort CEO romance:** a cold open on the most heated (implied, clothed) moment, a flash-back "One day earlier", name cards for each lead, a document twist, and "Episode N" persistent top-left. This sits at the edge of our implied-only ledger rule: we keep our line, not theirs.
   - (b) **Naturalistic slow-burn** (r4): handheld phone-real daylight, small subtitles, **message bubbles as plot beats**, a "*phone pings*" caption cue, and an ending on a smile at the phone. **Neither is the golden-hour "aura" edit the draft describes.** The aura edit is a third, separate format (statement/glow-up), already covered by the `aura-cinematic` style preset.
8. **Side-choosing endings risk Meta's engagement-bait demotion.** Meta's distribution guidelines demote posts that explicitly ask for votes or comments with specific answers ("comment A or B"). Asking people to show support for an *issue* is exempt.
   - **Correction:** end on a genuine open question or a Part-2 tease, not "comment TEAM MIRA".
   - Use the native poll sticker sparingly, on organic posts only.

---

## §7 Drama / conflict (villain), corrected card
### 7. Drama / conflict (villain) [measured: https://www.instagram.com/reel/Da9ltsbPQAf/, https://www.instagram.com/reel/DU7YHpGD2Rr/, https://www.instagram.com/reel/DVM_VTjlKMH/; deeper: villains-conflict.md]
- **Why it works:** the conflict line starts at frame 1. The camera's allegiance stays with the target. Cuts accelerate into the cruelty, then sound drops out and one beat is held. The **evidence** reverses the scene (the receipts), the consequence lands, and the viewer is left with a real question.
- **Pacing map (30 s ad; measured d6 scaled from 90 s, d3 for the escalation):**

| Beat | 30 s | Shot length | Sound |
|---|---|---|---|
| Cold open mid-conflict: the cruel or accusing line, spoken from 0.0-0.2 s | 0-2 s | singles, 0.8-1.2 s | dialogue only, ≈ -14 LUFS |
| Stakes: who is wronged, the target's side said in one line | 2-8 s | shot-reverse-shot, median ~1.5 s, MCU→CU | room tone + low bed |
| Escalation: villain pushes, the target is cornered | 8-16 s | cuts tighten to ~1.0 s (d3: cuts per third 7 → 12 → 13) | bed swells; hits on the push lines |
| The cruelty / hit | 16-18 s | the fastest cuts (0.3-0.8 s), then a **hard stop** | **0.8-1.3 s silence** right after (d3: 1.0 s + 1.3 s) |
| Aftermath / evidence: the receipt (phone video, chat, document) | 18-25 s | ONE held shot or insert, 4-8 s (d6 holds ~30 s at 90 s length) | evidence audio up, music low |
| Consequence + turn (ad: brand as the helper, never the villain) | 25-28 s | back to singles ~1.5 s | swell |
| Open question / Part-2 tease (no vote-bait) | 28-30 s | CU of the target | bed out on the last word |

- **Shot grammar:**
  - singles for each speaker, mostly MCU/CU on 50-85 mm; d6 is almost all singles plus one wide establishing at 0 s.
  - the villain gets a slight low angle and colder fill;
  - the target gets eye level and warmer key;
  - insert shots for the evidence (a hand holding the phone, a screen);
  - one held wide two-shot for the aftermath;
  - no handheld shake except during a physical fight (d3).
- **Look:** contrasty and motivated. d6 uses a warm porch-light night exterior, then a neutral interior day for the evidence scene (a location change marks the reversal). There is a warm/cold split by character, inside a white or black 9:16 frame with a header line above the picture (format, see Preset).
- **genre_key:** `grounded dramatic realism, motivated contrasty practical lighting, intimate singles in shot-reverse-shot, shallow depth of field, natural performances, villain lit slightly colder from a low angle, target lit warm at eye level, no melodramatic overacting`
- **Shot JSON:**
```json
{"id":"S01","dur":2,"model":"seedance_2_5","mode":"omni_reference",
 "camera":"locked MCU single on @VILLAIN, 50mm, slight low angle, porch light camera-left",
 "subject":"@VILLAIN (identity from asset bible) in the doorway",
 "action":"start: already mid-shout, finger pointing off-screen -> end: holds the glare",
 "environment":"@SET_PORCH at night, house number on the wall, warm bulb",
 "light":"single warm practical key, cold blue fill from the street",
 "audio":"dialogue only, the accusing line from frame 1, no music",
 "constraints":"line starts at 0.0 s, no establishing beat, same wardrobe as S02-S12",
 "genre_key":"<drama genre key>"}
```
- **Sound:**
  - dialogue-forward and compressed (target -14 LUFS, LRA ≈ 5);
  - a low bed under the stakes;
  - hits on escalation lines;
  - **0.8-1.3 s true silence after the cruel beat**;
  - a swell only at the consequence, and no hype stims on the villain.
- **Ad template:** reuse D1-D10 in marketing-engine ad-strategy.md §5. D4 (One-Upper) and D9 (Receipts) map directly onto this pacing map. Add one rule: the **turn is an evidence insert**, never a speech.
- **Compliance:**
  - SG health: the evidence is a mechanism or guideline, never a patient record or a result;
  - characters are fictional and labelled as a dramatisation where they could be mistaken for real;
  - no vote-bait endings (Meta engagement-bait guideline);
  - sexual shaming involves adults 25+ only (ledger).
- **Preset:** drama-conflict (corrected below).

**Corrected preset `drama-conflict.json`:**
```json
{
  "name": "drama-conflict",
  "label": "Drama / conflict (villain)",
  "kind": "genre",
  "description": "Measured 2026-10-25 on Dhar Mann Studios 'Girl Finds Out Whole Life's A Reality Show' (IG, 238K likes: median shot 1.5 s, first word at 0.11 s, 137 wpm, -14.3 LUFS, LRA 4.9) and 'The Slap' Pt 1 (median 1.17 s, cuts accelerating 7/12/13 per third, 1.0-1.3 s silence after the hit). Dialogue from frame 1, singles in shot-reverse-shot, bold condensed caps captions low in frame, a persistent one-line header with one emoji, silence after cruelty, one held evidence beat.",
  "reference": "research/genre-research-2026-10/drama-mystery-thriller-romance.md#7",
  "pacing": {"remove_silence_over_s": 0.35, "pad_s": 0.08, "remove_fillers": "hard", "max_shot_s": 2.5},
  "captions": {"font": "Anton", "bold": true, "uppercase": true, "max_words": 4, "animation": "static", "size": 0.04, "outline": 4, "position_y": 0.66, "keyword_caps": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "outline", "persistent": true, "uppercase": false, "max_words": 7, "position_y": 0.1, "size": 0.03},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0.8, "db": -14, "min_gap_s": 0.8, "map": {"hook": "bass", "broll": "bass", "end": "swell"}},
  "music": {"energy": "low", "db": -22, "duck": true},
  "grade": {"contrast": 1.1, "saturation": 0.95, "warmth": 0.03, "vignette": false},
  "end_card": {"enabled": false},
  "_needs_feature": {
    "layout.frame": {"bg": "#FFFFFF", "picture_aspect": "4:5", "header_in_margin": true, "why": "d6/d3 put the picture inside a white or black 9:16 frame with the header in the top margin"},
    "silence_after_beat_s": 1.0,
    "hold_beat_roles": ["evidence", "aftermath"],
    "cut_acceleration": {"start_median_s": 1.6, "end_median_s": 0.9}
  }
}
```
Changes vs the current preset:
- `max_shot_s` 5 → 2.5;
- silence removal 0.9 → 0.35 (dialogue is tight; the one designed silence is placed, not left over);
- captions fade → static caps condensed, as in d6;
- smooth push every 5 s → no auto-zoom (d6 cuts, it doesn't push);
- a persistent header added;
- the end card off (episode feel).

**3 core rules (§7):**
1. **The conflict line is the hook, spoken from frame 1.** No establishing beat, no "so this happened".
2. **Cut fast into the cruelty, then stop.** Median ~1.2 s, accelerating, then ≥ 0.8 s of true silence and a held face. The villain never gets music.
3. **The turn is evidence, not a speech:** a phone video, chat, document or CCTV insert held 4-8 s. In ads it is the brand's mechanism, never a patient result.

**Flags for Klaus (§7):**
- Is the white-frame + header format wanted for brand accounts? It reads "Dhar Mann / repost page". It suits personal and organic accounts, maybe not Physio Spot ads.
- The ledger asks for "side-choosing" endings. I propose rewording them to avoid explicit vote-bait ("Team A or B? comment"), which Meta demotes. Does he want to keep poll stickers on organic posts?
- d3 is a clip account reposting a broadcast TV drama. I used it for rhythm only; it is not a format to copy (rights).

---

## §7a NEW sub-style: Micro-drama episode / series (`microdrama-episode`)
### 7a. Micro-drama episode (series) [measured: https://www.instagram.com/reel/Ddt9waGtvbS/, https://www.instagram.com/reel/Da9ltsbPQAf/; researched: "Screen Time" (nofilmschool.com/issa-rae-vertical), Crocs × ReelShort (marketingdive.com)]
- **Why it works:** every episode is one scene with one turn, ending on a cliffhanger, so the binge runs on the open loop. "Screen Time" made 55 one-minute episodes with one setting and five actors: Ep 1 drew 26 M views, and late episodes still 2-3 M each. Brands (Crocs, General Mills, Marc Jacobs, JK Super Cement, RuPay) now pay to be *inside the plot* (R2).
- **Pacing map (one 60-90 s episode):**
  - 0-3 s: "Previously" flash, OR a cold open on the episode's hottest line;
  - 3-50 s: one scene, one objective, shot-reverse-shot at a ~1.5 s median;
  - 50-80 s: the turn (evidence / reveal / entrance);
  - last 2-3 s: **cliffhanger line plus a freeze or a hard cut to black** with "Part N+1" (SocialPeta: the freeze-frame cliffhanger drives the next tap).
- **Series bible:**
  - 1 contained premise and 1-2 locations;
  - 3-5 characters with locked identities (Gate 4 assets reused every episode);
  - 8-12 episodes per season for a brand (Crocs ran 5 and 7). The 50-100-episode app seasons are not for brands.
- **Shot grammar:** as §7, plus a persistent "Episode N · Title" label top-left (r1, d1). Name cards with role on first appearance: "[Cheng Junwen, CEO of Cheng Corporation]" (r1).
- **Look:** consistent across episodes (same grade line, same frame). A fixed episode-number position.
- **genre_key:** §7 key + `consistent series look across episodes, same sets and wardrobe per character, vertical 9:16 framing with faces in the upper-middle third`
- **Shot JSON:** `{"id":"E03-S14","dur":3,"camera":"CU @LEAD, 85mm, eye level","action":"start: reads the message -> end: looks up to the door as it opens (freeze on this frame)","constraints":"last frame must be a clean freeze candidate: face + door both readable"}`
- **Sound:**
  - an original series theme sting of 2-3 s, the same every episode, on the title and on the cliffhanger;
  - dialogue-forward, -14 LUFS;
  - a riser into the freeze.
- **Brand placement (R2 lesson):** the product is a *plot device* (Crocs' Jibbitz carry the flirtation), not an ad break. One episode in 5 may carry a direct CTA.
- **Compliance:**
  - label as fiction;
  - no real patients;
  - SG health: the education sits in the episode's turn and end card, never as a cure;
  - minors never appear in romance or revenge plots.
- **Preset:** microdrama-episode (new).

```json
{
  "name": "microdrama-episode",
  "label": "Micro-drama episode (series)",
  "kind": "genre",
  "description": "One 60-90 s episode of a vertical series: cold open or 'previously' flash, one scene with shot-reverse-shot at ~1.5 s median, a turn, a freeze/black cliffhanger with 'Part N+1'. Measured on Dhar Mann Studios and FAME Ep 2 (IG, 2026); grounded in 'Screen Time' (TikTok/PineDrama, 26 M views on Ep 1) and Crocs x ReelShort.",
  "reference": "research/genre-research-2026-10/drama-mystery-thriller-romance.md#7a",
  "structure": {"name": "episode", "target_s": [60, 120], "beats": ["previously/cold open 0-3s", "scene objective", "turn", "cliffhanger freeze + Part N+1"]},
  "pacing": {"remove_silence_over_s": 0.4, "pad_s": 0.08, "remove_fillers": "hard", "max_shot_s": 3.0},
  "captions": {"font": "Anton", "uppercase": true, "max_words": 4, "animation": "static", "size": 0.038, "outline": 4, "position_y": 0.68},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "kicker", "persistent": true, "uppercase": false, "position_y": 0.07, "size": 0.026, "max_words": 5},
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0.6, "db": -14, "map": {"hook": "sting", "end": "riser"}},
  "music": {"energy": "low", "db": -22, "duck": true},
  "grade": {"contrast": 1.08, "saturation": 0.95, "warmth": 0.02},
  "end_card": {"enabled": true, "dur_s": 1.5},
  "_needs_feature": {
    "end_freeze": {"dur_s": 1.5, "zoom": 1.06, "text": "PART {n+1}"},
    "episode_label": {"text": "Episode {n} · {title}", "position": "top-left", "persistent": true},
    "previously_recap": {"max_s": 3, "source": "previous episode's turn"},
    "name_cards": {"on_first_appearance": true, "style": "[Name, role]"}
  }
}
```
**3 core rules (§7a):** (1) one scene and one turn per episode, ending on an unanswered line; (2) locked identities and sets across the whole season (Gate 4 assets reused, never re-generated per episode); (3) the brand is a plot device, not a mid-roll.

**Flags:** brand seasons of 5-12 episodes vs the app-style 50+; whether to build `end_freeze` and `episode_label` into the editor (small features, high reuse); a weekly cadence needs ~1 episode per 2 days (Party of Two, Instagram's own 7-episode series, released every other day).

---

## §14 Mystery / reveal, corrected card
**Draft bug found:** the current §14 card's **Sound / Compliance / Preset lines are copy-pasted from §29 edu-song** ("the vocal plus an original backing… every lyric is a clinical claim… Preset: edu-song"). They must be replaced. The corrected lines are below.

### 14. Mystery / reveal [measured: https://www.instagram.com/reel/Dc-RntLBfcK/ (narrated variant), https://www.instagram.com/reel/DbYOd-HD7E3/ (puzzle variant); researched: Loewenstein 1994 information-gap theory (cmu.edu Golman & Loewenstein), d6 evidence-reveal structure]
- **Why it works:** curiosity is a *specific, closeable* gap (Loewenstein 1994; Golman & Loewenstein). The hook has to name the question precisely ("who was in the corridor?"), the clues have to look solvable, and the reveal has to re-read earlier frames (a rewatch).
  - Puzzle mysteries ("can you spot the contradiction?") pull comments at ~1:1 with likes (m5: 81 likes, 78 comments), because the answer *is* the comment. That is an organic engagement driver, but on Meta the CTA "comment your answer" is phrased as a question, not as a bait instruction.
- **Pacing map (30 s ad):**
  - 0-2 s: the specific question as on-screen text plus the strangest frame;
  - 2-20 s: 3 clues, each 3-6 s, each with ONE insert of the clue object (partial framing, rack focus);
  - 20-24 s: a misdirect (the obvious suspect);
  - 24-26 s: **silence 0.5-0.8 s, then the reveal** (the first full, frontal, well-lit shot);
  - 26-30 s: a fast rewind montage of the clues (0.3-0.5 s each) re-read with the answer, then the CTA.
- **Shot grammar:**
  - clue inserts on a macro or 85 mm with a rack focus;
  - suspects in partial framing (hands, backs, reflections) until the reveal;
  - the reveal is the only symmetrical, frontal, evenly lit frame;
  - the rewind montage reuses the clue shots exactly.
- **Look:** low-key, a pool of light on each clue. The reveal brightens by 1 stop.
- **genre_key:** `mysterious low-key lighting, pools of light on key objects, partial framing of people, rack focus to the clue, restrained locked camera, quiet tension`
- **Shot JSON:** `{"id":"S03","dur":4,"camera":"macro insert, 100mm, rack focus from the cup rim to the sugar spoon","action":"start: steam over the cup -> end: focus lands on the dry spoon (the clue: nobody stirred)","light":"single pool of warm light, everything else falls to black","audio":"clock tick, a low pad, one soft ding as focus lands"}`
- **Sound (replaces the edu-song text):**
  - a sparse low pad or piano;
  - a soft tick under the clue beats;
  - one ding or click when each clue lands;
  - a riser into **0.5-0.8 s of true silence**;
  - the reveal hit (impact + sub);
  - a reverse-whoosh on the rewind montage.
- **Compliance (replaces the edu-song text):**
  - the mystery must resolve to something true: no fake "what doctors don't want you to know" curiosity bait for health;
  - SG health: the reveal is a mechanism or a common cause, never a cure or result;
  - no real crimes or real victims as puzzles (ledger: real tragedies are not entertainment);
  - a "comment your answer" CTA is phrased as a question, not a bait instruction.
- **Ad template:** "Why does X keep happening?" → 3 everyday clues → the obvious wrong answer (the myth) → the real cause (the brand's mechanism) → the rewind showing the clues were the cause → CTA. This fits the D8 "Trial" and D6 skeletons.
- **Preset:** mystery-reveal (corrected below).

```json
{
  "name": "mystery-reveal",
  "label": "Mystery / reveal",
  "kind": "genre",
  "description": "Specific question as the hook, 3 clue beats with one insert each, misdirect, 0.5-0.8 s silence, reveal hit, fast clue-rewind montage. Low-key grade that lifts at the reveal. Grounded 2026-10-25 in IG mystery micro-fiction and detective-puzzle reels plus information-gap theory (Loewenstein 1994).",
  "reference": "research/genre-research-2026-10/drama-mystery-thriller-romance.md#14",
  "pacing": {"remove_silence_over_s": 0.6, "pad_s": 0.15, "max_shot_s": 6},
  "captions": {"animation": "fade", "max_words": 5, "keyword_caps": false, "font": "Instrument Serif", "bold": false, "size": 0.034, "position_y": 0.76},
  "hook_text": {"enabled": true, "uppercase": false, "max_words": 8, "position_y": 0.2, "dur_s": 3.0, "font": "Instrument Serif Italic"},
  "zoom": {"mode": "smooth", "every_s": 6, "scale": 1.05, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 5, "max_dur_s": 3, "min_dur_s": 1.5, "mode": "full"},
  "sfx": {"density_per_10s": 0.8, "db": -14, "min_gap_s": 1.5,
          "map": {"hook": "riser", "broll": "ding", "title": "tick", "end": "impact"},
          "stacks": {"reveal": [{"type": "riser", "db": -16}, {"type": "impact", "db": -9}, {"type": "boom", "db": -12}]},
          "reveal_every_s": 0},
  "music": {"energy": "drone", "db": -24, "duck": true},
  "grade": {"contrast": 1.1, "saturation": 0.85, "brightness": -0.04, "vignette": true},
  "transitions": {"default": "dip", "on": "beats", "dur_s": 0.25, "strength": 0.6},
  "end_card": {"enabled": true, "dur_s": 1.5},
  "_needs_feature": {
    "silence_before_reveal_s": 0.7,
    "reveal_grade_lift": {"brightness": 0.04, "contrast": 1.0},
    "clue_rewind_montage": {"per_clip_s": 0.4, "reverse_whoosh": true, "source": "beats with role 'clue'"}
  }
}
```
**Variant `mystery-narrated` (m2 measured: 246 wpm first-person VO, 1.13 s median, one orange caps keyword per cut, white frame + header, LRA 1.6).** The same preset with these overrides: `captions {max_words: 1, animation: pop, uppercase: true, font: Anton, color: #FF8A3D}`, `pacing {remove_silence_over_s: 0.25, max_shot_s: 2.0}`, `broll {every_s: 1.2, max_dur_s: 1.2}`, `music {energy: drone, db: -22}`. VO-led brand mysteries only; never recap someone else's film or series.

**3 core rules (§14):** (1) the hook names ONE specific, closeable question, not "wait for the end"; (2) every clue gets its own insert and its own sound, and the rewind re-shows them after the reveal; (3) silence before the reveal, and the reveal is the first frontal, fully lit frame.

**Flags:** the §14 card in genre-playbooks.md needs its Sound/Compliance/Preset lines fixed (copy-paste from §29). The mystery reels found on IG had weak engagement (3-352 likes). The strongest evidence for the reveal structure is d6's evidence turn (238 K) and the information-gap research, so Klaus may want to send 2-3 mystery references he rates.

---

## §13 Thriller / heist / suspense, corrected card
### 13. Thriller / heist / suspense [measured: https://www.instagram.com/reel/DUJOUnrj2cU/ (Crime 101 promo), https://www.instagram.com/reel/Csyv74MAu-e/ (comedy heist), https://www.instagram.com/reel/DD5hcfgSTxB/ (AI chase); researched: "Screen Time" thriller, Pitch Black Heist / Rififi silence (reelscotland.substack.com)]
- **Why it works:** a heist is a list of rules or steps the viewer can follow, so they become the crew.
  - The Crime 101 promo is built as **"THE RULES"**: the host states each rule to camera on a black void, a big serif rule card appears ("IF A JOB FEELS WRONG IT IS WRONG"), then 3-6 film inserts prove it. Measured: median shot **0.83 s**, 142 wpm, LRA 3.8.
  - The thriller pull is the ticking clock plus the one hitch. Silence is the heist's sharpest tool (Pitch Black Heist and Rififi's silent half-hour robbery, where any sound sets off the alarm).
- **Spine B, the flash-forward (t4, 3.4 K likes):** a cold open on the end-state (sirens, a mask, "Where are you?") → a title card → an "ONE HOUR BEFORE THE HEIST" time-jump card → the plan briefing at 150-230 wpm with a 1.5 s median → a payoff that calls back to the open. It shares the time-jump card with §10 romance.
- **Pacing map (30 s ad, "the rules" spine):**
  - 0-2 s: the stakes line to camera ("In and out in 90 seconds.");
  - 2-4 s: the title card "THE RULES";
  - 4-22 s: 3 rules × ~6 s, each rule = a card (1 s) + inserts at a **0.6-1.0 s median** (hands, tools, timers, screens);
  - 22-25 s: the hitch: an alarm or a door, cuts stop, **1 s of silence**;
  - 25-28 s: the clean escape / the reveal of the trick (the product is the "tool");
  - 28-30 s: CTA as "Rule #4".
- **Shot grammar:**
  - inserts of hands, tools and timers; over-the-shoulder on screens; tracking shots;
  - a host or mastermind on a dark void or limbo set, MCU, centred;
  - cuts accelerate to the hitch, then one held wide.
- **Look:** steel blue/teal shadows, warm practicals (sodium street-light orange), high contrast, night aerials of the city. Title cards in a warm cream condensed serif or slab.
- **genre_key:** `taut heist thriller, night city, cool steel-blue shadows with warm sodium practicals, precise tracking camera, tight inserts of hands and tools, high contrast, clean modern grade`
- **Shot JSON:** `{"id":"S06","dur":1,"camera":"top-down insert, 50mm macro, locked","subject":"@CREW_HAND (gloved)","action":"start: thumb over the timer button -> end: presses, the display flips to 01:30","light":"single cold top light, warm LED reflection on the glove","audio":"one click, pulse bed continues"}`
- **Sound:**
  - a pulse/ostinato bed at 100-130 BPM, compressed (LRA ≈ 4, -14 LUFS, as t2);
  - a click or tick per insert;
  - a whoosh into each rule card;
  - **the bed cuts out on the hitch (≥ 1 s silence)**;
  - a bass hit on the escape.
- **Ad template:** "The heist" (the viewer's problem is the vault; the brand's method is the crew's tool) or "The Rules of ___" (3 rules = 3 product truths). It pairs with ad-strategy.md D5 (Interview Panel) as the "plan" variant.
- **Compliance:**
  - no crime how-to detail (ledger hard line: no crime how-tos), so locks, alarms and tools stay generic and stylised;
  - no real brands' vaults or logos;
  - SG health: the "heist" is never against a competitor or a health system (no comparative claims).
- **Preset:** thriller-suspense (corrected below).

```json
{
  "name": "thriller-suspense",
  "label": "Thriller / heist / suspense",
  "kind": "genre",
  "description": "Measured 2026-10-25 on the Crime 101 'rules of the heist' promo (IG): median shot 0.83 s, 142 wpm, -14.1 LUFS, LRA 3.8, no silence until the designed hitch. Host-to-camera rules + big serif rule cards + 0.6-1.0 s inserts, pulse bed, click per insert, silence on the hitch, steel-blue/sodium-orange grade.",
  "reference": "research/genre-research-2026-10/drama-mystery-thriller-romance.md#13",
  "pacing": {"remove_silence_over_s": 0.3, "pad_s": 0.05, "remove_fillers": "hard", "max_shot_s": 2.0},
  "captions": {"max_words": 3, "uppercase": true, "font": "Bebas Neue", "animation": "pop", "size": 0.04, "position_y": 0.72},
  "hook_text": {"enabled": true, "uppercase": true, "font": "Archivo Black", "max_words": 6, "position_y": 0.4, "dur_s": 1.6, "color": "#F2D3A2"},
  "zoom": {"mode": "snap", "every_s": 2.5, "scale": 1.08, "on_hook": 1.12},
  "broll": {"every_s": 2.5, "max_dur_s": 1.2, "min_dur_s": 0.5, "mode": "full"},
  "sfx": {"density_per_10s": 2.5, "db": -15, "cut_coverage": 0.4, "min_gap_s": 0.3,
          "map": {"hook": "impact", "zoom": "tick", "broll": "click", "title": "whoosh", "end": "bass"}},
  "music": {"energy": "high", "db": -18, "duck": true},
  "grade": {"contrast": 1.16, "saturation": 0.88, "teal": 0.05, "warmth": 0.02},
  "transitions": {"default": "flash", "on": "beats", "dur_s": 0.12, "strength": 0.5},
  "end_card": {"enabled": true, "dur_s": 1.5},
  "_needs_feature": {
    "rule_cards": {"style": "big serif cream on picture", "font": "DM Serif Display", "dur_s": 1.2, "source": "beats with role 'rule'"},
    "music_cut_on_beat_role": {"role": "hitch", "silence_s": 1.0},
    "countdown_overlay": {"from": "01:30", "font": "Space Grotesk"}
  }
}
```
**3 core rules (§13):** (1) structure it as a plan the viewer can follow (rules or steps on cards), not as vibes; (2) inserts at a 0.6-1.0 s median with a click or tick per insert, accelerating to the hitch; (3) the hitch is the one silence, and the escape is the product's role, never a real crime method.

**Flags:**
- The Crime 101 promo has a movie star as the host. For brands, the host is the founder (Klaus) or an original character.
- The t1 AI heist (3 likes, median 4.75 s, first word at 9.7 s) vs t2/t4/t3: a generic slow AI "cinematic heist" does not travel. Measured, but n=1 per side.
- `rule_cards` could reuse `texts[]` type `title` today; a dedicated style would be nicer.

---

## §10 Romance / aura / sensual (implied), corrected card
### 10. Romance / aura / sensual (implied) [measured: https://www.instagram.com/reel/DewJSY9AquY/, https://www.instagram.com/reel/DZCnMOLjhWL/, https://www.instagram.com/reel/C8MfUipINoB/; researched: ReelShort billionaire-romance 419 M views, 75 % female audience; Meta/TikTok adult-content ad policies; ledger: implied only, adults 25+]
- **What the evidence changed:** the draft mixed three formats. On Reels, romance that performs is **serial and dialogue-driven** (r1, r4, R3), not slow golden-hour montage. The "aura" edit is a statement/glow-up *style*, already covered by the `aura-cinematic` style preset. This card covers **romance-drama**; §10a covers the naturalistic texting romance.
- **What the C-drama cold open does (r1, sheet viewed) vs what we do:**
  - r1 opens on the most heated moment: a bed, a kiss, hands, rapid intercut. Then "one day earlier", name cards, and a document twist (a pregnancy scan) for the conflict.
  - **We keep the structure (cold open on the peak, then flash back) but stop at the implied line:**
    - the peak is a held near-kiss, foreheads or hands, then a cut-away (a door, a curtain, a phone lighting up);
    - adults 25+, fully clothed;
    - no bed framing in ads (Meta's ad standards flag "implied sexual activity"; the TikTok adult-content policy bars suggestive content for many categories).
- **Pacing map (30 s ad / 60-90 s episode):**
  - 0-3 s: the cold open on the charged moment (near-touch or loaded line) with a slow-mo of 1-2 shots;
  - 3-5 s: "One day earlier" / "3 months earlier" card;
  - 5-20 s: meet → friction; shot-reverse-shot at a **~2 s median** (r1 2.04 s, d7 2.0 s), music-forward with ≤ 60 wpm, and name cards on first appearance;
  - 20-26 s: the obstacle / twist insert (a message, a ring, a document);
  - 26-30 s: a glance back + cut-away + "Part 2" or the brand line.
- **Shot grammar:**
  - 85 mm CUs, glances held 1.5-3 s;
  - hands and near-touch inserts;
  - silhouettes against windows;
  - cut away at the peak (door, curtain, phone light);
  - **never** body-part framing (Meta ads policy) and never bed framing in paid placements.
- **Look:** soft warm key, bloom, correct skin tones, low contrast. Night interiors in warm practicals; golden hour for exteriors only.
- **genre_key:** `cinematic romantic drama, warm soft key light with gentle bloom, 85mm shallow focus close-ups, held glances, near-touch hands, elegant tasteful framing, implied intimacy only, fully clothed adults over 25, cut away before any kiss completes`
- **Shot JSON:** `{"id":"S01","dur":3,"camera":"CU two-shot profile, 85mm, slow push 5%","subject":"@LEAD_A and @LEAD_B, both 30s, fully clothed","action":"start: foreheads almost touching -> end: @LEAD_B's phone lights up between them; both look down","light":"warm practical lamp behind, soft bloom","audio":"breath, low pad, phone buzz at the end","constraints":"no bed, no lying down, no body-part framing, cut before lips meet"}`
- **Sound:**
  - an OST-style piano or pad, music-forward (unlike drama);
  - breath and room tone in the near-touch;
  - a phone buzz or ding as the twist cue;
  - a swell on the glance back.
- **Ad template:** fragrance, fitness, men's health ("feel like yourself"): the brand enables confidence, never promises attraction or sexual results. Sexual-health brands use clinical wording only and no implied outcome (ledger; SG health pack).
- **Compliance:**
  - adults 25+, implied only;
  - no bed or undress framing in paid ads;
  - no "attract anyone" claims;
  - Meta personal-attributes rule (no "your ED");
  - dating-app-style ads: no suggestive copy (TikTok).
- **Preset:** romance-drama (new) for the serial form; `aura-cinematic` stays for statement/glow-up edits.

```json
{
  "name": "romance-drama",
  "label": "Romance drama (implied, serial)",
  "kind": "genre",
  "description": "Cold open on the charged (implied, clothed) moment, 'one day earlier' card, dialogue shot-reverse-shot at ~1.5-2 s, name cards, a twist insert, a cut-away at the peak, 'Part 2'. From C-drama/ReelShort episodes on IG (iQIYI 'Irresistible Young Love' Ep 1, ReelShort EP 1) - structure kept, explicitness not (ledger: implied only, adults 25+).",
  "reference": "research/genre-research-2026-10/drama-mystery-thriller-romance.md#10",
  "pacing": {"remove_silence_over_s": 0.8, "pad_s": 0.2, "remove_fillers": "hard", "max_shot_s": 4.0},
  "captions": {"font": "Instrument Serif", "bold": false, "uppercase": false, "max_words": 6, "animation": "fade", "size": 0.032, "position_y": 0.76, "keyword_caps": false},
  "hook_text": {"enabled": true, "renderer": "card", "card_style": "kicker", "persistent": true, "uppercase": false, "position_y": 0.07, "size": 0.026, "max_words": 5},
  "zoom": {"mode": "smooth", "every_s": 4, "scale": 1.05, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0.3, "db": -18, "map": {"hook": "swell", "broll": "ding", "end": "swell"}},
  "music": {"energy": "low", "db": -18, "duck": true},
  "grade": {"contrast": 0.96, "saturation": 0.98, "brightness": 0.02, "warmth": 0.05, "vignette": false},
  "transitions": {"default": "glow", "on": "beats", "dur_s": 0.3, "strength": 0.4},
  "end_card": {"enabled": false},
  "_needs_feature": {
    "slowmo_on_role": {"role": "peak", "speed": 0.6},
    "time_jump_card": {"text": "One day earlier", "style": "small serif centred", "dur_s": 1.2},
    "name_cards": {"on_first_appearance": true, "style": "[Name, role]"},
    "bloom": 0.15
  }
}
```

### 10a. NEW: Slow-burn texting romance (`romance-texting`) [measured: https://www.instagram.com/reel/C8MfUipINoB/]
- **Why it works:** r4 ("Scenes From a Love Story", Mumbai, 1,260 likes, Ep 2) is handheld phone-real daylight with small subtitles.
  - The plot moves through **message bubbles** ("Hi Sahir here, lmk if you need help with further life decisions") and a "*phone pings*" caption. It ends on the other lead smiling at his phone.
  - It is relatable, cheap to make, and fits creators and real people. It reuses `chats[]` / chatanim.
- **Pacing (60-90 s episode; r4 measured: median 3.3 s, 28 wpm, first line at 17 s, silences of 1.3 s and 1.55 s kept):**
  - 0-5 s: a goodbye or a small moment (the picture carries it; words can come late);
  - message bubble beats every 10-20 s, each held 2-3 s over the shot (not a full black card as in §30);
  - the reply arrives on the other lead's face;
  - the ending is a smile at the phone + "Follow for Ep 3".
- **Shot grammar:** handheld eye-level, natural light, real homes and streets, mostly singles. A bubble overlay sits top-centre over the shot.
- **genre_key:** `naturalistic handheld phone-shot realism, soft daylight and warm lamp interiors, real lived-in homes, candid small smiles, adults over 25, no glamour lighting`
- **Sound:** live sound + a light acoustic bed, a "ping" per message, no hits.
- **Compliance:** fictional; composite chats only (texting §30 rules); adults 25+.
- **Preset:** romance-texting (new).

```json
{
  "name": "romance-texting",
  "label": "Slow-burn texting romance (naturalistic)",
  "kind": "genre",
  "description": "From 'Scenes From a Love Story' Ep 2 (IG @molshriii, 1.26K likes): handheld daylight realism, small subtitles, message bubbles overlaid on the shot as plot beats, a ping per message, ends on a smile at the phone + 'Follow for Ep 3'.",
  "reference": "research/genre-research-2026-10/drama-mystery-thriller-romance.md#10a",
  "pacing": {"remove_silence_over_s": 1.2, "pad_s": 0.25, "remove_fillers": "none", "max_shot_s": 6.0},
  "captions": {"font": "Poppins", "bold": false, "size": 0.026, "color": "#FFE14D", "outline": 2, "max_words": 8, "animation": "static", "position_y": 0.8, "uppercase": false, "keyword_caps": false},
  "hook_text": {"enabled": false},
  "zoom": {"mode": "smooth", "every_s": 0, "scale": 1.0},
  "broll": {"every_s": 0},
  "sfx": {"density_per_10s": 0.3, "db": -16, "map": {"broll": "pop", "end": "ding"}},
  "music": {"energy": "low", "db": -22, "duck": true},
  "grade": {"contrast": 1.0, "saturation": 1.0, "warmth": 0.03},
  "end_card": {"enabled": true, "dur_s": 1.5},
  "_needs_feature": {
    "chats.overlay_mode": {"mode": "overlay", "position_y": 0.22, "hold_s": 2.5, "why": "r4 shows one bubble over the live shot, not a full black chat card"}
  }
}
```
**3 core rules (§10 + 10a):** (1) cold open on the charged moment, then jump back in time: structure from C-drama, explicitness from our ledger (implied only, clothed, adults 25+, cut away before the kiss completes); (2) the obstacle arrives as an object or message insert (phone, ring, document), and the reply lands on the other face; (3) end on a glance or smile and an open loop ("Part 2"), never on the payoff.

**Flags for Klaus (§10):**
- Split §10 into "romance-drama" (serial) and keep "aura" as a style (`aura-cinematic`)?
- How far does "implied" go for organic vs paid? Proposal: organic may show a completed kiss between adults; paid stops at the near-kiss and never shows a bed.
- C-drama-style cold opens (r1) are more explicit than our line. We copy the structure only.

---

## Late results (measurements that finished after the cards were drafted)
(Values here supersede "see late results" in the evidence table.)

| ID | Module | Cuts · avg / median shot | Thirds (cuts) | First word · wpm | Loudness | Silence ≥ 0.5 s | What the sheet shows |
|---|---|---|---|---|---|---|---|
| r4 Scenes From a Love Story Ep 2 (1,260 likes) | §10a | 19 · 3.81 / **3.27 s** (max 11.7) | 10 / 4 / 5 | **17.0 s** · **28 wpm** (Hindi, sparse) | -14.1 LUFS, LRA **11.5** | **1.3 s, 1.55 s** | handheld daylight, small yellow subtitles, white chat bubbles over the shot, "*phone pings*" caption, ends on the other lead smiling at his phone |
| r1 iQIYI Irresistible Young Love Ep 1 (1,534 likes) | §10 | 43 in 120 s · 2.73 / **2.04 s** | 12 / 10 / **21** | 3.4 s · **6 wpm** (music-led montage) | -13.2, LRA 5.8 | none | implied/clothed bed + wall kiss montage cold open (more explicit than our line), vertical name cards, "Episode 1" label top-left, document twist (scan), "one day earlier" flashback |
| d7 ReelShort "Your Love Broke My Heart" (2,239 likes) | §10 / §7a | 18 · 2.31 / **2.0 s** | 4 / 8 / 6 | 0.0 s · 59 wpm | -15.1, LRA 6.2 | none | trailer-style clip: a man teaches her to shoot ("don't anticipate… remember this feeling"), romance + revenge set-up |
| d2 amandalpaca "reacting to low budget short form dramas pt 15" (**10,169 likes**) | §7a parody signal | 41 in 120 s · 2.86 / 1.77 s | 11 / 19 / 11 | 0.0 s · 199 wpm (zh/en) | -14.1, LRA 9.0 | none | 2 reactors over a PIP of micro-drama clips (fake-doctor tropes); the audience knows the tropes well enough to laugh at them |
| m2 "The Lampshade Evidence" (352 likes) | §14 | **71** in 99 s · 1.37 / **1.13 s** | 20 / 29 / 22 | 0.0 s · **246 wpm** first-person VO | -14.1, **LRA 1.6** | none | **first-person "movie story" recap** of what looks like a European crime series: one orange caps word per cut, white frame + header "Tell a movie story from the first person perspective…", evidence = phone → TV autoplay → the killer is the detective |
| t4 alloramomo "The heist (short film)" (3,442 likes) | §13 | 26 · 2.22 / **1.53 s** | 7 / 12 / 7 | 0.0 s · **228 wpm** | -16.0, LRA 7.1 | none | **flash-forward cold open** (balaclava, sirens, "Where are you?") → "The Heist" title over a bank → "One hour before the heist" card → the plan meeting derails into a comic argument → callback to the late getaway driver; phone-shot, serif subtitles |

| d4 Dhar Mann "Model Fired For Being Too Short" (3,316 likes) | §7 | 60 in 92.6 s · 1.52 / **1.42 s**, **max 2.71 s** (metronomic) | 23 / 18 / 19 | **0.0 s** · 129 wpm | -14.1, LRA 8.6 | none | opens on the insult ("You would never make it as a model… with a walk like that"); white frame + header; class/looks villain |
| r6 ReelShort "Summer Situationship" EP 1 (661 likes) | §10 / §7a | 44 in 98 s · 2.18 / **2.13 s** | 14 / 14 / 16 | 0.9 s · 111 wpm | -14.7, LRA 13.1 | 1.0 s at the very start | **flash-forward cold open** on the fight + VO thesis ("If someone makes you crazy, you're either hopelessly in love with them or you hate their guts"), "A FEW MONTHS LATER" card, **name cards with relation** ("Emmett, Jules's Ex-Boyfriend"), class humiliation (she is the maid for her ex-best friend) |
| d1 FAME Ep 2 (3,366 likes, 78 comments) | §7a | 9 in 120 s · median **4.48 s** (long takes, max 52 s) | 5 / 1 / 3 | 3.5 s · 79 wpm | -13.4, LRA 13.6 | none | indie long-take micro-drama (music/fan scene); proof that an engaged community series survives slow cutting, but it is the exception |
| t3 Jason Zada "The Heist" (all text-to-video, 430 likes) | §13 | 56 in 116 s · 2.04 / **1.62 s** | 21 / 21 / 14 | **no dialogue** | -14.1, LRA 6.0 | none | 16:9 posted as-is; 70s NYC getaway chase: title on the bank façade, wheel/pedal inserts, driver CU, windscreen POV, cop car; **one hero object (the green car) locked across shots** |
| t1 AI heist (38 s, **3 likes**) | §13 control | 5 cuts · median **4.75 s** | 0 / 4 / 1 | 9.7 s (pt) · 41 wpm | -14.1, LRA 3.9 | 0.7 s | slow, generic "cinematic AI heist" with no rules, no character hook, first word at ~10 s: the counter-example |
| m5 "man found dead… can you spot the contradiction" (81 likes, **78 comments**) | §14 puzzle | **0 cuts** (one illustrated board, typewriter text) | n/a | 0.0 s · **206 wpm** | -14.7, LRA 2.3 | none | challenge hook "If you can solve this case, you're in the top 2% of logical thinkers"; 5 suspects × 1 alibi each, one with a contradiction; ends "comment your answer and tag someone…" (tag-bait: Meta demotes it) |

Not measured (time): m1, m3, m4 (3-10 likes, low signal), r2, r3, r5 (AI romance edits, ≤ 31 likes), d5 (fan repost).

**What these change:**
- **Dhar Mann is metronomic.** d4 never holds a shot longer than 2.71 s (median 1.42 s) and starts on the insult at 0.0 s. Two official Dhar Mann reels now agree: §7's `max_shot_s: 2.5` is right.
- **"Time-jump + name card" appears three times** (r1, r6, t4). The relation-labelled name card ("Emmett, Jules's Ex-Boyfriend") lets a 90 s episode skip all exposition. Promote `name_cards` and `time_jump_card` in priority.
- **AI heist counter-example:** t1 (slow, generic, 3 likes) vs t2/t4 (fast, rules or a characterful plan, 641-3,442 likes) vs t3 (fast wordless chase, 430 likes). A **fast cut plus a character or a rule spine** is what travels, not "cinematic AI".
- **Puzzle mysteries can be zero-cut** (m5): one board, a typewriter reveal, 206 wpm VO, and the comment count ≈ the like count. A cheap evergreen format for any brand ("spot the posture mistake").
- **Romance is slower and music-led.** Medians run 2.0-2.04 s for the serial/C-drama form and 3.3 s for the naturalistic form, with very few words (6-59 wpm). The naturalistic form is the only measured genre here with real silences (1.3-1.55 s). Updates:
  - §10 dialogue shot-reverse-shot becomes **~2 s median, music-forward, ≤ 60 wpm**;
  - §10a holds **3-4 s median, first line can come late (the picture carries it), keep 1-1.5 s silences**;
  - `romance-texting` should use `remove_silence_over_s` ≥ 1.2 (raised from 0.7).
- **The time-jump card is shared by heist (t4: "One hour before the heist") and romance (r1: "one day earlier").** Flash-forward cold open → time-jump card → the build → payoff that calls back to the open. Add it to §13's pacing map as an alternative spine to "the rules", and keep `time_jump_card` as one shared `_needs_feature`.
- **Heist dialogue is FAST:** 228 wpm (t4) and 142 wpm (t2). The plan briefing is the content, so §13 captions stay at 3 words and silence removal stays tight.
- **Mystery has two speeds:**
  - (a) the **narrated recap** (m2): 246 wpm VO, 1.1 s median, one keyword per cut, LRA 1.6 (wall-to-wall);
  - (b) the staged slow-clue reveal in the card above.

  The draft only knew (b). Add a `mystery-narrated` variant: VO-led, caption one word per cut, `max_words: 1`, `animation: pop`, `remove_silence_over_s: 0.25`, B-roll every 1.2 s. **Do not copy m2's source** (it recaps someone else's series). Use it for brand-made narrated mysteries ("I found the reason my back hurt every morning…").
- **The white frame + one-line header container shows up again** (m2), after d6. It is the dominant "story page" container on IG drama, mystery and recap reels. That raises the priority of `layout.frame`.

---

## Decisions for Klaus (one list)
1. Fix the §14 card's copy-paste bug (Sound/Compliance/Preset come from edu-song).
2. Approve the shorter drama pacing (median ~1.2-1.5 s with designed holds) over the draft's 2-4 s.
3. Reword "side-choosing" endings to avoid Meta vote-bait demotion (ledger 2026-10-20 says "end on side-choosing").
4. Build small editor features that recur across these modules: `layout.frame` (white/black frame + header margin), `end_freeze` + `episode_label`, `silence_after_beat_s` / `music_cut_on_beat_role`, `chats.overlay_mode`, `slowmo_on_role`, `clue_rewind_montage`.
5. Add the new presets `microdrama-episode`, `romance-drama`, `romance-texting`. Keep `aura-cinematic` as the statement/glow-up style.
6. Paid vs organic line for romance (near-kiss vs completed kiss; no bed in paid).
7. Send 2-3 mystery and heist references he rates. The IG mystery reels found here were low-signal.

## Sources
- Dhar Mann Studios on IG: https://www.instagram.com/reel/Da9ltsbPQAf/ · https://www.instagram.com/reel/DU7YHpGD2Rr/ · WNYC profile (60 B views): https://wnyc.org/story/dhar-mann-studios-dhar-mann · format notes: https://tvtropes.org/pmwiki/pmwiki.php/Trivia/DharMann
- Screen Time (Issa Rae / Hoorae / TikTok / PineDrama): https://nofilmschool.com/issa-rae-vertical · https://thegrio.com/2026/04/09/issa-rae-tiktok-screen-time-microdrama · https://goodfest.westfield.com/2026/05/issa-rae-made-tiktoks-biggest-micro-drama-screen-time-heres-how/
- Brands in micro-dramas: https://marketingdive.com/news/brands-content-gold-microdramas-will-they-muck-up-moment/819961 · https://www.ypulse.com/newsfeed/2026/02/19/crocs-is-the-latest-brand-to-lean-into-microdramas-as-marketing/ · https://www.easternprogress.com/superordinary-and-crocs-launch-tiktok-microdrama-series-built-for-conversion/article_3030049c-854a-5e45-a982-48dbececff9c.html · https://www.tubefilter.com/2026/07/07/tiktok-microdrama-brand-marketing-ad-product-growth-max/amp/ · https://www.exchange4media.com/digital-news/as-microdramas-take-off-brands-move-from-placement-to-participation-157687.html · https://www.emarketer.com/content/microdramas-turn-repeat-mobile-viewing-new-opportunities-brands
- Micro-drama market/structure: https://socialpeta.com/blog/Short-Drama-Weekly-Ranking:Family-Search-Revenge-Romance-Soars · https://www.subscriptioninsider.com/blog/streamers-face-a-new-challenger-for-mobile-attention-microdramas-news · https://ca.rollingstone.com/culture/werewolf-billionaire-ceo-husbands-are-taking-over-hollywood/ · https://www.aol.com/reelshort-ceo-joey-jia-used-151738812.html · Instagram's own series "Party of Two": https://www.socialsamosa.com/industry-updates/instagram-micro-drama-series-party-of-two-9782648 · Meta Reels series test: https://onlinemarketing.de/social-media-marketing/meta-series-reels-instagram-facebook-microdrama-trend
- Curiosity / information gap: https://www.cmu.edu/dietrich/sds/docs/golman/golman_loewenstein_curiosity.pdf · https://nautil.us/curiosity-depends-on-what-you-already-know-235803 · reveal vs twist: https://nofilmschool.com/difference-between-plot-twist-reveal
- Heist craft: https://reelscotland.substack.com/p/interview-john-maclean-on-pitch-black-heist · Crime 101 promo: https://www.instagram.com/reel/DUJOUnrj2cU/
- Platform rules: Meta engagement bait: https://transparency.meta.com/features/approach-to-ranking/content-distribution-guidelines/engagement-bait/ · Meta ad standards, adult nudity & sexual activity: https://transparency.meta.com/policies/ad-standards/objectionable-content/adult-nudity-and-sexual-activity/ · TikTok ads adult content: https://ads.tiktok.com/help/article/tiktok-ads-policy-adult-content
- Hook timing (secondary, attributed to TikTok; original not retrieved): https://houseofmarketers.com/importance-of-tiktok-ad-hooks-first-3-seconds/
- All other reels: URLs in the evidence table.
