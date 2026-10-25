# Auto-editor: raw footage → finished edits (tools/editor)

Use this for "edit this footage", "make a UGC edit", "cut my talking head", "revise the edit", or "make 9:16/1:1/16:9 versions". For setup on Klaus's PC see `tools/editor/README.md`.
The tool is local and free. Claude makes decisions only and edits only the **recipe** (`edit.vN.json`); ffmpeg renders it deterministically.

## 1. Flow (gates match the studio rules)
1. **Is there an existing brief, script or final cut?** Ask first. If there is, it is the master spec: put its lines and order into `brief.json` beats and never re-write them.
2. **Ingest.** Run `python tools/editor/editor.py --project P ingest <files|folders>`, then read only `projects/P/autoedit/ingest/summary.md`. It lists the kept lines with source times, the dropped retakes, throat-clearing and a hook shortlist. Never read the raw words.json.
3. **Strategist brief.** Inside a Claude Code session, run `editor.py brief --pack-only`, read `brief_prompt.md`, write `brief.json` yourself, then run `editor.py brief --from-json brief.json`. Don't nest a `claude -p` call. On Klaus's PC, `Run-Editor.ps1` makes the single call.
   - The brief sets the goal (wise/expert/trust/sell/founder/entertain), audience, platform/aspect, 5 ranked hooks (formulas from `story-engine.md`), structure, beats mapped to clip ranges, CTA, compliance notes and the preset.
   - Show Klaus the 1-page `EDIT_BRIEF.md` and let him swap the hook or preset before cutting.
4. **B-roll.** Run `editor.py broll-match --llm none`. Then look at `broll_sheet.jpg` and edit the `pick` values (0/1/2/null) in `broll_candidates.json` yourself. Never pick a flagged clip.
5. **Assemble.** Run `editor.py assemble [--preset X --aspects 9:16,1:1,16:9 --music file --music-licence original]` to get `edit.v1.json`.
6. **Draft.** Run `editor.py render` (the lowest quality, every aspect), then `editor.py qc`. LOOK at the contact sheets listed in `QC_vN_draft.md` before reporting.
7. **Revise.** Each note from Klaus makes a new version.
   - Run `editor.py revise "<note>" --llm none` for quick phrases (§4).
   - For anything else, run `editor.py fork -m "<note>"`, edit the newest `edit.vN.json` by hand, run `editor.py validate`, then re-render.
   - "Go back to v3" is `revise "go back to v3"`.
8. **Approve, then final.** Only on Klaus's yes, run `editor.py approve`, then `render --final`, `qc --final` and `handoff`. Then go to `/sound` (if it isn't done yet) and `/publish`.
9. **Learn.** After delivery, ask for his verdict and the biggest miss, then run `/learn`.

## 2. Recipe cheatsheet (`edit.vN.json`)
- `items[]`: `{id, clip, in, out, beat, speed, zoom:[{at, scale, ease}], focus_x, fit}`.
  - `in`/`out` are **source** seconds within the ingest clip. Order in the list = playback order.
  - Snap zoom = a key at `at` with `scale` (e.g. 1.08). Smooth push = two keys, the second with `"ease": "linear"`.
  - `fit` is `auto|cover|blur` (`blur` pads vertical footage into 16:9).
- `broll[]`: `{path, src_in, dur, anchor:{item, offset}, mode: full|pip|greenscreen, flag}`. Anchors follow trims.
- `texts[]`: `{type: hook|title|lower_third, text, anchor, dur}`.
  - Hook text = what the viewer reads in the first second. Don't duplicate a spoken hook that is already captioned.
- `captions`: words come from ingest automatically.
  - Fix them with `replace` ({"heal": "heal360"}), force keywords with `emphasis`, and blank ranges with `hide` ([[t0, t1]] output time).
- `audio`: `music {path, licence, db, duck}` + `sfx[] {type: whoosh|impact|pop|ding|riser|click, anchor, db}` + `loudness` (-14).
  - Files in `assets/sfx/<type>/` beat synthesised SFX.
- `style`: the merged preset, StyleCard and brand guide (captions, hook_text, zoom, pacing, broll, sfx, music, grade, end_card, safe_zone, compliance).
  - Change it per version, e.g. `style.captions.position_y`.
- `end_card`: `{enabled, dur, lines[], cta}`.
- `approved`: set only by `editor.py approve`, after Klaus says yes.

## 3. Presets (`tools/editor/presets/`)
| Preset | Use for |
|---|---|
| talking-head-punchy (default) | founder/expert reels: jump cuts, punch-in every ~3 s, 2-3 word pop captions |
| deadpan-comedy | skits: silence kept, static captions, crash zoom only on the reveal, one impact |
| premium-calm | clinic/brand: slow pace, soft push-ins, sentence captions, warm grade |
| genz-chaos | 0.8-1.5 s shots, punch every cut, 1-2 word caps captions, stim every 1.5-3 s |
| aura-cinematic | statement edits: slow pushes, minimal words, riser, crushed grade + vignette |
| documentary | VO-led, B-roll every ~4 s, lower-thirds, sentence captions |
| ugc-selfie-talking-head · ugc-unboxing · ugc-try-on-demo · ugc-reaction · ugc-pov · ugc-testimonial-style · ugc-day-in-the-life · ugc-green-screen | UGC formats; each preset carries its typical beat structure, pacing and caption style |
| **30 researched styles** (retention-max, story-vlog, clean-explainer, luxury-broll, moral-skit, magic-transition, silent-deadpan, podcast-clip, street-interview, storytime-text, product-hero, manifesto-montage, map-explainer, motion-explainer, cinematic-vlog, doc-trailer, absurd-sketch, mascot-unhinged, clinic-trust, b2b-founder, myth-buster-expert, exercise-demo, doctor-reacts, raw-gym-vlog, aesthetic-lifestyle, fast-recipe, tech-review-premium, ugc-ad-hook-stack, sea-skit, sensitive-health-edu) | pick from `style-catalog.md` (use-for, brands, funnel, compliance locks); each carries a `sync` block (B-roll, fillers, music, emotion map) used by the story-sync skill |
| style-<creator> | made by `editor.py preset from-stylecard <name>` from Supabase `style_cards` (or `/style <creator>`) |

- **Precedence:** ledger > brand file (the `edit-brand` block) > Klaus's script/brief > preset > defaults. The brand block wins on fonts, caption/hook placement, colours and the end card.
- **`ugc-testimonial-style`** means experience-style: the creator or founder talks about their own experience. In regulated health markets (SG) never use patients, outcomes or "it fixed me". The QC compliance scan enforces the forbidden words.

## 4. Quick revision phrases (0 tokens)
- **Trim:** cut first N s, trim last N s.
- **Versions:** go back to vN.
- **Captions:** punchier captions, smaller captions, captions off.
- **Music:** no music, music up, music down.
- **Zooms:** more zooms, fewer zooms, no zooms.
- **SFX:** more sfx, less sfx.
- **Pacing:** tighter, slower (both re-cut from the beats).
- **Hook text:** `hook text: <text>`.
- **Aspects:** only 9:16, add 1:1.

## 5. Token rules
- Read `summary.md`, `EDIT_BRIEF.md` and `QC_vN.md`. Never read words.json or the sqlite index.
- One contact sheet per B-roll decision round, not one per beat.
- For revisions, prefer quick phrases. Otherwise edit the JSON directly; the recipe has no word lists, so it stays small.
- Use the self-review (`qc --llm claude-cli`) only on Klaus's PC runs. In a session, you look at the sheets yourself.

## 6. Sound and compliance hooks
- **Sound:** `/sound` decides the track. Brand accounts get `audio.music.licence` = `original` or `licensed:<source>`; the renderer refuses unlicensed music for brand accounts. Trending sounds on personal accounts are `in-app`: never baked into the file, and recorded in `PUBLISH.md`.
- **SFX:** density and stim types follow the preset (see `voice-persona-audio.md` stim map).
- **Compliance:** the QC word scan uses the brand's `compliance.forbid_words` plus the health pack list for health/clinic brands. It is a tripwire, not legal review: still run the compliance pack in `/publish`.
- **B-roll consent:** clips flagged by path markers, `broll_flags.json` or Creator Brain sensitivity are never auto-picked.

## 7. QC checks, staged passes and handoff (added 2026-10-25 from Klaus's reference videos)
- **Critique before cutting.** The brief's `critique[]` holds "watch it all, tell me what would make it better" notes, each with its fix. It shows up in `EDIT_BRIEF.md`.
- **Edit in staged passes, one recipe version per pass:** cut → captions → B-roll → style → graphics. Never ask for everything in one note.
- **New `qc` checks:**
  - **No leaked retakes.** Fails if any 6-word run is spoken twice in the cut.
  - **Script coverage.** When `brief.script_lines` holds the approved script, every line must appear once, in order.
  - **Face occlusion.** OpenCV face boxes are compared against the caption and hook-text boxes on the 9:16 render. Fails if text covers a face. Needs `opencv-python-headless<5` (installed by `Run-Editor.ps1`); otherwise the check is skipped and noted in the report.
  - **Attribution manifest.** `qc/ATTRIBUTION_vN.md` lists every music, B-roll and SFX file with licence, scope, source and credit line, taken from `assets/licences.csv` (columns: path, source_url, licence, scope, attribution). Unknown licences are flagged; `/publish` copies the credit lines into the description. YouTube Audio Library or "free" stock assets need a row, with platform scope, before they go on brand accounts.
- **Human-editor handoff.** `editor.py export [--version N]` writes `edit_vN.edl` (CMX3600: the A-roll cut plus B-roll on V2, with source file names) for finishing in Premiere or Resolve. Captions and graphics stay in the burned render.
- **Quiz-reveal preset.** `quiz-reveal`: question card → countdown → reveal → "what did you guess?".
- **Roadmap (not built yet; see `research/sources-reference-videos.md`):**
  - a boards pipeline (per-line "needs a visual?" planner → HTML boards from the brand design system → word-timestamp sync → HyperFrames render → `boards` layer)
  - human-edit diff learning (re-read the edited timeline and propose `/learn` rules)
  - `decode-style <reference>` → preset JSON
  - person-tagged B-roll library (cast photos → tags, action captions)
  - an optional script-following teleprompter that logs takes (local speech recognition only, for client privacy)

## 8. Boards and cards (explainer graphics, carousels, LinkedIn PDFs)
- **Boards** = animated brand cards over the video, timed to the word: `boards[]` in the recipe (`{id, card, anchor, dur, mode}`). `mode: panel` keeps the speaker visible (card in the top ~40 %, panel shrinks to its content); `mode: full` replaces the frame and auto-hides captions while it is up (the VO keeps playing).
- **Card types:** title, stat (counts up), list, steps, quote, compare, definition, myth_fact, chart (bars grow), cta. `*word*` = highlight colour. Brand colours/fonts come from the `edit-brand` block (`colors`, `fonts`, optional `cards` overrides, `handle`); brand font files in `assets/fonts/<brand>/`.
- **Planning (0 tokens):** `editor.py boards [--mode panel|full --max N --dry-run]` runs the "understandable by listening alone?" test per spoken phrase (numbers, dates, steps, definitions) and drafts cards; presets with `"boards": {"auto": true}` (clean-explainer, b2b-founder, linkedin-founder-video, motion-explainer, myth-buster-expert, map-explainer) plan them at assemble. Drafted stat cards carry `_todo: add source`; Claude or Klaus finishes the copy in the recipe.
- **QC:** every stat/chart board has a `source`; no `_todo` left; each board ≥ 2 s on screen. Board-in SFX uses the preset's `sfx.map.board` (else `title`).
- **Revise phrases:** "no boards", "boards full", "boards panel".
- **Carousels / LinkedIn documents:** `editor.py cards SPEC.json --aspect 4:5|1:1|9:16|16:9 [--brand B --out DIR --no-pdf]` → `slide_NN.png` + `slides.pdf` + `contact_sheet.jpg` (page numbers, handle, "swipe →"). Spec = `{"brand", "aspect", "theme": {...}, "cards": [...]}`. Look at the contact sheet before calling it done. Archetypes: `styles/carousel.json`.
- Premium path: the same card JSON drives HyperFrames/Remotion when a piece needs bespoke motion.
