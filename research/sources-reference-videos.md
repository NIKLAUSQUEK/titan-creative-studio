# Klaus's reference videos (shared 2026-10-25): what we took, what we rejected

Transcripts came from the Firecrawl catalogued YouTube provider (5 credits per video); no video files were downloaded. Non-English videos (Hindi/Urdu, Spanish, Indonesian) were translated. All eight are vendor-, sponsor- or affiliate-backed, so income, cost and win-rate claims are unverified.

| # | Video | Creator · date · length | Used in |
|---|---|---|---|
| 1 | [I Replaced 8 Hours of Video Editing with This (Open Source)](https://youtu.be/dXz1qkLc9PQ) | Sirio Berati · 2026-10-21 · 20:17 | editor.md §7 (script-anchored retake check, boards roadmap, NLE handoff), story-sync explainer insert rule |
| 2 | [Edit 10 Videos a Day With Claude (No Editor Needed)](https://youtu.be/RDOy_HkTWyY) | Aaghaz · 2026-10-14 · 10:49 (Hindi/Urdu audio) | editor face-occlusion QC, attribution manifest, critique-before-edit, staged passes, quiz-reveal preset |
| 3 | [Crea Videos Stickman con IA GRATIS (y Claude los Edita Solo)](https://youtu.be/hjDMZjGZUlE) | Fannquis · 2026-10-24 · 15:16 (ES) | faceless explainer rules (ai-video-playbook §10), motion budget, NLE-file handoff idea, human-edit diff learning (roadmap) |
| 4 | [Google acaba de Regalar los Vídeos Largos con Audio por IA GRATIS](https://youtu.be/IWA9LCvNW8g) | Alejavi Rivera · 2026-09-27 · 26:33 (ES) | free-tier animatic lane (internal only), order-confirmation before auto-assembly |
| 5 | [If You Don't Understand Funnels, You Don't Understand Marketing](https://youtu.be/-8YiaBpl3DU) | Oren John · 2026-08-24 · 26:49 | funnels §8 (pre-call page, minimum nurture, setter/closer, swipe teardown, manual DMs), copy-angle triad |
| 6 | [Give Me 16 Minutes and I'll Make You $1M on LinkedIn](https://youtu.be/jiMt2D-ZhTY) | Nader Alnajjar · 2026-09-24 · 15:29 | LinkedIn profile spec + 40/40/20 split (platform-signals, content-strategy), awareness-mapped magnets, thank-you segmentation, weekly webinar route, teardown + format bank |
| 7 | [5 Trik Seedance 2.5 Ini Bikin Video AI-Mu Sekelas Pro](https://youtu.be/XjK7C0HDRus) | Manzoti AI · 2026-10-24 · 15:09 (ID) | character sheet v2 (face lock, headless body, "Additions"), focus lines, extend recipe, first/last-frame identity caveat, MP4 VO lip-sync trial |
| 8 | [3-Step Workflow To Make Ultra-Realistic AI Ads](https://youtu.be/3rDs6FhFoUQ) · prompts: https://higgsfield.ai/s/cinema-studio-higgsfieldai-whzLmx | Higgsfield AI · 2026-06-23 · 35:37 (Seedance 2.0) | `style_prefix` / `scene_overrides` / shot ids / `--shot` in compile_shots.py; layout-map schematic; state-variant sheets; duplicate-face erase; 2×2 motion test; 3/4 locations; composite-mask wardrobe; move-by-move choreography (compiler warning); music input; match-cut contracts; keeper-seconds editing; FOV-in-degrees anatomy |

## Built in this change
- `scripts/compile_shots.py`:
  - `style_prefix` prepended to every prompt and `scene_overrides` per scene
  - shot ids must be unique, and `--shot <id>` compiles one prompt
  - warns when a shot says "dances/fights" without spelling out the moves
- `tools/editor`:
  - QC fails on leaked retakes (a 6-word run spoken twice)
  - QC checks the approved `script_lines` are all present, in order
  - QC checks for caption or hook text over a face (OpenCV 4, or YuNet on OpenCV 5)
  - QC writes an attribution manifest from `assets/licences.csv`
  - `export` writes a CMX3600 EDL for finishing in Premiere or Resolve
  - the brief gains `critique[]` and `script_lines`
  - new `quiz-reveal` preset

## Roadmap (proposed, not built)
| Upgrade | Effort | Notes |
|---|---|---|
| Boards pipeline: per-line "understandable by listening?" planner → board brief → HTML boards from the brand design system → word-timestamp sync → HyperFrames render → `boards` recipe layer | L | Seed from Sirio's MIT board templates (github.com/sirioberati/YouTube-AI-Video-Editing-System), restyled per brand. HyperFrames: Apache-2.0 |
| OTIO / FCPXML export with captions as a subtitle track | M | OpenTimelineIO (Apache-2.0); the EDL exists now |
| Human-edit diff learning: re-import the edited timeline, diff it against the agent version, propose `/learn` rules | M | |
| `editor.py decode-style <file/url>` → preset JSON + intro-as-skill | S–M | Use legal reference clips only |
| Person-tagged B-roll library: face match against cast photos, action captions, clip list, consent flag | M | face_recognition (MIT). Avoid InsightFace's non-commercial models |
| Script-following teleprompter that logs takes (`take.json`) + `AGENTS.md` per footage folder | M | Local speech recognition only (e.g. Vosk); Chrome Web Speech sends audio to the cloud, which is wrong for clinic footage |
| Asset Bible `variants[]` + schematic asset type in `compile_shots.py` validation | S | |

## Rejected (breaks studio rules or platform terms)
- **Fake accounts:** multiple Google accounts to farm free credits (video 3).
- **Location spoofing:** a VPN to unlock region-locked voice cloning (video 4).
- **Watermark removal:** stripping AI watermarks (video 4).
- **Third-party IP:** generating a game franchise (video 4).
- **Real-person likeness:** seeding character sheets from internet photos of real people (video 7).
- **Unlicensed assets:** "copyright-free internet" B-roll, and YouTube Audio Library tracks used outside their scope (video 2).
- **Poreless skin:** the poreless-skin prompt line (video 7) conflicts with realism.md.
- **Unverified claims:** cost, error-rate and income claims treated as fact (videos 1, 4, 5, 6).
