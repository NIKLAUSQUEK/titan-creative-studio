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
- `broll[]`: `{path, src_in, dur, anchor:{item, offset}, mode: full|pip|split|greenscreen, flag}`. Anchors follow trims. `split` = B-roll on the top half, the speaker's centre band on the bottom half (ref #8/#9 layout).
- `texts[]`: `{type: hook|title|lower_third, text, anchor, dur}`.
  - Hook text = what the viewer reads in the first second. Don't duplicate a spoken hook that is already captioned.
- `chats[]`: `{anchor, dur, style: dark|light, size, sfx: pop, captions: hide, messages:[{side: me|them, name, text, at, typing, punch}]}`.
  - A texting cutaway: bubbles pop in one by one, a "•••" typing bubble shows for `typing` s before a reply, the stack scrolls, and `punch` shows one line alone and large. Captions are hidden while it's up. A brief beat's `chat` field creates one (ref research/edit-references-2026-10.md #7).
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
| genz-header-skit | raw selfie/travel/skit: persistent top header (emoji context line + 2-4 word CAPS reaction 😭💀), no subtitles, SFX hit per reaction (ref research/edit-references-2026-10.md #1) |
| trend-beat-switch | 'My name is… but they call me…' intro in white rounded boxes, then clips switch ON the beat with one label word each; needs a music file (beat-synced) |
| horror-tension | cold teal grade, crushed blacks, long holds, slow push, flicker on beat changes, drone bed + stings |
| genre presets (drama-conflict, feelgood-emotional, founder-inspire, cautionary-ladder, thriller-suspense, mystery-reveal, action-hype, scifi-tech, kdrama-soft, anime-energy, news-expose, luxury-reveal, asmr-satisfying) | one per genre module in genre-playbooks.md §0; the brief picks the genre and its preset |
| texting-suspense | interview/talking-head spine + full-black iMessage cutaways (`chats[]`) when someone quotes a text; persistent small title, drone bed + hits (ref #7) |
| edu-song | song-led teaching: spoken hook, then the song; bouncy karaoke captions, on-beat cuts, recap chorus; pair with `editor.py song` (edu-songs-mnemonics.md) |
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

## 6b. Smart visuals (who, what, where)
- **Beat visuals:** each brief beat has `visual: {type, query, metaphor, person, entity, real_person}`.
  - `own_broll`: your footage, searched with both the literal query and the metaphor (`"walk | fresh start sunrise"`).
  - `me` / `person`: clips where an enrolled person is recognised.
  - `web_image`: licensed photo of a named thing or place.
  - `text_card` / `none`: no cutaway (hooks and CTAs stay on the face).
- **Faces (local, OpenCV YuNet + SFace):**
  - Enrol: `people enroll klaus <photos> --consent self`. Search: `broll-search "@klaus gym"`.
  - Every candidate carries `people` and `unknown_faces`. QC fails a sell piece with unrecognised faces in B-roll.
- **Scene labels:** `describe` is zero-token CLIP labels ("a man exercising in a gym, lifting weights"). That is the text Claude reads when picking.
- **Web images:** `broll-match --web` (or the `web_image` type) searches Openverse then Wikimedia Commons.
  - Licences: CC0, PD, CC BY and CC BY-SA only. Images are ranked locally with CLIP.
  - CC BY images get an on-screen credit plus `web/ATTRIBUTION.md` for the caption.
  - Never Google Images (no licence data; ToS).
  - Real people only as credited editorial/commentary context, never in ads (QC flags).
- **Assignment:** the strongest beat↔clip pairs are assigned first, each clip is used once, and weak matches reserve nothing.

## 7. Trial-reel expander (`expand`)
- **What it makes:** one base edit → N variants (default 12) in `variants/v<N>/`: reels, carousel-text, carousel-image, single quote card, single poster.
- **Axes:**
  - hook: original, or another footage hook moved first
  - header: intro, persistent, or none (header text from the brief's ranked hooks + optional `brief.headers`, CTA lines excluded)
  - length: full, short (~60%), or micro
  - speed: within `--speeds`, default 1.0-1.4 with pitch kept
  - captions: one of 7 caption packs
  - sequence: one safe swap of adjacent beats
  - framing: punch-in/crop and a small saturation nudge
- **Diversity:** every reel pair differs on ≥3 axes (≥2 when hooks are scarce).
- **Story guard:**
  - Hook first, CTA last.
  - Roles hook/turn/lesson/payoff/cta are never dropped.
  - Beats marked `fixed` never move.
  - A line starting with so/and/but/because/that's why/this/which/then/it never swaps.
  - So: give beats roles in the brief.
- **Real differences, not disguise:**
  - Each variant rotates to other acceptable B-roll picks for the same beats.
  - About 1 in 3 reels opens on a 1.2 s cutaway (a cold open) instead of the face.
  - Every reel has a unique opening: no two share the same first line plus header text.
  - A distinctness check compares the opening frames (structure and colour) and the first 3 s of words, and flags look-alike pairs in VARIANTS.md.
  - The tool does not add noise, pitch shifts or metadata tricks to dodge platform duplicate detection. That breaks platform rules and risks the account; the variety has to be real.
- **Cost:** zero Claude tokens. About 3-5 s per draft reel variant on a CPU.
- **Honest note:**
  - Platforms fingerprint audio and video, so speed or crop tweaks alone don't make a repost "new". The hook, structure and format changes are what make a fresh test.
  - One variant per test slot, own caption, never cross-posting duplicates from several accounts.

## 7b. On-screen text cards (emoji, boxes, labels)
- **Card styles:** `hook_text.renderer: "card"` or any text containing emoji renders as a PNG card (Pillow + colour emoji font). Card styles:
  - `outline`: Gen Z header
  - `box`: white rounded TikTok boxes
  - `label`: one word per montage clip
  - `kicker`: news tag bar plus headline
- **Header copy:** the brief returns `headers[]` written in the preset's style. Use "\n" for a context line (e.g. "🇵🇰\nNAHHH BRO 😭💀"). The expander rotates them across variants.
- **Labels:** beat `label` puts one word on that beat's clip.
- **Beat sync:** `beat_sync` presets snap B-roll, labels and SFX to the music's onsets (detected locally).
- **Precedence:** the brand's `edit-brand` hook placement still wins over the preset (e.g. Physio Spot hook at 61.5%).

## 7d. Learn a style from links (`editor.py study`)
- `editor.py study <3-5 links or files> --name "<style>" [--llm claude-cli]`:
  1. downloads the refs with yt-dlp (study only, git-ignored);
  2. measures cuts, median shot, words/min, first word, speech share and LUFS, and makes 1 fps + hook frame sheets;
  3. writes `research/style-studies/<style>/STYLE_STUDY.md` and the preset `style-<style>`.
- With `--llm claude-cli`, one Claude call (sonnet) looks at the sheets and describes captions, header, layout, graphics, grade, sound and "steal / avoid" lists. Without it: zero tokens, numbers only.
- LOOK at the sheets before using the preset. The brand's edit-brand block and the ledger still win.

## 7c. Songs, raps and jingles (`editor.py song`)
- `editor.py song --list` shows the public-domain tunes and their syllables per line.
- `editor.py song --tune twinkle --lyrics lyrics.txt` (or `--rap --bpm 92`, or `--beat` to add drums under a tune) writes `autoedit/song/`:
  - `LYRICS.md`: a syllable-fit table, with rhyme and flow checks in rap mode;
  - `guide.wav`: a one-bar count-in plus the synthesised melody or beat (original audio);
  - `lyrics.srt` / `lyrics.json`: line and word timings for karaoke captions.
- Zero tokens. Fix every non-ok line, record over the guide, then `assemble --preset edu-song --music mix.wav --music-licence original`.
- The rules (formats, kids-TV levers, copyright) are in edu-songs-mnemonics.md.

## 8. Model routing (token saving)
- `tools/editor/models.json` sets the Claude model per step: brief = sonnet, B-roll pick = haiku, free-text revision = sonnet, self-review = haiku. `--claude-model` overrides all of them.
- Search, face recognition, web-image ranking, cutting, rendering and variants never call Claude.

## 6. Sound and compliance hooks
- **Sound:** `/sound` decides the track. Brand accounts get `audio.music.licence` = `original` or `licensed:<source>`; the renderer refuses unlicensed music for brand accounts. Trending sounds on personal accounts are `in-app`: never baked into the file, and recorded in `PUBLISH.md`.
- **SFX:** density and stim types follow the preset (see `voice-persona-audio.md` stim map).
- **Compliance:** the QC word scan uses the brand's `compliance.forbid_words` plus the health pack list for health/clinic brands. It is a tripwire, not legal review: still run the compliance pack in `/publish`.
- **B-roll consent:** clips flagged by path markers, `broll_flags.json` or Creator Brain sensitivity are never auto-picked.
