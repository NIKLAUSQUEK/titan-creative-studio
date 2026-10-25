# Emotion QC

Run after every draft (with `scripts/qc_frames.py` / editor `qc`), against the Sync Map's emotion line per beat.

## Three passes [RoT; grounded in Cohen's Congruence-Association Model and Chion]
1. **Muted.** Does picture alone carry the story (faces, reactions, text)? Most feed viewing starts on mute: captions and on-screen text must carry the hook.
2. **Audio only, eyes closed.** Can you name each section's emotion from music, voice and SFX? Do risers resolve? Is every word intelligible over the bed?
3. **Together, at speed.** Do accents land where intended (drop within 2-3 frames of the reveal)? Are off-beat moments deliberate?

## Retention reading (after posting)
Cliff at 0-3 s = weak hook or mismatched opening sound · slow steady decline = no rising stakes / no interrupts · drop before payoff = setup too long · spikes = rewatched moments (replicate them) · end bump = loop works.

## Common mismatches → fix
| Mismatch | Fix |
|---|---|
| Happy music under a sad story (unless set-up irony) | swap mood row; or strip to room tone |
| Riser into nothing | resolve with hit or silence |
| Music melody fighting the voice | stems: drop melody, keep drums; more ducking |
| Hype sound on premium/health | calm/premium row; 0-2 SFX total |
| Stinger on a cruel beat (camera sides with the bully) | cold sound |
| Comedy cue under a sincere CTA | button the comedy, clean tail under CTA |
| Trend audio on a business account | CML/Sound Collection track with the same beat map |
| Drop lands off the reveal by > 3 frames | slip music or trim picture |
| Missing room tone (jump cuts audible) | lay continuous room tone |
| B-roll over the most emotional line | hold the face |
| Same shot length throughout (metronome) | vary lengths around the energy average |

Log the verdict per beat (PASS/FIX) in `projects/<p>/SYNC_MAP.md`; recurring misses → `/learn`.
