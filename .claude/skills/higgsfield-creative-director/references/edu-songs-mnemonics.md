# Edu-songs, mnemonics and musical explainers

Klaus, 2026-10-25: "music and trend-jacking popular songs or classics... like science explainer channels doing covers of popular songs... learn from children's shows... my boring physio or men's health content can use those methods."

Use this for: "make it a song / rap / jingle / chant", "teach this with a rhyme", "make the exercise steps stick", "kids-show style", "parody of <song>".
Genre module: genre-playbooks.md §29 (`edu-song`). Tool: `editor.py song` (tools/editor/titan_editor/melody.py). Status: [draft]. This is first-principles plus the formats below; it has not been measured against our own analytics yet.

---

## 1. Why it works (what kids' TV figured out)
These are the levers the best preschool and edu-music shows use. Each lever has a physio or men's-health version.

| Lever | What it is | Physio / men's-health version |
|---|---|---|
| Melody = memory hook | A familiar tune carries new words for free; the brain already knows the rhythm. | Pelvic-floor routine to Twinkle Twinkle; posture checklist to Frère Jacques. |
| Repetition with one change per round | Verse 1 teaches, verse 2 repeats with one new move (cumulative songs like "Head, Shoulders, Knees and Toes"). | "Chin tuck… chin tuck AND shoulder roll… chin tuck, shoulder roll AND hip hinge". |
| Count-along / do-along | The song IS the timer: the reps live in the lyric. | "Squeeze for 1-2-3, rest for 1-2-3" so the viewer does the set while watching. |
| Call and response | Host asks, a pause, the answer comes. The pause makes viewers say it in their heads. | "Where does sciatica start?" (beat) "THE LOWER BACK!" |
| Pause for response | Dora-style: look at the camera and wait 1.5-2 s. | "Can you touch your toes? Try it now…" (2 s of beat only). |
| Chunking (3-5 items) | Never more than 5 facts per song; one per line. | "3 signs your back pain is NOT a muscle" as a 3-line chorus. |
| Mnemonic acronym | The first letters spell a word, sung as the chorus. | RICE / PEACE & LOVE (soft-tissue care); "FAST" style for red flags. |
| Recap song | The last 8-10 s re-sing the whole lesson fast. | A 4-line chorus recap before the CTA. |
| Mascot / puppet | A recurring character with one trait who asks the "dumb" question. | "Spine-y" the cartoon vertebra (animation-3d-cartoon.md), always slouching. |
| Movement = meaning | Every line has one gesture, the same one each time. | A hand gesture per step, filmed once, reused in every version. |
| Big, simple visuals | One object per frame, high contrast, bold colours, words on screen as they're sung (karaoke). | The muscle lights up as it's named; lyric captions bounce on the beat. |

Science channels' version: the song parody explainer, where a familiar structure carries dense facts (e.g. ASAP-style "covers", element and periodic-table songs, history raps). What they share: dense facts, strict scansion, a visual for every line, and the song arriving after a 3-5 s spoken cold-open hook, not as the hook itself.

---

## 2. Formats (pick one)
1. **Do-along routine song (30-45 s).** The exercise set is the song; viewers follow along. The best fit for physio (pelvic floor, desk stretches, ankle rehab). It saves-and-reshares well: "save this for your next desk break".
2. **Mnemonic chorus (15-25 s).** One 4-line chorus that makes an acronym or a checklist stick. For red flags, RICE / PEACE & LOVE, "when to see a physio".
3. **Myth-busting rap (30-60 s).** 8-16 bars over an original beat, one myth per couplet, each followed by the fix. For men's health ("no pain no gain", "cracking your back"). Use `editor.py song --rap`.
4. **Classic re-lyric (10-20 s).** Iconic public-domain melodies (Ode to Joy, In the Hall of the Mountain King; the tool's list) with new words. Short and funny; works as a hook or mid-roll gag. Mountain King's accelerando suits "the pain gets worse and worse" escalation.
5. **Jingle sign-off (3-6 s).** A brand's own 4-note sonic logo plus a 5-word line, the same every video. Build it once (original), reuse forever.
6. **Kids-show parody (adult audience).** Play the preschool-host grammar deadpan for adult topics ("Today we're learning about… prostate exams!"). The comedy comes from the format clash. Check the compliance pack before medical claims.
7. **Trend-jack (personal accounts only).** Write new words to a trending sound's rhythm, then post in-app with the platform's licensed sound. Never for brand or ad accounts (see §5).

---

## 3. Craft rules (where songs fail)
- **Scansion first.** One syllable per note, stresses on the strong beats. `editor.py song` counts syllables per line against the tune's phrase lengths and flags "cut 2 syllables". Fix every flagged line before recording. Off-meter lyrics are the #1 amateur tell.
- **Rhyme the line ends** (couplets, AABB) and keep the syllable counts within ±2 between couplet lines. The rap checker flags weak rhymes and uneven flow.
- **One fact per line, one action per line.** If a line needs a comma to make sense, split it.
- **Hook spoken, song second.** Open with a 2-4 s spoken or on-screen hook ("Your pelvic floor workout, but make it a nursery rhyme"), then drop the song. The song is the retention device, not the scroll-stopper.
- **Karaoke captions are mandatory.** Words highlight as they're sung (lyrics.srt + edu-song preset). Most people watch muted.
- **Accuracy over rhyme.** Never bend a clinical fact to fit a rhyme; change the rhyme. Every line passes the compliance pack (SG health: no superlatives, no guaranteed results, no testimonials).
- **Length:** a do-along runs exactly as long as the set. A chorus is 4 lines. A rap is 8-16 bars at 85-100 BPM, and should be readable at 1x.
- **Voice:** the brand's own person singing badly-but-committed beats a polished AI vocal for trust. Use AI or TTS only for a character or mascot voice (voice-persona-audio.md; never clone a real singer).

---

## 4. Workflow
1. Pick the format (§2) and the lesson. Get the facts from the brand's clinicians or sources; the compliance pack applies.
2. Write the lyrics: `/story` or script-doctor. Ask for "lyrics to <tune>, lines of N syllables" using the `editor.py song --list` phrase lengths.
3. Run `editor.py song --tune <tune> --lyrics lyrics.txt` (or `--rap --bpm 92`), then fix the flagged lines and re-run until all are ok.
4. Record the vocal over `song/guide.wav` (phone voice memo is fine), or have Klaus perform it on camera with the guide in an earpiece.
5. Make the mix: the vocal plus an original backing (the guide's beat, an original track, or a licensed library track). Then run `editor.py assemble --preset edu-song --music mix.wav --music-licence original`.
6. Captions: the edu-song preset gives bouncy karaoke captions from the transcript. For a pure song with no speech, load `song/lyrics.srt` in the final edit.
7. Visuals: one visual per line (B-roll match, an animation shot or a text card). Show the move on the exact line that names it.
8. QC: are the words intelligible at 1x, do captions match the sung words, is any line clinically wrong, and does the music licence hold?

---

## 5. Copyright and platform rules (read before using any existing song)
- **Public-domain compositions are safe to re-lyric and re-perform:** traditional nursery tunes and classical works whose composers died long ago (all of `editor.py song --list`). Only the composition is free. A specific recording or a modern arrangement is still protected, so perform or synthesise it yourself; never rip audio.
- **Copyrighted pop songs:** new lyrics on a copyrighted melody are a derivative work. Parody or fair-use defences differ by country and are decided case by case, so do not count on them for a brand. Rules:
  - **Brand, clinic and ad accounts:** original melodies or public-domain melodies only, and licensed or original audio only (studio hard rule). No pop-song parodies.
  - **Personal or creator accounts:** a trend-jack may be posted in-app using the platform's own licensed sound (TikTok/IG music library). It must stay in-app, with no reposting of the downloaded file elsewhere, and no ads or boosting of that post.
  - Want a pop song's FEEL? Write an original melody "in the style of" the genre (tempo, groove, instrumentation). Styles aren't owned; melodies are.
- **Happy Birthday and other "maybe" songs:** treat as not cleared unless confirmed for the target market.
- **AI music generators:** check the generator's commercial licence terms per track. Keep the licence note in the project, and never prompt "in the style of <named artist>" for a brand.
- When unsure, the deliverable goes out with original audio and the trend version is offered as "personal account only" proposal B.

---

## 6. Ready-to-adapt lyric seeds (fix scansion with `editor.py song`)
- **Pelvic floor do-along (Twinkle):** "Squeeze and lift and hold for three / Now relax and let it be / Ten a day, then rest a while / Stronger core and steady smile". The 7-syllable lines fit Twinkle exactly. The compliance pass removes any promised outcome for SG health.
- **Desk-break round (Frère Jacques), checked 8/8 by the tool:** "Chin tuck, chin tuck / Chin tuck, chin tuck / Shoulders back / Shoulders back / Stand up from the desk now / Stand up from the desk now / Walk it out / Walk it out".
- **Myth rap (92 BPM, original beat):** couplets of "myth → fix", e.g. "They said no pain, no gain, just push through the burn / Pain's a signal, not a medal, that's the first thing to learn".
- **Mountain King escalation (classic re-lyric):** the same 7-note line sung faster each round as the "desk posture" gets worse, ending in a comic crash, then the spoken fix.

These seeds are starting points; the brand voice, the brain's profile and the compliance pack decide the final words.
