# Giveaways, contests and "if X happens" prize drops

Klaus, 2026-10-28: "random giveaways, contests, funny caption winners, giving chances to one lucky commenter and reposter of this post should Vietnam win, or if xx player scores, we will give 50 USD, or an iPhone, or a free dinner at a steakhouse… free hotel stays too."
Giveaways feed the "talk of the town" series: they turn a post into something people comment on, repost and send. Use at most 1-2 a month per account, so they stay special and the winners report can tell whether they work (`giveaway` column in posts.csv).

## 1. Formats
| Format | Mechanic | Best for |
|---|---|---|
| **"If Vietnam win" prize drop** | "If Vietnam beat Korea on 15 Jan, one lucky commenter AND one lucky reposter win ___." The draw only happens if the condition comes true. | big matches, finals, "if <player> scores" |
| **Prediction contest** | "Comment the final score. Closest guess wins." A skill element, and the comments explode. | any match |
| **Funny caption contest** | Post a ridiculous Saigon photo or clip: "Best caption wins." Winner chosen by us (skill, not luck). | only-in-Saigon moments, motorbike-load photos |
| **Lucky commenter / reposter** | Comment (and repost or Story-share on IG/TikTok) → random draw. | the monthly hero post |
| **"Tag who you'd take"** (IG/TikTok only) | Comment tagging the person you'd bring → random draw. Both win. | dinners, hotel stays |
| **Photo/UGC contest** | "Post your Saigon shot with #snapsaigon" → we pick the best. | photo spots, festivals |

## 2. Prizes (mix cash, wow and partner prizes)
- Cash: 50 USD / 1-2M VND.
- Wow: an iPhone (headline prize for the biggest moments only).
- Partner prizes, which cost us little and pay the partner in reach: a steakhouse dinner for two, **free hotel stays** (a night or a weekend at a partner hotel), rooftop bar packages, spa days, áo dài rentals.
- Own product: a free Snap Saigon shoot (the best prize for the business: the winner posts the photos and tags us).
Partner prizes are sponsored posts: tag the partner and add the paid-partnership/"Quảng cáo" label (Law 75/2025).

## 3. How to run one (the studio does steps 1, 2, 5, 6)
1. **Hook ladder first** (series §2b): the prize is a rung, not the opener. "If Vietnam win on the 15th, Saigon won't sleep… and neither will one of you, because you're winning a weekend at ___."
2. **Rules** in the caption (short) plus a pinned comment or link (full): who can enter, how, deadline, how and when the winner is picked and announced, prize and how it's delivered, "no purchase necessary", and on Instagram "This promotion is not sponsored or run by Instagram" plus a release of Instagram.
3. **Notify** (Vietnam, luck-based draws): the business notifies the Department of Industry and Trade where it runs at least 3 working days before it starts (Decree 81/2018 as amended by 128/2024 and 239/2026). If a luck prize ends up with no winner, 50% of its announced value goes to the state budget. Skill contests (caption, prediction, best photo) are not luck draws. Confirm the current procedure with a VN lawyer before the first one.
4. **Post and pin** the rules comment; Stories countdown to the deadline.
5. **Draw:** export the comments (and reposters), then `python tools/analytics/pick_winner.py comments.csv --reposters reposters.csv --exclude staff.txt --seed "<post id + draw time>" --out marketing/giveaways/<id>.md`. One entry per person, staff and partners excluded, the seed published so anyone can re-run it.
6. **Announce:** winner video or Story (with their OK), DM them, deliver within the stated time, log the result. The announcement is its own post: it proves the giveaways are real.

## 4. Platform rules that change the mechanic
- **Facebook:** entry can't require sharing, posting on timelines or tagging friends (Meta Promotion Guidelines). On FB use "comment to enter" or the prediction/caption formats; you can still *ask* for shares, just not as an entry condition.
- **Instagram / TikTok:** tag-a-friend and Story-share entries are common; the official rules and the Instagram release are required on IG.
- No "bet / cược / kèo" wording, no odds, no paid entry: it's a free giveaway, not betting (sports betting is restricted in Vietnam).
- SG health brands: no giveaways tied to treatments or results (inducement rule); the formats in this file are for travel, food, lifestyle and media brands.
