# Fillers and pattern interrupts

"Filler" here = the shots and devices between beats that reset attention without new story: punch-ins, whips, freezes, text cards, reaction cutaways, sound-only beats. (Spoken fillers - um/uh, retakes, dead air - are removed by the editor: `pacing.remove_fillers`, `remove_silence_over_s`.)

## Device → emotional effect [RoT synthesis]
| Device | Effect | Notes |
|---|---|---|
| Punch-in (digital 110-130%) | emphasis, intimacy, "this matters"; hides jump cuts | cheapest reset |
| Slow push-in | tension or sincerity | premium/health-safe |
| Snap/crash zoom | comic emphasis, shock | creator-coded; not for clinics |
| Whip pan | energy, jump in time/place | pair with a whoosh peaking on the cut |
| Flash frame (1-2 white frames) | shock, memory, camera flash | **photosensitivity: never repeated** |
| Freeze frame | irony, "you're probably wondering…", chapter beat | storytime, comedy, doctor-reacts |
| Text card | pause, punchline, stat | readable on mute |
| Sound-only beat (black/hold, audio runs) | suspense, gravitas | very premium |
| Reaction cutaway | tells the audience how to feel | strongest comedy tool |
| Meme insert | self-aware humour | personal accounts only |
| Speed ramp | hype, power, reveal | overused in fitness; sparingly |
| Match cut | wit, connects two ideas (Eisenstein's intellectual montage) | premium-safe |
| Glitch | tech, error, chaos | cheapens health/premium |
| Time-skip card ("Day 3") | progression | vlogs, challenges |
| Layout change (fill ↔ split) | new speaker/energy | podcast clips |

## Eisenstein's montage methods → studio use
Metric (fixed lengths) = beat-cut montage · Rhythmic (cut to movement in shot) = cut on action · Tonal (cut to mood) = mood B-roll · Overtonal = all combined · Intellectual (juxtaposition creates an idea) = metaphor B-roll, match cuts.

## Cadence by energy [RoT - evidence is weak and guides conflict; confirm on the retention curve]
| Energy | Visual change | Sound accent | Allowed devices |
|---|---|---|---|
| High (skit, creator, GenZ) | every 1.5-3 s | every 3-5 s | all incl. snap zooms, memes (personal), stims |
| Medium (explainer, UGC ad, vlog) | every 3-6 s | at structure beats | punch-ins, text cards, whips, reaction cuts |
| Low / premium / health / doc | every 5-10 s, motivated only | 0-2 per piece | slow push-ins, match cuts, dissolves, sound-only beats |
A jump cut every second is noise, not energy. Variation beats fixed intervals.

## When interrupts cheapen
Clinic, health, luxury and B2B-trust pieces lose credibility with memes, glitches, snap zooms, cartoon SFX, flash frames and speed ramps on clinical content. Restraint signals competence.

## Editor mapping
`style.zoom {every_s, scale, mode snap|smooth, on_emphasis}`, `texts[]` (title/lower_third cards), `audio.sfx[]` anchors, `pacing.max_shot_s`. Preset cadence per archetype: `style-sync-patterns.md`.
