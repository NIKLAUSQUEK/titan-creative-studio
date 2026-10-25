---
name: story-sync
description: Synchronises picture, B-roll, filler/pattern-interrupt shots, music, trending audio and sound design with the emotion and story beats of ANY video (ad, skit, UGC, explainer, doc, podcast clip, reel, short film). Use when planning or revising an edit's rhythm - "where should B-roll go", "what music fits", "make it feel more emotional/tense/premium/funny", "sync cuts to the beat", "use a trending sound", "the edit feels flat", "why does this feel off", "edit like <creator/style>" - and at Gate 3 scripts, /edit briefs and recipes, /sound plans and QC. Turns a script into a beat-by-beat Sync Map (emotion → picture → B-roll → filler → music → SFX → text) and checks the finished cut against it.
---

# Story Sync

The editor's job is to make the audience feel the right thing at the right second. Walter Murch weights an ideal cut **emotion 51% · story 23% · rhythm 10% · eye-trace 7% · 2D plane 5% · 3D space 4%**: when something must give, give from the bottom. Sound changes what viewers believe they saw (Chion's "added value"; Boltz 2001), so **fix emotional problems in sound first** - it is cheaper than regenerating picture.

## When to load what
| Need | File |
|---|---|
| Where/what/how long B-roll; J/L cuts; ratios; B-roll that hurts | `references/broll-grammar.md` |
| Punch-ins, whips, freezes, text cards, memes, ramps, match cuts - what each makes people feel, how often | `references/fillers-interrupts.md` |
| Mood → tempo/harmony/instruments; music arc ↔ story arc; beat-cutting, silence, risers, ducking, editing music to length | `references/music-emotion.md` |
| SFX layers, stims, ASMR, cold vs hype sound | `references/sound-design.md` |
| Trending sounds: lifecycle, when to jump, licensing per platform, adapting a trend's format with licensed audio | `references/trending-audio.md` |
| Story structure → shot-length curve, B-roll, music, SFX, silence (hook-problem-solution, storytime, myth-buster, listicle, skit, manifesto, doc…) | `references/structure-rhythm.md` |
| How specific creators/brands/archetypes sync (viral, pro, niche) | `references/style-sync-patterns.md` |
| Muted / audio-only / together QC passes, retention-dip reading, common mismatches | `references/emotion-qc.md` |
| Blank Sync Map | `templates/SYNC_MAP.md` |

## Workflow (runs inside the normal studio gates)
1. **Read first:** `ledger/learnings.md`, the brand file (§voice, edit-brand block, compliance pack), the project SCRIPT.md / BRIEF.md / EDIT_BRIEF.md, any StyleCard or preset chosen. An existing script or cut is the master spec: sync work never changes lines, jokes, order or CTA.
2. **Emotion target per beat.** Write one line per beat: `0-3 s curiosity / 3-9 s tension / 9-12 s relief / CTA warmth`. Pick the structure row in `structure-rhythm.md`.
3. **Set the two music dials separately** (Husain et al. 2002): tempo/energy = arousal; mode/harmony = valence. Mixed cues = mixed feelings on purpose (slow + major = bittersweet nostalgia; fast + minor = defiance).
4. **Fill the Sync Map** (`templates/SYNC_MAP.md`): per beat → picture (A-roll), B-roll (type + the exact word it lands on), filler/interrupt, transition, music section + event (start/swell/drop/stop), SFX/stim, on-screen text, silence. Save to `projects/<p>/SYNC_MAP.md`.
5. **Hand off:**
   - Gate 3 script table → the Sync Map columns become the script's audio/B-roll columns.
   - `/sound` → music picks must match the mood row and the arc; trending-audio rules decide licence per account.
   - `/edit` → map to the recipe: `broll[]` anchors on the Sync Map words, `audio.sfx[]` on its stims, `style.music.db/duck`, `style.zoom` cadence, `texts[]`; pick the preset whose sync pattern matches (`style-sync-patterns.md`).
   - Generation (`/plan`, `/draft`) → B-roll and insert shots needed but missing become shot-list items (real footage first, then generated).
6. **QC the cut** with the three passes in `emotion-qc.md` (muted, audio-only, together) plus the retention curve once posted; log mismatches → `/learn`.

## Defaults (rules of thumb - tune with the account's retention data)
- **Interrupt cadence by energy:** high (skit/creator) a visual change every 1.5-3 s + a sound accent every 3-5 s · medium (explainer/UGC ad) 3-6 s · premium/health/doc 5-10 s, motivated changes only. Vary lengths - shot-length *variation* holds attention better than a metronome (Cutting et al. 2010).
- **B-roll share:** talking-head short 20-40% · UGC ad 10-30% · explainer 50-70% · mini-doc 50-60% · brand ad 60-90%.
- **Mix:** dialogue -14 LUFS integrated, ≤ -1 dBTP; music bed 12-18 dB under voice and ducked (editor default `music.db -19` + sidechain); stims never mask a word.
- **Hold the face** on the most emotional or most credible line; cut away on the key noun/verb, not over the feeling.
- Every riser resolves (hit or silence). Silence after a build = the gut-punch (pauses drop arousal below baseline, Bernardi 2006).

## Hard rules
- Brand/business accounts: licensed or original music only (TikTok Commercial Music Library, Meta Sound Collection, licensed library, original). Chart/trending songs = personal/creator accounts, added in-app, never baked into the file (ledger).
- Cruelty beats get **cold** sound (music out, dry room tone), never hype stingers (ledger 2026-10-20 villains rule).
- Health/clinic brands: no memes, glitches, snap zooms, cartoon SFX, rapid flashes or "miracle" swell-and-drop under outcome claims; no patient before/after or testimonial VO (compliance-sg.md). Restraint reads as trust.
- Never use a real artist's song "style-alike" brief for generated music ("in the style of <artist>"): describe genre, BPM, mood, instruments.
- Photosensitivity: no repeated white flash frames.

Sources: `research/sources-story-sync.md`. Labels in references: [R] research · [O] official · [P] practitioner · [RoT] rule of thumb (test it).
