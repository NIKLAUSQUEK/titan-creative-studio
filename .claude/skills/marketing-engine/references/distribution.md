# Distribution playbook

Specs table lives in `repurpose-waterfall.md` §2 (verify in-app; specs change). Every package passes `compliance-sg.md` first for health brands. Klaus posts; we package.

## 1. Universal caption formula
```
Line 1  HOOK (restates the video's curiosity gap in different words; ≤ 12 words)
Line 2-4 VALUE (the one idea, or the story turn in one line)
Line 5  WISDOM / TAKEAWAY (Klaus's verbatim line where possible)
Line 6  CTA (one action matched to funnel stage: follow / save / comment <word> / read / WhatsApp)
Line 7  keywords / hashtags (per platform rules below)
```
Write in Klaus's voice (`brain/identity/profile.md`). One CTA only. Health brands: CTA is a neutral next step ("WhatsApp us to book an assessment"), never a free/discount offer.

## 2. Per-platform playbook
### TikTok
- Structure: hook 0-2 s (spoken + text), payoff by ~60%, loop-able ending or open loop to part 2.
- Caption: 1-3 lines, keyword-rich (TikTok search reads captions, on-screen text and speech - RoT). 3-5 hashtags: 1-2 niche (#pelvichealth), 1 topic, 1 brand/series.
- Sound: licensed only on brand accounts (`/sound`); trending meme sounds personal accounts only, added in-app (ledger).
- Pin a comment that adds context or a source.

### Instagram (Reels, carousels, Stories)
- Reels: as TikTok; cover frame designed for the 3:4 grid crop. Caption keyword-first (IG search indexes captions - RoT). Hashtags: 3-5 relevant (Instagram has repeatedly advised few, relevant hashtags; verify the current cap in-app).
- Carousels: playbook-carousel.md; last slide = save/share prompt + CTA; caption repeats slide 1 hook in other words. Add alt text per image (accessibility + context).
- Stories: daily lightweight - poll, question box, BTS, link sticker to the week's hero. Use answers as content ideas.
- Collab posts with brand account when founder content features the clinic.

### YouTube long
- **Title:** ≤60 visible chars RoT, keyword near front, a curiosity gap that the video truthfully pays off. Generate 5-10 → vidIQ `vidiq_generate_titles` / `vidiq_score_title` → pick 1, keep 2 for A/B (YouTube "Test & Compare" if available on the channel).
- **Thumbnail:** `higgsfield-youtube-thumbnail` skill (truthful information gap, ≤3 words, face + one object) → vidIQ `vidiq_score_thumbnail`. Title and thumbnail say different things that add up.
- **Description:** first 2 lines = what they'll learn + primary keyword (shows in search); then summary, chapters, sources (for any stat), links, disclaimer for health ("Educational only, not medical advice; see a registered professional"). Hashtags: up to 3 RoT (YouTube ignores all hashtags on a video if there are more than 60 - YouTube Help).
- **Chapters:** first timestamp 0:00, at least 3, each ≥10 s (YouTube Help). Draft with vidIQ `vidiq_generate_video_chapters` or from the transcript.
- **Keywords:** vidIQ `vidiq_keyword_research` for the topic; pick one primary + 2-3 secondary; use naturally in title, description, spoken in the first 30 s.
- End screen → next video in the series; pinned comment with a question.
### YouTube Shorts
- Title = hook text; link to the related long video (Shorts "related video" link). Same compliance.

### LinkedIn (personal first, company page second)
```
Line 1-2  hook (visible before "see more"): a specific moment or a contrarian line
blank line
Short paragraphs (1-2 sentences), 150-300 words RoT
The turn → the lesson → one practical takeaway
Question to the reader (invites comments that are about them, not us)
0-3 hashtags; links in first comment only if reach data says so (test it, don't assume)
```
- Formats: story post, PDF carousel, native video with burned captions, "clinic notes" (de-identified, never a testimonial).
- Reply to every comment in the first hour Klaus can manage (RoT).

### Facebook
- Reels cross-post from IG (Meta Business Suite) + 4:5 feed video for older/local audiences. Groups: answer questions as Klaus, no link-dropping.

### X / Threads
- One idea per post; thread = hook post + 3-6 posts + recap + link. Pull lines from the hero transcript. Threads: conversational, 500 chars.

### Newsletter / blog
```
Subject ≤50 chars RoT (curiosity or specific benefit)  |  Preheader completes the subject
Opening scene or question (2-3 lines)
The story / insight (Creator Brain card)
What to do with it (3 bullets max)
One link to the hero piece  |  One CTA (reply / book / forward)
P.S. personal line or next week's tease
Footer: unsubscribe + sender identity (PDPA / Spam Control Act - compliance-sg.md)
```
Sequences → `marketing:email-sequence`. Blog/SEO → `marketing:seo-audit` + `marketing:content-creation`; each article answers one search query in the first paragraph.

### Podcast
- Title = guest/topic + promise; show notes with chapters, sources, links; cut clips via repurpose-waterfall.md. Guest consent for clips and any "correct speech" edit (clipping-podcast.md).

## 3. Hashtags / keywords method
1. Primary keyword from vidIQ `vidiq_keyword_research` or platform search autocomplete.
2. Say it in the first 3 s, show it on screen, put it in caption line 1.
3. Hashtags = topic + niche + series/brand; no banned/irrelevant tags; no trend-hijacking unrelated tags.

## 4. Package template (what `/publish` outputs)
Saved to `projects/<p>/PUBLISH.md` (or `marketing/calendar/<yyyy-mm>/<slot>.md` for non-project posts).
```
## <platform> - <slot id> - <brand/account> - hero_id: <id>
Asset: <path> (aspect, duration, QC contact sheet checked: y/n)
Hook (on-screen): ...           Title (YT): ... [vidIQ score: ...]
Caption: ...
Hashtags/keywords: ...
Thumbnail/cover brief: ...       Alt text: ...
CTA + link destination: ...
Compliance: PASS / FIX (items)  Sources: SOURCES.md lines
Post window: <day, SGT time from the account's own analytics>
Checklist: see §5
```

## 5. Posting checklist
```
[ ] Compliance-sg PASS (health brands) and platform policy check (compliance-sg.md §3)
[ ] Right account (founder vs brand), right aspect, captions burned for sound-off, -14 LUFS
[ ] Text inside safe zones on a phone preview; cover/thumbnail legible at small size
[ ] Caption: hook line, one CTA, keywords, hashtags per platform; links work (UTM: ?utm_source=<platform>&utm_medium=social&utm_campaign=<slot>)
[ ] Alt text / subtitles file uploaded where supported
[ ] Music licence status recorded (brand = licensed/CC0)
[ ] Disclosures: paid partnership / AI-generated label where the platform requires it
[ ] Post time from account analytics (not a generic "best time")
[ ] First-hour plan: pinned comment, who replies, Stories share
[ ] Log the post URL + hero_id in the calendar row (for /review)
```

## 6. Comments / community reply playbook
- Pull: vidIQ `vidiq_video_comments` + `vidiq_comment_insights` (YouTube); native inbox elsewhere. Draft replies with `vidiq_generate_comment_replies`; **Klaus approves before anything is posted** (`vidiq_reply_to_comment` only on his go).
- Reply types: thank + add one fact; answer the question in public (general info only); turn great questions into the next video ("reply with video" on TikTok/IG).
- Health: never diagnose or give individual advice in comments; "Everyone's case differs - a registered physio can assess you." Move personal details to DM/WhatsApp; don't ask people to post symptoms publicly.
- Never reply to a comment that praises the clinic's treatment results by amplifying it (pinning/resharing = testimonial use).
- Trolls: one calm factual reply or none; hide/delete spam, slurs, health misinformation; never argue.
- Log recurring questions + pains to `marketing/reviews/` → they feed pillars and the calendar.

## 7. Cross-posting rules
- Same video can go to TikTok, Reels, Shorts, FB Reels; export clean files without another platform's watermark (Instagram has said it de-prioritises recycled watermarked content - Instagram/@mosseri statements; verify current guidance).
- Re-write caption, hook text and hashtags per platform; change the cover.
- Stagger by hours/days, not the same minute, so you can learn which platform leads.
- LinkedIn and newsletter get rewritten text, not pasted captions.
- Brand vs founder: don't post the same asset from both accounts the same day; use Collab/reshare instead.
