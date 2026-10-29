# Snap Saigon: 10 mock ad drafts (round 1)
Status: **MOCK for Klaus's review. Nothing approved, rendered, launched or posted.** No existing brief, script or winning ad was found, so these are studio drafts, not Klaus's version A. If Klaus has a script for any of them, his script becomes A and these become proposal B.
Built from matrix.md (angles A1-A8), hooks.md (H01-H36) and round-1.md. Next step for any draft Klaus picks: `/ad` (story-director Gates 1-5; the drafts render at the lowest quality first) or `/edit` for real-footage cuts.

## Shared blocks (every draft uses them; each draft lists only its extras)
**[PAID] paid-frame rules**
- "Quảng cáo / Sponsored" is visible on frame 1 / slide 1 (top-left, small) and as the first word of the caption, plus Meta's own label.
- The VN line comes first, and the EN line goes below it at ≤3/4 size (VN 0.031 / EN 0.023 of frame height; captions VN 0.026 / EN 0.019).
- For spoken English, burn in VN subtitles above the EN subtitles.
- Font: Inter Bold. Colours: edit-brand draft (#111111 / #FFC727 / #FFFFFF; #E63946 only for the ⚠️ kicker).
- VN copy is a studio draft and needs a native check [CONFIRM].

**[EC-PC] end card, Saigon Postcard** (2.0 s, from edit-brand `end_card`; the lines sit over the final shot, darkened for legibility, never on a sudden blank page)
| VN (first, larger) | EN (below, ≤3/4) |
|---|---|
| Saigon Postcard · 1 giờ · 40 ảnh đã chỉnh + 3 clip dọc · nhận trong ngày | saigon postcard · 1 h · 40 edited photos + 3 vertical clips · same day |
| Từ USD 27.69 / nhóm tối đa 6 người (+150.000 VND mỗi người thêm) | from USD 27.69 per group of up to 6 (+150,000 VND per extra person) |
| Thanh toán online, không dùng tiền mặt · Không hoàn tiền, chỉ dời lịch | pay online, no cash · no refunds, postponement only |
| Đặt lịch tại snapsaigon.com | book at snapsaigon.com |
- Wordmark "snap saigon", lowercase, bottom-right.
- Paste the prices and the refund line verbatim from the live checkout and /terms on the day the copy is locked [CONFIRM].

**[CMP] compliance baseline**
- No reviews, testimonials, ratings or "customers say".
- No best / #1 / safest / guaranteed / official / tour / free.
- No fake scarcity.
- Blur bystanders, plates, shop signs and phone numbers.
- Real people only with written ad release, and no customer photos.
- No drone.
- Staged scenes carry "Minh hoạ / Dramatisation".
- "Same day" is claimed only for Postcard, "next morning" only for Half-Day.
- The 14 languages are site languages only.
- CTA = snapsaigon.com (no WhatsApp until a real number exists).

**[SND] sound baseline**
- Brand/paid audio is licensed only: Meta Sound Collection or TikTok Commercial Music Library (VN), chosen through `/sound`.
- The VN radar (marketing/audio/VN-2026-10-22.md) sets the mood only. Chart songs never go on these ads.
- Street ambience is recorded on the shoot day.
- Shutter click on each photo reveal.

**Footage:** real snapper footage is the default. Generated plates are a last resort and run through realism.md; a staged or generated scene carries the same "Minh hoạ / Dramatisation" label as any staged scene (a VN dramatisation label, not an AI label). No AI label in the video or caption; switch on the platform's AI-disclosure toggle for photoreal AI shots (ledger [ai-labels]). Never generate an AI likeness of a real snapper.

**Cast:** organic skits use the locked cast (Hân, Khang, Ben: cast/snap-saigon-influencer.md). These paid drafts default to real snappers and released actors (real people beat generated ones); a cast variant sits in iterations.md (C01 lever 16 d). Reused real clips come from `editor.py collab scout` (Claude collects; creators tagged in the caption, no on-screen credit).

---
## C01: "The Designated Photographer" (drama skit)
- **Ad name:** `R1_C01_alwaysphotog_skit_friendgroup_postcard_problem_h01`
- **Persona:** P1 friend groups (cuts for P2 couples, P4 solo) · **Awareness:** problem-aware · **Angle:** A1 "always the one taking everyone's photos"
- **Format / aspect:** drama skit (§5 skeleton D10 Deadpan Anticipation, scaled to 30 s) · 9:16 master, 4:5 feed cut · 30 s / 15 s
- **Genre:** §2 comedy skit / deadpan → brand look after the turn · **Preset:** `deadpan-comedy` · **genre_key** (only if a plate has to be generated): `naturalistic comedic tone, locked-off framing, clean even practical light, deadpan performances, no exaggerated mugging, realistic skin, everyday setting`
- **Hooks (test 3):**
  - H01 call-out: "Chuyến đi nào bạn cũng là người chụp cho cả nhóm? / always the one taking everyone's photos?"
  - H02 text-over-gallery: "214 tấm ảnh. 0 tấm có mình. / 214 photos. 0 of me."
  - H04 visual-only: a 4th phone stacked into Jess's hand.
  - Spares: H03, H05.
- **Gag locks (for spec.json hard_rules):**
  - **Who carries the gag:** JESS's camera roll and her stack of friends' phones. Jess never speaks before the turn.
  - **Hidden until the reveal at 14 s:** Jess's face never appears inside any photo frame or phone screen. The gallery count and the "only photo of me = my thumb" frame stay off screen until 14 s.
  - **Pun:** none.
- **Characters:** all fictional actors with releases, adults 25+. JESS (the designated photographer), SAM, ANA, KIM (friends), and a real SNAPPER (staff, release).

| s | Visual (camera owner) | Spoken / SFX | On-screen VN | On-screen EN |
|---|---|---|---|---|
| 0-2 | Nguyen Hue walking street, City Hall end. Neutral static WS: Jess crouched low, phone up; 3 friends posing. Her face is turned away | street ambience; shutter ×3 | [PAID] label · H01 · "Minh hoạ" | H01 · "dramatisation" |
| 2-5 | Neutral MS: Sam steps out of the pose, hands Jess a 2nd phone | SAM: "One more! Now on my phone." | Thêm tấm nữa! Giờ chụp bằng máy mình nhé. | one more! now on my phone. |
| 5-8 | Insert CU: Jess's hand, now holding 3 phones; Ana slides a 4th on top | 4 stacked shutter clicks | (none) | (none) |
| 8-11 | 3-shot montage, 1 s each: Ben Thanh south gate, Notre-Dame park side, sunset at Landmark 81 park. Each time Jess is behind the phone, in a new absurd crouch (she carries the gag) | one soft "tick" per cut | Ben Thanh · Nhà thờ Đức Bà · Landmark 81 | (spot names) |
| 11-14 | Hotel room, night, neutral WS: friends on the bed scrolling, delighted. Jess sits apart, opens her own gallery | ANA: "These are so good!" | Đẹp quá trời! | these are so good! |
| 14-17 | **REVEAL.** Jess-POV screen insert: album "Saigon · 214". She types "me" in search → 1 result: a blurry thumb over the lens. Crash zoom + 0.5 s freeze + one impact | impact, then silence | 214 tấm ảnh. 0 tấm có mình. | 214 photos. 0 of me. |
| 17-18 | Neutral CU: Jess's deadpan face, 0.8 s hold (cut on the eyes) | silence | (none) | (none) |
| 18-22 | **TURN** (brand look from here: warm golden-hour grade, lowercase type). Screen recording of the real snapsaigon.com: Saigon Postcard → time → meeting point Nguyen Hue → pay by secure link | soft licensed bed starts; UI taps | Saigon Postcard · 1 giờ · từ USD 27.69 / nhóm tối đa 6 người | saigon postcard · 1 h · from USD 27.69 per group of up to 6 |
| 22-27 | Real SNAPPER at Nguyen Hue directing all 4, Jess in the middle. Callback: Sam now holds all the phones | SNAPPER: "Xin chào! Everyone in. Jess, you too." · shutter | Xin chào! Tất cả vào hình. Cả Jess nữa. | hi! everyone in. jess, you too. |
| 27-28 | Insert: Jess's phone that evening, gallery shows her in the shots (photos from that real shoot, actors released) | shutter | Lần này, bạn có mặt trong ảnh. | this time, you're in the photos. |
| 28-30 | [EC-PC] | bed resolves | [EC-PC] | [EC-PC] |

- **Shot list (one shoot morning plus one hotel-room hour):**
  1. Nguyen Hue static WS, tripod, 28 mm.
  2. MS of the phone hand-off.
  3. Insert CU of the phone stack.
  4. 3 crouch angles at 3 spots (ideally the same shoot day as C04/C06/C08).
  5. Hotel WS.
  6. Jess-POV gallery screen recording (built in the editor; mock gallery with released photos only).
  7. CU of Jess for the reaction.
  8. Site screen recording.
  9. Snapper directing the group WS + MS.
  10. Phone insert of the delivered gallery.
- **Sound:** [SND]. The skit runs on room tone, not music. One licensed impact on the reveal, then silence. From the turn, a warm licensed V-indie/lo-fi bed with a soft guitar feel.
- **CTA:** a spoken line could be added in proposal B: "Book a snapper at snapsaigon.com". The visual CTA is the [EC-PC] card plus the Meta "Book now" button.
- **Compliance:** [PAID] [CMP].
  - The characters are fictional and labelled. Jess never says "I booked and loved it" (that would read as a testimonial).
  - The delivered gallery shows only released talent photos from the real shoot, and no customer photos.
  - The hotel room is generic, with no brand/hotel names.
- **15 s cut:** 0-2 hook → 8-11 montage (2 s) → 14-18 reveal → 22-27 snapper (3 s) → end card.

---
## C02: "3 tricks police flagged in 2026" (scam-tip soft-opener carousel)
- **Ad name:** `R1_C02_localfriend_carousel_shortstay_brand_unaware_h25`
- **Persona:** P1 + P4 + P5 (expats share it with visiting friends) · **Awareness:** unaware → problem-aware · **Angle:** A3 street-smart local friend
- **Format / aspect:** 7-slide carousel, 4:5 (1080×1350) · organic first on the FB page + IG. The paid version (calm "boost" to in-market travellers) runs only after pre-flight blocker 1 is cleared.
- **Genre:** §22 news / scam-expose, carousel form · **Preset:** `news-expose` (expander carousel-text with the kicker card) · **genre_key:** `credible photojournalistic style, clear evidence framing, neutral daylight, no dramatisation`
- **Hooks (slide-1 variants):**
  - H25 "3 chiêu lừa du khách ở TP.HCM năm 2026, theo nguồn công an và Tuổi Trẻ / 3 tricks on visitors in HCMC in 2026, per police and Tuoi Tre"
  - H26 "Trang đặt chỗ này thật hay giả? / is this booking page real?"
  - Third variant: "Lưu ý nhanh trước khi ra Bến Thành / quick heads up before you go to ben thanh"

| Slide | Visual | VN (first) | EN (below) | Source line (every slide) |
|---|---|---|---|---|
| 1 | Kicker bar "⚠️ MẸO SÀI GÒN / SAIGON TIP" (#E63946). Background: a real street photo near Ben Thanh with every face and plate blurred | [PAID version only: "Quảng cáo / Sponsored"] · 3 chiêu lừa du khách ở TP.HCM năm 2026, theo nguồn công an và Tuổi Trẻ | 3 tricks on visitors in HCMC in 2026, per police and tuoi tre | Nguồn / Source: Tuổi Trẻ News 2026-08-08, 2026-08-20; VietnamPlus 2026-07 [verify date] |
| 2 | Icon card (robe + bowl pictogram, no photo of any person) | 1. Áo tu hành và lời xin tiền. Có người mặc áo tu hành tiếp cận du khách quanh chợ Bến Thành để xin tiền. Bạn không bắt buộc phải cho: từ chối lịch sự, đi tiếp. | 1. robes and a donation request. people dressed as monks approached tourists around ben thanh market asking for money. you don't have to give: say no politely, keep walking. | Tuổi Trẻ News, 2026-08-20: police detained a group https://news.tuoitre.vn/5-chinese-detained-over-alleged-fake-monk-scam-targeting-foreign-tourists-in-ho-chi-minh-city-103260820161825797.htm |
| 3 | Icon card (playing cards + house) | 2. Ván bài "thân thiện". Người lạ mời về nhà chơi bài, cho bạn thắng trước, rồi rủ rút tiền để chơi tiếp. Từ chối mọi lời mời chơi bài ở nhà riêng. | 2. the "friendly" card game. a stranger invites you to a home game, lets you win first, then asks you to withdraw cash to keep playing. decline any private card-game invite. | VietnamPlus, 2026-07 [verify date]: a group charged over 18 cases https://en.vietnamplus.vn/foreign-nationals-charged-over-scam-targeting-tourists-post348856.vnp |
| 4 | Generic mock of a lookalike booking page (no real brand, no real URL) with a red circle on the URL bar | 3. Trang đặt chỗ giả. Trang sao chép trang thật của khách sạn và vé tham quan. Chỉ đặt trên trang riêng của chính doanh nghiệp, kiểm tra kỹ địa chỉ web. | 3. fake booking pages. copies of real hotel and ticket pages. book only on the business's own website, and check the web address. | Tuổi Trẻ News, 2026-08-08: HCMC Dept of Tourism + police on online booking scams https://news.tuoitre.vn/ho-chi-minh-city-tightens-tourism-management-amid-growing-scams-visitor-solicitation-103260808145850558.htm |
| 5 | Checklist card (4 ticks) | Trước khi trả trước online, kiểm tra: ✓ tên doanh nghiệp + liên hệ trên web ✓ điều khoản bằng văn bản (hoàn tiền / dời lịch) ✓ thanh toán qua cổng bảo mật, không chuyển khoản cá nhân ✓ thông tin khớp với trang mạng xã hội | before you prepay online, check: ✓ business name + contact on the site ✓ written terms (refunds / postponement) ✓ secure payment link, not a personal bank transfer ✓ details match their social pages | "Tips from snap saigon, based on the sources above" |
| 6 | Card: "Gặp chuyện? / in trouble?" | Gọi công an: 113. Lưu bài này cho chuyến đi. | police: 113. save this for your trip. | n/a |
| 7 (paid version only) | Real snapper photo at Nguyen Hue, warm grade | Chúng mình là snap saigon: thợ chụp ảnh địa phương. Giá niêm yết trên web, thanh toán qua cổng bảo mật, điều khoản rõ ràng. | we're snap saigon: local photographers. prices on our site, secure payment link, terms in writing. | n/a |

- **Shot list:** one real Ben Thanh street photo, blurred in post. Icon cards come from the editor (0 credits). No photos of the detained or charged people, even though the press ran stories (we don't need them, so we lower the risk).
- **Sound:** a static carousel has no music. If it gets cut to a video carousel: [SND] + low suspense pulse, "⚠️" ping on the kicker, a tick per step, a release chord on slide 5.
- **CTA:**
  - Organic: "Save + share with whoever you're travelling with."
  - Paid: Meta "Learn more" → snapsaigon.com/about.
  - No booking CTA on slide 1, and no price anywhere in this carousel (it is a soft opener).
- **Compliance:** [CMP].
  - Patterns only. **Nationalities are omitted** even though the source headline states them (punch at the trick). No individual or business is named.
  - Every fact is linked on its slide. We never call ourselves "báo/press/official".
  - **Slide 5 is a promise the brand must keep:** if snapsaigon.com lacks a business name or real contact, cut slide 7 and don't run the paid version.
  - Paid boost only in a calm form (no red-circle face shots, no rage).
  - The paid version carries "Quảng cáo / Sponsored" on slide 1.

---
## C03: "POV: 1 day in Saigon" (POV reel)
- **Ad name:** `R1_C03_timeshort_pov_shortstay_postcard_solution_h14`
- **Persona:** P1 short-stay (cut for P3 creators with H33) · **Awareness:** solution-aware · **Angle:** A4 timeshort (+ A5 mechanism inside)
- **Format / aspect:** POV / UGC · 9:16 · 18 s / 12 s
- **Genre:** §5 POV / relatable · **Preset:** `ugc-pov` · **genre_key** (only if generated): `first-person POV framing, subject reacting directly to camera as if to the viewer, phone-natural light, everyday location`
- **Hooks:** H14 POV card (lead) · H15 "1 giờ chụp. Nhận ảnh trong ngày. / 1 hour. photos the same day." · H16 "POV: your snapper shows you the first shot" · H33 for creators.
- **Camera owner:** VIEWER-POV throughout (the lens is "you"). The real snapper performs to the lens.

| s | Visual | Spoken / SFX | On-screen VN | On-screen EN |
|---|---|---|---|---|
| 0-2.5 | Viewer-POV walking onto Nguyen Hue (City Hall end), morning. Snapper turns, waves to lens | ambience; SNAPPER: "Xin chào! Hi! Ready?" | [PAID] · POV: chỉ có 1 ngày ở Sài Gòn và muốn thật sự có mặt trong ảnh | POV: 1 day in saigon and you want to actually be in the photos |
| 2.5-5 | Snapper gestures "a step left", frames with her hands | SNAPPER: "One step left… chin down a bit." | Lùi trái một bước… cằm thấp xuống chút. | one step left… chin down a bit. |
| 5-8 | Snapper drops low; the City Hall roofline behind the lens | shutter ×3 | Snapper lo góc chụp. | your snapper finds the angles. |
| 8-11 | Snapper: "Now walk toward me, don't pose." Walking-backwards shot | SNAPPER: "Walk to me. Don't pose." · shutter | Đi về phía mình. Đừng tạo dáng. | walk to me. don't pose. |
| 11-13 | Snapper turns the camera screen to lens: the real frame (talent, released) | SNAPPER: "Look, that's you." · soft ding | Nhìn nè, là bạn đó. | look, that's you. |
| 13-16 | 3 delivered photos + 1 s of a vertical clip, from the same real session | shutter per photo | 1 giờ · 40 ảnh + 3 clip dọc · nhận trong ngày | 1 h · 40 photos + 3 vertical clips · same day |
| 16-18 | [EC-PC] (short version: price + terms + URL lines) | bed resolves | [EC-PC] | [EC-PC] |

- **Shot list:**
  - Gimbal or phone at chest height, walking in, then walking backwards.
  - The snapper's lines are performed to the lens.
  - Camera-back insert, filmed for real (not a mock-up).
  - Delivered photos from the same session.
  - The "you" person is never fully seen, except in the delivered photos (that person is released talent).
- **Sound:** [SND]. A light licensed indie-pop bed, the snapper's live voice, a shutter on each photo.
- **CTA:** the snapper's last line, proposal B: "Book me at snapsaigon.com". "Book now" button deep-links to the Postcard package.
- **Compliance:** [PAID] [CMP].
  - "Same day" sits next to Postcard only. No "before your flight", no "in 1 hour".
  - The snapper's languages are not claimed.
  - Bystanders on Nguyen Hue are blurred.

---
## C04: "My selfie vs 60 seconds with a snapper" (street-photo before/after: process, not fake results)
- **Ad name:** `R1_C04_noawkward_process_solo_postcard_problem_h09`
- **Persona:** P4 solo travellers (cut for P2) · **Awareness:** problem-aware · **Angle:** A5 noawkward (mechanism: 4 moves)
- **Format / aspect:** process before/after · 9:16 master + 4:5 · 24 s / 15 s
- **Genre:** §26 before/after transformation, used as process · **Preset:** `ugc-try-on-demo` (matched framing, whoosh on the switch) · **genre_key:** n/a (real footage only; this ad must not use generated images at all, because its whole claim is that the photos are real)
- **Hooks:** H09 split selfie (lead) · H13 curiosity "60 giây sau… / 60 seconds later…" · H08 "starring… your arm?" · H11 "don't know how to pose? good." · H12 snapper on the pavement.
- **Honesty locks (spec hard_rules):**
  1. The "before" selfie is shot honestly by the talent at arm's length, the way they normally would. No deliberately bad angle, no darkening.
  2. Same person, same day, same spot, same outfit.
  3. Show the SOOC (straight-out-of-camera) frame before the edit.
  4. The edit is limited to what the package delivers (colour + crop) [CONFIRM the editing standard]. No face or body retouching.
  5. Persistent label: "Ảnh thật · cùng người · cùng ngày · cùng địa điểm / real photos · same person · same day · same spot".

| s | Visual | Spoken / SFX | On-screen VN | On-screen EN |
|---|---|---|---|---|
| 0-2 | Split: left, the talent's real arm-length selfie at Notre-Dame park side (towers cropped); right, the same spot, blurred (the snapper's frame fills it at 19 s) | none | [PAID] · Ảnh selfie của mình vs. 60 giây với snapper | my selfie vs 60 seconds with a snapper |
| 2-6 | Step 1: the snapper's hand guides the talent one step out of the tourist line (bystanders blurred) | tick; SNAPPER: "Out of the crowd line." | Bước 1: ra khỏi dòng người | step 1: out of the crowd line |
| 6-10 | Step 2: the snapper turns the talent 30° toward the light | tick; "Face the light." | Bước 2: quay về phía ánh sáng | step 2: face the light |
| 10-14 | Step 3: the snapper drops to the pavement so the towers fit | tick; shutter | Bước 3: hạ thấp máy để vừa cả hai tháp | step 3: get low so both towers fit |
| 14-17 | Step 4: "walk, don't pose": the talent walks, laughing | tick; "Walk. Don't pose." | Bước 4: đi tự nhiên, đừng tạo dáng | step 4: walk, don't pose |
| 17-19 | The SOOC frame, full screen, label "SOOC" | shutter | Ảnh gốc, chưa chỉnh | straight out of camera |
| 19-21 | Whoosh to the delivered edit, the same frame; label "edit: colour + crop" | whoosh | Đã chỉnh: màu + cắt khung | edited: colour + crop |
| 21-24 | [EC-PC] + the persistent "real photos" label | bed resolves | [EC-PC] | [EC-PC] |

- **Shot list:**
  - Selfie on the talent's own phone (screen-record it, or keep the file with EXIF).
  - Over-the-shoulder BTS, 35 mm, as the snapper works.
  - The snapper's own frames from the camera.
  - Keep the SOOC + edited files in `projects/<p>/proof/` as the substantiation file.
- **Sound:** [SND]. Light licensed bed, a tick per step, shutter, one whoosh on the switch.
- **CTA:** "Book now" → Postcard. Proposal B: an on-screen typed line "book your 60 seconds… and the other 59 minutes" [draft].
- **Compliance:** [PAID] [CMP].
  - This is a process demo, not a result claim. The talent is staff or hired, released, and not posed as a customer review.
  - The "before" must not be sabotaged (Universal: claims only you can prove).
  - Notre-Dame scaffolding [verify]; move to the Nguyen Hue City Hall end if the towers are covered.

---
## C05: "Photo duty" (texting scene with the editor's chats[] cutaway)
- **Ad name:** `R1_C05_alwaysphotog_texting_friendgroup_postcard_problem_h06`
- **Persona:** P1 friend groups · **Awareness:** problem-aware · **Angle:** A1 (same argument as C01, a different look: series character JESS)
- **Format / aspect:** texting / receipts suspense · 9:16 · 25 s (§30 is a 60-90 s map; this compresses it to ad length: the punch bubble alone + one silence beat are kept)
- **Genre:** §30 texting suspense · **Preset:** `texting-suspense` (beats carry `chat`, rendered by tools/editor chatanim.py) · **genre_key** (interview plate if generated): `intimate documentary interview, warm practical lamp light, shallow depth of field, muted desaturated palette, still locked camera, tense quiet atmosphere`. Prefer real footage of the actor.
- **Hooks:** H06 "Jess ơi, lại tới lượt bạn cầm máy rồi 😂 / jess you're on photo duty again 😂" (lead) · H07 punch-first "Mình không có tấm nào ở Bangkok luôn. / i have 0 photos of me from bangkok." · H02.
- **Chat language rule:** each bubble shows the VN line first, with the EN line smaller below it inside the same bubble (Art. 18 reading [verify]). The chat is a composite, written by us, and labelled "Minh hoạ / Dramatisation".

| s | Visual | Chat bubbles (VN / EN) | SFX |
|---|---|---|---|
| 0-3 | Jess's hotel-room shot, dimmed and blurred; over it the group chat "Saigon trip 🇻🇳", one bubble alone and large | SAM: "Jess ơi, lại tới lượt bạn cầm máy rồi 😂" / "jess you're on photo duty again 😂" | cold open, low pulse |
| 3-6 | Locked MS: Jess on a hotel bed, lamp light, looking at her phone (the actor; [PAID] label + "Minh hoạ") | (none) | pulse |
| 6-11 | Bubbles over Jess's shot (dimmed) | ANA: "Ai mang máy xịn vậy?" / "who's bringing the good camera?" · KIM: "Jess chứ ai 😂" / "jess obviously 😂" · typing dots (Jess) | tick per bubble |
| 11-14 | **PUNCH** (the twist): hard cut to Jess's CU, frozen; her bubble large over it, then 0.8 s of silence | JESS: "Mình không có tấm nào ở Bangkok luôn." / "i have 0 photos of me from bangkok." | silence |
| 14-16 | Jess looks up to the lens, says nothing | (none) | soft hit |
| 16-21 | Bubbles over Jess's shot (dimmed), her small smile behind them | JESS: "Mình đặt snapper rồi. 1 tiếng, Nguyễn Huệ, từ USD 27.69 cho cả nhóm." / "booked us a snapper. 1 h, nguyen hue, from USD 27.69 for all of us." · SAM: "Cả nhóm luôn hả?" / "wait, the whole group?" · JESS: "Tối đa 6 người. Trả online. Có ảnh trong ngày." / "up to 6. paid online. photos same day." | tick per bubble |
| 21-23 | Real snapper photo from the shoot: Jess in the centre of the group | KIM: "Jess cuối cùng cũng có mặt trong ảnh 😭" / "jess finally in the photos 😭" | shutter + release chord |
| 23-25 | [EC-PC] | | bed resolves |

- **Shot list:** 2 locked set-ups of the actor (bed MS, look-up CU) + 1 group photo from the C01 shoot. The chats are editor graphics (0 credits), laid over the dimmed bed shot (genre §30 default; until the editor's chat overlay mode exists, the full-black chat card is the fallback).
- **Sound:** [SND]. Licensed low pulse bed, a tick per bubble, silence on the punch, a release chord on the group photo.
- **CTA:** [EC-PC] + "Book now". Proposal B: a final bubble from Jess, "link: snapsaigon.com".
- **Compliance:** [PAID] [CMP].
  - A composite chat, never a real customer's. It must not look like a screenshot from a real user (keep our styled cards, not a native iMessage/WhatsApp UI clone).
  - Jess is fictional, and her "booked" line is story, not a testimonial claim of results.
  - "Same day" is used with Postcard context only (1 h = Postcard).

---
## C06: "This is me… and this is also me" (multi-spot montage)
- **Ad name:** `R1_C06_spotpicker_montage_creator_postcard_solution_h18`
- **Persona:** P3 creators (cut for P2 couples) · **Awareness:** solution-aware · **Angle:** A6 spotpicker (+ A8 reels-ready)
- **Format / aspect:** match-cut montage (the format of §36, but with **real footage, no AI clone**) · 9:16 · 16 s / 10 s
- **Genre:** §36 "this is also me" format with a §4 beat-switch rhythm · **Preset:** `trend-beat-switch` (beat_sync on) · **genre_key** (montage, only if generated): `bold readable compositions, single clear subject per frame, high clarity, vivid colour, centred framing`
- **Hooks:** H18 "Đây là mình… / this is me…" (lead) · H19 "saigon at sunset, or bui vien at midnight?" · H33 "3 vertical clips included…".
- **Truth lock:** the 4 looks are **separate Postcard sessions** (one meeting point per booking) unless Klaus confirms multi-spot sessions [CONFIRM]. Small persistent label: "Mỗi địa điểm là một buổi chụp riêng / each spot is a separate session". The same released creator-talent appears in all 4, in 4 outfits.

| s | Visual (match cut: same pose and head position across spots) | On-screen VN | On-screen EN | SFX |
|---|---|---|---|---|
| 0-2 | Talent at Notre-Dame park side, morning, looking to lens | [PAID] · Đây là mình ở Nhà thờ Đức Bà… | this is me at notre-dame… | beat 1 |
| 2-4 | Match cut: Ben Thanh south gate, a different outfit | …và đây cũng là mình ở chợ Bến Thành | …and this is also me at ben thanh | whoosh |
| 4-6 | Match cut: Thao Dien, Xuan Thuy street, café-lined (generic signage) | …cũng là mình ở Thảo Điền | …also me in thao dien | whoosh |
| 6-8 | Match cut: Landmark 81 riverside park at sunset | …và lúc hoàng hôn ở Landmark 81 | …and at sunset at landmark 81 | whoosh |
| 8-10 | Match cut: Bui Vien / De Tham corner at night, neon (bystanders blurred) | …và cả Bùi Viện lúc tối | …and bui vien at night | drop |
| 10-13 | 2×2 grid of the vertical clips playing (real Postcard deliverables) | Mỗi buổi Postcard: 40 ảnh + 3 clip dọc · nhận trong ngày | every postcard session: 40 photos + 3 vertical clips · same day | beat |
| 13-16 | [EC-PC] with the line "6 điểm hẹn, bạn chọn / 6 meeting spots, you pick" | [EC-PC] | [EC-PC] | resolve |

- **Shot list:** 5 spots × 1 locked "hero pose" per spot (a tripod mark at the same height and focal length, 35 mm) for clean match cuts, plus the snapper's vertical clips. Spread across the 1-2 shoot days with C08.
- **Sound:** [SND]. A licensed upbeat V-pop-feel instrumental with clear onsets (beat_sync), a whoosh per swap.
- **CTA:** "Book now" → /photo-spots.
- **Compliance:** [PAID] [CMP].
  - Don't imply that one session covers 5 spots.
  - No "best at sunset" (write "at sunset").
  - Bui Vien: blur faces and signage, no alcohol focus.
  - The talent is a creator hired with a release, and if they post it themselves, it is a paid partnership with disclosure (Law 75/2025 KOL duties).

---
## C07: "Three questions people ask before they book" (snapper talking head)
- **Ad name:** `R1_C07_pricetransparent_talkinghead_shortstay_postcard_problem_h31`
- **Persona:** P1 + P4 (+ P5 organic) · **Awareness:** problem-aware → product-aware · **Angle:** A2 price transparency + A7 rain + honest no-refund (objection handling)
- **Format / aspect:** snapper talking head with B-roll every 2-3 s · 9:16 + 4:5 · 35 s / 20 s
- **Genre:** §21 explainer / myth-buster · **Preset:** `talking-head-punchy` · voice reference: Ho Nguyen Minh Khang (style_creators id 51, pending StyleCard), used for technique only · **genre_key:** n/a (real snapper only; never AI likeness)
- **Speaker:** a real Snap Saigon snapper (staff), written release, added to `cast/registry.md` [CONFIRM name and consent]. If Klaus is the founder on camera, swap the speaker and keep the same script.
- **Hooks:**
  - H31 "Xin chào! Mình là [tên], snapper ở Sài Gòn. / hi! i'm [name], a snapper in saigon." (lead)
  - H24 "Giá trên web là giá bạn trả. / the price on the site is the price you pay." (only if checkout adds no fees [CONFIRM])
  - H27 "before you pay anyone in saigon: 3 things" (after the site trust fix)
  - H22 "no haggling. no cash."
- **Script source:** the three questions come from the site FAQ question list (rain, payment, refunds) [web 2026-10-25]. The answers paraphrase /terms and must be checked against the verbatim text [CONFIRM].

| s | Visual | Spoken (VN first, then EN) | On-screen VN | On-screen EN |
|---|---|---|---|---|
| 0-3 | MS of the snapper, Nguyen Hue City Hall end, camera on a strap | "Xin chào! Mình là [tên]. Hi, I'm [name], a snapper in Saigon." | [PAID] · Xin chào! Mình là [tên], snapper ở Sài Gòn. | hi! i'm [name], a snapper in saigon. |
| 3-5 | Same shot | "Three questions people ask before they book." | 3 câu hỏi trước khi đặt lịch | 3 questions before you book |
| 5-12 | B-roll: the site's price page screen recording → a hand paying on a phone (no card numbers) | "One: is the price the price? Postcard is from 27.69 US dollars for a group of up to six, plus 150,000 dong per extra person. You pay online. No cash." | 1. Từ USD 27.69 / nhóm tối đa 6 người · +150.000 VND mỗi người thêm · thanh toán online, không tiền mặt | 1. from USD 27.69 per group of up to 6 · +150,000 VND per extra person · pay online, no cash |
| 12-19 | B-roll: rain on a café awning (generic) → the snapper under an umbrella, smiling | "Two: what if it rains? We have an indoor plan, at no extra cost." | 2. Trời mưa: có phương án trong nhà, không tính thêm phí | 2. rain: indoor plan at no extra cost |
| 19-26 | Back to the snapper, straight to lens, no music dip | "Three: can I get a refund? No. But you can postpone. We'd rather tell you now." | 3. Không hoàn tiền, nhưng bạn có thể dời lịch | 3. no refunds, but you can postpone |
| 26-31 | B-roll: the snapper directing a released talent at Ben Thanh south gate, 3 delivered photos | "Then you just show up. I find the angles." | Bạn chỉ cần có mặt. Snapper lo góc chụp. | you just show up. your snapper finds the angles. |
| 31-35 | [EC-PC] | "Book at snapsaigon.com." | [EC-PC] | [EC-PC] |

- **Shot list:**
  - Talking head in one location, 2 framings (MS and MCU) for punch-ins.
  - Site screen recordings.
  - Payment insert.
  - Rain B-roll (real, on a rainy afternoon; season Oct-Nov).
  - BTS directing.
  - Lav mic + room noise reduction (`editor.py enhance`). Real voice, never TTS (ledger 2026-10-25).
- **Sound:** [SND]. A low licensed bed under the voice, a light whoosh on each number card. Live voice first.
- **CTA:** spoken, naming the channel: "Book at snapsaigon.com". "Book now" button.
- **Compliance:** [PAID] [CMP].
  - The snapper speaks only about what she knows (KOL duty; she is staff, so disclose it as a brand ad).
  - The refund line is stated plainly, never hidden.
  - "Indoor plan": no venue name and no "same time" until confirmed.
  - No claims about the snapper's languages unless true for her.

---
## C08: "6 meeting spots" (carousel)
- **Ad name:** `R1_C08_spotpicker_carousel_couples_postcard_solution_h17`
- **Persona:** P2 couples (cut for P3) · **Awareness:** solution-aware · **Angle:** A6 spotpicker
- **Format / aspect:** 8-slide carousel · 4:5 · organic first, then as a paid carousel in T1/T2
- **Genre:** clean bilingual info carousel (Vietcetera-style reference, id 62, pending) · **Preset:** expander `carousel-text` on the brand photo-ad family (warm grade, lowercase type); not the kicker card · **genre_key:** n/a (real photos only)
- **Hooks (slide 1):**
  - H17 "6 điểm hẹn. Bạn chọn phông nền. / 6 meeting spots. you pick the backdrop." (lead)
  - H19 "Sài Gòn lúc hoàng hôn, hay Bùi Viện lúc nửa đêm? / saigon at sunset, or bui vien at midnight?"
  - H20 "not every spot has to be a crowd spot."

| Slide | Real photo (released talent, the couple) | VN (first) | EN (below) |
|---|---|---|---|
| 1 | 6-tile grid | [PAID] · 6 điểm hẹn. Bạn chọn phông nền, snapper lo góc chụp. | 6 meeting spots. pick your backdrop, your snapper finds the angles. |
| 2 | Notre-Dame Cathedral, park side | Nhà thờ Đức Bà (phía công viên): kiến trúc cổ, nắng sáng | notre-dame cathedral (park side): old architecture, morning light [draft tip] |
| 3 | Nguyen Hue walking street, City Hall end | Phố đi bộ Nguyễn Huệ (phía UBND TP): rộng, thoáng, nhiều góc đi bộ | nguyen hue walking street (city hall end): wide, open, made for walking shots |
| 4 | Ben Thanh Market, south gate | Chợ Bến Thành (cổng Nam): màu sắc và nhịp sống chợ | ben thanh market (south gate): colour and market life |
| 5 | Landmark 81 riverside park, sunset | Công viên ven sông Landmark 81: nên đi lúc hoàng hôn | landmark 81 riverside park: go at sunset |
| 6 | Thao Dien, Xuan Thuy street | Thảo Điền, đường Xuân Thủy: quán xá, cây xanh, yên tĩnh hơn | thao dien, xuan thuy street: cafés, trees, quieter |
| 7 | Bui Vien / De Tham corner, night | Góc Bùi Viện / Đề Thám: đèn neon về đêm | bui vien / de tham corner: neon at night |
| 8 | Price + how-to card over a soft photo | Chọn điểm hẹn → chọn giờ → thanh toán online. Saigon Postcard từ USD 27.69 / nhóm tối đa 6 người · Half-Day Explorer từ USD 53.85 · Không hoàn tiền, chỉ dời lịch · snapsaigon.com | pick a spot → pick a time → pay online. saigon postcard from USD 27.69 per group of up to 6 · half-day explorer from USD 53.85 · no refunds, postponement only · snapsaigon.com |

- **Shot list:** 6 spots × 1 hero frame of the couple (the C06 shoot can supply them). Generic signage only; blur bystanders; no drone.
- **Sound:** none (static). For a Reels version: [SND] + a shutter per slide.
- **CTA:** "Book now" → /photo-spots. Organic: "Comment the spot you'd pick" [draft; no giveaway attached].
- **Compliance:** [PAID] [CMP].
  - The site's "best at sunset" becomes "go at sunset". Spot descriptions are neutral (the "[draft tip]" lines need Klaus or the snappers to confirm).
  - No Independence Palace.
  - Half-Day appears with its price only; "next morning" is claimed only if shown with Half-Day.

---
## C09: "Rain? Your shoot still happens." (rain-plan reassurance)
- **Ad name:** `R1_C09_rainplan_static_shortstay_postcard_product_h28` (video sibling: `R1_C09v_rainplan_shortvid_shortstay_postcard_product_h29`)
- **Persona:** P1 in-market and pre-trip, Oct-Nov · **Awareness:** product-aware (objection) · **Angle:** A7 rainplan
- **Format / aspect:** static 4:5 + 10 s video 9:16 · **seasonal:** run Oct-Nov only. HCMC's rainy season runs about May-Nov, mostly short afternoon storms (localvietnam.com, a blog, indicative). Pause Dec-Apr.
- **Genre:** feel-good reassurance (§9 accent, light) · **Preset:** `feelgood-emotional` for the video; brand photo-ad family for the static · **genre_key** (only if generated, labelled): `soft warm light after rain, wet reflective street, gentle cheerful mood, natural colour`
- **Hooks:**
  - H28 "Trời mưa ở Sài Gòn? Buổi chụp vẫn diễn ra. / rain in saigon? your shoot still happens." (lead)
  - H29 "Mưa thì vào trong. Không tính thêm phí. / rain? we go indoors. no extra cost."
  - H30 "saigon rainy season: usually afternoons."
- **Static (4:5):**
  - Real photo: a released couple laughing under a café awning, rain visible, plates blurred.
  - Top: [PAID] · H28 VN / EN.
  - Middle: "Có phương án trong nhà · không tính thêm phí / indoor plan · no extra cost".
  - Bottom strip: "Saigon Postcard từ USD 27.69 / nhóm tối đa 6 người · Không hoàn tiền, chỉ dời lịch / saigon postcard from USD 27.69 per group of up to 6 · no refunds, postponement only · snapsaigon.com".
- **Video (10 s):**

| s | Visual | SFX | On-screen VN | On-screen EN |
|---|---|---|---|---|
| 0-2 | Motorbikes in ponchos in heavy rain (plates and faces blurred) | rain + horn ambience | [PAID] · Trời mưa ở Sài Gòn? | rain in saigon? |
| 2-5 | The snapper opens an umbrella over the couple, leads them under cover | umbrella pop, laugh | Buổi chụp vẫn diễn ra. | your shoot still happens. |
| 5-8 | Indoor frames of the couple (generic interior, no venue branding) + 2 delivered photos | shutter ×2 | Phương án trong nhà · không tính thêm phí | indoor plan · no extra cost |
| 8-10 | [EC-PC] short (price + terms + URL) | resolve | [EC-PC] | [EC-PC] |

- **Sound:** [SND]. Real rain ambience up front, then a gentle licensed acoustic bed. (The GREY D "dự báo thời tiết hôm nay mưa" chart track is a mood note only; never use it.)
- **CTA:** "Book now" → the rain FAQ anchor, then the Postcard package.
- **Compliance:** [PAID] [CMP].
  - "Free" → "no extra cost" (the edit-brand forbids "free").
  - Don't promise "same time", a named venue or "rain-proof" results [CONFIRM what the rain plan is: a location swap or a reschedule?].
  - The rain footage is real; a generated plate is the last resort and carries the usual "Minh hoạ / Dramatisation" staged-scene label (no AI label).

---
## C10: "Know the price before you go" (static retargeting)
- **Ad name:** `R1_C10_pricetransparent_static_retarget_allpkg_mostaware_h21` (variant B: `..._h23` per-group math)
- **Persona:** retargeting (site visitors 30 d, 50% video viewers of C01/C03/C04, carousel engagers) · **Awareness:** most aware · **Angle:** A2 pricetransparent
- **Format / aspect:** native static, 1:1 (1080×1080) + 4:5 · single image, or a 3-card carousel (one package per card)
- **Genre:** native static / long-copy image · **Preset:** photo-ad family (photo-effects.md for the real photo; type from edit-brand) · **genre_key:** n/a (real photo)
- **Hooks:**
  - H21 "Biết giá trước khi đi. / know the price before you go." (lead)
  - H23 "Từ USD 27.69 cho cả nhóm tối đa 6 người / from USD 27.69 for the whole group, up to 6"
  - H22 "Không mặc cả. Không tiền mặt. / no haggling. no cash."
- **Layout A (1:1):**

| Zone | VN (first, larger) | EN (below, ≤3/4) |
|---|---|---|
| Top-left tag | Quảng cáo | sponsored |
| Headline | Biết giá trước khi đi. | know the price before you go. |
| Row 1 | Saigon Postcard · 1 giờ · 40 ảnh + 3 clip dọc · nhận trong ngày · từ USD 27.69 | saigon postcard · 1 h · 40 photos + 3 vertical clips · same day · from USD 27.69 |
| Row 2 | Half-Day Explorer · 4 giờ · 100 ảnh + 10 clip · sáng hôm sau · từ USD 53.85 | half-day explorer · 4 h · 100 photos + 10 clips · next morning · from USD 53.85 |
| Row 3 | Full Day · 8 giờ · từ USD 103.85 · chi tiết trên web | full day · 8 h · from USD 103.85 · details on site |
| Footer | Giá cho nhóm tối đa 6 người (+150.000 VND mỗi người thêm) · Thanh toán online, không tiền mặt · Không hoàn tiền, chỉ dời lịch · Mưa: phương án trong nhà, không tính thêm phí · snapsaigon.com | per group of up to 6 (+150,000 VND per extra person) · pay online, no cash · no refunds, postponement only · rain: indoor plan, no extra cost · snapsaigon.com |

- **Background:** a real, warm-graded photo of a released talent group at Nguyen Hue (from C01), darkened behind the table for legibility.
- **Layout B:** headline H23 over the same photo, with a single line under it: "≈ dưới USD 5/người khi đi 6 người / that's under USD 5 each when 6 of you share". The maths: 27.69 ÷ 6 = 4.62. It must keep "from" and the +150,000 VND line.
- **Primary text (caption), VN first:** "Quảng cáo · Thợ chụp ảnh địa phương ở Sài Gòn. Giá niêm yết, thanh toán online, có ảnh trong ngày với gói Postcard. / Sponsored · local photographers in saigon. listed prices, pay online, same-day photos with the postcard package."
- **Sound:** n/a.
- **CTA:** "Book now" → the package page that matches the ad they saw (congruence).
- **Compliance:** [PAID] [CMP].
  - Full Day shows its price only (its deliverables are "to confirm" on the site).
  - The "our top pick" site label is not used (it is close to a superlative).
  - The per-person maths is labelled approximate and tied to the "from" price.
  - If checkout adds fees or taxes, the headline "know the price" must include them [CONFIRM].

---
## Which preset/genre each draft uses (quick index)
| Draft | Format | Genre module | Editor preset | Aspect | Real footage? |
|---|---|---|---|---|---|
| C01 | drama skit | §2 comedy (D10) | deadpan-comedy | 9:16, 4:5 | actors + real snapper |
| C02 | scam-tip carousel | §22 news / scam-expose | news-expose (carousel-text kicker) | 4:5 | 1 street photo + icons |
| C03 | POV reel | §5 POV | ugc-pov | 9:16 | real snapper |
| C04 | process before/after | §26 before/after (process) | ugc-try-on-demo | 9:16, 4:5 | real only (hard rule) |
| C05 | texting scene | §30 texting | texting-suspense (chats[]) | 9:16 | actor + editor chats |
| C06 | multi-spot montage | §36 format + §4 rhythm | trend-beat-switch | 9:16 | real talent |
| C07 | snapper talking head | §21 explainer | talking-head-punchy | 9:16, 4:5 | real snapper |
| C08 | 6-spots carousel | info carousel | carousel-text (photo family) | 4:5 | real photos |
| C09 | rain static + 10 s | §9 feel-good accent | feelgood-emotional | 4:5, 9:16 | real (or labelled) |
| C10 | retargeting static | native static | photo-ad family | 1:1, 4:5 | real photo |
