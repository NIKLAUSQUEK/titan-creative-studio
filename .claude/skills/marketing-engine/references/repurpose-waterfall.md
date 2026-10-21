# Repurpose waterfall: one hero piece → many derivatives

Klaus's own system lives in Drive: **"Secret content creator waterfall system"**. If it conflicts with this file, his version wins (it is his brief); read it via Google Drive when available and note differences here.
Principle: record once, cut many, re-hook every derivative. A derivative is a new hook on the same truth, never a lazy crop. Never change what the speaker meant (clipping-podcast.md).

## 1. Hero sources
| Hero | Typical yield (rule of thumb, not a benchmark) |
|---|---|
| Podcast / long talking-head (30-60 min) | 6-10 shorts, 2 carousels, 5 quote cards, 1 newsletter, 1 blog/LinkedIn article, 3-5 X/Threads posts, YouTube long + chapters |
| YouTube explainer (8-15 min) | 3-5 shorts, 1 carousel, 1 newsletter, 1 LinkedIn post, 1 blog |
| Story card (`brain/stories/STORY-###`) | 1 short, 1 long-form story post, 1 carousel, 2-3 quote cards, 1 newsletter essay |
| Studio ad / skit (finished cut) | cut-downs 6/15/30 s, 1:1 + 4:5 + 16:9 reframes, BTS short, "how we made it" (TITAN.AI) |

## 2. Derivative specs
Specs change; verify in-app before posting. Sources: platform help/creator pages (TikTok, Instagram, YouTube Help, LinkedIn Help); items marked RoT are rules of thumb.

| Derivative | Aspect / px | Length | Hook position | Caption / text length | Text-safe zone (RoT) |
|---|---|---|---|---|---|
| TikTok video | 9:16, 1080x1920 | 15-60 s sweet spot RoT (platform allows much longer) | first 1-2 s, spoken + on-screen | caption max 4,000 chars; use 1-3 lines | keep text out of bottom ~20% and right ~15% (UI); centre band 15-75% height |
| IG Reel | 9:16, 1080x1920 (grid preview crops to 3:4) | up to 3 min; 15-45 s RoT | first 1-2 s | caption max 2,200 chars; first ~125 chars show before "more" (RoT) | same as TikTok; keep key text inside centre 3:4 for grid |
| YouTube Short | 9:16 (square also accepted) | up to 3 min; ≤60 s RoT for loops | first 1 s | title ≤100 chars; add #Shorts optional | bottom ~25% has title/channel UI |
| YouTube long | 16:9, 1920x1080 (4K ok) | per topic; 8-15 min explainer RoT | first 15-30 s state the promise | title ≤100 chars (~60 visible RoT); description ≤5,000 chars | thumbnail 1280x720, ≤2 MB; bottom-right timestamp covers ~corner |
| IG carousel | 4:5, 1080x1350 (or 3:4 1080x1440) | up to 20 slides; 7-10 RoT | slide 1 (≤8 words, playbook-carousel.md) | 2,200 chars | 80 px margins (playbook-carousel.md) |
| LinkedIn document (PDF carousel) | 4:5 or 1:1 | 6-12 pages RoT | page 1 | post ≤3,000 chars; first ~2-3 lines visible before "see more" | 60 px margins RoT |
| LinkedIn native video | 1:1, 4:5 or 16:9 | 30-90 s RoT | first 2 s + burned captions (sound-off) | ≤3,000 chars | - |
| IG / FB Stories | 9:16 | ≤60 s per frame | first frame | stickers: poll/question/link | top ~14% and bottom ~20% UI (RoT) |
| Facebook Reel / feed video | 9:16 Reels; 4:5 feed | 15-60 s RoT | first 2 s | short; 1-3 lines | as Reels |
| X post | 16:9 or 1:1 media | video ≤2:20 standard accounts | line 1 | 280 chars (standard accounts) | - |
| Threads post | 4:5 / 1:1 media | ≤5 min video | line 1 | 500 chars | - |
| Quote card | 4:5 (IG/LinkedIn), 1:1 (X) | 1 wisdom line | the line itself | ≤20 words on card RoT | 80 px margins |
| Newsletter | email, 600 px wide body RoT | 400-900 words RoT | subject + preheader | subject ≤50 chars RoT | - |
| Blog / article | web | 1,200-2,000 words for search RoT | H1 + first paragraph answers the query | meta description ~155 chars RoT | - |
| Podcast audio | audio (RSS) | full episode | first 60 s cold open | show notes + chapters | - |

## 3. Ordered checklist (per hero piece)
```
[ ] 0  Compliance pre-scan of the hero transcript (compliance-sg.md): flag testimonial-like lines, superlatives, unsourced claims
[ ] 1  Transcript with word timestamps (clipping-podcast.md §6, or Riverside / transcribe-so)
[ ] 2  Moment-finder: 8-12 candidates → rerank → best 6 (clipping-podcast.md §2 prompt); log in projects/<p>/clips.json
[ ] 3  Pick the HERO packaging first: YouTube title + thumbnail (distribution.md §YouTube) - derivatives point back to it
[ ] 4  Shorts: per clip write 3 hooks (story-engine.md §3), cut, reframe 9:16, captions, -14 LUFS, qc_frames.py
[ ] 5  Carousel: lessons → slides (playbook-carousel.md); imagery without text, type set in template
[ ] 6  Quote cards: 3-5 wisdom lines verbatim (Klaus's words only)
[ ] 7  Long text: LinkedIn post / article + newsletter (distribution.md formats); blog if search intent exists (vidIQ keyword / marketing:seo-audit)
[ ] 8  Short text: 3-5 X/Threads posts from the sharpest lines
[ ] 9  Stories: 1 poll/question frame per derivative day to drive replies
[ ] 10 /publish each derivative → package + checklist; slot into marketing/calendar/<yyyy-mm>.md (stagger, §4)
[ ] 11 Tag every derivative with hero_id so /review can attribute results back to the hero
```

## 4. Staggering (rule of thumb)
Day 0 hero (YouTube/podcast) → D1 best short + LinkedIn post → D2 carousel → D3 short #2 + quote card → D5 newsletter → D7+ remaining shorts 2-3/week. Re-test the best clip with a new hook 3-6 weeks later.

## 5. Running it with the studio
| Need | Route |
|---|---|
| Cut clips from podcast/long video | clipping-podcast.md (local faster-whisper + ffmpeg, Riverside Magic Clips, or Higgsfield Katana) |
| Rewrite hooks / long text from the hero | `/story` (story-writer) with goal + the hero transcript as source |
| B-roll / cutaways / reframes needing generation | `/brief` → `/plan` → `/draft` (lowest quality) → `/qc` → `/final` |
| Carousel / quote card imagery | playbook-carousel.md; photo-effects.md; `higgsfield-product-photoshoot` for product slides |
| Thumbnail | `higgsfield-youtube-thumbnail` → vidIQ `vidiq_score_thumbnail` |
| Captions / titles / hashtags per platform | `/publish` (distributor agent) |
| Dub/localise | Higgsfield `dubbing` or Riverside; localisation.md pack; real local VO preferred for Singlish |
Spend no credits on a derivative that can be cut from existing footage.
