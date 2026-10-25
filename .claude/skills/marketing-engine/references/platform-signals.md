# Platform signals: how each platform ranks content, and how every creative is built for it

Applies to EVERY creative and post (ads, skits, UGC, explainers, carousels, docs, clips), every brand. Researched 2026-10-25 from platform primary sources; full citations in `research/sources-platform-algorithms.md`.
Labels: **[O]** the platform says so (help centre, policy, ranking card, named exec) · **[S]** secondary reporting · **RoT** our rule of thumb (test it against the account's own data, analytics-loop.md). Platforms change monthly: re-verify anything older than 6 months before staking a campaign on it.

The one-line model for every platform: **ranking predicts how real viewers will react to THIS piece** (watch through, rewatch, send, save, comment, follow, or skip / "not interested") and filters out what is unoriginal, inauthentic, unlabelled or unsafe. There is no device, IP or "priming" trick that beats a piece people actually finish and send.

## 1. Verdict on the "Enterprise Algorithmic Arrest & Global Growth Masterplan" (received 2026-10-25)
Klaus asked that all creatives follow it. We adopt what is true, adapt what is half-true, and **reject what is false or breaks platform rules** (it would get client accounts restricted or banned, and an agency running fake-origin accounts for a clinic is a reputational and legal risk).

| Masterplan item | Verdict | What we do instead |
|---|---|---|
| Hook window 2.5 s (West) / 1.2 s (East) | PARTLY. No platform gives these numbers. IG ranks on "watching < 3 s" and uses "skips within 2 s" [O]; TikTok ads: proposition in the first 3 s, hook within 6 s [O]; Douyin/XHS publish no figure | **Frame 1 + first spoken line carry the hook; promise lands by 3 s on every platform** (§3). Our QC already requires the hook in the first 0.5 s |
| OCR reads overlays; put hook in a high-contrast box, upper third | PARTLY. On-screen text helps sound-off viewers and IG search reportedly models the video itself [S]; no official OCR ranking signal, no "upper third" rule | High-contrast hook text **inside the safe zones** (no faces covered, ledger 2026-10-10). Upper third is fine when the face is lower; never under UI |
| Change frames every 1.8-2.2 s or lose a "visual velocity score" | UNSUPPORTED. No such score exists | Pacing is a **retention** tool: visual change every ~2-4 s for punchy formats (preset `zoom.every_s`, `max_shot_s`), slower for premium/doc. Judge by the retention curve |
| Speak exact keyword in first 3 s (ASR indexes it) | PARTLY. YouTube search matches "video content" [O]; TikTok indexes captions/sounds/hashtags [O]; spoken-keyword indexing not officially confirmed. LinkedIn: no evidence | **Keyword in 3 places**: spoken early (cheap insurance, helps auto-captions), on screen, caption/title line 1. Editor brief `search_keyword` → QC checks it is spoken by 3 s |
| Music -18 to -22 dB, voice -3 to -6 dB or ASR misindexes | UNSUPPORTED as stated (mixes dBFS peak with loudness; no evidence ASR errors cut reach). Direction right: noise degrades auto-captions [O] | **Delivery spec**: -14 LUFS integrated, ≤ -1 dBTP, music bed ~15-20 LU under dialogue and ducked (editor default music -19 dB + sidechain duck). Review auto-captions; upload SRT on YouTube/LinkedIn |
| Loop ending (1.5× watch → top of feed) | PARTLY. Completion and ">95% watched" are ranking predictions [O]; Shorts count replays as views [O]; no 1.5× threshold | Loopable endings where the format allows (§3); never at the cost of the CTA on BOFU ads |
| New account: 5-7 posts on one keyword group | UNSUPPORTED as a mechanism; sensible as strategy | Launch each account with one tight series (same pillar, same promise) so viewers know what they follow. Not "training", just clarity |
| Western = interest graph; Eastern = private-traffic clusters / trust score | PARTLY. Douyin and XHS are centralised algorithmic feeds [O]; only WeChat Channels has a real social-graph layer; account health/credit scores exist as penalties, not the main driver | §5 |
| Xiaohongshu as a search engine; manual-style notes | SUPPORTED. 70% of XHS monthly users search [O-reported] | §5.1, with SG health limits (no price-led notes for clinics) |
| Keyword auto-reply funnelling leads into private WeChat groups | CONTRADICTED on XHS. Since 2025-01-07 WeChat IDs/phone numbers banned in auto-replies; 2025-03-12 rules ban contact details, QR codes, cross-platform diversion | XHS official tools only (社媒名片, 私信获客/留资, XHS shop). WeChat funnel lives on WeChat (Service Account + WeCom), promoted elsewhere |
| Caption = keyword headline / value bullets / 3 niche hashtags (max 5) | PARTLY. Instagram caps hashtags at 5 (2025-12-18) [O]; FB: ≤5 perform best [O]; Threads 1 topic tag; YouTube ignores all past 60; TikTok no cap | Adopted per platform in distribution.md §1-3 |
| Post at 7:30 / 12:15 / 18:30 local | UNSUPPORTED | Post window from the account's own analytics (unchanged rule) |
| SOP-OPS-044 Phase 1: factory-reset phones, target-country SIM in airplane mode, residential proxy, whoer.net "100% anonymity", fresh foreign email, never linked | **REJECTED.** Meta bans assets that deceive "about the identity, or origin" of an audience; TikTok bans "tricks meant to bypass our systems"; LinkedIn requires real identity; X bans fake personas. TikTok says device/account settings get **lower weight** than how viewers interact [O]. No platform documents SIM/MCC-based distribution | §6: legitimate account set-up + legitimate cross-border reach |
| Phase 2: 3-day "priming" (watch, like competitors, follow, comment) | **REJECTED as a ranking tactic.** Every documented signal is about viewers reacting to your content, not your browsing. Mass follow/like can read as spam | Do competitor and audience research (it's useful research, not ranking). Real community replies, by a named person, any time |
| Phase 3: strip EXIF, then 1% zoom / 0.5% speed / colour shift to "rewrite the hash so scanners think it's original" | **REJECTED. Contradicted by every platform.** IG: borders, watermarks, speed changes are not original; YouTube: pitch/speed changes are not meaningful; FB: stitching/watermarking doesn't count; TikTok: reused material needs "anything new"; deliberate disguise = circumvention | Originality is added value (§4). Strip GPS from staff/clinic photos for **privacy** only. Our own footage cross-posted cleanly is fine |
| One device + one manager per account; 12 h between logins to "mimic travel" | **REJECTED** as folklore. X explicitly allows social-media managers; Meta Business portfolio, TikTok Business Center, YouTube permissions exist so teams share access without sharing passwords | Role-based access (§6). Least privilege is good security, nothing more |
| "3 posts at 0-50 views = device flagged → delete app, new proxy IP, redo priming" | **REJECTED.** TikTok: low views don't "necessarily mean it broke a rule" [O]. New IPs/accounts to escape a restriction = ban evasion on every platform | Low-reach diagnosis tree, analytics-loop.md §6 |

## 2. What each platform actually ranks on [O unless marked]
| Platform | Documented ranking signals | Search reads | Hard filters / penalties |
|---|---|---|---|
| **TikTok** | Viewer interactions (watch-through of longer videos is strong, likes, shares, follows, comments), video info (captions, sounds, hashtags); device/account settings lower weight; follower count and past hits **not** direct factors | captions, sounds, hashtags (on-screen text/speech: not officially confirmed) | FYF-ineligible: unoriginal/reused without "anything new", inflated engagement, other-platform watermark [S], "extreme fitness or dieting", "overgeneralized mental health advice" (guidelines in force 2026-09-24). AI realistic content must be labelled |
| **Instagram Reels** | Top 3 = watch time, likes per reach, sends per reach (sends weigh more for non-followers, likes for followers; Mosseri 2025). Card predicts: < 3 s watch (skips within 2 s), > 95% watched, reshare, share off-IG, follow, use audio | caption + comment text, models of the media itself [S]; public pro-account posts indexed by Google/Bing since 2025-07-10 [S] | Shown less: low-res, watermarked, muted, borders, mostly text, already posted on IG. Unoriginal (incl. speed changes, screenshots of others' posts) → not recommended to non-followers; account-level loss until most of last 30 days is original (check Account Status). Hashtags capped at 5 and "don't increase reach" |
| **Instagram Feed / Explore / Stories** | Feed: time spent, comments, likes, shares, profile taps. Explore: likes, saves, shares. Stories: tap-in, reply, next | as above | Recommendation Guidelines (suggestive, regulated goods, repeat violations, profile/bio) |
| **Facebook Reels** | Watch duration, continued watching full-screen, click to full screen, like, watch vs skip, completion, see-less, hide, session start, next reel (card 2026-06-19) | captions | Unoriginal (stitching, adding your watermark) → reduced distribution on everything; best: no links in caption, minimal caps, ≤ 5 hashtags |
| **YouTube** | Clicks, watch time, "valued watch time" from satisfaction surveys, shares, likes, dislikes, channel reputation/quality. Search: relevance (title, tags, description, video content), engagement for that query, E-E-A-T quality | title, description, tags, video content; review auto-captions | "Inauthentic content" (2025-07-15): mass-produced/templated incl. generic AI, reused with minimal changes, pitch/speed tweaks. >60 hashtags = all ignored. Test & Compare picks thumbnails by **watch-time share**, not CTR. Shorts views count every start/replay since 2025-03-31 ("engaged views" still drive YPP) |
| **LinkedIn** | LLM-based retrieval + generative ranker over member history [O research/S]; P(skip) model lowers posts people scroll past ("time well spent") | text; image alt text (manual), video captions/SRT | One real-name account; no automation, browser bots, pods ("don't agree ahead of time to like or re-share") |
| **X** | Grok-based Phoenix model: Σ weight × P(action) over like, reply, repost, quote, DM share, link/profile clicks, dwell, video watch, follow; negatives (not interested, mute, block, report) weigh heavily; author-diversity decay, 48 h age filter (xai-org/x-algorithm, Aug 2026). Links no longer penalised per X product head (Jul 2026) [S] | text | Up to 10 accounts with distinct purposes (SMMs explicitly allowed); no fake personas, pods, bought engagement, "excessive unrelated hashtags" |
| **Threads** | Not published; links "working much better" (Mosseri) [S] | 1 topic tag/post | Meta policies |
| **Xiaohongshu** | Not published as a formula; >50% daily traffic to creators < 1k followers [O-reported]; "CES score" (like 1, save 1, comment 4, share 4, follow 8) = **folklore**, never confirmed | title, body, tags (OCR/speech indexing unverified) | No diversion (contact details, QR, links); paid seeding only via 蒲公英 with label; AI content must be self-labelled (undeclared → limited, 2026-02); fake engagement → credit Lv0; medical/aesthetic content heavily policed |
| **Douyin** | Per-user prediction of like, follow, share, comment, save, repeat view × value weights; "almost doesn't rely on tags"; completion counts; more review rounds as traffic grows (2025-03 disclosure). Traffic-pool tiers = creator lore | — | Re-upload/light re-edit "搬运" banned; account 健康分 starts at 100, low = reduced reach. Real-name with mainland ID/permit (no passports) |
| **WeChat Channels** | Following + friends-liked ("朋友赞过") + recommended | — | Same-entity Official Account/Mini Program links; "Add WeCom" button is the sanctioned private-traffic route |

## 3. The Platform-Fit build spec (applies at script, edit and package stage)
Every script (story-director Gate 3, story-writer, editor brief) and every edit must meet these. Items marked RoT are defaults, not laws: change them if the account's data says otherwise.

**Hook (0-3 s)**
1. Frame 1 is already interesting: face mid-action, the problem object, or the hook text. No logo sting, no black frame, no "hi guys" (editor QC: first frame not black, speech within 0.5 s).
2. Spoken hook + on-screen hook in the first second; the **promise/proposition is clear by 3 s** (TikTok ads guidance, IG "< 3 s" prediction).
3. On-screen text: high contrast (white/yellow with black outline or box), ≤ 7 words, inside safe zones, never over faces; readable at 5-10 words/s.
4. The hook is truthful and the video pays it off (skips and "not interested" are negative signals everywhere; YouTube surveys reward satisfied viewers).

**Body (retention)**
5. Payoff by ~60%; open loop or "wait for it" only if the payoff really comes.
6. Visual change every ~2-4 s on punchy short formats (cut, zoom, B-roll, text, angle) RoT; premium/doc presets slower. Never change shots so fast the message is lost; the retention curve decides.
7. Captions burned in for sound-off; auto-captions reviewed (YouTube/LinkedIn: upload SRT).
8. One idea per short. Length = the idea, not a target: 15-45 s for most shorts RoT; long-form per topic.

**Search (say it, show it, write it)**
9. Pick one `search_keyword` per piece: the phrase the audience types (vidIQ `vidiq_keyword_research`, platform search autocomplete, XHS search suggestions). Use plain local nouns ("lower back pain", "physio Tampines", "whey protein Singapore"), not internal jargon.
10. Say it in the first 3 s (RoT), show it on screen or in the cover, put it in caption/title line 1 and the YouTube description's first 2 lines. LinkedIn: keyword in text only.

**Share / send triggers (the strongest non-follower signal on IG)**
11. Each piece names who it's for so viewers send it to that person ("send this to your friend who sits all day"). Saves: checklists, steps, myth-vs-fact, tables (carousels).
12. Loopable ending where natural (the last frame flows into the first) for entertainment/TOFU; BOFU keeps a clear CTA instead.

**Originality and authenticity (non-negotiable)**
13. Our own footage, or real added value on others' material (commentary, narration, story, analysis). Never reposts of others with crop/zoom/speed/watermark changes. No screenshots of other people's posts as content.
14. Cross-post our own videos as **clean exports without another platform's watermark**, and re-hook, re-caption and re-cover per platform (distribution.md §7).
15. Label realistic AI visuals/voices with each platform's tool (TikTok AIGC label, Meta "AI info", YouTube altered/synthetic, XHS AI declaration; China's AIGC labelling measures since 2025-09-01). Keep C2PA credentials from generators; don't strip them.
16. Paid partnerships use the platform's disclosure tools (TikTok "Disclose commercial content", IG/FB Paid partnership label, YouTube "paid promotion", XHS 蒲公英) plus ASAS #ad wording in SG.

**Audio**
17. -14 LUFS integrated, ≤ -1 dBTP; dialogue clearly on top; music bed ~15-20 LU under voice and ducked; no noisy rooms for talking heads (auto-caption accuracy).

**Category safety (reach killers)**
18. Fitness/protein/body brands: no "extreme fitness or dieting" framing, rapid-weight-loss promises or body shaming (TikTok FYF exclusions, IG Recommendation Guidelines) on top of the compliance pack. Physio/health: no overgeneralised medical advice; "see a registered physio" framing.

## 4. Originality ladder (use it when repurposing)
| Level | Example | Distribution |
|---|---|---|
| 0 Repost | Someone else's clip, re-uploaded / zoomed / sped up / re-watermarked | Not recommended (IG, FB, TikTok, YT); account-level penalties. **Never** |
| 1 Our own asset, cross-posted clean | Our Reel exported without TikTok watermark, new caption + cover | Fine (IG only penalises content "already posted on Instagram") |
| 2 Re-cut | New hook, new order, new length from our own footage (repurpose-waterfall.md) | Fine; treated as a new piece |
| 3 Transformed | Reaction, critique, stitch/duet, commentary, narration over licensed/our footage | Fine; must add meaning, not just appear |
| 4 Original | New shoot / new generation from an approved spec | Best |

## 5. Eastern stack: what is real for a Singapore brand
**Who should use what:** TikTok for SG/MY short video (not Douyin). Xiaohongshu for Chinese-speaking SG/MY audiences and as a search channel (SG penetration is modest: ~22% of surveyed SG respondents use it, 2025). Douyin and WeChat Channels only with a licensed China partner/entity, for a real China go-to-market. Never register with VPNs, borrowed IDs or bought "blue-V" verifications (brokers sold fake ones, 2026).

### 5.1 Xiaohongshu (RedNote) note spec
- Account: professional account verified via the "境外及港澳台" route with ACRA documents, in-house (≈ RMB 600, non-refundable; medical categories may be refused: check first).
- Note = search answer. Title ≤ 20 characters with the keyword; body ≤ 1,000 characters, structured (problem → steps/list/table → takeaway); ~5-10 relevant tags; 3:4 cover with large Chinese hook text; up to 18 images. Manual-style carousels: exercise guides, "how to choose", ingredient tables, comparison grids. [S specs; verify in-app]
- Language: Simplified Chinese written by a native writer, SG/MY context (place names, local terms); not machine-translated.
- Banned: superlatives (最/第一/最佳/国家级, China Ad Law Art. 9), efficacy/cure claims, testimonials and before/afters for health/body (Art. 16), fabricated "素人" reviews, AI notes without declaration, any WhatsApp/WeChat/phone/QR/link in notes, comments, profile or auto-replies.
- Leads: 社媒名片, 私信获客/留资 lead components, XHS shop (overseas brand store for Power Protein). Paid creators: only via 蒲公英 with the sponsored label.
- SG health rules still apply on top (no price/discount-led clinic notes, no testimonials).

### 5.2 Douyin
Real-name verification needs a mainland ID / HK-Macau permit / PR card (no passports); blue-V needs a matching business licence. Re-uploads and light re-edits are penalised; account health score gates reach. Route: China partner agency or cross-border store with a co-liable partner. Get China ad-law + PIPL advice before any health claim or moving China leads to SG.

### 5.3 WeChat (Channels + Official Account + WeCom)
The only Eastern surface where friends' likes spread content. Overseas entities can verify an enterprise Service Account (~USD 99/yr). The sanctioned private-traffic loop is Channels profile → "Add WeCom" → WeCom groups/1:1, plus Mini Programs. Promote the Service Account from our other channels, not from XHS.

## 6. Accounts and cross-border reach: the legitimate SOP (replaces SOP-OPS-044)
**Set-up**
1. The client owns every account in their legal/brand name; the agency gets roles: Meta business portfolio → Partners (agency portfolio ID), TikTok Business Center ("Manage account"), YouTube Studio permissions (Manager/Editor), LinkedIn Page admin, XHS professional account sub-users. No shared passwords, no accounts in staff names for brands, no bought or aged accounts.
2. 2FA on every account, recovery email/phone owned by the client, access list in `brands/<brand>.md` §accounts (names + roles only, never credentials). Remove access when people leave.
3. Schedulers only through official APIs (Meta Business Suite, TikTok's own scheduler, YouTube Studio, Metricool or another API partner Klaus approves). No browser-automation, auto-like/follow/comment tools, engagement pods or bought engagement (bans on LinkedIn, X, TikTok, Meta, YouTube).
4. Real people in a real place: VPNs are fine for staff privacy on public Wi-Fi; never to fake where the brand is.

**Reaching another country's audience (all allowed)**
- Content in the audience's language, with local nouns, settings and references (localisation.md pack); local-language captions/subtitles; YouTube translated titles/descriptions and multi-language audio tracks (≥ 25% watch time from other languages, where available).
- Location tags for real locations (the clinic, the event, the city you're actually shooting in).
- Local creators via Collabs, Spark Ads, Partnership Ads, 蒲公英 — disclosed.
- Paid geo-targeting at country/city level (Meta, TikTok, YouTube, LinkedIn): the sanctioned way to buy local reach (ads-* skills).
- A separate local account only if the brand genuinely operates there (X/Meta allow per-market/language brand accounts), run transparently.

**New account launch (RoT)**
Bio = who it's for + what they'll get + one link; first 6-9 posts = one series on one pillar so the profile reads clearly; reply to every genuine comment in the first hour; Trial Reels (IG) to test hooks on non-followers without cluttering the grid.

## 7. Platform tests we use instead of guessing
- Instagram **Trial Reels**: 2 hooks on the same body, shown to non-followers; keep the winner (metrics after 24 h).
- YouTube **Test & Compare**: 3 thumbnails (title tests where available); winner = watch-time share.
- TikTok/Meta paid: 3-5 genuinely different creatives per test (TikTok guidance); one variable per organic test (analytics-loop.md §3).
- Retention curve review on every hero: where people drop → fix the hook/pacing rule for the next piece → `/learn`.

## 8. Platform-fit gate (run by /publish; also self-check at Gate 3 and in /edit)
```
[ ] Hook: frame 1 interesting, spoken + on-screen hook in 1 s, promise clear by 3 s, truthful
[ ] search_keyword chosen; spoken ≤ 3 s, on screen/cover, caption/title line 1 (per platform: §3.10)
[ ] Retention: payoff by ~60%, no dead air, pacing fits the preset, loop or CTA ending chosen deliberately
[ ] Send/save trigger present (who to send it to / save-worthy list)
[ ] Original: own footage or real added value; clean export (no other platform's watermark); not a repost
[ ] Hashtags within platform limits (IG 5 cap; FB ≤ 5; YT ≤ 3 shown, never > 60; Threads 1 topic; XHS 5-10 relevant; X few, relevant)
[ ] AI label set where realistic AI is used; paid partnership tool on where paid; ASAS #ad for SG
[ ] Audio -14 LUFS / ≤ -1 dBTP, voice on top, captions burned + reviewed
[ ] Category safety: no extreme fitness/diet framing, no overgeneralised medical advice, compliance pack PASS
[ ] Eastern: XHS no contact details/QR/links anywhere, 蒲公英 for paid creators, AI declared, Chinese copy native-written
[ ] Posted by the brand's own account through role-based access or an approved API scheduler; real location tag only
```
