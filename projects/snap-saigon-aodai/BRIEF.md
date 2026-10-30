# Snap Saigon: áo dài try-on + "market Saigon" workflow (draft, not approved)

- **Workflow:** `.claude/skills/higgsfield-creative-director/references/cultural-wear-tryon.md` (áo dài module).
- **Sights:** `.claude/skills/higgsfield-creative-director/references/locations-hcmc.md`.
- **Brand:** `brands/snap-saigon.md` (ad rules §2 and §9 apply). **Cast:** `cast/snap-saigon-influencer.md` (Hân, Khang, Ben locked).
- **Goal:** people see themselves in an áo dài at real Saigon sights, then book a snapper shoot, with an áo dài rental partner as an optional extra.
- **Platforms:** IG and FB (4:5 and carousel), Reels and TikTok (9:16), DM previews (1:1).

## What it is
1. **For customers (the product):**
   - A lead sends a selfie and a full-body photo.
   - They get 3 private previews in their chosen áo dài at 3 sights.
   - Then they book a shoot. A partner rental is optional and labelled.
   - Previews are a style and colour preview, not a size fit. Sizing comes from the partner's chart.
2. **For marketing (the reach):** brand characters and real shoots show off áo dài at Saigon's landmarks, with true culture cues. The formats are listed in the workflow module: transformation reel, spots carousel, "áo dài or qipao?", "wear it like a local", seasonal drops.

## Pilot shot list (proves the look before any customer sees it)
| # | Who | Garment | Sight (real plate) | Aspect | Use |
|---|---|---|---|---|---|
| P1 | **Ben** (locked) | áo dài nam, navy silk, black khăn đóng | Central Post Office façade, LEFT third of frame, three-quarter turn | 4:5 | transformation reel end frame + carousel slide |
| P2 | **Hân** (locked) | yellow #FFC727 cách tân with white wide trousers, digicam in hand | Nguyễn Huệ, City Hall end, blue hour | 9:16 | Story / Reel cover |
| P3 | **Klaus** (his own photos, his yes) | áo dài nam, cream brocade | Ben Thanh south-gate clock tower | 4:5 | first real-person identity test (the customer flow) |
| P4 | **Mia + Jay** (EP 1 couple; sheets from EP 1 Stage 1) | matching red silk áo dài + áo dài nam | Opera House steps (avoids the cathedral scaffolding) | 4:5 | EP 2 tease: "Photos of Us" finally get their photo |
| M1 | Ben | from P1 | spin from backpacker outfit into the áo dài (start frame = Ben's sheet, end frame = P1) | 9:16, 5 s | transformation reel |
| M2 | Mia + Jay | from P4 | slow walk down the steps, front panels lifting in the breeze | 9:16, 5 s | EP 2 tease |

## Order of work (cost-gated; quote before each stage)
Quotes read on 2026-10-30:
- `nano_banana_2` 1k: 1.5 cr per image.
- `gpt_image_2` low 1k: 0.5-1 cr.
- `seedance_2_5` 480p 5 s: 15 cr.
- Balance: 361.66 cr. This is not the ~868 assumed earlier.

| Stage | What | Cost |
|---|---|---|
| 0 | Hân character sheet (`nano_banana_2` 1k). Ben, Mia and Jay sheets come from EP 1 Stage 1. Klaus sends 1 face photo and 1 full-body photo | 1.5 cr |
| 1 | 3 garment references (navy men's with khăn đóng; yellow cách tân; red couple set). 0 cr if the rental partner sends product photos | ≈3 cr |
| 2 | 4 location plates from real photos (`editor.py web-images`, licensed, credits kept) | 0 cr |
| 3 | P1-P4 draft stills (`nano_banana_2` 1k), QC, max one regen each | 6 cr (12 worst case) |
| 4 | M1-M2 Seedance 2.5 480p drafts, `qc_frames.py` | 30 cr |
| 5 | Edit: transformation reel + "6 spots made for áo dài" carousel + "áo dài or qipao?" carousel; `/sound` VN plan | 0 cr |
| | **Pilot total** | **≈40.5 cr, cap 55** |

Then: Klaus approves the drafts. Finals (stills at `nano_banana_pro` 2k, video 1080p) are quoted separately.

## Customer DM flow (after the pilot passes)
1. Lead DMs "ÁO DÀI" (comment-to-DM).
2. Reply with the consent text (`CONSENT.md`). Proceed only after a "yes".
3. Collect the inputs: face, full body, style, colour, 3 sights from the six Snap Saigon spots.
4. Generate 3 drafts (`nano_banana_2` 1k, about 4.5 cr per lead) and QC them.
5. Send them privately, with "preview of style and colour; real fit is measured at the rental" and the booking link.
6. Delete the source photos and previews 30 days after the shoot. Log only the lead ID.

**Cost watch:** at about 4.5 cr per lead, 50 leads use 225 cr. Cap leads per week, or move to the partner's own kiosk photos.

## Hard rules (copied into spec.json)
- The garment passes the áo dài must-have list (collar, waist-high slits, trousers, right-side buttons). A qipao look is an automatic regen.
- No slimming, skin lightening or beautifying of anyone, ever.
- Landmarks come only from real plates. No invented signage or text in generation; all text goes in post.
- Religious sites: modest poses, outside the gates only. No state symbols as props. No posts on remembrance dates.
- Customer images are private previews only, unless there is a separate written ad opt-in.
- Paid creative: Vietnamese headline first; partner rental labelled "Quảng cáo / Sponsored".
