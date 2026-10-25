# Silent relatable loop (ref A) + premium moving talking head (ref B), 2026-10-25

Klaus sent two reels to turn into reusable formats for the auto-editor (tools/editor) and the studio.
- **A** https://www.instagram.com/reel/Deroo8FscPs/: "I like this relatable humour and the results show for itself, save as a format we can use for our b roll or silent storytelling."
- **B** https://www.instagram.com/reel/DYwset0R5kP/: "This format or style is amazing for editing for professional sleek feel, moving talking head with premium style edits."

**Download status.**
- A downloaded once with yt-dlp (no cookies or workarounds).
- **B is blocked.** Instagram returned `HTTP Error 429: Too Many Requests` twice (the first try, then a retry after 20 s), so it was not downloaded. Nothing in §B is measured from B. §B is written as a spec built from the genre, and every number in it is tagged **[draft]**. §B.6 lists the exact measurement pass to run once the file is available. Klaus can save the reel on his phone and drop the file into `research/refs-2026-10-25/media/B.mp4`.
- Scratch files (frame sheets, crops) are in `/tmp/claude-0/-home-user-titan-creative-studio/68a052f1-4cae-5452-90a6-d9033d4e58c0/scratchpad/agentE/A/`.

---

## A. @waxedbyolesya "The emotional stability of your favorite waxer" (501,374 likes, 3,892 comments, posted 2026-10-19)

### A.1 Measured numbers
| What | Value |
|---|---|
| Duration / format | 14.61 s, 1080x1920, 30 fps, VP9 + AAC 44.1 kHz stereo |
| Scene cuts (`gt(scene,0.2)`, same at 0.08) | 1.833, 3.667, 5.500, 7.300, 9.133, 10.967, 12.800 s → **8 segments of exactly 1.833 s (55 frames)** |
| What the "cuts" are | **The same 1.83 s take, looped 8 times.** I sampled frames at the same offset in each of the 8 loops and compared them at 64x64 grey: the mean difference to loop 1 is 0.4-9/255, which is ≤1 frame of phase jitter. The 2 fps sheet confirms it: every segment shows the identical action. |
| Speech | **None.** faster-whisper small found no segments; its language guess was "jw" at 0.61, which is a nonsense label for music. |
| Loudness | **-14.1 LUFS integrated, LRA 0.4 LU.** A flat, compressed music track with no dynamics and no SFX. |
| Music pulse | Onset autocorrelation gives a 0.50 s period (~120 BPM) **[low confidence]**. The 1.833 s loop is not locked to the bar (it is 3.67 beats at 120 BPM). The cut lands on the loop seam, not on a beat. |
| Text | 8 captions, one per loop, each on screen for the full 1.83 s with a hard swap at the seam. The last 3 frames of a loop sometimes have no caption (sheet frame at 9.0 s). |
| Camera | **One locked phone shot**, wide (~0.5x-1x), chest height, at the end of a corridor looking at a doorway. The subject goes from full body (~40% of frame height) to a close fill as she storms the lens. There is no zoom, no reframe and no grade change. The light is flat, overhead and natural. |

### A.2 The action (one 1.83 s take, 8 fps strip read)
| t in loop | Beat |
|---|---|
| 0.00-0.35 s | She walks fast out of the doorway (full body, frame centre-left). |
| 0.35-0.65 s | She flings her bag at the floor with her right arm. The bag is airborne in frame, the peak "rage" pose. |
| 0.65-1.20 s | She stomps toward camera, body bent and hair flying. |
| 1.20-1.83 s | She fills the frame and exits past the lens to the right. The frame is the empty corridor + the doorway again, so **the loop seam is invisible**: exit past the lens → re-enter at the door. |

### A.3 Caption script (time, exact text)
| # | Window | Caption | Role |
|---|---|---|---|
| 1 | 0.00-1.83 | Client is 10min late | setup (a negative trigger) |
| 2 | 1.83-3.67 | Client is 10min early | **opposite** trigger, same reaction → the joke lands here |
| 3 | 3.67-5.50 | No bookings | new pair: bad |
| 4 | 5.50-7.30 | Fully booked | its opposite: good, same rage |
| 5 | 7.30-9.13 | When your client cancels | bad |
| 6 | 9.13-10.97 | When your client shows up | good, same rage |
| 7 | 10.97-12.80 | When your client | **escalation by subtraction**: the trigger loses its verb |
| 8 | 12.80-14.61 | When | the trigger is gone: she reacts to *existing* |

Post caption: "The emotional stability of your favorite waxer 🤦🏻‍♀️🙄 (jokes aside I really love my job) 🥰💜". The disclaimer pre-empts "rude to clients" comments, and the brand needs it.

**Type style (measured from crops):**
- TikTok/IG native "Classic" text: white, rounded geometric bold sans (closest in our pack: **Poppins SemiBold/Bold**; TikTok Sans is OFL if we add it), thin black stroke (~6 px at 1080 w), no box, no shadow.
- One line, never wrapped. Glyph height ≈ 0.040 of frame height. Line width 41-73% of frame width.
- Centred horizontally, at **y ≈ 0.66** for captions 1-6 and drifting to **≈ 0.74** for 7-8 (hand-placed in-app). We fix it at one height.
- No animation: it appears on the cut and is gone at the next cut.

### A.4 Why it works (comedic structure)
1. **The premise is in the post caption, the proof is on screen.** The title "emotional stability" is ironic, and every loop is the evidence. The viewer is only asked to read 2-5 words per 1.8 s, about 2 words/s, readable on mute.
2. **Opposite pairs.** Late/early, no bookings/fully booked, cancels/shows up. The same reaction to opposite inputs is the joke ("there's no winning"). Pairing means the second caption of each pair gets the laugh, so the laugh comes every 3.7 s.
3. **Escalation by subtraction, not addition.** The captions get *shorter* ("When your client" → "When"), so the trigger shrinks to nothing while the reaction stays maximal. Final read: she rages at existence. That is the punchline, and it cost zero extra footage.
4. **The loop makes it rewatchable.** There is no end card, and the seam is invisible (she exits past the lens, re-enters at the door). The video restarts at "late" and viewers watch 2-3 times. At 14.6 s the completion rate is high.
5. **Relatable to a whole profession.** Every service worker (stylist, physio, barista, photographer) has the late/early and empty/full complaints, and they tag colleagues.
6. **"The results show for itself":** 501 K likes on one 1.8 s take, one location and a phone. Production cost is near zero, and the whole idea lives in the caption list.

**Without sound:** it works 100% on mute. The music is an energy bed (flat -14 LUFS, LRA 0.4) and carries no information. That makes it ideal for B-roll and silent storytelling, and it means brand accounts can use any licensed or original track without losing the joke.

### A.5 Reusable format: "Same reaction, every trigger" (silent loop) + its B-roll sibling
**Variants:**
- **A-loop (exact ref):** one take, looped ×6-8, one caption per loop.
- **A-results:** loop ×4-6, then break the loop with a **0.6-1.2 s result shot** (the thing your job actually produces: the photo, the shake, the shipped screen, a calm treatment room). That shot is the "results show for itself" beat. Brand-safe, because the result is *your own work or process*, never a customer outcome.
- **A-montage (B-roll silent story):** 6-10 *different* 1.2-2.0 s B-roll shots, one caption each, same type style. Use it when there is no single performance but plenty of B-roll. The structure of pairs → subtraction → payoff stays the same.

**Beat template (8 slots, 1.6-2.0 s each, 13-16 s total):**
| Slot | Caption pattern | Purpose |
|---|---|---|
| 1 | Bad trigger A ("Client is 10min late") | setup, establish the reaction |
| 2 | Opposite of A ("…10min early") | first laugh: the reaction doesn't change |
| 3 | Bad trigger B | rhythm |
| 4 | Opposite of B | second laugh |
| 5 | Bad trigger C (longest line, most specific) | max specificity before the collapse |
| 6 | Opposite of C | third laugh |
| 7 | C with the verb removed ("When your client") | escalation by subtraction |
| 8 | One word ("When" / "Monday" / "Hi") | punchline; loops back to slot 1 |
| (A-results) 9 | no caption, or 1-2 words ("anyway") | the result shot, 0.6-1.2 s, then loop |

**Writing rules:**
- Each pair is a real opposite.
- Captions get shorter from slot 5.
- Never explain the joke on screen; the premise goes in the post caption.
- The disclaimer line goes in the post caption ("jokes aside I love my job"), not on screen.

**Text card style (silent-caption):**
- Poppins SemiBold, white #FFFFFF, black stroke ≈ px/9, no box, no shadow, sentence case (no caps), one line.
- Size 0.040; shrink to fit one line (≤ 82% width) rather than wrap.
- Centred at y 0.66, or the brand's hook height if set (Physio Spot = 0.615). It sits in the safe zone above the IG/TikTok UI.
- Hard swap on the cut, no pop or fade.
- Emoji off on screen (they belong in the post caption).

**Phone shot list template (one location, 10 minutes):**
| # | Shot | How | Why |
|---|---|---|---|
| 1 | Hero loop take | Phone locked on a tripod or a shelf, 0.5x or 1x, chest height, at the end of a corridor or room, the door or entrance in frame. The actor starts **out of frame or in the doorway**, does ONE big readable action (throw, slam, spin, drop into a pose), then **exits past the lens or back out of frame**. 1.6-2.0 s. Shoot 8-10 takes and pick the cleanest seam. | An invisible loop seam; full body reads on a small screen |
| 2 | Seam check | Film 2 s of the empty frame before and after. | Lets the editor trim to frame-matched in/out points |
| 3 | Prop throw | The prop must be big and dark against a light wall (her black bag on a cream wall). | Silhouette readability |
| 4 | Result shot (A-results) | 1-2 s of the finished product / your work, same light. | The "results show for itself" beat |
| 5 | Montage set (A-montage) | 8-10 × 2 s handheld B-roll of the job: hands, tools, the queue, the screen, the street. Hold each 3 s and keep the horizon level. | Silent-story sibling |
| — | Settings | 1080x1920, 30 fps, AE/AF lock on the doorway, no zoom during the take, natural light. Wardrobe contrasts with the wall. | Matches the ref |

### A.6 Five concepts for Klaus's brands
Every concept runs through the brand's compliance pack before scripting. Skits are clearly dramatised, the cast is staff or Klaus, and no patient or customer appears.

1. **Physio Spot (SG men's pelvic health; SG health rules).**
   - *"Nothing you say will shock your physio."* This inverts the ref: the reaction is the same **calm, warm nod while sipping tea** (the physio in the treatment room doorway, locked shot).
   - Captions: "He thinks it's 'just stress'" / "He googled it at 2am" / "He's too embarrassed to ask" / "He finally asks" / "He asks AND does his exercises" / "When he says 'is this normal'" / "When he says" / "When".
   - A-results shot = the private, calm treatment room (process), no outcome.
   - Post caption: "Zero judgement. It's literally our job." No testimonials, no "fixed", no superlatives, no free-consult offer. The CTA is "Book a private assessment" (no inducement).
   - Gag carrier: the physio's unbothered face and teacup. Hidden until the reveal: nothing; the joke is the sameness.
2. **Power Protein (protein café, Thao Dien, HCMC).**
   - *"The barista's emotional stability."* Same action every loop: the barista spins, slams a shake on the counter and slides it to camera.
   - Captions: "Customer is bulking" / "Customer is cutting" / "Customer skipped leg day" / "Customer hit a PR" / "Customer just walked past" / "When you walk past" / "When".
   - A-results: 1 s macro of the shake pour plus the menu name.
   - Localise with an EN/VI caption pair (VI under EN at 0.5 size) per localisation.md.
3. **PeachForm (women's glute/lower-body strength, brand [draft]).**
   - *"Her answer to everything."* Same action: she drops into a hip thrust with a glute band, one explosive rep, exits.
   - Captions: "Bad day" / "Good day" / "He didn't text back" / "He texted back" / "Ate 3 croissants" / "Didn't eat the croissants" / "Monday" / "When".
   - A-results: the creator's **own** training log or form check. No customer before/after and no body-transformation claims until the brand file confirms the market rules.
4. **TITAN.AI (AI agency).**
   - *"Agency founder's emotional range."* Same action: Klaus cracks his knuckles, slams the laptop open, hits Enter and walks off.
   - Captions: "Client wants a website" / "Client wants an app" / "Client wants it in 2 weeks" / "Client wants it yesterday" / "Server is down" / "Server is up" / "When the client" / "When".
   - A-results: a 1 s screen recording of a real shipped TITAN.AI page (own work, credits on).
5. **Snap Saigon (local photo snappers, HCMC).**
   - *"Your snapper, unbothered."* Same action: the snapper drops into the low hero-angle crouch, fires a burst and pops up. Locked shot on a District 1 street or alley.
   - Captions: "It's 38°C" / "It's raining" / "Couple wants candid" / "Couple wants posed" / "Tourist brought 4 outfits" / "Tourist brought a dog" / "When they say" / "When".
   - **A-results is mandatory here:** after loops 2, 4 and 6, flash the actual photo from that situation for 0.5 s (own portfolio, client release on file). The punchline is the final photo, held 1.2 s.
   - Brand line in the post caption: "your local snapper in saigon".

### A.7 What our editor can do today vs what to add
**Already possible with a hand-written recipe.**
- Items can repeat the same clip with the same `in`/`out`.
- A source with no words is kept whole (`spans_for` returns `[(t0, t1)]` when there are no words).
- `texts[]` with `type: "title", style: "outline", uppercase: false, position_y, size, dur` render as Pillow cards (textcard.py).
- Captions off, music via `audio.music`, `end_card.enabled: false`.

Example (one loop shown):
```json
{"items": [{"id": "c01", "clip": "loop", "in": 0.20, "out": 2.03, "speed": 1.0, "zoom": [], "focus_x": 0.5}, {"id": "c02", "clip": "loop", "in": 0.20, "out": 2.03, "speed": 1.0, "zoom": [], "focus_x": 0.5}],
 "texts": [{"type": "title", "style": "outline", "uppercase": false, "position_y": 0.66, "size": 0.040, "text": "Client is 10min late", "anchor": {"item": "c01", "offset": 0.0}, "dur": 1.83},
           {"type": "title", "style": "outline", "uppercase": false, "position_y": 0.66, "size": 0.040, "text": "Client is 10min early", "anchor": {"item": "c02", "offset": 0.0}, "dur": 1.83}]}
```

**Missing (specs):**
1. **`structure.loop`: an auto loop builder.**
   - `{"clip": "<id>", "repeats": 8, "captions": [...], "result_clip": "<id>", "result_after": [2, 4, 6], "result_dur_s": 0.6}`.
   - The brief or recipe step emits one item per repeat and one `title` text per item.
   - **Seam finder:** search the clip for the in/out pair (each within ±0.5 s of the requested ends) that minimises the frame difference between `out-1f` and `in`. Use 64x64 grey MAD, the same metric used to measure this ref. Report the seam score in QC (target < 3/255).
2. **`text_fit: "one_line"`** in `card()`: shrink the font until the line fits `max_w` (0.82 W) instead of `wrap_lines`. The ref never wraps.
3. **Label style override:** `labels.style` (e.g. `"outline"`). Beat `label` is currently hard-wired to `style: "label"` (recipe.py ~235). The montage variant wants per-beat captions in the outline style.
4. **Captions writer:** `brief.py` prompt mode `silent_pairs`. It returns 8 captions following the A.5 rules (opposite pairs → subtraction → one word) plus a post caption with the disclaimer, then runs the compliance word scan.
5. **QC:** a mute-readability check: each caption needs ≥ 0.35 s per word on screen (the ref: 1.83 s for ≤ 5 words).

### A.8 Preset: `silent-loop-reaction`
```json
{
  "name": "silent-loop-reaction",
  "label": "Silent loop: same reaction to every trigger (caption swaps per loop)",
  "kind": "style",
  "description": "From ref A (@waxedbyolesya, measured 2026-10-25): one 1.83 s locked phone take looped x8, one sentence-case outline caption per loop (opposite pairs, then escalation by subtraction to one word), no speech, flat music bed, no zooms, no SFX, no end card, invisible loop seam. Variants: results (break the loop with your own work), montage (different B-roll per caption).",
  "reference": "research/refs-2026-10-25/silent-and-premium.md#a",
  "structure": {
    "name": "silent-loop",
    "target_s": [12, 16],
    "beats": ["trigger A", "opposite A", "trigger B", "opposite B", "trigger C", "opposite C", "C minus verb", "one word -> loop"],
    "loop": {"repeats": 8, "loop_s": [1.6, 2.0], "seam": "auto", "_needs_feature": "structure.loop auto builder + seam finder (A.7 #1)"},
    "variants": {"results": {"result_after": [2, 4, 6], "result_dur_s": 0.6, "_needs_feature": "structure.loop.result_clip"}, "montage": {"broll_per_caption": true}}
  },
  "pacing": {"remove_silence_over_s": 99, "pad_s": 0.0, "remove_fillers": "none", "max_shot_s": 2.2, "drop_retakes": false},
  "captions": {"enabled": false, "font": "Poppins"},
  "hook_text": {
    "enabled": false,
    "renderer": "card",
    "card_style": "outline",
    "font": "Poppins",
    "size": 0.040,
    "color": "#FFFFFF",
    "uppercase": false,
    "position_y": 0.66,
    "max_words": 6
  },
  "loop_captions": {
    "style": "outline", "font": "Poppins", "size": 0.040, "position_y": 0.66, "uppercase": false,
    "fit": "one_line", "max_w": 0.82, "swap": "hard_on_cut", "min_s_per_word": 0.35,
    "_needs_feature": "per-loop caption list + text_fit one_line + labels.style outline (A.7 #1-3)"
  },
  "zoom": {"mode": "snap", "every_s": 0, "scale": 1.0, "on_hook": 1.0, "on_emphasis": false},
  "broll": {"every_s": 0, "mode": "full"},
  "transitions": {"default": "none"},
  "sfx": {"density_per_10s": 0.0},
  "music": {"energy": "high", "db": -14, "duck": false},
  "grade": {"contrast": 1.0, "saturation": 1.0, "warmth": 0.0, "vignette": false},
  "end_card": {"enabled": false},
  "safe_zone": {"top": 0.12, "bottom": 0.22, "right": 0.15}
}
```
Brand use: the brand's `edit-brand` caption height wins (Physio Spot 0.615). Brand accounts use licensed or original music only (`/sound`); a trending track goes on personal accounts, in-app.

---

## B. Premium moving talking head (ref B: NOT DOWNLOADED, HTTP 429 twice)

Everything below is a **[draft]** spec of the "premium moving talking head" look Klaus describes ("professional sleek feel, moving talking head with premium style edits"). It is built from the genre, not from this reel. Replace every [draft] number with the measured one via §B.6 before building the preset into tools/editor/presets/.

### B.1 What the look is made of [draft, to confirm against B]
- **Camera movement.**
  - The talking head is never static. There is a slow continuous drift on every shot: a 2-4% scale push plus 1-3% lateral slide over the shot, eased in and out.
  - Two sources are likely: (a) a real gimbal slow orbit or slider (parallax visible: the background moves more than the face) or (b) a digital "virtual camera" on locked 4K footage (no parallax: everything moves together).
  - **How to tell on B:** track two points, one on the face and one on the background. Equal motion means digital; different motion means real parallax.
- **Framing per sentence.**
  - It alternates wide/medium → tight close-up at sentence or idea boundaries (scale ~1.0 ↔ 1.25-1.35). The subject sits off-centre on the thirds line, and the side swaps with the framing.
  - Changes land on sentence starts, not on a fixed timer.
- **Layering.**
  - B-roll as full-frame cutaways of 1.5-3 s, each with its own slow push.
  - Floating rounded-corner cards (product screens, stats) with a soft drop shadow over a blurred talking head.
  - Minimal kinetic type (one keyword per idea) that sometimes sits behind the subject.
- **Captions and type.**
  - Small, clean sentence-case subtitles (or none), low in frame.
  - Keyword titles in an editorial serif or a clean grotesk (our pack: Instrument Serif / Space Grotesk).
  - Soft fade or blur-in, never pop.
- **Grade.**
  - Soft contrast, lifted blacks, warm skin, slightly desaturated background, gentle vignette, fine grain.
  - A shallow depth-of-field look (real or faked background blur).
- **Transitions.**
  - Mostly straight cuts made invisible by the moving camera, plus soft-flash / light-leak hits or blur dissolves at section changes (every 8-15 s).
  - A zoom-blur whip into B-roll.
- **Sound design.** A clean, de-essed voice at -14 LUFS, a soft piano/ambient bed at -22 to -26 dB with ducking, a subtle whoosh on each framing change, and one swell into the CTA. Low SFX density (≤ 1 per 10 s).
- **Pace [draft targets].** A shot or framing change every 2.5-4 s; B-roll ~25-35% of runtime; 150-175 wpm; silence trimmed at 0.4-0.5 s (premium-calm range), not punchy 0.3 s.

### B.2 What tools/editor already does (editor.md §2, §7f, and the code)
| Need | Status today |
|---|---|
| Push-in per shot | `zoom.mode: "smooth"`: one **linear** scale ramp per item, centred x, y anchored 0.4 (`recipe.place_zooms`, `render.zoom_chain`). No ease, no pan, no rotation. |
| Alternating punch-in | `zoom.mode: "snap"` already alternates 1.0 / `scale` on every cut and every `every_s` (time-based, not sentence-based). Crop is centred; `focus_x` is static per item. |
| B-roll Ken Burns | Only for still images (`zoompan` 1→1.06 in `render_broll`). Video B-roll has no move. |
| B-roll layering | `broll.mode` full / pip / split / side / greenscreen; code-motion cards (`kind: motion`: step-cards, stat-counter, kinetic-quote). |
| Captions | `two_level` glow captions, fonts pack (Instrument Serif, Space Grotesk), `animation: fade`. |
| Transitions | `transitions.default` flash / dip / glow = a brightness pulse only (no overlay texture, no blur). |
| Grade | contrast / saturation / gamma / warmth / LUT / vignette. No grain, halation or background blur. |
| Sound | whoosh peak +60 ms, SFX stacks, cut_coverage, ducking, swell, loudness -14. |

### B.3 Missing features, specced to build
Each feature works on locked footage first; it must also be safe on already-moving gimbal footage, where `strength` scales down.

1. **Virtual camera drift (`camera.drift`).** A per-item eased move on overscanned footage.
   - Keys: `{"scale": [1.04, 1.08], "pan_x": [-0.02, 0.02], "pan_y": [-0.01, 0.01], "rotate_deg": [-0.4, 0.4], "ease": "inOutSine", "alternate": true, "overscan": 1.12}`.
   - Per item, pick a start and end pose from the ranges. `alternate` flips pan direction every item so consecutive shots don't all drift the same way.
   - ffmpeg: `scale=W*o:H*o` → `rotate='r(t)':ow=W*o:oh=H*o:fillcolor=none` → `crop=W:H:x='cx(t)':y='cy(t)'`. Here `p(t)=0.5-0.5*cos(PI*t/d)` (inOutSine), `cx = (in_w-W)/2 + pan_x(p)*W`, and scale is applied by a crop-size expression or a `zoompan` with `d=1` at fps.
   - Clamp pan so the crop never leaves the overscan. Add `focus_from_face: true` to bias the start pose so the face (faces.py) stays on a thirds line.
2. **Handheld micro-shake (`camera.handheld`).**
   - `{"amp_px": 3, "rot_deg": 0.15, "freqs": [0.31, 0.53, 0.97]}`: a sum of incommensurate sines, seeded per item, added to drift `cx`/`cy`/rotate.
   - This gives organic "operator" life without real shake. Default off for premium; on for UGC.
3. **Sentence-aligned framing plan (`framing.plan: "per_sentence"`).**
   - From ingest words, split on sentence ends (`.?!` or gaps > 0.45 s). Assign alternating framings from `framing.cycle: ["wide", "close", "medium_left", "close", "medium_right"]` with scales `{"wide": 1.0, "medium": 1.15, "close": 1.32}` and `x_bias` (left/right thirds: -0.06/+0.06 of W).
   - Emit them as item zoom keys at sentence starts (snap) with drift continuing inside.
   - Guard: never change framing inside a word, and allow at most one change per `framing.min_hold_s` (2.0).
   - Replaces the time-based `every_s` for this preset.
4. **Eased zoom keys.** `zoom[].ease` accepts `linear | inOutSine | inOutCubic | outExpo` in `zoom_chain` (it is currently linear only). Plus **motion-blurred punch** (`zoom.punch_blur`): a 3-frame `tmix=frames=3` around a snap to soften it the premium way.
5. **Light-leak / soft-flash transition (`transitions.default: "leak"`).**
   - `{"dur_s": 0.45, "strength": 0.8, "palette": "warm|cool|brand", "on": "sections|beats|cuts"}`.
   - Implementation A: a library `assets/overlays/leaks/*.mp4` (licensed or CC0 film-burn clips, credits kept) blended with `blend=all_mode=screen` over the window, alpha = a fade-in 40% / fade-out 60% envelope.
   - Implementation B (no assets): a procedural moving radial gradient via `geq` or a Pillow-rendered 1/4-res frame sequence (orange→pink blob translating across, gaussian-blurred 80 px), upscaled and screen-blended.
   - The existing `flash` pulse can sit under it at 0.3 strength.
6. **Blur dissolve and zoom-blur whip (`transitions.default: "blur_dissolve" | "zoom_whip"`).**
   - `blur_dissolve`: `xfade=transition=fade:duration=0.3` with `gblur=sigma` ramped 0→18→0 across the overlap.
   - `zoom_whip`: the last 4 frames of A scale to 1.25 with radial blur (`zoomblur` approximation: average 5 progressively scaled copies) into the first 4 frames of B scaling from 1.25 to 1.0, plus a whoosh at +60 ms. Needs `xfade` in the item concat (today items are hard-cut concatenated).
7. **Depth blur / fake bokeh (`grade.depth_blur`).**
   - `{"sigma": 10, "feather_px": 12, "engine": "mediapipe_selfie|rembg"}`.
   - Per-frame person mask (cache it as a grey mask video next to the ingest clip, the same caching as faces.py). Then `[src]gblur=sigma=S[bg];[src][bg][mask]maskedmerge`, with the mask inverted so the background is blurred.
   - Skip it on B-roll unless the flag is set. QC: edge halo check on hair (mask feather).
8. **2.5D parallax (`camera.parallax`).** It reuses the depth-blur mask. Drift moves the background layer at 1.0x and the subject layer at `subject_ratio: 0.6`, with the background inpainted by edge-extend plus blur (keep moves ≤ 2% so holes stay hidden). This fakes a slider move on locked footage.
9. **Video B-roll push.** Apply `camera.drift` to video B-roll too, so every cutaway moves (today only still images get Ken Burns).
10. **Floating card layer (`broll.mode: "card"`).** `{"radius": 0.04, "shadow": 0.35, "scale": 0.78, "bg": "blur_speaker"}`: rounded B-roll window with a drop shadow over a blurred, dimmed talking head, sliding in 8% with outCubic over 0.35 s.
11. **Grain + halation grade.** `grade.grain: 0.04` (`noise=alls=..:allf=t`) and `grade.halation: {"threshold": 0.85, "sigma": 14, "tint": "#FF7A3D", "mix": 0.12}` (split highlights → blur → tint → screen).

Build order by value/effort: 1 + 3 + 4 (the core "moving premium" feel, pure ffmpeg) → 5 → 6 → 9 → 7 → 11 → 10 → 8.

### B.4 Preset: `premium-moving-talking-head` [draft until B is measured]
```json
{
  "name": "premium-moving-talking-head",
  "label": "Premium moving talking head (virtual camera drift, per-sentence framing, soft leaks)",
  "kind": "style",
  "description": "DRAFT from Klaus's ref B (Instagram DYwset0R5kP, not yet downloadable: HTTP 429). Locked or gimbal talking head that never sits still: eased 4-8% drift per shot, wide/close alternation on sentence starts with thirds offset, moving B-roll cutaways and floating cards, serif keyword titles + small sentence subs, soft warm grade with depth blur and grain, light-leak at section changes, sparse whooshes, ambient bed ducked.",
  "reference": "research/refs-2026-10-25/silent-and-premium.md#b",
  "structure": {"name": "short", "target_s": [25, 50], "beats": ["hook claim 0-3s (close)", "context (wide)", "point 1-3 (alternate framing, B-roll per point)", "turn/insight (close + leak)", "CTA (wide, swell)"]},
  "pacing": {"remove_silence_over_s": 0.45, "pad_s": 0.12, "remove_fillers": "hard", "max_shot_s": 4.0, "drop_retakes": true},
  "captions": {
    "enabled": true, "font": "Space Grotesk", "bold": false, "size": 0.030, "color": "#FFFFFF", "highlight": "#F3E6D3",
    "outline": 0, "shadow": 2, "position_y": 0.78, "max_words": 6, "animation": "fade", "uppercase": false, "keyword_caps": false, "emoji": false
  },
  "hook_text": {"enabled": true, "font": "Instrument Serif", "bold": false, "size": 0.05, "uppercase": false, "position_y": 0.22, "dur_s": 2.4},
  "zoom": {"mode": "smooth", "every_s": 3.0, "scale": 1.06, "on_hook": 1.12, "on_emphasis": true},
  "camera": {
    "drift": {"scale": [1.04, 1.08], "pan_x": [-0.02, 0.02], "pan_y": [-0.01, 0.01], "rotate_deg": [-0.4, 0.4], "ease": "inOutSine", "alternate": true, "overscan": 1.12, "focus_from_face": true},
    "handheld": {"enabled": false, "amp_px": 3, "rot_deg": 0.15},
    "parallax": {"enabled": false, "subject_ratio": 0.6},
    "_needs_feature": "camera.drift / handheld / parallax (B.3 #1, #2, #8)"
  },
  "framing": {
    "plan": "per_sentence", "cycle": ["close", "wide", "medium_left", "close", "medium_right"],
    "scales": {"wide": 1.0, "medium": 1.15, "close": 1.32}, "x_bias": 0.06, "min_hold_s": 2.0,
    "_needs_feature": "sentence-aligned framing plan (B.3 #3); until built, zoom.mode smooth + every_s 3 approximates it"
  },
  "broll": {"every_s": 6.0, "max_dur_s": 3.0, "min_dur_s": 1.5, "mode": "full", "video_drift": true, "card": {"radius": 0.04, "shadow": 0.35, "scale": 0.78, "bg": "blur_speaker"}, "_needs_feature": "broll video_drift + mode card (B.3 #9, #10)"},
  "transitions": {"default": "glow", "on": "beats", "dur_s": 0.18, "strength": 0.5, "section": {"kind": "leak", "dur_s": 0.45, "palette": "warm", "_needs_feature": "leak / blur_dissolve / zoom_whip (B.3 #5, #6)"}},
  "sfx": {"density_per_10s": 0.8, "db": -20, "cut_coverage": 0.25, "min_gap_s": 2.5, "map": {"hook": "swell", "zoom": "whoosh", "broll": "whoosh", "title": "tick", "end": "swell"}},
  "music": {"energy": "low", "db": -24, "duck": true},
  "grade": {
    "contrast": 0.98, "saturation": 0.94, "brightness": 0.01, "gamma": 1.02, "warmth": 0.04, "lut": null, "vignette": true,
    "grain": 0.04, "halation": {"threshold": 0.85, "sigma": 14, "tint": "#FF7A3D", "mix": 0.12},
    "depth_blur": {"enabled": true, "sigma": 10, "feather_px": 12, "engine": "mediapipe_selfie"},
    "_needs_feature": "grade.grain / halation / depth_blur (B.3 #7, #11)"
  },
  "end_card": {"enabled": true, "dur_s": 2.0},
  "safe_zone": {"top": 0.14, "bottom": 0.2, "right": 0.15}
}
```
The engine ignores the `_needs_feature` blocks, so today the preset renders as a premium-calm-like edit: smooth pushes every 3 s, glow pulses, fade captions, warm grade. It is usable now and upgrades automatically as each feature lands.

### B.5 Shooting notes so the edit can look premium [draft]
- Film in 4K (or the highest the phone allows) **locked on a tripod**, subject on a thirds line, 1.5-2 m in front of a lit background with depth (practical lamp, shelves). Overscan gives the virtual camera 12% to move without losing resolution in a 1080p deliverable.
- Soft key light at 45°, with a background 1-1.5 stops darker than the face.
- Lapel mic. Record 10 s of room tone.
- Shoot B-roll as slow handheld or gimbal moves (3-5 s each), so cutaways match the moving A-cam.

### B.6 Measurement pass to run when B is available
For `B.mp4`, use the same commands as A:
- scene cuts → shot lengths (mean / median);
- whisper words → wpm, sentence starts vs cut and framing-change times (does framing change on sentence starts?);
- ebur128 → LUFS / LRA of voice vs bed;
- 1 fps 8x8 sheet + first 3 s at 4 fps;
- **camera move type:** extract every 5th frame of one A-cam shot, track a face point and a background point (OpenCV `calcOpticalFlowPyrLK`), and compare their displacement (equal = digital drift, different = real parallax). Measure scale change per second (drift %) and pan px/s;
- crops of captions/titles for font size, position_y, animation;
- transition frames (± 3 frames around each cut) to classify leak / flash / blur / whip.

Then fill the numbers into B.1, change B.4 from [draft] to [measured], copy it into `tools/editor/presets/`, and add the archetype row below.

---

## Archetype and comedy-format cards (layout of style-archetypes.md)

**Comedy format library (§B) new row:**
| # | Format | Structure | Gag carrier | Best preset / tool |
|---|---|---|---|---|
| C17 | Same reaction, every trigger (silent loop) | one 1.6-2 s locked take looped ×8; captions in opposite pairs, then shrink to one word; invisible seam; optional "results" shot of your own work | the actor's one big action + prop (the thrown bag) | silent-loop-reaction [measured: refA] |

**Archetype rows:**
| # | Archetype | Feels like | Hook pattern | Edit grammar | Captions + type | Sound | Preset |
|---|---|---|---|---|---|---|---|
| 25 | Service-worker relatable (silent) | "literally me at work" | the first trigger caption over the peak action | ONE locked phone take looped ×8 (1.83 s), hard caption swap per loop, no zoom/SFX; or a B-roll montage, one caption per shot | sentence-case white Poppins outline, one line, y 0.66, no animation | any licensed/original bed, -14 LUFS, works on mute | silent-loop-reaction [measured: refA] |
| 26 | Premium moving talking head | sleek, expensive, calm authority | the boldest claim in a close-up | eased virtual-camera drift on every shot, wide/close per sentence on thirds, moving B-roll + floating cards, light-leak at sections | small sentence subs (Space Grotesk) + serif keyword titles (Instrument Serif), fade | ducked ambient bed, sparse whooshes, swell to CTA | premium-moving-talking-head [draft: refB blocked, 429] |
