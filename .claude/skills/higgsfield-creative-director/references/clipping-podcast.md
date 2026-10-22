# Clipping & podcast highlights (long-form → shorts, episodes → highlights)

Use this for podcasts, interviews, webinars, Klaus's talking-head videos, clinic talks and livestreams. Source tags are explained in `research/sources-editing.md`.
Compliance comes first: apply the brand's compliance pack. Example, in Singapore health content, a clip must not become a testimonial, a superlative claim or an inducement. Re-check the hook line and the caption against the localisation.md SG pack, and never cut a clip so it changes what the speaker meant.

## 1. Pick the route
| Situation | Route |
|---|---|
| Recorded in Riverside, want speed | Riverside Magic Clips + text-based editor (§5) |
| Any file / YouTube link, want control and no subscription | Local pipeline: faster-whisper + Claude + ffmpeg (§6) |
| Want a stylised "aura" edit or teaser recreated from a reference | Higgsfield Katana in Claude (`/katana`), on Higgsfield credits [HF-Clip] [HF-Katana-blog] |
| YouTube video → quick clips inside Higgsfield | Higgsfield "Personal Clipper" (via MCP) [HF-Help] |
| Premiere project already exists | Premiere MCP `apply_cutlist` route (see claude-editing.md) |

## 2. Finding moments: what makes a clip work
From [HF-Clip] (Katana/Claude clipping) plus podcast practice:
1. **It works on its own.** A cold line, a crazy move, a confident reaction, a hilarious story. Someone who has never seen the show should "get it". Leave in **a few seconds of setup** so first-time viewers understand. [HF-Clip]
2. **Time the payoff.** The line finishes and the beat drops on the best shot. [HF-Clip]
3. **One feeling per clip.** Every shot builds the same vibe, so viewers comment "who is this guy?" or "what show is this?". [HF-Clip]
4. **There are two formats.** An *aura/statement edit* says "damn, this person is sharp" and is built around one strong statement. A *teaser* says "wait, what happens next?": it reveals some, withholds the resolution and ends on the open loop. One episode can give several teaser angles. [HF-Clip]
5. **Use a proven reference.** Pick it by views, likes, shares and comment reactions. A bad reference gives a bad result. [HF-Clip]
6. **Score with more than the transcript.** Combine the transcript with audio energy and laughter spikes, scene cuts and face reactions. Small LLMs score everything in a narrow band, so **rerank the finalists head-to-head**. [Clips-Kitty]

Physio Spot moment types: a myth-bust ("stretching won't fix your back because…"), a surprising number with its source, a patient-type story told as a generic scenario (never a named or identifiable patient, never a testimonial), a "do this, not that" demo, or a strong opinion from Klaus.

### Moment-finder prompt (paste into Claude with the transcript JSON)
```
You are a short-form editor for a men's-health physio (Singapore). From this word-timestamped transcript,
find 8-12 candidate clips, 20-60 s each, that stand alone. For each return JSON:
{start, end, hook_line (first 3 s, verbatim from transcript), payoff_time, format: "statement"|"teaser"|"myth-bust"|"demo",
 why_it_works, setup_needed_s, risk_flags: [testimonial|superlative|medical-claim-needs-source|out-of-context]}
Rules: start on a sentence boundary; payoff inside the last 30%; no clip that changes the speaker's meaning;
flag any claim that needs a citation. Then rerank the top 12 head-to-head and return the best 6.
```

## 3. Hooks (first 1-3 s)
- **Open on the strongest line**, not on "so, um". It's fine to pre-roll the payoff line as a cold open and then cut back to the setup (a "flash-forward hook").
- **Hook text on screen** in 1-6 words with a keyword colour that restates the curiosity gap ("Your back pain isn't your back").
- **Multi-hook test:** make 2-3 alternative opening hooks on the same body (Higgsfield `/marketing-hook-variants` "Hook Multiplier" for paid ads). [HF-MCP-page]
- Tie-in: the hook library in `research/` and the anthropic-skills `hook-engineering-agent` skill.

## 4. Format details
- **Reframe 16:9 → 9:16:** a single speaker gets a face-tracked crop. Two people either get **camera-switch** (full 9:16 on whoever is talking, cutting rather than panning) or a **top/bottom split**. Use a blurred pillarbox only when both people talk at once in a wide shot. [OSS-clipping] [Clips-Kitty]
- **Captions:** word-level karaoke or 1-2-word pops, placed in the lower-middle third and clear of platform UI. Keep keyword emphasis for 1-2 words per line. Riverside claims about 99% caption accuracy. [Riverside]
- **B-roll:** cut away on keyword moments (stock, Higgsfield-generated, or Klaus's own clinic footage). Riverside can generate B-roll from a prompt. Code graphics for key points work well: "captions and graphics that make the key point stand out". [HF-Clip] [Riverside]
- **Sound:** cut on the beat, keep music under the talking head only (about -19 dB), and use whooshes and textures on graphics (see claude-editing.md sound rules). [UE-Sound]
- **Loudness:** normalise to about -14 LUFS for social.
- **Localise:** translate and dub for other markets (Riverside does 30+ languages; Higgsfield `dubbing`). Have Claude double-check meaning, not only words. [HF-Clip] [Riverside]
- **Repurpose:** aura and statement edits usually work unchanged across Reels, TikTok and Shorts. [HF-Clip]

## 5. Riverside (riverside.com): what it does for podcasts [Riverside]
- **Recording:** local recording up to 4K video with uncompressed WAV, a **separate track per speaker** (unaffected by internet), and AI audio polish and noise removal.
- **Editing:** a text-based editor (search, cut, copy and paste in the transcript), multi-track editing (remove crosstalk, change layouts), brand presets (logo, colours, intro and outro), and animated caption styles.
- **AI tools:** remove filler words and silences in one click, **fix eye contact**, **correct speech** (edit the transcript and AI re-syncs voice and lips), generate B-roll, auto-layouts by active speaker, and translate and dub into 30+ languages.
- **Magic Clips:** AI picks highlights, with presets for TikTok, Reels and Shorts and anything from vertical to widescreen. You can pick a focus speaker or topic, set length and ratio, apply brand presets, edit customisable captions, export up to 4K and use an "AI Co-Creator" for titles, posts and thumbnails. There is a free plan.
- **Publishing:** built-in podcast hosting (Spotify, Apple, YouTube) with auto titles, descriptions, chapters and takeaways, plus multistream live and webinars.
- **Studio caution:** "correct speech" literally changes what someone said. Never use it on a clinician's medical statement or on any guest without written OK, and never to create an endorsement.

**Recommended Riverside flow for Klaus's podcast:** record (separate tracks) → AI audio polish → remove filler and silences → full episode export (16:9) → Magic Clips with a brand preset at 9:16 → export the clips plus the per-speaker WAVs → run the clips through §2 compliance and QC (`scripts/qc_frames.py`). Optionally re-edit the best 3 locally (§6) for custom captions and graphics.

## 6. Local pipeline: ffmpeg + faster-whisper + Claude (no subscription)
Open-source tools that already do this end to end (read their code before running, and treat downloads as untrusted): `podcli` (Claude/Codex scoring, face tracking, MCP), `Steezy-code/clipper` (faster-whisper + local Qwen3 + OpenCV), `PodClipper` (Whisper + Claude + YOLO/MediaPipe), `opensource-clipping` (faster-whisper + MediaPipe + pyannote split-screen), `Clips Kitty` (multimodal scoring + TalkNet active speaker). [OSS-clipping] [Clips-Kitty]

Minimal DIY version:
```bash
# 0) get media (own content or licensed only)
yt-dlp -f "bv*[height<=1080]+ba/b" -o ep.mp4 "<url>"          # optional
ffmpeg -i ep.mp4 -vn -ac 1 -ar 16000 ep.wav                    # 16 kHz mono for ASR

# 1) word-level transcript
pip install faster-whisper
python3 - <<'PY'
from faster_whisper import WhisperModel
import json
m = WhisperModel("large-v3", device="auto", compute_type="int8")   # use float16 on CUDA
segs, info = m.transcribe("ep.wav", word_timestamps=True, vad_filter=True)
out = [{"start": s.start, "end": s.end, "text": s.text,
        "words": [{"w": w.word, "s": w.start, "e": w.end} for w in s.words]} for s in segs]
json.dump(out, open("ep.words.json", "w"), indent=1)
PY

# 2) Claude picks moments (prompt in §2) -> clips.json

# 3) cut one clip (re-encode for frame accuracy)
ffmpeg -ss 754.20 -to 801.90 -i ep.mp4 -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k clip01.mp4

# 4a) static centre crop to 9:16 (speaker roughly centred)
ffmpeg -i clip01.mp4 -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920" -c:a copy clip01_v.mp4
#     off-centre speaker: replace the x term with a pixel offset you read off the contact sheet, e.g. crop=ih*9/16:ih:820:0

# 4b) blurred pillarbox (two people / wide shot)
ffmpeg -i clip01.mp4 -filter_complex \
 "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:5[bg];\
  [0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" -c:a copy clip01_v.mp4

# 5) tighten dead air: find silences, then let Claude build a keep-list (no padding over ~20 ms on talking heads [Joseph-YT])
ffmpeg -i clip01_v.mp4 -af silencedetect=noise=-35dB:d=0.35 -f null - 2> silences.txt

# 6) captions: Claude writes captions.ass from words.json (karaoke \k tags, 1-3 words per line, safe margins) then burn
ffmpeg -i clip01_v.mp4 -vf "ass=captions.ass" -c:a copy clip01_cap.mp4

# 7) music bed ducked under voice + loudness
ffmpeg -i clip01_cap.mp4 -i bed.mp3 -filter_complex \
 "[1:a]volume=0.25[m];[m][0:a]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=400[duck];\
  [0:a][duck]amix=inputs=2:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k clip01_final.mp4

# 8) QC: contact sheet + LOOK at it
python3 scripts/qc_frames.py clip01_final.mp4
```
For a face-tracked crop rather than a static one, use one of the OSS tools above, or have Claude write a small MediaPipe/YuNet script that samples face centres every 0.2 s, smooths them with a dead-zone so it doesn't jitter, and writes an ffmpeg `sendcmd` or per-segment crop list. Cut on speaker changes instead of panning. [Steezy] [Clips-Kitty]

## 7. Claude-driven clip edit prompt (Katana style, also works for local)
```
Here is the episode (or link), a reference edit I like, and the music. Make a <30-45> s vertical 9:16 edit.
Strong opening (best line in first 2 s), pacing that matches the reference, cuts synced to the music beats,
original speech kept, captions + graphics that make the key point stand out. Report back after each stage
(moment choice -> cut -> graphics -> sound) so I can redirect before you continue.
```
[HF-Clip]. Ask for a batch: "give me 10 clips from this episode with different moments and hooks." [HF-Clip]

## 8. Deliverables per episode
`projects/<p>/clips/clipNN_final.mp4` (9:16), `clips.json` (timecodes, hook, format, risk flags), the caption `.ass` files, a contact sheet per clip, and a `SOURCES.md` entry for any stat that was said on air.
