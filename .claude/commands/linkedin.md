LinkedIn operating mode for the active brand or person. Rules are in `.claude/skills/marketing-engine/references/linkedin-playbook.md`; read it first. Argument is one of the following:

- `post <topic>`
- `carousel <topic>`
- `video <footage or topic>`
- `newsletter <topic>`
- `profile`
- `week`
- `comments`
- `ads`
- `review`

**Clinic directors:** every output passes playbook §8 and `compliance-sg.md` before Klaus sees it.

1. **post**
   1. Run `python scripts/styles.py offer --brand <b> --platform linkedin --goal "<topic>"`.
   2. Klaus picks a format (or you recommend one).
   3. The story-writer drafts version A from that template plus the matching script style, using the active brain's real story/data (AI edits only, never invents).
   4. Deliver:
      - a hook of 140 characters or less over 2 lines
      - 700–900 characters (stories 150–250 words)
      - one CTA
      - a first comment (source/context)
      - 0–3 hashtags
      - an image brief (authentic photo, or a cards-engine graphic that matches the text)
2. **carousel**
   1. Pick an archetype (`styles.py find --family carousel "<topic>"`).
   2. Write 6–12 cards to `projects/<p>/carousel.json` (card types: title, stat, list, steps, quote, compare, definition, myth_fact, chart, cta). Every stat/chart needs a `source`.
   3. Run `python tools/editor/editor.py cards projects/<p>/carousel.json --aspect 4:5 --brand <b>`.
   4. LOOK at `contact_sheet.jpg`.
   5. Deliver `slides.pdf`, a document title and the post text.
3. **video**
   - Footage: `/edit` with preset `linkedin-founder-video` (9:16 or 4:5, auto panel boards, low bed).
   - Topic only: write a 30–75 s script first (promise in sentence 1 = caption line 1).
   - Get a cover brief.
4. **newsletter**
   - Search-friendly title, story intro, 3–5 sections, takeaway box, lead-magnet CTA (PDPA consent).
   - Cut 3 posts and 1 carousel out of it.
5. **profile**
   - Audit against the platform-signals profile spec and playbook §5:
     - headline
     - banner with one CTA
     - About
     - Featured: newsletter + lead magnet + best post
     - Follow button
     - Services
   - Clinic: hide recommendations; no superlatives.
6. **week**
   - Build next week's plan from playbook §11 (Klaus 4 posts + newsletter in alternate weeks, page 3, clinic director 2) using the strategy pillars and last week's tracker.
   - Write it to `marketing/calendar/linkedin-<yyyy>-W<ww>.md`.
7. **comments**
   - Build or refresh the 30–50 account target list per person (`manifold:find-linkedin-posts-to-comment` if available).
   - Suggest today's 5–10 posts to comment on, with a 25–60 word angle for each.
   - Klaus writes and posts every comment himself (never automated or AI-posted).
8. **ads**
   1. Pick the TLA candidate from the tracker (saves + sends + profile views).
   2. Lay out the funnel (TLA → gated Document Ad → Conversation Ad / book a call).
   3. Give the budget and a cost quote.
   4. **Klaus approves spend** (cost gate).
   5. Hand off to `anthropic-skills:ads-linkedin`.
9. **review**
   1. Update the weekly tracker (per-post saves, sends, substantive comments, profile views, followers gained; weekly DMs, calls, pipeline).
   2. Compare the top 3 against the weakest.
   3. Run `/review` → `/learn`.

**Never:** posting or commenting on Klaus's behalf, pods, automation tools, "comment YES" bait, editing a link into a live post, or patient testimonials/recommendations/reviews.
