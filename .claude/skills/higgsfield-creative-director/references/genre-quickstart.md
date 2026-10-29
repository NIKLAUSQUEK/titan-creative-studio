# Genre quickstart: every genre in plain English, with a worked example

The deep reference is [genre-playbooks.md](genre-playbooks.md) (prompt keys, shot JSON, sound levels, compliance detail). The measured data behind it is in `research/genre-research-2026-10/*.md`. This file is the fast version: what each genre is, how real creators pace it, and one script you could shoot tomorrow.

## How to read this
1. Pick a genre from the picker below (one main genre, at most one accent).
2. Every section has the same shape: what it is → when to use it → **5 beats with real timings** → the best measured reel → a full script for one of our brands → why the order works → the 2 classic mistakes → the editor preset.
3. Timings are **measured** from real reels (ffmpeg cut detection + transcripts) unless marked *[not measured]*.
4. "Median shot 1.5 s" means half the shots are shorter than 1.5 s and half are longer (the typical shot).
5. "wpm" = words per minute. 150 is normal talking; 220+ is fast.
6. "-14 LUFS" = the standard loudness for Reels/TikTok. Just export at that.
7. Scripts rotate brands: Snap Saigon (HCMC snappers + city stories), Physio Spot (SG men's health physio, SG health rules), TITAN.AI, Power Protein (Thao Dien protein café), Klaus personal.
8. Lines in [square brackets] are facts to fill or verify before filming. Never invent them.
9. Klaus's own script or final cut always wins (version A). These scripts are starting points, not replacements.
10. Rules at the bottom ("Universal rules") apply to every genre.
11. Shot words: WS = wide shot, MS = mid shot (waist up), MCU = medium close-up (chest up), CU = close-up, insert = a close shot of an object or hand, PiP = picture-in-picture (a small video in a corner), VO = voice-over.
12. "Over the shot" means the text sits on top of the footage. We don't cut to a plain black or white text page in the middle of a video (ledger [edit]).

## Quick picker: goal → genre
| You want… | Use | Brand fit |
|---|---|---|
| A laugh that also makes a point | 2 Deadpan · 5 POV · 6 Absurd · 35 Petty sermon | all |
| People to share because they saw themselves | 5 POV · 8 Class · 34 Stick loop | all |
| Fast reach from a trend | 4 Beat-switch · 31 Borrowed cold open · 6a Meme reply | personal, TITAN.AI, Power Protein |
| Trust in a person | 11 Founder · 30 Texting · 35 Sermon | Klaus, TITAN.AI |
| Teach something that sticks | 21 Myth-buster · 29 Edu-song · 33 Code tutorial · 19 Cartoon | Physio Spot, TITAN.AI |
| Make people want a product | 24 Luxury reveal · 27 ASMR · 18 Anime jingle · 28 Event | Power Protein |
| Show proof of a result | 26 Before/after · 16 Tech launch · 25 UGC demo | TITAN.AI, Snap Saigon |
| Warn people (safety, scams) | 22 News/scam · 12 Cautionary ladder | Snap Saigon, Physio Spot |
| Hold attention to the end | 14 Mystery · 20 Documentary · 13 Heist rules | Snap Saigon stories, TITAN.AI |
| Feelings: tears, pride, love | 9 Feel-good · 10 Romance · 15 Sport hype · 17 K-drama | Snap Saigon, Power Protein |
| A series people binge | 7a Micro-drama · 10a Texting romance · 32 Absurd how-to | any |
| Tension or a parody scare | 1 Horror · 13 Thriller | Power Protein, TITAN.AI |
| Reach a feeling against a villain | 7 Drama/conflict | Snap Saigon, personal |
| Recut what we already filmed | 17a Fan-edit · 4 Beat-switch · 36 Clone | any |

---

## 1. Horror / thriller tension
- **What it is:** a scary-movie build where the camera waits too long, the sound gets tense, it goes silent, then something jumps out.
- **Use it when:** a parody scare or a "the problem is the monster" ad; the brand is the light at the end, never the monster.
- **The 5 beats (30 s ad):**
  1. 0-3 s: a still wide shot where one thing is slightly wrong.
  2. 3-12 s: one slow push-in (8-10 s, one shot); something moves behind the lead; a sting every 1-2 s.
  3. 12-20 s: 2-3 shorter shots (2-3 s): eyes, hands, the empty space; stings get closer; music drops out.
  4. 20-23 s: at least 0.8 s of total silence, then the scare (crash zoom or hard cut + bass hit).
  5. 23-30 s: hard cut to black, then the brand's warm, calm world and a calm CTA.
- **Real example:** Klaus's ref #5, the DJI RS5 bathroom scare (99 s, typical shot ≈ 10 s, a sting every 1-2 s, silence right before the scare; `research/edit-references-2026-10.md` #5). It works because nothing is cut fast: the waiting is the fear.
- **Example script (Power Protein, "The 3 pm thing"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Still wide: a dim office, blinds down. The snack drawer hangs open, empty. Header: "It always comes at 3 pm." | fluorescent buzz |
| 3-12 s | One slow push-in on Linh at her laptop. Behind her, the kitchen door drifts open by itself. | low drone; stings at 1-2 s gaps |
| 12-20 s | Her heavy eyelids (2 s) · her hand finds only crumbs in the snack tin (3 s) · the clock flips to 15:00 (2 s) | stings tighten, slow breathing, drone cuts out |
| 20-21 s | Hold on her face, eyes closing | total silence (1 s) |
| 21-23 s | Crash zoom: her forehead hits the keyboard; the doc fills with "jjjjjjjjjjjj" | impact + bass drop |
| 23-26 s | Black. Then warm café light: a Power Protein box slides onto her desk. | silence → warm room tone |
| 26-30 s | She opens it, sits up, keeps typing. Over the shot: "Power Protein · Thao Dien" | VO: "3 pm doesn't have to win. Order from the link in bio." |

- **Why it works (logic chain):**
  - Beat 1 makes the viewer name the fear ("3 pm"), so beat 2 can stretch time without losing them.
  - Beats 2-3 make the viewer expect a scare, so the silence in beat 4 feels like a held breath and the keyboard faceplant lands as a laugh.
  - The scare is the problem (the crash), so beat 5 can make the brand the relief, and the CTA answers the header.
- **Don't:** cut fast in the build (tension comes from holding, not cutting); make the brand or a health outcome the scary thing.
- **Preset:** `horror-tension` · deep card: genre-playbooks.md §1

## 2. Comedy skit / deadpan
- **What it is:** show a silly, over-complicated way first, then one person calmly does the obvious thing in one unbroken shot.
- **Use it when:** "their way vs the obvious way" or "what they say vs reality"; any brand with a simple truth to show.
- **The 5 beats (30 s):**
  1. 0-6 s: the premise: the over-complicated way, several 1-3 s shots with their own music (up to 12 s if it's funny by itself).
  2. 6-25 s: hard cut, music stops. ONE locked wide shot, 10-28 s, zero cuts. The escalation happens inside the shot.
  3. ~60-70 % in: the longest pause (0.5-1.7 s of stillness), then the punch.
  4. Last 1-3 s: the button: a signature gesture, a deadpan look to the lens, or a walk-off.
  5. +3-5 s (ads only): hard cut to the brand world, calm VO.
- **Real example:** Khaby Lame (khaby1) https://www.instagram.com/reel/DceEuVnii0u/ (9.7 M likes): a 12.3 s "life hack" premise, then 18.4 s in one take; his music stops the moment he walks in. The silence makes the obvious fix look even more obvious.
- **Example script (TITAN.AI, "How agencies write one caption"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-6 s | Fast shots: a 9-person meeting · a whiteboard "CAPTION BRAINSTORM v14" · sticky notes everywhere · a file "caption_FINAL_final2.docx". Header: "How agencies write one caption:" | upbeat corporate music |
| 6-7 s | Hard cut to one locked wide: Klaus alone at a desk, laptop, coffee | music stops dead; room tone |
| 7-14 s | He types one line, reads it, nods once. | keyboard clicks; 0.5 s dead air between actions |
| 14-19 s | He turns the laptop to the lens: the caption is done. He hits "schedule". | one click |
| 19-20.5 s | He just looks at the lens. Nothing moves. | silence (1.5 s) |
| 20.5-25 s | Punch: he scrolls; 30 more captions are already scheduled, a whole month. | one soft "ding" |
| 25-27 s | Button: both palms open to the lens, "that's it". | silence |
| 27-30 s | Logo + line over the same wide (Klaus still in frame) | VO: "One brief. A month of posts. TITAN.AI. Link in bio." |

- **Why it works (logic chain):**
  - Beat 1 makes the viewer feel the waste, so beat 2 can stay silent and still be funny.
  - The one-take makes the viewer trust nothing was faked, so the pause in beat 3 builds real anticipation.
  - The punch shows more than the premise asked for (a month, not one caption), so the CTA ("a month of posts") is the exact payoff.
- **Don't:** cut inside the deadpan take or let silence removal eat the pause; let the performer explain the joke (the header or premise tells it). Only show what the tool really does.
- **Preset:** `deadpan-comedy` (default, no crash zoom; Klaus's crash zoom = proposal B on his own skits) · deep card: genre-playbooks.md §2
- **Sub-styles:**
  - **2a Silent rebuttal** (`deadpan-silent-rebuttal`): the same, fully wordless, ends on the open-palm gesture. Works in every language (Khaby: 142.8 M followers).
  - **2b Quote vs reality** (`quote-reality-oneshot`): a persistent two-box header ("'AI will do it all for you'" / "The AI:") over ONE 8-12 s static take that contradicts it (corp1: 10.9 s, 0 cuts, 4 words).

## 3. Gen Z vlog / reaction
- **What it is:** raw phone footage with a reaction header on top the whole time, and a sound hit every time someone reacts.
- **Use it when:** a real-life funny moment (travel, street, banter) on organic accounts; the CTA goes in the caption.
- **The 5 beats (20 s):**
  1. 0 s → end: the header is up the whole time: a context emoji line + 2-4 CAPS reaction words + 😭💀.
  2. 0-3 s: the weird thing starts (no intro).
  3. 3-12 s: long handheld takes (4-6 s each); a sound hit on every reaction, every 1.5-2 s.
  4. Last third: the payoff (the funniest frame, punched in ~1.15×).
  5. No CTA card. The caption asks a question and carries the CTA.
- **Real example:** "Who upset lil bro?!" (Tyler Blunden, ref #1): 21 s, 5.7 M plays, only 3 cuts, hits at 0.5, 1.95, 3.35, 5.35 and 8.55 s. The header tells you how to feel before the footage proves it.
- **Example script (Snap Saigon, Bui Vien crossing):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-20 s | Header: "🇻🇳 first time in Saigon" / "NAHHH BRO 😭💀" | — |
| 0-4 s | Selfie walk: Khang (our snapper, cast/snap-saigon-influencer.md) walking backwards, Ben the backpacker behind him at the Bui Vien corner | Khang: "Okay Ben, rule one: just keep walking." · hit at 0.5 s |
| 4-9 s | A motorbike passes carrying a full-size fridge. Ben freezes, mouth open. | hit on the freeze · Ben: "Is that a FRIDGE?" |
| 9-14 s | Whip to a second bike: a family of four plus a dog. Ben grabs Khang's arm. | hit · Ben: "Sorry, is this… normal?" · hit |
| 14-17 s | Khang turns his camera round: the shot he just took, Ben mid-scream with the fridge bike behind | Khang: "Trust me bro. Photo of the trip." |
| 17-20 s | Punch-in on Ben's face, laughing | hit |
| Caption | "Who warned him?? 😭 Book a local snapper (link in bio) 🇻🇳 #saigon #hochiminhcity #vietnamtravel" | |

- **Why it works (logic chain):**
  - The header makes the viewer expect chaos, so the slow 4-6 s takes feel like waiting for it.
  - Each hit marks a reaction, so the viewer laughs on cue and stays for the next one.
  - The payoff is the photo, so the caption's CTA ("book a snapper") follows from what they just saw.
- **Don't:** jump-cut it into a frenzy (the ref has 3 cuts in 21 s); write the header as a title ("Saigon traffic") instead of a reaction. Brand copy never says "best" (Snap Saigon forbid-words).
- **Preset:** `genz-header-skit` · deep card: genre-playbooks.md §3

## 4. Trend beat-switch montage
- **What it is:** "My name is X, but they call me…", then one clip per beat of the music, each with one label word.
- **Use it when:** you have a list (roles, services, moods) and good existing clips; trend audio only on personal accounts, in-app.
- **The 5 beats (17 s):**
  1. 0-2 s: to camera, box caption 1: the setup ("My name is…").
  2. 2-4 s: box caption 2: the teaser ending in "…".
  3. ~4 s: the beat drops.
  4. 4-15 s: a new clip on every beat (1.2-2 s each), ONE centred label word each.
  5. Last clip: held for two beats.
- **Real example:** "My name is… but they call me…" (Alyson Hannigan, ref #6): 17.5 s, 4.9 M plays, cuts at 4.2, 6.1, 7.9, 9.3, 12.2, 13.9, 15.5 s. The intro is a fill-in-the-blank promise; every beat pays it off.
- **Example script (Klaus personal):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-2 s | Klaus to camera. Box 1: "My name is Klaus…" | trend sound intro (in-app) |
| 2-4.2 s | Box 2: "…but people call me a lot of things." | build |
| 4.2-6.1 s | Clinic, Klaus in navy scrubs. Label: "PHYSIO" | drop |
| 6.1-7.9 s | Laptop at night, three screens. Label: "FOUNDER" | beat |
| 7.9-9.3 s | Gym, spotting a mate who is clearly not lifting. Label: "SPOTTER" | beat |
| 9.3-12.2 s | Screen full of AI-generated shots. Label: "THE AI GUY" | beat |
| 12.2-13.9 s | Power Protein counter, holding a box. Label: "CUSTOMER #1" | beat |
| 13.9-17.5 s | Back to camera, deadpan. Label: "KLAUS" (held two beats) | last beat |

- **Why it works (logic chain):**
  - The "…" teaser makes the viewer wait for the list, so the drop pays off instantly.
  - Each label is one readable word, so the viewer can follow a 1.5 s clip and keeps counting.
  - The last held clip returns to the face from the intro, so the loop closes on who he is.
- **Don't:** cut off the beat (cuts must land on the music onsets); put two words or a sentence on a 1.5 s clip.
- **Preset:** `trend-beat-switch` · deep card: genre-playbooks.md §4

## 5. POV / relatable
- **What it is:** the camera is "you"; an actor talks straight into it as a type of friend everyone knows, three times, each worse.
- **Use it when:** you can name a recognisable type tied to the brand's problem; dialogue-led, no music.
- **The 5 beats (25-30 s):**
  1. 0 s → end: a persistent header "POV: the friend who…" (names a TYPE, not a situation).
  2. 0-8 s: vignette 1 in location A: one locked take into the lens; establish the trait; first word at 0.0 s.
  3. 8-18 s: vignette 2, location B, same outfit: the trait gets bigger. Dialogue at 200-225 wpm.
  4. 18-28 s: vignette 3, location C: the longest pause (1-1.7 s) right before the punch line, at ~65 % of the runtime.
  5. Last 2 s: a petty button line. No CTA card (caption carries it).
- **Real example:** pov1 https://www.instagram.com/reel/Dd9hI51P_aw/ (406 K likes): 3 vignettes (8.3 / 10.1 / 12.0 s), 223 wpm, a 1.72 s pause, then the punch "Emily?" at 67 %.
- **Example script (Physio Spot, "POV: the friend who googles every symptom"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-30 s | Header: "POV: the friend who googles every symptom" | no music |
| 0-8 s | Car, passenger seat. Dev into the lens, phone in hand. | "Bro, I googled it. It's either a pulled muscle or I have, like, three weeks. Google wasn't clear." |
| 8-18 s | Gym bench, same tee. | "Update. Reddit says posture, TikTok says chakras, and ChatGPT asked if I'd seen a professional. Rude. Who raised it?" |
| 18-25 s | Café. He scrolls a spreadsheet: "SYMPTOMS SINCE MARCH". You (off camera) slide a card across: "Physio Spot". He reads it. | "I've logged every twinge since March. Colour-coded." … (1.5 s silence) |
| 25-28 s | He looks up at the lens. | "…you mean ask an actual human?" |
| 28-30 s | Button: he pockets the card. | "Fine. But I'm bringing the spreadsheet." |
| Caption | "Tag your Dev. Questions about pelvic or men's health? WhatsApp Physio Spot (number in bio)." | |

- **Why it works (logic chain):**
  - The header names the type, so vignette 1 gets a laugh of recognition in the first second.
  - Each vignette raises the absurdity, so the pause in vignette 3 makes the viewer expect the worst.
  - The punch is the one sensible idea (ask a human), so the caption CTA is the punch line's own answer.
- **Don't:** add a music bed under the dialogue; make Dev a patient or promise any result ("my physio fixed me" is banned in SG health).
- **Preset:** `ugc-pov` · deep card: genre-playbooks.md §5

## 6. Absurdist / meme chaos
- **What it is:** one weirder-and-weirder picture after another, each with a big label, ending on the most ridiculous image, held.
- **Use it when:** the brand can laugh at itself (self-mockery only); short, sound-led, 5-16 s.
- **The 5 beats (label-escalation shape, 12 s):**
  1. 0-3 s: picture 1, centred and frontal, with a big label (a year, a rating, "Me:").
  2. 3-6 s: picture 2, weirder, new label.
  3. 6-8 s: picture 3, weirder still.
  4. 8-12 s: the most absurd image, held longest (chaos is in the picture, not the cut speed: typical shot 1.7-5.2 s).
  5. One hit on the final image; the track is the rhythm throughout.
- **Real example:** duo1 https://www.instagram.com/reel/DFttLM7ATju/ : 3 shots of ~5.3 s, each with a big year label, each weirder. Duolingo's "unhinged owl" grew from 50 K to ~16 M TikTok followers this way.
- **Example script (Power Protein, "Protein snacks through history"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | A grey bar on a plate, dust drifting off it. Label: "2015: CHALK" | licensed track starts |
| 3-6 s | A shaker bottle exploding in slow motion over a gym bag. Label: "2019: THE SHAKER INCIDENT" | track |
| 6-8 s | A protein muffin with a sad face drawn on. Label: "2022: 'HEALTHY' MUFFIN" | track |
| 8-12 s | A Power Protein bar on a velvet throne, wearing a tiny crown, a spotlight, a single tear on a fan. Label: "2026: THAO DIEN" (held 4 s) | one hit on the cut |
| Caption | "We did not choose the throne. The throne chose us. Order from the link in bio." | |

- **Why it works (logic chain):**
  - The labels form a timeline, so the viewer instantly gets the pattern and guesses where it ends.
  - Each picture is weirder, so the viewer stays to see how far it goes.
  - The final, most absurd image is the brand, so the joke and the product land on the same frame.
- **Don't:** cut fast and stack SFX ("stim every 1.5 s" is not what the measured memes do); mock customers, competitors or real people.
- **Preset:** `meme-chaos-short` (`genz-chaos` only for fast talking-head chaos edits) · deep card: genre-playbooks.md §6
- **Sub-styles:**
  - **6a Brand meme reply** (`brand-meme-reply`): a customer/trend clip (≤ 3.5 s) → the brand replies in character, one caps word per beat → a 1 s fake-card punch. 5-8 s total (Ryanair model). Fake prices must read as a joke; never in SG health.
  - **6b Lore roll-call** (`lore-rollcall`): 5-8 original characters, one per shot (median 2.7 s), a name tag top-right, the last one held 8-11 s. "Meet the TITAN agents". brain1: 445-691 K likes on single reels.

## 7. Drama / conflict (villain)
- **What it is:** a short scene that opens mid-fight, lets a villain go too far, then proof turns it around.
- **Use it when:** you want anger → justice and comments; the brand is the helper or the proof, never the villain.
- **The 5 beats (30 s):**
  1. 0-2 s: the cruel or accusing line, spoken from frame 1 (no establishing shot).
  2. 2-16 s: stakes, then escalation: shot-reverse-shot, typical shot ~1.5 s tightening to ~1.0 s.
  3. 16-18 s: the cruelty: the fastest cuts (0.3-0.8 s), then a hard stop and 0.8-1.3 s of total silence.
  4. 18-25 s: the evidence (a phone, a chat, a document), ONE held shot of 4-8 s. This is the turn.
  5. 25-30 s: the consequence lands, then a side-choosing question on the target's face (or "Part 2").
- **Real example:** Dhar Mann Studios https://www.instagram.com/reel/Da9ltsbPQAf/ (238 K likes): first word at 0.11 s, median shot 1.5 s, 137 wpm, and an evidence reveal that flips the scene.
- **Example script (Snap Saigon, dramatised with actors):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-2 s | MCU Jess (designer bag, ring light in hand), slight low angle, cathedral park behind | Jess: "You flew to Saigon and paid a stranger to take your photos? That's so sad." |
| 2-8 s | Reverse on Mai (eye level, warm light) · Jess · Mai | Mai: "He's a local photographer. I wanted one trip where I'm actually in the pictures." · Jess: "Babe, I have 80K followers. I'm the photographer." |
| 8-16 s | Faster singles (~1 s) | Jess: "My ring light cost more than your package." · Mai: "Okay." · Jess: "I'll post your selfie so everyone sees what 'local' looks like." |
| 16-18 s | Jess grabs Mai's phone, types fast (0.5 s cuts), sends a blurry selfie to the group chat: "look at this tragedy 😭" | then 1.2 s total silence on Mai's face |
| 18-25 s | Insert held 6 s: Mai's phone pings. A gallery link: "Your 40 edited photos + 3 clips are ready." She scrolls: golden shots at Nguyen Hue. | ping; low bed returns |
| 25-28 s | Jess's phone: the group chat now says "WHO TOOK THESE??" under Mai's gallery. Jess, quietly: | Jess: "…can I get his number?" |
| 28-30 s | CU Mai, deciding. Text: "Would you give her the number?" | bed out on the last word |
| Caption | "Same-day photos from a local snapper: link in bio. (Dramatisation.)" | |

- **Why it works (logic chain):**
  - The insult in beat 1 makes the viewer take Mai's side in two seconds, so the escalation feels unfair and keeps them.
  - The silence after the cruelty makes the viewer want justice, so the evidence (the real deliverable: 40 photos + 3 clips, same day) lands as the reversal.
  - The villain ends up asking for the brand, so the side-choosing question invites comments and the caption CTA is what Jess wanted.
- **Don't:** give the villain music or a hype stim; make the turn a speech (it must be evidence). Show only real package promises.
- **Preset:** `drama-conflict` · deep card: genre-playbooks.md §7 (+ villains-conflict.md)
- **Sub-style 7a Micro-drama episode** (`microdrama-episode`): 60-90 s episodes, one scene and one turn each, a cold open on the hottest line, a freeze-frame cliffhanger + "Part N+1". 8-12 episodes per brand season, same cast and sets (Gate 4 assets reused). The product is a plot device, not an ad break.

## 8. Class & status
- **What it is:** the same situation through two bank accounts (or one out-of-touch rich person), with both sides treated with respect.
- **Use it when:** you want recognition and shares; punch at behaviour and waste, never at being poor.
- **The 5 beats (20 s, two-hander dialogue):**
  1. 0-2.8 s: a persistent header states the class premise; the first absurd line is already spoken.
  2. 2.8-15 s: the volley: shot-reverse-shot at ~1.0 s per shot; each rich line escalates, each reply is 1-3 words.
  3. 15-19 s: the topper: the most absurd line, said casually, held a bit longer (1.5-2.8 s).
  4. Last 1-2 s: the normal person's silent face, held. No line.
  5. CTA in the caption (no end card). The normal side is the viewer's stand-in and gets the last look.
- **Real example:** Shabaz Says × Channel 4 https://www.instagram.com/reel/Czds85lsTIq/ (83 K likes, the top performer: a persona satire at 170-250 wpm). The two-hander spine below is C2 https://www.instagram.com/reel/DWOhh_VCAb_/ (5.7 K likes, 1.0 s median shot, 180 wpm).
- **Example script (TITAN.AI, "When a funded startup explains its content plan"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-20 s | Header: "When a funded startup explains its content plan:" | room tone only |
| 0-2.8 s | MCU Hugo (crisp linen shirt), one room, one light | Hugo: "So the content team flies to Bali every quarter." |
| 2.8-6 s | Thanh (hoodie) · Hugo · Thanh, ~1 s each | Thanh: "For…?" · Hugo: "Vibes." · Thanh: "Ah." |
| 6-11 s | Volley continues | Hugo: "Then a six-week discovery phase." · Thanh: "For a reel?" · Hugo: "Two reels." |
| 11-15 s | Volley | Hugo: "Legal reviews every emoji." · Thanh: "Which emoji?" · Hugo: "We're still deciding." |
| 15-18.5 s | Hugo, held, casual | Hugo: "Anyway. We posted once. In March." |
| 18.5-20 s | Thanh's face. He blinks. Nothing else. | silence |
| Caption | "Thirty posts a month, no Bali required. TITAN.AI, link in bio." | |

- **Why it works (logic chain):**
  - The header tells the viewer whose world this is, so every line reads as a joke from the first second.
  - The 1-word replies keep Thanh as the viewer's stand-in, so the escalation feels like their own disbelief.
  - The topper reveals the result (one post), so the silent face is the punch and the caption's "thirty posts" is the obvious answer.
- **Don't:** use split-screen or two colour grades (no measured class reel does; class lives in props and words); make the poorer side the joke.
- **Preset:** `class-two-wallets` (spines A, B, D) · `class-persona-satire` (persona spine) · deep card: genre-playbooks.md §8 (+ class-status.md)
- **Sub-style 8a Wordless parable:** two families in the same locked frame, 4-6 steps of 4-6 s, a reaction close-up per step, the two outcomes in one frame held 8-10 s. Under 10 words; the score carries it (C4: 5.2 K likes). The moral is about choices anyone can make.

## 9. Feel-good / emotional
- **What it is:** someone repeats a small kind act you don't understand, others doubt it, it goes quiet, then you see what it gave back.
- **Use it when:** festive films, brand love, values; the brand only appears at the end, as the enabler.
- **The 5 beats (30 s cutdown of a 90-180 s film):**
  1. 0-3 s: the act, no dialogue, a small header asking why.
  2. 3-12 s: the same act on different days: hands, details, 2-2.5 s shots.
  3. 12-17 s: doubt: someone mocks or shakes their head (2.5-3 s shots).
  4. 17-25 s: a quiet hole (music drops to room tone), then the reveal, held 4-5 s (8-11 s in the full film); music swells 2-3 s into the hold, not on the cut.
  5. 25-30 s: one slow wisdom line (≤ 60 wpm), then the title and logo over the last shot.
- **Real example:** Thai Life Insurance "Unsung Hero" https://www.instagram.com/reel/DWXnBo1DMbN/ (6 M views in its first week, 117 M+ on the original upload). The payoff hold is long enough to cry in.
- **Example script (Snap Saigon, real people with consent):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Dawn, Ben Thanh south gate. Snapper Bao photographs an old flower seller, Bà Lan. Header: "He does this every morning. Why?" | street ambience, soft guitar |
| 3-12 s | Different mornings (2-2.5 s each): rain, sun, her hands tying lotus stems, his shutter, her not looking up | guitar; shutter clicks |
| 12-17 s | A fellow snapper laughs at him and taps his watch; Bao runs late to a booking | colleague: "She never buys anything, you know." |
| 17-20 s | Bao at a print shop, a stack of photos coming out | music drops to room tone |
| 20-25 s | He hands Bà Lan an album: 100 mornings of her. She turns the pages slowly, then looks up at him, eyes wet. (held 5 s) | 2 s of room tone, then the guitar returns |
| 25-30 s | Bà Lan still turning the pages; handwritten title over the shot | VO (slow): "Everyone in this city is in someone's photo. Few get one of their own." · text over the shot: "Snap Saigon · Saigon, through a local lens" |

- **Why it works (logic chain):**
  - The header asks a question, so the repetition in beat 2 feels like clues, not filler.
  - The doubt makes the viewer half-agree "it's a waste", so the reveal flips them and lands harder.
  - The reveal is about photos, so the wisdom line and the brand line say the same thing and the brand feels earned.
- **Don't:** put the music swell on the cut (let the face land first); make the brand the saviour of real hardship or use anyone without consent.
- **Preset:** `feelgood-emotional` (cutdown: same preset, `target_s` [15, 30]) · deep card: genre-playbooks.md §9

## 10. Romance / aura (serial romance drama)
- **What it is:** open on the most charged moment, jump back in time, show how they got there, then end on a glance and "Part 2".
- **Use it when:** serial organic content or a light brand story; the product can be the thing they keep reaching for.
- **The 5 beats (30 s):**
  1. 0-3 s: cold open on the charged moment (a near-touch or loaded line), 1-2 slow-motion shots.
  2. 3-5 s: a time-jump line ("One week earlier") over the first flashback shot.
  3. 5-20 s: meet → friction; shot-reverse-shot at a ~2 s typical shot, glances held 1.5-3 s, music-forward, few words (≤ 60 wpm), name cards on first appearance.
  4. 20-26 s: the obstacle arrives as an object insert (a message, a ring, a ticket).
  5. 26-30 s: back to the cold-open moment, a glance back, a cut-away, "Part 2".
- **Real example:** "Irresistible Young Love, Ep 1" (iQIYI) https://www.instagram.com/reel/DewJSY9AquY/ : the C-drama shape (peak first, then "one day earlier", name cards, an object twist), median shot ~2 s. We copy the structure, not the explicitness.
- **Example script (Power Protein, organic and paid-safe):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Slow motion: two hands reach for the last protein bar on the counter at the same time; fingers almost touch | breath, low piano pad |
| 3-5 s | Empty café at dawn, chairs still up. Text over the shot: "One week earlier" | pad continues |
| 5-11 s | 6:10 am, Power Protein. Name cards: "An, 31 · runs at 6 am" / "Kai, 33 · runs at 6:05". He takes her usual window seat. She stares. | piano melody enters |
| 11-17 s | Next mornings: same order, same minute. She leaves him a note on the box: "my seat." He leaves one back: "my bar." Glances held 2 s. | piano; one small laugh |
| 17-20 s | She almost smiles. He almost speaks. | music lifts |
| 20-26 s | Insert: An's phone lights up on the counter: "Flight SGN → LHR · tomorrow 07:05". Both see it. | phone buzz; music thins |
| 26-30 s | Back to the hands: she lets go and slides the bar to him, walks out. He looks at the door. Text over the shot: "Part 2" | pad holds, cut on the door |

- **Why it works (logic chain):**
  - The cold open makes the viewer ask "how did they get here?", so the quiet morning routine plays like a countdown.
  - The notes build a private joke, so the flight insert hurts and creates the obstacle without a word.
  - The ending returns to the opening hands, so the loop closes and "Part 2" is a promise, not a cliffhanger trick.
- **Don't:** turn it into a slow golden montage with no story (serial and dialogue-led is what performs); promise attraction or any health result.
- **Line:** organic may go further (anything except private parts); paid ads stop at the kiss; adults 25+, original characters only (ledger [romance]).
- **Preset:** `romance-drama` (`aura-cinematic` stays for glow-up/statement edits) · deep card: genre-playbooks.md §10
- **Sub-style 10a Texting romance** (`romance-texting`): phone-real handheld episodes, the plot moves through message bubbles held 2-3 s over the shot, the reply lands on the other face, ends on a smile at the phone + "Follow for Ep 3" (r4: median 3.3 s, silences of 1.3-1.55 s kept).

## 11. Founder / comeback
- **What it is:** a real founder retells ONE scene where it could have gone wrong, in their own words, with details only they know.
- **Use it when:** trust and thought leadership; organic and Spark/Thought-Leader ads. Every number must be real.
- **The 5 beats (founder clip, 45-80 s):**
  1. 0-7 s: header with the stakes + the founder already mid-sentence (close-up, words from frame 0).
  2. 7-20 s: set the scene: where, who, what was at risk, one concrete number or object; cut close ↔ wide every 3-5 s.
  3. 20-45 s: the ask or the risk, quoted ("I said…", "she said…"), punch-in on the key line.
  4. 45-60 s: the turn: the line that changed it, then a beat on a reaction.
  5. Last 10-15 s: one-sentence lesson; the brand only as the result, no hard CTA.
- **Real example:** Sara Blakely (Spanx) https://www.instagram.com/reel/DC47FDWxlpv/ (11 K likes): 76.5 s, ~4.5 s average shot, a 7 s CAPS header, small sentence subs, no music (talk-led beats montage).
- **Example script (Klaus personal; placeholder story, swap in a real STORY card before filming):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-7 s | CU Klaus. Header: "The day I told my family I'd treat men's pelvic health" | "…and my [uncle] put his chopsticks down. Just put them down." (clean voice, no music) |
| 7-14 s | Wide: Klaus on a stool, interviewer in frame | "[Year], Lunar New Year dinner. Twelve people at one round table. I'd just quit my [hospital job]." |
| 14-20 s | CU | "I had [real number] saved and one rented room for a clinic." |
| 20-32 s | CU, punch-in on the quote | "He said, 'You studied four years to talk about THAT?' And the whole table went quiet." |
| 32-45 s | Wide, then CU | "I said, 'Uncle, half the men at this table won't talk about it. That's exactly why.'" |
| 45-52 s | Reaction wide: the interviewer laughs | (live laugh) |
| 52-60 s | CU, hold | "[Real detail of what happened next, e.g. who called first.]" |
| 60-70 s | CU, hold | "Lesson: the thing people are embarrassed to say is usually the thing they need most." (Physio Spot shown only as the clinic behind him) |

- **Why it works (logic chain):**
  - Starting mid-sentence makes the viewer lean in, so the scene-setting in beat 2 is answering their question, not delaying.
  - The quoted line makes the stakes personal, so Klaus's reply in beat 3 is the turn people repeat.
  - The lesson generalises the reply, so the brand appears as proof the bet worked, with no pitch needed.
- **Don't:** invent or round numbers ("overnight", "first in SG" need proof); talk about patient outcomes (SG health: his own journey only).
- **Preset:** `founder-clip` (default) · `founder-inspire` for a produced founder film (low → climb → peak, desaturated past → warm present) · deep card: genre-playbooks.md §11

## 12. Cautionary / decision ladder
- **What it is:** one small bad choice leads to a slightly worse one, faster and faster, until the cost lands; then one simple thing to do instead.
- **Use it when:** safety, PSAs, "don't ignore it" health education; the cost must be realistic, never a scare diagnosis.
- **The 5 beats (30 s):**
  1. 0-3 s: the ordinary want + a 0.5-1 s flash-forward of where this ends.
  2. 3-9 s: rung 1, the first shortcut, in a locked master frame (2-3 s shots).
  3. 9-20 s: rungs 2-3: the same frame or call, shots shrinking from 1.5 s to 0.7 s; cross-cut the enabler.
  4. 20-26 s: the consequence: one held shot, 4-6 s, no music hits.
  5. 26-30 s: one doable action (+ one sourced stat if you have it), then the brand's calm space.
- **Real example:** ThaiHealth "Phone" PSA https://www.instagram.com/reel/DY84J-VClM5/ (10.6 K likes): shots shrink from 1.98 s to 0.76 s as the friend's instructions stack, then a comic catch.
- **Example script (Physio Spot, "Ask the group chat"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-2.3 s | MCU Ben, 34, pumping up his bike tyre. Text: "Sunday: 100 km with the boys" | Ben: "Nothing's stopping this ride." |
| 2.3-3 s | Flash-forward insert (0.7 s): Ben on the sofa, phone showing the group's ride photo without him | one low hit |
| 3-9 s | Master frame: Ben at his desk, wincing, typing in the group chat (2-3 s shots) | Ben (reading): "Pelvic pain after long rides. Normal?" · Chat: "just stretch bro" |
| 9-14 s | Same frame, shots ~1.5 s: Chat: "take two painkillers and ride" · Ben nods · cross-cut his mate typing | typing ticks |
| 14-20 s | Faster, ~0.7 s: "real men don't do physio" · "harden up" · Ben clicks "Going ✅" | ticks speeding up |
| 20-26 s | Sunday, held 5 s: Ben on the sofa with a cushion, phone lights up with the group's ride photo | no music, room tone |
| 26-30 s | Calm Physio Spot room, Edison bulb flickers on. Text: "Pain that keeps coming back? Get it checked by a professional." [+ one SG-sourced stat if available] | VO: "Once you spot it, come to Physio Spot." · caption has the WhatsApp number |

- **Why it works (logic chain):**
  - The flash-forward tells the viewer where it ends, so every rung becomes "don't do it, Ben".
  - The shrinking shots make the bad advice feel like it is snowballing, so the long silent hold on the sofa lands as the cost.
  - The cost is a missed ride (proportionate), so the action "get it checked" is believable and the brand line follows naturally.
- **Don't:** keep rungs at an even 3-5 s (they must speed up); end on "don't be him" instead of one action; scare with a diagnosis or offer a discount/free consult.
- **Preset:** `cautionary-ladder` · deep card: genre-playbooks.md §12 (+ mature-edge.md §1)
- **Sub-styles:** **12a Ripple** (`cautionary-ripple`): the bad decision off-screen, then the consequence travels through people in 2-3 s shots under an ironic licensed upbeat song, ending on a 13 s hold (THINK! film). **12b Comedy-twist** (`cautionary-twist`): a repeated exchange (call, chat, sat-nav) steers him into an embarrassing but proportionate catch; dialogue only, one hit on the reveal.

## 13. Thriller / heist / suspense
- **What it is:** a heist told as a list of rules the viewer can follow, cut fast to a ticking clock, with one silent hitch before the escape.
- **Use it when:** "The rules of ___" (3 rules = 3 product truths) or "the heist" (the viewer's problem is the vault, the brand is the tool).
- **The 5 beats (30 s, "The rules"):**
  1. 0-2 s: the stakes line to camera ("In and out in 90 seconds.").
  2. 2-4 s: the title "THE RULES", big, over the host.
  3. 4-22 s: 3 rules × ~6 s: the rule as big text over its first insert (1 s) + inserts at a 0.6-1.0 s typical shot (hands, timers, screens), a click per insert.
  4. 22-25 s: the hitch: cuts stop, the music cuts out for ≥ 1 s.
  5. 25-30 s: the clean escape (the product's role), then the CTA as "Rule #4".
- **Real example:** Crime 101 "the rules of the heist" https://www.instagram.com/reel/DUJOUnrj2cU/ : host to camera on a black void, big serif rule cards, inserts at a 0.83 s median, 142 wpm (the spine below). The strongest in the set is the comedy heist https://www.instagram.com/reel/Csyv74MAu-e/ (3.4 K likes; flash-forward spine).
- **Example script (TITAN.AI, "The rules of a content heist"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-2 s | Klaus MCU on a black void | "One brief in. A month of posts out. Ninety seconds." · pulse bed 120 BPM |
| 2-4 s | Klaus holds on the void; cream serif "THE RULES" slams in over him | whoosh |
| 4-10 s | "RULE 1: NEVER START FROM A BLANK PAGE" over the first insert → inserts: hands paste a brief · timer 01:30 starts · cursor blinks (0.8 s each) | click per insert |
| 10-16 s | "RULE 2: ONE IDEA, THIRTY CUTS" over the first insert → inserts: a hook list scrolls · a calendar fills · 30 thumbnails tile in | clicks speed up |
| 16-22 s | "RULE 3: A HUMAN SIGNS OFF" over the shot → Klaus reads, crosses one line out, approves | click, click |
| 22-25 s | A message slides in: "Client: can we have it by today?" Cuts stop. Klaus looks at the lens. | bed cuts out: 1.2 s silence |
| 25-28 s | He turns the laptop: every post already scheduled. Timer stops at 00:04. | bass hit |
| 28-30 s | "RULE 4: SEND US THE BRIEF" over the scheduled screen | VO: "Link in bio." |

- **Why it works (logic chain):**
  - The stakes line sets a clock, so every insert feels like time running out.
  - The rules are the plan, so the viewer follows along like a crew member and expects a twist.
  - The hitch is the client's real fear (a deadline), so the escape proves the product's role and Rule #4 is the obvious next step.
- **Don't:** make it slow "cinematic heist" vibes without a plan (the slow AI heist got 3 likes); show any real crime method or a capability the product doesn't have.
- **Preset:** `thriller-suspense` · deep card: genre-playbooks.md §13

## 14. Mystery / reveal
- **What it is:** ask one specific, provocative question, drop clues, mislead once, go silent, then reveal a true answer.
- **Use it when:** retention matters most; "always be provocative" (Klaus): a strong curiosity hook, a light but true payoff.
- **The 5 beats (30 s):**
  1. 0-2 s: the specific question as text + the strangest frame.
  2. 2-20 s: 3 clues, 3-6 s each, each with ONE insert (partial framing, rack focus) and one sound.
  3. 20-24 s: the misdirect (the obvious answer).
  4. 24-26 s: 0.5-0.8 s of silence, then the reveal: the first frontal, fully lit shot.
  5. 26-30 s: a fast rewind of the clues (0.3-0.5 s each) re-read with the answer, then the CTA.
- **Real example:** "The Lampshade Evidence" https://www.instagram.com/reel/Dc-RntLBfcK/ (352 likes, narrated). Mystery evidence on IG is thin (3-352 likes); the strongest proof of the reveal shape is the evidence turn in Dhar Mann's 238 K-like drama (§7).
- **Example script (Snap Saigon "Saigon Stories", Central Post Office; every fact to SOURCES.md):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-2 s | The post office's iron arches from below, half in shadow. Text: "Everyone says Eiffel built this. Did he?" | VO (Hân, our host): "Every tour guide in Saigon tells you Gustave Eiffel built this post office." · low pad |
| 2-8 s | Clue 1 insert: rack focus to the iron roof trusses | VO: "Look up. Iron arches, like his tower." · tick, ding |
| 8-14 s | Clue 2 insert: the date on the façade, [1891] | VO: "The building opened in [1891], two years after his tower." · ding |
| 14-20 s | Clue 3 insert: [an archival record naming the architect], name out of focus | VO: "And the records name the architect. Not him." · ding |
| 20-24 s | The misdirect: an Eiffel portrait slides in | VO: "So it's Eiffel's, right?" |
| 24-26 s | 0.7 s silence. Then the name, frontal and lit: "[Alfred Foulhoux]" | reveal hit |
| 26-30 s | Rewind: trusses, date, record (0.4 s each) | VO: "[Foulhoux], the city's architect. Eiffel's name just sells better postcards." · CTA text: "Book a snapper who knows the stories: link in bio" |

- **Why it works (logic chain):**
  - The hook challenges something the viewer "knows", so they stay to see who's right.
  - Each clue looks solvable, so the misdirect feels like their own guess, and the silence makes them wait for the answer.
  - The answer is light but true and re-reads the clues, so the CTA (a snapper who knows the stories) promises more of the same payoff.
- **Don't:** use "wait for the end" as the hook (name the exact question); bait with a false or unverifiable claim (verify the architect and dates before posting).
- **Preset:** `mystery-reveal` (VO-led variant `mystery-narrated`: 246 wpm, one orange caps keyword per cut) · deep card: genre-playbooks.md §14

## 15. Action / sport hype
- **What it is:** effort and impact cut to the music, faster and faster, then the big moment shown in full.
- **Use it when:** 15a anthem = a message with pride (brand film); 15b gym/event hype = energy, recaps, PRs.
- **The 5 beats (15b gym hype, 20 s):**
  1. 0-1.5 s: a word-by-word title or the heaviest moment.
  2. 1.5 s → the drop: 1-2 beats per shot (~0.6-1.0 s).
  3. After the drop: one shot per beat (0.4-0.65 s), with bursts of 0.15-0.3 s.
  4. The money rep / finish: held uncut, 3-12 s.
  5. A 2-3 s end line over the finished lift.
- **Real example:** Nike "You Can't Stop Us" https://www.instagram.com/reel/Cy-JFIkyqgM/ (~60 M YouTube views, Cannes Lions 2021): match-cuts on motion across sports, the cut rate rising with the argument. For 15b, the 300 kg lift https://www.instagram.com/reel/DZ7owTXN8Yp/ holds the money rep 12.5 s uncut.
- **Example script (Klaus personal, PR day):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-1.5 s | Word by word: "LAST · SET · PR?" over the loaded bar | trend track (personal, in-app) |
| 1.5-6 s | 0.6-1.0 s shots: chalk clap · belt cinched · plates slid on · Klaus's eyes · his mate (the "spotter") filming | cuts on onsets |
| 6-10 s | Drop: 0.4-0.6 s shots + a 0.2 s burst: grip, breath, feet, crowd of three regulars | impacts on the beat |
| 10-17 s | The full lift, low side angle, ONE uncut take: setup, pull, lockout, plates settle | music under; real grunt and the bar's clang kept |
| 17-20 s | The lockout frame, held; over it: "[real weight] KG · DONE" · @handle | crowd yell |

- **Why it works (logic chain):**
  - The "PR?" title makes the viewer wait for one outcome, so every fast cut is build-up, not noise.
  - The speeding cuts raise the pulse, so the switch to one long uncut take feels like holding your breath.
  - The uncut rep is the proof (no cutaway to fake it), so the end card number is believed.
- **Don't:** cut away during the money rep or speed it up; promise transformations ("X kg in Y weeks") or use a patient as the athlete.
- **Preset:** 15b `action-hype` · 15a `sport-anthem` (provocation → slow-mo effort → match-cuts → 0.4-1 s peak burst → held payoff + line) · deep card: genre-playbooks.md §15

## 16. Sci-fi / tech launch
- **What it is:** a normal person in a real, warm place asks for help, and the product quietly does the work on real screens.
- **Use it when:** AI/product launches (TITAN.AI); future shown as human benefit in the present, not holograms.
- **The 5 beats (45 s, "human-day film"):**
  1. 0-3 s: cold open in a real place at dusk; a name card under 1 s; no claim yet.
  2. 3-12 s: the ask: MCU, 1.5-2 s shots; the person asks the product for something ordinary.
  3. 12-30 s: the product acts in-world: screen inserts ↔ the human reaction at ~1.7 s; a smile is the proof.
  4. 30-40 s: scale up: the same help, bigger (more people, more places).
  5. Last 3-5 s: one-line brand card on a solid colour; no feature list.
- **Real example:** OpenAI "Introducing dots" https://www.instagram.com/reel/Dd4RMfMJ7kO/ (50.6 K likes): warm wood rooms, practical lamps, real people, median shot 1.71 s, the product only on in-world screens.
- **Example script (TITAN.AI):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Dusk, a small café in District 3, chairs going up. Name card: "Hoa, owner" | room tone, airy score |
| 3-12 s | MCU Hoa at the counter laptop, tired. She types into TITAN.AI (1.5-2 s shots) | Hoa: "Can you turn today into tomorrow's posts?" |
| 12-21 s | Inserts ↔ her face, ~1.7 s: today's phone photos fly into a draft · a caption appears · a 15 s reel previews | soft UI chimes |
| 21-30 s | She laughs at one hook, edits one word, taps "schedule" | one chime |
| 30-40 s | Same evening, three other shops: a florist, a barber, a bánh mì cart, each closing up as their posts schedule | score builds |
| 40-45 s | Solid brand colour, logo | card: "TITAN.AI · Close up. We'll post." · bass swell |

- **Why it works (logic chain):**
  - The tired owner at closing time makes the viewer feel the problem, so the plain ask needs no explanation.
  - The product works on her real laptop and she edits one word, so it reads as help, not magic, and the viewer believes it.
  - Scaling to other shops says "this is for you too", so the one-line card closes the story instead of selling features.
- **Don't:** use the cyan-hologram look (it appears only in 1-like stock explainers); show a capability the product doesn't have.
- **Preset:** `scifi-tech` · deep card: genre-playbooks.md §16
- **Sub-styles:** **16b UI-proof launch** (`ui-proof-launch`): story cold open → a big title over the story shot at ~1.7 s → floating "input → result" UI cards → metric curves → stat cards (real, dated numbers) → story return → comment-to-DM CTA (Higgsfield S5: 2.9 K likes, 772 comments). **16c Concept sci-fi**: the cyan/holographic look only for literal future-world concepts, always with one warm human in frame.

## 17. K-drama
- **What it is:** a sincere Korean-drama romance played straight, then popped by a comic twist.
- **Use it when:** rom-com mini-films and product-placement gags; Korean visitors are a likely Snap Saigon audience.
- **The 5 beats (30-45 s):**
  1. 0-3 s: a header naming the premise + a wide of the lead hesitating.
  2. 3-20 s: attempt × 3 (rule of three): close-ups at 1.5-2 s; each fails faster; a 1-2 s silence before each rejection.
  3. 20-30 s: the real K-drama moment (rain, umbrella, car at night): a wide two-shot 4-6 s → CU → CU, OST enters, a held look of 3-5 s (the only long holds).
  4. 30-37 s: the twist: one line or object breaks the spell; hard cut, music stops.
  5. Last 3-4 s: logo or the product in the final frame.
- **Real example:** Wacky Willy "rejection" ad https://www.instagram.com/reel/DSRr7PTkc3E/ (4,050 likes): median shot 1.97 s, real silences (-43 dB) before each rejection, ends on a comic puncture, not a swoon.
- **Example script (Snap Saigon, Nguyen Hue; Korean with subtitles):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Header: "Why I'm scared to take couple photos:" · wide: Ji-woo holding his phone up, unsure | room tone |
| 3-8 s | Attempt 1, selfie: his arm too short, only her forehead in frame. She looks at it. | 1.5 s silence · Seo-yeon: "Delete it." |
| 8-13 s | Attempt 2: a passer-by takes it, thumb over the lens. | 1 s silence · "Delete it." |
| 13-20 s | Attempt 3: phone on a timer on a bench; a scooter drives through the frame. She just walks off. | scooter horn · no line |
| 20-26 s | Light rain. He runs after her with one clear umbrella. Wide two-shot from across the street, held 5 s. | rain; OST piano enters at 1.5 s |
| 26-30 s | CU her, looking up · CU him, holding her gaze (held 4 s) | piano |
| 30-37 s | CLICK. Khang (our snapper) leans out from behind a pillar, camera up. "Got it. Trust me bro, one more?" Both stare at the lens. | music stops dead; one comic sting |
| 37-40 s | The shot Khang took, with the logo over it | text: "Snap Saigon · your local snapper in Saigon" |

- **Why it works (logic chain):**
  - The header admits a fear everyone has, so each failed attempt is a laugh of recognition.
  - Three failures make the viewer want one perfect moment, so the umbrella hold feels earned and very K-drama.
  - The twist reveals someone was there to catch it, so the brand is the punch line and the CTA is the photo itself.
- **Don't:** hold every shot 3-5 s (only the romantic beat holds); use real actor lookalikes or school uniforms in romance.
- **Preset:** `kdrama-soft` · deep card: genre-playbooks.md §17
- **Sub-styles:** **17a Fan-edit** (`kdrama-fan-edit`): recut the brand's OWN K-drama footage to one song, median 0.63 s, 47 % of cuts on the beat, one persistent "POV:" header. **17b Self-aware PPL gag**: in the big moment someone hands over the product "out of nowhere" in slow motion while the other stares at the camera (Kopiko gag: 1,834 comments).

## 18. Anime-inspired (CM / jingle)
- **What it is:** a Japanese-TV-ad style jingle: flat 2D original characters, a chanted word on every shot, then the product held.
- **Use it when:** a product jingle or mascot chant; the song IS the ad (original, 90-100 BPM).
- **The 5 beats (30 s):**
  1. 0-1 s: a pastel field; the first chant word slams in; the character pops in.
  2. 1-12 s: chant verse: 0.3-0.6 s cuts on the beat, ONE big label per shot.
  3. 12-16 s: one proof card (a real, sourced fact), held ~2.5 s.
  4. 16-25 s: chorus: all characters together; cuts slow to ~1 s.
  5. Last 4-5 s: product + logo held; the final chant line sung once.
- **Real example:** Nissin Cisco "Gorogura" CM https://www.instagram.com/reel/DayFKseMzpH/ (2,603 likes on the repost): median 0.53 s slowing to 1.0 s into a 4.5 s packshot, ~91 BPM, zero flash frames; the label on every shot is the energy.
- **Example script (Power Protein, original chant at 92 BPM):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-1 s | Teal (#2ED3C7) field; "PRO!" slams in; a barbell-girl character pops up | chant: "PRO!" |
| 1-6 s | 0.5 s cuts: "TEIN!" · "POW!" · "ER!" · macro of a bar snapping · "CRUNCH!" · "CHEW!" | chant on each downbeat |
| 6-12 s | Character poses ↔ product textures: sleepy office guy wakes up · runner skids in · label "THAO DIEN!" | "Pro-tein! Pow-er! Thao Dien!" |
| 12-15 s | Proof card, a counter animating: "[X] g protein per bar (from the pack label)" | one whoosh |
| 15-25 s | Chorus: all three characters on a hill, cuts ~1 s | chorus repeats the chant twice |
| 25-30 s | Packshot: the bar + logo, held 4.5 s | sung once: "Power Protein!" · one impact |

- **Why it works (logic chain):**
  - The chant word on every shot gives the viewer something to read and hum, so 0.5 s cuts never feel confusing.
  - The proof card arrives after the hook is stuck in their head, so one real fact is enough.
  - The chorus slows the cuts, so the held packshot feels like the song's landing and the name is the last word sung.
- **Don't:** copy a real anime OP's song, studio or characters (original only, or licensed); put an unsourced stat on the card.
- **Preset:** `anime-energy` · deep card: genre-playbooks.md §18
- **Sub-style 18a Anime-OP parody** (`anime-op-parody`): "<X> be like (anime opening)": a 1.4 s setup card, then 9-12 trope shots at a 1.5 s median, a white label naming each trope, a ~3 s final hold. "Anime Openings Be Like" https://www.instagram.com/reel/C064YKqLshP/ (513 K likes). Original OP-style track only.

## 19. 3D Pixar / cartoon
- **What it is:** a cute 3D mascot acts out an idea, paced like a comedy or a feel-good short.
- **Use it when:** kid-safe or stigma-heavy topics where a character makes it easier to listen; see animation-3d-cartoon.md for the style key and character sheet.
- **The 5 beats (20 s) *[not measured; paced as comedy, 2-3 s shots]*:**
  1. 0-3 s: the mascot in trouble or confused (the problem as a gag).
  2. 3-8 s: the setup: what everyone gets wrong, one bouncy shot per idea.
  3. 8-14 s: the turn: a helper shows the simple truth.
  4. 14-18 s: the payoff gag (relief, a dance, a sigh).
  5. 18-20 s: a one-line takeaway + logo.
- **Real example:** no cartoon reel was measured. The closest measured 3D character win is studysongz "Skeletal Bones" https://www.instagram.com/reel/C3J3vLDuHKo/ (142 K likes): one continuous 3D animation, the named part enlarged as it's mentioned.
- **Example script (Physio Spot, "Your first pelvic health session, explained by a nervous cartoon"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Mascot "Bao the bean" (original 3D bean in a hoodie) hides behind a plant in a beige waiting room | VO (Bao): "I've booked a pelvic health physio. I'm going to faint." · boing |
| 3-6 s | Bao imagines: spotlights, a crowd, a microphone | Bao: "Will they make me talk about it in front of people?" |
| 6-8 s | The fantasy pops like a bubble | pop |
| 8-14 s | A calm physio character (original, navy scrubs) sits at eye level with a notepad | Physio: "First we just talk. I explain everything before we do anything, and you can say no to any part." |
| 14-18 s | Bao un-hides, sits down, exhales; a tiny dance in the chair | Bao: "Oh. That's… normal." · soft chime |
| 18-20 s | Bao sitting calmly in the chair; over the shot: "Questions? WhatsApp Physio Spot." + logo | warm room tone |

- **Why it works (logic chain):**
  - The panicking bean names the real fear (embarrassment), so the viewer laughs at a feeling they actually have.
  - The fantasy is bigger than reality, so the calm, factual explanation feels like relief, not a sales pitch.
  - The payoff is "that's normal", so the CTA (ask a question) is the next small, low-pressure step.
- **Don't:** use a mascot that resembles existing IP; slip in outcome claims because "it's only a cartoon".
- **Preset:** pace with `deadpan-comedy` or `feelgood-emotional` (no dedicated preset) · deep card: genre-playbooks.md §19 → animation-3d-cartoon.md

## 20. Documentary / investigative
- **What it is:** a narrated paper trail: you watch someone dig, then each document moves the story one step until the twist.
- **Use it when:** real stories and history (Snap Saigon "Saigon Stories"), research pieces; every fact sourced.
- **The 5 beats (60-90 s short):**
  1. 0-9 s: a cold open of *process*, not a talking head (searching, maps, a document coming out), near-wordless + one line.
  2. 9-15 s: the question, said plainly.
  3. 15-50 s: evidence beats of 6-10 s each, cut inside at a 1.2-2 s typical shot; each = a document or archive image + a source tag + one VO sentence.
  4. ~65 %: the turn: the paper trail reveals the twist.
  5. Last 5-10 s: what it means + the CTA.
- **Real example:** Johnny Harris https://www.instagram.com/reel/DRfLDUfk4qJ/ (5.3 K likes): ~9 s silent cold open of dead links and "video unavailable", then printed filings with a highlighter swipe, cut at a ~1.2 s median.
- **Example script (Snap Saigon, Ben Thanh Market; facts in brackets go to SOURCES.md first):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-6 s | Hands unfold an old city map on a café table; a magnifier slides over the riverbank | paper rustle, low bed (-22 dB) |
| 6-9 s | Today's Ben Thanh clock tower, wide | VO (Hân, our host): "This isn't where Ben Thanh Market started." |
| 9-15 s | Map close-up, a red circle near the river | VO: "So where did it start, and why does it keep the name?" |
| 15-25 s | Archive postcard of [the old riverside market] (source tag top-right) · 1.5 s cuts on details | VO: "[The first market stood by the river, near the old citadel.]" · paper slap on each image |
| 25-35 s | The map close-up again, the riverbank in focus; over it: "Bến = wharf · Thành = citadel" [verify] | VO: "The name means [the wharf by the citadel]." |
| 35-45 s | Archive photo of construction, date stamp "[1912-1914]" | VO: "[After the old market was lost], the city built this one, inland, [in 1912-14]." |
| 45-52 s | The turn: split, today's south gate vs the riverbank now | VO: "The wharf is gone. The citadel is gone. The name walked inland and stayed." · swell → impact |
| 52-60 s | Snapper's shot of a visitor at the south gate | VO: "Stand at the south gate and you're standing in a name that moved." · text: "Full story + sources in the caption. Photos here? Link in bio." |

- **Why it works (logic chain):**
  - The cold open shows someone searching, so the viewer starts searching too before a word is said.
  - Each document answers one small part of the question, so the viewer keeps watching for the next piece.
  - The turn explains the name, so the closing line gives the visitor a story to stand in, and the photo CTA fits that moment.
- **Don't:** open on a talking head or a slow title slate; state any fact without a source tag (and SOURCES.md).
- **Preset:** `documentary` · `doc-paper-trail` for investigations · deep card: genre-playbooks.md §20 (+ documentary-3d.md)

## 21. Explainer / myth-buster
- **What it is:** show the myth as people actually see it, look closely, show the real mechanism, then where the myth came from.
- **Use it when:** expert education (Physio Spot, TITAN.AI); fast talk, no dead air.
- **The 5 beats (45-70 s; voice from 0.0 s at 220-240 wpm):**
  1. 0-4 s: the myth as the artefact (a recreated post or the claim in its own words) + a provocation.
  2. 4-12 s: "look closely": the claim's own evidence, zoomed.
  3. 12-35 s: the mechanism with labelled evidence (diagram, model, props) and the expert in a corner; the layout changes every 4-6 s.
  4. 35-55 s: back to the face: why the myth hurts and who it hurts.
  5. Last 10 s: where the myth started (a dated receipt) + a one-line verdict.
- **Real example:** Dr Karan Rajan's toilet-paper myth https://www.instagram.com/reel/CxkzKPFs6Dx/ (75 K likes): voice at 0.0 s, 230-240 wpm, labelled evidence with the expert as a picture-in-picture. The slow control (104 wpm with gaps) got 30 likes.
- **Example script (Physio Spot, "Pelvic floor exercises are only for women"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-4 s | Recreated post card: "Pelvic floor exercises: for women after childbirth 💗" | Klaus: "If you think pelvic floor exercises are only for women, your body disagrees." |
| 4-12 s | Zoom into the post: every image is a woman; the word "men" appears nowhere | "Look closely. Every picture, every caption: women. Men don't even get a mention." · whoosh |
| 12-20 s | Labelled 3D pelvis, Klaus as a small PiP bottom-right: "pelvic floor", "bladder", "bowel" | "Men have a pelvic floor too. A sling of muscle from the pubic bone to the tailbone." · pop on each label |
| 20-28 s | Prop demo: a resistance band stretched between two hands as "the sling" | "It helps hold up your bladder and bowel, and helps you control when you go." |
| 28-35 s | Same band, a second label: "sexual function" | "It's part of sexual function too. That's anatomy, not a promise." |
| 35-50 s | Klaus to camera, mid-shot in the clinic | "So when men only hear 'that's for women', many never ask about pain or leaks. They sit on it for years." |
| 50-58 s | Receipt: [a dated search-results screenshot, private names masked] | "Most of what you've scrolled past was written for women. Fair. Just not complete." |
| 58-62 s | Klaus to camera; the verdict line over the shot | "Verdict: men have one. A physio can assess it. Questions? WhatsApp Physio Spot." · one impact |

- **Why it works (logic chain):**
  - The myth is shown exactly as viewers have seen it, so they feel personally addressed in the first second.
  - The anatomy is concrete and labelled, so the correction feels like a fact, not an opinion.
  - "Who it hurts" turns a fun fact into a reason to act, so the verdict ("a physio can assess it") is the logical CTA, with no outcome promised.
- **Don't:** talk slowly or leave gaps (dead air, not shot length, is what loses); say "cure", "fix" or any superlative (SG health).
- **Preset:** `myth-buster-stitch` (fallback `talking-head-punchy` when there's no evidence footage) · deep card: genre-playbooks.md §21

## 22. News / scam-expose
- **What it is:** a warning card in the first second, what the victim sees, how the trick works in numbered steps, one number, what to do.
- **Use it when:** "don't fall for this" posts; describe patterns, never name private people. Rotate spines, never the same one twice in a row.
- **The 5 beats (40 s, voiced):**
  1. 0-1 s: kicker card ("⚠️ CẢNH BÁO / SCAM ALERT") + a 6-word claim over the evidence, voice from frame 0.
  2. 1-8 s: what the victim sees, labelled "Example" or "Dramatisation".
  3. 8-30 s: how it works: 3-5 numbered beats, one idea each, 4-6 s per beat, B-roll cuts every 1.7-2.5 s.
  4. 30-35 s: ONE number (a counter) with its source line.
  5. Last 5-8 s: 3-4 numbered actions + the official helpline, then a 1-2 s logo.
- **Real example:** the strongest in the set is Hougang NPC's trick-on-the-viewer parody https://www.instagram.com/reel/DWkv0WID7gG/ (370 K likes, 5 M+ views; see 22b), up to 1,600× the same police family's plain advisories. The voiced spine below follows news pages at 2-4 K likes (N6-N8).
- **Example script (Snap Saigon, organic tip; Vietnamese first):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-1 s | Red kicker bar: "⚠️ CẢNH BÁO / SCAM ALERT" · "Đồng hồ taxi chạy nhanh hơn bạn / This meter runs faster than you" | news sting · VO: "Your Saigon trip can cost double." |
| 1-4 s | Dramatisation: Ben the backpacker (our cast) gets into an unmarked taxi at the airport (label "Dramatisation") | VO: "Not at the hotel. In the taxi." |
| 4-8 s | Close-up of a meter jumping (plates blurred) | VO: "Here's how the rigged meter works." |
| 8-14 s | "1" · the driver waves off the app: "no app, cheaper" | VO: "One: they skip the app 'to save you money'." · tick |
| 14-20 s | "2" · the meter digits jump faster than the street signs pass | VO: "Two: the meter runs fast, or 'breaks'." · tick |
| 20-26 s | "3" · drop-off, the driver shrugs: "no change" | VO: "Three: at drop-off, there's 'no change'." · tick |
| 26-30 s | Over the meter close-up: counter "[one official figure]" · small source line "[source, date]" | swell + impact |
| 30-37 s | Over Ben paying in an app car, the price on his phone: "What to do": 1 Use a ride-hailing app with the price fixed upfront · 2 Photo the taxi number · 3 Pay in small notes · 4 Report: [police 113 / official tourist hotline, verify] | VO reads the four lines · tick per line |
| 37-40 s | Logo pill | "Save this. Send it to whoever's visiting." |

- **Why it works (logic chain):**
  - The kicker and "cost double" give an instant stake, so the viewer stays for the "how".
  - Numbered steps make the trick learnable, so the viewer feels smarter at each tick and keeps going.
  - The actions answer each step (app vs skipped app, photo vs no meter, small notes vs "no change"), so "save this" is genuinely useful.
- **Don't:** open on an advisory slate or crest (7-10 s to the first word = the losing format); name or show a private driver, plate or business.
- **Preset:** `news-expose` (voiced) · `news-silent-case` (text-on-stock, no VO) · deep card: genre-playbooks.md §22
- **Sub-styles:** **22b Trick-on-the-viewer remix** (`scam-remix-onetake`): one 15-25 s take, direct address at ~220 wpm, three "you think X, but Y" reveals, a lesson line, a final reveal ("not even the real me"); at most ~1 post in 5, a new trick each time. **22c News-card carousel** (expander `carousel-text`, `card_style: kicker`): kicker + CAPS title → the artefact → 4 numbered steps → one sourced stat → what to do → who to call + "save this".

## 23. Commentary / receipts
- **What it is:** a real claim, the actual post, the context, what the data says, your verdict, with the other side argued fairly once.
- **Use it when:** a real controversy or viral claim; opinion labelled, every claim in SOURCES.md, no AI likeness of real people.
- **The 5 beats (40 s) *[not measured; 2-3 s evidence beats]*:**
  1. 0-3 s: the claim on screen + your one-line stance.
  2. 3-10 s: the receipt: the actual post or clip (screenshot or short excerpt).
  3. 10-18 s: steelman: the best version of their side.
  4. 18-32 s: what the data or source says, one card per point.
  5. 32-40 s: your verdict (labelled opinion) + a question for the comments.
- **Real example:** not measured; the format lives in commentary-controversy.md (receipts format). The nearest measured shape is §21's myth-buster (75 K likes).
- **Example script (Klaus personal, "AI will replace every marketer by 2027"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Quote card of the viral claim (handle masked unless public figure; tag in caption) | Klaus: "This post says AI replaces every marketer by 2027. I run an AI agency. Let's check." |
| 3-10 s | The post itself, zoomed on the claim and its likes | "[N] likes. No source. Just vibes and a robot emoji." |
| 10-18 s | Klaus to camera, softer | "To be fair: AI already writes first drafts faster than any of us. That part is real." |
| 18-25 s | Over B-roll of a job-board scroll: "[sourced figure on marketing job postings, year]" (small source line) | "But here's [source]: [what it shows]." · pop |
| 25-32 s | Screen recording: TITAN.AI drafts with Klaus's edits in red | "And in our own work, every AI draft still gets a human edit before it ships." |
| 32-38 s | Label "OPINION" top-left; Klaus to camera | "My take: AI replaces tasks first. The marketer using it replaces the one who doesn't." |
| 38-40 s | Klaus to camera; text over the shot: "Agree or nah?" | (caption tags the original post's creator) |

- **Why it works (logic chain):**
  - The stance plus "let's check" makes the viewer expect a verdict, so the receipt is the first payoff.
  - Steelmanning first makes the viewer trust the critique, so the data lands as fair, not as a rant.
  - The verdict is labelled opinion and ends on a question, so comments argue the idea, not the person.
- **Don't:** fabricate quotes or put a real person's face/voice in AI; skip the source line on any number.
- **Preset:** `documentary` (or `talking-head-punchy`) · deep card: genre-playbooks.md §23 → commentary-controversy.md

## 24. Luxury / product reveal / new release
- **What it is:** a flash of the product, a short dream of the world it belongs to, then the product held still at the end.
- **Use it when:** launches and premium products; three shapes: narrative film, calm object film, FOOH (impossible CGI product in a real street).
- **The 5 beats (30 s, narrative):**
  1. 0-1.6 s: the brand flash: the product for 0.5-1 s, then cut to the world.
  2. 1.6-12 s: the story: fast cuts, typical 0.85 s, about half on music onsets.
  3. 12-20 s: emotional peaks held 3-4 s between the fast cuts.
  4. 20-26 s: the story returns to the product in use.
  5. 26-30 s: the hero packshot held 2-4 s + the name.
- **Real example:** Bleu de Chanel L'Exclusif cut https://www.instagram.com/reel/DY42Z6-ScTk/ (8,042 likes): 27 cuts in 30 s, median 0.88 s, the bottle at 1.1-1.6 s and again for the last ~2 s.
- **Example script (Power Protein, new flavour launch; flavour is an example):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-0.8 s | Darkness; a thin light sweep catches the new bar's black wrapper | sub hum |
| 0.8-1.6 s | Cut to dawn: Thao Dien riverside path, a runner's shoes | score starts |
| 1.6-8 s | 0.8 s cuts on the beat: breath in cold air · a hand pulls a zip · river light · a café shutter rolling up | whoosh peaks on fast cuts |
| 8-11.5 s | Held 3.5 s: the runner stops, hands on knees, the city waking up behind | music breathes |
| 11.5-20 s | Fast again: the counter at Power Protein · a hand snaps the bar · slow-motion crumbs of black sesame (held 3 s) | crack, crumbs (real foley) |
| 20-26 s | The runner on a bench, one bite, eyes closed, sun up | whispered: "Black Sesame." |
| 26-30 s | Centred packshot on black, held 3 s: "BLACK SESAME · NOW AT POWER PROTEIN" | sub boom |
| Caption | "[Real launch date, price and where to buy.]" | |

- **Why it works (logic chain):**
  - The opening flash tells the viewer what this is about, so the fast story never feels like a random montage.
  - The holds put feelings (calm, a waking city) between the cuts, so the viewer wants the moment, not just the snack.
  - The crumbs shot makes the product sensory, so the held packshot is the object they take away.
- **Don't:** cut everything at the same speed (the calm object film has no cut under 2.5 s; the narrative needs its holds); invent scarcity or prices.
- **Preset:** `luxury-reveal` (narrative) · `luxury-object-calm` (8-10 shots of 2.5-3.5 s) · `fooh-oneshot` (one 7-8 s take, the scale reveal at 60-85 %; Jacquemus bags https://www.instagram.com/reel/CqqN8w6K3rL/ , ~2 M likes on the campaign) · deep card: genre-playbooks.md §24

## 25. UGC demo / experience-style
- **What it is:** a real person picks up the product on their phone and shows it working: problem, use, result.
- **Use it when:** trust and conversion on paid social; real people beat generated ones; never posed as customer testimony in regulated markets.
- **The 5 beats (25 s) *[not measured in this run; ugc-* presets]*:**
  1. 0-3 s: the problem in the creator's words, face to camera.
  2. 3-8 s: the product appears (screen, box, hands).
  3. 8-16 s: using it, 1.5-3 s shots, face ↔ screen.
  4. 16-22 s: the result, shown, not claimed.
  5. 22-25 s: a keyword or link CTA.
- **Real example:** "Build your own AI video editor with Claude Code" (millee.md, ref #9): 18.3 K likes and 10.2 K comments from a "comment MOTION" CTA; split layout, 2.7 s median, 256 wpm.
- **Example script (TITAN.AI, Klaus as himself):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Selfie in a Grab car, voice note waveform on screen | "I gave our AI a 2-minute voice note I recorded in traffic." |
| 3-8 s | Screen recording: the voice note dropped into TITAN.AI | "No script. Just me complaining about hooks." |
| 8-13 s | Split: face top, screen bottom; five hooks appear | "It pulled out five hooks. Number three is actually mean." |
| 13-18 s | He reads hook 3 aloud, laughs | "'Your content isn't bad. It's just invisible.' Rude. Correct." |
| 18-22 s | The finished 15 s reel plays in the bottom half | "Then it cut the reel. I changed one word." |
| 22-25 s | Face, CTA text "Comment HOOKS" | "Comment HOOKS and I'll send you the prompt." |

- **Why it works (logic chain):**
  - A messy voice note is a problem everyone has, so the demo starts from the viewer's real situation.
  - Reading the hook aloud shows the result instead of claiming it, so the viewer judges it themselves.
  - The CTA gives away the exact thing they just watched work, so commenting is an easy yes.
- **Don't:** script fake "real" reactions or pose staff as customers; show output the tool didn't really make.
- **Preset:** `ugc-selfie-talking-head` (also `ugc-unboxing`, `ugc-try-on-demo`, `ugc-reaction`, `ugc-day-in-the-life`, `ugc-green-screen`, `ugc-testimonial-style`) · deep card: genre-playbooks.md §25

## 26. Before / after transformation
- **What it is:** show the worst "before" first, the satisfying process, then the same framing again as the "after", side by side.
- **Use it when:** proof of change (objects, spaces, files, screens); in SG health, never people.
- **The 5 beats (20 s ad, "reveal last" variant):**
  1. 0-1.5 s: the worst view of the before + a title.
  2. 1.5-5 s: process beat 1 (0.6 s detail cuts, or a locked one-take time-lapse).
  3. 5-14 s: process beats 2-5.
  4. ~70 % (14 s): back to the exact before framing → a wipe to the after.
  5. Last 3-5 s: a BEFORE | AFTER split card held ≥ 2 s, then the CTA.
- **Real example:** pink rug restoration https://www.instagram.com/reel/DR4YtfODqnh/ (18.8 K likes): one locked overhead camera for 179 s (median shot 7 s), the dirty rug visible at 0 s, a wipe-split BEFORE | AFTER card in the last 3 s.
- **Example script (TITAN.AI, our own content folder, screen recording):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-1.5 s | Locked screen: a desktop with 400 files, "final_v9_REAL.mp4". Title: "Our content folder, Monday 9 am" | messy click sounds |
| 1.5-5 s | 0.6 s cuts: files sorted into Hooks / Reels / Captions | soft swooshes |
| 5-10 s | 0.6 s cuts: captions drafted · a calendar filling day by day | typing ticks |
| 10-14 s | 0.6 s cuts: thumbnails rendering in a grid | pops |
| 14-17 s | Same framing as 0 s → wipe to the clean desktop: one folder, "OCTOBER - SCHEDULED" | whoosh on the wipe |
| 17-20 s | Split card held 2.5 s: BEFORE | AFTER, same screen | ding · CTA text: "Your folder next? Link in bio." |

- **Why it works (logic chain):**
  - The before opens a loop ("can they fix THAT?"), so the viewer stays through the process.
  - The process is satisfying on its own, so the middle never sags.
  - The after uses the exact same framing, so the split card is proof, and the CTA offers the same change.
- **Don't:** change the framing or light between before and after; show people before/after for SG health brands (process, objects or spaces only).
- **Variants (Klaus):** build at least 2 and test: snap-first (after flashes at 1-2 s), reveal mid-way, reveal last.
- **Preset:** `before-after-process` (one-take/slow) · `before-after-fast` (0.6 s detail cuts) · deep card: genre-playbooks.md §26

## 27. ASMR / satisfying
- **What it is:** one continuous, close, loud-sounding action from empty to finished, no talking, no music, then it loops.
- **Use it when:** food, products with texture and sound; the sound is half the format.
- **The 5 beats (one-take, 20 s):**
  1. 0-0.5 s: the action has already started.
  2. 0.5-8 s: one locked shot, the first layers or steps.
  3. 8-17 s: the build continues in the same shot (no cut).
  4. 17-20 s: the finished object held 2-3 s.
  5. Loop: the last frame cuts cleanly back to the first.
- **Real example:** "Ultimate Kinetic Sand Drop & Squish" https://www.instagram.com/reel/DaQQ9EuuNu4/ (44.7 K likes): one 19.7 s take + a 2.2 s hold, -17.9 LUFS with 53.6 sound hits per 10 s. The brand's own silent version (-45.9 LUFS) got 66 likes.
- **Example script (Power Protein, the parfait build):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-0.5 s | Locked side-on macro: a clear glass, granola already pouring in | granola rattle (close mic) |
| 0.5-5 s | Granola settles; a spoon presses it flat | crunch, press |
| 5-10 s | Thick yoghurt poured in one slow ribbon | glossy pour |
| 10-14 s | Berries dropped one by one | soft plops |
| 14-17 s | A protein bar snapped over the top, crumbs fall | sharp snap, crumbs |
| 17-20 s | The finished glass, still, held 3 s | room tone · loop to frame 1 |

- **Why it works (logic chain):**
  - The action is already happening at 0 s, so there's nothing to skip and the viewer is hooked by the sound.
  - One continuous shot means the viewer must stay to see it complete.
  - The finished hold satisfies the loop they opened, and the clean loop makes them watch it again.
- **Don't:** cut away, add music or talk over it; open on a logo or billboard (the 18-like snack reel broke the ASMR promise in its first 6 s).
- **Preset:** `asmr-satisfying` (one-take default) · `asmr-product-cut` (ads: 0.7-1.5 s shots, each completing one sound) · deep card: genre-playbooks.md §27

## 28. Event / retail / mall promo
- **What it is:** a 15-25 s virtual walk-in: the door, the product, hands trying things, then the bag or the when-where card.
- **Use it when:** openings, pop-ups, launches; a real discount can open it when it makes people want the product (never for SG health).
- **The 5 beats (20 s with VO):**
  1. 0-1 s: the storefront or the hero product with the real offer on it.
  2. 1-3 s: the dates said in the first 3 s (VO ~140 wpm).
  3. 3-10 s: 1 s inserts on the beat: hero product → hands using the activation.
  4. 10-17 s: the freebie or photo moment → a walk-through.
  5. Last 2-3 s: a bag-out with the what-where-when text over it, held ≥ 2 s.
- **Real example:** POP MART opening, Mall of America https://www.instagram.com/reel/DQxooZQEaIl/ (627 likes on a mall account): 10.7 s, median 1.03 s, storefront at 0 s → 7 hero inserts → a shopper walks out with the bag. (Mall reels get hundreds of likes; the pacing is solid, the reach comes from the anchor product.)
- **Example script (Power Protein's birthday weekend; offer and dates are placeholders):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-1 s | Storefront, Xuan Thuy street, a teal balloon arch; text on the hero bar: "[real offer]" | licensed upbeat track · VO starts |
| 1-3 s | Hero bar on the counter | VO: "Power Protein turns one: [Sat-Sun, date], Thao Dien." |
| 3-7 s | 1 s inserts on the beat: a smoothie blender · a hand grabs a bar from an ice tray · the menu board | VO: "[Offer, exactly as on the terms]." |
| 7-10 s | Hands at a "build your own bowl" station | VO: "Build your own bowl." |
| 10-14 s | Photo wall moment (staff and consenting creators only) · free tasting cups [with terms] | VO: "Free tastings, [hours]." |
| 14-17 s | Walk-through past the shelves, ending at the door | track |
| 17-20 s | A customer walks out of the door with the bag; over it, held 3 s: "[Date] · [hours] · [address], Thao Dien · terms in caption" | pop |

- **Why it works (logic chain):**
  - The offer on the product makes it worth stopping for, so the dates in the first 3 s are heard.
  - The hands-on inserts let the viewer rehearse the visit, so they picture themselves there.
  - The closing text repeats when and where, so the viewer leaves with everything they need to come.
- **Don't:** open on a bare price slide or a fake countdown ("10 % off every $88" was the 3-like low performer); film identifiable shoppers without consent.
- **Preset:** `event-guide-vo` (with VO) · `event-retail-promo` (music only, 0.8-1.0 s median) · deep card: genre-playbooks.md §28

## 29. Edu-song / mnemonic
- **What it is:** a catchy song that teaches one list or diagram, with the picture changing on every line.
- **Use it when:** anatomy, steps, checklists, PSAs; study content people save. Brand accounts: original or public-domain melodies only.
- **The 5 beats (30 s study song):**
  1. 0 s: the song starts AND a value-promise header is on screen (held 8-12 s). No intro, no count-in.
  2. 0-10 s: section 1: one fact per line; the diagram changes every 1-2 s; the named part lights up as it's sung.
  3. 10-20 s: section 2, with a new persistent step label.
  4. 20-25 s: the recap/count line with every label on screen at once.
  5. 25-30 s: end (optional 1.5 s logo over the diagram); the CTA lives in the caption ("save for your exam").
- **Real example:** AsapSCIENCE mitosis song, filmed off a monitor https://www.instagram.com/reel/C6LnMbiiLuT/ (302 K likes): singing at 0.0 s, header "If you study biology and you don't know this song…", a step label per phase, one phone take. Adult study songs run at 3.0-3.4 syllables per second (close to rap); slow kids' songs got no saves.
- **Example script (Physio Spot, proof-screen song, original beat at 92 BPM):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-2 s | Phone filming a clinic monitor: an animated pelvis diagram. Header (held to 10 s): "Men: you have a pelvic floor. Here's the song." Step label: "1. Where it is" · the pubic bone lights up | sung from 0.0 s: "From your pubic bone…" |
| 2-10 s | The tailbone lights up, then the sling between them, then the organs above it (a change every ~2 s) | sung: "…to your tailbone, a sling / a muscle hammock underneath / holding everything" |
| 10-20 s | Step label: "2. What it does" · bladder, bowel, then a "control" valve icon light up in turn | sung: "Holds the bladder, holds the bowel / helps you hold it, helps you go / plays a part in sex as well / now you know" |
| 20-25 s | All labels on screen at once | sung count line: "Support, control, function: that's the floor." |
| 25-30 s | Hold on the full diagram; small logo corner | last chord rings out |
| Caption | "Save this for later. Questions? WhatsApp Physio Spot." | |

- **Why it works (logic chain):**
  - The header promises a fact the viewer probably didn't know, so the song starting at 0.0 s already pays it off.
  - The diagram lights up on every line, so the eye and the ear learn the same thing at once.
  - The count line compresses it into three words, so "save this" is a real use, not a request.
- **Don't:** open with a 4-5 s instrumental intro (the low performers did); sacrifice accuracy for a rhyme (every lyric is a clinical claim, so run the compliance pack line by line).
- **Preset:** `edu-song-screen` (one-take proof screen, the cheapest winner) · `edu-song` (3D mascot cut) · `editor.py song` checks the syllable fit · deep card: genre-playbooks.md §29 (+ edu-songs-mnemonics.md)
- **Sub-style 29b Brand PSA song:** an original melody, one cute character per verse doing a "dumb" thing, the message as the chorus, a dance simple enough to copy (Dumb Ways to Die: 50 M views in ~7 months). Researched, not measured.

## 30. Texting / receipts suspense
- **What it is:** someone retells what was said, and the actual texts appear as chat bubbles over their shot (dimmed and blurred behind the bubbles), bubble by bubble, until the line the story turns on.
- **Use it when:** "they told me…" stories; real messages need both people's consent, recreations say "dramatised"; never patient chats.
- **The 5 beats (45-90 s):**
  1. 0-3 s: the most shocking text, alone and large, over a dim frame of the speaker.
  2. 3-20 s: the speaker sets the stakes (locked interview shot, warm light).
  3. Each "they texted" moment: the bubbles pop in over the speaker's shot (dimmed, 4-7 s), one by one, with a typing dot before each reply. Default: over the footage; variation: the full-black chat card of the measured ref.
  4. The turn (the twist): a hard cut to the speaker's own reaction close-up, with the punch message large over it, then a beat of silence.
  5. The aftermath on the speaker's face, then the CTA or "full story".
- **Real example:** the "MUSK" documentary reel (@muskdoc, ref #7): 91.2 s, 93.6 K likes, average shot 6.1 s, a hit or pulse every 1-3 s, the turning line shown alone ("I have over 10 thousand lasers in space right now.").
- **Example script (Klaus personal; dramatised recreation, details to confirm):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Klaus's lamp-lit desk, dimmed and blurred; one large bubble over it: "Can you make it go viral by Friday?" | drone bed; one hit |
| 3-12 s | Klaus, locked mid-shot, lamp light | "A client sent me that at 11:48 pm. It was Wednesday." |
| 12-19 s | Bubbles over Klaus's shot (dimmed): me "Viral isn't a deadline." · typing… · them "My competitor did it. 2 million views." · me "Send me the link." | tick per bubble |
| 19-26 s | Klaus | "So I opened the link. And I recognised the edit. Same hook ladder, same captions. Then I saw who made it." |
| 26-30 s | The twist: hard cut to Klaus's CU, frozen mid-blink; the punch large over it: "That's ours. We made it." | silence (1 s) |
| 30-36 s | Bubbles over Klaus's shot (dimmed): them, typing… stops… typing… "Can I book the same team?" | ticks, then a soft laugh from Klaus under the bubbles |
| 36-45 s | Klaus's face, then a small smile | "Viral isn't a deadline. It's a habit. We post the boring version every day until one isn't boring." · text: "Full story on the channel" |

- **Why it works (logic chain):**
  - The opening text is an impossible ask, so the viewer wants to know how he answers.
  - The bubbles let the viewer read ahead of the voice, so they guess the turn and get it twice (read + heard).
  - The punch flips who has the power, so the lesson ("a habit, not a deadline") lands as earned, and "full story" promises more.
- **Don't:** put captions over the bubbles (the voice runs underneath; the bubbles are the text); cut to a plain black page for commentary or titles; show a real person's private messages without consent.
- **Preset:** `texting-suspense` (beats carry `chat`, rendered by chatanim) · deep card: genre-playbooks.md §30

## 31. Borrowed cold open / bait-and-switch
- **What it is:** open on a moment everyone recognises, then "skip" to you and teach something, keeping the same layout.
- **Use it when:** a lesson needs a scroll-stopper. Format-jack (recreate it with our people) is fully owned; clip-jack uses the real clip (`editor.py collab add`, creator tagged in the caption, no on-screen credit).
- **The 5 beats (35 s):**
  1. 0-3 s: the most recognisable moment of the borrowed bit, no intro.
  2. 3-10 s (up to ~15 s): let it run only while it still delivers.
  3. The switch: a UI "skip" (video-chat next, a channel change, a record scratch) into you, same frame/layout.
  4. The lesson: 3 numbered steps, a list growing on screen, one CAPS word per beat.
  5. Keep a reaction element running (the other window's face), then the CTA.
- **Real example:** Omegle "ex-lovers" clip → "3-step scaling roadmap" (Vaughn Major, ref #8): 40.9 s, one cut that matters at 16.3 s; the other window's face keeps "reacting" to the lesson.
- **Example script (TITAN.AI, format-jack with our own actors):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Video-chat UI, split top/bottom. Top: a stranger, Linh. Bottom: Khoa. | Linh: "Wait. Why do you look like my old intern?" |
| 3-10 s | Both lean closer | Khoa: "…Linh?" · Linh: "KHOA? You said you'd 'go viral and never come back'." · Khoa: "I posted for a year. 200 views." |
| 10-11 s | The top window "skips": NEXT → Klaus appears | skip whoosh |
| 11-17 s | Klaus top, Khoa still bottom, nodding | Klaus: "If you've posted for a year and nothing grows, here are 3 fixes." · list appears: "1." |
| 17-23 s | List: "1. HOOK IN SECOND ONE" | "One: your first second has to make a promise. Not a logo." |
| 23-29 s | List: "2. ONE IDEA PER POST" · Khoa writes it down | "Two: one idea per post. If you need 'also', it's two posts." |
| 29-33 s | List: "3. REPOST THE WINNER" | "Three: when one works, post it again with a new hook." |
| 33-35 s | Khoa gives a thumbs up · text "Comment HOOK for our hook list" | Klaus: "Comment HOOK." |

- **Why it works (logic chain):**
  - The reunion is a moment people already love, so the first 10 s cost no attention.
  - Khoa's "200 views" sets up the exact problem, so the skip to Klaus feels like the answer, not an interruption.
  - Khoa stays on screen taking notes, so the joke keeps running and the "Comment HOOK" CTA continues the lesson.
- **Don't:** run the borrowed bit after it stops delivering; let the switch misrepresent (no fake news or fake patient footage).
- **Preset:** `talking-head-punchy` or `genz-header-skit` + B-roll `mode: split` (music-led: `trend-beat-switch`) · deep card: genre-playbooks.md §31

## 32. Absurd how-to (narrated 3D)
- **What it is:** a calm cooking-show voice explains an impossible task step by step; it ends on a wordless twist.
- **Use it when:** a series with a recurring character; the "recipe" must be safe, true advice underneath the joke.
- **The 5 beats (38 s):**
  1. 0-2.5 s: the absurd action is already happening; VO: "First, X. But don't just Y."
  2. 2.5-5 s: an open-loop aside ("This is our last recipe…").
  3. 5-30 s: one step per shot, 2-2.5 s each, an imperative verb on every cut (~200-210 wpm).
  4. 30-34 s: the sensory payoff, the longest hold (3.5-4.5 s).
  5. 34-38 s: the wordless twist, then the series name over the last shot.
- **Real example:** @storygoaten "How to Cook a Carnotaurus Leg" (ref anim1, 140 K likes, 1,773 comments): 38.7 s, a caveman on a cobalt grid void, one step per 2-2.5 s shot, foley on every verb, a callback twist.
- **Example script (Snap Saigon, "How to cross a Saigon street, Stone Age edition"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-2.5 s | 3D caveman at a kerb on the blue grid void; a river of motorbikes flows past | VO (calm): "First, find the crossing. But don't trust the stripes." · engine whoosh |
| 2.5-5 s | He looks back at an empty cave | VO: "This is the last tip my tribe ever gave me." |
| 5-10 s | He raises one hand, palm out | VO: "Raise one hand. Be seen." · bikes slow |
| 10-15 s | He steps off the kerb | VO: "Walk. Slowly. Like a turtle with somewhere to be." · footstep |
| 15-20 s | Bikes bend around him like water | VO: "Never run. Never stop. The bikes flow around you." · whoosh, whoosh |
| 20-25 s | A bánh mì cart glides past his face | VO: "Ignore the bánh mì. It's a trap." · sizzle |
| 25-30 s | Last lane | VO: "Keep the same speed. They're reading you." |
| 30-34 s | He reaches the far kerb; a cold coffee is waiting; long slurp (held 4 s) | ice clink, slurp |
| 34-38 s | Wordless: he turns; Hân, our snapper, is behind him, already showing him the photo of every step. He stares. Over the shot: "CAVEMAN IN SAIGON · EP 1" | one impact |

- **Why it works (logic chain):**
  - An impossible task in a calm tutorial voice makes the viewer laugh and listen at the same time.
  - The steps are the real safe advice (walk slowly, steadily, don't run), so the joke also teaches.
  - The "last tip from my tribe" loop pays off with someone who had his back, so the twist is the brand and sets up episode 2.
- **Don't:** let the twist be an injury scare; change the character's design between shots.
- **Preset:** `absurd-howto-3d` · deep card: genre-playbooks.md §32

## 33. Code-made motion + screen tutorial
- **What it is:** a calm walkthrough of how you make something, with a burst of code-rendered proof cards in the middle.
- **Use it when:** tools/AI how-tos and build-in-public; a comment-keyword CTA drives comments and follows.
- **The 5 beats (60 s short cut of a 60-145 s tutorial):**
  1. 0-3 s: series tag + a glitch-in title ("PART 1") over the finished result, already playing.
  2. 3-12 s: the contrast claim on two screens ("before" vs "with this") + the effort hook.
  3. 12-35 s: the steps over real screen recordings, keyword captions in the empty half of the frame (VO ~120 wpm, 5-10 word sentences).
  4. 35-48 s: the proof burst: code-rendered cards at 0.03-0.6 s, one idea per card, cut to a beat.
  5. Last 8-12 s: the keyword CTA ("Comment X") + "part 2".
- **Real example:** @miftahul_islam_efaz animation tutorial 2/3 (ref anim2): 143.6 s, 1,667 likes and 2,040 comments (more comments than likes) from "Comment SKILL for the file".
- **Example script (Klaus personal, "How I make stat cards with code"):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | The finished animated counter already playing; over it: tag "BUILD IN PUBLIC" + glitch title "PART 1: STAT CARDS" | glitch hit |
| 3-12 s | Two screens: left, a wobbly stat in a template app; right, a frame-exact animated counter | VO: "Left: twenty minutes dragging boxes. Right: one command. Same number." |
| 12-20 s | Screen recording: a JSON with the number and its source line | VO: "Step one. Write the number and where it came from. Always the source." |
| 20-28 s | Terminal: `editor.py motion` with the stat-counter template | VO: "Step two. Pick the template. Stat counter." |
| 28-35 s | The render progress, then the 1080p file | VO: "Step three. Render. It's exact to the frame, every time." |
| 35-48 s | Proof burst: 20 cards cut on the beat (0.1-0.6 s each) | beat-synced track, one hit per card |
| 48-60 s | Klaus voxel avatar at a desk · text "Comment CARDS" | VO: "Comment CARDS and I'll send the template. Part two: step cards." |

- **Why it works (logic chain):**
  - The side-by-side shows the pain and the result in one frame, so the viewer wants the "how".
  - The steps are small and real, so the viewer believes they can do it.
  - The burst proves range after they've learned the method, so the keyword CTA offers the exact file they now want.
- **Don't:** fake UI or claim output you can't show; let the CTA promise a file you won't send.
- **Preset:** `code-motion-tutorial` (cards from tools/motion) · deep card: genre-playbooks.md §33

## 34. Side-by-side progression loop (stick figures)
- **What it is:** two identical stick figures; only one changes ONE habit; counters tick until a typed punchline, then it loops.
- **Use it when:** "same X, only one added Y" habits; reads muted and in any language. In SG health: show behaviours, not body or pain outcomes.
- **The 5 beats (14 s, one shot, zero cuts):**
  1. 0-1.5 s: week 1, both figures equal; the header "SAME X. SAME Y."
  2. 1.5-6 s: ticks 1-3 (~1.5 s each): a synced action; the variable changes on the right only; the delta pops.
  3. 6-11 s: ticks 4-7: the difference grows (glow, posture, colour).
  4. 11-14 s: the typed punchline with a cursor, over a slow push-in.
  5. 14 s: hard cut back to frame 1 (seamless loop).
- **Real example:** @stickmaxx "Same gym. Only one added weight." (ref anim3, 14.6 K likes): 14.6 s, one locked symmetrical shot, counters every ~1.5 s, a typed verdict, then a loop.
- **Example script (Physio Spot, "Same desk. Only one stands up."):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-1.5 s | Two white stick figures at identical desks. Header: "SAME DESK. SAME HOURS." Counters: "Breaks: 0" / "Breaks: 0" | licensed track starts |
| 1.5-3 s | Tick: both type; right figure stands, stretches 2 s, sits. Right counter "+1" (amber), left "+0" (grey) | pop |
| 3-6 s | Ticks 2-3: the same; the right figure's desk lamp glows a little warmer each time | pop · pop |
| 6-11 s | Ticks 4-7: the right figure sits a little taller, the left sinks lower into a curve (labelled "dramatised illustration") | pop per tick |
| 11-14 s | Typed with a cursor: "SAME DESK. ONE MOVES EVERY HOUR." over a push-in on the right figure | keyboard ticks |
| 14 s | Hard cut to frame 1 | loop |
| Caption | "One small habit, every hour. Questions about desk pain? WhatsApp Physio Spot." | |

- **Why it works (logic chain):**
  - Identical figures make the one difference impossible to miss, so the viewer reads it without words.
  - Counters make the habit concrete (a number, not a promise), so the exaggeration reads as illustration, not a claim.
  - The typed line names the behaviour, so the loop replays the lesson and the caption CTA follows.
- **Don't:** show guaranteed body or pain results; cut (the format is one continuous shot).
- **Preset:** `stick-compare-loop` (counters and type from tools/motion) · deep card: genre-playbooks.md §34

## 35. Petty victory sermon
- **What it is:** a small win delivered like a revival-church sermon at "that one person who doubted you", in one take.
- **Use it when:** personal or founder accounts; the joke is the mismatch between a small win and biblical-scale defiance.
- **The 5 beats (30 s, one take, 0 cuts):**
  1. 0-3 s: the rhetorical question to the doubters, eyes off camera.
  2. 3-12 s: escalating declarations, short lines with pauses (~125 wpm).
  3. 12-20 s: bigger declarations; the win's proof (the sign, the gown) in frame.
  4. 20-26 s: the absurd physical button ("Touch it.").
  5. 26-30 s: the biggest scripture-style line, then hold.
- **Real example:** "Who is that man in my family that said I'll fail?" (@jerrydeberry2333, ref comedy1): 50.3 K likes, 765 comments, 35.4 s, 0 cuts, 125 wpm, one caps word at a time.
- **Example script (Klaus personal, in front of the clinic sign; use his real doubter if there is one):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Locked mid-full shot, slight low angle: Klaus in navy scrubs, sunglasses, arms folded, the Physio Spot sign behind; dreamy haze | Klaus (to the sky): "Who is that man in my family who said physio is not a real job?" · choir bed |
| 3-8 s | One word on screen at a time | "Uncle. Finish your soup… and come back." |
| 8-12 s | | "You said, 'Just become a doctor.'" (pause) |
| 12-20 s | He points slowly at the sign | "This… is my clinic. My name is on the door. The door… is real." |
| 20-26 s | He pulls the scrub top forward | "This is my scrub top. Touch it." |
| 26-30 s | Hold on the stance | riser · "No weapon formed against my booking calendar shall prosper." · hold |

- **Why it works (logic chain):**
  - The question names a doubter everyone has, so the viewer is on his side from the first line.
  - The sermon cadence is far bigger than the win, so each pause makes the next line funnier.
  - The sign in frame is the proof, so the final verse lands as earned defiance, not a brag.
- **Don't:** cut (one take is the format); use a patient's recovery as the "win" (testimonial rule) or promise outcomes.
- **Preset:** `petty-sermon` · deep card: genre-playbooks.md §35

## 36. Clone / character swap
- **What it is:** "this is me… and this is also me": one person's walk is cut, step by step, into different original characters.
- **Use it when:** creator flex, A/B model tests, one actor playing every role; original characters only, never real lookalikes.
- **The 5 beats (30 s):**
  1. 0-2 s: you, walking (the driver clip).
  2. 2-10 s: match cuts on the step every 1.5-2.5 s into 4-6 characters.
  3. 10-12 s: the "how?" beat (back to you, to camera).
  4. 12-25 s: the 3-step how-to over screen recordings.
  5. 25-30 s: a keyword CTA.
- **Real example:** @hi.boly "This is me and this is also me" (ref hfclone): 48.6 s, 7 cuts, the same street walk cut on the step into 4 characters, then the spoken method. Clone A/B tests (ref clone1: 465 likes, 391 comments) prove the comment-CTA pull.
- **Example script (Klaus personal):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-2 s | Klaus walking towards camera on a Saigon street | "This is me." |
| 2-4 s | Cut on the step: an original grandpa character in a singlet, same walk | "…and this is also me." · whoosh |
| 4-6 s | Cut: an original chef in whites | whoosh |
| 6-8 s | Cut: an original anime-style hero | whoosh |
| 8-10 s | Cut: an original rich uncle with a golf umbrella | whoosh |
| 10-12 s | Back to Klaus, to camera | "Yes, it's all one clip. Here's how." |
| 12-25 s | Screen: 1 film your walk · 2 build an original character sheet · 3 motion transfer onto it (cheap draft first) | "Film one walk. Build a character, not a lookalike. Transfer the movement." |
| 25-30 s | Klaus to camera; over the shot: "Comment CLONE" | "Comment CLONE for the steps." |

- **Why it works (logic chain):**
  - The same walk in every shot makes the swap obvious, so the viewer's "how??" fires within seconds.
  - Returning to the real face answers "is that you?", so the how-to feels like the reveal.
  - The CTA offers the method they just asked about, so comments come from curiosity, not bait.
- **Don't:** clone a real person or make a lookalike; burn credits on finals before a cheap draft passes QC. No AI label on screen or in the caption; use the platform's AI-disclosure toggle (ledger [ai-labels]).
- **Preset:** side/split B-roll + `genz-header-skit` · deep card: genre-playbooks.md §36 → clone-character-swap.md

---

## 37. Lead magnet / comment-to-DM
- **What it is:** give away one useful thing (map, checklist, prompt pack) and ask people to comment one word to get it.
- **Use it when:** you want comments, DMs and leads; any brand with something genuinely useful to hand over.
- **The 5 beats (25-30 s):**
  1. 0-3 s: name the thing + one reason to believe it. First word on frame 1.
  2. 3-6 s: what it is in one line ("It's one map with…"); show it by 3-5 s.
  3. 6-20 s: three quick proofs (a number, examples, it working), a new screen every 1.5-2.5 s.
  4. 20-24 s: how you use it, one line.
  5. Last 3-5 s: say the ask out loud: reason → keyword → "I'll send it". Keyword big on screen in quotes; caption line 1 = the same ask.
- **Real example:** @nick_saraev "prompts.chat" https://www.instagram.com/reel/Dc6IUUVvmUE/ (6,993 likes, 12,717 comments): ask spoken at 86 % of the video. Reels that only asked in the caption got 2-37 comments per 100 likes; spoken asks got 106-182.
- **Example script (Snap Saigon, keyword MAP):**

| Time | On screen | Said / sound |
|---|---|---|
| 0-3 s | Hân (our snapper) walks into frame past tourists all shooting the same Notre-Dame angle (real clips via `editor.py collab scout`, creators tagged in the caption) · "SAIGON PHOTO SPOT MAP" | Hân: "Every tourist takes this exact photo. Here's my map of where we shoot instead." |
| 3-6 s | Phone: a map with 6 pins | "One map, every spot we use, each with the best time of day." |
| 6-16 s | Landmark 81 at sunset → Thao Dien café street → Nguyen Hue, City Hall end | "Riverside at sunset. Thao Dien for the café look. Nguyen Hue from the City Hall end, crowd behind you." · whoosh per spot |
| 16-20 s | Screen recording: tap a pin, the note opens | "Tap a pin, walk there, the angle's in the note." |
| 20-25 s | Hân to camera, map thumbnail · **Comment "MAP"** 👇 | "Want the map? Comment MAP and I'll send it to you." · pop |
| Caption | "Comment MAP and I'll send you our Saigon photo spot map 📍 6 spots, best time, exact angle." | |

- **Why it works (logic chain):**
  - The hook names a concrete thing, so the viewer knows what they could get in 3 seconds.
  - Three proofs make it feel valuable, so wanting it is the viewer's own idea by the time we ask.
  - The ask is spoken, shown and captioned with one word that is the thing's name, so commenting takes zero thought.
- **Don't:** ask only in the caption; use two keywords or a phrase ("MOBILITY PROGRAM").
- **Preset:** `lead-magnet` · deep card (with Physio Spot DESK and TITAN.AI PROMPT scripts): genre-playbooks.md §37

## Universal rules (every genre)
- **No abrupt blank pages:** don't cut from real footage to a plain text card for commentary; put the text over the footage. Save hard contrast cuts for twists, and then cut to a character reaction image + on-screen text (ledger [edit]).
- **Defaults, not laws (Klaus, 2026-10-29):** every card here is the measured best practice for version A. Older styles and settings (crash zooms, earlier presets) are fine as variations: hook variations, trial reels, proposal B.
1. **Hook ladders, not single hooks** (ledger [hooks]): each line opens a new loop that pays off the last and raises the stakes: tease → twist → reveal → why → stakes → proof → things to note → end. Write 3-5 hook variations per post. Wordless formats do the same with the picture and the header.
2. **Start at 0.0 s.** First word, first action or first chant at frame 1; no slates, logos, intros or count-ins (every measured winner in news, edu-song, drama and ASMR does this; the losers open on 4-10 s of nothing).
3. **Protect the pause.** The 0.5-1.7 s of silence before a punch, scare or reveal is the most valuable second in the video; never let silence removal eat it.
4. **Pay off the hook, and make the CTA the payoff's next step.** A spoken CTA names the channel (WhatsApp, link in bio); the number goes in the caption. Mystery and curiosity content: provocative hook, light but true payoff (ledger [retention]).
5. **No on-screen credit text, ever** (ledger [credits]): tag reused clips' creators in the caption and reach out. **No AI/CGI label on screen or in captions** (ledger [ai-labels]); switch on the platform's AI-disclosure toggle for photoreal AI.
6. **Compliance first, every line.** SG health (Physio Spot, heal360): no testimonials, outcome promises, superlatives, people before/after or discount/free-consult inducements. Vietnam paid ads: Vietnamese first. Real prices, dates and terms only. Brand accounts use licensed or original audio; trend audio only on personal accounts, in-app.
7. **Rotate formats** (ledger [variety]): never the same spine twice in a row on one account; the trick-on-the-viewer remix at most ~1 in 5, with a new trick each time. Make variants and test (`/expand`).
8. **Klaus's version is version A.** An existing script or final cut is the master spec; new ideas (crash zooms, extra lines, alternate endings) go in as proposal B.
