# editbymmh (Metro Media House): sound-design study, refs ed04-ed09 (2026-10-25)

Refs: ed04 (AE wiggle tutorial, 9:16) · ed05 Ozempic / White Castle · ed06 FaceTime → OnlyFans · ed07 Bill Ackman · ed08 Robert Pattinson · ed09 Christopher Nolan.
Inputs: `scratchpad/refs/b2/pack/<id>/` (meta.json, transcript, sheet, hook), plus the raw mp4s. All audio measurements below come from my own numpy analysis of the final mix: 22.05 kHz mono, 10 ms hop. The scripts are `scratchpad/agentB/analyze.py`, `eta.py`, `extra.py` and `zoom.py`. Log-frequency spectrogram crops are `scratchpad/agentB/zoomA.png` and `zoomB.png`.
I studied these for technique only. No reference audio or footage goes into our edits.

**About the "timeline" panel.** ed05-ed09 are 16:9 breakdown reels: "Final output:" on the left and "Sound design:" on the right, over a blurred backdrop with a CTA line ("Learn from timeline or hire the team" / "Want this for your content? Link in bio"). The panel is a **Final Cut Pro** timeline, not After Effects. You can tell from the green audio clips with `fx` badges, the "1" channel badges on the primary storyline, the ♫ music-clip icon and the role-coloured lanes. It is a static screenshot that changes page at section boundaries: a frame-diff test on ed07 shows no scrolling between 28 and 49 s. The zoom is too far out to read clip names. **The panel has no legible layer names.** The SFX vocabulary below therefore comes from the audio itself (spectrogram shapes, band envelopes) and is marked [inferred] wherever it names a sound type. ed04 is the only After Effects reel, a 9:16 tutorial showing the AE Transform/`wiggle()` workflow.

What the panel does show (ed07 at 30 s, zoomed 3×):
- Up to **~12 stacked SFX lanes** under the dialogue storyline, plus one long music clip spanning the page (♫ icon, fade handle at the end).
- About **35-40 SFX clips per page**, with **5-8 clips overlapping the playhead at once**.
- Clip shapes are of two kinds. Many are short with an early waveform spike (hits and ticks). The rest are 1-3 s long with a slow hump or a long decay tail (swells and booms). Several have visible fade-out handles.
- ed05, ed08 and ed09 panels use FCP role colours: green lanes at the top (dialogue/music) and a dense column of purple (ed05/ed08) or red/pink (ed09) short clips underneath. That column is the effects role [inferred colour mapping].

---

## 1. Measured numbers

"Cut events" = meta.json cuts merged when they fall within 150 ms of each other. Their reels use 2-5-frame flash/stutter bursts, which the detector reports as several cuts. "Strong transients" = spectral-flux peaks above 4× the median flux and above an adaptive median+3·MAD threshold. These include some speech plosives, so read them as a ceiling on SFX hits. "ETA" = event-triggered average of band energy around every cut event, minus the average around 2,000 random times. It is the most robust measure of "what happens on a cut".

| ref | dur s | cut events /10 s | burst cuts | median shot s | wpm | LUFS | strong transients /10 s | decay of transients (median, s) | cut events with a transient ≤250 ms | ≤80 ms (chance) | transient-minus-cut lag, median (IQR) ms |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ed04 | 44.0 | 3.0 | 6 | 0.54 | 188 | -14.3 | 9.5 | 0.17 | 0.38 | 0.15 (0.14) | +26 (-49..+80) |
| ed05 | 85.4 | 8.5 | 7 | 0.63 | 195 | -14.4 | 17.6 | 0.43 | **0.63** | **0.44 (0.26)** | **-28 (-47..+44)** |
| ed06 | 77.9 | 10.1 | 20 | 0.45 | 163 | -14.2 | 4.5 | 0.67 | 0.22 | 0.10 (0.07) | +20 (-136..+76) |
| ed07 | 94.9 | 11.0 | 33 | 0.32 | 159 | -14.1 | 8.0 | **1.69** | 0.37 | 0.12 (0.12) | -7 (-81..+174) |
| ed08 | 76.6 | 7.4 | 3 | 1.05 | 203 | -14.2 | 6.1 | 0.36 | 0.40 | 0.09 (0.09) | -86 (-162..+77) |
| ed09 | 103.4 | 5.3 | 6 | 1.16 | 164 | -14.1 | 10.4 | **2.24** | 0.47 | **0.35 (0.16)** | **-18 (-46..+53)** |

| ref | HF 5-11 kHz around cuts: peak dB @ ms | sub 20-90 Hz around cuts: peak dB @ ms | HF click transients /10 s (share within 80 ms of a cut) | sub booms /10 s | dropouts ≥80 ms at -18 dB, per min | level p5 / p50 / p95 dBFS (100 ms) | share of time below -30 dBFS |
|---|---|---|---|---|---|---|---|
| ed04 | +6.9 @ +494 (few cuts) | +6.8 @ +100 | 1.6 (0.00) | 0.45 | 4.1 | -34.0 / -20.5 / -12.1 | 11.6 % |
| ed05 | +6.3 @ **-50** | +0.9 (none) | 2.7 (**0.39**, lag -29 ms) | 0.35 | 1.4 | -28.3 / -18.3 / -11.1 | 2.8 % |
| ed06 | +3.5 @ +279 | +4.2 @ +120 (90-300 Hz: +5.9 @ +75) | 0.3 | 0.13 | 0.8 | -28.9 / -17.6 / -12.0 | 4.2 % (mostly outro) |
| ed07 | +4.1 @ **+80** | +2.4 @ +40 | 1.6 (0.07) | 0 | 0.6 | -32.5 / -17.5 / -12.1 | 6.3 % (mostly outro) |
| ed08 | +5.0 @ **0** | +3.9 @ -80 | 0.9 (0.14) | 0.52 | 3.1 | -29.7 / -18.3 / -11.8 | 4.6 % |
| ed09 | +4.7 @ **+145** | +2.8 @ +125 | 2.6 (0.22, lag -1 ms) | 0 | 0 | **-23.3** / -16.7 / -10.9 | **1.5 %** |

Spectral-flux density per 10 s (all onsets: speech + SFX) stays at 43-57 in every ref. The rate never sags, because the gaps between words are filled.

How to read these numbers:
- **Not every cut gets a sound.** Between 22 % and 63 % of cut events carry a transient within ±250 ms. ed05 (tight hits) and ed09 (tonal hits) sit clearly above chance at ±80 ms. ed07 and ed08 do not.
- **ed07 and ed09 are "long" mixes.** Transient tails run 1.7-2.2 s: swells, booms and reverb tails rather than dry clicks. Their lag histograms put the mass at **-250..-80 ms and +150..+250 ms**. Swells start before the cut and the tails ring after it, so the sounds aren't stuck on the frame. The caption "We went long on sfx" seems to be literal [inferred].
- **Cuts are wrapped in HF energy** (whoosh/air/noise), +3.5 to +7 dB above the average, peaking between -50 and +145 ms. The median is roughly +40..+80 ms after the cut. Our whoosh placement (+37 ms peak) is in range but on the early side.
- **Low-end (sub/low) energy rises +2.5..+7 dB, peaking +40..+125 ms after cuts** in 5 of 6 refs (ed05 is the exception). That is an impact/sub layered with the cut, with its body arriving after the frame.
- **There is almost never silence.** Below -30 dBFS for 1.5-4.6 % of runtime, excluding the AE tutorial and the outro tails. p5 sits at -23..-32 dBFS, i.e. a bed (music/drone/room tone) runs about 6-15 dB under the voice at all times. Loudness is -14.1..-14.4 LUFS on every ref, which already matches our `loudness: -14`.
- **Silence is a rare, deliberate device.** Dropouts of 0.1-0.4 s happen 0-4 times a minute: most in ed04 (didactic) and ed08 (cold-open → narrator), none in ed09.

---

## 2. Per reference

### ed04: "One line of code" AE tutorial (9:16, 44 s, 17.4k likes, the top performer)
- **Hook (0-3 s):** "Look at this edit. Nothing special, right?" over a collage card (Jack-of-spades card, Greek columns, money). A centred word-by-word caption with green highlight boxes. The image drifts subtly; that drift is the point of the lesson.
- **Structure:** demo (look) → contrast (turn movement off → "goes flat", 5.1 s) → indictment ("that's what most of your edits look like") → step-by-step AE screen recording (adjustment layer → Transform → `wiggle(3,12)`) → payoff ("Eight seconds of work…") → reaction memes (Mr Bean, Lego) → sass CTA ("noobs") → logo sting.
- **Edit grammar:** 3.0 cut events/10 s, but each "shot" moves (UI zooms, menu pops). Captions are one word, centred low, with a pill highlight. AE UI close-ups are cropped to the menu item being said ("adjustment", "Distort", "Transform"). The meme punch-ins sit on a white or black field. The end is the m-logo on black with 3 diagonal line wipes.
- **Sound:** the sparsest mix of the six and the only one with real silence (11.6 % below -30 dBFS). There are deliberate holes at 0.74 s (0.32 s) and 4.75 s (0.37 s), just before "But if you look closely" and "Now turn that movement off… flat". This is **silence used as the demonstration of flatness**. 15 of the 42 strong transients are sub thumps. There are dry UI clicks/pops on the menu actions [inferred from 1.6 clicks/10 s plus the UI visuals]. Decay is short (0.17 s): dry tutorial sound.

### ed05: "A 5 cent burger is the reason Ozempic is a $70B drug" (85 s, "The sound design has the same job the sugar does")
- **Hook:** the burger spins in from blurred to sharp over 0.75 s ("5 cent burger" in tiny type over it). Then a glitch frame (1.25 s), then a red "1921" stamp counting in over a b/w archival collage. Then a white card where the words "is the [redacted bar] reason" type in. The **redaction-bar reveal** is a recurring device.
- **Structure:** paradox claim → present (GLP-1s everywhere) → "someone built it" → 1921 origin (White Castle, The Jungle, clean white walls) → the system (assembly line, copied by everyone) → a century of engineered eating (sugar, lab snacks) → twist ("GLP-1s turn off the craving") → callback punchline ("every Big Mac is an Ozempic pre-order", "$50 a week to undo what a 5 cent burger started").
- **Edit grammar:** 8.5 cut events/10 s, 0.63 s median shot. White editorial "paper" cards with black grotesk type alternate with archival b/w photos. Giant numbers and words are stamped in red or black ("1921", "OWN", "SAME BURGER", "ACCIDENTALLY", "$70 Billion"). There are scribble/arrow overlays, pills and pens flying across, b/w with red accents, eye/mouth macro close-ups (eating) and a data-mosh frame. Quote cards show the speaker on a dark-blue newsroom background.
- **Sound:** the **tightest hit-on-cut mix**. 63 % of cut events carry a transient. 44 % carry one within ±80 ms against 26 % chance, with a median lead of **-28 ms** (IQR -47..+44). Strong transient density is the highest of the set at **17.6/10 s**, peaking at 38/10 s in the 70-80 s climax. HF peaks at -50 ms, so the attack is slightly ahead of the frame. In the 4.3-5.5 s cut burst the spectrogram shows a vertical broadband line on every cut: a **tick/typewriter train synced one-per-frame-burst** to the redaction/type-on card [inferred: typewriter or UI tick]. There are sub booms at 0.96 s and 2.2-2.6 s, a long 60 Hz body under "$70 billion" [inferred: the "billion" stamp gets a boom]. The music bed is low and almost tonal-free in the low end (a stable-bass proxy shows ~9 % of frames) [inferred: textural/percussive bed, not a melodic track].

### ed06: "This man is the reason the entire adult industry exists" (78 s, "What are you addicted to?")
- **Hook:** b/w Steve Jobs portraits snap in as photo cards on black. A pixel-glitch frame lands on his face. Then a dark field fills with floating icons (OnlyFans logo, peach and cherry emojis, "Adult Industry" neon type, photo tiles), one popping in per word.
- **Structure:** taboo claim → mystery ("one thing this man put in your hands in 2010") → reveal via archival keynote ("We call this… FaceTime") → irony ("He wanted you to call your mom") → consequence chain (creators → paid → money: "Show me the money!" movie clip) → stats ($8 B/yr, 18-year-olds out-earning surgeons) → ironic closer (Apple still bans adult apps).
- **Edit grammar:** 10.1 cut events/10 s, with the most burst cuts (20 stutter clusters). Black backgrounds with object cut-outs. Lips/mouth macro inserts. A bar-race chart. A blood-red ink splash card. Money macro (Franklin's eye). Movie-quote insert.
- **Sound:** fewer sharp transients (4.5/10 s) but longer ones (0.67 s decay). Around cuts the **90-300 Hz band** rises +5.9 dB at +75 ms: a low "thump/body" layer rather than a click. On the FaceTime reveal (21.6-22 s) the spectrogram shows a **sustained low tone building from ~20.9 s through the 22.0 s cut burst and carrying on after it**: a sub swell into the reveal, then held [inferred: sub drone/riser → boom]. There is one 0.23 s boom exactly on the 11.57 s cut ("put in your hands"). The panel shows many long green clips on separate lanes: overlapping beds and swells rather than single hits.

### ed07: Bill Ackman, "the investor every CEO is afraid of" (95 s, "We went long on sfx. It keeps paying.")
- **Hook:** the poker-table clip. Words appear one at a time in small white sans ("The / is / the / investor"). A white flash card, then a colour-negative/neon flash, then a red **x-ray outline of him** (1.0-1.25 s). Then a grid of CEO face tiles populates around him, one per word ("every CEO in America").
- **Structure:** fear claim → "real Wolf of Wall Street" → legality question → name reveal → MBIA short (2002, "fraud") → 6 years of ridicule → 2008 vindication ($1.4 B) → Icahn "Carl, f*** you" → Herbalife reversal (lost) → present-day threat → "Neither does Ackman."
- **Edit grammar:** the fastest cutter (11 cut events/10 s, 0.32 s median shot, 33 burst clusters). It mixes AE tracking-data overlays ("x: 864 y: 63" crosshair boxes, dashed motion paths), shattered-glass/pixel-sort transitions, a red stock-crash line, Goldman/AAA/MBIA logos, a news chyron "WORST NOT OVER?", money macros, Pac-Man, a Herbalife pyramid diagram, and kinetic words that grow ("tried to **bury** him").
- **Sound:** **long-tailed design.** Transient decay median 1.69 s. The lag histogram is bimodal: 10 events at -250..-80 ms (swells starting before the cut) and 15 at +80..+250 ms (tails/booms after). ±80 ms alignment is only at chance (0.12). The cuts are wrapped in swells, not stamped with clicks. HF peaks +80 ms after the cut, sub at +40 ms. On "Carl, f*** you" (61.5-63.3 s) the spectrogram shows a **pitched sweep (rising tonal lines) for ~1.3 s into the 63.2-63.6 s cut burst, then a low-end bloom**: a riser → impact/sub stack on the punchline [inferred]. Around "Then, 2008 hit" (35.5-39.5 s) a steady 50-100 Hz bed runs under the voice: a drone/score bed held through. The panel page at 30 s shows about 8 SFX clips concurrent at the playhead.

### ed08: Robert Pattinson, "on a run we haven't seen in a very long time" (77 s, "He never plays it safe, neither does this timeline")
- **Hook:** a **9-second cold open of film-clip performances**: shouting scenes from his films, a talk-show clip and "UGLY" title type. Then the narrator takes over at 9.8 s.
- **Structure:** cold-open montage → thesis → the Twilight trap → "he becomes them" (voice/body transformations) → the throne promised to Gyllenhaal → picks roles that scare others → filmography list ("Seven films this decade") → Al Pacino 1972-76 comparison → "he's the only one in it".
- **Edit grammar:** slower (1.05 s median shot, 7.4 cut events/10 s), letting film clips play. Film titles are set in big serif type ("Twilight", "The DEVIL ALL THE TIME", "AL PACINO", "SOUNDS" in red). Quote cards with huge quote marks ("He never had to — say it out LOUD"). White paper cards with a poster collage. A red-curtain grade on the closer.
- **Sound:** a **dialogue-led mix with silence as a section break.** Low-band energy drops for ~0.4-0.7 s (8.3-9.0 s, measured dropout at 8.62 s) right before the cold open hands over to the narrator. At 9.0 s a broadband noise wall enters (whoosh/impact transition), and a sub punch hits the 9.75-9.93 s cut burst. There is a second dropout at 24.19 s before "Turns out, anything he wants." HF peaks **exactly on the cut (0 ms)**. Sub/low energy **leads** the cut by 65-80 ms: the boom body starts before the picture changes [inferred: a pre-lap hit]. There are 4 sub booms, 25 % of them on cuts. Film-clip dialogue is used as SFX ("I am better than you" lands as a sting).

### ed09: Christopher Nolan, "the closest thing we have to a modern Kubrick" (103 s, "SFX that Zimmer would definitely approve")
- **Hook:** behind-the-scenes Nolan footage plus a viral interview quote ("My life is like a Christopher Nolan movie…", 0-10 s). Then the stat card: "**12**" stamped on white with flying photo tiles, then "**All Hits**".
- **Structure:** meme cold open → stat (12 films, all hits) → "internet thinks he's finished" pattern → Odyssey doubt (Bronze-Age armour, casting, Travis Scott) → vindication ("masterpiece") → precedent (Heath Ledger's Joker) → filmography montage (Memento, Inception, Tenet) → "keep doubting him".
- **Edit grammar:** 5.3 cut events/10 s, 1.16 s median shot. Editorial white "paper" cards with postage-stamp and photo collages. Tweet and Reddit screenshot cards. Big red words ("SCARED", "ANCIENT"). Letterboxed film clips with small word-by-word captions. "TENET" title type.
- **Sound:** the **densest bed, with no true silence**. p5 is -23.3 dBFS, the time below -30 dBFS is 1.5 % and there are 0 dropouts. Decay median 2.24 s: score-like booms and tails ("Zimmer"). Cut-locked hits are clearly above chance (0.35 vs 0.16, median -18 ms). On the "12 films" reveal (10.22 s) the low band empties about 150 ms before the cut (9.9-10.05 s). A broadband swell starts ~170 ms before the cut and peaks on it. Then a **sustained sub bloom runs from 10.1 s to beyond 12 s**: the classic *bed hole → swell → BRAAM/sub hit on the reveal*. The 2.2-3.0 s cut burst (5 cuts) has a harmonic stack with one vertical hit per cut [inferred: tonal stabs/piano hits]. The panel shows the effects lanes in a red/pink cluster stacked 6-10 deep in the middle of the page.

---

## 3. The editbymmh sound-design rulebook (for the auto-editor)

**R1. There is a bed under everything.** Music, drone or texture runs continuously at **6-15 dB under the VO**; p5 short-term level should stay ≥ -30 dBFS. True silence makes up ≤ 3 % of runtime and is always deliberate (R7). Ducking is shallow: keep the bed 6-10 dB under speech, never pumped to nothing.

**R2. Density.** Aim for **6-10 discrete SFX events per 10 s** in story reels: ed05 = 17.6 strong transients/10 s incl. plosives, ed09 = 10.4, ed07 = 8 plus long swells. Peaks of 15-20/10 s are fine in the climax (ed05 70-80 s = 38 transients). Expect **3-8 layers concurrent** on dense moments (panel). Split the budget roughly like this:
- cut-attached: **40-60 % of cut events** get a sound (measured 22-63 %), giving 2-5 per 10 s
- text/type-on ticks: 1.5-3 per 10 s (HF click rate 1.6-2.7/10 s)
- reveal stacks: 1 per 8-15 s
- the beds.

**R3. Map events to sounds.** Each row lists the visual event, the sound for it and how it is placed against the cut/event (t = 0).

| visual event | sound | placement vs cut/event (t = 0) |
|---|---|---|
| hard cut to new B-roll / archival | whoosh (air/noise), optional low thump | whoosh **peak +40..+80 ms**; thump onset -10 ms (body peaks +40..+120 ms) |
| stutter / flash-frame burst (2-5 cuts in <150 ms) | glitch burst **or** one tick per flash frame | first onset -20..-30 ms; ticks onset -5 ms on each frame |
| word-by-word kinetic text, typing, redaction bar | tick / typewriter key / soft UI click per word (not every word: about 1 in 2) | onset -5..-30 ms vs the word's appear frame |
| photo/card slams in (collage tiles, "1921" stamp) | shutter / paper slap / pop, plus a sub on the big number | onset -10..-30 ms |
| big number or stat ("$70 Billion", "12", "$1.4 billion") | **stack**: swell (0.4-1.0 s, peak on cut) + impact + sub/boom (tail 1-2 s) | swell peak 0 ms, impact onset -10 ms, sub onset -10 ms |
| section turn / reveal / punchline ("FaceTime", "Carl, f*** you", "12 films") | **stack**: bed hole 150-400 ms → riser/swell (0.8-1.5 s) peaking on the cut → impact + sub boom → bed returns, often a new cue | bed drop starts 150-250 ms before the cut, riser peak 0 ms, impact/sub onset -10..-30 ms |
| cold-open → narrator handover | 0.3-0.7 s silence, then a broadband whoosh/impact into the title | silence ends on the transition frame |
| movie / news / meme clip insert | let the clip's own audio play as the SFX (quote = sting), with the bed ducked deeper (-12 dB) | clip audio starts on the cut |
| money, phone, camera, food on screen | literal foley (cash, phone buzz, shutter, crunch) [inferred: typical of the genre; not verifiable from the mix] | onset -10 ms |
| outro / logo | swell into the logo, then line wipes with whoosh ticks; music tail fade 0.5-1 s | logo hit onset -10 ms |

**R4. Offsets (measured).**
- Tight hits: onset **-20..-30 ms** before the frame (ed05 median -28, ed09 -18; IQR ±50 ms).
- Air/whoosh: energy peak **+40..+80 ms** after the frame. The HF peak range across refs is -50..+145 ms.
- Sub/low: peak **+40..+125 ms** after the frame. Use onset -10 ms and let the attack carry it. ed08 uses a **pre-lap** where the low body starts 65-80 ms before the cut, for the heaviest moments.
- Swells/risers: start **150 ms-1.5 s** before the cut, peak on the frame (ed09 swell starts -170 ms; ed07 tonal riser runs about 1.3 s).
- Long tails are allowed to ring **1-2 s** across the next shot. Do not cut SFX tails at the next edit.

**R5. Layer the reveals.** The signature move appears in ed09, ed07 and ed06:
1. Bed hole (low band out for **150-400 ms**).
2. Swell or riser peaking on the cut.
3. Impact with a sub boom; the sub tail lasts 1-2 s.
4. Bed returns, louder or as a new cue.

Use it 1 time per 8-15 s at most. Less frequent beats are reserved for the 2-3 biggest beats. Gains for the reveal stack:
- impact at -8..-10 dB
- sub at -10 dB
- swell at -14..-16 dB
- everyday cut whooshes at -16..-18 dB

**R6. Vary everything.** Never the same take twice in a row; vary gain ±3 dB per cue. Not every cut, not every word: ~50 % coverage keeps the hits meaningful. Short ticks (dry, <0.2 s) and long swells (1-2 s tails) are mixed in one reel. The "long" style of ed07/ed09 has a median tail of 1.7-2.2 s; the "tight" style of ed05 has 0.4 s.

**R7. Silence as emphasis.** Use 0.1-0.4 s dropouts **0-4 per minute**, placed:
- immediately before the line the hook demonstrates (ed04 "goes flat")
- at the cold-open → narrator handover (ed08 8.3-9.0 s)
- before a twist line (ed08 24.2 s).

Never leave silence in two consecutive 10 s windows.

**R8. Loudness.** Master at -14 LUFS integrated, TP ≤ -1 dBTP. Short-term p95-p5 spread is 12-23 dB (100 ms windows): dense but not brick-walled.

**R9. Two sub-styles to expose as presets/variants:**
- **tight** (ed05): cut coverage 60 %, offsets -28 ms, ticks/typewriter, short tails 0.3-0.5 s, density 12-18/10 s.
- **long/cinematic** (ed07/ed09): cut coverage 40-50 %, swells straddling cuts (-250..+250 ms), booms with 1.5-2.5 s tails, a continuous score bed, density 8-10/10 s.

---

## 4. Our engine vs the rulebook

**What `tools/editor` already does** (`titan_editor/sfx.py`, `recipe.auto_sfx`, `render.py` mix):
- 11 kinds: whoosh, impact, pop, ding, riser, click, bass, sting, scratch, shutter, drone.
- Takes come from the library, then Earshot, then the synth, and rotate per cue.
- Each file's onset and peak are measured; placement is by role: hits/pops/clicks onset -10/-11 ms, whoosh **peak +37 ms**, riser **peak on the cue**. These match the measured windows: whoosh is at the early edge of +40..+80, and hits could move 10-20 ms earlier.
- The mix has music with a sidechain duck (ratio 6, attack 15, release 350) and loudnorm to -14 LUFS with the limiter. The drone bed is synthesised only when `music.energy == "drone"` and no music is given.
- `auto_sfx` builds cues from three sources only: **hook** (item 0), **B-roll in** (-80 ms) and **zoom snaps**. It caps them with `round(density_per_10s × duration / 10)` and drops lower-priority cues by list order.

**Gaps:**
1. `_defaults.json` maps `title → pop` and `end → riser`, but **`auto_sfx` never reads `map.title` or `map.end`**. Also, cues at or after `total` are skipped in render, so an end-card riser can't fire. Text events produce no sound at all.
2. There are **no cut-attached cues**: item boundaries (jump cuts), beat/section boundaries and B-roll *outs* get nothing. The reference sound is mostly cut-driven (40-60 % coverage).
3. **One sound per cue.** There is no stacking, so the reveal stack (swell + impact + sub) and the "whoosh + low thump" cut cannot be expressed.
4. **No music automation.** There is no bed hole/drop before a reveal, no clip-insert duck, and no "new cue after the reveal". The duck depth is fixed (ratio 6). There is no floor guarantee: the bed can be ducked to near-silence.
5. **No silence beats** (R7) and no cold-open handover gap.
6. The density budget is a single number with no `min_gap_s`, no per-source quotas and no reserve for big moments. Hook > B-roll > zoom ordering means a 90 s reel spends its budget early.
7. **Missing kinds:**
   - `swell` (reverse cymbal / reverse whoosh, 0.4-1.5 s, align peak 0 ms; distinct from the tonal `riser`)
   - `tick` (typewriter / soft UI tick, 0.01-0.15 s, onset -5 ms)
   - `glitch` (digital stutter 0.1-0.5 s, onset -20 ms; today it is borrowed by `scratch` via earshot `pro_glitch`)
   - `boom` (sub hit with a long 1.5-3 s tail, onset -10 ms; current `bass` is capped at 3 s and filtered for 120 ms attack, keep that)
   - `paper` (photo/card slap, onset -10 ms)
   - `tape_stop` (end-of-section stop, align **end** on the cue)
   - `foley:<noun>` (Openverse query per noun, e.g. cash register, phone buzz)
   - `texture` bed (film crackle / room tone loop to keep the floor when there is no music).
8. **Gain is flat per role:** `db`, with +2 for the hook and -2 for zooms. There is no ±3 dB jitter and no per-kind gain table, so the reveal stack can't sit hotter than everyday whooshes.
9. **Scale.** A dense reel is about 60-100 SFX inputs for 90 s, and `render.py` adds every cue as an ffmpeg `-i` input and an `amix` leg. Pre-mix the SFX into one stem (a numpy mixer reading the measured files, then a single input) or chunk the `amix`, or dense presets will choke ffmpeg's input/filtergraph limits.
10. **QC is blind to sound.** Add a sound check to `qc.py`, reusing the analysis in `scratchpad/agentB/analyze.py` and `extra.py`. It should report:
    - strong transients/10 s
    - share of cut events with a transient within ±250 ms
    - lag median
    - share of time below -30 dBFS
    - dropouts/min

    and compare them against preset targets (`sfx.qc_targets`).

**Changes in priority order:**
1. **Event sources in `auto_sfx`:**
   - `cut` (every item boundary after the first; apply a `cut_coverage` probability, deterministic by hash)
   - `cut_burst` (boundaries <150 ms apart collapse to one cue)
   - `section` (first item of a new beat)
   - `title` / `label` / `hook_text` appear, giving a `tick` per text event; for word-by-word captions, one per N words via `title_word_every`
   - `broll_out`
   - `number` (caption/text token that is a number or currency; this needs captions emphasis data)
   - `end` (re-anchor at `total - 0.05` into the body, or let render add end-card cues).
2. **Stacks:** `sfx.stacks = {"reveal": [{"type":"swell","db":-15},{"type":"impact","db":-9},{"type":"boom","db":-10}], "cut": [{"type":"whoosh","db":-17},{"type":"bass","db":-20,"p":0.3}]}`. `map` values may name a stack. Each layer keeps its own role placement from `KINDS`.
3. **Music automation in render:**
   - `music.drop_before_reveal_s` (0.15-0.4): a `volume` with an `enable=between(t,a,b)` envelope or `afade` pairs that pull the bed down `drop_floor_db` before every reveal-stack cue.
   - `music.duck_depth_db` instead of the fixed ratio 6, e.g. map to threshold/ratio so the bed sits about 6-8 dB under the VO.
   - `music.insert_duck_db` for clip inserts with their own audio.
   - `music.bed_always`: when there is no music, insert the `texture`/`drone` bed at -26 dB.
4. **Silence beats:** `sfx.silence.before = ["hook_line_2", "section_after_cold_open"]`, `len_s 0.25`, `max_per_min 3`. This mutes bed and SFX for that window; the voice stays.
5. **Budget:**
   - `min_gap_s` 0.12 between discrete hits; beds and tails are exempt
   - per-source quotas
   - reserve 15 % of the budget for `reveal`
   - spread cues over time, a round-robin per 10 s window instead of a list cut.
6. **New kinds** as in gap 7, plus `gain_jitter_db` and per-kind `db` defaults.
7. **Offset tweaks:**
   - hits -10 → -20 ms for the `tight` style
   - whoosh peak +37 → +55 ms in `long` presets; leave the default
   - add `pre_lap_ms` for boom (-70 ms) on reveal stacks (ed08).
8. **SFX stem pre-mix** (gap 9), then **QC targets** (gap 10).

---

## 5. Preset: `story-sfx-dense`

The schema follows `tools/editor/presets/*.json`. Keys the engine reads today are used as-is. Keys that need new engine code are listed in `_needs_feature` and are ignored by the current `resolve_style` merge until built. Captions follow the editbymmh look: small, centred, 1-3 words, white, no box. Cards and B-roll are frequent and short. This preset was not written to `tools/editor/presets/`, per the task scope; copy it there to use it.

```json
{
  "name": "story-sfx-dense",
  "label": "Story edit, SFX-dense (editbymmh / Metro Media House)",
  "kind": "style",
  "description": "Founder/celebrity story reels: VO-led, archival + editorial white cards, cut every ~0.5 s, word-by-word small captions, and a sound layer on almost everything. Continuous bed, 40-60 % of cuts carry a whoosh/thump, ticks on type-ons, swell -> impact + sub-boom stacks on reveals with a 150-400 ms bed hole, rare silence beats. Measured on ed04-ed09 (research/refs-2026-10-25/editbymmh-sound.md).",
  "reference": "research/refs-2026-10-25/editbymmh-sound.md",
  "structure": {
    "name": "story-short",
    "target_s": [45, 100],
    "beats": ["paradox/claim hook 0-3s", "context", "origin", "escalation", "twist/reveal by ~65%", "callback punchline", "logo sting"]
  },
  "pacing": {
    "remove_silence_over_s": 0.25,
    "pad_s": 0.05,
    "remove_fillers": "hard",
    "max_shot_s": 2.5,
    "drop_retakes": true
  },
  "captions": {
    "max_words": 2,
    "animation": "pop",
    "size": 0.034,
    "position_y": 0.5,
    "uppercase": false,
    "keyword_caps": false,
    "highlight": "#FFFFFF",
    "outline": 0,
    "shadow": 1
  },
  "hook_text": {
    "enabled": true,
    "max_words": 6,
    "size": 0.06,
    "uppercase": true,
    "position_y": 0.45,
    "dur_s": 1.6
  },
  "zoom": {
    "mode": "snap",
    "every_s": 2.0,
    "scale": 1.05,
    "on_hook": 1.1,
    "on_emphasis": true
  },
  "broll": {
    "every_s": 1.5,
    "max_dur_s": 1.6,
    "min_dur_s": 0.4,
    "mode": "full"
  },
  "sfx": {
    "density_per_10s": 8,
    "db": -16,
    "map": {
      "hook": "impact",
      "zoom": "whoosh",
      "broll": "whoosh",
      "title": "tick",
      "end": "swell",
      "cut": "cut",
      "cut_burst": "glitch",
      "section": "reveal",
      "number": "reveal",
      "photo": "paper",
      "broll_out": "whoosh"
    },
    "stacks": {
      "reveal": [
        {"type": "swell", "db": -15},
        {"type": "impact", "db": -9},
        {"type": "boom", "db": -10, "pre_lap_ms": -70}
      ],
      "cut": [
        {"type": "whoosh", "db": -17},
        {"type": "bass", "db": -21, "p": 0.3}
      ]
    },
    "cut_coverage": 0.5,
    "title_word_every": 2,
    "min_gap_s": 0.12,
    "reserve_for_reveal": 0.15,
    "max_reveals_per_10s": 1,
    "gain_jitter_db": 3,
    "offset_ms": {"impact": -20, "click": -15, "tick": -5, "glitch": -20, "whoosh_peak": 55, "swell_peak": 0, "riser_peak": 0, "boom": -10},
    "tails": "ring",
    "silence": {
      "before": ["hook_line_2", "after_cold_open", "twist"],
      "len_s": 0.25,
      "max_per_min": 3
    },
    "qc_targets": {
      "strong_transients_per_10s": [6, 18],
      "cut_events_with_hit_250ms": [0.4, 0.65],
      "hit_lag_ms_median": [-40, 10],
      "time_below_-30dbfs": [0.0, 0.04],
      "dropouts_per_min": [0, 4],
      "lufs": -14
    }
  },
  "music": {
    "energy": "mid",
    "db": -20,
    "duck": true,
    "duck_depth_db": 7,
    "insert_duck_db": 12,
    "bed_always": true,
    "bed_fallback": "texture",
    "drop_before_reveal_s": 0.2,
    "drop_floor_db": -30,
    "drop_max_per_min": 4,
    "new_cue_after_reveal": true
  },
  "grade": {
    "contrast": 1.08,
    "saturation": 0.95,
    "brightness": 0.0,
    "gamma": 1.0,
    "warmth": -0.02,
    "lut": null,
    "vignette": true
  },
  "transitions": {
    "default": "cut",
    "burst_flash_frames": 3
  },
  "end_card": {
    "enabled": true,
    "dur_s": 1.5
  },
  "_needs_feature": {
    "sfx.map.cut / cut_burst / section / number / photo / broll_out": "auto_sfx event sources beyond hook/broll/zoom; map.title and map.end exist in _defaults but are never read today",
    "sfx.map values naming a stack + sfx.stacks": "one cue -> several layered sounds, each with own db, probability p and role placement",
    "sfx kinds swell, tick, glitch, boom, paper, texture (+ tape_stop, foley:<noun>)": "new KINDS entries in sfx.py with Openverse queries, durations, align/offset; synth fallbacks in render.SFX_SYNTH",
    "sfx.cut_coverage": "share of item boundaries that get a cut cue (deterministic hash pick)",
    "sfx.title_word_every": "tick on every Nth caption word appear (word-by-word kinetic text)",
    "sfx.min_gap_s / reserve_for_reveal / max_reveals_per_10s": "budget spread over time instead of list truncation",
    "sfx.gain_jitter_db": "per-cue random gain, deterministic by cue time",
    "sfx.offset_ms": "per-preset override of KINDS offset_ms; whoosh_peak/swell_peak are peak-aligned",
    "sfx.stacks.*.pre_lap_ms": "start a layer's body before the cut (ed08 low-end pre-lap)",
    "sfx.tails": "'ring' = never truncate SFX at the next cut (already true in render; keep when pre-mixing)",
    "sfx.silence": "mute bed + SFX (not voice) for len_s at named moments",
    "sfx.qc_targets": "qc.py audio check against these ranges",
    "music.duck_depth_db / insert_duck_db": "replace fixed sidechain ratio 6 with a target depth; deeper duck under inserted clip audio",
    "music.bed_always / bed_fallback": "always lay a bed; synth/library 'texture' when no music given",
    "music.drop_before_reveal_s / drop_floor_db / drop_max_per_min": "bed hole automation before reveal stacks",
    "music.new_cue_after_reveal": "switch to the next music section/cue at a reveal",
    "transitions.default 'cut' + burst_flash_frames": "flash-frame stutter bursts at section changes (only 'flicker' exists today)",
    "render: SFX stem pre-mix": "60-100 cues per reel; mix SFX to one stem before the ffmpeg graph"
  }
}
```

---

## 6. Limits of this study
- The panel has no legible clip names, so the SFX vocabulary is inferred from spectral shape (vertical broadband line = tick/click/impact; noise hump = whoosh/swell; rising tonal lines = riser; low sustained blob = sub boom/drone). Exact sound sources are unknown.
- The transient counts include speech plosives. The cut-alignment numbers are chance-corrected (random cut times, ±80 ms) and are the most trustworthy figures here, along with the ETA band-energy curves.
- The music-presence proxy (stable low-frequency peaks) reads 2-9 % for all refs. Beds seem to be textural or score-like rather than bass-melodic [inferred]. I could not separate music from SFX stems.
- ed04 is a vertical AE tutorial, a different format. It is included for its silence device and its 17k likes (the highest in the set), not as a template for the dense mix.
