# Genre playbooks: the same genre language for generation (Higgsfield) and the edit (tools/editor)

Pick a genre module in Gate 2 (story directions) for ads too, not just films. The module sets:
- pacing, shot grammar, camera, light/grade and the sound plan;
- the prompt block pasted into every shot (`genre_key` in spec.json);
- the editor preset used to cut it.

**Status:** a module tagged **[measured]** comes from Klaus's reference reels. A module tagged **[draft]** comes from established craft conventions and still needs 2+ measured real examples (the overnight research run adds them). Klaus approves or corrects each one, and `/learn` writes the rule.

## 0. Genre picker (choose 1 primary + at most 1 accent; e.g. "comedy skit + horror accent" for a parody scare)
| # | Genre | Use when the script is… | Feeling | Avg shot | Pace curve | Grade | Sound | Editor preset |
|---|---|---|---|---|---|---|---|---|
| 1 | Horror / tension | a fear, a reveal, a parody scare | dread → jolt | 6-10 s | slow → slower → SNAP | cold teal, crushed | drone, stings, silence | horror-tension |
| 2 | Comedy skit / deadpan | a joke with a reveal; "their way vs the obvious way"; quote vs reality | anticipation → laugh | premise 1-5 s, then ONE 10-28 s take | premise → still take → pause → punch at ~65 % | natural / brand | room tone, no music under the take, ≤ 1 hit | deadpan-comedy (+ deadpan-silent-rebuttal, quote-reality-oneshot) |
| 3 | Gen Z vlog / reaction | real-life moment, travel, banter | "nahhh" | 3-6 s | raw, reaction-led | natural, bright | SFX per reaction | genz-header-skit |
| 4 | Trend beat-switch montage | a list, roles, "they call me…" | delight, recognition | 1.2-2 s | intro → drop → on beat | punchy | music-led | trend-beat-switch |
| 5 | POV / relatable | "POV: the friend who…", a recognisable type | recognition | 5-12 s per vignette | 3 vignettes, escalating; pause before the punch | phone-natural | dialogue-led (~200+ wpm), no bed | ugc-pov |
| 6 | Absurdist / meme chaos | brand self-mockery, escalating nonsense, mascot lore | shock-laugh | 1.5-5 s (memes 5-16 s in total) | label escalation → hold the most absurd image | saturated, one consistent style | the sound/track is the rhythm, one hit at the end | meme-chaos-short (+ brand-meme-reply, lore-rollcall); genz-chaos for chaos talking-head edits |
| 7 | Drama / conflict (villain) | bully, betrayal, side-picking | anger → justice | 2-4 s | build → confrontation → consequence | contrasty, warm/cold split | score swells, cold cruelty beats | drama-conflict |
| 8 | Class & status | rich vs broke, same problem two wallets | recognition, both-sides | 2-3 s | split-screen rhythm | two grades | ironic music | talking-head-punchy |
| 9 | Feel-good / emotional | kindness, family, small win | warmth, tears | 3-5 s | gentle rise → payoff | warm, soft | piano/strings, natural sound | feelgood-emotional |
| 10 | Romance / aura / sensual (implied) | attraction, glow-up, confidence | longing | 3-6 s | slow, lingering | golden, soft contrast | ambient, breathy pads | aura-cinematic |
| 11 | Founder / comeback / inspirational | origin, struggle → win | belief | 2-4 s | low → climb → peak | desaturated past → warm present | build-up score | founder-inspire |
| 12 | Cautionary / decision ladder | bad choices escalate | "don't be him" | 2-3 s | step-down rhythm | slowly colder | tick, low hits | cautionary-ladder |
| 13 | Thriller / heist / suspense | plan, chase, ticking clock | tension, momentum | 1.5-3 s | accelerating cross-cuts | steel blue/orange | pulse, ticking | thriller-suspense |
| 14 | Mystery / reveal | a question answered at the end | curiosity | 3-5 s | slow clues → twist | moody low-key | sparse piano, risers | mystery-reveal |
| 15 | Action / sport hype | training, game day, transformation | adrenaline | 0.5-1.5 s | fast, speed ramps | high contrast, crushed | bass, whoosh, hits on beat | action-hype |
| 16 | Sci-fi / tech futurism | AI, product-of-the-future (TITAN.AI) | awe | 2-4 s | smooth, deliberate | cool cyan + one accent | synth pads, glitch ticks | scifi-tech |
| 17 | K-drama | soft romance, family, longing glances | tenderness | 3-5 s | slow, held looks | pastel, soft bloom | OST piano, slow-mo | kdrama-soft |
| 18 | Anime-inspired | hype, rivalry, "power-up" | intensity | 0.8-2 s | impact frames, holds | saturated, speed lines | whooshes, impact, choir hits | anime-energy |
| 19 | 3D Pixar / cartoon | mascots, kids-safe explainers | charm | 2-3 s | bouncy | bright, clean | playful foley | (see animation-3d-cartoon.md) |
| 20 | Documentary / investigative | real story, research, recon | trust, revelation | 3-6 s | measured, VO-led | neutral, archival | VO + subtle bed | documentary |
| 21 | Explainer / myth-buster | expert education | "I finally get it" | 2-3 s | brisk | clean, bright | light whooshes on graphics | talking-head-punchy |
| 22 | News / scam-expose | warnings, tips, "don't fall for this" | alarm → protected | 1.5-3 s / slides | headline-first | high clarity | news stings, ticks | news-expose |
| 23 | Commentary / receipts | real controversy | judgement | 2-3 s | evidence beats | neutral | minimal | documentary (see commentary-controversy.md) |
| 24 | Luxury / product reveal / new release | launches, premium products | desire | **narrative film 0.8-1.1 s median; object film 2.6-3.3 s; FOOH one take 7-8 s** | **brand flash ≤1.5 s → story or tease → hero packshot held 2-4 s at the end** | rich blacks, one brand colour | score/whoosh-led, sub hit on the packshot | luxury-reveal (+ new luxury-object-calm, fooh-oneshot) |
| 25 | UGC demo / experience-style | creator uses the product | trust | 1.5-3 s | problem → use → result | phone-natural | voice, light music | ugc-* presets |
| 26 | Before / after transformation | change over time (home, car, hair, product) | proof, "wait for it" | **process 0.6 s median (detailing) or locked one-take time-lapse 7+ s (rug); reveal held to the last 3-5 s** | before shown at 0 s → process → split/wipe reveal at the end (or "part 2") | matched light, locked camera | real process foley, no VO; a whoosh/ding on the reveal | before-after-process (new) |
| 27 | ASMR / satisfying | process, pouring, building, cleaning | calm, completion | **top performer: one locked take (11-20 s) → completed state held 2-3 s; brand reels cut 0.7-1.5 s** | one continuous action → finished object → loop | clean, bright, macro | loud close foley (onsets 15-54 per 10 s), no music, no VO | asmr-satisfying (one-take default) + asmr-product-cut (new) |
| 28 | Event / retail / mall promo | openings, pop-ups, launches, mall events | FOMO, fun | **0.8-1.0 s median (music-only); 1.5 s when there is a VO** | storefront at 0 s → 1 s hero/product/activation inserts → bag-out or what-where-when | bright, natural store light | licensed upbeat track; ~140 wpm VO with dates for events | event-retail-promo (new) |
| 29 | Edu-song / mnemonic / musical explainer | teaching steps, routines, checklists, myths ("boring" health or how-to) | delight, "I can't unhear it" | 1-3 s, on the beat | spoken hook → song → recap chorus → CTA | bright, clean, saturated | the song IS the music (original or public-domain melody) + pops | edu-song |
| 30 | Texting / receipts suspense | someone retells what was said or texted; DMs, leaks, "she told me…" | intrigue, dread | 4-7 s holds | slow build, each message a beat, punch line alone | warm interview vs black chat cards | drone/pulse bed, hit every 1-3 s, tick per bubble | texting-suspense |
| 31 | Borrowed cold open / bait-and-switch | a lesson that needs a scroll-stopper; riding a moment everyone recognises | recognition → surprise | the borrowed clip 3-16 s, then the creator's normal pace | familiar viral moment → "skip" → your lesson | match the borrowed clip, then your own look | the original's audio, a skip/whoosh on the switch, then yours | split layout + trend-beat-switch or talking-head-punchy |
| 32 | Absurd how-to / survival recipe (narrated 3D) | a calm tutorial voice over an impossible task; series with a recurring character | delight, "wait what" | 2-2.5 s | step per shot → sensory payoff → wordless twist | hyper-detailed 3D on a blank cobalt grid void | deadpan VO, foley per verb, one impact | absurd-howto-3d |
| 33 | Code-made motion + screen tutorial | tools/AI how-to, founder build-in-public, exact numbers on screen | "I can do this" | screen holds + 0.03-0.13 s bursts | calm walkthrough → proof burst → CTA | dark UI, brand accent | voice-led, clicks/ticks | code-motion-tutorial (tools/motion) |
| 34 | Stick / minimal compare loop | "same X, only one added Y", compounding habits | recognition → "do it" | one shot, ticker every ~1.5 s | identical start → divergence → typed verdict → loop | black, white figures, one accent | trending/licensed track only | stick-compare-loop (tools/motion compare-loop) |
| 35 | Petty victory sermon (hype-preacher comedy) | a small win delivered like scripture at the doubters | laugh at the mismatch | one long take | slow-mo stance → rising sermon → "touch it" button | dreamy haze, warm, washed | epic/choir bed, a riser into the last line | petty-sermon |
| 36 | Clone / character swap ("this is also me") | one person becomes many characters, A/B model tests, one actor plays every role | "how??" | match cut every 1.5-2.5 s | me → also me ×4-6 → how-to → CTA | match the driver clip | walk/beat-synced cuts, whoosh on each swap | side/split B-roll + genz-header-skit (clone-character-swap.md) |

**Pairing rules:**
- Comedy can borrow any genre's grammar for a parody (horror parody, heist parody); hold the genre seriously until the reveal.
- Ads keep the genre's grammar until the turn, then switch to the brand's look.
- Never mix two primaries.


## How a module plugs in
- **spec.json:** `"genre": "horror-tension"`, `"genre_key": "<the module's style key line>"`, and per shot `duration`, `camera`, `light`, `sound` taken from the module's shot grammar.
- **Prompts:** put the genre key LAST in every image and video prompt (identity and camera stay first; prompt-patterns.md universal grammar).
- **Edit:** `editor.py assemble --preset <module preset>`. Sound comes from the module's stim plan through `/sound`.
- **Ads:** keep the genre's grammar up to the turn. Then use the brand's own ending look (e.g. Physio Spot cuts to the calm beige clinic), and apply the compliance pack to every line.

---

## 1. Horror / thriller tension (`horror-tension`)
**Reference:** Klaus's ref #5 (research/edit-references-2026-10.md): a 99 s bathroom scare. Measured average shot ≈ 10 s, a sting roughly every 1-2 s in the build, and silence before the scare.

**Why it works:** the camera stays longer than is comfortable. Darkness and sound do the work; cuts are rare. The audience knows something is wrong before the character does.

### Pacing map (scale to the runtime; 30 s ad shown)
| Beat | 30 s ad | Shot | Sound |
|---|---|---|---|
| Cold open: wrongness | 0-3 s | static wide, a held frame where something is slightly off (a door ajar, a figure in the mirror) | room tone, fluorescent buzz |
| Normal + tension | 3-12 s | slow push-in on the lead (8-10 s, one shot); a reflection or shadow moves behind them unnoticed | low drone fades in; single stings at 1-2 s gaps |
| Escalation | 12-20 s | lights flicker; 2-3 shorter shots (2-3 s): eyes, hand on the door, the empty stall | stings tighten; breathing; music drops out |
| Silence | 20-21.5 s | hold on the face or the empty frame | dead silence (≥ 0.8 s) |
| Scare / reveal | 21.5-23 s | snap: crash zoom or hard cut to the reveal | impact + bass drop, peaking at -1 dBTP |
| Turn (ads) | 23-30 s | hard cut to black, then the brand's calm world (light comes back) | silence → warm room tone → VO/CTA |

### Shot grammar
- **Camera:** gimbal-smooth slow push-ins and drifts; static locked-off wides for "wrongness"; low or high angles only for the scare. No handheld shake except POV panic.
- **Lens:**
  - 24-28 mm wides (the space is a character);
  - 50-85 mm tight on eyes and hands in the escalation;
  - deep focus in wides so the background threat is readable.
- **Blocking:** the threat lives in the background, frame edges, reflections or doorways. Leave negative space where something could appear.
- **Light:** motivated practicals only (fluorescent tubes, phone torch, a bulb). Cold teal-green fluorescent, deep shadows, faces half-lit. Light failure (flicker or blackout) is a story beat.
- **Grade:** teal shadows, slightly green mids, saturation ~0.7, crushed blacks, vignette. The editor preset applies the same values.

### Prompt blocks (Seedance 2.5 / Kling 3.0)
Genre key (paste last, identical in every shot):
```
horror thriller tone, cold fluorescent teal-green light, deep crushed shadows, desaturated, faces half in shadow, slow deliberate camera, held frames, negative space, practical lights only, subtle film grain, no jump-scare blur, no gore
```
Shot JSON (use for each line of spec.json `shots[]`; compile_shots.py turns it into the prompt):
```json
{
  "id": "S02", "dur": 8, "model": "seedance_2_5", "mode": "omni_reference",
  "camera": "slow push-in on gimbal, 28mm, eye level, from doorway toward @LEAD at the mirror",
  "subject": "@LEAD (identity from asset bible) washes hands, unaware",
  "action": "start: hands under tap -> end: she looks up into the mirror; behind her the far stall door drifts open 10 cm on its own",
  "environment": "@SET_BATHROOM: white tiles, green stripe, three stalls on the left, mirror right",
  "light": "two fluorescent tubes, the far one buzzing and dim, cold teal-green, shadows pooling under stalls",
  "audio": "fluorescent hum, dripping tap, faint low drone; no music",
  "constraints": "keep stall door movement subtle and slow, no figures visible yet, same wardrobe, no face morphing",
  "genre_key": "<horror genre key above>"
}
```
- **Kling multi-shot:** label the shots, one camera owner per shot, and keep the grade line identical across shots.
- **Moderation-safe horror:** suggest the threat (a shadow, a reflection, a door, a sound). Show no gore and no real-person likeness; children never appear in horror. Adult themes follow mature-edge.md.

### Sound plan (into `/sound` and the edit)
- **Bed:** drone or room tone (the editor synthesises an original drone when there is no licensed bed).
- **Build:** stings at 1-2 s gaps that tighten toward the scare; breathing and foley (tap drip, door creak) carry the realism.
- **The scare:** ≥ 0.8 s of TRUE silence before it, then impact plus a bass drop on the reveal frame.
- **Levels:** VO is king for the ad turn. Stims never mask a spoken word (voice-persona-audio.md).

### Horror-framed ad template (any brand)
- **Hook (0-3 s):** a "wrongness" frame plus a header that names the fear in the viewer's words.
- **Build:** the everyday situation turns uneasy (the product's problem, staged as a threat).
- **Scare or reveal:** the problem lands.
- **Turn:** a hard cut to light. The brand is the relief, never the monster.
- **CTA:** calm, in the brand voice.
- **Compliance:** fear appeals must stay proportionate. No fear-mongering for health claims (compliance-packs.md); in SG health ads the scare can't be a medical outcome claim.

### Edit preset
`horror-tension`: long holds, pause removal only above 1.6 s, slow push-in every 8 s, flicker-in at each beat change, sting/impact SFX, drone bed, teal grade, small low serif captions.

---


---

## Module cards (same layout as §1)
Each card gives:
- the pacing map (30 s ad)
- shot grammar
- look
- `genre_key` (pasted LAST in every prompt)
- one shot JSON example
- sound
- ad template + compliance
- the editor preset

Shot JSON keys are the same as in §1 (id, dur, model, mode, camera, subject, action, environment, light, audio, constraints, genre_key); only the key fields are shown below.

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

(preset `deadpan-comedy`: tools/editor/presets/deadpan-comedy.json)
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
- **Research file:** research/genre-research-2026-10/comedy-pov-absurd.md

### 2a. NEW sub-style: Silent over-complication rebuttal (`deadpan-silent-rebuttal`) [measured: khaby1, khaby2]
- **What:** a "life hack" or "expert" method that is absurdly over-complicated (0-12 s) → the performer, silent, does the obvious thing in one locked take → the signature open-palm "it's that easy" gesture.
- **Why:** it's wordless, so it is language-free and works in every market. Khaby Lame built 142.8 M+ TikTok followers on it (Guinness 2022) and 7.9-9.7 M likes per IG reel in 2024-26 (measured above).
- **Brand version:** "How people think you fix a stiff neck (17-step gadget routine)" → the physio silently does one simple, safe cue → the gesture → the brand card.
  - The rebuttal must be **safe general education**, never a treatment claim.
  - Never mock a real creator's clip: recreate a generic version.
- **Preset JSON:**
(preset `deadpan-silent-rebuttal`: tools/editor/presets/deadpan-silent-rebuttal.json)
- **Research file:** research/genre-research-2026-10/comedy-pov-absurd.md

### 2b. NEW sub-style: Quote vs reality, one shot (`quote-reality-oneshot`) [measured: corp1; also brain2 "Other people lives: / Me:"]
- **What:** a persistent two-part header: the quote or claim ("We need you in the office to experience the company culture"), then the label ("The culture:"). Under it, ONE static take that contradicts it. 8-12 s.
- **Measured:** corp1 is 10.9 s, 0 cuts, 4 words. brain2 is 8.3 s: "Other people lives:" for 2.6 s, then "Me:" held for 4.2 s.
- **Brand use:** corporate satire (TITAN.AI: "'AI will do it all for you' / The AI:"); for SG health, "'Just rest it' / Your desk setup:" (no outcome claims).
- **Preset JSON:**
(preset `quote-reality-oneshot`: tools/editor/presets/quote-reality-oneshot.json)

---
- **Research file:** research/genre-research-2026-10/comedy-pov-absurd.md

### 3. Gen Z vlog / reaction [measured: ref #1]
- **Why it works:** a header frames the viewer's reaction before the payoff. The footage is raw, so it feels real, and every reaction gets a sound hit.
- **Pacing (20-30 s):**
  - 0 s onward: header on screen the whole time;
  - 0-3 s: the weird thing starts;
  - reactions every 1.5-2 s (sound hits);
  - payoff in the last third;
  - no CTA card (the CTA goes in the caption).
- **Shot grammar:** selfie or handheld walk-and-talk, long takes of 4-6 s, whip to the subject, snap punch-in of about 1.15 on the funniest frame.
- **Look:** natural daylight, phone colour, no grade tricks.
- **genre_key:** `handheld smartphone vlog, natural daylight, front camera selfie angle, spontaneous candid moment, slight motion blur, real street ambience, unpolished authentic look`
- **Shot:** `{"camera":"selfie front camera, arm's length, walking backwards","action":"start: host talks to camera -> end: kid behind him pulls a face, host turns"}`
- **Sound:** live audio plus a hit per reaction (bass, pop, scratch); a trending sound only on personal accounts, in-app.
- **Ad template:** the creator's real reaction to the product or situation, with a header in the viewer's words. Never fake a "real" reaction for a regulated claim.
- **Preset:** genz-header-skit (header written as an emoji context line + 2-4 CAPS words + 😭💀).

### 4. Trend beat-switch montage [measured: ref #6]
- **Why it works:** the intro makes a fill-in-the-blank promise; the drop pays it off with rapid proof, one clip per beat.
- **Pacing:**
  - 0-4 s: to camera, two box captions (a setup line and a "but…" teaser);
  - from the drop: a clip on every beat (1.2-2 s), each with one label word;
  - the last clip holds two beats.
- **Shot grammar:** a mix of archive, B-roll and stills; each clip readable in under 1 s; frame the subject centred so the label sits clear of the face.
- **genre_key:** `bold readable compositions, single clear subject per frame, high clarity, vivid colour, centred framing` (montage stills/clips)
- **Sound:** the music carries it (licensed or original for brands); cuts land exactly on onsets (beat_sync).
- **Ad template:** "We're a clinic, but our patients call us…" (no testimonials in SG health; use roles or services instead of patient quotes).
- **Preset:** trend-beat-switch.

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

(preset `ugc-pov`: tools/editor/presets/ugc-pov.json)
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
- **Research file:** research/genre-research-2026-10/comedy-pov-absurd.md

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
(preset `meme-chaos-short`: tools/editor/presets/meme-chaos-short.json)
**`genz-chaos.json` correction (small):** the description claims "[measured]" in style-archetypes #6, but no reel in this run supports a punch-in every 1.5 s or 4 SFX per 10 s for *meme* content. Keep the preset for a fast talking-head edit only, and relabel it in §0 row 6 → meme-chaos-short. If Klaus wants it calmer: `zoom.every_s` 1.5 → 3.0 and `sfx.density_per_10s` 4 → 2. **Flag for Klaus: I did not measure a talking-head chaos reel, so I'm not changing genz-chaos numbers myself.**

**3 core rules (§6):**
1. **Chaos is in the image, not the cut.** One bizarre, centred, frontal subject per shot, held long enough to read (1.5-5 s); the last, most absurd image gets the longest hold.
2. **Label every beat.** A year, rating, "Me:", a name tag or a one-word caps line: the label turns nonsense into a pattern the viewer can follow.
3. **The brand mocks itself, fast and short.** 5-16 s, sound-led, a reply to something the audience already said, never punching down.

**Unsure, for Klaus:**
- **Is "brainrot" style on-brand for any of his brands?** It is huge (445-691 K likes on single reels) but polarising, with child-safety press. I'd keep it to TITAN.AI or personal accounts.
- **Fake product cards** ("Boogie Fee 49.00") are a strong punch for Power Protein / PeachForm, but a fake price can read as an advertised price; it needs a "joke" signal. Not for SG health at all.
- **Plane-face-style "mascot face" effects need a mascot.** Which brands have one? A Gate 4 character-design job may come first (character-design.md).
- **Research file:** research/genre-research-2026-10/comedy-pov-absurd.md

### 6a. NEW sub-style: Brand meme reply (`brand-meme-reply`) [measured: ryan1]
- **Format:** platform Stitch/Remix of a customer or trend clip (≤ 3.5 s) → the brand mascot/face replies in-character (one word per caption beat) → a 1 s fake-card or product punch. 5-8 s in total.
- **Researched:** Ryanair reports 111 M organic impressions in a month from low-fi memes and reactive posts (podcast summary via WebSearch; unverified). The team posts within days of a trend, and speed beats polish.
(preset `brand-meme-reply`: tools/editor/presets/brand-meme-reply.json)
Rights: the opening clip comes in only through the platform's Stitch/Remix, or with written permission (genre §31). Never downloaded and re-uploaded.
- **Research file:** research/genre-research-2026-10/comedy-pov-absurd.md

### 6b. NEW sub-style: Lore roll-call / character parade (`lore-rollcall`) [measured: brain1]
- **Format:** 5-8 original AI characters, one per shot (1-4.5 s, median 2.7 s), each with a name tag top-right and a chanted name; the final character is held 8-11 s while the chant loops.
- **Why:** each character is a collectible and a comment prompt ("which one are you?"). It fits a studio that already builds character sheets (Gate 4).
- **Brand use:** TITAN.AI "meet the agents" or a Power Protein flavour-creature roster, built from original characters only.
- **genre_key for the set:** `vintage 1990s cel-animated TV cartoon look, warm sunlit forest background, one hybrid creature centred full body, soft film grain, consistent character design style across shots, no text`
(preset `lore-rollcall`: tools/editor/presets/lore-rollcall.json)

---
- **Research file:** research/genre-research-2026-10/comedy-pov-absurd.md

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

(preset `drama-conflict`: tools/editor/presets/drama-conflict.json)
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
- **Research file:** research/genre-research-2026-10/drama-mystery-thriller-romance.md

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

(preset `microdrama-episode`: tools/editor/presets/microdrama-episode.json)
**3 core rules (§7a):** (1) one scene and one turn per episode, ending on an unanswered line; (2) locked identities and sets across the whole season (Gate 4 assets reused, never re-generated per episode); (3) the brand is a plot device, not a mid-roll.

**Flags:** brand seasons of 5-12 episodes vs the app-style 50+; whether to build `end_freeze` and `episode_label` into the editor (small features, high reuse); a weekly cadence needs ~1 episode per 2 days (Party of Two, Instagram's own 7-episode series, released every other day).

---
- **Research file:** research/genre-research-2026-10/drama-mystery-thriller-romance.md

### 8. Class & status [draft; deeper: class-status.md]
- **Pacing:** the same problem shown in two wallets, cutting between them every 2-3 s; split-screen at the punchline.
- **Shot grammar:** mirrored framing for the two lives (same angle, different set); matching action cuts.
- **Look:** two grades (rich: clean, cool, glossy; broke: warm, practical, cluttered), but equal dignity.
- **genre_key (per side):** `same framing and action as counterpart shot; {rich: polished minimalist interior, soft cool daylight | broke: lived-in small flat, warm practical bulb}`
- **Compliance:** sourced statistics only; punch at behaviours and systems, never at being poor.
- **Preset:** talking-head-punchy, or genz-header-skit for the comedy version.

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
- **Research file:** research/genre-research-2026-10/action-feelgood-founder.md (also: 9c festive-film sub-card, new ad formats N1-N3, 3 core rules + flags per module)

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

(preset `romance-drama`: tools/editor/presets/romance-drama.json)
- **Research file:** research/genre-research-2026-10/drama-mystery-thriller-romance.md

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

(preset `romance-texting`: tools/editor/presets/romance-texting.json)
**3 core rules (§10 + 10a):** (1) cold open on the charged moment, then jump back in time: structure from C-drama, explicitness from our ledger (implied only, clothed, adults 25+, cut away before the kiss completes); (2) the obstacle arrives as an object or message insert (phone, ring, document), and the reply lands on the other face; (3) end on a glance or smile and an open loop ("Part 2"), never on the payoff.

**Flags for Klaus (§10):**
- Split §10 into "romance-drama" (serial) and keep "aura" as a style (`aura-cinematic`)?
- How far does "implied" go for organic vs paid? Proposal: organic may show a completed kiss between adults; paid stops at the near-kiss and never shows a bed.
- C-drama-style cold opens (r1) are more explicit than our line. We copy the structure only.

---
- **Research file:** research/genre-research-2026-10/drama-mystery-thriller-romance.md

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
- **Research file:** research/genre-research-2026-10/action-feelgood-founder.md (also: 9c festive-film sub-card, new ad formats N1-N3, 3 core rules + flags per module)

### 12. Cautionary / decision ladder [draft; deeper: mature-edge.md §1]
- **Pacing:** each bad choice is a step of 3-5 s with an on-screen step number; things get slowly worse; the consequence; the "don't be him" wisdom.
- **Shot grammar:** a repeated framing per step so the decay is visible (same angle, worse state).
- **Look:** the grade cools a little each step.
- **genre_key:** `consistent locked framing across steps, gradually colder and darker grade, realistic consequences, no glamorising`
- **Sound:** a clock tick bed; a low hit on each step.
- **Preset:** cautionary-ladder.

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

(preset `thriller-suspense`: tools/editor/presets/thriller-suspense.json)
**3 core rules (§13):** (1) structure it as a plan the viewer can follow (rules or steps on cards), not as vibes; (2) inserts at a 0.6-1.0 s median with a click or tick per insert, accelerating to the hitch; (3) the hitch is the one silence, and the escape is the product's role, never a real crime method.

**Flags:**
- The Crime 101 promo has a movie star as the host. For brands, the host is the founder (Klaus) or an original character.
- The t1 AI heist (3 likes, median 4.75 s, first word at 9.7 s) vs t2/t4/t3: a generic slow AI "cinematic heist" does not travel. Measured, but n=1 per side.
- `rule_cards` could reuse `texts[]` type `title` today; a dedicated style would be nicer.

---
- **Research file:** research/genre-research-2026-10/drama-mystery-thriller-romance.md

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

(preset `mystery-reveal`: tools/editor/presets/mystery-reveal.json)
**Variant `mystery-narrated` (m2 measured: 246 wpm first-person VO, 1.13 s median, one orange caps keyword per cut, white frame + header, LRA 1.6).** The same preset with these overrides: `captions {max_words: 1, animation: pop, uppercase: true, font: Anton, color: #FF8A3D}`, `pacing {remove_silence_over_s: 0.25, max_shot_s: 2.0}`, `broll {every_s: 1.2, max_dur_s: 1.2}`, `music {energy: drone, db: -22}`. VO-led brand mysteries only; never recap someone else's film or series.

**3 core rules (§14):** (1) the hook names ONE specific, closeable question, not "wait for the end"; (2) every clue gets its own insert and its own sound, and the rewind re-shows them after the reveal; (3) silence before the reveal, and the reveal is the first frontal, fully lit frame.

**Flags:** the §14 card in genre-playbooks.md needs its Sound/Compliance/Preset lines fixed (copy-paste from §29). The mystery reels found on IG had weak engagement (3-352 likes). The strongest evidence for the reveal structure is d6's evidence turn (238 K) and the information-gap research, so Klaus may want to send 2-3 mystery references he rates.

---
- **Research file:** research/genre-research-2026-10/drama-mystery-thriller-romance.md

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
- **Research file:** research/genre-research-2026-10/action-feelgood-founder.md (also: 9c festive-film sub-card, new ad formats N1-N3, 3 core rules + flags per module)

### 16. Sci-fi / tech futurism (TITAN.AI) [draft]
- **Pacing:** smooth 2-4 s shots; an interface or hologram reveal; "the future" line; product as the hero.
- **Shot grammar:** symmetrical compositions, slow dolly, macro on light and interfaces, clean negative space.
- **Look:** cool cyan with one warm accent; clean, glossy, volumetric light.
- **genre_key:** `sleek near-future aesthetic, cool cyan volumetric light with one warm accent, symmetrical composition, slow dolly, clean minimal surfaces, subtle holographic UI`
- **Sound:** synth pads, soft glitch ticks on UI events, a bass swell on the reveal.
- **Compliance:** AI claims must be substantiable; no "replaces humans" fear angle.
- **Preset:** scifi-tech.

### 17. K-drama [draft; localisation packs for market]
- **Pacing:** held looks of 3-5 s; a slow-motion turn; an OST cue on the realisation; a cliffhanger last line.
- **Shot grammar:** two-shot → close-up → close-up; rain or snow; umbrella framing; a lingering back-of-head shot.
- **Look:** pastel, soft bloom, bright clean skin.
- **genre_key:** `Korean drama aesthetic, soft pastel grade, gentle bloom, slow motion glance, romantic framing, clean bright skin tones`
- **Sound:** OST-style piano and strings (original or licensed), a heartbeat on the look.
- **Preset:** kdrama-soft.

### 18. Anime-inspired [draft; mature-edge.md Japanese mode]
- **Pacing:**
  - impact frames (a 2-4 frame flash);
  - a power-up hold of 1-2 s;
  - speed lines;
  - an exaggerated reaction cut-in.
- **Shot grammar:** extreme low angles, dramatic zooms, split-panel compositions, dramatic still holds.
- **Look:** saturated, cel-shaded if animated; live-action uses hard colour light.
- **genre_key:** `anime-inspired dynamic composition, dramatic perspective, speed lines, impact frame flash, saturated cel-shaded colour` (an original style, never a named studio or IP)
- **Sound:** whooshes, impacts, choir or orchestral hits.
- **Preset:** anime-energy.

### 19. 3D Pixar / cartoon: see animation-3d-cartoon.md (style key, character sheet, consistency); pace as comedy or feel-good.

### 20. Documentary / investigative [draft; deeper: documentary-3d.md, commentary-controversy.md]
- **Pacing:** a cold open on the strongest fact → the question → evidence beats (3-6 s each, VO-led) → the turn → what it means.
- **Shot grammar:** slow push on photos and documents, establishing wides, lower-thirds for names and sources, interview framing at 1/3.
- **Look:** neutral, with an archival texture for the past.
- **genre_key:** `documentary realism, natural available light, observational camera, archival texture for past events, sober composition`
- **Sound:** VO first, a subtle bed at -21 dB, room tone.
- **Compliance:** every fact goes in SOURCES.md.
- **Preset:** documentary.

### 21. Explainer / myth-buster [draft; story-engine.md myth-buster]
- **Pacing:** the myth (hook) → why people believe it → the mechanism (graphic) → what to do → the callback; 2-3 s beats.
- **Shot grammar:** talking head with punch-ins; a graphic or B-roll for each mechanism line.
- **genre_key:** `bright clean educational look, clear subject, simple uncluttered background, diagram-friendly composition`
- **Sound:** light whooshes on graphics only.
- **Compliance:** claims must be sourced.
- **Preset:** talking-head-punchy.

### 22. News / scam-expose (video + carousel) [draft until ref #2 arrives]
- **Pacing:**
  - kicker bar plus headline at 0 s ("⚠️ SCAM ALERT");
  - "how it works" in 3-5 numbered steps;
  - "how to protect yourself";
  - the source line.
- **Carousel:** slide 1 = kicker + 6-word claim over the evidence photo; slides 2-6 = numbered steps, one idea each; the last slide = what to do + who to contact.
- **Look:** high clarity, credible, no meme fonts; a red or amber accent for the warning; the brand logo small.
- **genre_key:** `credible photojournalistic style, clear evidence framing, neutral daylight, no dramatisation`
- **Sound (video):** a news-style sting on the kicker, ticks on each step.
- **Compliance:** never name or accuse individuals without proof; blur faces and plates of private people; state the source and date.
- **Preset:** news-expose (expander: carousel-text with the kicker card).

### 23. Commentary / receipts: see commentary-controversy.md (steelman, receipts format, no AI likeness of real people).

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
- **Research file:** research/genre-research-2026-10/luxury-retail-transform-asmr.md

### 25. UGC demo / experience-style: the editor's ugc-* presets (selfie, unboxing, try-on, reaction, POV, experience-style, day in the life, green screen). Real people beat generated ones; experience-style is never posed as customer testimony in regulated markets.

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
- **Research file:** research/genre-research-2026-10/luxury-retail-transform-asmr.md

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
- **Research file:** research/genre-research-2026-10/luxury-retail-transform-asmr.md

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
- **Research file:** research/genre-research-2026-10/luxury-retail-transform-asmr.md

### 29. Edu-song / mnemonic / musical explainer (`edu-song`) [draft]
Full guide: edu-songs-mnemonics.md (formats, kids-TV levers, copyright). Tool: `editor.py song`.
- **Pacing map (30-45 s do-along):**
  - 0-3 s: a spoken or on-screen hook that frames the gag ("Your pelvic floor routine, but it's a nursery rhyme");
  - 3-5 s: count-in;
  - 5-35 s: the song, one step per line, a cut or visual change on every line, with the exercise done on camera in real time;
  - 35-42 s: the recap chorus, double speed or with all the moves in a row;
  - last 3 s: the CTA (save this / follow for part 2).
- **Shot grammar:** locked frontal medium (the host mirrors the viewer), big hand gestures, one prop or diagram per line, a cartoon mascot insert for the "dumb question" (animation-3d-cartoon.md), and karaoke words on screen.
- **Look:** bright, high-key, saturated brand colours, clean background; kids-TV clarity, not kids-TV cheapness.
- **genre_key:** `bright high-key studio, clean solid-colour backdrop, cheerful saturated palette, playful educational children's-show staging, crisp friendly lighting`
- **Shot:** `{"camera":"locked frontal medium, eye level","action":"start: host counts on fingers -> end: host freezes in the stretch, grinning","light":"soft high-key, no shadows"}`
- **Sound:** the vocal plus an original or public-domain backing, a pop or ding per step, a riser into the recap. No pop-song melodies on brand accounts.
- **Compliance:** every lyric is a clinical claim; run the compliance pack line by line. No promised outcomes in SG health.
- **Preset:** edu-song.

### 30. Texting / receipts suspense (`texting-suspense`) [measured: ref #7]
- **Pacing map (60-90 s):**
  - 0-3 s: the most shocking text, shown alone and large, cold;
  - 3-20 s: the interviewee or founder sets the stakes;
  - each "they said / they texted" moment cuts to a full-black chat card, 4-7 s, with bubbles one by one and a typing dot before each reply;
  - the turn: the punch message alone and large, then a beat of silence;
  - the aftermath on the speaker's face, then the CTA or "watch the full story".
- **Shot grammar:** a locked interview mid-shot with a warm practical light; archival or B-roll inserts; the chat cards are full-frame graphics (`chats[]`), never a filmed phone (unless it's a real phone in the scene).
- **Look:** the warm interior vs pure-black cards; a small persistent title top-left; slightly desaturated.
- **genre_key:** `intimate documentary interview, warm practical lamp light, shallow depth of field, muted desaturated palette, still locked camera, tense quiet atmosphere`
- **Shot:** `{"camera":"locked 50mm interview mid-shot, slightly off-axis","action":"start: subject looks down at phone -> end: looks up to lens, says nothing","light":"single warm practical, deep falloff"}`
- **Sound:** a low drone or pulse bed, a hit every 1-3 s, a soft tick on each bubble, and silence on the punch line.
- **Compliance:** real messages need consent from both parties; recreations are labelled "dramatised" when they could be mistaken for real; health brands never show patient chats.
- **Preset:** texting-suspense (brief beats carry `chat`; renders via tools/editor chatanim.py).

### 31. Borrowed cold open / bait-and-switch (hook-jacking) [measured: ref #8]
The idea: open on something the audience already knows and loves (a viral clip, meme moment, famous scene or trending audio), then "skip" or "switch" into your lesson. The recognition stops the scroll; the switch is the pattern-interrupt.
- **Pacing map:**
  - 0-3 s: the most recognisable moment of the borrowed clip (no intro);
  - up to ~15 s: let it run only while it's still delivering;
  - the switch: a UI "skip" (Omegle next, FaceTime swap, TV channel change, "wait…" record scratch) into you, keeping the same frame or layout so it feels like the same video;
  - the lesson in 3 numbered steps with a growing list on screen;
  - leave a reaction element running (the other window's face) for comedy;
  - CTA.
- **Variants:**
  - **Format-jack:** recreate the viral moment with your own people ("Omegle but it's a physio"). Fully owned.
  - **Moment-jack:** reference a trend everyone knows (a meme line, a viral sound) and act it out yourself.
  - **Clip-jack:** the actual third-party footage. Only under the rights rules below.
  - **Scene parody:** a famous film or TV scene restaged with the brand's twist (see filmmaking-longform.md for staging; no lookalikes of real actors).
- **Layout:** the editor's `split` B-roll mode (top = the borrowed or recreated window, bottom = the speaker), or full frame with a UI frame graphic.
- **Rights (hard rules):**
  - **Brand, clinic and ad accounts:** format-jack or moment-jack only. Never third-party footage, and never real private people from viral clips (likeness + privacy). In SG health, also no implied endorsements.
  - **Personal or creator accounts, clip-jack allowed only via:**
    - the platform's own Remix / Stitch / Duet, where the original creator enabled it (platform licence, auto-credit); or
    - written permission from the rights holder (DM screenshot saved to the project), credited on screen.
    - Commentary or reaction on the clip itself is a judgement call per market, and never for a sales post.
  - Never download and re-upload someone else's viral clip as your own opener without one of the above. It is copyright infringement, is often muted or removed, and the people in it never agreed.
- **Compliance:** the switch must not misrepresent (no fake "news" or fake "patient" footage).
- **Preset:** talking-head-punchy or genz-header-skit, plus B-roll `mode: split` for the opener; trend-beat-switch if music-led.

### 32. Absurd how-to / survival recipe, narrated 3D (`absurd-howto-3d`) [draft; measured: ref anim1]
- **Why it works:** an impossible ingredient or task explained in a calm, familiar tutorial voice. The process is satisfying, an early aside opens a loop, and a wordless twist pays it off and sets up the next episode.
- **Pacing map (35-40 s):**
  - 0-2.5 s: the absurd action is already happening (no intro); VO "First, X, but don't just Y."
  - 2.5-5 s: the open-loop aside ("This is our last recipe…").
  - 5-30 s: one step per shot, 2-2.5 s each, with an imperative verb on each cut and state carried across cuts.
  - 30-34 s: the sensory payoff (crack, pour, bite) and the longest hold (3.5-4.5 s).
  - 34-38 s: the wordless twist (threat appears / it backfires), then an in-world series card ("CAVEMAN 1 RIP").
- **Shot grammar:** one master angle (a high 3/4 overhead, cooking-show top shot) for most steps; 3-4 macro inserts on hands and material; one low hero angle saved for the twist. A locked camera or slow push. The character's outfit and markings never change.
- **Look:** a hyper-detailed 3D character on an infinite cobalt-blue grid void; warm food and material tones against cold blue; soft overhead key light.
- **genre_key:** `hyper-detailed 3D character render on an infinite saturated cobalt-blue studio floor with a thin white perspective grid fading to a pale-blue horizon, no walls, no other props, soft overhead key light with gentle contact shadows, tactile macro textures, warm food tones against the cold blue, clean tutorial staging, same character design in every shot, no text in frame`
- **Shot:** `{"camera":"high three-quarter overhead, 35mm, locked, slight push-in","action":"start: @CAVEMAN packs rock salt around the leg -> end: only the bone end pokes out of a smooth white mound","light":"soft overhead key, contact shadows, cold blue bounce"}`
- **Sound:** a deadpan VO at ~200-210 wpm (~7-8 words per shot); one-word captions; foley on every process verb (crunch, sizzle, crack); a low bed at -24 dB; one impact on the twist; no meme sounds on brand accounts.
- **Compliance:** for a health brand, the "recipe" must be safe technique or education, with no outcome or cure claims, no testimonials and no superlatives. The twist can be slapstick but never a medical injury scare. Food or supplement versions make no nutrition claims beyond the label.
- **Preset:** absurd-howto-3d (JSON in research/refs-2026-10-25/ai-animation.md).

### 33. Code-made motion + screen tutorial (`code-motion-tutorial`) [draft; measured: ref anim2]
- **Why it works:** the contrast hook ("slop vs this"), then proof (a 10-15 s burst of code-rendered cards), then a calm, doable how-to. The series tag and comment-keyword CTA drive comments and follows.
- **Pacing map (60-145 s; 16:9 YouTube/LinkedIn or 9:16):**
  - 0-3 s: series tag plus a glitch-in title ("PART 2").
  - 3-12 s: the contrast claim on two screens ("AI SLOP" vs "WITH THE SKILL") and the price or effort hook.
  - 12-25 s: who it's for / where it runs (a chalkboard or card list), then "now let's cook" (a mascot card).
  - 25-60 s: steps over screen recordings, with keyword captions in the empty half of the frame and smooth push-ins on the UI.
  - 60-76 s: the PROOF BURST, a code-rendered showreel with cards at 0.03-0.6 s and one idea per card.
  - 76-130 s: the second method or part, over a painted plate background.
  - Last 8 s: the keyword CTA ("Comment X") plus "part 3".
- **Shot grammar:** real screen recordings for UI (never faked UI). A voxel or illustrated host room for the bookends. Code cards for claims and numbers. The camera is a smooth digital push in the edit.
- **Look:** dark UI + cream/black type cards, a heavy grotesk for punch words, an italic serif for poetic lines, mono HUD micro-text (frame counters, coordinates); accents in mint and orange-red, or the brand's hex.
- **genre_key (non-code layers only):** `cosy voxel-art 3D diorama, chunky cube-built characters and furniture, soft warm desk-lamp key with cool window fill, muted sage-green walls, gentle depth of field, clean readable silhouettes, no text`
- **Shot:** `{"camera":"slow dolly-in, 35mm, eye level toward the desk","action":"start: @VOXEL_HOST beside two dark monitors -> end: left monitor flickers on showing cluttered slop, right shows a clean card, host leans in","light":"warm desk lamp key, monitor glow on the host"}`
- **Sound:** a conversational VO at ~120 wpm with 5-10 word sentences; a mid-energy bed at -20 dB ducked under the VO; clicks and whooshes on UI moves; the burst cut to a beat-synced track with one hit per card.
- **Compliance:** only claim what our real outputs show (no "Higgsfield-level for free" claims we can't back). Reference videos are study-only and never downloaded and re-cut. A keyword CTA must deliver what it promises, and it is never an inducement on SG health posts. Show real client work only with permission.
- **Preset:** code-motion-tutorial; the burst comes from tools/motion (proposed) as one full B-roll clip.

### 34. Side-by-side progression loop, stick figures (`stick-compare-loop`) [draft; measured: ref anim3]
- **Why it works:** two identical figures and ONE variable. Counters tick on screen and the difference compounds visually (glow, size, colour) until a typed punchline lands. Then it loops to frame 1, so it reads muted and in any language.
- **Pacing map (12-16 s):**
  - 0-1.5 s: Month/Week 1, both figures equal, counters visible (the persistent header "SAME X. SAME Y.").
  - 1.5-11 s: 6-7 ticks at ~1.5 s each; per tick, a synced action rep, the variable changes on the right only, the delta pops ("+0" grey / "+10" amber) and the exaggeration grows.
  - 11-14 s: the typed punchline with a cursor ("SAME SQUATS. DIFFERENT LEGS.") over a slow push-in on the changed feature.
  - 14 s: a hard cut back to the first frame (seamless loop).
- **Shot grammar:** one continuous shot, zero cuts; a locked, perfectly symmetrical wide; a single shared prop between the figures as the "same" anchor; only the final push-in moves the camera.
- **Look:** white capsule stick figures, a black reflective void, warm emissive floor tiles, bloom on the "winning" figure's head, a pixel/mono display font, white header + amber winner stats + grey control stats.
- **genre_key:** `minimal 3D render, two identical white matte stick figures with capsule limbs and round heads, black void with a glossy reflective floor, glowing warm emissive floor tiles, soft bloom, perfectly symmetrical side-by-side composition, locked camera, no background detail, no text in frame`
- **Shot:** `{"camera":"locked wide two-shot, 35mm, slightly high, centred","action":"start: both figures stand with barbells -> end: both finish one synced squat; @STICK_B's legs are slightly thicker and his head glows brighter","light":"warm emissive tiles, faint bloom, black void"}`
- **Sound:** music-led (a licensed CML track or an original for brands; a trending chart song only on personal accounts, in-app); a pop per counter tick; a whoosh on each prop swap; keyboard ticks on the typed punchline; no VO.
- **Compliance:** this is a comparison format, so in SG health it is close to before/after. Show behaviours and inputs (breaks taken, protein added, tasks automated), not guaranteed body or pain outcomes. Label exaggeration as "dramatised illustration", use no patients and no "results" numbers. Counters and type are built in code so the numbers are exact and checkable.
- **Preset:** stick-compare-loop; the counters, type and loop come from the tools/motion split-compare template (proposed). The figures come from code (three.js capsules) or Seedance start/end morphs.

### 35. Petty victory sermon (`petty-sermon`) [measured: ref comedy1, research/refs-2026-10-25/comedy-clone.md]
- **Why it works:** a small, real win (graduation, first pull-up, the clinic's first anniversary) is delivered with the cadence of a revival preacher at "that man in my family who said I'd fail". The joke is the mismatch of scale, and the defiance is relatable. It rides the trending sound/hashtag (#whoisthatmaninmyfamilythatsaidiwillfail) when one exists.
- **Pacing map (25-40 s, ONE take, 0 cuts in the ref):**
  - 0-3 s: the rhetorical question to the doubters, eyes off-camera;
  - 3-20 s: escalating declarations, each one a short line with a pause, at a slow ~125 wpm;
  - 20-30 s: the absurd physical button ("This is my tail. Touch it.");
  - end on the biggest scripture-style line, then hold.
- **Shot grammar:** locked mid-full shot of the hero at the victory location (the logo or sign in frame proves the win), a slight low angle, a slow push. Wardrobe sells it (gown, sunglasses, the medal).
- **Look:** heavy dreamy haze and glow, warm washed-out grade, slow-motion feel. Captions: ONE big word at a time, white caps with a cyan outline, centred.
- **genre_key:** `dreamy hazy glow, soft bloom, warm washed-out sepia tones, slow-motion stillness, hero standing proudly in a victory location, low angle, epic triumphant mood`
- **Sound:** an epic or choir bed under the voice, a riser into the final line; no other SFX.
- **Brand versions:** physio: "Who is that man at the office who said I'd never deadlift again?" Use only Klaus's or staff's OWN recovery; never a patient story in SG health (testimonial rule), never an outcome promise. Founder: "Who is that investor that said TITAN would fail?"
- **Preset:** petty-sermon.

### 36. Clone / character swap (`clone-character-swap.md`) [measured: refs clone1, hfclone]
Full workflow, formats and hard rules are in clone-character-swap.md:
- driver clip + original character sheet → Genjutsu / Seedance 2.5 / Wan 3.0 motion transfer;
- formats: "this is me… and this is also me" match cuts, the A/B model test (editor B-roll `mode: side`), and one actor playing every role in a skit;
- never a real-person lookalike, and always label it as AI.
