# Cultural-wear try-on: "see yourself in it" previews

Use for: "show me / my customer in an áo dài", "how would I look in a hanbok / kimono / sari / baju kurung", fit previews before a rental or a shoot, and marketing that shows off a culture's dress at its landmarks.
Works for any brand. The first module (below) is áo dài × Ho Chi Minh City; add a module per garment × city.
Locations come from a sight library (HCMC: `locations-hcmc.md`).

## The honest promise
- A try-on is a **style and colour preview, not a size fit.** The model cannot know the person's measurements, so the copy says "preview" or "see yourself in…", never "your perfect fit".
- Real fit comes from the rental or tailor partner's size chart (height, bust, waist, hip).
- This keeps the hook and stays truthful, so it needs no AI label (ledger 2026-10-28: no AI labels; use the platform toggle only where required).
- Real shoot photos stay real. A preview is never posted as a "photo from our shoot".

## People: who can be previewed
| Subject | Allowed | Gate |
|---|---|---|
| Brand characters (e.g. Hân, Khang, Ben) | yes | character sheet approved (Gate 4) |
| Klaus / staff / snappers | yes | their own yes; best first real test |
| Customers / leads | yes, private preview only | written consent first (`projects/<p>/CONSENT.md` text); adults only; minors only with a parent's consent and never in marketing |
| Customer preview used in an ad or post | only with a separate written **ad opt-in** | VN Civil Code Art. 32 (image consent), Personal Data Protection Law 91/2025 [verify whether face photos count as sensitive data] |
| Real public figures, celebrities, lookalikes | never | hard line |

- Data handling: delete customer source photos and previews 30 days after the shoot (or sooner on request). Never put customer photos in git; keep them in `%LOCALAPPDATA%` or the Higgsfield workspace. Log only an anonymous ID in `registry/generations.csv`.
- **Never** slim, reshape, whiten or "beautify" a real person. Skin tone, body shape, face and hair stay exactly as photographed. In VN beauty-filter culture this is the line people cross most, and it is also the line that makes previews dishonest.

## Inputs (collect before any credit is spent)
1. **Face photo:** front-facing, even light, no sunglasses, face at least 1/4 of the frame.
2. **Full-body photo:** standing straight, fitted clothes, feet visible. It anchors proportions and height.
3. **Garment reference:**
   - Best: the partner's real product photo (flat lay or on a mannequin), with the exact colour and fabric.
   - Fallback: a generated garment reference approved at Gate 4.
4. **Location plate:** a real photo of the sight from our own shoots or a licensed source (`editor.py web-images`: Openverse or Wikimedia, credit kept).
   - Generated landmarks drift (wrong spires, wrong colours), so landmarks are never invented.
   - If no real plate exists, use a generic street or setting and do not name a landmark.
5. **Choices:** style (classic, cách tân, groom/bride, men's), colour, sight, time of day, aspect ratio (4:5 feed, 9:16 Reels/Stories, 1:1 DM).

## Stages (cost-gated, cheapest first; quote before each stage)
| # | Stage | Model / tool | Cheapest setting (quoted 2026-10-30) | Gate |
|---|---|---|---|---|
| 0 | Consent + inputs | DM / form | 0 cr | consent text returned |
| 1 | Garment reference (only if no real product photo) | `gpt_image_2` low 1k or `nano_banana_2` 1k | 0.5-1 cr / 1.5 cr | garment accuracy QC (below), Klaus approves |
| 2 | Location plate | real photo, editor `web-images` | 0 cr | landmark accuracy QC |
| 3 | Try-on draft still | `nano_banana_2` 1k, image refs: 1 person, 2 garment, 3 plate | 1.5 cr per image | identity + garment + place QC; one regen max |
| 4 | Final still | `nano_banana_pro` 2k with the approved draft as image 1 | quote at the time | Klaus approves the draft first |
| 5 | Motion (optional) | `seedance_2_5` image-to-video 480p, 5 s | 15 cr | `scripts/qc_frames.py` contact sheet; 1080p only after approval |
| 6 | Edit | editor carousel / reel + `/sound` | 0 cr | `/qc` |

Alternates when the default drifts on identity: `kling_omni_image` 1k or `nano_banana_2_1` 1k (both take image references; quote first).
Watch the model field in `jobs_wait`: Pro jobs have come back labelled `nano_banana_2` before (ledger 2026-10-10).

## Prompt template (one change per pass; image order = upload order)
```
Image 1 is the person. Keep their face, facial features, skin tone, body shape, height, hairstyle and expression exactly
as in image 1. Do not slim, lighten, smooth or beautify. Dress them in the garment from image 2: [GARMENT LOCK from the
module]. Place them in the location from image 3, [POSE + POSITION: e.g. standing on the LEFT third of frame, three-quarter
turn toward camera, right hand lightly holding the front panel]. [LIGHT: soft late-afternoon sun from the right]. Keep the
building in image 3 exactly as it is. Photorealistic photo, natural skin texture, true fabric folds and sheen,
[ASPECT], upright vertical photo, ground along the bottom edge. No text, no logos, no extra people in focus.
```
- Garment fails: regenerate with the failed image as image 1, plus "recreate exactly with ONE change: [the fix]".
- Face drifts: "the face changed; keep the face exactly as in image 1 and redo" (photo-effects.md).

## QC checklist (score every image; any ✗ on identity or garment = REGEN, once)
- **Identity:**
  - same face shape, eyes, nose, jaw and skin tone as the photo;
  - no slimming, whitening or added makeup beyond the brief;
  - hands with 5 fingers.
- **Garment:** the module's must-have list passes (below), the colour matches the reference, and the fabric looks real.
- **Place:**
  - the landmark matches the plate (windows, spires, colours);
  - no invented signage or fake text;
  - no garbled Vietnamese diacritics anywhere: all text goes in post.
- **Respect:**
  - modest at religious sites;
  - no flags, state symbols or political banners as props;
  - the garment is not sexualised in organic brand posts. The romance rules in the ledger still apply to adult original characters, but never at religious or remembrance sites.

---

## Module: ÁO DÀI × HCMC

### Garment lock (paste into the prompt)
- **Women's classic:** a Vietnamese áo dài:
  - long fitted silk tunic;
  - high mandarin collar (cổ đứng);
  - raglan sleeves to the wrist;
  - side slits (xẻ tà) opening from the waist down into a long front panel and back panel that reach the shins;
  - a row of small snap buttons running from the collar across to the right underarm and down the right side;
  - worn over loose, wide-leg, floor-length satin trousers (quần) in [white / matching colour].
- **Cách tân (modern):** knee-length, looser tunic, shorter sleeves allowed, worn over wide trousers or a flowing skirt. Same collar and side slits.
- **Men's:** áo dài nam:
  - straighter, looser cut, knee to shin length;
  - mandarin collar, side slits, worn over straight trousers.
  - Formal or wedding: add a khăn đóng (round wrapped headband-turban) in a matching or black colour.
- **Wedding:** red or gold áo dài with a khăn vấn / khăn mấn headdress (a round ring) and brocade (gấm) patterns.
- **Accessories:** nón lá (conical palm-leaf hat), a small fan, a hand-held tà (front panel lifted while walking). Keep to one accessory per image.
- **Fabrics:** silk (lụa), brocade (gấm), chiffon or organza (voan) overlay, velvet (nhung) for cool-season looks.

### Must-haves (garment QC)
- [ ] mandarin collar
- [ ] side slits that start at the waist, not the thigh
- [ ] trousers visible under the slits
- [ ] front and back panels long and separate
- [ ] raglan sleeve line
- [ ] buttons on the right side, not down the centre of the chest

### Never (the common AI mistakes; reject on sight)
- **Qipao or cheongsam instead:** a one-piece dress with no trousers, a thigh-high slit, frog buttons across the chest, or Chinese dragon-phoenix embroidery with Hanzi.
- Kimono or hanbok features: obi belt, wrap front, a jeogori-length top.
- Bare legs under the slits.
- Chinese New Year red lanterns with Chinese characters as "Vietnamese" decor in HCMC. Hội An-style silk lanterns are fine.
- **White áo dài on adults styled like a schoolgirl:** white is the southern high-school uniform. Fine on adults for elegance, but no school props (satchels, bicycles plus a uniform look), never in a romance or sensual post, and every character is clearly an adult.

### Colour cues (for marketing copy and choices)
- **Red / gold:** Tết, weddings, luck.
- **Yellow:** imperial Huế heritage. Also Snap Saigon's accent #FFC727, a good brand tie-in.
- **Purple:** Huế romance (with a nón bài thơ, a poem hat).
- **Pastels and florals:** spring and everyday.
- **White:** purity, youth, graduation.
- **Áo dài nam with khăn đóng:** weddings and Tết visits.

[verify each cue with a local stylist or the rental partner before it goes in copy]

### When áo dài is everywhere (content calendar hooks)
Dates [verify yearly]:
- **Tết:** Lunar New Year 2027 ≈ 6 Feb 2027. Nguyễn Huệ flower street runs for Tết.
- **8/3:** International Women's Day.
- **HCMC áo dài festival:** usually spring.
- **Mid-Autumn:** Lương Nhữ Học lantern street (Chợ Lớn).
- **20/10:** Vietnamese Women's Day.
- **Christmas:** at the cathedral.
- **New Year countdown:** on Nguyễn Huệ.

**Not on remembrance dates** (ledger 2026-10-28): no try-on, booking or glam posts on 30/4, 27/7, 10/8, 2/9 or 7/5.

### Marketing formats (organic first; paid only with the brand's ad rules)
1. **"See yourself in an áo dài before you land"**: the DM lead magnet.
   - Send a selfie and a full-body photo, then get 3 free previews at 3 Saigon sights.
   - Then book the shoot, with an optional áo dài rental from the partner.
   - "Free" is truthful only if it truly costs the lead nothing; keep the same wording in ads.
2. **Hook-ladder Reel, the transformation:**
   - Ben in his backpack outfit, a spin, then áo dài nam and khăn đóng outside the post office.
   - Hân: "wait, film this." Ben: "sorry, is this… normal?"
   - Then real snapper footage and the offer card. Seedance 480p for the spin; the drop is real footage.
3. **Carousel "6 Saigon spots that were made for áo dài":** real shoot photos plus one tip per slide (best light, crowd time, what to wear). Sights from `locations-hcmc.md`.
4. **Educational carousel "Áo dài or qipao? 5 ways to tell":** collar, slit height, trousers, buttons, history. Saves and shares, and respect for the culture.
5. **"How to wear an áo dài like a local":** sitting (lift the back panel), walking (hold the front panel), stairs, motorbike side-saddle (only as a passenger and safe), shoes, the nón lá angle, and what not to wear at temples.
6. **Couple or friends previews:** two people in matching colours. One consent per person.
7. **Seasonal drops:** a Tết red-gold set at the Nguyễn Huệ flower street (real plate shot that week), Mid-Autumn lanterns, 8/3 and 20/10 tributes (no booking push on 20/10 morning posts; tribute first, offer in the comments).
8. **Trial reels:** `/expand` the transformation reel: hook, colour, sight, length.

### Brand rules that bite (Snap Saigon; check the brand file each time)
- **Paid ads:**
  - Vietnamese headline first, English below at no more than 3/4 size.
  - Partner (rental shop) features are labelled "Quảng cáo / Sponsored" plus the paid-partnership tag.
  - Prices exactly as on the live site.
  - No "best", "#1", "official" or "tour".
- Customer previews or shoot photos in ads only with a written ad opt-in.
- Independence Palace: VND 500k per camera fee from 1 Aug 2026. Leave it off sample shots unless the fee is priced in.
