# Learnings ledger (append-only; newest at top). Each entry = a standing rule.
## 2026-10-28 - genre card review (Klaus)
- [stories] Travel/city brands also tell the stories behind places: bars, restaurants, cafés, buildings, and the deep, dark colonial and city history behind them (narrated mini-docs with hook ladders, archival vs today, every fact sourced; war/post-1945 stays factual and official-term).
- [clips] Claude collects the clips (not the VA): search the web, check with `collab scout`, commit the shortlist; Klaus's PC downloads it with `collab add-list`.
- [analytics] Every post is logged (lane, hook ladder, CTA, format, giveaway) and a winners report over the last 2-3 months (`tools/analytics/winners.py`) must justify next month's content: do more of what scored above the median on shares/sends/comments, drop what scored below.
- [giveaways] Giveaways and contests are part of the mix: random draws, funny caption winners, lucky commenter + reposter, "if Vietnam win / if <player> scores" prize drops; prizes like 50 USD, an iPhone, steakhouse dinners, free hotel stays, free shoots (giveaways-contests.md; fair draw with pick_winner.py).
- [hooks] Hook LADDERS, not single hooks: every line opens a new loop that pays off the last one and raises the stakes, so attention grows line by line. Pattern: tease ("next week something is happening in HCMC") → twist ("or should I say, happening AWAY from HCMC") → reveal ("expect a ghost town") → why ("everyone's fleeing home for the long Tết break") → stakes ("these services are hit hardest") → proof (stats, facts, hours) → things to note → end. Exaggerate and paint the hook; write 3-5 different hook variations per post.
- [credits] No on-screen credit text on reused clips, ever. Tag in the caption only.
- [retention] Mystery/curiosity content exists to hold retention: a strong, provocative, thought-provoking curiosity hook, then a light (but true) payoff. "Always be provocative."
- [variety] Never run one format every post: rotate spines/styles per account (no spine twice in a row; the trick-on-the-viewer scam remix at most ~1 in 5, a new trick each time).
- [before-after] Reveal placement is flexible (snap first, mid-way or last); make variants and test. SG health: still no people before/after.
- [retail] A real discount can open a retail ad when it makes people want the product (product first, real terms shown). Never for SG health brands.
- [ai-labels] No AI/CGI label on screen or in captions; use the platform's own AI-disclosure toggle where TikTok/Meta require it for photorealistic AI.
- [clips] More real people's clips: reposts, Remix, Stitch, Duet and reused clips are ONE workflow (`editor.py collab add`); Klaus/his VA handle backend and copyright, so no permission gates in the studio. Never burn credits on screen ("via @handle" looks ugly and stupid, Klaus); tag the original creator in the caption + outreach (shoutout/collab DM) + tracker.
- [romance] Organic romance/sensual: anything goes except showing private parts (no genitals, female nipples, explicit sex acts); kisses, making out, bed scenes, lingerie and implied sex are fine. Paid ads stop at the kiss (Meta/TikTok ad rules). Adults 25+, original characters only.
- [skits] Crash zooms on Klaus's own skits = proposal B; side-choosing endings stay.
## 2026-10-25 - robotic voices (Klaus)
- [voice] Robotic TTS (espeak/SAPI-style) never appears in anything Klaus sees as a sample or deliverable: "sounds so robotic… this would never work". Real recorded voices first (enhanced with `editor.py enhance`), then natural neural voices for test/demo footage (Piper locally) and premium licensed AI voices (ElevenLabs/Higgsfield archetypes, never cloning real people) only when a voice must be generated. When showing a test render, say what the voice is.
## 2026-10-20 - draft vs final quality (Klaus)
- [quality] Drafts always render at the LOWEST quality/resolution the model offers (cheapest tier, e.g. 480p/std/draft). Only after Klaus approves the draft, re-render at the HIGHEST quality at 1080p. Never render a draft at 1080p, never skip the draft.
## 2026-10-20 - villains & conflict (Klaus)
- [story] Compelling stories need villains: rich one-uppers, bullies, slut-shamers, degraders are in scope. Depict honestly, never glorify: camera stays with the target, cruelty gets cold sound (no hype), show the aftermath, consequence lands (downfall/karma/realistic cost/earned redemption), end on side-choosing. Sexual-themed shaming = adult characters only.
## 2026-10-20 - class & status (Klaus)
- [class] Rich/hot and broke/struggling stories get equal humanity; tone dial (humour, disdain, wit, debate, hyperbole, melodrama, sincerity); punch at behaviours/systems, never at being poor; sourced stats; signature format 'same problem, two bank accounts'. Roster cards carry class_background + money_wound.
## 2026-10-20 - composite aesthetics (Klaus)
- [cast] Study public style at CATEGORY level (WAG glam, F1 paddock, runway, athlete builds…) and blend ≥3 sources into original people across races and ages. No real names/teams/logos in prompts; lookalike QC → regen with 2 features changed. roster_gen.py builds balanced cards.
## 2026-10-20 - character design (Klaus)
- [cast] Studio builds ORIGINAL attractive characters (female-led for representation): build archetypes, specific face/hair/skin vocabulary, voice archetypes, character cards → AI Influencer builder or character sheet → Element. Never lookalikes of real WAGs/athletes/models, never real people's bodies/voices without consent. Diverse heritages, skin tones rendered correctly, adults 25+.
## 2026-10-20 - sensitive true stories (Klaus)
- [sensitive] Stories like UK grooming-gang scandals: blame specific perpetrators + failing institutions, never a whole ethnicity/religion/culture; state ethnicity only as documented by official sources, in context; include in-community voices; run the culture-blame test on every line.
- [child-safety] Child victims: no depiction/re-enactment/AI recreation of abuse, nothing suggestive, symbolic visuals only; UK lifelong victim anonymity; no AI likeness of real victims/perpetrators; helplines at end.
## 2026-10-20 - commentary & social justice (Klaus)
- [commentary] Real-figure/controversy content (OnlyFans economy, manosphere, influencer controversies, tech billionaires): receipts format, web-sourced claims in SOURCES.md, opinion labelled, steelman first, never fabricated quotes, never AI likeness/voice of real people.
- [justice] Race and social issues = shining a light on real experiences: community voices, credible data, dignity not trauma porn, a path to action. (Klaus clarified: no racist punchlines intended.)
- [implicit] (Updated 2026-10-28, see [romance] above.) Sensual = expressions, cut-aways, metaphors; no private parts or explicit sex acts; adults 25+.
## 2026-10-20 - mature/edge (Klaus)
- [edge] Adult (18+) edge is welcome: Decision-Ladder cautionary stories, raunchy innuendo for sexual-health/adult brands, dark & absurd comedy, rage-hook writing, Japanese modes, profanity dial 0-3 per placement. Plan ad-safe vs organic vs age-gated cuts.
- [hard-line] Never: explicit/porn, bypassing moderation, anything sexual near minors (students = clearly 25+, non-school), sexualising real people, real tragedies as entertainment, group-degrading punchlines, fake engagement, crime how-tos.
## 2026-10-20 - localisation (Klaus)
- [locale] Every brief sets a market; load its pack (settings, language register, humour, sound, casting, law). Packs: SG/Singlish, Bollywood/Indian, MY, VN, TH, ID, NG, UK, US. ≥1 of the 5 directions leans fully local.
- [voice] Real local VO beats AI accents for Singlish/Hinglish; archetypes only, never impersonate stars or reuse famous dialogue.
- [legal] SG health clients (heal360, Physio Spot SG): no testimonials, paid reviews, superlatives, or free-consult/discount inducements; dramatised skits must not pose as real patient testimony.
## 2026-10-20 - voice, reactions, stims (Klaus)
- [voice] Commentary personas are ORIGINAL archetypes (posh nature-doc, Bronx hype, streamer reactor, West Coast smooth, diva rant, Nollywood melodrama, deadpan British, play-by-play). Never clone/imitate real people or reuse their catchphrases.
- [faces] Reaction-face archetypes held 0.6-1.2 s, cut on the eyes, paired with a stim; performed by cast from the community the joke is about; humour from inside the community.
- [audio] Stims are core for skits/reactions (one per 1.5-3 s); /sound gives licensed trending tracks (Higgsfield TikTok CML) + SFX cue sheet. Meme sounds only on personal accounts, in-app.
## 2026-10-20 - asset handoff
- [assets] Generate assets one at a time in dependency order; after each: show it, state what is locked + who inherits it ("Created @X. We'll preserve her face, skin tone and body proportions for @Y."), one-line QC, approve/fix. Identity anchors with face cropped or hidden = automatic REGEN.
## 2026-10-20 - asset bible (Klaus)
- [assets] After script approval: Asset Bible with @HANDLE cards (description, identity lock, derived-from, framing, used-in, source, copy-ready prompt). Real photos first; variants derive from the approved base identity. Every asset visually approved before any video; validator blocks unapproved handles.
## 2026-10-20 - cinematic ad flow (Klaus)
- [flow] Every ad/story request runs 3 gates: brief intake (echo "Your creative brief" + compliance line) → 5 story directions (diversity matrix across funnel/angle/vibe/format/segment, 13-field cards, one Recommended) → second-by-second production script with speaker & timing locks. No render before Gate 3 approval.
- [model] Default cinematic stack: Seedance 2.5 omni_reference (draft 480p → 1080p high bitrate) + Genjutsu motion transfer for performance-critical shots + 4K upscale of the final. Other models only with a stated reason.
- [cta] No on-screen text requested → spoken CTA names the channel (e.g. WhatsApp); number goes in caption/CTA button.
## 2026-10-11 - research budget rule
- [budget] vidIQ style-library research capped at 2,000 credits/month (Boost), spent gradually by weekly batch (see Creator_Style_DNA_Library.xlsx > Budget Plan). Before any vidIQ call: state the batch, credits it costs, and remaining for the week. Stop at the weekly line; anchors first, less-famous creators in month 2+.
- [streamers] Catalogue streamers (source energy) AND clip editors (the addictive edit layer) separately.
## 2026-10-10 - v5 render (edit-only, 0 credits)
- [edit] Rebuild a lost final cut from Higgsfield history: download all clips, transcribe (faster-whisper; feed numpy audio - av version clash), match lines to the brief, use word timestamps + RMS energy to place cuts.
- [hook] Hook text must never cover faces/reactions. Physio Spot placement: DejaVu Bold 60px, 2 lines, top at 61.5% height (just above 74% captions); end it when the POV shot starts (face sits in that band).
- [sfx] Measure zoom freeze by frame-diff; put the boom exactly there (drop clip: 2.27s).
- [render] Overlay PNGs only for their own window (setpts offset + eof_action=pass); full-length looped layers exceed 5 min.
## 2026-10-10 - MASTER BRIEF RECEIVED (Physio Spot v4) - supersedes conflicting entries below
- [process] A finished 36 s v4 ad + full brief already existed. I QC'd mid-production iterations as if they were the final intent and proposed a rebuild. RULE: ask "is there an existing brief / final cut?" BEFORE any QC or rebuild.
- [brand] The skit is for PHYSIO SPOT (men's health clinic), not heal360. Ending = Nik in navy scrubs, beige room, bulb flicker.
- [correction] voice_change with ElevenLabs "Benji" is a deliberate voice choice, not patching waste.
- [correction] 3 s kling3_0 pro clips + trims + ffmpeg edit IS the proven pipeline (start_image keyframes from gpt_image_2_5 with image_references; soul_2 only for Nik).
- [correction] The friend is NOT lifting (hands on stomach) - intended. Leak wording that passes filters: "three small water drop marks on the front panel of the shorts", "just a darker shade of the same grey".
- [correction] Spotter skin must be DRY and matte (no sweat sheen) or the leak reads as sweat - my char sheet B prompt asked for sweat sheen: wrong for this ad.
## 2026-10-10 - feedback round 3
- [hook] Klaus's skits lead with a blunt all-caps text hook stating the payoff (e.g. "BUFF BOY PISSES HIMSELF IN GYM 😂"). Comedy runs on anticipation: viewer knows, characters don't. Hook = post-production overlay only; keep crude words out of generation prompts.
## 2026-10-10 - feedback round 2: SCRIPT DRIFT (most important lesson so far)
- [script] I rewrote Klaus's skit without asking: turned a lying-still lifter into a failed bench press, and gave the leak to the wrong character. ROOT CAUSE: my QC labelled his intentional staging ("hands folded, bar racked") as a physics error.
- [rule] When the user's previous footage contradicts my reading of the joke, ASK what it means before calling it a bug. Original footage is evidence of intent.
- [rule] Before any rebuild, state back WHO does WHAT, WHOSE prop/wardrobe the gag lives on, and WHAT must stay hidden until the reveal. Get a yes.
- [rule] Puns/reveals: list what the audience must NOT see before the payoff and encode it as a hard_rule in the spec ("B's shorts out of frame in shots 1-3").
- [script] Gym skit truth: lifter lies still, deadpan; spotter scrolls; "Bro... are you spotting?" = pun on wet spots; reveal = spotter's grey shorts with damp spots (the spotter peed).
## 2026-10-10 - production round 3 (heal360 skit)
- [api] CONFIRMED: kling_o3_image_reference multi_shots fails silently on Higgsfield (3/3: with 3 refs x2, with 1 ref x1); every single-shot call succeeds. Do NOT use multi-shot on this route until Higgsfield fixes it; build skits as single shots + ffmpeg stitch.
- [api] Batch submits can be intercepted by an auto preset suggestion ("IN THE DARK") instead of creating a job - resubmit with declined_preset_id.
- [framing] With ONE wide image_reference, Kling Omni copies the reference composition and ignores CU/MCU/low-angle instructions (shots 3+4 came back wide). Every shot with a different framing needs its OWN reference still composed at that framing.
- [framing] "Lifter's POV looking up" came back as a front-on two-shot from the feet - acceptable, but true POV needs a POV reference still.
- [min] Kling min duration 3s - render 3s and trim in post for 2s beats.
## 2026-10-10 - production round 2 (heal360 skit)
- [blocking] Relative blocking ("head end", "behind his head") failed on the first start frame. Use ABSOLUTE screen positions: "lifter's head on the RIGHT of frame, spotter at far RIGHT between rack uprights". Passed first try after that.
- [blocking] Fix one thing at a time: regen with the failed frame as reference image 1 + "recreate exactly with ONE change".
- [continuity] Shot 1 action must start from the start frame's exact pose (frame showed lockout; prompt said "stalls halfway").
- [api] kling_o3_* multi_prompt: models_explore says string_array, backend REQUIRES [{prompt, duration}] objects (422 otherwise, no charge). Trust the backend.
- [api] Kling 3.0 Omni 4-shot std draft (job 8ce3f14d) sat 'queued' ~4 min then 'failed' with NO reason returned. Unresolved: moderation on shot 4 wording ("gaze ... toward A's hips") vs provider-side failure. Next attempt: strip body-part targets from gaze lines; if it fails again, split-test with a single-shot call before re-spending. Check `transactions` for refund after any failed paid job.
- [api] RETRY (job f261483b) with moderation-safe shot 4 failed IDENTICALLY (~4 min queued -> failed, no reason). Moderation hypothesis weakened; suspect kling_o3_image_reference multi-shot + 3 x 2k image_references, or provider outage. RULE: after 2 identical silent failures, stop paid retries; run a 3.75-cr single-shot diagnostic or switch route (kling3_0 + start_image 21cr/12s; seedance_2_5 draft 36cr/12s).
- [api] DIAGNOSTIC (job 2beb3406, 3.75cr): kling_o3_image_reference single-shot + ONE image_reference -> went straight to in_progress, rendered in ~2 min, PASS (geography held, identity held, audio present, 720p std). Failed jobs never left 'queued'. => fault is multi-shot mode and/or 3 x 2k references, not the model or moderation. Next isolation: multi-shot with 1 ref.
- [api] std output = 720x1280; finals need pro (1080p) or upscale.
- [api] Nano Banana Pro jobs report as nano_banana_2 in jobs_wait; quality held.
## 2026-10-10 - feedback round 1 (heal360 skit)
- [script] Klaus REJECTED all dialogue I added. Never put new lines into a generation spec; offer them separately as optional, default = his words only + silent beats.
- [image][9:16] Vertical set plates can render rotated 90 deg. Always state: "upright vertical photo, camera held vertically, floor along bottom edge, ceiling at top".
- [character] "very muscular" under-delivers; specify mass relative to an average man + named garment cut ("deep-cut bodybuilding stringer").
- [routing] Jobs requested as nano_banana_pro came back labelled nano_banana_2 - verify the model field in jobs_wait output; flag substitutions.
## 2026-10-10 - heal360 brief answers (gym skit)
- [heal360][pelvic-floor] The leak is the education hook. Imply it, never show it: bracing -> freeze -> "...oh no" -> spotter's gaze drifts below frame -> silence. The education lands on the end card ("Common. Not normal."), not in the body shot.
- [heal360] Comedic skits use ORIGINAL AI characters; Physio Niklaus appears via end card / real footage (pending his answer).
- [heal360] Causal link carries the message: no spotter -> lifter over-braces alone -> leak. Keep claims educational, no stats unless sourced.
## 2026-10-10 - seeded from QC of the 9-10 Oct gym "spotting" skit run
- [skit][gym] State a camera owner (A-POV / B-POV / neutral) for every shot; never write bare "POV".
- [skit][gym] Spotter stands behind the lifter's HEAD, facing the lifter's feet. Lifter's hands on the bar. Encode in the set map.
- [VOID] (was: lifter must be mid-press) - contradicted Klaus's intent; see master brief.
- [video] Spoken line shots >= 4 s; whole skit as one multi-shot Kling 3.0 Omni generation with native dialogue - no 3 s clips + voice_change patching.
- [video] Lock characters with Elements/Soul before motion; same wardrobe line verbatim each shot.
- [policy] No crotch/fluid visuals - restage gags; NSFW blocks burned 2 gens.
- [process] get_cost preflight + draft/std first; QC contact sheet before calling anything final.
