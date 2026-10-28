# Genre research: §37 Lead magnet / comment-to-DM (2026-10-28)

**Why this file exists.** Klaus: our genre cards "do not reflect how lead magnets and other creators structure their videos and pace", "the logical consistency and storytelling needs examples", and the explanations are "a bit convoluted". So this file measures real comment-to-DM reels and writes the result in short, plain sentences. The card built from it is §37 in `.claude/skills/higgsfield-creative-director/references/genre-playbooks.md`; the editor preset is `tools/editor/presets/lead-magnet.json`.

**A lead magnet reel** = a short video whose job is to make people comment a keyword, DM, save or tap a link to get a free thing (a guide, map, checklist, template, prompt).

## How I measured
- Found reels with web search (Firecrawl, `site:instagram.com/reel "comment …"`), picking ones with high comment counts.
- Downloaded public Instagram reels only (no login, no cookies). Instagram rate-limited us often; I waited and retried once, then moved on.
- `editor.py study` measured cut times, shot lengths, loudness and made 1-frame-per-second sheets (in `research/style-studies/leadmagnet-ai/`, `leadmagnet-travel/`, `leadmagnet-health-biz/`, `leadmagnet-mixed/`). I looked at every sheet.
- A second pass (faster-whisper, English forced) gave the word timings: when the first word starts, when the keyword and the word "comment" are said, and words per minute.
- Likes and comments are what Instagram returned on 2026-10-28. No view counts were available.
- **"C/L" = comments ÷ likes.** It is our best signal for "did people comment the keyword". Caveat: when the creator's auto-DM tool also replies publicly, the comment count can include those replies, so treat C/L as a ranking signal, not an exact number.

## The examples (14 measured)
| # | Reel | Account | Likes | Comments | C/L | Length s | Median shot s | wpm | First word s | Value starts s | Spoken CTA at | CTA on screen | Keyword said |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 | [PROMPT: prompts.chat](https://www.instagram.com/reel/Dc6IUUVvmUE/) | @nick_saraev | 6,993 | 12,717 | **1.82** | 28.6 | 2.1 | 246 | 0.0 | 4.4 (names it) | 24.7 (86 %) | keyword in quotes, teal highlight, last 3 s | 1× as CTA (+ "prompt" is the topic word in the hook) |
| L2 | [PROMPT: "Pinterest for AI prompts"](https://www.instagram.com/reel/DbLpxfKPKoN/) | @nick_saraev | 4,632 | 5,955 | **1.29** | 28.1 | 1.6 | 230 | 0.0 | 3.0 | 24.8 (88 %) | same | 1× as CTA (topic word 1× earlier) |
| L3 | [MAP: "my treasure map"](https://www.instagram.com/reel/DGixNzBx9lm/) | @lexielimitless | 10,900 | 12,656 | **1.16** | 16.7 | 0.7 | 201 | 0.0 | 2.0 (map on screen) | 10.8 (65 %) | word-by-word captions incl. "Comment map" over the map | 3× ("treasure map" in the hook, CTA, payoff) |
| L4 | [BUILD: ManyChat template](https://www.instagram.com/reel/DV8k1RDD06K/) | @nick_saraev | 1,927 | 2,033 | **1.06** | 33.2 | 2.5 | 231 | 0.0 | 5.2 | 29.0 (87 %) | keyword in quotes, last 3 s | 1× |
| L5 | [GUIDE: "never been easier to make money"](https://www.instagram.com/reel/DWJikSmyVQg/) | @maria.wendt | 251 | 505 | **2.01** | 14.6 | one take | 0 (silent, text only) | n/a | 0 (text block) | none (caption only) | no | 0 |
| L6 | [FIX IT: 10 posture exercises](https://www.instagram.com/reel/C8rvB2vsJvt/) | @jennlashley_ | 101 | 159 | **1.57** | 61.7 | 11.8 (selfie, few cuts) | 250 | 0.0 | 22.9 (the "what I wish I knew" list) | 53.9 (87 %) "link in profile" | red card "Comment FIX IT and I'll send it to you" + guide thumbnail from ~42 s (68 %) to the end | 0 spoken, on screen 20 s |
| L7 | [LAMP: follow automation](https://www.instagram.com/reel/DTvM3ZvDegP/) | @devinjatho | 5,628 | 2,350 | 0.42 | 79.7 | 1.7 | 217 | 0.0 | 6.0 | **28.9 (36 %)**, then keeps teaching | a fake comment box with "LAMP" typed in | 1× |
| L8 | [MAP: Madeira 100+ spots](https://www.instagram.com/reel/Dc_kH6Phgwz/) | @molly.and.mike | 1,354 | 502 | 0.37 | 20.1 | 1.0 | 0 (music only) | n/a | 3 (place names) | none (caption only) | no | 0 |
| L9 | [GUIDE: Ireland map](https://www.instagram.com/reel/Db3t0t5RJsk/) | @explorewithcriostoir | 1,109 | 396 | 0.36 | 28.9 | 1.3 | 219 | 0.0 | ~17 (map on screen) | none (caption only) | no | 0 ("guide" said once, no ask) |
| L10 | [MANYCHAT (sponsored)](https://www.instagram.com/reel/DQtSCx1lR0s/) | @aliabdaal | 610 | 126 | 0.21 | 87.4 | 4.0 | 263 | 0.0 | 8.1 | 40.5 (46 %) and 82.9 (95 %) | no | 2× |
| L11 | [PROMPT: reverse prompting](https://www.instagram.com/reel/DVhQkseDnOd/) | @chriswinfield | 4,444 | 240 | 0.05 | 138.4 | 6.0 | 197 | 0.0 | 25.9 | **none**; ends "Save this right now" | no | 0 as an ask |
| L12 | [PAIN: shoulder routine](https://www.instagram.com/reel/DHQrSmGtJxy/) | @sunaina_rekhi | 2,997 | 122 | 0.04 | 59.3 | one take | 132 | 0.0 | 14.7 (the move) | none (caption only) | no | 0 |
| L13 | [MAP: West Coast road trip, 9 stops](https://www.instagram.com/reel/DSSdzvmiGj_/) | @vh_travelwithme | 53,984 | 1,381 | 0.03 | 25.7 | 0.6 | 0 (music) | n/a | 0 (route on a globe) | none (caption only) | no | 0 |
| L14 | [MOBILE: posture flow](https://www.instagram.com/reel/DRs7PU5D3fl/) | @flolyfe | 1,164 | 25 | 0.02 | 19.0 | 2.6 | 264 | 0.0 | 4.9 | none; CTA buried mid-caption | no | 0 |

Not measured (rate-limited or empty media): @willharlowphysio ROADMAP (1,957 likes, [link](https://www.instagram.com/reel/DeSGn32TWC1/)), @golf_physio_aus MOBILITY, a few travel MAP reels. Their captions show the same "Comment WORD and I'll send you…" line.

## What the numbers say (plain words)
1. **Say the ask out loud AND put it on screen.** Every reel where comments matched or beat likes (L1-L4, L6) asked out loud or showed a big "Comment WORD" card. Every reel that only asked in the caption got 3-37 comments per 100 likes (L8, L9, L12-L14). The ask is the difference between 0.03 and 1.8.
2. **The keyword is the thing's own name.** MAP for a map, PROMPT for prompts, FIX IT for a posture fix. It is often already in the hook ("this is my treasure map"), so by the time you hear "comment map" it feels obvious, not salesy.
3. **First word at 0.0 s. Always.** All 11 voiced reels start talking on frame 1. No intro, no logo, no "hey guys".
4. **The hook names the thing and gives one reason to believe it in one breath (2-4 s).** "After traveling to every country in the world, this is my treasure map." "Someone just built the world's biggest prompt library and made it free." "I gained 400,000 followers in 12 months and this one tool was behind most of it."
5. **The value starts by 3-6 s.** "It's called …" lands at 3-5 s in the best ones. When the map or tool only appears at 17-26 s (L9, L11), C/L drops.
6. **Middle = 3 quick proofs, not a lecture.** Show the thing doing its job: a number (10,000+ prompts, 150+ spots), 3 categories ("writing, coding, images"), one screen of it working. A new screen every ~1.5-2.5 s.
7. **The ask comes at the end of short reels (86-88 % of the runtime).** Under 35 s: the last 3-5 s. On 60 s+ reels, ask once early (L7 at 36 %: "First, I'm gonna let you steal it. Comment LAMP") or put the card up from ~2/3 (L6), then keep teaching.
8. **The ask is one sentence with a reason:** "So if you want the link, just comment PROMPT down below and I'll send it to you directly." Reason ("if you want …") → keyword → promise ("I'll send it").
9. **Pace:** about 200-250 words a minute (fast, but natural). Median shot 1.5-2.5 s for talking head + screens; 0.6-1.3 s for travel montages; a single selfie take also works if the face and words carry it (L5, L6).
10. **Short wins for this job.** The 4 best C/L reels with a spoken ask are 17-33 s long. The two long ones (80-138 s) get likes but fewer comments.
11. **Loudness** is always about -14 LUFS (normal for Reels).
12. **Silent text reels can work** when the text makes a big, desirable claim (L5: 2.0 C/L). But that format runs on income-style claims, which our brands cannot make; treat it as a variant, not the default.

## What we keep, what we drop
- **Keep:** first word at 0 s; thing named in the hook; keyword = the thing's name; 3 proofs on screen; spoken + on-screen ask in the last 3-5 s; caption line 1 = the ask, word for word.
- **Drop:** long intros ("Hi I'm…" before the hook; L3 only gets away with it because the hook already came first), CTA buried in the caption, "save this" as the only ask, 2-minute tutorials when the goal is comments.
- **Compliance flags seen in the wild:** "your shoulder pain is gone" (L12) and "best exercises" (L6) are outcome promises / superlatives: banned for SG health brands. Income claims (L5) are not allowed for our brands either.

## Sources
- The 14 reels above (links in the table); downloads and sheets in `research/style-studies/leadmagnet-*` (videos are git-ignored, study only, never cut into edits).
- Search results that surfaced them: Firecrawl web search, 2026-10-28 (queries `site:instagram.com/reel "comment GUIDE"`, `"comment PROMPT"`, `"comment" "I'll send you" map`, physio/mobility "free program").
