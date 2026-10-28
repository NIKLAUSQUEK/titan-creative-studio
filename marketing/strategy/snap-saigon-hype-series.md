# Snap Saigon: monthly "talk of the town" hype series ("SAIGON IS ABOUT TO GO CRAZY") [draft]

Klaus, 2026-10-28: "the saigon travel content should also include festivities, wild expat parties, amazing and big celebrations, historic events that might happen (Vietnam U23 wins final, streets riot…) → do fun trailer and upcoming posts and events and comment tag your friend to get them ready or DM this if they should know why the streets will be crazy… needs a wild, fun, exciting, TOFU, event sharing, interest grabbing post monthly."

Klaus, 2026-10-28 (follow-up): "can be event, can be food, can be whatever gets people talking, sharing and sparking interest."

## 0. Topic radar: anything people will talk about and send to a friend
Each month, pick the ONE topic with the most talk potential. Events are only one lane:
| Lane | Examples | Format twist |
|---|---|---|
| Events & celebrations | festivals, countdowns, Tết, "if Vietnam wins" street nights, expat/rooftop parties | trailer + date cards (§2) |
| Food | a viral dish or stall everyone's queueing for, a new night market, "the 15k vs 1.5M bowl of phở", weird foods tourists dare each other to try, a famous spot closing | "Saigon is about to queue for THIS" / taste-test reaction; the address on the last card |
| New & changing city | a new metro line or station, a new rooftop or mall opening, a street being pedestrianised, an iconic place disappearing | "Saigon in 2016 vs now" / "last chance to see" |
| Only-in-Saigon moments | rainy-season flooding chaos, motorbike moving-day loads, Bui Vien at 3am, the sudden-downpour poncho sea | "POV: your first day in Saigon" / relatable humour (§5, §6) |
| Prices & money | what $10 / 100k VND gets you, tourist vs local price, the cheapest rooftop | stat cards, side-by-side |
| Viral local stories | a stall owner gone viral, a street performer, a wholesome stranger moment (non-political) | repost the creator's clip, credited (`collab add`) |
| Hidden spots | secret cafés in old apartment blocks, hẻm food alleys, sunset spots | "save this" carousel; often a Snap Saigon photo spot |

**Talkability score (pick the highest):** 1 point each for: people will tag or send it to someone · there's a "wait, really?" surprise · it has a date or deadline (urgency) · locals AND tourists care · great real footage exists to repost · it ties to a Snap Saigon photo spot. Score ≥4 = hero; 2-3 = support post.
The trailer format (§2) works for any lane: open on the most surprising real clip, build with cards (dates, prices, addresses), end on the tag/send CTA.

## 1. What the series is
- **Job:** top of funnel. Reach, shares and follows from tourists, expats and young locals. It sells nothing directly; the end card plants "get snapped at it" (snapsaigon.com).
- **Cadence:** one **hero trailer reel** per month (posted ~7-10 days before the month's biggest moment), plus support posts around it (§4).
- **Hooks:** always a hook ladder (§2b), 3-5 versions per post.
- **Promise to the viewer:** "Here's what all of Saigon will be talking about this month, and where to go for it." Every post is a guide (date, place, price) disguised as a movie trailer.
- **Accounts:** Snap Saigon IG/TikTok/FB page (handles: CONFIRM). English-first, with a Vietnamese line on every slide and caption.

## 2. The hero trailer format (20-35 s, 9:16)
Genre grammar: §15 action/sport **anthem** (accelerating cuts) + §28 event promo (dates held ≥2 s) + §31 borrowed cold open (real clips; creators tagged in the caption, never on screen).

| Time | What's on screen | Sound |
|---|---|---|
| 0-2 s | **The wildest real clip from last time**: the streets after a Vietnam win, a Bui Vien Halloween crowd, Nguyen Hue fireworks. Header: "Saigon in 12 days:" | crowd roar up front, no music yet |
| 2-4 s | Black card, trailer type: "THIS NOVEMBER" / "THIS DECEMBER" | sub-boom on the card |
| 4-22 s | 3-5 events, each = 1 hype clip + a **date card** (event · date · place) held ≥2 s. Cuts speed up from ~3.5 s to ~1 s per shot as it builds | trailer drum build, a hit on every date card, riser into the last event |
| 22-28 s | The biggest moment last: "AND IF VIETNAM WINS…" + the craziest street clip, then cut to black | drop to silence 0.5 s → full crowd |
| 28-32 s | CTA card: **"Tag who's coming 👇"** / **"Send this to the friend who doesn't know why the streets will be crazy"** + small "get snapped there → snapsaigon.com" | music out on a hit |

- **Footage: Claude collects the clips.** Each month I search the web for the best public clips (last year's same event, creators' reels and reposts), check them with `editor.py collab scout <urls> --out marketing/collabs/clips-<topic>.csv` and commit the shortlist. Klaus's PC downloads the whole list with `editor.py collab add-list marketing/collabs/clips-<topic>.csv --browser firefox`. **No credit text on screen** (Klaus: it looks ugly); the creator is tagged in the caption. The shortlist names the creator of each clip for the caption tag and the shoutout DM (`collab dm @h --ask shoutout`). Our own snappers film the live moments for the recap (§4).
- **Editor:** `.\Run-Editor.ps1 -Project saigon-hype-<yyyy-mm> -Preset sport-anthem` with the date cards as `stat-counter`/`kinetic-quote` motion cards (`editor.py motion`). Vertical first, then 4:5 for the FB feed.
- **Type:** big condensed caps for date cards (Anton/Bebas), one accent colour per month. Vietnamese line under each card at ≤3/4 size.
- **Sound:** original or licensed trailer drums for the brand account (CLAUDE.md audio rule). Trending audio only in-app on personal/creator accounts. Real crowd and fireworks sound from the clips carries the energy.
- **Captions:** hook line + the event list with dates and places + the CTA twice (start and end) + 3-5 hashtags (#saigon #hochiminhcity #saigonnightlife #vietnam + the event tag). Vietnamese version under the English.

## 2b. The hook ladder (Klaus, 2026-10-28: "see how each links and grabs your attention more and more?")
Never one hook. Write a **ladder**: every line pays off the one before AND opens a bigger loop, so the viewer can't leave between lines. On screen, each rung is a text beat of ~1.5-3 s over a new clip; in the caption, each rung is its own line.

| Rung | Job | Example (Tết) |
|---|---|---|
| 1. Tease | something is coming, no details | "Next week, something is happening in Saigon." |
| 2. Twist | flip the viewer's guess | "Or should I say… happening AWAY from Saigon." |
| 3. Reveal | the surprising picture, exaggerated | "Expect a GHOST TOWN." |
| 4. Why | the human reason | "Millions are fleeing home for the longest break of the year." |
| 5. Stakes | what it means for YOU | "And these are the things that shut down first…" |
| 6. Proof | numbers, facts, hours | "Tan Son Nhat hit 170,000 passengers in ONE day last Tết." |
| 7. Things to note | the useful payoff people save and send | what's closed, what's open, surge prices, best empty-street photo hours |
| 8. End | the CTA that rides the momentum | "Send this to the friend landing in Saigon that week 👀" |

- **Paint and exaggerate the hook** (ghost town, the whole city on motorbikes, "Saigon will lose its mind"). The facts underneath stay true and sourced, so the exaggeration is a picture, not a false claim.
- **Write 3-5 different hook ladders per post** (different rung 1-3 openers) and test them as trial reels (`/expand`), or use the winner and keep the rest for Stories.

## 3. CTAs that make it spread
- **Tag:** "Tag the friend you're dragging to this 👇" / "Tag who's getting you home after 👇"
- **Send (the strongest share signal on IG):** "Send this to the friend who doesn't know why the streets will be crazy on the 15th"
- **Save:** "Save this, it's your Saigon calendar for November"
- **Vietnamese:** "Tag đứa bạn phải đi cùng 👇" / "Gửi cho đứa chưa biết vì sao đường phố sẽ 'bão'"
- Pin a first comment listing the dates again, so tags pile up under it.

## 4. The monthly stack (one hero + support)
| When | Post | Notes |
|---|---|---|
| ~D-10 | **Hero trailer reel** (§2) | Collab-invite the creators whose clips we used |
| ~D-7 | **Carousel "Your Saigon calendar: <month>"** (7-9 slides: one event per slide with date, place, a tip, best photo spot; last slide = save/send CTA) | thumbnail-designer agent, 4:5 |
| D-3 → D-0 | **Stories countdown** with the IG countdown sticker + "who's going?" poll | reminders opt in |
| Night of | **Live Stories** from our snappers on the street | real footage, credit tags |
| D+1 | **Recap reel**: "Saigon last night was INSANE" (best crowd clips, our photos, tagged people) | soft CTA: "Want photos like these at the next one? snapsaigon.com" |

## 5. Event radar (refresh every month; verify dates before posting)
| Date | Event | Why it's wild | Hero? | Source / confidence |
|---|---|---|---|---|
| **Sat 31 Oct 2026** | Halloween on Bui Vien + Nguyen Hue | Thousands of young locals and tourists packed Bui Vien in 2025; Nguyen Hue is the gentler, photo-friendly option | bonus post THIS WEEK (§6 A) | recurring; [Tuoi Tre 2025](https://news.tuoitre.vn/young-locals-foreign-visitors-flock-to-ho-chi-minh-citys-bui-vien-street-for-halloween-celebrations-103251031135715769.htm), [VOV](https://vov.gov.vn/thousands-fill-hcm-citys-backpacker-area-amid-halloween-celebrations-dtnew-1035589) |
| 5-10 Nov | HCMC Fashion Week (SECC) | runways, street style | support | one listing, last updated months ago: [visitsaigon.co](https://visitsaigon.co/saigon/events) (verify) |
| 11 + 15 Nov | Vietnam vs Chinese Taipei / Kyrgyzstan friendlies (Ninh Binh) | watch-party warm-up for the Asian Cup | support | [VietnamNet](https://vietnamnet.vn/en/asian-cup-2027-to-go-ahead-as-vietnam-prepare-for-november-friendlies-2567952.html) |
| 12-15 Nov | HCMC International Food Festival | street-food overload | support | [visitsaigon.co](https://visitsaigon.co/saigon/events) (verify) |
| **20 Nov → 12 Dec** | **10th Vietnam National Games**: opening ceremony 20 Nov, Thong Nhat Stadium | opening show, city-wide sport month | **November hero** | [Wikipedia](https://en.wikipedia.org/wiki/2026_Vietnam_National_Games) (verify the venue) |
| Sat 5 Dec | Miss Charm 2026 final, HCMC | glam, international crowd | support | [Wikipedia](https://en.wikipedia.org/wiki/Miss_Charm_2026) |
| **24 Dec** | Christmas Eve in District 1: crowds at Notre-Dame Cathedral, lights on Nguyen Hue | both are Snap Saigon photo spots | December hero (with NYE) | recurring |
| **31 Dec** | New Year countdown + fireworks (Nguyen Hue / Saigon River) | the year's biggest street party | **December hero** | recurring; 2026 had fireworks at 4 HCMC sites ([DTiNews](https://dtinews.dantri.com.vn/print/20251208193011399.htm)); 2027 plan not announced yet |
| **11, 15, 20 Jan 2027** | **AFC Asian Cup**: Vietnam vs UAE, **vs South Korea**, vs Yemen (Group E) | a win sends Saigon "đi bão": the whole city on motorbikes with flags, like after the AFF Cup win in Aug 2026 | **January hero** | [ESPN draw](https://www.espn.com/soccer/story/_/id/48727844/afc-asian-cup-draw-japan-face-qatar-south-korea-play-vietnam-socceroos-play-iraq), [VietnamNet](https://vietnamnet.vn/en/afc-confirms-asian-cup-2027-schedule-amid-postponement-rumors-2567011.html); kick-off times in VN time to verify |
| early Feb 2027 | Nguyen Hue Tết flower street opens | the most photographed week of the year | February hero | recurring (dates announced in January) |
| **Sat 6 Feb 2027** | **Tết** (Year of the Goat): Tết Eve fireworks, then the city empties | fireworks + the eerie empty-Saigon contrast | **February hero** | [Jungle Boss](https://junglebosstours.com/explorer/tourism-blog/vietnam-tet-2027), [Office Holidays](https://www.officeholidays.com/holidays/vietnam/tet-nguyen-dan) |
| ongoing | Expat parties: rooftop and Thao Dien parties, Bui Vien weekends, festival launches | the "wild expat parties" pillar | slot into any month | venue pages + expat groups (Claude collects) |

No confirmed December 2026 music festival turned up in search (8Wonder Winter ran in Dec 2024 and may return). I check venue pages and event listings around the 20th of each month.

## 6. First posts (drafts): each with 3-5 hook ladders
Clips in every post: real people's footage via `collab add`, creators tagged in the caption only. Each post = pick one ladder (A/B/C…) for the reel; the others become trial-reel variants.

**A. BONUS, this week: Halloween on Bui Vien (post Thu 29 / Fri 30 Oct; Halloween is Sat 31 Oct)**
- Ladder 1: "This Saturday, one street in Saigon stops being normal." → "500 metres. Thousands of people. Zero chill." → "Bui Vien on Halloween." → "Get there before 9 or you're not getting in" → costume/crowd/neon montage → "Want the calmer version? Nguyen Hue." → "Tag who's coming as the worst costume 👇"
- Ladder 2: "Saigon's scariest night isn't about ghosts…" → "it's about finding your friends on Bui Vien." → crowd chaos → tips (meet-up point, go early, keep your phone zipped) → "Send this to the friend who'll get lost first."
- Ladder 3: "POV: you thought Halloween wasn't big in Vietnam." → wall-to-wall crowd clip → "this is Bui Vien last year" → "and it's THIS Saturday" → CTA.
- End card (all): "Our snappers are on Bui Vien Saturday night 📸 snapsaigon.com"

**B. November: National Games opening, 20 Nov, Thong Nhat Stadium (post ~10 Nov)**
- Ladder 1: "In 10 days, Saigon becomes the centre of Vietnamese sport." → "Not one event. 3 WEEKS of it." → opening-ceremony fireworks → "20 Nov, Thong Nhat Stadium" → what else is on (food festival 12-15 Nov, fashion week if verified) → "Send this to the friend who says there's nothing to do in Saigon."
- Ladder 2: "Something is landing in Saigon on 20 November…" → "thousands of athletes, one stadium, one massive opening night" → stakes: traffic around Thong Nhat, where to watch → CTA.
- Ladder 3: "Saigon in November is unfair." → rapid cards: food festival → fashion week → National Games opening → "and Vietnam play twice before the Asian Cup" → "Save this, it's your November."

**C. December: Christmas + New Year countdown (post ~18 Dec)**
- Ladder 1: "Saigon has 2 nights left in 2026 where nobody sleeps." → "Night 1: 24 December." → Notre-Dame crowd → "Night 2: you already know." → NYE fireworks → where to stand, when to arrive, how to get home (Grab surge, walk-out routes) → "Tag who you're kissing at midnight 👀"
- Ladder 2: "Everyone in Saigon will be in the same 2 streets on 31 December." → "here's which side to stand on" → tips → CTA.
- Ladder 3: "Christmas in a country where most people aren't Christian looks like… THIS." → the D1 crowd at the cathedral → lights on Nguyen Hue → countdown teaser → "Save this for 24.12 and 31.12."

**D. January: the Asian Cup and the motorbike streets ("đi bão") (post ~8 Jan)**
The hero is the street celebration itself, not the match: the whole city on motorbikes, flags, horns, people standing on seats, strangers high-fiving, after ANY big Vietnam win (AFF Cup Aug 2026, U23 runs, SEA Games golds). I collect the best clips from all of them (first shortlist: `marketing/collabs/clips-dibao-streets.csv`).
- Ladder 1: "If Vietnam win on 15 January, Saigon will not sleep." → "Not a party. Not a parade." → "the ENTIRE city gets on a motorbike." → wall of flags and horns → "This is called 'đi bão' (going storming)." → the fixtures: 11.01 vs UAE · 15.01 vs SOUTH KOREA · 20.01 vs YEMEN → where to watch (big screens, D1/Thao Dien bars: Claude confirms) → "Send this to the friend who doesn't know why the streets will be crazy on the 15th."
- Ladder 2: "Imagine an entire city honking at the same time." → "it happens every time Vietnam win something big" → montage → "next chance: 15 January vs South Korea" → CTA.
- Ladder 3: "Tourists in Saigon on the 15th have no idea what's about to hit them." → street chaos → "what to do if you're caught in it: stand back, wave a flag, enjoy it" → CTA "Tag the friend landing that week."
- Ladder 4: "Vietnam vs South Korea. The match is in Riyadh. The real show is in Saigon." → crowds → CTA.
- If Vietnam win: the recap reel goes up the next morning, "Saigon last night 🇻🇳".

**E. February: Tết, Saigon becomes a ghost town (post ~28 Jan; Tết is Sat 6 Feb 2027)**
- **Ladder 1 (Klaus's):** "Next week, something is happening in Saigon." → "Or should I say… happening AWAY from Saigon." → "Expect a GHOST TOWN." → "Millions are heading back to their hometowns for the longest holiday of the year." → "And these are the things that shut down first…" → proof + things to note (below) → "Send this to the friend landing in Saigon that week 👀"
- Ladder 2: "Did you know Saigon becomes a ghost town on 6 February?" → empty Nguyen Hue / empty roundabouts at noon → "where did everyone go?" → why → what's closed → "the one week you get Saigon's streets to yourself (best photo week of the year)" → CTA.
- Ladder 3: "Saigon's traffic disappears for one week a year." → before/after of the same intersection → "here's when, why and what to know" → CTA.
- Ladder 4: "Landing in Saigon on 6 February? Read this first." → the stakes list → CTA "Save this."
- **Proof and things to note** (verify all the week we post):
  - Tết (Mùng 1) = Sat 6 Feb 2027. The official public-holiday dates are proposed at about 7 days (e.g. 5-11 Feb); confirm the final Ministry of Home Affairs notice ([CafeF](https://cafef.vn/bo-noi-vu-thong-bao-lich-nghi-tet-nguyen-dan-dinh-mui-2027-188261010092338947.chn), [LSVN](https://lsvn.vn/hai-bo-dong-y-nghi-7-ngay-tet-dinh-mui-4-ngay-van-hoa-a177252.html)).
  - Last Tết, Tan Son Nhat handled 170,000+ passengers in a single day, a record in over a decade ([Tuoi Tre](https://news.tuoitre.vn/highways-congested-as-millions-return-to-ho-chi-minh-city-after-tet-holiday-103260223101257738.htm)); train tickets out of HCMC sold out on the peak days ([DTiNews](https://dtinews.dantri.com.vn/print/20260122085104992.htm)).
  - What's hit hardest (Claude verifies for 2027 the week we post): street-food stalls and family restaurants (mostly closed Mùng 1-3), local markets, banks and government offices, many small shops; Grab/taxi surge pricing and fewer drivers; flights and buses out of the city sold out the days before.
  - What stays open: big malls, chain cafés and convenience stores, hotel restaurants, Nguyen Hue flower street and the fireworks on Tết Eve.
  - Photo angle: empty landmark streets for a few days = Snap Saigon's rarest shots ("book an empty-Saigon shoot").

## 6b. Giveaways and "if Vietnam win" prize drops
Full playbook: marketing-engine `giveaways-contests.md`. 1-2 a month, built into the hero post as a rung of the hook ladder.
- **January (Asian Cup):** "If Vietnam beat Korea on the 15th… one lucky commenter AND one lucky reposter win a weekend at <partner hotel> / 50 USD / dinner for two at <steakhouse>." Plus a prediction contest: "Comment the final score, closest guess wins." On Facebook: comment-to-enter only.
- **"If <player> scores" mini-drop** on the same post: 50 USD to one commenter.
- **Funny caption contest** (any month): the craziest motorbike-load or Tết-traffic photo: "Best caption wins a free Snap Saigon shoot."
- **Tết ghost-town post:** "Tag who you're spending Tết with: one pair wins a free empty-Saigon photo shoot."
- **Prizes:** cash (50 USD), an iPhone for the biggest moment of the year, partner prizes (hotel stays, steakhouse dinners, rooftop packages) and free Snap Saigon shoots.
- Draw with `tools/analytics/pick_winner.py` (published seed), announce in a follow-up post, deliver, log in posts.csv (`giveaway=yes`).

## 6c. Analytics: winners decide next month
- Every published post gets one row in `marketing/analytics/snap-saigon/posts.csv`: url, date, platform, lane, hook, hook_ladder (which ladder variant), cta, format, giveaway.
- Platform exports (IG/FB Insights, TikTok Studio, Metricool…) go into `marketing/analytics/snap-saigon/exports/` monthly.
- `python tools/analytics/winners.py --brand snap-saigon --days 90` writes `marketing/reviews/snap-saigon-<yyyy-mm>-winners.md`: talk score per post (shares/sends weigh most), winners and losers, and **do more / do less / test again** calls by lane, hook ladder, CTA, format and giveaway over the last 2-3 months.
- The monthly run reads the latest report first and justifies its hero pick with it ("events + tease-twist ladders + send CTAs averaged 1.6x the median over 90 days, so…").

## 7. Guardrails (market law: Vietnam pack in compliance-packs.md + brand file §2)
- **"Streets will go crazy" = celebrations.** Show flags, horns, crowds, fireworks. Don't show fights, police clashes or property damage, and no political or protest content: the page is not the press (brand file §2 rule 5).
- **Parties:** no drug references; alcohol shows as atmosphere, never as an offer. Never promote spirits of 15% ABV or more (VN alcohol-advertising law); a paid venue partner gets labelled as sponsored (Law 75/2025).
- **Faces:** crowd clips are fine organic; blur obvious minors, and never single out a drunk or embarrassing stranger.
- **Paid boosts:** Vietnamese headline first, English below (Advertising Law Art. 18).
- **Dates:** every date card verified against an official or news source the week we post; unconfirmed items say "TBC".

## 8. Monthly routine
- **~20th of each month:** refresh §5 for the next month (web search: listings, venues, expat groups, news), pick the hero moment, draft the trailer + carousel scripts (a monthly scheduled task does this and pings Klaus).
- **Claude:** collects 15-30 candidate clips per month with `collab scout` and commits the shortlist (creator, length, views, why). Klaus's PC runs `collab add-list` once to download them.
- **Klaus:** approves the script, then `/edit` cuts it from the collab clips (no generation credits needed).
- **After posting:** `/review` reads shares, sends, saves and tags per post; the best CTA wording becomes the default.
