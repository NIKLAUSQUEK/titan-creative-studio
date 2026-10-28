# Snap Saigon: "SAIGON IS ABOUT TO GO CRAZY" (monthly hype series) [draft]

Klaus, 2026-10-28: "the saigon travel content should also include festivities, wild expat parties, amazing and big celebrations, historic events that might happen (Vietnam U23 wins final, streets riot…) → do fun trailer and upcoming posts and events and comment tag your friend to get them ready or DM this if they should know why the streets will be crazy… needs a wild, fun, exciting, TOFU, event sharing, interest grabbing post monthly."

## 1. What the series is
- **Job:** top of funnel. Reach, shares and follows from tourists, expats and young locals. It sells nothing directly; the end card plants "get snapped at it" (snapsaigon.com).
- **Cadence:** one **hero trailer reel** per month (posted ~7-10 days before the month's biggest moment), plus support posts around it (§4).
- **Promise to the viewer:** "Here's why Saigon is about to go crazy this month, and where to be." Every post is a date-and-place guide disguised as a movie trailer.
- **Accounts:** Snap Saigon IG/TikTok/FB page (handles: CONFIRM). English-first, with a Vietnamese line on every slide and caption.

## 2. The hero trailer format (20-35 s, 9:16)
Genre grammar: §15 action/sport **anthem** (accelerating cuts) + §28 event promo (dates held ≥2 s) + §31 borrowed cold open (real clips, credited).

| Time | What's on screen | Sound |
|---|---|---|
| 0-2 s | **The wildest real clip from last time**: the streets after a Vietnam win, a Bui Vien Halloween crowd, Nguyen Hue fireworks. Header: "Saigon in 12 days:" | crowd roar up front, no music yet |
| 2-4 s | Black card, trailer type: "THIS NOVEMBER" / "THIS DECEMBER" | sub-boom on the card |
| 4-22 s | 3-5 events, each = 1 hype clip + a **date card** (event · date · place) held ≥2 s. Cuts speed up from ~3.5 s to ~1 s per shot as it builds | trailer drum build, a hit on every date card, riser into the last event |
| 22-28 s | The biggest moment last: "AND IF VIETNAM WINS…" + the craziest street clip, then cut to black | drop to silence 0.5 s → full crowd |
| 28-32 s | CTA card: **"Tag who's coming 👇"** / **"Send this to the friend who doesn't know why the streets will be crazy"** + small "get snapped there → snapsaigon.com" | music out on a hit |

- **Footage:** real people's clips from creators and locals, brought in with `editor.py collab add <url> --creator @h --use repost` (credit "via @h" burns on screen). The VA finds the original creator of reposted clips and tags them, then sends `collab dm @h --ask shoutout`. Our own snappers film the live moments for the recap (§4).
- **Editor:** `.\Run-Editor.ps1 -Project saigon-hype-<yyyy-mm> -Preset sport-anthem` with the date cards as `stat-counter`/`kinetic-quote` motion cards (`editor.py motion`). Vertical first, then 4:5 for the FB feed.
- **Type:** big condensed caps for date cards (Anton/Bebas), one accent colour per month. Vietnamese line under each card at ≤3/4 size.
- **Sound:** original or licensed trailer drums for the brand account (CLAUDE.md audio rule). Trending audio only in-app on personal/creator accounts. Real crowd and fireworks sound from the clips carries the energy.
- **Captions:** hook line + the event list with dates and places + the CTA twice (start and end) + 3-5 hashtags (#saigon #hochiminhcity #saigonnightlife #vietnam + the event tag). Vietnamese version under the English.

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
| ongoing | Expat parties: rooftop and Thao Dien parties, Bui Vien weekends, festival launches | the "wild expat parties" pillar | slot into any month | venue pages + expat FB groups (the VA collects) |

No confirmed December 2026 music festival turned up in search (8Wonder Winter ran in Dec 2024 and may return). The VA checks venue pages around the 20th of each month.

## 6. First posts (drafts)
**A. BONUS, this week: "Bui Vien on Halloween" (post Thu 29 or Fri 30 Oct)**
- 0-2 s: the craziest Bui Vien Halloween 2025 crowd clip (collab, credited). Header: "Saigon this Saturday:"
- Card: "31.10 · BUI VIEN · from 8pm". Then 3 fast costume / crowd / neon clips → card: "Want it calmer? NGUYEN HUE walking street".
- CTA: "Tag the friend who still has no costume 👇" / "Gửi cho đứa chưa có đồ hoá trang".
- End: "Our snappers are on Bui Vien Saturday night 📸 snapsaigon.com"

**B. November hero: "SAIGON IS ABOUT TO GO CRAZY: NOVEMBER" (post ~10 Nov)**
- Cold open: a stadium-fireworks opening-ceremony clip + "Saigon in 10 days:"
- Date cards: Fashion Week 5-10 Nov (if verified) → Food Festival 12-15 Nov → **National Games opening, 20 Nov, Thong Nhat Stadium** last, biggest.
- Bonus beat: "and Vietnam play twice before the Asian Cup… watch parties all over District 1."
- CTA: "Send this to the friend who keeps saying there's nothing to do in Saigon."

**C. December hero: "THE LAST 7 DAYS OF 2026 IN SAIGON" (post ~18 Dec)**
- Cold open: last NYE's Nguyen Hue fireworks.
- Cards: Christmas Eve at Notre-Dame Cathedral (24.12) → Nguyen Hue lights → rooftop parties → **COUNTDOWN 31.12, Nguyen Hue / Saigon River**.
- CTA: "Tag who you're kissing at midnight 👀" / "Save this for 31.12".
- End card: "Christmas + NYE shoots at Notre-Dame and Nguyen Hue → snapsaigon.com" (both are our photo spots).

**D. January hero: "IF VIETNAM BEAT KOREA ON THE 15TH…" (post ~8 Jan)**
- Cold open: the real "đi bão" clips from the AFF Cup win in August 2026 (horns, flags, the whole city on bikes), credited.
- Cards: "11.01 vs UAE" → "15.01 vs SOUTH KOREA" → "20.01 vs YEMEN" + where to watch (big screens, sports bars in D1/Thao Dien: the VA confirms).
- Close: "If they win… THIS is Saigon 10 minutes after the final whistle." → full-volume street chaos.
- CTA: "Send this to the friend who doesn't know why the streets will be crazy on the 15th" / "Gửi cho đứa chưa biết vì sao 15/1 đường phố sẽ 'bão'".
- If Vietnam win, the recap reel goes up the next morning: "Saigon last night 🇻🇳".

**E. February hero: "SAIGON'S BIGGEST WEEK" (post ~28 Jan)**
- Cold open: the Nguyen Hue flower street + Tết Eve fireworks.
- Cards: flower street (dates TBC) → Tết Eve fireworks (5 Feb, night) → "then the city goes EMPTY" (eerie empty-street shot: the perfect contrast beat).
- CTA: "Tag who you're spending Tết with 🧧" / "Save: everything that's open during Tết in Saigon" (support carousel).

## 7. Guardrails (market law: Vietnam pack in compliance-packs.md + brand file §2)
- **"Streets will go crazy" = celebrations.** Show flags, horns, crowds, fireworks. Don't show fights, police clashes or property damage, and no political or protest content: the page is not the press (brand file §2 rule 5).
- **Parties:** no drug references; alcohol shows as atmosphere, never as an offer. Never promote spirits of 15% ABV or more (VN alcohol-advertising law); a paid venue partner gets labelled as sponsored (Law 75/2025).
- **Faces:** crowd clips are fine organic; blur obvious minors, and never single out a drunk or embarrassing stranger.
- **Paid boosts:** Vietnamese headline first, English below (Advertising Law Art. 18).
- **Dates:** every date card verified against an official or news source the week we post; unconfirmed items say "TBC".

## 8. Monthly routine
- **~20th of each month:** refresh §5 for the next month (search + VA's venue/expat-group check), pick the hero moment, draft the trailer + carousel scripts (a monthly scheduled task does this and pings Klaus).
- **VA:** collects 15-30 candidate clips per month (last year's same event, creators' reposts), finds the original creators and runs `collab add`; logs everything in `marketing/collabs/snap-saigon.csv`.
- **Klaus:** approves the script, then `/edit` cuts it from the collab clips (no generation credits needed).
- **After posting:** `/review` reads shares, sends, saves and tags per post; the best CTA wording becomes the default.
