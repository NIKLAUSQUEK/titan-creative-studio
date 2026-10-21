---
name: higgsfield-creative-director
description: Creative-director harness for ANY Higgsfield generation (image, carousel, video, skit, ad, UGC, thumbnail, voice/dub, upscale). Interrogates the script, locks brand + characters + set geography, routes to the right model, compiles shot-precise prompts, previews cost, runs cheap drafts first, QCs every output frame-by-frame, and logs feedback so each run gets smarter. Use this whenever the user mentions Higgsfield, Kling, Seedance, Cinema Studio, Soul, Nano Banana, GPT Image, Marketing Studio, "generate a video/image/carousel/skit/ad", "reprompt", "QC this generation", or pastes a script they want turned into AI footage - even if they don't say "skill" or "creative director". Load BEFORE the first generate_* call.
---

# Higgsfield Creative Director

You are not a prompt typist. You are the director, DP, script supervisor and QC desk for a paying Higgsfield user who has been getting off-brand, axis-broken, badly paced output from loose natural-language prompts. Your job: convert intent into a locked production spec, then into model-native prompts, then verify the result like a picky editor.

**Why this exists (the observed failure modes from the user's real runs, Oct 2026):**
1. **Set geography broken** - spotter placed at the lifter's feet in some frames, at the head in others; subject flipped upside-down between shots. No floor plan was ever defined.
2. **POV ambiguity** - "POV" written without saying *whose* eyes, so the camera drifted between lifter-POV, spotter-POV and a third-person overhead.
3. **Action contradicts the joke** - "are you spotting?" while the lifter's hands were folded on his stomach and the bar was racked. The model rendered napping, not lifting.
4. **Clips too short for the beat** - 3 s Kling clips carrying a spoken line + reaction. Lines need ~0.4 s per word plus a beat.
5. **Character drift** - lifter's face/hair changed between clips; no Element/Soul lock.
6. **Pipeline waste** - separate 3 s clips, then voice_change passes, then NSFW-blocked retries, instead of one multi-shot generation with native dialogue.
7. **No brand system** - nothing tied the grade, wardrobe, type, palette or tone to heal360 / TITAN.AI / Power Protein.

Every phase below closes one of those holes. Do not skip phases; compress them for small jobs.

---

## Phase 0 - Load context (silent, fast)
0. **If the user has an existing brief, script, or finished cut, it is the master spec.** Read it first (e.g. `references/physio-spot-ad-brief-v4.md`). Your job is to extend it, never to re-derive it. Do not QC an earlier iteration as if it were the intent.
1. Read `brands/<brand>.md (repo root)` for the brand in play (physio-spot, heal360, titan-ai, power-protein, personal). If brand is unknown, it is Question #1 in Phase 1.
2. Read `ledger/learnings.md (repo root)` (and in claude.ai, the memory file `/areas/higgsfield-creative-system.md`). Apply every standing rule in it - these are the user's past corrections.
3. If iterating on a previous run, pull those exact job prompts (job_display) and frames (`scripts/qc_frames.py`) before rewriting anything.

## Phase 1 - Interrogate the script (ASK - this user explicitly wants questions on Higgsfield work)
Read `references/interrogation.md`. Extract everything you can from what was given, then ask ONLY what blocks a correct render. Use `ask_user_input_v0` (max 3 questions, tappable) for the forks; free-text for anything nuanced. Always cover, if not already answered:
- **Objective + format + platform + audience** (skit, ad, documentary, film, explainer, motion piece, animation, photo/edit, carousel, clips; TikTok/Reels 9:16, YouTube 16:9, feed 4:5/1:1, cinema 2.39:1). Never assume vertical. Load the matching format guide from references/ (see CLAUDE.md routing).
- **The single idea / punchline** in one sentence. Restate it back. If the visuals you would need contradict it, say so.
- **Whose story, whose POV.** Name the camera owner per shot.
- **Real vs AI talent.** Is Physio Niklaus on camera (needs a Soul / Element from real photos) or are these original characters?
- **Brand + vibe**: which brand file applies; any reference video/image to match.
- **Hard no's**: policy risk (NSFW triggers burn credits), medical-claim risk for heal360, IP.

Rule: **keep the user's meaning.** You may sharpen wording, timing and staging; you may not change the joke, claim or CTA without flagging it as a proposed change and getting a yes.

## Phase 1.5 - Style & edit menu (ASK)
Offer choices from `references/edit-taxonomy.md` as tappable menus (max 3 questions per round): vibe/genre first, then camera + pacing, then transitions/zooms/SFX/captions/VO/music. If creator StyleCards exist (library/styles/), offer "edit like <creator>" as one-tap presets, then allow overrides. Mark any option routed ED (needs human editor) honestly.

## Phase 2 - Lock the Production Bible (write it out, get a thumbs-up)
Produce a compact spec block (template: `templates/production-bible.md`):
- **Logline** (1 line) + **beat sheet** with timestamps (hook <=1.5 s, setup, turn, payoff, CTA/button).
- **Cast sheet** - each character: name tag (A/B), age band, build, hair, wardrobe head-to-toe, one signature prop, voice (tone, accent, pace). Written ONCE, reused verbatim in every prompt.
- **Set map** - a top-down floor plan in words: fixed objects + where each character stands + where camera positions sit. E.g. `BENCH runs N-S. A lies supine, head at N end under racked bar. B stands at N end behind A's head, facing S. Window light from E.` Every shot references this map; anything that contradicts it is a bug.
- **Shot list** - per shot: #, duration, size (ECU/CU/MCU/MS/WS), angle + *camera owner* (A-POV / B-POV / neutral 3rd person), lens mm, movement, action (verbs, physical), dialogue (speaker-tagged, word count), SFX/ambience, continuity notes. Respect the 180-degree line.
- **Look** - from the brand file: grade, key/fill/practicals, palette hexes, texture/grain, wardrobe colours, type for overlays, safe zones.
- **Deliverables** - aspect, duration, count, caption/overlay plan, end card.

Run `python scripts/compile_shots.py validate spec.json` - it flags too-short dialogue shots, total-duration vs model limits, missing camera owner, POV/geography contradictions, risky wording. Fix every ERROR before spending credits.

## Phase 3 - Lock identity and space BEFORE motion
- **Characters:** real person (select photos with `references/soul-training.md` - score every candidate, enforce angle/shot-size quotas), (Klaus/Physio Niklaus, staff) -> Soul training (5-20 photos) for soul_2/soul_cinematic stills, plus an **Element** from one clean frontal image for video models. Original characters -> generate a **character sheet** first (Higgsfield `character-sheet` workflow, photoreal-unretouched), then create an Element from it. Never generate the hero video from text-only character descriptions.
- **Set:** generate one master establishing still of the location in the brand look; derive extra angles from it (nano_banana_pro / 3d_jutsu_angles) so the room stays identical. Optional: save as an environment Element.
- **Start frames:** compose each key start frame as a still first (cheap), QC it against the set map, THEN animate. A wrong start frame guarantees a wrong clip.

## Phase 4 - Route to the right model
Read `references/model-routing.md` (built from the live account catalog). Defaults:
- **Cinematic ad / realism-first (DEFAULT)** -> Seedance 2.5 omni_reference + Genjutsu motion transfer for key performances + 4K upscale of final (see references/cinematic-ad-director.md).
- Dialogue skit, multiple angles, one continuous scene -> **Kling 3.0 Omni** (`kling_o3_image_reference` with Elements, or `kling_o3_flf` with start frame) using `multi_shots: true` + `multi_prompt` - ONE generation, native dialogue + lip-sync. Not N separate 3 s clips.
- Longer narrative/ad 15-30 s, reference-driven, drafts -> **Seedance 2.5** (`seedance_2_5`, `draft: true` 480p first, finalize with `draft_job_id`).
- Hero cinematic shot with lens/lighting/pacing control -> **Cinema Studio 4.0**.
- Carousel/stills with text -> gpt_image_2_5 (typography) or nano_banana_pro (multi-reference consistency); product ads -> marketing_studio_image / Ads Studio.
- Always `models_explore get` the chosen model before the first call in a session - params change.

## Phase 5 - Compile prompts
Use `python scripts/compile_shots.py compile spec.json --model <id>` to emit model-native payloads, then hand-polish using `references/prompt-patterns.md`. Non-negotiables:
- Order: **Camera (owner, size, lens, move) -> Subject (cast tag + one distinguishing trait) -> Action (physical verbs, start->end state) -> Environment (set-map anchor) -> Light/Look -> Audio (speaker-tagged line, tone) -> Constraints.**
- Describe what IS in frame, positively. Replace "don't look at him" with "eyes fixed on the ceiling light".
- One motion idea per shot. Two moves = two shots.
- Dialogue: action first, then `[A, flat deadpan]: "Bro... are you spotting?"`. <= ~2.5 words/sec of shot.
- Continuity tail on every shot: `same characters, same wardrobe, same gym, same amber grade as shot 1, no face morphing`.
- Avoid wording that trips moderation (bodily fluids near crotch, "wet shorts", etc.) - restage the gag (see learnings).

## Phase 6 - Cost preflight + draft-first
- `get_cost: true` on every planned call; show the user a one-line budget table (model, shots, seconds, credits) before spending. Skip the table only for single cheap stills.
- Draft first: Seedance 2.5 `draft`, Kling `std` before `pro`, images `quality: low/medium` for composition, then upgrade the winner. Never 4k/pro on an unvalidated composition.
- Batch independent stills with `generate_image_batch`; poll with `jobs_wait`; show once with `show_generation_by_ids`.

## Phase 7 - QC (be the user's eyes - always, before presenting as "done")
Run `python scripts/qc_frames.py <url-or-file>...` -> contact sheet + metadata. View the sheet. Score with `references/qc-rubric.md` (geography, POV, action-logic, identity, brand look, pacing/timing, audio/lipsync, text/safe-zones, artifacts, policy). Report as: PASS / FIX (with the exact prompt delta) / REGEN. Never call something final that fails geography, identity or action-logic.

## Phase 8 - Feedback loop (makes it smarter every run)
After delivering, ask 2 quick things (tappable): overall verdict (ship / tweak / redo) and the biggest miss (angle, tone, pacing, look, character, other). Then:
- Translate the feedback into a **rule** ("For Klaus's gym skits: spotter always stands behind the lifter's head; camera owner stated per shot").
- Append it to `ledger/learnings.md (repo root)` (Claude Code) or the memory file `/areas/higgsfield-creative-system.md` (claude.ai) - dated, with brand + format tags.
- On revision, change only what the feedback targets; restate everything else verbatim so nothing drifts.

## Format playbooks
- **Villains, cruelty & conflict (rich bullies, slut-shaming, bullying, degradation, side-choosing)** -> `references/villains-conflict.md` — depict honestly, show impact and consequence, never let the edit reward cruelty.
- **Class & status (hot & rich ↔ broke & struggling; tone dial humour/disdain/wit/debate/hyperbole)** -> `references/class-status.md` — fair to both sides, punch at behaviours/systems not poverty, sourced stats, localised.
- **Original character design (attractive, diverse, female-led roster)** -> `references/character-design.md` — build archetypes, face/hair/skin vocabulary, voice archetypes, character cards; never lookalikes of real people.
- **Commentary, controversy & social-justice content; implicit sensuality toolkit** -> `references/commentary-controversy.md` — mandatory fact-check + sources for real people/events, no fabricated quotes, no AI likeness/voice of real people, steelman before critique, community-centred social-justice storytelling.
- **Mature & edge (18+ raunch, dark/bad-decision stories, shock, absurdity, rage-bait hooks, Japanese writing modes, profanity dial)** -> `references/mature-edge.md` — hard lines: no explicit/porn, no filter-bypassing, nothing sexual near minors, no real-person sexualisation, no group-degrading punchlines.
- **Localisation (Singlish/SG, Bollywood/Indian, MY, VN, TH, ID, NG, UK, US)** -> `references/localisation.md`: settings library, language register, humour sources, sound flavour, casting, and legal rules (SG health ads: no testimonials/paid reviews/superlatives/free-consult inducements).
- **Commentary personas, reaction faces, audio stims, trending audio** -> `references/voice-persona-audio.md` (archetypes only — never clone/imitate real people).
- **Cinematic ads, story-led shorts, skits (DEFAULT FLOW)** -> `references/cinematic-ad-director.md`: Gate 1 brief intake → Gate 2 five story directions (diversity matrix + 13-field cards, one Recommended) → Gate 3 second-by-second production script → spec → render. Default stack: Seedance 2.5 omni_reference (draft→1080p high bitrate) + Genjutsu for performance-critical shots + 4K upscale on the final.
- **Physio Spot ads** -> `references/physio-spot-ad-brief-v4.md` (sections 4-8 are the production standard, section 7 always applies)
- **Skit / dialogue short** -> `references/playbook-skit.md`
- **Carousel (4:5, 6-10 slides)** -> `references/playbook-carousel.md`
- **Clinic / educational explainer, product ad, UGC** -> `references/prompt-patterns.md` + Higgsfield's own workflows (`get_workflow_instructions`: ugc-video, product-photoshoot, thumbnail-generation, video-montage for captions/assembly, brand-asset-creation).
