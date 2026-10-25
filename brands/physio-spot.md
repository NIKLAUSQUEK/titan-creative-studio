# Physio Spot - brand look file (source of truth: references/physio-spot-ad-brief-v4.md)
- What: Nik's men's health physiotherapy clinic brand: erectile dysfunction, premature ejaculation, pelvic pain, prostate conditions.
- Ad formula: deadpan gym comedy -> humiliating reveal (crash zoom + impact + silence + laugh) -> hard cut to black -> calm premium clinic ending with Nik.
- Ending look: navy scrubs (no logos), warm beige minimalist room, single bare Edison bulb, bulb-flicker in, slow push-in.
- Type: Cormorant Garamond Italic (conditions, tagline), Playfair Display Italic ("Physio Spot"), panel #EFE3D3 @88%, text #4E3B2E / #6B5544. Never clinical red.
- Captions: DejaVu Sans Bold 46 px, white, 4 px black border, centred at 74% height, on the spoken word, key word CAPS.
- Nik: Soul "Nik" soul_id 1e8acf3a-cd75-43a0-ac2b-e97706906d2c (retrain planned with better photos -> references/soul-training.md).
- Voices: friend = ElevenLabs "Benji" via voice_change (e6f9b893-51b1-51d3-afe9-9e0482cb7ac1); buff guy = Kling native deep voice. "Dylan" rejected.
- Signature line: "Once you spot it, come to Physio Spot ... Don't wait till it's too late."
- SECTION 7 OF THE BRIEF (Dramatisation system) IS A STANDING RULE FOR EVERY AD.
- COMPLIANCE (Singapore health advertising): no testimonials/endorsements/patient photos reproduced in ads, no paid reviews, no superlatives (best/leading/No.1/most trusted), no free-consult or discount inducements, claims must be substantiable (HCS (Advertisement) Regulations 2021 Reg 14 + professional codes — confirm which apply with counsel). Dramatised skits must not pose as real patient testimony.

## 6b. Edit guide (machine-readable, read by tools/editor; sizes are fractions of frame height)
Captions and hook placement follow ledger 2026-10-10 (hook text never covers faces; hook just above the 74% captions).
```edit-brand
{
  "colors": {"primary": "#EFE3D3", "accent": "#6B5544", "text": "#4E3B2E"},
  "fonts": {"display": "Playfair Display", "body": "Cormorant Garamond"},
  "captions": {"font": "DejaVu Sans", "bold": true, "size": 0.024, "color": "#FFFFFF", "outline": 4, "outline_color": "#000000", "position_y": 0.74, "highlight": "#EFE3D3"},
  "hook_text": {"font": "DejaVu Sans", "bold": true, "size": 0.031, "position_y": 0.615, "uppercase": true},
  "end_card": {"enabled": true, "dur_s": 2.5, "bg": "#EFE3D3", "font": "Playfair Display", "color": "#4E3B2E", "sub_font": "Cormorant Garamond", "sub_color": "#6B5544"},
  "grade": {"warmth": 0.03},
  "cards": {"look": "editorial", "bg": "#EFE3D3", "panel": "#F8F1E7", "text": "#3E2F24", "muted": "#7A6656", "accent": "#6B5544", "marker": "#DCC5A8"},
  "compliance": {"forbid_words": ["best", "leading", "no.1", "#1", "most trusted", "guaranteed", "cure", "free consult", "discount"]}
}
```
