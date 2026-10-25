# LinkedIn playbook: organic, comments, outreach, ads, clinic rules, weekly SOP

LinkedIn now gets the same depth as TikTok and IG. This file is the operating manual. `platform-signals.md` keeps the cross-platform ranking model, the profile spec and the §8 gate. Formats live in the style home (`styles/linkedin.json`, `python scripts/styles.py find --family linkedin`). Sources, dates and evidence notes are in `research/sources-linkedin.md`.

**Labels:**
- **[O]** official LinkedIn or regulator.
- **[R]** research, including van der Blom's Algorithm InSights (secondary research) and LinkedIn papers. **[R-v]** vendor dataset.
- **[P]** practitioner.
- **[RoT]** rule of thumb.
- **[unverified]** circulates online with no primary source. Do not quote it as fact.

## 1. How the feed works now (2025-2026)

**Ranking [O].** Engineering blog, 2026-03-12:
- One LLM dual-encoder retrieves posts by topic interest, including from people you are not connected to.
- A sequential Generative Recommender reads more than 1,000 past interactions and predicts click, skip, long dwell, like, comment and share.
- Interests are inferred from profile text even without history.
- New posts are embedded within minutes.
- No weights are published.

**Downranked [O].** Tim Jurka (VP Engineering), 2026-03-12:
- "comment YES" bait, poll-baiting and click-driven posts
- recycled thought leadership that says little
- video unrelated to its text
- engagement pods and comment automation; third-party tools and extensions are "not allowed"

**Rewarded [O].** Actionable insights: trend breakdowns and leadership perspectives.

**AI slop [O, reported].** 2026-07-30:
- LinkedIn added a "seems like AI slop" report button and rolled back the AI "enhance post" feature.
- Van der Blom 2025 [R]: fully AI-written posts got about 2.8x less reach and about 5x less engagement.
- **Studio rule:** the human's own story, data and opinion; AI only edits.

**Reach is down, relevance is up [R].** Van der Blom 2025, about 1.8M posts:
- Views, engagement and follower growth fell 40–60%. Headline numbers conflict between write-ups.
- His reading: shown to fewer but more relevant people.
- Company pages reach about 1.6% of followers (directional).

**What to optimise:**

| Lever | Rule | Evidence |
|---|---|---|
| Topic consistency | Headline, About and posts stay inside your pillars so the LLM can place you. Say the keyword in plain text in line 1–2 | [O] mechanism + [RoT] |
| Saves and sends | Design for them: frameworks, checklists, tables, carousels. Saves lift the odds of suggested-feed distribution by more than 60% | [R] |
| Dwell | Hook ≤140 characters over 2 lines (mobile fold), then substance. 700–900 characters is van der Blom's reach sweet spot | [P]/[R] |
| Meaningful comments | Ask questions experts can answer. Reply to every real comment substantively | [O] predicted action |
| Out-of-network reach | Educational posts travel beyond your network; personal stories mostly reach people who know you. Mix both on purpose | [R] |
| Format diversity | Rotate text, image, document and video. Same-format streaks lose reach ("LinkedIn values diversity") | [R] |
| Links | No published penalty. Measured 26.5% lower reach (Ordinal, 900k posts) to more. Use links only on conversion posts and accept the cost | [O]/[R-v] |
| Edits | Fix typos only. Large edits after posting, and above all adding or removing a link, cut reach | [R]/[R-v] |
| Hashtags | 0–3, as labels. The hashtag feed and follow were removed; no reach boost | [R] |
| Tagging | Only people who are in the post and will reply. Unanswered mass tags tank posts | [R]/[P] |
| Formatting | ≤5 decorative emoji. Single blank lines, never double. Don't flood your own comments. Company-page first comments weigh less | [R] |
| Golden hour | Only post when you can reply for 60 minutes. No official threshold | [RoT] |
| Frequency | Pages weekly or more (LinkedIn: 2x engagement). People 2–5 posts a week | [O]/[RoT] |

**Ignore these [unverified]:**
- "save = 5x like", "comment = 15x"
- "561% employee advocacy reach"
- "13% Lead Gen Form conversion"
- "edit at 15 min for +14%"
- "65% personal vs 5% page reach"

## 2. Formats: what each is for

Pick from `styles/linkedin.json`. Every entry has a fill-in template.

| Format | Use for | Specs and evidence |
|---|---|---|
| Text only | Opinions, stories | ≤3,000 characters. Below-average reach overall, but works with strong hooks [R] |
| Text + image (default) | Most posts | Vertical, authentic own-camera photos beat polished brand graphics. The image must match the text; a selfie on an educational post gets punished [R]. Infographics drive saves |
| Document carousel | Frameworks, checklists, saveable teaching | PDF 4:5 or 1:1, ≤300 pages / 100 MB [O]. 6–12 slides (watch for "document fatigue") [R]. **Render with the cards engine** (§10) |
| Native vertical video | Trust, face time, B2B explainers | 3 s–15 min, ≤5 GB [O]. Under 1 minute preferred; you as the star; captions [R]. Preset `linkedin-founder-video`. §9 |
| Newsletter | Repeat reach, depth, funnel | Every edition sends push + in-app + email to all subscribers [O], so it bypasses the ranker. Followers are auto-invited [O]. Every 2 weeks |
| Poll | Genuine research only | High reach [R] but poll-baiting is downranked [O]. Publish the results as a carousel |
| Events / Live | Webinars, launches, AMAs | Live needs >150 followers, a clean record and an account ≥30 days old [O] |
| Company page post | Credibility, hiring, ads base | A complete page gets 30% more weekly views [O]. Organic reach is low; staff add comments when they have something to say |
| Articles (non-newsletter) | Reference / search | Low feed reach. Prefer the newsletter |
| Collaborative articles | Skip | The Community Top Voice badge was retired in Oct 2024 |

## 3. Post anatomy

- **Fold:** about 140 characters on mobile, about 210 on desktop. Short lines truncate earlier. The hook must land in two short lines.
- **Length:**
  - 700–900 characters for reach.
  - SLAY stories run 150–250 words.
  - Long posts (1,500–2,500 characters) only when every line earns its place.
- **Readability:** 1–3 line paragraphs, single blank lines, bullets or numbers for lists.
- **Structures:**
  - SLAY: Story → Lesson → Actionable → You (Lara Acosta) → script style `acosta-slay`.
  - Content matrix: one idea × 5–7 formats (Justin Welsh) → `welsh-linkedin`.
  - Topic → aspects → hooks (Jasmin Alić).
- **CTA (one per post), in order of preference:**
  1. A question that invites expertise
  2. "save this"
  3. "send to a <role>"
  4. The newsletter (Featured + banner)
  5. "DM me <word>" only on conversion posts
  - Never "comment YES".
- **First comment:** context, source link or data table. Never a bait trick.
- **12 templates:** contrarian, framework, listicle, failure lesson, behind the scenes, case study, data observation, myth vs evidence, story → principle, trend breakdown, how-to, genuine question. All are in `styles/linkedin.json` (`styles.py find --family linkedin`).

## 4. Comment strategy (manual only)

- **Why:**
  - LinkedIn's own creator account says commenting weekly can triple profile views [O, reported].
  - One comment raises the chance of seeing that creator's next post by about 80%, versus about 40% for a reshare and 25% for a like [R]. Affinity grows both ways.
- **Quality:**
  - 2–4 sentences (25–60 words) that add a fact, example, respectful disagreement or question.
  - Longer, personalised comments drove more profile views (a small test) [R-v].
  - Never generic praise. **Never AI-written or automated comments** (explicitly targeted [O]).
- **Targets:** 30–50 accounts per person in three tiers:
  - (a) buyers and prospects (SG/MY/UK SME owners, HR, ops)
  - (b) peers at a similar size
  - (c) 5–10 big voices in AI, SME and health
  - Comment early on posts likely to take off.
- **Cadence [RoT]:**
  - 2 × 15–20 minute blocks a day, with 5–10 substantive comments.
  - Reply to all comments on your own post within 60 minutes of posting, then twice a day for 48 hours.
- **Creator mode** was removed in 2024 [O]; all its tools are open. Set **Follow** as the primary button if settings allow (verify in-app).

## 5. Profile, page, Sales Navigator, outreach

- **Profile** (adds to the platform-signals spec):
  - Featured = newsletter, one lead magnet, one best post.
  - Custom URL. Real photo. Banner = one CTA.
  - Services only if relevant.
- **Company page:**
  - Every field complete: logo, overview, site, CTA button, industry, size, locations.
  - Post weekly or more.
  - Showcase pages only for genuinely separate audiences.
  - Named admins.
- **Sales Navigator (manual social selling):**
  - ICP lead and account lists. Example: SG SMEs, 11–200 staff, F&B, retail or professional services; owner, MD or ops titles.
  - Alerts on job changes and posts. Engage before reaching out.
  - Core plan: about 50 InMail credits a month, rolling over to 150. A credit comes back if the recipient replies within 90 days. Verify in the plan.
- **Connection requests:**
  - LinkedIn doesn't publish the weekly cap (about 100 per week [P]).
  - Notes are about 200 characters.
  - **10–20 hand-written requests a day maximum, each with a reason.**
- **DMs:**
  - No pitch in message 1. Be specific or ask one question.
  - Offer value by message 2–3. Ask for a call only after they engage.
  - Never volume templates or automation (User Agreement §8.2 [O]).
- **Off-platform:** SG PDPA + DNC before WhatsApp or SMS; UK GDPR + PECR for email.

## 6. LinkedIn Ads (TITAN.AI; cost gate + Klaus approval)

**Objectives:** awareness, engagement, video views, website visits, lead gen, conversions, talent.

**Thought Leader Ads (TLA)**, the default:
- Sponsor a person's post. The author approves.
- Works with non-employee posts (1st- or 2nd-degree connections, or a pasted URL) since 2024.
- Eligible: image, video, link and event posts.
- Not eligible: documents, polls, multi-image posts, reshares. Articles and newsletters are disputed; check in Campaign Manager.
- Vendor benchmark (ZenABM 2026, 211 companies) [R-v]:
  - Median CTR 2.68%, CPC $2.29, vs 0.42% for single image and 0.24% for video.
  - Fatigue at about 12 weeks vs 4–5 for single image.

**Document Ads:**
- PDF, DOC or PPT, ≤300 pages.
- Optional gate: preview 3–4 pages, then a Lead Gen Form unlocks the rest [O].

**Lead Gen Forms:**
- 3–5 fields plus one qualifying question; CRM sync.
- SG: PDPA consent line + purpose statement.
- Lead quality is often lower [R-v].

**Conversation / Message Ads:**
- Pay-per-send, so use them for warm retargeting only.
- EEA and Switzerland require opt-in [O]. Confirm SG and UK in Campaign Manager.

**Matched audiences:**
- Minimum 300 members; about 50k suggested [O].
- Sources: Insight Tag site visitors, video viewers (25/50/75/97%), form openers and submitters, page visitors, event attendees, company and contact lists.

**TITAN funnel:**
1. TLA or video to the cold ICP.
2. Retarget 50%+ viewers with a gated Document Ad (playbook).
3. Retarget openers with a Conversation Ad or website conversion (book a call).

**Budgets:**
- Minimum $10/day and $100 lifetime [O]; Dynamic Group Budget $30/day [O].
- Spend can run up to 50% over the daily budget [O].
- Learning floor: SGD 50–100/day per campaign for 2–4 weeks [RoT].

**Benchmarks [R-v]:**
- Dreamdata: ROAS 113% (2024) → 121% (2025); CPC €5.35 → €5.98.
- Sponsored CTR 0.4–0.65%.
- APAC single-image CPC £1.55 vs EMEA £3.98 (2024, one agency).
- UK: £5–12 mid-level, £15–25+ C-suite.
- No SG benchmark exists: use APAC, then your own 30-day data.

**Strategy [R]:** the 95:5 heuristic (B2B Institute / Ehrenberg-Bass): about 5% of buyers are in market at any time. Build memory with the 95% (TLA, video); activate the 5% (retargeting, forms). It is contested, so treat it as a heuristic.

**Weekly ad check:**
- CTR, CPC, cost per lead, SQL rate.
- Pause any TLA running 4 weeks below 1.5% CTR [R-v threshold].
- Skills: `anthropic-skills:ads-linkedin`, `manifold:research-linkedin-ads`.

## 7. Founder personal-brand system (Klaus)

**Pillars:**

| Pillar | Share | Reach behaviour |
|---|---|---|
| AI for SMEs (how-tos, teardowns, tools) | 40% | educational, travels out of network |
| Building TITAN (behind the scenes, numbers, decisions, hiring) | 20% | |
| Founder story and values | 15% | reaches people who know you, builds trust |
| Market POV (SG/MY/UK SME trends, contrarian) | 15% | |
| Proof (anonymised, permissioned client cases) | 10% | |

**Cadence:**
- 3–4 posts a week, rotating formats.
- Newsletter every 2 weeks.
- Daily comment blocks.

**Batching:**
- One 90-minute filming block (4–6 vertical clips).
- One 2-hour writing block (4 posts + the newsletter).

**Repurposing:** podcast or long video → transcript → 3 text posts + 1 carousel + 2 vertical clips + 1 newsletter (`/repurpose`, clipping-podcast.md).

**Funnel:** post → profile → Featured/banner → newsletter (notification reach floor) → monthly lead magnet → owned email list (PDPA consent) → call.

**Weekly tracker** (analytics now show saves, sends, profile views from the post and followers gained from the post [O]):
- Per post: impressions, members reached, saves, sends, comments (and how many are substantive, 25+ words), profile views from the post, followers gained, link clicks.
- Per week: profile views, net followers, newsletter subscribers, inbound ICP DMs and requests, conversations, calls booked, pipeline SGD, deals.
- Monthly: the top 3 by saves + sends and by profile views. Do more of those formats and pillars. `/review` → `/learn`.

## 8. Clinic directors on LinkedIn (SG): compliance gate

*Not legal advice. Confirm each entity with counsel or MOH.*

**Which rules apply:**
- **Doctor-led clinics** are HCSA licensees: the Healthcare Services (Advertisement) Regulations 2021 apply in every medium, plus the SMC Ethical Code and Guidelines (2016).
- **Standalone physio** falls under the AHPC code.
- MOH announced (2025-03-07) a review allowing some allied-health professions to advertise under HCSA content rules. No implementation date was found. **Apply HCSA-level rules anyway.**

**Hard rules [O, MOH FAQ excerpts]:**
- No testimonials, endorsements or patient photos on the licensee's website or social media, including reposts of patient posts.
- Paid reviews breach Reg. 14.
- Laudatory statements are prohibited **even if true**.
- No inducements.
- SMC: no testimonials on any medium the doctor controls.

**LinkedIn traps:**
1. Hide patient **Recommendations**. Never request them.
2. Don't enable or ask for **Service-page reviews**.
3. Never repost or pin patient or partner praise.
4. Headline and About: accurate credentials only. No "leading", "top", "best", or "specialist" unless formally recognised.
5. **Boosting or a TLA of clinic posts = advertising.** Full HCS rules apply. No free assessments or discounts.
6. Real cases, even anonymised outcome stories, read as testimonials. Use labelled composites with no outcomes claimed.

**Lower-risk formats:**
- Myth vs evidence (`myth-evidence`), with guidelines cited and "educational, not individual advice".
- Conference and CPD takeaways; research summaries.
- Leadership and operations: team building, training standards, patient-safety processes (no patients shown).
- Industry commentary: workforce, ageing, men's health awareness.
- Equipment and protocol behind the scenes.
- B2B: corporate wellness and ergonomics for HR buyers.
- Speaking and event posts.

**CTA:** neutral only ("Book an assessment", "contact the clinic"). No urgency or price hooks.

Every clinic post and profile passes `compliance-sg.md` before publishing. Re-check the profile quarterly.

## 9. Video on LinkedIn

- **Platform:**
  - A full-screen vertical video feed rolled out in 2025 [O]; uploads up 36% year on year.
  - Van der Blom says the early vertical boost was later turned down [R].
- **What works [R]:** vertical, native upload (YouTube links become link posts), under 1 minute, captions, **you as the star** speaking to the ICP. That beats event or product footage.
- **Matching rule [O]:** video unrelated to the text gets no extra reach. Caption line 1 and the first spoken sentence state the same promise.
- **Specs [O]:**
  - Organic: 3 s–15 min, ≤5 GB.
  - Ads: 3 s–30 min; 15–30 s recommended; 16:9, 1:1, 4:5 or 9:16.
  - Upload an SRT *and* burn in captions.
  - 79% of feed video plays muted (2021 [O]).
  - Use a single audio source (2022 [O]).
- **Edit (preset `linkedin-founder-video`):**
  - 9:16 or 4:5.
  - 2–4 word captions in the lower third.
  - B-roll or screen recordings every 3–6 s on key nouns.
  - Auto panel **boards** on numbers, steps and definitions.
  - Low ducked bed or none.
  - One CTA line. 30–75 s.
- **Cover:** a custom cover where available: face plus a 3–5 word claim. The first frame works as a cover.

## 10. Production in this repo

| Need | Command |
|---|---|
| Pick a format or offer options | `python scripts/styles.py offer --brand titan-ai --platform linkedin --goal "<goal>"` |
| Write the post | `/story` (story-writer) with the chosen `styles/linkedin.json` template + script style; clinic posts → compliance gate |
| Document carousel (PDF) | Write `projects/<p>/carousel.json` (cards: title/stat/list/steps/quote/compare/definition/myth_fact/chart/cta) → `python tools/editor/editor.py cards projects/<p>/carousel.json --aspect 4:5 --brand <brand>` → PNG + `slides.pdf` + contact sheet. LOOK at the contact sheet |
| Vertical video | `/edit` with `--preset linkedin-founder-video`; boards auto-planned; `editor.py boards` to re-plan; QC fails stat boards with no source |
| Package (caption, first comment, alt text, document title) | `/publish` (distributor) using §3 and the platform-signals §8 gate |
| Weekly loop | `/linkedin week` (see the command): plan → write → film → publish → comment blocks → Friday review |

## 11. Weekly SOP (Klaus, TITAN.AI page, one clinic director)

**Monday (90 min), plan:**
- Read last week's tracker.
- Pick 4 Klaus posts, 3 page posts and 2 clinic posts from the pillars.
- Run `/story` for drafts. Clinic drafts go through compliance first.
- Refresh the comment target lists.

**Tuesday, film and write (2.5 h):**
- Klaus films 4–6 vertical clips.
- Newsletter in alternate weeks.
- Clinic director: one 60–90 s educational video or carousel.

**Klaus rhythm (SGT)** — never post without 60 minutes free afterwards. Test 4–6 pm SGT for UK reach.

| Day | Format | Pillar |
|---|---|---|
| Tue 8:30 | Text + authentic photo | founder story |
| Wed 8:30 | Document carousel | AI-for-SME framework |
| Thu 12:30 | Vertical video | how-to or teardown |
| Fri 8:30 | Text | contrarian or market POV |
| Alternate Sat | Newsletter | deep dive → lead magnet |

**TITAN.AI page:**
- Mon: proof or case (permissioned).
- Wed: reshare Klaus's carousel with company commentary, or a team behind-the-scenes post.
- Fri: event, webinar or hiring.

**Clinic director:**
- Tue: education (carousel or video).
- Thu: leadership, operations or industry.
- Daily comment block.
- Quarterly profile compliance check.

**Daily (all three), 2 × 15–20 min:**
- Substantive comments on target accounts.
- Reply to own comments.
- Screen connection requests.
- Klaus: 10–20 hand-written ICP requests and 3–5 warm DMs.

**Friday (45 min), review:**
- Update the tracker; note the top and weakest post per person and why.
- Pick the TLA candidate (Klaus approves spend).
- `/review` → `/learn`.
- Monthly: refresh comment lists, retire tired formats, refresh TLA creative.

**Never:** pods, auto-commenters, non-API schedulers, AI-written comments, "comment YES", editing in links, patient testimonials, recommendations or reviews in any form.
