# Genre feedback: overnight run 2026-10-25/26 (2-5 am SGT)

Every module below was re-grounded on real reels measured locally: scene cuts, shot lengths, loudness, words/min and frame sheets I looked at. Sources, numbers and full cards are in `research/genre-research-2026-10/*.md`. The corrected cards are merged into `genre-playbooks.md`, and the presets in `tools/editor/presets/` are render-tested on the self-test footage.
**Measurement limits:**
- Only public Instagram reels download from the cloud machine. YouTube, TikTok and Vimeo demand a login, and I did not bypass that.
- Brand films were measured from reposts, so their loudness is Instagram's normalisation.
- The likes counts are the evidence of performance; views are mostly not public.

**Klaus reviewed every card on 2026-10-28** (interactive page https://claude.ai/artifact/FK43HR4gwjbx7aKgGr7uYW): 19 approved, 4 fixed, 0 rejected. Fixes are applied in genre-playbooks.md as "Klaus's correction (2026-10-28)" lines.

| § | Module | What changed | Strongest example | 3 core rules | Verdict |
|---|---|---|---|---|---|
| 2 | Comedy skit / deadpan (+2a silent rebuttal, 2b quote vs reality) | Top deadpan reels cut **2-5× slower** than the old card: a premise, then ONE 10-28 s take. Crash zoom removed. | [@khaby00 9.7M likes](https://www.instagram.com/reel/DceEuVnii0u/) | One take for the answer · protect a 0.5-1.7 s pause before the punch · the header tells the joke, the performer never explains it | ✅ approved |
| 5 | POV / relatable | Not 1-2 s cuts: a persistent "POV: the friend who…" header + 3 vignettes of 5-12 s each, ~220 wpm, no music | [@amitmizrachix 406K](https://www.instagram.com/reel/Dd9hI51P_aw/) | Header names a TYPE · 3 vignettes, 3 locations, to the lens · dialogue is the speed, pause before the punch | ✅ approved |
| 6 | Absurd / meme (+6a brand meme reply, 6b lore roll-call) | The chaos is in the image and the labels, not the cuts (1.5-5 s holds). New default `meme-chaos-short` | [Duolingo 253K](https://www.instagram.com/reel/DFttLM7ATju/) | One bizarre centred subject per shot · label every beat · the brand mocks itself, 5-16 s | ✅ approved |
| 24 | Luxury / product reveal | Show the product in the first 1.6 s (not ~12 s); ~0.85 s cuts for fragrance and fashion, ≥2.5 s for objects; packshot hold 2-4 s. Split into luxury-reveal / luxury-object-calm / fooh-oneshot | [Jacquemus CGI bags](https://www.instagram.com/reel/CqqN8w6K3rL/) | Brand at 1.6 s, packshot end · speed by category · spectacle (labelled CGI) beats montage | ✅ approved |
| 28 | Event / retail / mall | Frame 1 is the storefront or product, never a discount; hands-on activation ~1 s each; ends on a bag-out or a date card | [POP MART Mall of America](https://www.instagram.com/reel/DQxooZQEaIl/) | No discount opener · hands at ~1 s · proof of visit or a what-where-when card ≥2 s | 🔧 fix: a discount opener is fine sometimes, make people want it (applied) |
| 26 | Before / after | Not a beat snap: the "before" at 0 s, the process for most of the runtime, a wipe/split reveal in the last 3-5 s from the same camera. **SG healthcare: no people before/after at all (HCSA reg 5(1)(d))** | [pink rug 18.8K](https://www.instagram.com/reel/DR4YtfODqnh/) | Same camera and light · the process is the content · objects and spaces, never health results in SG | 🔧 fix: reveal can be first (beat snap), mid-way or last; make variants (applied) |
| 27 | ASMR / satisfying | One locked continuous take + a 2.2 s hold; the sound IS the product (dense, loud). A near-silent brand reel flopped | [44.7K](https://www.instagram.com/reel/DaQQ9EuuNu4/) | Loud dense foley · one take by default · frame 1 already makes the sound | ✅ approved |
| 15 | Action / sport | Two modes: an **anthem** (accelerating 3.75 → 2.3 → 1.0 s, cut on VO lines, `sport-anthem`) vs **gym hype** (0.44-0.62 s on the beat, `action-hype`); the money rep plays uncut 3-12 s | [Nike "Winning Isn't for Everyone"](https://www.instagram.com/reel/C9po_ojpF6t/) | Pick the mode · the proof plays uncut · loudness and cut rate build together | ✅ approved (note: both modes work, pick by mood) |
| 9 | Feel-good (+9c festive film, in the research file) | Medians 1.8-2.9 s (not 3-5 s), one 9-11 s reveal hold, music drops ~15 dB before the payoff; 90-180 s film map + cutdown | [Thai Life "Unsung Hero"](https://www.instagram.com/reel/DWXnBo1DMbN/) | Brisk story + one long hold · take the music away before the payoff · show first, say last | ✅ approved ("amazing example… 100%") |
| 11 | Founder | High-engagement founder reels are talk-led (4-10 s shots, 150-235 wpm, words from frame 0, ~7 s header, ONE specific scene). New `founder-clip`; the cinematic `founder-inspire` is kept, unmeasured | [Sara Blakely](https://www.instagram.com/reel/DC47FDWxlpv/) | One scene, not the journey · words from frame 0 + stakes header · real voice, real room | ✅ approved ("powerful, agreed") |
| 7 | Drama / conflict (+7a micro-drama episode) | Much faster than the old 2-4 s: a 1.2-1.5 s median, dialogue at 0.0 s, ~1 s of silence after the hit. Micro-drama: one scene and one turn per episode, freeze-frame cliffhanger | [Dhar Mann 238K](https://www.instagram.com/reel/Da9ltsbPQAf/) | Conflict line at frame 1 · fast into the cruelty, then true silence · the turn is evidence (chat/CCTV), not a speech | ✅ approved |
| 14 | Mystery / reveal | **Fixed a copy-paste bug** (the card had edu-song's sound/compliance/preset). One closeable question, a clue per insert, silence before the reveal, a clue rewind. Evidence weak (3-352 likes) | [narrated mystery](https://www.instagram.com/reel/DbYOd-HD7E3/) | One specific question · every clue its own insert + sound · silence, then a rewind | 🔧 fix: retention first, strong provocative curiosity hook, light payoff (applied) |
| 13 | Thriller / heist | A plan the viewer can follow (rule or step cards), inserts at 0.6-1.0 s with a tick each, silence on the hitch. A slow "cinematic AI heist" got 3 likes | [heist short 3.4K](https://www.instagram.com/reel/Csyv74MAu-e/) | A plan, not vibes · fast inserts with ticks · the hitch gets silence | ✅ approved |
| 10 | Romance (+10a slow-burn texting) | Romance that performs is serial and music-led (~2 s median, ≤60 wpm, cold open on the charged moment, then "a few months earlier"). Implied-only line kept: adults 25+, clothed, cut before the kiss in paid ads | [C-drama serial](https://www.instagram.com/reel/DewJSY9AquY/) | Cold open, then a time jump · structure from C-drama, explicitness from our ledger · chats as plot beats | ✅ approved |
| 22 | News / scam-expose (+22b trick-on-the-viewer remix, 22c news-card carousel) | Voice or kicker at frame 0; official advisories (7.6-9.8 s to the first word) were the weakest. A one-take parody that plays the scam on the viewer got ~400-1,600× the likes of the police advisories | [Hougang NPC "Singa(pore) Inferno" 370K](https://www.instagram.com/reel/DWkv0WID7gG/) | Voice at frame 0 · one trick per post, performed on the viewer · one stat with source + date | 🔧 fix: can't use one style every video; rotate spines, 22b ≤1 in 5 (applied) |
| 20 | Documentary | Medians 1.2-3.2 s inside 6-10 s VO beats at 170-216 wpm (not 3-6 s shots); the investigator on screen in the cold open; a source tag on every evidence shot. New `doc-paper-trail` | [Johnny Harris paper trail](https://www.instagram.com/reel/DRfLDUfk4qJ/) | See research file §D | ✅ approved |
| 21 | Explainer / myth-buster | The myth as its own artefact → "look closely" → labelled evidence + expert PiP → where it started → one-line verdict. 230-240 wpm; dead air loses, not shot length. New default `myth-buster-stitch` | [Dr Karan Rajan 75K](https://www.instagram.com/reel/CxkzKPFs6Dx/) | See research file §D | ✅ approved |
| 17 | K-drama (+17a fan edit, 17b self-aware product-placement gag) | 2025-26 brand K-drama ads are **rom-com subversions**, not pastel swooning: 1.5-2.0 s median, ONE romantic beat held 3-6 s (umbrella/car), then a twist punctures it; warm low-contrast film or tungsten night | Wacky Willy (4,050 likes on the repost); Kopiko PPL commentary (1,834 comments) | See research file | ✅ approved |
| 18 | Anime (+18a OP parody) | Impact flashes are real anime-opening craft, but the reels that perform use **zero flashes**: Nissin CM 0.53 s median with a chanted label per shot + packshot; "Anime Openings Be Like" (513K) 1.53 s with a label box per trope | Anime Openings Be Like (513K) | See research file | ✅ approved |
| 29 | Edu-song (+29a screen song, 29b brand PSA original song) | Winners **start singing at 0.0 s** with the hook in a header: no spoken hook, no count-in. 3.0-3.4 syllables/s (~2-2.6 per beat at 90-100 BPM); the slow kids' controls flopped. Copyrighted-melody covers are creator-only | AsapSCIENCE mitosis (302K repost), studysongz (142K), SimpleNursing (51K) | Sing at frame 0 · header carries the hook · ~3 syllables/s | ✅ approved |
| 8 | Class & status (+8a wordless two-wallet parable) | Four measured spines, not one split screen: a two-hander dialogue volley (1.0 s median, 180 wpm, same room and light; class lives in vocabulary and props), two locked takes of the same action, persona satire, and a wordless parable. The top performer is a **persona satire** (out-of-touch rich narrator) | [Shabaz Says × Channel 4 #ChangeClimate 83K](https://www.instagram.com/reel/Czds85lsTIq/) | One grade, class in props and words · punch at hypocrisy, never at poverty · end on the silent reaction | ✅ approved |
| 12 | Cautionary / decision ladder (+12a consequence ripple, 12b comedy-twist ladder) | Each decision is a step, and the steps **accelerate** (2.0 → 0.76 s); a flash-forward of the consequence early, one long held wide for the stat, and the ending is ONE doable action (fear without an action backfires, Tannenbaum et al. 2015) | [ThaiHealth "Phone" 10.6K](https://www.instagram.com/reel/DY84J-VClM5/) | Steps speed up · show the consequence early, hold the stat · end on one action, not dread | ✅ approved |
| 16 | Sci-fi / tech (TITAN.AI) (+16b UI-proof launch, 16c cyan concept look opt-in) | **Reversed the old card:** winning AI/tech launches are warm and human (wood rooms, practical lamps, real skin, the product as in-world screens or a friendly mascot); cyan/hologram looks were the negative controls. `scifi-tech` is now warm; the cyan look is the opt-in 16c. New `ui-proof-launch`: story cold open, floating real UI cards, one stat | [OpenAI "Introducing dots" 50.6K](https://www.instagram.com/reel/Dd4RMfMJ7kO/) | Humans and warm light first · show real UI, labelled if simulated · one capability, one proof | ✅ approved |

## Klaus's decisions (2026-10-28)
1. Crash zooms: kept as proposal B on his skits (applied to §2).
2. Side-choosing endings: **kept** (ledger rule stands).
3. Physio before/after (HCSA reg 5(1)(d)): Klaus checks with compliance. Until then, no people before/after.
4. Trick-the-viewer remix: brand and health accounts allowed (applied to §22b), rotated per §22.
5. Romance line: anything goes in organic posts except showing private parts; paid ads stop at the kiss (applied to §10 and the ledger).
6. Frame container: build it (engine feature queued).
7. AI/CGI labels: none on screen or in captions (applied to §24, §27). Platform AI-disclosure toggles stay on for photorealistic AI, since TikTok/Meta require them.
8. Physio do-along song: A/B against a study song first.
9. Real people's clips: reposts, Remix, Stitch, Duet and reuse are one workflow on every account; Klaus handles rights. Studio credits, tags, does outreach and tracks (`editor.py collab`, creator-collabs.md).
10. ASAS fear clause: Klaus gets it checked.
11. FTC AI-claims check: not needed (Klaus). The basic rule stays: never show a capability the product doesn't have.
12. Thin-evidence references: skipped for now.

## Original questions (answered above)
1. **Crash zoom** in your own skits: the new deadpan default has none (the measured reels use none). Keep your BUFF BOY-style crash zooms as proposal B?
2. **Side-choosing endings** ("comment Team A or B"): Meta demotes vote-bait. Replace with an open question or a Part-2 tease? (This touches a ledger rule, so it's your call.)
3. **Before/after for Physio Spot's own channels:** my reading of HCSA reg 5(1)(d) is "no people before/after anywhere, including own social". Confirm with your compliance contact.
4. **Trick-the-viewer scam remix:** allowed on brand or health accounts, or personal only?
5. **Romance paid vs organic line:** proposal is that organic may show a completed kiss between adults, while paid stops at the near-kiss with no bed framing.
6. **The white/black 9:16 frame container** (the picture inside a frame with a header, common in drama and mystery reels): on brand accounts it can read like a repost page. Build it anyway?
7. **AI/CGI labels** for FOOH-style spectacle: caption only, or on screen too?
8. **Physio do-along song:** no measured winner exists yet. Proposal: A/B a do-along against a study-song format before investing.
9. **Persona satire with real people's clips (§8 spine C):** I've set it as personal accounts only (Remix/Stitch or written permission); brand accounts recreate the evidence with original actors. OK?
10. **Fear appeals in paid cautionary ads (§12):** SG's ASAS code has a fear clause I could not check tonight. Have it checked before any paid health or safety PSA runs.
11. **AI capability claims (§16):** the FTC's "Operation AI Comply" (Sept 2024) targets deceptive AI claims. I've set the rule that every capability shown must be real or labelled "simulated / concept"; the source still needs a check before TITAN.AI US ads.
12. **Send references** you rate for mystery/heist, gym edits and SG founder reels: the evidence there was the thinnest.

## Engine features the research asks for (not built yet; marked `_needs_feature` in presets)
Ordered by how many modules need them:
- a protected pause before the punch, plus silence beats;
- uncut "money" holds;
- a wipe/split before|after reveal card;
- cut-rate acceleration targets;
- a music dip longer than 0.3 s and a music build;
- the frame container layout;
- name, time-jump and date/place end cards;
- freeze-frame and episode labels;
- speed ramps;
- a clue-rewind montage.

## Consistency check (2026-10-28)
Done while writing `.claude/skills/higgsfield-creative-director/references/genre-quickstart.md` (plain-English beats + a worked script per genre). Cards compared with each other, with `tools/editor/presets/*.json` and with `ledger/learnings.md`.

**Fixed (small, clearly wrong):**
1. §0 picker was never updated after the corrections: preset column now matches the cards (§10 romance-drama, §11 founder-clip default, §15 + sport-anthem, §20 + doc-paper-trail, §21 myth-buster-stitch, §22 + news-silent-case / scam-remix-onetake, §26 + before-after-fast). "Avg shot" now uses the measured numbers (§7 ~1.5 → 1.0 s, not 2-4 s; §9 2-3 s + reveal hold; §10 ~2 s, not 3-6 s; §13 inserts 0.6-1.0 s, not 1.5-3 s; §20 1.2-2 s, not 3-6 s; §22 1.7-2.5 s).
2. §7 still proposed dropping side-choosing endings ("no vote-bait"); Klaus kept them (decision 2, ledger [skits]). Pacing row and flag now say: keep them, phrased as a real question.
3. §10's 3 core rules still said "implied only … cut away before the kiss completes", against ledger [romance] (organic: anything but private parts; paid: stop at the kiss). Rule (1) updated.
4. §14 carried a stale flag ("needs its Sound/Compliance/Preset lines fixed, copy-paste from §29") and "(replaces the edu-song text)" labels after the fix was already made. Removed.
5. §24 FOOH said 'Caption "CGI" or "concept"', two lines above the card's own "no AI/CGI label" rule (ledger [ai-labels], decision 7). Now: never claim it really happened. Same leftover fixed in `fooh-oneshot.json` ("Label CGI/AI in the caption").
6. §36 said "always label it as AI" (ledger [ai-labels] says no label on screen/caption, platform toggle only). Fixed.
7. §2 said brand accounts must recreate Khaby-style trigger clips (pre-decision-9 rights rule). Now: reuse via `collab add` or recreate when the joke mocks the method. Same stale line fixed in `research/edit-references-2026-10.md` ref #8 ("brand and clinic accounts never reuse the footage").
8. §32 pointed to "JSON in research/refs-2026-10-25/ai-animation.md"; the preset file exists (`tools/editor/presets/absurd-howto-3d.json`).
9. `kdrama-fan-edit.json`: `music.energy` "medium" is not a valid value (none|low|mid|high) → "mid"; `max_shot_s` 1.4 → 2.3 (the card measures max 2.3 s and holds the opening shot ~1.5 s, which 1.4 would chop).
10. `genz-header-skit.json`: `sfx.density_per_10s` 2.5 → 5.0. The density is a budget cap (recipe.auto_sfx); ref #1 measured hits at 0.5, 1.95, 3.35, 5.35, 8.55 s (one per reaction, every 1.5-2 s ≈ 5-6 per 10 s), and 2.5 capped it at one per 4 s.
Selftest after the preset edits: 41/41.

**Open (needs a decision or engine work, not changed):**
1. `CLAUDE.md` routing row for clones still says "always labelled AI", as does clone-character-swap.md, against ledger [ai-labels]. The ledger wins; the row and the guide need the same wording as §36.
2. `recipe.py` (line ~278) adds an on-screen `credit` text for CC BY web images. Ledger [credits] bans on-screen credit text for reused clips, and Klaus called on-screen credits "ugly". CC BY attribution can live in the caption (`webimg.attribution` already writes it). Decide: caption-only credit for web images too?
3. Decision 9 above says "Studio credits, tags…": "credits" here means the caption tag, not on-screen text. Worth rewording to avoid a future agent burning a credit on screen.
4. §16 still asks for "on-screen UI labelled simulated in post" and cites the FTC check that Klaus waived (decision 11). Keep the basic rule (never show a capability the product doesn't have); drop the on-screen "simulated" label?
5. §22c is titled with a preset name (`news-card-carousel`) that doesn't exist; it really uses the expander's `carousel-text` + `card_style: kicker`.
6. §5 still says Stitch replies need "the original enabled (§31 rights rules)"; §31 rights are now the one-workflow rule. Platform-native Stitch still needs the original's setting, so only the cross-reference is stale.
7. §29 says "no pop-song melodies on brand accounts (§5 copyright …)": that §5 is edu-songs-mnemonics.md §5, not genre §5 POV. Ambiguous reference.
8. Presets whose hard caps fight a card's long hold (no feature yet to exempt one beat): `class-two-wallets` max_shot 7 vs the §8a payoff held 8-10 s; `ui-proof-launch` max_shot 8 vs "story bookends up to 21 s"; `anime-energy` max_shot 1.2 vs the ~2.5 s proof card. Needs a per-beat `hold` override (the `_needs_feature` "uncut money holds" item).
9. `deadpan-silent-rebuttal` plays a mid music bed until `music.stop_at_beat` is built, so today the silent take gets music under it (§2: no music under the take).
10. `texting-suspense` (1.5 per 10 s) and `horror-tension` (1.2 per 10 s) SFX budgets are below the "a hit every 1-3 s" / "sting every 1-2 s" in the refs. Probably right if the pulse lives in the drone bed; confirm by measuring a test render before raising them.
11. Physio Spot's brand file names "crash zoom + impact" as the ad formula, while §2's default has no crash zoom (proposal B). Not a contradiction for the existing v4 cut (master spec = version A), but new Physio Spot skits need a one-line rule: brand formula or genre default?
