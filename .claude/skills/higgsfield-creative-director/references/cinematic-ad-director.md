# Cinematic Ad / Story Director flow (default for ads, story-led shorts, skits)
Three gates. Never skip a gate; never render before Gate 3 is approved.

## GATE 1 — Brief intake (ask only what's missing; tappable options, max 3 per round)
Required fields → echo back as "Your creative brief":
- **Brand / client** (brand file applies) · **Audience** (who + where + segment) · **Service/product**
- **Desired result** (what the customer wants to feel/look/get) · **Concerns/objections** (top 2-3)
- **Proof available** (real photos/videos/reviews/results — "we'll use actual material once supplied")
- **Offer & CTA** (exact channel: WhatsApp/DM/link/booking; number goes in caption/button unless told otherwise)
- **Format** (length, aspect, platform, visible speakers?, on-screen text yes/no, VO yes/no, language/accent)
- **Funnel stage** TOFU / MOFU / BOFU (or "give me a spread")
- **Mood range** wanted or banned (warm, dark, sad, humour, tense, aspirational, absurd)
- **Real people / real events?** yes → fact-check layer + SOURCES.md (references/commentary-controversy.md); no AI likeness of real people
- **Mature/edge settings** (references/mature-edge.md): 18+ gate, profanity dial 0-3, placement (paid / organic / age-gated), edge level (spicy / dark / absurd / rage)
- **Market/locale** (loads references/localisation.md pack: settings, language, humour, sound, compliance)
- **Voice & sound**: commentary persona (see references/voice-persona-audio.md — archetypes only), sound energy (stim-heavy / balanced / clean), target community for humour
- **Constraints**: claims we can't make (prices, discounts, medical outcomes), must-include, must-avoid
Close the brief with a compliance line, e.g. "Budget is handled through the consultation/quote, without claiming prices or discounts not confirmed."

## GATE 2 — Five story directions
First show a one-line **diversity matrix** so the 5 are genuinely different (vary ≥2 axes each):
| # | Funnel | Angle | Vibe | Format | Segment |
Axes (also: Decision-Ladder cautionary arc, raunch/innuendo, Japanese mode, rage-hook — see mature-edge.md): Funnel (TOFU hook/entertain · MOFU objection/demo/proof · BOFU offer/testimonial/urgency) · Angle (identity, convenience, budget, social proof, fear/objection, status, transformation, humour-relief) · Vibe (warm, dark, sad, humour, tense, aspirational, absurd, nostalgic) · Format (single speaker, duo dialogue, trio, skit, POV, UGC testimonial, founder-led, mini-film, montage) · Segment (sub-audience: first-timers, budget-conscious, luxury, diaspora, etc.)

Each direction card (all fields, in this order):
1. **"Title"** (+ "— Recommended" on exactly one, with why)
2. **Conversion angle**
3. **First-second visual hook** (what the eye sees in frame 1)
4. **Spoken hook** (first line, exact words)
5. **Premise** (the story in 2-4 sentences, incl. the payoff line)
6. **Audience insight / sales hypothesis** (why this converts)
7. **Emotional journey** (A → B → C)
8. **Visual signature** (lens/light/texture that makes it recognisable)
9. **Pattern interrupt / hero camera moment**
10. **Offer reveal / persuasion**
11. **Objection / proof opportunity** (which real proof slots in, with permission)
12. **Ending / CTA** (exact closing line)
13. **What it tests / best platform**
Write it like a director pitching: say what you're trying to make the viewer feel and why each choice (hook, interrupt, reveal) earns retention. Then ask: "Pick 1-5, or mix (e.g. hook of 2 + ending of 4)."

## GATE 3 — Production script for the chosen direction
1. **STORY N: "TITLE"** — Brand — length + format · 2-sentence logline · what the transformation/scene represents (and what it does NOT promise).
2. **Proposed creative decisions for approval**: cast (count, age, look, ethnicity per brief), location, wardrobe colour logic, props, language/accent, VO/no VO, on-screen text yes/no.
3. **Second-by-second table**:
| Time | Visuals & performance (shot size, lens, camera move, action, emotion, reaction-face archetype, edit/transition in) | Exact dialogue & delivery (SPEAKER/persona, line, delivery note) | Audio stim / music cue |
Rules: each spoken shot ≥ words/2.5 s + 0.8 s; one camera owner per shot; mark "Visual-only beat" explicitly; hero reveal shows emotion BEFORE the full look.
4. **Look**: lenses (50 mm dialogue, 85 mm hero, macro details), lighting motivation, grade palette, skin-tone fidelity rule.
5. **Edit rhythm**: where it's fast vs smooth, match cuts, opening impact, what is NOT used (slow-mo, VFX…).
6. **Music & SFX**: genre, level under speech, where it lifts, banned effects.
7. **Speaker & timing locks**: who speaks which lines only; visible mouth on every line; total duration exact; total word count (≈2.1 words/s for 30 s ≈ 60-65 words).
8. **Contact/CTA treatment**: spoken CTA names the channel; number/link in caption or CTA button unless on-screen text is allowed.
9. **Compliance notes**: claims avoided, proof needing permission.
10. **Model plan & cost**: per shot → model, mode, references, duration, draft/final, est. credits (get_cost). Then the normal spec.json → validate → approval → draft → QC loop.

## Default model stack for cinematic ads (override only with a stated reason)
- **Seedance 2.5** `mode: omni_reference`: cast stills (nano_banana_pro 2k character sheets / Soul for real people) + set plate as image_references; generate_audio for native dialogue; 4-30 s; **draft:true (480p) → finalize via draft_job_id at 1080p, bitrate_mode: high**.
- **Genjutsu** (`hf_mult_motion_control`): for performance-critical shots (subtle emotion, exact gestures, lip timing) — Klaus or an actor films the shot on a phone → reference video + cast image → AI cast performs it. Strongest human-realism lever. 1080p.
- **4K**: upscale the locked final cut (upscale_video / topaz) — no model renders native 4K here.
- Switch to: Kling 3.0 (single-shot dialogue, cheaper std drafts), Cinema Studio 4.0 (lens/camera-body control for hero shots), Marketing Studio/Ads Studio (product-catalogue ads).
- Known limits (ledger): kling_o3 multi-shot fails silently; one framing reference per framing; vertical plates must state "upright vertical, floor at bottom".

## 30-second funnel templates
- TOFU: 0-2 hook (visual + line) · 2-8 tension · 8-20 escalation/pattern interrupt · 20-26 payoff · 26-30 soft CTA
- MOFU: 0-3 objection voiced · 3-10 empathy/explanation · 10-20 demo/proof · 20-26 result reveal · 26-30 CTA
- BOFU: 0-3 result/testimonial first · 3-12 offer + why now · 12-24 proof stack · 24-30 direct CTA (channel named)

## GATE 4 — Asset Bible + visual confirmation (after script approval, before ANY video)
Principle: **real photos beat generated ones.** Ask first: "Do you have real photos of the talent / staff / location / product?" Real staff who represent the business (e.g. the actual stylist, Physio Niklaus) must use real photos or their Soul — never a fictional stand-in unless Klaus says so. Generate only missing fictional talent or sets.

For every recurring element create an asset card with an `@UPPER_SNAKE` handle:
- **@HANDLE — role** (e.g. @BRIDE_PREP — Bride before styling)
- **Description**: age band, ethnicity/region per brief, build, skin texture, hair, wardrobe (colour logic from the script), expression/energy.
- **Identity lock**: what must stay identical across every shot (face, skin tone, body proportions, layout + lighting for locations).
- **Derived from** (variants only): "Use @BASE as the exact identity reference" — e.g. @BRIDE_FINISHED from @BRIDE_PREP: same face/skin/proportions, only makeup/hair/outfit/accessories change.
- **Useful framing**: characters → waist-up, face clearly visible, plus three-quarter view (hands visible if they act with hands); locations → wide view showing every area used + window/light source position.
- **Used**: which scenes/timestamps.
- **Source**: REAL (upload) | SOUL (real person) | GENERATED.
- **Prompt** (copy-ready plain text block): photoreal, natural skin texture/pores, no beauty filter, exact wardrobe, neutral or in-set background, model + aspect + resolution (default nano_banana_pro 2k; variants pass the base image as image_reference).
- **Status**: draft → approved (with Higgsfield job id / Element id).

Asset types to cover: every speaking character, every look-variant (before/after, outfit change), the shared location(s) as a set plate, hero props/products, brand-critical wardrobe.

### Asset-by-asset handoff (default rhythm)
Generate in dependency order: base identities → derived variants → supporting cast → locations → props. After EACH asset:
1. Show the image(s).
2. One confirmation line stating what is now locked and who inherits it, e.g. "Created @BRIDE_PREP. We'll preserve her face, skin tone and body proportions for @BRIDE_FINISHED."
3. QC verdict in one line (PASS / FIX + reason). **Identity anchors FAIL if the face is cropped, obscured or tiny** — a wardrobe-only crop cannot lock identity; require waist-up with the full face plus a three-quarter view.
4. Quick approve / fix-this option for Klaus, then move to the next asset. (Batch mode is available when Klaus says "do them all", but approval is still per asset.)

### Visual confirmation loop
1. Batch-generate all draft assets cheaply (generate_image_batch, ~2 credits each), base identities first, then derived variants using the approved base as reference.
2. QC each (identity consistency base↔variant, wardrobe matches script, realism/skin, framing usable, ethnicity/age per brief, no text/logos).
3. Show one gallery; Klaus approves per asset (multi-select). Rejected → regenerate with the exact delta, never silently.
4. Lock: write `projects/<p>/assets.json` {handle: {source, image_job_ids, element_id?, approved:true}}; for recurring talent create a Higgsfield Element; add to cast/registry.md.
5. Only then Gate 5.

## GATE 5 — Shot rendering
Each spec shot lists `uses: ["@BRIDE_PREP", "@FLAWLESS_BRIDAL_STUDIO"]`; those approved images go in as Seedance 2.5 `image_references` (≤4 per shot, character first, location last) and the prompt names them in that order ("the woman in image 1… the studio in image 2"). The validator refuses any shot using an unapproved or missing handle.
