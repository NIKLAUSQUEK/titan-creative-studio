# AI video playbook: what works for marketing (Oct 2026)

This file complements `model-routing.md`, `prompt-patterns.md`, `realism.md`, `credit-saving.md` and `qc-rubric.md`. Where they conflict, the CLAUDE.md default stack and the ledger win. Researched 2026-10-25; sources are listed in `research/sources-agency-playbooks.md` §6. **[V]** marks a vendor claim.

## 0. Ten rules
1. **Lock the look before you animate.** Approve the style frame, character sheet and location plate first, then run image-to-video or reference-to-video. Google calls this "unparalleled control" (Veo 3.1 guide). It matters more than which model you pick.
2. **Write prompts as shot lists, not prose.** Label and time each shot, with one camera move and one subject action per shot. Veo, OpenAI, Kling and Higgsfield's Seedance 2.5 guide all converge on this.
3. **Default to Seedance 2.5** for long, multi-shot cinematic work: up to 30 s, up to 50 references, audio generated in the same pass. **Use Kling 3.0 for dialogue** (per-character voice binding, accents, EN/ZH/JA/KO/ES). **Kling 4.0** (launched 15 Oct 2026) needs a pilot before we rely on it.
4. **Draft at 480p.** Seedance 2.5 costs 30, 70 or 120 credits per 10 s at 480p, 720p or 1080p [V], so a draft round costs about a quarter of a final.
5. **Expect a low usable rate.** One Veo spot (Kalshi, Jun 2025) took about 300–400 generations to get 15 usable clips. Budget 5–10% usable on hard shots.
6. **Audiences notice AI and punish undisclosed AI.** Cint 2026: 74% of US consumers want disclosure, and 44% trust less when AI use is undisclosed. NIQ's EEG work found weaker memory activation even for high-quality AI ads. Use real staff and real product wherever trust matters.
7. **Disclosure is mandatory or default on every major platform** (Meta "AI info", TikTok's AI ad label, YouTube's revised labels). EU AI Act Art. 50 has applied since 2 Aug 2026.
8. **Never fake testimonials, patients, doctors or reviewers.** This is illegal under SG HCS Ads Reg 14, FTC 16 CFR 465 and UK CAP. Disclosing it as AI doesn't make a deceptive message legal (CAP, May 2025).
9. **Put AI inserts around real footage, not in place of it.** Use Genjutsu motion transfer from a phone reference, AI B-roll around real talking heads, and AI VFX on real packshots.
10. **QC every frame** (§7). Fix local errors with region edit, not a full re-render.

## 1. Models (as of Oct 2026; leaderboards disagree, so test on our own briefs)
| Model | Per pass | Strengths | Watch out | Use for |
|---|---|---|---|---|
| **Seedance 2.5** (ByteDance; on Higgsfield since Aug 2026) | 30 s, extendable; 480/720/1080p (4K is an upscale) | Up to 50 references, era/palette (hex)/lens/lighting selectors, region edit, Draw-to-Video, 3D scene builder, native ambience/foley/score | Likeness guardrails may block real-person uploads after the 2026 IP disputes. Dialogue lip-sync isn't documented on Higgsfield | **Hero model**: cinematic ads, product films, multi-shot narrative |
| **Kling 3.0** | 3–15 s, 720/1080p | Custom multi-shot with exact per-shot durations, Elements (look + voice), 3+ characters, dialogue syntax with tone and language | 15 s cap; about 12 credits/s at 1080p with audio | Dialogue skits, UGC-style talking, multilingual |
| Kling 4.0 | 30 s | Omni reference (15 assets, 10 keyframes) | 10 days old | Pilot on choreographed action |
| Veo 3.1 | 4/6/8 s | Strong native audio, first/last frame, ingredients, timestamp prompting, SynthID | 8 s cap | Dialogue close-ups, first-to-last-frame transitions |
| Gemini Omni Flash | ~10 s | Conversational multi-turn editing | Short | Iterative edits; the explainer pipeline |
| Wan 3.0 | 2–30 s | Strong on some leaderboards, cost-efficient | Closed API | Alternative if Higgsfield lists it |
| Sora 2 | — | The prompting guide is still useful | Consumer app closed Mar 2026; API reportedly retired | **Don't build pipelines on it** |

**Routing:**
- Over 15 s, cinematic or multi-shot: **Seedance 2.5 omni_reference**.
- On-camera lines: **Kling 3.0** with bound Elements, or Veo 3.1 for 8 s close-ups, or an ElevenLabs VO plus a lip-sync pass.
- Performance-critical moments: **Genjutsu**.
- Stills, sheets and plates: Nano Banana or GPT Image 2.5.
- Fast ad variants from a product URL: Marketing Studio.
- Non-photoreal narrated pieces: higgsfield-video-explainer.

## 2. Pre-production for AI (edit before you generate)
1. **Script and timed beat sheet.** Energetic spots run about 1.25–1.5 s per shot (Higgsfield examples).
2. **Shot list.** For each shot: size, lens field of view, height and move, action as counted beats, screen direction, audio cue, references used.
3. **Style frames.** 1–3 stills that fix grade, a 3–5 colour palette (hex), lens feel and era.
4. **Character sheets.** Use real staff photos first (Soul ID or Element from 2–4 images). For fiction, use an original character card, never a lookalike. Lock wardrobe.
5. **Location plates.** One wide plus 2–3 angles per location. Higgsfield: "a vague location is the most common reason a multi-shot sequence starts drifting."
6. **Animatic.** Cut the stills to scratch VO and music in the auto-editor and **lock timing**, so every generation has an exact duration.
7. **Previs.** For complex blocking, use Blender or Higgsfield 3D-jutsu to make guide frames to use as start frames.

**Consistency, strongest first:**
1. Reference-to-video or image-to-video beats text-to-video for identity. Caveat: image-to-video can look too clean and is easiest to spot as AI (UNIST: 79% detected). Add grain, imperfect light and handheld motion.
2. Give every shot a start frame, and an end frame when the move or pose matters. Chain shots by using the last good frame as the next start frame.
3. **State each reference's role in the prompt:** "@char identity + wardrobe locked; ignore the reference backdrop"; "use video ref for camera and pacing only".
4. Counts and invariants: "exactly four members", "exactly five fingers per hand", "turbulence only in shots 1–2".
5. Seeds are good for A/B prompt tests, but they don't lock identity across prompts.
6. Spell out the 180° rule and screen direction: "they never swap sides; camera stays north of the street", plus opening blocking ("x 42%, facing frame-left").

## 3. Prompt anatomy (merged from Google, OpenAI, Kling and Higgsfield)
```
[GLOBAL] aspect, total duration, shot count, era/stock, grade, palette (3-5 hex)
[REFS] @char = identity+wardrobe locked; @loc = set geography; @product = every detail per asset; ignore ref backgrounds
[FIRST FRAME / BLOCKING] who is where (screen %), facing, prop states
Shot 1 (0.0-2.5s): [size + lens FOV + height] [ONE camera move] - [subject] [ONE action as counted beats] - [light source + quality] - Hard cut
Shot 2 (…)
[PHYSICS] weight, cloth, liquid; no slow motion, no speed ramps, no ghosting
[CONSTRAINTS] exactly N people; five fingers per hand; text "BRAND" sharp and correctly spelled when visible; NOT 3D-render, NOT plastic CGI sheen
[AUDIO] ambience; SFX: …; Dialogue block (speaker labels, short lines)
```
- **Google's five parts:** cinematography + subject + action + context + style.
- **OpenAI:** one camera setup, one action and one lighting recipe per shot. Write actions as counted beats ("four steps to the window, pauses, pulls the curtain in the final second"). Describe light by source and quality.
- **Replace "cinematic" with concrete detail:** "wet asphalt, zebra crossing, neon in puddles".
- **Camera vocabulary that models follow:**
  - Sizes: ECU, CU, MCU, MS, WS, OTS, POV.
  - Moves: push-in, pull-back, tracking, orbit/arc, crane, pan, tilt, handheld, locked-off, drone.
  - Lens: rack focus, dolly zoom, Dutch angle, macro, shallow DOF, FOV numbers.
  - Never pair contradictory moves ("static" + "orbit"). For Kling single takes, write "one continuous long take without any cuts".
- **Performance:** describe the body, not the emotion label ("jaw tightens, eyes drop to the cup, half-second pause, small exhale"). Veo takes an `Emotion:` line; Kling takes `Name (tone, language): "line"`. **For comedy timing and reveals, film the talent on a phone and transfer the motion** rather than prompting the acting.
- **Avoid artifacts:**
  - Keep clips short (two 4 s clips beat one 8 s clip; keep 1.5–5 s per shot even on 30 s models).
  - Phrase negatives as positive states ("a landscape with no buildings").
  - Change one variable per iteration.
  - When a shot fails: freeze the camera, simplify the action and clear the background, then add complexity back.
  - Known failure zones: hands holding small objects, product text, crowds, fast spins, liquids, mirrors, people crossing paths.
- **Dialogue:** keep it in its own block, 1–2 short lines per 4 s. **Regulated claims go in approved ElevenLabs VO plus a lip-sync pass**, never generated. Native audio usually lacks Malay and Tamil, so dub those.
- **Length per beat:** hook 0–1.5 s · product beat 1–2 s · reaction 2–3 s · establishing 2–4 s · dialogue line 2–4 s · montage ~1.25 s per cut.

## 4. Hybrid workflows (where TITAN wins)
1. **Genjutsu motion transfer.** The source clip keeps its motion, camera, timing and audio; cast, location, wardrobe and style are rebuilt from references (3–30 s).
   - Shoot the reference on a tripod or with a deliberate handheld move, against a plain background, with real timing and line reads, in the storyboard framing.
2. **Real footage plus AI inserts.** Generate only what is impossible, expensive or unsafe (macro physics, exploded views, weather, period scenes, drone moves). Grade-match, add matched grain, and use the same lens FOV.
3. **AI B-roll around real talking heads.** Cut to it every 2–4 s; the editor's B-roll matcher (story-sync `broll-grammar.md`) handles this.
4. **Product VFX.** Use a real packshot as `@product`, described "per the asset when floating, touched, worn". **Composite the real logo and packshot in post**; never trust a generated logo.
5. **Upscale and interpolate last.** Lock the edit, re-render PASS shots at 1080p, then upscale the final. Interpolate only shots without fast limb motion.
6. **Sound after picture.** Native audio is fine for drafts. Finals get licensed or original music, ElevenLabs VO, SFX on cuts and a `/sound` plan.

## 5. AI ads that perform
- **No rigorous independent head-to-head data on AI vs human creators.** Anecdotes:
  - A dubbed avatar ad beat the human control by 31% on CPA in Brazil but failed in France and Germany (RevenueCat).
  - Human UGC still won on ROAS, and the winning AI hook did best when re-shot with a real face (Segwise [V]).
- **Rule: use AI for hook and variant volume, then move the winning hooks onto real faces.** Use AI for stylised spectacle and localisation.
- **Brand-scale AI can test well despite backlash.** Coca-Cola's 2025 AI holiday ad scored System1 5.9 amid criticism. McDonald's NL pulled its AI ad after "creepy" reactions.
- **Trust research:**
  - NIQ (2024): AI ads read as more annoying, boring and confusing, with weaker memory activation.
  - Cint (Oct 2026): 74% want disclosure; 44% trust less when it's undisclosed.
  - Learning about AI use *after* a purchase hurt trust more than disclosing it upfront.
  - Academic results are mixed: a Vietnam Gen-Z study found disclosure raised trust.
  - **Conclusion: disclose upfront and make the work good. Hiding AI is the worst option.**

**Slop signals and fixes:**

| Signal | Fix |
|---|---|
| Plastic, poreless skin | Real reference photos; "visible pores, fine vellus hair, uneven skin tone"; "NOT plastic CGI sheen"; grain in post |
| Uncanny eyes, frozen blinks | Motion transfer; medium shots, not ECUs; cut away sooner |
| Warped hands, morphing props | "Exactly five fingers"; simpler hand action; one prop state; region edit |
| Garbled text or logos | Composite in post; never generate claims as on-screen text |
| Generic stock look | Brand hex palette; real local plates (HDB void deck, kopitiam, MRT); imperfect light |
| Floaty physics, ramps, ghosting | A PHYSICS section in the prompt |
| Background doubles, crowd mush | Explicit people counts; shallow depth of field; empty locations |
| Mismatched room sound | Rebuild audio in post |

**Authenticity order:** real staff, product and (where legal) customers first → AI for world-building, B-roll, spectacle, variants and localisation → AI talent only for fictional characters, always disclosed.

**Hook testing:**
- Generate 5–10 variants of the first 1.5–3 s over one locked body.
- Cull after 48–72 h on thumb-stop and hold, then on CPA.

**Localisation:**
- Dub with consented voices.
- Regenerate culture-specific B-roll rather than just translating.
- Watch market sensitivity (the Brazil vs Europe result above).

## 6. Compliance (add to spec.json `hard_rules`)
- **Platforms.** Use Meta "AI info" and self-disclosure, TikTok's AI ad label (realistic people, voices, product shots), and YouTube's altered/synthetic declaration (health content gets a prominent badge). **Never strip C2PA, SynthID or other provenance metadata.**
- **Singapore:**
  - ASAS: same standards with or without AI; disclose where needed to avoid deception; consent for people and property; endorsements must be authentic.
  - HCS Ads Reg 14 makes an AI "patient" or "doctor" testimonial doubly prohibited.
  - The Online Safety (Relief and Accountability) Act 2025 is phasing in impersonation and deepfake takedown categories.
  - Copyright protects human-made works only; the MinLaw/IPOS consultation closed 22 Oct 2026.
- **US.** Prompts alone don't give authorship (USCO Part 2, Jan 2025). **Contracts must not promise exclusive copyright in raw generations**; the protectable layers are script, edit, composites, grade, original music and VO. FTC Part 465 bans AI fake reviews and testimonials.
- **UK CAP.** Would the audience be misled without disclosure? Does the disclosure clarify or contradict the message? Disclosure can't rescue a deceptive claim.
- **EU AI Act Art. 50.** Deployers must visibly label deepfakes; creative work can be labelled unobtrusively.
- **Likeness and voice.** Get signed releases (scope, media, term, territory, AI use, withdrawal). ElevenLabs' voice CAPTCHA proves a voice match, not legal rights.

**hard_rules lines to add:**
- Signed likeness/voice releases for every real person.
- No AI people presented as real customers, patients, clinicians or reviewers; no synthetic before/after.
- No real-person or IP lookalikes.
- Disclosure label set on every platform.
- Provenance metadata kept, plus a prompt/edit log as evidence of human authorship.
- Brand compliance pack applied to script, VO and captions.

## 7. Credits and QC
**Credits:**
- Iterate on stills first.
- Draft at 480p; turn native audio off in drafts if it will be replaced.
- Generate only the shots the animatic needs, at exact durations.
- Batch 3–5 prompts at a time and review between batches.
- Reuse Elements and Soul IDs.
- Use region edit or shot regenerate instead of full re-renders.
- Budget 3–4 takes per simple shot and 10+ for hands, product interaction and dialogue.
- Finals: re-render only PASS shots at 1080p, then upscale.

**QC rubric:** score each shot 0–2 and ship nothing with a zero. This extends `qc-rubric.md`.

| # | Check | Fails when |
|---|---|---|
| 1 | Identity | Drifts from the reference or between shots |
| 2 | Hands / anatomy | Wrong finger count, fused fingers, broken joints |
| 3 | Physics | Floating, sliding feet, impossible liquid or cloth, clipping |
| 4 | Text / logos | Misspelled, warped or flickering |
| 5 | Lip-sync | Visible offset; p/b/m mouth shapes wrong |
| 6 | Temporal stability | Flicker, boiling textures, morphing backgrounds, people appearing |
| 7 | Continuity | 180° flips, prop states change, lighting jumps |
| 8 | Brand look | Palette, grade or product accuracy off |
| 9 | Slop tells | Plastic skin, dead eyes, stock composition |
| 10 | Compliance | Claims, testimonials, consent, disclosure label |
| 11 | Master-spec fidelity | Staging, jokes, lines or CTA differ from version A |

Run `scripts/qc_frames.py`, view the contact sheet, then scrub at 25% speed for flicker and hands.

## 8. SOPs
**30 s AI ad**
1. Intake: ask "existing brief or final cut?"
2. Insight and promise; choose the format.
3. Script of ≤75 spoken words, 5 hook variants, compliance sign-off.
4. Shot list: 10–16 shots of 1.5–3 s.
5. Asset Bible (Gate 4) with real photos first.
6. 2–3 style frames.
7. Storyboard stills.
8. Animatic with locked timing.
9. `/sound` plan.
10. spec.json, `get_cost`, Klaus's approval.
11. Phone performance references → Genjutsu.
12. Drafts at 480p (Seedance; Kling for lines), 3–5 prompts per batch.
13. Rough cut + QC + regenerations; Klaus approves.
14. Finals: 1080p PASS shots, real logo composite, final VO/mix/captions, disclosure label, upscale, 9:16 + 1:1 + 16:9.
15. Publish with AI toggles set, run the hook test, `/review` at 7 days, then `/learn`.

**60 s AI short film**
1. Logline, theme and ending; confirm who carries each gag.
2. Story bible.
3. Three-act beat sheet (~10 / 35 / 15 s).
4. Minimal dialogue (2–4 s lines).
5. Character sheets (front, ¾, profile, expressions, wardrobe).
6. Location bible with the 180° line drawn.
7. Style key.
8. 20–30 shots with coverage.
9. 3D previs.
10. Animatic with temp score, then cut 10%.
11. Performance references.
12. Generate scene by scene, chaining last frame to first frame.
13. Continuity QC per scene.
14. Picture lock → sound design, score, VO/ADR, grade, grain, titles, AI label card.
15. Package with BTS showing the human authorship trail; `/learn`.

## 9. Shot templates (Seedance 2.5 / Kling)
Append to every template: `{aspect}, {era/stock}, palette {hex×3-5}, light film grain, NOT 3D-render, NOT plastic CGI sheen, exactly five fingers per hand.`

| # | Template | Core prompt |
|---|---|---|
| T1 | Product macro reveal (4 s) | Shot 1 0–2 s: ECU, 100 mm macro look, very shallow DOF, slow lateral slide across @product texture, single hard key top-left, background to black. Shot 2 2–4 s: slow push MCU → CU on the front face; it rotates exactly 30° clockwise and stops; label "{BRAND}" sharp and correctly spelled; no levitation or morphing. Audio: soft whoosh, tactile click at 3.5 s, no music |
| T2 | Talking-head UGC (8 s) | Single continuous take; MCU phone look, slight sway; @presenter locked in {real plate}, window light frame-left, warm practical behind; beats: looks into lens and raises brows → lifts @product to chest, label to camera → half-smile, one nod; visible pores; dialogue (casual, warm, Singapore English, ≤18 approved words); room tone. *Real staff preferred; if AI, label it; never framed as a customer testimonial* |
| T3 | Walk-and-talk (6 s) | Dolly back at walking pace ahead of @A (left) and @B (right); 35 mm MS two-shot; they never swap sides; @A speaks with one gesture → @B glances and laughs once; exactly two out-of-focus extras walking away; footsteps on tile |
| T4 | Reaction close-up (3 s) | Static CU, 85 mm, face fills 60% of frame, soft key frame-right; neutral, looking off-left → eyes widen slightly, breath catches → slow exhale, one-sided smile; natural blink; near silence. *Drive comedy timing with Genjutsu* |
| T5 | Fitness demo, no transformation (6 s) | Locked-off at hip height, 28 mm, bright daylight {plate}; @coach sets stance → exactly two slow controlled reps → stands, thumbs-up; no before/after, no body change, no text claims |
| T6 | Clinic calm establishing (5 s) | Slow push through the doorway of {real clinic plate}: empty room, morning light through blinds, plants, folded towels; no people, patients or signage text; dust motes; room tone, soft birdsong, one soft chime at 4 s |
| T7 | Comedic reveal (5 s) | Shot 1: MS static, @A hides {object} behind back, @B leans in; object fully hidden until Shot 2; hard cut. Shot 2: wider, same side of the line; reveal {gag object}; @B freezes deadpan, slow blink; tiny squeak, then 1 s silence. *Encode in hard_rules who carries the gag and what stays hidden* |
| T8 | Drone establishing (5 s) | Slow forward glide + tilt-down from high over {SG location at dawn} to {target} centred; 24 mm, haze, warm first light on rooftops; realistic slow traffic; straight verticals; wind, city hum, rising pad |
| T9 | Match-cut transition (4 s) | Start frame @frameA (circle) → end frame @frameB (matching circle); locked top-down slow push; alignment at 2 s holding exact size and position; constant speed; whoosh peaking at 2 s |
| T10 | Kinetic-type background plate (4 s) | Background only: slow orbit around @product on a {brand hex} seamless, softbox key, rim light, empty right third; **no text, letters or logos**. Type and claims are added in post (human-set, compliance-checked) |
