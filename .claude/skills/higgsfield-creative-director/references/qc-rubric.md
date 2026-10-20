# QC rubric (score 0-2 each; any 0 in rows 1-4 = REGEN or FIX before delivery)
| # | Check | 0 = fail | 2 = pass |
|---|---|---|---|
| 1 | Set geography | People/objects jump positions vs set map; subject flipped | Matches set map in every frame |
| 2 | Camera owner / POV | POV ambiguous or switches mid-shot | Owner obvious; 180-degree line respected |
| 3 | Action logic | Physical action contradicts the line/joke | Action makes the line land |
| 4 | Identity continuity | Face/hair/build/wardrobe drift between shots | Same people throughout |
| 5 | Brand look | Grade/palette/wardrobe off brand file | On-brand |
| 6 | Timing & pacing | Line clipped, no reaction beat, hook > 1.5 s | Hook fast, line lands, reaction breathes |
| 7 | Audio & lip-sync | Missing/mismatched audio, wrong speaker | Correct speaker, synced, ambience present |
| 8 | Framing & safe zones (9:16) | Faces/text under top 14% or bottom 20% UI zones, or in right-edge button column | Key action in central safe area |
| 9 | Artifacts | Extra fingers, warped bar, morphing, flicker | Clean |
| 10 | Policy & claims | Moderation risk, unsupported health claim | Clean |

Report format per asset: `job_id | score /20 | PASS/FIX/REGEN | top issue | exact prompt delta`.
Use `scripts/qc_frames.py` for the contact sheet (frames at 5/35/65/95% + safe-zone overlay) and metadata (duration, fps, resolution, audio track present).

## Asset (Gate 4) checks
- Identity anchor shows full face, sharp, ≥ 25% of frame height, plus a three-quarter view → else REGEN (face cropped/hidden = automatic fail).
- Derived variant: same face, skin tone, proportions as base (side-by-side check) → else REGEN with base as reference.
- Wardrobe/colour matches script; no text/logos; natural skin texture.
- Location plate: every area used in the script visible + light source position clear.

## Story ethics check
- Does the edit reward cruelty (hype music, slow-mo swagger, laugh on the victim)? → FIX.
- Is the target's impact shown at least once? Is there a consequence or a clear cost? → else FIX.
