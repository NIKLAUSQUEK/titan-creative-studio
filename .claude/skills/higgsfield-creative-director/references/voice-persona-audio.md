# Voice, commentary, reaction faces & audio stims

## RULE: archetypes, never impersonations
Personas are ORIGINAL characters inspired by a register/vibe. Never clone, name-match or imitate a specific real person's voice, never reuse their catchphrases, never imply endorsement (right-of-publicity + platform takedown risk). Voices come from Higgsfield presets (list_voices / seed_audio), ElevenLabs library voices, Klaus/actors recorded then voice_change, or a custom voice created WITH the speaker's consent.

## Commentary / narration personas
| Persona | Delivery spec | Best for |
|---|---|---|
| **Posh Nature-Doc Narrator** | Hushed British RP, ~120 wpm, reverent whisper-to-wonder swells, long pauses before the reveal, treats mundane humans as wildlife ("And here… the male… attempts the bench press… alone.") | Deadpan gym/clinic observational comedy, contrast humour |
| **Bronx Hype Commentator** | Fast NYC cadence ~190 wpm, loud, rhetorical questions, call-and-response, disbelief escalations ("Nah. Nah nah nah. Run that back.") | Fails, reveals, reaction skits |
| **Streamer Live Reactor** | Crescendo screaming, talking to "chat", stands up/leans into lens, fake-out calm then eruption | Reaction videos, clip edits, hype product drops |
| **Laid-back West Coast Smooth** | Slow drawl ~110 wpm, unbothered, warm low pitch, cool understatement | Chill brand ads, "life's good" lifestyle, contrast against chaos |
| **Theatrical Diva Rant** | Fast, emphatic, stretched vowels, dramatic pauses, finger-point energy | Hot takes, myth-busting, "who told you that?!" health myths |
| **Nollywood Melodrama Narrator** | Moralising, operatic emotion, slow-zoom drama, "and that was when…" | Story ads, cautionary tales, "don't wait till it's too late" |
| **Deadpan British** | Flat, dry, minimal inflection, perfectly timed silences | Physio Spot-style deadpan skits |
| **Sports Play-by-Play** | Broadcast pace, rising pitch at action, stats as jokes | Workout fails, PB attempts, gym content |
Each persona spec in a script = voice source + wpm + pitch + pause pattern + register + 2-3 ORIGINAL signature devices.

## Reaction-face library (expression archetypes — prompt fragments)
Hold reactions 0.6-1.2 s; pair with a stim; cut on the eyes.
- **Slow side-eye** — head still, eyes slide to camera/other character, lips pressed. (stim: record scratch / low "hmm")
- **Hand-to-chest gasp** — sharp inhale, hand flat on chest, eyebrows up, mouth open O. (stim: gasp sting)
- **Disbelief head-pull** — chin tucks back, eyes squint, slow headshake. (stim: "nah" bass hit)
- **Awkward silent stare at lens** — dead eyes, mouth neutral, held 2 s while room goes silent (Druski-adjacent archetype — awkwardness is the joke). (stim: room-tone dropout / crickets)
- **Suppressed laugh** — lips pressed, cheeks puff, shoulders shake. (stim: soft snort)
- **Double-take** — glance away, snap back, eyes widen. (stim: whip swish + ding)
- **Melodrama freeze** — wide eyes, slow push-in, frame freezes (Nollywood-style drama). (stim: dramatic sting + reverb tail)
- **Cringe recoil** — whole body leans back, teeth bared, squint. (stim: squeak / glass crack)
Casting rule: reactions are performed by cast from the community the joke is about.

## Community humour rule
Punchlines come from INSIDE a community's shared experience (laughing with, not at). Cast members of that community, have the script sanity-checked by someone from it, no slurs, no accent-as-the-joke, no stereotypes as punchlines. Target communities explicitly in the brief (e.g. Nigerian aunties at weddings, NYC gym bros, Singapore NS boys).

## Audio stims (sound design that keeps short-form addictive)
Stim map — beat type → stim:
| Beat | Stim |
|---|---|
| Hook / first frame | bass drop, whoosh-in, or record stop |
| Reveal / punchline | heavy impact boom, sting |
| Side-eye / judgement | record scratch, low "hmm" |
| Awkward silence | music + ambience cut to dead air or crickets |
| Text/caption pop | pop / click / keyboard |
| Transition | swish, whip, riser-to-cut |
| Suspense | riser, ticking, heartbeat |
| Fail | descending "wah" horn, glass crack |
| Win / glow-up | sparkle, choir "ahh", cash register |
Density: comedy/skit/reaction = one stim every 1.5-3 s; story/ad = at structural beats only; serious/clinic = 0-2 total. Mix: dialogue -14 LUFS target, stims peak ≤ -1 dBTP, duck music 8-10 dB under speech, stims never mask a spoken word.
Sources (in order): `assets/sfx/` curated royalty-free library (CC0/commercial-licensed packs Klaus downloads; log licence per file) → synthesised in edit (whoosh/boom/riser via scripts) → ElevenLabs sound tools (verify availability) . Trending MEME sounds (copyrighted originals) = personal accounts only, added in-app at upload — never baked into brand ads.

## Trending audio button (/sound)
1. Higgsfield `tiktok_music_trending` (needs TikTok account connected in Higgsfield; `tiktok_accounts` → connector_id): Commercial Music Library tracks, filter country (US/SG/GB/NG/MY/ID/TH/VN), genre (HIP_HOP/RAP, POP, EDM, LO-FI, CHILL_BEATS, EPIC…), window 1DAY/7DAY/30DAY → licensed for brand use. Show 3 picks with listen links + why each fits the beat map.
2. Weekly Trend Radar (`library/trends/`): trending sounds/memes/audio formats with licence status + expiry date.
3. Output an **SFX cue sheet** aligned to the script: `timestamp | beat | stim | source file | level`.
Music is attached at TikTok publish time (tiktok_prepare_publish widget) or mixed in the edit for other platforms.

## Gate hooks
- Gate 1 asks: commentary/voice persona (or none) · sound energy (stim-heavy / balanced / clean) · target community for humour.
- Gate 3 script table gains a 4th column: **Audio stim / music cue**.
