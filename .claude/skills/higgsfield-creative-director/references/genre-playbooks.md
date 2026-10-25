# Genre playbooks: the same genre language for generation (Higgsfield) and the edit (tools/editor)

Pick a genre module in Gate 2 (story directions) for ads too, not just films. The module sets:
- pacing, shot grammar, camera, light/grade and the sound plan;
- the prompt block pasted into every shot (`genre_key` in spec.json);
- the editor preset used to cut it.

**Status:** each module was built from one reference only. Klaus approves or corrects each one: `/learn` writes the rule.

## How a module plugs in
- **spec.json:** `"genre": "horror-tension"`, `"genre_key": "<the module's style key line>"`, and per shot `duration`, `camera`, `light`, `sound` taken from the module's shot grammar.
- **Prompts:** put the genre key LAST in every image and video prompt (identity and camera stay first; prompt-patterns.md universal grammar).
- **Edit:** `editor.py assemble --preset <module preset>`. Sound comes from the module's stim plan through `/sound`.
- **Ads:** keep the genre's grammar up to the turn. Then use the brand's own ending look (e.g. Physio Spot cuts to the calm beige clinic), and apply the compliance pack to every line.

---

## 1. Horror / thriller tension (`horror-tension`)
**Reference:** Klaus's ref #5 (research/edit-references-2026-10.md): a 99 s bathroom scare. Measured average shot ≈ 10 s, a sting roughly every 1-2 s in the build, and silence before the scare.

**Why it works:** the camera stays longer than is comfortable. Darkness and sound do the work; cuts are rare. The audience knows something is wrong before the character does.

### Pacing map (scale to the runtime; 30 s ad shown)
| Beat | 30 s ad | Shot | Sound |
|---|---|---|---|
| Cold open: wrongness | 0-3 s | static wide, a held frame where something is slightly off (a door ajar, a figure in the mirror) | room tone, fluorescent buzz |
| Normal + tension | 3-12 s | slow push-in on the lead (8-10 s, one shot); a reflection or shadow moves behind them unnoticed | low drone fades in; single stings at 1-2 s gaps |
| Escalation | 12-20 s | lights flicker; 2-3 shorter shots (2-3 s): eyes, hand on the door, the empty stall | stings tighten; breathing; music drops out |
| Silence | 20-21.5 s | hold on the face or the empty frame | dead silence (≥ 0.8 s) |
| Scare / reveal | 21.5-23 s | snap: crash zoom or hard cut to the reveal | impact + bass drop, peaking at -1 dBTP |
| Turn (ads) | 23-30 s | hard cut to black, then the brand's calm world (light comes back) | silence → warm room tone → VO/CTA |

### Shot grammar
- **Camera:** gimbal-smooth slow push-ins and drifts; static locked-off wides for "wrongness"; low or high angles only for the scare. No handheld shake except POV panic.
- **Lens:**
  - 24-28 mm wides (the space is a character);
  - 50-85 mm tight on eyes and hands in the escalation;
  - deep focus in wides so the background threat is readable.
- **Blocking:** the threat lives in the background, frame edges, reflections or doorways. Leave negative space where something could appear.
- **Light:** motivated practicals only (fluorescent tubes, phone torch, a bulb). Cold teal-green fluorescent, deep shadows, faces half-lit. Light failure (flicker or blackout) is a story beat.
- **Grade:** teal shadows, slightly green mids, saturation ~0.7, crushed blacks, vignette. The editor preset applies the same values.

### Prompt blocks (Seedance 2.5 / Kling 3.0)
Genre key (paste last, identical in every shot):
```
horror thriller tone, cold fluorescent teal-green light, deep crushed shadows, desaturated, faces half in shadow, slow deliberate camera, held frames, negative space, practical lights only, subtle film grain, no jump-scare blur, no gore
```
Shot JSON (use for each line of spec.json `shots[]`; compile_shots.py turns it into the prompt):
```json
{
  "id": "S02", "dur": 8, "model": "seedance_2_5", "mode": "omni_reference",
  "camera": "slow push-in on gimbal, 28mm, eye level, from doorway toward @LEAD at the mirror",
  "subject": "@LEAD (identity from asset bible) washes hands, unaware",
  "action": "start: hands under tap -> end: she looks up into the mirror; behind her the far stall door drifts open 10 cm on its own",
  "environment": "@SET_BATHROOM: white tiles, green stripe, three stalls on the left, mirror right",
  "light": "two fluorescent tubes, the far one buzzing and dim, cold teal-green, shadows pooling under stalls",
  "audio": "fluorescent hum, dripping tap, faint low drone; no music",
  "constraints": "keep stall door movement subtle and slow, no figures visible yet, same wardrobe, no face morphing",
  "genre_key": "<horror genre key above>"
}
```
- **Kling multi-shot:** label the shots, one camera owner per shot, and keep the grade line identical across shots.
- **Moderation-safe horror:** suggest the threat (a shadow, a reflection, a door, a sound). Show no gore and no real-person likeness; children never appear in horror. Adult themes follow mature-edge.md.

### Sound plan (into `/sound` and the edit)
- **Bed:** drone or room tone (the editor synthesises an original drone when there is no licensed bed).
- **Build:** stings at 1-2 s gaps that tighten toward the scare; breathing and foley (tap drip, door creak) carry the realism.
- **The scare:** ≥ 0.8 s of TRUE silence before it, then impact plus a bass drop on the reveal frame.
- **Levels:** VO is king for the ad turn. Stims never mask a spoken word (voice-persona-audio.md).

### Horror-framed ad template (any brand)
- **Hook (0-3 s):** a "wrongness" frame plus a header that names the fear in the viewer's words.
- **Build:** the everyday situation turns uneasy (the product's problem, staged as a threat).
- **Scare or reveal:** the problem lands.
- **Turn:** a hard cut to light. The brand is the relief, never the monster.
- **CTA:** calm, in the brand voice.
- **Compliance:** fear appeals must stay proportionate. No fear-mongering for health claims (compliance-packs.md); in SG health ads the scare can't be a medical outcome claim.

### Edit preset
`horror-tension`: long holds, pause removal only above 1.6 s, slow push-in every 8 s, flicker-in at each beat change, sting/impact SFX, drone bed, teal grade, small low serif captions.

---

## 2+. Modules to build (tonight's research run fills these; each gets the same sections as §1)
- **comedy skit / deadpan:** see playbook-skit.md and the deadpan-comedy preset. Needs a pacing map from top references.
- **Gen Z vlog / reaction** (`genz-header-skit`): Klaus's ref #1. Needs shot grammar for generated versions.
- **trend beat-switch** (`trend-beat-switch`): Klaus's ref #6.
- **luxury / product reveal / new release:** ref #3 pending from Klaus.
- **news / scam-expose carousel:** ref #2 pending.
- **action / sport hype**, **romance / aura**, **documentary / investigative**, **mystery / reveal**, **feel-good / emotional**, **K-drama / anime-inspired**, **ASMR / satisfying**, **before-after transformation** (check the compliance packs).
