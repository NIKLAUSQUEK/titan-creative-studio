# Part 5-6 v4: proper coverage (Klaus: "skips, too fast, not like a screenplay, voice doesn't match the mouth")

Rules for this cut:
- **Whoever speaks is on screen, lip-synced.** Seedance 2.5 `omni_reference` with the ElevenLabs line as `audio_references`.
- **Thoughts play over a close-up of Hân with her mouth closed**, as a slightly softer voice-over.
- **Every line gets a reaction beat** (0.4-0.8 s) on the listener. Natural pauses, no speed-up, no frozen frames.
- **Shot sizes move from wide to close** as the tension builds; the café geography stays fixed (Jake on the left, Hân on the right, window behind).

| # | Shot | Who's on screen | Audio | ≈s |
|---|---|---|---|---|
| 1 | WIDE café, Hân sits opposite Jake | both | hook text "he said 'I know you want it'…"; café ambience | 2.0 |
| 2 | CU Hân | Hân (lip-sync) | "Hi… J?" | 1.6 |
| 3 | CU Jake, slow smirk | Jake (reaction) | — | 0.8 |
| 4 | CU Hân, mouth closed, glancing at his eagle shirt | Hân (thought VO) | "Okay. This is easier than it looks. He's a G.I. Just say no to his advances." | 4.0 |
| 5 | MCU Jake leaning on his elbows | Jake (lip-sync) | "So, is it hot in Saigon, or is it just you?" | 3.0 |
| 6 | CU Hân, awkward polite laugh | Hân (reaction) | small nervous laugh | 0.8 |
| 7 | 2-SHOT, his arm along her chair | Jake (lip-sync) | "Relax. I don't bite. Unless you ask nicely." | 3.6 |
| 8 | CU Hân, mouth closed | Hân (thought VO) | "Just say no. Say it nicely though!" | 2.4 |
| 9 | CU Jake leans in, puckering | Jake (lip-sync) | "Come on… I know you want it." | 2.2 |
| 10 | CU Hân tipping back, chair creaks | Hân (thought VO) | "How do I say no nicely?!" | 1.8 |
| 11 | (splash SOUND over black, 0.3 s) → CU damp jeans, Hân looks down | Hân (lip-sync, out loud) | "Wait… did I just…?!" | 2.0 |
| 12 | REWIND, "2 seconds earlier…" | — | tape-rewind whine | 0.8 |
| 13 | WIDE: Trâm flings the water | all | splash + café gasp | 1.4 |
| 14 | CU Hân, relief | Hân (thought VO, exhale) | "Oh thank god. It was her." | 1.9 |
| 15 | LOW MCU Trâm | Trâm (lip-sync) | "CLIENT MEETING, JAKE?!" | 1.9 |
| 16 | MCU Jake soaked, hands up | Jake (lip-sync) | "Babe! This is… my… accountant?" | 3.1 |
| 17 | end card | — | "Part 7 →" | 1.2 |

**New lip-sync renders:** shots 2, 5, 7, 9, 11, 15, 16 (7 × 12 credits at 480p ≈ 84).
**Reused:** shots 1, 3, 4, 6, 8, 10, 13, 14 (existing clips and stills).

## v5 (30 Oct 2026): one continuous scene
After Klaus said "feels like a lot of individual parts" and shared the reference reel DfD0qcCMqJy:
- **Re-shot** (v5/): opening wide `s2`, two-shot `s7` and the lean-back `t10`, all in the same café with Hân LEFT and Jake RIGHT and a calm crowd. v4's `s7` was in a different café with the sides flipped, and `c5` already showed the splash water.
- **Edit** (`assemble_p56_v5.py`):
  - one timeline, with continuous café ambience and an original music cue;
  - J-cuts and L-cuts on every line, so each line starts under the previous shot;
  - an eyeline insert on the eagle shirt;
  - the "just say no" thought split over a cutaway of his arm on her chair;
  - thought VOs with their inner pauses tightened to 0.25 s, at natural speed;
  - music dies on "I know you want it", then a splash hit, then a comedic bounce;
  - word-by-word captions;
  - the last frame freezes with "Part 7 →" over it.
- Cost: 4 stills (6 credits) + 3 clips at 480p (36 credits) ≈ 42 credits. Output `pi_job_part5-6_v5_480p.mp4`, 27 s.
