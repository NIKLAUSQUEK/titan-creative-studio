# Snap Saigon: testing round 1 (mock plan, nothing launched)
Template: ad-strategy.md §8. Tags: **[CONFIRM]** = Klaus has to answer · **[studio]** = our starting default, which is NOT a benchmark and gets tuned by `/review` · **[LM]** = Leo Moore (ad-strategy.md §2) · **[P]** = platform docs.
Nothing launches, posts or spends from this file. Paid setup goes through the `anthropic-skills:ads-meta` skill, and only after Klaus explicitly says go.

## 1. Round header
| Field | Value |
|---|---|
| Round | R1 (launch test, no prior winners) |
| Dates | starts on Klaus's go, after the pre-flight blockers below [CONFIRM]. The read dates are counted from launch day: L+7 and L+14 |
| Budget/day | **USD 20/day, about USD 280 for 14 days [CONFIRM: assumed "modest launch budget"]** |
| Platform | Meta (FB + IG feed, Reels, Stories) first, because the trust arm is a Facebook page. TikTok goes in round 2 [draft] |
| Objective / event | Sales → **Purchase on snapsaigon.com** if the Meta pixel + Conversions API fire on payment success [CONFIRM]. If they don't fire yet: optimise for Landing Page Views and track bookings by UTM, plus the site's own booking log |
| Target CPA | **baseline TBD.** Working placeholder: USD 14 per booking (≈50% of the cheapest Postcard price) **[studio placeholder; replace it with the real margin after snapper pay + editor cost]** |
| Break-even CPA | TBD = average order value minus snapper and editor cost per booking [CONFIRM the cost per shoot] |
| Hook-rate reference | 3-s plays ÷ impressions. Motion calls 20-40% "generally solid" [3P], used here only as a sanity check. The account baseline is TBD |
| Hold definition used | ThruPlays (15 s or complete) ÷ 3-s plays |

## 2. Volume
- **LM rule:** about 1 ad per USD 1k of spend, doubled at low spend. USD 280-600/month works out to ≥1-2 concepts a month, which is too thin to learn from. **Quality floor wins here:** "five genuinely great ads will beat 200 slop volumes" [LM].
- **Concurrent creatives:** <USD 500/day → 3-5 [LM]. At USD 20/day we run **4 ads at once in the test campaign plus 1-2 in retargeting**.
- **Winners-needed method:** we need 1 TOFU winner and 1 retargeting winner. At an assumed 10-20% hit rate [LM range] that means about 5-10 concepts across R1 + R2. R1 ships 10 drafts (mock-drafts.md), launches 6 and holds 4 as swaps.
- **Learning-phase reality:** Meta's learning phase wants about 50 optimisation events per ad set per week [P, verify current wording]. At USD 20/day that won't happen on Purchase. **R1 is therefore a creative read (hook rate, hold, CTR, cost per landing-page view, first bookings), not a CPA verdict.** State this in every review.

## 3. Structure + budget split
At launch there are no winners, so 100% of spend is testing: 3-5 concepts × 2-3 hooks [§8 launch default].
| Campaign | Share | Audience | Ads (from mock-drafts.md) |
|---|---|---|---|
| T1 TOFU test (one Advantage+/CBO campaign, one broad ad set per geo) | 70% ≈ USD 14/day | (a) people travelling in HCMC (Meta "travelling in" location), (b) pre-trip: KR, AU, US, SG, EU interest in Vietnam travel [draft]. Age 21-45 [draft] | C01 skit (H01, H02) · C04 process reel (H09) · C03 POV (H14) |
| T2 retargeting | 20% ≈ USD 4/day | site visitors 30 d, 50% video viewers of T1, engagers of organic C02/C08 (once there is enough volume; Meta needs a minimum audience size) | C10 static (H21) · C09 rain (H28) in Oct-Nov only |
| Net-new reserve | 10% ≈ USD 2/day, from week 2 | goes into T1 as swaps | C05 texting, C06 montage (whichever replaces the first kill) |
| Organic (0 spend) | n/a | FB page + IG + TikTok | C02 scam-tip carousel, C08 6-spots carousel, C07 snapper talking head. The best organic performer gets a calm paid "boost" in R2 |

**Net-new share:** ≥10-20% [LM] is satisfied (R1 is 100% net-new). From R2: 70% winners + iterations / 20% iterations under test / 10%+ net-new [studio default].

## 4. Pre-flight blockers (none of these are creative problems, but any one of them can sink R1)
1. **Site trust signals.** Add the legal entity, business registration, address and a real WhatsApp number to /terms or /about. Online-booking scams were named in the HCMC tourism + police agreement (Tuoi Tre 2026-08-08). Our own C02 checklist tells people to check exactly these things. If the site fails them, C02 must not run [CONFIRM].
2. **Pixel/CAPI** on the payment-success page, plus UTMs on every ad (`utm_campaign=R1&utm_content=<ad name>`).
3. **Language rule.** VN-first on every paid frame until counsel or Klaus clears English-only. The open question is whether ads served only abroad (KR/AU/US) are still in scope of Art. 18 [verify].
4. **Consent.** Written model releases with ad use for every snapper and actor. Customer photos are never used in ads (no written opt-in exists). Blur bystanders and plates.
5. **Exact terms text.** Paste the /terms refund + rain sentences verbatim into the brief before any copy is locked.
6. **Shoot day.** One real shoot day covers C01, C03, C04, C06, C07, C08 and C10 (Nguyen Hue → Notre-Dame park side → Ben Thanh south gate, plus Landmark 81 at sunset). Phone + one mirrorless camera. No drone. Check the Notre-Dame scaffolding on the day [verify].

## 5. Kill / keep / scale (R1 thresholds, with the [studio] numbers marked)
| Signal | Action | Source |
|---|---|---|
| Spent ~3x target CPA (≈USD 42 at the placeholder), 0 bookings, frequency not low | Kill | [LM]; USD figure [studio] |
| Hook rate in the bottom third of R1's ads after ≥1,000 impressions, while CTR among viewers is fine | Keep the body, test new hooks (§10 rung 1, levers 11/14/17/22) | [studio] |
| Hook OK, hold low | Recut the first 10 s, add a stim every 1.5-3 s (levers 12-14, 20) | [studio], ledger |
| Hold OK, CTR low | Put a spoken CTA naming snapsaigon.com earlier and add the price as text over the footage (levers 8, 10, 25) | §9 |
| CTR high, bookings ≈0 | Landing-page congruence: deep-link to the package (C03/C04 → Postcard, C08 → /photo-spots, C09 → rain FAQ). Check placements and age (levers 10, 24) | [LM ≈2:17] |
| CPA ≤ target with ≥5 bookings | Provisional winner: run the iterations.md SOP and graduate it to a scaling ad set | [studio threshold] |
| Meta "creative limited" / "creative fatigue" | Queue iterations / replace | [P via Jon Loomer] |
| Scale step | ≤20-30% budget increase per step, watch CPA for 3 days | [studio] |

## 6. Read dates
- **L+3:** delivery sanity check only (spend flowing, no rejections, captions show "Quảng cáo / Sponsored").
- **L+7:** hook rate + hold + CTR by ad. Kill or swap the bottom ad for C05/C06. Add hooks to the best body.
- **L+14:** cost per landing-page view, initiate-checkout, bookings, CPA by angle/format/persona → `/review snap-saigon` → `marketing/reviews/` → `/learn`.
- Naming for the export: `R1_<concept>_<angle>_<format>_<persona>_<offer>_<awareness>_<hook#>` (see mock-drafts.md), so the review can group by every field.

## 7. Top 3 bets (hypotheses)
1. **C01 skit (A1 alwaysphotog).** We believe friend groups and couples in or bound for HCMC will click because "I'm never in the photos" is a universal, self-recognised pain that needs no explaining. Evidence: the brand §3 pain plus travel press on solo travellers hiring photographers. No customer data yet [draft].
2. **C04 process reel (A5 noawkward).** We believe solo travellers and couples will book because seeing the snapper's 4 moves removes the "will it look cringe?" objection with real process, not claimed results. Evidence: the brand §3 objection and the site line "your snapper finds the angles" [draft].
3. **C10 static retargeting (A2 pricetransparent).** We believe warm visitors will convert because exact prices, "pay online, no cash" and stated terms answer the "is it legit?" fear that HCMC authorities themselves flagged in 2026 (Tuoi Tre 2026-08-08). This works only once the site shows a legal entity.
