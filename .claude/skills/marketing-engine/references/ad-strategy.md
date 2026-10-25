# Ad strategy: performance-creative playbook (paid + organic-as-ad)
The ad-strategist agent decides **what** ads to make and **how to test them**: angles, personas, awareness, formats, hooks, volume, budget split, kill/scale and iteration. It also writes the ad brief that `/ad` (story-director) turns into scripts. It never renders, never launches, and never spends.

Sits between: `brands/<brand>.md` + strategy (`marketing/strategy/`) → **ad-strategy (this file)** → `/ad` (cinematic-ad-director.md Gates 1-5) → `/expand` (variants) → `/publish` → `/review` (analytics-loop.md) → `/learn`. The genre comes from genre-playbooks.md §0; compliance comes from compliance-packs.md + compliance-sg.md.

Evidence tags: **[LM]** = Leo Moore (sourced, §13); **[P]** = platform docs; **[3P]** = third-party practitioner/vendor; **[studio]** = our starting default, to be tuned by `/review` data. Never present a [studio] number as a benchmark.

---
## 1. Ten rules (read before any brief)
1. **The idea is most of the result.** Concept ideation and selection from research is "80, 85…" per cent; "the hook and the idea of the ad is basically 85 to 90% of the result most of the time" [LM-course ≈1:12]. Spend thinking before production.
2. **Concept = angle × format × offer × persona (+ awareness level).** Name every ad by these fields [LM-course ≈1:01, ≈1:17].
3. **Few angles, many formats.** "There's 5 to 10 angles max" per offer. "Find a winning message, replicate it across 10 to 20 formats" [LM-course ≈1:27]. Diversity means different visuals and spokespeople for the same winning argument, not 25 unrelated reasons to buy.
4. **Look like the feed, not like an ad.** Ads must "merge into the feed rather than stick out" [LM-killer ≈16:00]. Copy formats the persona already consumes organically, which is why "podcast ads work so well" [LM-course ≈1:15]. Talking-head-only accounts can sit at a 0% win rate unnoticed [LM-course ≈1:18].
5. **Start where their head already is.** Hook = the problem in the words they already use (from sales calls, DMs, reviews, comments). Prefer problem-aware over making them aware of a new problem. Avoid criteria call-outs ("8-figure brands…") and hyperbolic claims [LM-killer ≈15:00-25:00].
6. **Most ads lose.** "90% of your ads will be complete failures and 10% … will change your life"; the best hit rate he has seen is ~20% [LM-killer ≈4:00-5:00]. Optimise swings × hit rate.
7. **Winners get iterated, fast.** New hooks, a new actor, a new location, new B-roll, a new editor, a new hook stacked in front [LM-killer ≈30:00]. Diversification and iteration are different jobs; Meta says iteration should not replace true diversification [P-Meta via 3P, Dec 2025].
8. **Drama beats slop.** Story ads where characters voice the objections and the product arrives as the payoff out-perform generic AI content (Leo's opinion in ads1, not measured; see research/refs-2026-10-25/ads-leoxmoore.md). AI is the camera, not the idea.
9. **Fatigue is guaranteed. Keep a pipeline.** Meta flags "creative limited" when cost per result rises versus the ad's past, and "creative fatigue" at ≥2x [P via 3P, Jon Loomer 2025-09-15]. TikTok: "even the best ads will experience creative fatigue… refresh … often" [P-TikTok].
10. **Compliance before cleverness.** The market × industry pack decides which angles exist at all (§11). SG health kills testimonial, superlative, inducement and guarantee angles before ideation.

---
## 2. Leo Moore frameworks (verbatim-anchored; timestamps ≈ from auto-captions)
| Topic | What he says / does | Source |
|---|---|---|
| Ad job | Stop the scroll, then "Yes, I have this problem / this ad is for me / I want it solved / you can help me" | LM-killer ≈7:00-8:00 |
| Research | List problems, problems with current solutions, frustrations. Mine sales calls for the "epiphany moment" phrase and "drag [it] as high into the top of the funnel as humanly possible" | LM-killer ≈8:00; LM-course ≈1:08 |
| Simplest winning script | "Struggling with [pain]? You need [solution]. Here's how you get [outcome] without [pain]." Test 5 pains in the hook, keep the winner, spread it across formats | LM-killer ≈10:00-12:00 |
| Body | After the hook, raise perceived likelihood, cut time delay, cut effort and sacrifice (value equation): proof → why it's free/cheap → objection → result | LM-killer ≈12:00-14:00 |
| Unique problem mechanism | Name the hidden root cause of the pain, then the unique mechanism that fixes it (credits copywriter Kyle Milligan) | LM-killer ≈24:00-26:00 |
| Awareness ladder for scale | Ready-now buyers, then "thinking about it", then the bigger problem-aware market. Each step down is harder to convert but bigger. Most small spenders have not tapped out their market | LM-killer ≈27:00-29:00 |
| Direct-offer angle | Scales only when most of the market is already highly aware or the offer is a no-brainer. Otherwise it is a bottom-of-funnel asset | LM-course ≈1:03-1:04 |
| Personas | "Probably … the most overrated aspect". Target issues (e.g. "hates their agency", "GLP-1 side effects") not micro-demographics | LM-course ≈1:06-1:07 |
| Angle examples | "3 reasons why X solution doesn't work", "Her husband didn't want X to happen until [outcome]", symptom-led problem-aware, "doctor visit, bad news" (health) | LM-course ≈1:04-1:06 |
| Volume | "One ad per $1,000 in spend" as a lazy rule. At ≤$20-30k/month launch about 2x that. Exact: winners needed ÷ hit rate, using winner = significant spend above target KPI, measured over 6-12 months | LM-course ≈1:22-1:25 |
| Quality floor | "Five genuinely great ads will beat 200 slop volumes" | LM-course ≈1:26 |
| Concurrent tests by budget | <$500/day: 3-5 creatives · $500-1k: 5-10 · ~$2k: 10-20 · $3k+: 20-30 | LM-killer ≈31:00 |
| Net-new vs iterations | Budget at least 10-20% to net-new concepts; at scale most ads are iterations of winners, triggered by an SOP when an ad hits a spend-at-ROAS KPI | LM-course ≈1:32, ≈3:16 |
| Kill rule | Rarely turns ads off in a CBO test. Off if ~3x target CPA spent with no results and frequency is not low, or if it brings unqualified leads | LM-course ≈1:50 |
| Naming + feedback loop | Name ads `round_id_angle_format_avatar_offer_awareness`. Export the account, have AI report win rate and spend by format/angle/issue, review monthly | LM-course ≈1:17, ≈2:52 |
| Leading indicators at scale | Top-ad fatigue, winner replacement ratio, burnout rate of new ads, top-1/3/5 ad spend share. Fatigued winners go to a bid-cap "graveyard" campaign | LM-course ≈2:22-2:25 |
| Funnel diversity | "Funnel diversity is just as good as creative diversity": a congruent landing page per winning ad | LM-course ≈2:17, ≈3:14 |
| Gap-finding | Audit an account for missing formats, e.g. a podcast-interviewer opener introducing the founder with authority | LM-course ≈1:29 |
| Drama ads (ads1) | DR beats hidden in a scene: avatar call-out, dream outcome, objection handling, price anchor, risk reversal, urgency; product only after the promise and objections | IG reel 2026-10-20 |

---
## 3. The creative-strategy loop (one cycle = one "round")
```
RESEARCH → MATRIX → CONCEPTS (hypotheses) → BRIEFS → PRODUCE (cheap first) → LAUNCH TEST → READ METRICS (§9) → KILL / KEEP / SCALE → ITERATE (§10) → LOG (/learn) → next round
```
- **Research inputs (cite each):** sales-call/DM/WhatsApp phrases (with consent, de-identified), reviews and comments (organic only, never as ad testimony in SG health), competitor ad libraries (Meta Ad Library; TikTok Creative Center), organic outliers in the persona's feed (vidIQ `vidiq_instagram_tiktok_outlier_search`, budget rule applies), Creator Brain story bank, `marketing/reviews/`.
- **Round size:** set by §8. Each round ships net-new concepts plus iterations of last round's winners.

---
## 4. Angle matrix + format library
### 4a. Angle matrix template (one per brand × offer; save `marketing/ads/<brand>/matrix.md`)
| Issue (core problem) | Persona (issue-based) | Awareness (Schwartz: unaware / problem / solution / product / most aware) | Angle (entry point) | Proof we can legally use | Compliance flags | Status |
|---|---|---|---|---|---|---|
| e.g. "leaks when lifting" | men 25-55 who lift | problem-aware | "3 reasons pelvic-floor exercises from YouTube don't work" | mechanism animation, physio credentials | no outcome claims, no testimonials | untested |

**Angle families** (pick 5-10 per offer): pain-in-their-words · myth / "3 reasons X doesn't work" · unique problem mechanism · unique solution mechanism · doctor's-bad-news / turning point · objection-first ("I tried everything") · us-vs-them (old way vs new way; never name or disparage competitors where barred) · identity/status · convenience/time · cost-of-inaction · curiosity/secret · founder origin · direct offer (only if the market is highly aware and offers are legal) · social proof (**blocked in SG health**).

### 4b. Format library (vary the look, keep the winning argument)
| Format | Best for | Studio route | Notes |
|---|---|---|---|
| Drama / skit DR ad | TOFU-MOFU, objection-heavy offers | `/ad` + genre §2/§7, §5 skeletons | conflict = the claim; product is the payoff |
| Founder / expert talking head | trust, B2B, clinics | `/edit` talking-head-punchy | add a visual change every 2-3 s; never only this format |
| UGC / creator selfie ("yap"), unboxing, POV, day-in-life | DTC, apps | `/edit` ugc-* presets | in SG health, creator ≠ patient, no experience claims |
| Us-vs-them / old way vs new way split | solution-aware | genre §8 split rhythm | compare methods, not named rivals |
| Street interview / vox pop | TOFU, awareness, myths | real filming (consent forms) or clearly staged | no real-patient answers in SG health |
| Podcast-clip ad (host asks, expert answers) | info, health education | `/repurpose` + clipping-podcast.md | an interviewer opener adds authority [LM] |
| Green screen / receipts / news-style | myth-busting, B2B | genre §21-23 | sources on screen |
| Texting / DM drama | relationships, sensitive topics | genre §30 | composite chats only |
| Borrowed cold open / reaction-review ("Ad strategist reviews…") | organic, TITAN.AI | genre §31, editor `mode: split` | ads1 format; permission for third-party clips |
| Native static / long-copy image | older personas, FB feed | photo-effects.md, higgsfield-product-photoshoot | "random image + long story" [LM] |
| Mechanism animation / 3D explainer | health, tech | animation-3d-cartoon.md, documentary-3d.md | compliant proof substitute |
| Edu-song / jingle | low-attention categories | genre §29 | original or public-domain melodies only |
| AI-assisted photoreal | any, when real shoots are impossible | default Seedance stack | AI must look real (realism.md); no AI likeness of real people; real staff = real photos/Soul |

---
## 5. Drama-ad skeletons (10). Beats in seconds, scaled for a 45 s cut (30 s: ×0.67; 60-90 s: stretch the middle)
Common grammar (from ads1): **a hook line of conflict in second 1 → a character states the problem/benefit as a fact → others voice every objection → a withheld trade → the product as the payoff → mechanism in one line → offer/risk reversal (if legal) → callback joke + CTA.** Genre map: comedy §2 / drama-conflict §7 / mystery §14 / texting §30. Every skeleton lists who carries the gag and what stays hidden until the reveal (encode as spec hard_rules).

| # | Name | Beats (45 s) | Carries the gag / hidden until reveal | SG health swap |
|---|---|---|---|---|
| D1 | **Sceptical Gatekeeper** (ads1) | 0-3 official refuses ("I cannot accept this") · 3-10 evidence the benefit is "impossible" · 10-18 escalation ("speak to your manager") · 18-26 second official lists alternatives (they all fail) · 26-32 trade ("stamp it and I'll tell you") · 32-38 reveal + 1-line mechanism · 38-45 callback + CTA | the gatekeeper's disbelief / product name hidden to 32 s | the gatekeeper doubts a *habit* (e.g. "you can't have done 30 deadlifts with that back"); answer = an assessment approach, not a result |
| D2 | **Speak to the Manager** (service clash) | 0-3 customer explodes at the wrong person · 3-12 the real problem comes out · 12-22 staff try the usual fixes, fail · 22-30 an expert colleague asks the one right question · 30-38 mechanism · 38-45 CTA | the customer / the real cause hidden to 12 s | the expert is a registered physio explaining a common pattern; no "fixed in 1 session" |
| D3 | **Family Dinner Interrogation** | 0-3 an aunt's loaded question · 3-12 the table piles on with myths · 12-22 the quiet one pushes back · 22-32 proof by demonstration at the table · 32-40 the elders cave · 40-45 CTA | the quiet one / what they did differently hidden to 22 s | myths vs evidence (cite in SOURCES.md); no before/after |
| D4 | **The One-Upper** (villain, genre §7) | 0-3 cruel line · 3-12 the target's world · 12-25 confrontation, closer shots · 25-35 the target's quiet competence (the product/method) · 35-40 consequence lands · 40-45 side-choosing line + CTA | the target / the method hidden to 25 s | the villain mocks the condition; the brand stands with the target, never shames |
| D5 | **The Interview Panel** | 0-3 "Why should we pick you?" · 3-15 the candidate's flaw exposed · 15-25 the panel's objections · 25-35 the candidate's mechanism answer · 35-45 panel turns; CTA | the candidate / the answer hidden to 25 s | B2B/TITAN.AI fit; health: the panel = a sceptical patient's inner voices |
| D6 | **Bad News at the Doctor** (Leo's health angle) | 0-3 "Your results came back…" · 3-12 fear of the default option (meds/surgery) · 12-22 they try quick fixes, fail · 22-32 a professional explains the root cause (problem mechanism) · 32-40 the plan, not the result · 40-45 CTA | patient (actor) / mechanism hidden to 22 s | label as dramatisation; no fear-mongering; no outcome promise; neutral CTA "Book an assessment" |
| D7 | **The Unsaid Problem** (couple) | 0-3 a tense silence + one line · 3-12 misread signals (implied, never explicit) · 12-22 the argument · 22-30 one partner finds info · 30-38 the calm explanation · 38-45 they reconnect; CTA | the partner / the topic implied until 22 s | Physio Spot: clinical wording, no "your ED" (Meta personal-attributes rule), adults 25+ |
| D8 | **The Trial** (courtroom of objections) | 0-3 "The defendant claims…" · 3-25 prosecutor fires the objections one by one, the witness answers each · 25-35 the exhibit (mechanism demo) · 35-40 verdict · 40-45 CTA | the witness / the exhibit hidden to 25 s | the exhibit = an anatomy model or guideline citation, not a patient |
| D9 | **The Receipts** (texts/DMs, genre §30) | 0-3 the screenshot reveal · 3-15 the thread builds (each bubble a beat) · 15-25 the twist message · 25-35 the explanation · 35-45 CTA | the sender / the twist hidden to 15 s | composite chats; no patient chats, no real names |
| D10 | **Deadpan Anticipation Skit** (Klaus's gym-skit grammar) | 0-2 blunt text hook stating the payoff (post only) · 2-15 the viewer knows, the characters don't · 15-25 near-misses · 25-30 the reveal · 30-40 the expert turn (end card education) · 40-45 CTA | per ledger: who carries the gag; reveal hidden until 25 s | the education end card is mandatory; crude hook text only in organic post |

Per skeleton, also write a 30 s cut (MOFU) and a 15 s cut (hook + reveal + CTA) for `/expand`.

---
## 6. Hook bank structure (`marketing/ads/<brand>/hooks.md`)
One row per hook. Hooks are tested in front of a winning body before new bodies are written.
| id | angle | awareness | type (question / statement / call-out-by-problem / conflict line / visual-only / text-over-action / borrowed cold open) | first frame (what the eye sees) | spoken line | on-screen text | source phrase (customer words, cited) | compliance ok? | tested in (ad names) | hook rate | status |
Rules: the first frame and first line carry the problem by second 1-3 (TikTok: hook, then body, then close [P-TikTok]). Never open on a logo-only frame (studio default). Write 5 hooks per concept (`/story` does 5 by default). Crude hooks go in post only.

---
## 7. Ad brief template (`projects/<p>/AD_BRIEF.md`; feeds `/ad` Gate 1)
```
AD BRIEF - <brand> - round <n> - concept <id>
Ad name: R<n>_<conceptid>_<angle>_<format>_<persona>_<offer>_<awareness>_<hook#>
Objective + optimisation event: (purchase / lead / booking / WhatsApp click) · platform(s) + placement · aspect(s)
Persona (issue-based): ... · awareness level: ...
Core issue in THEIR words (sourced): "..."
Angle + hypothesis: "We believe <persona> will <act> because <insight>; evidence: <source>."
Format + genre module (genre-playbooks.md §0) + StyleCard if any
Hooks (3-5): visual + spoken + text, one per row
Body beats: (pick a §5 skeleton or the LM simple script) with seconds
Proof allowed: (what we can legally show) · Proof banned: ...
Offer + CTA: exact channel; legal in this market? (§11)
Compliance pack: <industry> × <market>; red lines restated
Success metric for this test: primary KPI + guardrail (e.g. CPA ≤ target, lead quality ≥ X) - baseline from reviews or "baseline TBD"
Production route + cost: (/ad cinematic, /edit, /expand) - cheap first
Iteration plan if it wins: next 3 iterations (§10)
```

---
## 8. Testing plan template (one per round; `marketing/ads/<brand>/round-<n>.md`)
```
Round <n> · dates · budget/day · target CPA (or ROAS) · break-even CPA
Volume: concurrent creatives per LM table (§2) · monthly concepts ≈ spend/$1k (≥2x at low spend) - or winners needed ÷ hit rate
Budget split [studio default, adjust from data]:
  70% proven winners + their iterations (scaling) · 20% iterations under test · 10% net-new concepts (LM: ≥10-20% to net-new)
  At launch with no winners: 100% testing, 3-5 concepts × 2-3 hooks
Structure: one testing campaign (CBO/Advantage+) with concept-level ads; winners graduate to the scaling campaign (+ partnership/whitelisted ads where available)
Read date: after each ad has spent ≥1-2x target CPA or has enough impressions to judge hook rate [studio default]
```
### Kill / keep / scale rules
| Signal | Action | Source |
|---|---|---|
| Spent ~3x target CPA, 0 results, frequency not low | Kill | LM-course ≈1:50 |
| Results but unqualified leads (sales feedback) | Kill or re-angle; check the hook's promise | LM-course ≈1:50, LM-killer ≈20:00 |
| Low hook rate, good CTR/CVR among viewers | Keep the body, new hooks (§10 rung 1) | [studio] |
| Strong hook rate, weak hold | Recut the body: tighten the first 10 s, add stimulation | [studio], TikTok code 5 [P] |
| Good CTR, weak CVR | Landing-page congruence / offer; make an ad-specific page | LM-course ≈2:17 |
| CPA ≤ target with "significant" spend (define per account) | Winner: trigger the iteration SOP + graduate to scaling | LM-course ≈1:22, ≈3:16 |
| Meta "Creative limited" (CPR up, <2x) | Queue iterations now | P via Jon Loomer |
| Meta "Creative fatigue" (CPR ≥2x past) | Replace or iterate; optionally bid-cap "graveyard" | P via Jon Loomer; LM ≈2:25 |
| Scale step | Raise budget gradually [studio default ≤20-30% per step]; watch CPA 3 days | [studio] |
| Top ads fatiguing, no replacements | Leading indicator of ROAS drop: emergency iteration batch | LM-course ≈2:23 |

---
## 9. Metric diagnosis table (video)
Definitions: **hook rate** = 3-s video plays ÷ impressions (Motion: "20-40% is generally solid") [3P-Motion]. **Hold rate** = ThruPlays (15 s or complete) ÷ 3-s plays (tool definitions vary; state the one used). **CTR (link)** = link clicks ÷ impressions. **CPM** = cost per 1,000 impressions. **CVR** = results ÷ clicks. **CPA** = spend ÷ results. Cost per click = CPM ÷ (1,000 × CTR); CPA = CPC ÷ CVR [LM-course ≈0:06]. Use the account's own baselines first.

| Symptom | Likely cause | Fix (route) |
|---|---|---|
| High CPM | weak/"scammy" creative quality, narrow audience, seasonality, restricted category | better native-looking creative, broaden, check policy flags |
| Low hook rate | first frame/line doesn't name their problem; looks like an ad | new hooks (§6), a borrowed-format opener, a visual hook change |
| Hook OK, hold low | slow body, no escalation, product too early with no reason to stay | tighten to the §5 beats, stims every 1.5-3 s (ledger), cut the intro |
| Hold OK, CTR low | no clear next step, CTA buried, offer unclear | spoken CTA naming the channel, CTA card, clearer offer |
| CTR high, CVR low | clickbait mismatch, landing page incongruent, bad placement/demographic clicks | match page to the ad; check placement + age breakdown [LM ≈1:57] |
| CVR fine, lead quality low | the hook attracts the wrong people (big-claim hooks) | problem-specific hooks; qualify in the body [LM-killer ≈21:00] |
| Winner's CPA rising week on week | fatigue | iteration ladder; new formats for the same angle |
| All ads drop at once | tracking, offer, seasonality, CPM inflation, or no new launches | check inputs: launches/week, win rate, top-ad fatigue [LM ≈2:05] |

---
## 10. Iteration ladder (cheapest first; change ONE variable per rung)
1. New hook in front of the same body (3-5 hooks; text-only and visual-only variants). Editor job, ~0 credits.
2. Same script, new edit: pacing, captions, B-roll, length (15/30/60), aspect (9:16/1:1/4:5/16:9). `/expand`.
3. Same script, new spokesperson / actor / location (approved @ASSETS; Genjutsu for performance).
4. Same angle, new format (§4b), e.g. talking head → drama skit → podcast clip → native static.
5. Same angle, new awareness entry (problem-aware ↔ solution-aware).
6. New angle for the same persona (next row of the matrix).
7. New persona/issue or new offer/funnel (a congruent landing page counts as a test).
Log every rung in the ad name (`_it<rung>`). Meta treats iteration and diversification as separate: keep ≥10-20% net-new concepts every round.

### 10b. The 25-lever iteration map ("you found a winning ad: here are 25 iterations")
Source: @gurnoorsinghofficial reel "Save this for your next winning ad" (IG, 2026-10, 27.9 s, 729 likes; research/refs-2026-10-25/ads-iterations.md). His list is the 25 levers; the columns below (what changes, rung, cost, what it tests) are ours.
Rule: from a winner, change ONE lever per variant, keep everything else byte-identical, and name it `<winner>_it<rung>-<lever>`. Start at the cheapest levers and move down the table only when the cheap ones stop finding lift.

| # | Lever | What you change (example for a scam-tips media brand) | Rung (§10) | Cost | What a win tells you |
|---|---|---|---|---|---|
| 1 | Avatar | tourists → expats → locals | 7 | high (new concept) | who the message works for |
| 2 | Sub-avatar | first-time backpacker → family with kids → business traveller | 6-7 | mid | which slice converts cheapest |
| 3 | Angle | "save money" → "stay safe" → "look like a local" | 6 | mid | the argument that sells |
| 4 | Desire | stress-free trip / insider status / bragging rights | 6 | mid | the motivation behind the click |
| 5 | Pain point | overcharged taxi / fake massage menu / stolen phone | 6 | mid | which fear or annoyance is sharpest |
| 6 | Awareness stage | unaware ("this happens to 1 in 3…") ↔ problem-aware ↔ solution-aware ("our map shows…") | 5 | mid | how much setup the audience needs |
| 7 | Unique mechanism | "the 3-question taxi test" / "the locals' price list" | 6 | mid | the believable "how" |
| 8 | Core promise | "never get ripped off" (check compliance) → "know the fair price in 10 s" | 6 | mid | the result people want |
| 9 | Emotion | anger (exposé) / relief / humour / pride | 4-6 | mid | the energy that stops the scroll |
| 10 | Offer | free guide / app / tour / newsletter / sponsored partner deal | 7 | high | what they'll actually take |
| 11 | Hook | first 1-3 s: line, visual, text (keep 3-5 per body) | 1 | ~0 | attention; read hook rate first |
| 12 | Storyline | exposé → POV → mockumentary → texting receipts | 4 | mid | narrative fit |
| 13 | Analogy | "a taxi meter that runs like a slot machine" | 2-4 | low | comprehension |
| 14 | Curiosity gap | "the 3rd one got me too" / hide the answer to the end | 1-2 | low | hold rate |
| 15 | Format | talking head / drama skit / street interview / carousel / static / texting scene | 4 | mid | the feed fit |
| 16 | Creator | Vietnamese host / Western expat / duo / AI character (clone workflow, labelled) | 3 | mid | trust and identification |
| 17 | Opening scene | the street, the receipt, the reaction face | 1 | low | the visual stop |
| 18 | B-roll | real street footage vs graphics vs screen recordings | 2 | low | credibility, pace |
| 19 | Editing style | style-archetypes.md preset swap (genz-header-skit ↔ news-expose ↔ texting-suspense) | 2 | ~0 (`/expand`) | the style that suits this audience |
| 20 | Pacing | 0.8 s vs 2.5 s average shot | 2 | ~0 | drop-off curve |
| 21 | Video length | 15 / 30 / 45 / 60 s | 2 | ~0 | the attention budget |
| 22 | On-screen text | header copy, kicker, caption pack | 1-2 | ~0 | the silent-viewer hook |
| 23 | Authority figure | a local guide / tour operator / police advisory quote / the founder | 3 | mid | believability |
| 24 | Price framing | "free" / "less than a bánh mì" / per-day cost | 7 | low-mid | conversion friction (check compliance) |
| 25 | CTA | save / follow / DM keyword / link / comment-to-get | 1-2 | ~0 | the action they'll take |

Cheap-first order for a fresh winner:
1. Hook ×5, on-screen text ×3 and CTA ×2. Ten variants, all from the editor, no new footage.
2. Pacing, length and editing style through `/expand`.
3. Creator / opening scene / B-roll: one re-shoot day.
4. Storyline / format / emotion.
5. Angle / pain point / desire / mechanism: new matrix rows.
6. Avatar / sub-avatar / offer / price: new concepts.

Read the diagnosis table (§9) first: a low hook rate means change levers 11, 14, 17 or 22; a good hook with a bad hold means 12-14 or 20; a good hold with a low CTR means 8, 10 or 25; clicks that don't convert mean 10, 24 or the landing page.

---
## 11. Compliance overlay per market (apply at the angle stage; details in compliance-packs.md, compliance-sg.md)
| Market × industry | Angles/formats blocked or changed | Safe substitutes |
|---|---|---|
| **SG health** (Physio Spot, heal360) | testimonials, reviews, before/after, patient stories, "X patients helped"; superlatives/comparisons; free consult, discounts, "limited slots", price urgency; guarantees/"cure"/"in 3 sessions"; money-back offers; price anchoring vs other providers; implying the viewer's condition ("your ED") on Meta | problem-in-their-words hooks, myth-busting, mechanism animation, clinician explainer, dramatised skits labelled as fiction with actors never posed as patients, education end card, CTA "Book an assessment" / "WhatsApp us to ask about appointments" |
| SG beauty / cosmetics | drug-like claims ("reverses ageing", "repairs DNA") | cosmetic wording ("looks smoother"); disclose filters/retouching |
| SG supplements (HSA) | disease claims | permitted claims only |
| MY health | ads often need prior MOH approval | plan pre-clearance into the timeline |
| AU health (AHPRA) | testimonials for regulated health services | same as SG health |
| UK (ASA/CAP) | unsubstantiated health/weight claims; undisclosed influencers | substantiation file; #ad / paid-partnership tools |
| US (FTC/FDA) | fake/undisclosed reviews; "results not typical" is no safe harbour | substantiated claims; disclosed endorsements |
| VN (Power Protein) | health/food claims need permits; confirm the local pack | load the VN pack before ideation |
| All markets | AI likeness/voice of real people; fake scarcity; algospeak to dodge moderation | original characters; real terms and end dates; plain clinical wording |
Drama ads in regulated markets: every character is clearly fictional, nobody claims a personal result, and the conflict dramatises the *problem* or a *myth*, not an outcome.

---
## 12. Review loop (with analytics-loop.md)
Monthly (or per round): export → group by naming fields → report spend, CPA, hook rate, hold, CTR, CVR, win rate and spend share **by angle, format, persona, awareness** → top 3 learnings → `/learn` writes 1-3 testable rules → update the matrix status and hook bank → plan the next round. Track: launches/week, win rate, winner replacement ratio, top-3 ad spend share [LM].

---
## 13. Sources (accessed 2026-10-25)
- **LM-ads1:** Leo Moore, Instagram reel "Ad Strategist Reviewing AI Ad", 2026-10-20, https://www.instagram.com/reel/DeteQDizpDr/ (breakdown: research/refs-2026-10-25/ads-leoxmoore.md).
- **LM-killer:** Leo Moore, "How To Make Killer Meta Ads (to get clients in 2025)", YouTube, 2025-07-04, https://www.youtube.com/watch?v=xT_lvYU9hx8 (auto-caption transcript; timestamps approximate).
- **LM-course:** Leo Moore, "The LAST Meta Ads Course You'll Ever Need to Watch (2027)", YouTube, 2026-10-17, 3 h 29 min, https://www.youtube.com/watch?v=_Gkus1moE3Q (auto-caption transcript; timestamps approximate).
- Leo Moore channel list: https://www.youtube.com/@LeoXMoore (titles incl. "How to Scale Facebook Ads with Better Creative (Post Andromeda)", not transcribed: YouTube bot-check). X bio: https://x.com/LXMoore_ (via search snippet; self-reported spend). Instagram profile: https://www.instagram.com/leoxmoore/ (not scraped).
- TikTok for Business, Creative Codes (6 principles; hook/body/close; Kantar Jan 2021 sound research), https://ads.tiktok.com/business/en/creative-codes (accessed 2026-10-25).
- Motion, "What is Thumbstop rate / hook rate?", glossary, last updated 2026-04-17, https://motionapp.com/library/glossary/thumbstop-rate-hook-rate
- Jon Loomer, "Creative Fatigue" (Meta's creative limited / fatigue statuses; links Meta help 1346816142327858), 2025-09-15, https://www.jonloomer.com/creative-fatigue-meta-ads/ ; Meta Business Help: https://www.facebook.com/business/help/1346816142327858
- Meta, creative diversification vs iteration (Dec 2025 post), cited second-hand via https://easyinsights.ai/blog/meta-andromeda-impact-on-ad-strategy/ and https://novoads.ai/blog/creative-diversity-meta-ads. Verify the wording on Meta's site before quoting externally.
- Eugene Schwartz, *Breakthrough Advertising* (1966): the five awareness stages.
- Internal: compliance-packs.md, compliance-sg.md, genre-playbooks.md §0/§2/§7/§30/§31, cinematic-ad-director.md, analytics-loop.md, ledger/learnings.md.
- Not used as evidence: third-party hook-rate benchmark tables that disagree (25-45%). Use account baselines.

---
## Agent draft
```markdown
---
name: ad-strategist
description: Performance-creative strategist for paid and organic-as-ad video. Builds the angle matrix (issue × persona × awareness × angle × format), hook bank, ad briefs, drama/skit DR ad concepts, testing rounds (volume, budget split, kill/scale rules), metric diagnosis and iteration plans, from brand files, research, competitor/organic outliers and ad-account exports. Use for "ad strategy", "what ads should we test", "why is this ad not working", "iterate this winner", "drama ad / skit ad for <brand>", "creative testing plan", "hook ideas for ads". Hands concepts to /ad; never renders, launches, posts or spends.
tools: Read, Write, Edit, Grep, Glob, WebSearch
---
Follow `.claude/skills/marketing-engine/references/ad-strategy.md` with `compliance-packs.md`, `compliance-sg.md`, `analytics-loop.md`, and `.claude/skills/higgsfield-creative-director/references/genre-playbooks.md` §0.
1. Read first: `ledger/learnings.md`, `brands/<brand>.md` (offer, compliance pack, edit-brand), `marketing/strategy/<brand>.md`, latest `marketing/reviews/`, existing `marketing/ads/<brand>/` (matrix.md, hooks.md, round-*.md) and any ad-account export Klaus supplies. Ask "Is there an existing brief, script or winning ad?" before proposing anything; existing winners and Klaus's scripts are version A.
2. Compliance gate first: load the brand's industry × market pack and strike blocked angles/formats (§11) before ideation. SG health: no testimonials, reviews, before/after, superlatives, free-consult/discount/limited-slot inducements, guarantees, money-back, competitor price anchors, or implying the viewer's condition.
3. Research: customer phrases (sales calls, DMs, comments: consented and de-identified), competitor ad libraries, organic outliers in the persona's feed (WebSearch; vidIQ only via the main session with the budget rule). Cite source + date for every insight; mark guesses `[draft]`. Never invent stats, benchmarks or quotes.
4. Build or refresh the angle matrix (§4a): 3-5 issues, 5-10 angles max per offer, an awareness level per row, legal proof per row. Then pick formats (§4b) the persona already consumes, varying the look rather than the argument.
5. Write concepts as hypotheses: ad name per §7 naming, 3-5 hooks each (§6 bank), body from the LM simple script or a §5 drama skeleton (beats in seconds, who carries the gag, what stays hidden), genre module + `genre_key`, CTA naming the channel. Save `projects/<p>/AD_BRIEF.md` per chosen concept.
6. Testing round (§8): volume (≈1 ad per $1k spend, ≥2x at low spend, or winners needed ÷ hit rate), concurrent creatives by daily budget, budget split (≥10-20% net-new), kill/keep/scale table, read date. Use real baselines from reviews or "baseline TBD"; label studio defaults as such.
7. Diagnosis (when data is supplied): compute hook rate, hold, CTR, CVR, CPA by angle/format/persona; use the §9 table to name the broken stage; prescribe the cheapest rung of the §10 iteration ladder that tests it. One variable per iteration.
8. Hand-offs: concepts → `/ad` (story-director Gates 1-5, cheap drafts first); winners → `/expand` variants; packaging → `/publish`; results → `/review` → `/learn`. Never launch, post, schedule or spend; paid-platform setup goes through the `anthropic-skills:ads-*` skills only with Klaus's explicit go.
9. Write outputs to `marketing/ads/<brand>/` (matrix.md, hooks.md, round-<n>.md, diagnosis-<date>.md). End with what changed, the round's top 3 bets with hypotheses, max 5 tappable questions for Klaus, and the next command.
```
