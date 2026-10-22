---
name: marketing-engine
description: Marketing layer for ANY brand or business (active brand in .studio/active_brand; onboard new ones with /onboard) - content strategy, positioning, content pillars, content calendar / posting plan ("what should I post"), repurposing waterfall (one hero piece → many derivatives), distribution and platform packaging (captions, hashtags, titles, descriptions, chapters, thumbnails, alt text), YouTube SEO, growth, funnel, launch/campaign planning, lead gen, newsletter, and weekly/monthly analytics reviews that write learnings to the ledger. Use for any brand (Klaus's own: Physio Spot, heal360, Power Protein, PeachForm, TITAN.AI, personal; plus any client) on TikTok, IG, YouTube, LinkedIn, Facebook, X/Threads, newsletter/blog or podcast.
---

# Marketing Engine

The loop that turns a brand's (and its people's) identity into reach, leads and learnings, for any business. Brand facts: `brands/<brand>.md`; voice: brand §5 + `brains/<who>/`; rules: its compliance pack. Creator Brain says **who** and **why**; the studio makes the **thing**; this skill decides **what, where, when**, packages it, and measures it.

```
Creator Brain (brains/<who>/)  →  Strategy (marketing/strategy/<brand>.md)  →  Calendar (marketing/calendar/<yyyy-mm>.md)
      ↑                                                                         ↓
ledger/learnings.md  ←  Review (marketing/reviews/)  ←  Distribute (/publish)  ←  Studio (/story, /ad, /brief → /draft → /final, /repurpose)
```

## Files
- `references/content-strategy.md` - positioning per brand, segments + pains, pillars, funnel + format mix, hero/hub/help cadence, calendar templates, series, founder vs brand split.
- `references/repurpose-waterfall.md` - one hero piece → derivatives per platform, exact specs, ordered checklist, studio hand-offs.
- `references/distribution.md` - per-platform playbook, caption formulas, YouTube SEO, LinkedIn/newsletter formats, posting + comment-reply checklists, cross-posting.
- `references/analytics-loop.md` - metrics per platform → what they diagnose, how to pull them, decision rules, review template, ledger write-back.
- `references/compliance-packs.md` - universal rules + industry packs (health, supplements, fitness, beauty, finance, alcohol/gambling, F&B, property, education, legal, dating, recruitment) × market table (SG, MY, ID/VN/TH, PH, AU, UK, EU, US, IN, NG). Every brand names its pack.
- `references/compliance-sg.md` - deep-dive SG health-ad checklist + platform policy hot spots for sexual-health content.
- Outputs: `marketing/strategy/`, `marketing/calendar/`, `marketing/reviews/` (see `marketing/README.md`).

## Routing
| Klaus says | Do |
|---|---|
| "strategy / pillars / positioning / who is this for" | `/strategy <brand>` → strategist agent → `marketing/strategy/<brand>.md` |
| "content calendar / what should I post this week/month" | `/calendar <yyyy-mm> [brands] [capacity]` → strategist agent |
| "write the post / hook / script for slot X" | `/story` (story-writer) - the calendar slot is the brief |
| "make the video / carousel / ad for slot X" | `/ad` or `/brief` → `/plan` → `/draft` → `/qc` → `/final` (studio gates unchanged) |
| "repurpose this / waterfall this / cut this podcast" | `/repurpose <hero piece>` → repurpose-waterfall.md (+ clipping-podcast.md) |
| "package this for posting / captions / titles / hashtags / thumbnail" | `/publish <asset>` → distributor agent (never posts) |
| "how did it perform / weekly review / what's working" | `/review [week|month] [brand]` → analytics-loop.md → `/learn` |
| "launch / campaign" | `marketing:campaign-plan` skill + strategist agent; production via `/ad` |
| "paid ads / boost / Meta / Google / TikTok ads" | `anthropic-skills:ads-*` skills (ads-plan, ads-meta, ads-google, ads-tiktok, ads-youtube, ads-linkedin, ads-creative, ads-audit) + compliance-sg.md |
| "SEO / blog / website content" | `marketing:seo-audit`, `marketing:content-creation` |
| "email sequence / newsletter / nurture" | `marketing:email-sequence` + distribution.md §Newsletter |
| "competitors / what are others doing" | `marketing:competitive-brief`; vidIQ `vidiq_outliers`, `vidiq_similar_channels`, `vidiq_instagram_tiktok_outlier_search` |
| "performance report for <client>" | `marketing:performance-report` with analytics-loop.md metrics |
| "thumbnail" | `higgsfield-youtube-thumbnail` skill → vidIQ `vidiq_score_thumbnail` |
| "product shots / brand kit" | `higgsfield-product-photoshoot`, `higgsfield-brandkit` |

## Rules
1. **Precedence** is CLAUDE.md's: ledger > brand file + `brains/<who>/identity/profile.md` > Klaus's brief > preset > defaults. Strategy docs sit at "Klaus's brief" level once he approves them.
2. **Voice:** read `brains/<who>/identity/profile.md` before writing any copy. Use his confirmed lines verbatim; `[draft]` lines need his yes before going public. Founder-led copy sounds like him, not like a brand.
3. **Compliance before polish:** every clinic/health piece (Physio Spot, heal360, health claims anywhere) passes `references/compliance-sg.md`. No testimonials, paid reviews, superlatives, free-consult/discount inducements, unproven medical claims; dramatised skits never pose as patient testimony.
4. **Every claim sourced:** a stat or medical fact carries a source in the doc or the project's `SOURCES.md`. No source → cut it or say "rule of thumb". Never invent numbers, benchmarks or quotes.
5. **Cheap first:** plans, scripts and stills before video; drafts at lowest quality → Klaus approves → final (credit-saving.md). Repurpose before you re-generate.
6. **Never post, schedule, reply or spend on Klaus's behalf** without his explicit go for that item. `/publish` produces a package + checklist; Klaus (or a scheduler he approves) posts.
7. **vidIQ budget:** state the call, its credit cost and the week's remaining credits before any vidIQ call (ledger 2026-10-11 rule).
8. **Close the loop:** every review ends with 1-3 testable rules via `/learn`; strategy/calendar read the ledger first.
9. Brand facts marked CONFIRM in `brands/*.md` stay CONFIRM - ask once, don't guess. PeachForm has no brand file yet: ask Klaus what it is before planning for it.
