# Playbook - carousel (IG 4:5 1080x1350, or TikTok photo mode 9:16)
Quick spec. Full playbook (16 archetypes, hook/re-hook, swipe devices, type sizes, ad statics, covers, QC, blueprints): `.claude/skills/marketing-engine/references/carousels-statics.md`.
1. Narrative arc: Slide 1 hook (problem/claim, <=8 words) -> Slide 2 second hook/curiosity -> 3..N-2 value (one idea per slide) -> N-1 payoff -> N CTA.
2. Design system FIRST (from brand file): grid (margins 80 px, 12-col), type scale (H1 72-96 px, body 36-44 px), 2 fonts max, palette hexes, one visual motif repeated every slide, slide number + handle position fixed.
3. Generate imagery WITHOUT text (gpt_image_2_5 / nano_banana_pro, same seed/refs for consistency), then set type deterministically in post (HTML/Canva/Figma template) - AI-rendered text drifts slide to slide.
4. If text must be generated, gpt_image_2_5 quality high, exact strings in quotes, font described, 4:5.
5. QC: same style across slides (contact sheet), legibility at phone size, safe zones, claim accuracy.
