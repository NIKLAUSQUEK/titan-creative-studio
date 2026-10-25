# Genre feedback: overnight run 2026-10-25/26 (2-5 am SGT)

Every module below was re-grounded on real reels measured locally: scene cuts, shot lengths, loudness, words/min and frame sheets I looked at. Sources, numbers and full cards are in `research/genre-research-2026-10/*.md`. The corrected cards are merged into `genre-playbooks.md`, and the presets in `tools/editor/presets/` are render-tested on the self-test footage.
**Measurement limits:**
- Only public Instagram reels download from the cloud machine. YouTube, TikTok and Vimeo demand a login, and I did not bypass that.
- Brand films were measured from reposts, so their loudness is Instagram's normalisation.
- The likes counts are the evidence of performance; views are mostly not public.

Tick one box per row: approve, fix (write what), or reject (the old card comes back from git).

| § | Module | What changed | Strongest example | 3 core rules | Verdict |
|---|---|---|---|---|---|
| 2 | Comedy skit / deadpan (+2a silent rebuttal, 2b quote vs reality) | Top deadpan reels cut **2-5× slower** than the old card: a premise, then ONE 10-28 s take. Crash zoom removed. | [@khaby00 9.7M likes](https://www.instagram.com/reel/DceEuVnii0u/) | One take for the answer · protect a 0.5-1.7 s pause before the punch · the header tells the joke, the performer never explains it | ☐ approve ☐ fix ☐ reject |
| 5 | POV / relatable | Not 1-2 s cuts: a persistent "POV: the friend who…" header + 3 vignettes of 5-12 s each, ~220 wpm, no music | [@amitmizrachix 406K](https://www.instagram.com/reel/Dd9hI51P_aw/) | Header names a TYPE · 3 vignettes, 3 locations, to the lens · dialogue is the speed, pause before the punch | ☐ ☐ ☐ |
| 6 | Absurd / meme (+6a brand meme reply, 6b lore roll-call) | The chaos is in the image and the labels, not the cuts (1.5-5 s holds). New default `meme-chaos-short` | [Duolingo 253K](https://www.instagram.com/reel/DFttLM7ATju/) | One bizarre centred subject per shot · label every beat · the brand mocks itself, 5-16 s | ☐ ☐ ☐ |
| 24 | Luxury / product reveal | Show the product in the first 1.6 s (not ~12 s); ~0.85 s cuts for fragrance and fashion, ≥2.5 s for objects; packshot hold 2-4 s. Split into luxury-reveal / luxury-object-calm / fooh-oneshot | [Jacquemus CGI bags](https://www.instagram.com/reel/CqqN8w6K3rL/) | Brand at 1.6 s, packshot end · speed by category · spectacle (labelled CGI) beats montage | ☐ ☐ ☐ |
| 28 | Event / retail / mall | Frame 1 is the storefront or product, never a discount; hands-on activation ~1 s each; ends on a bag-out or a date card | [POP MART Mall of America](https://www.instagram.com/reel/DQxooZQEaIl/) | No discount opener · hands at ~1 s · proof of visit or a what-where-when card ≥2 s | ☐ ☐ ☐ |
| 26 | Before / after | Not a beat snap: the "before" at 0 s, the process for most of the runtime, a wipe/split reveal in the last 3-5 s from the same camera. **SG healthcare: no people before/after at all (HCSA reg 5(1)(d))** | [pink rug 18.8K](https://www.instagram.com/reel/DR4YtfODqnh/) | Same camera and light · the process is the content · objects and spaces, never health results in SG | ☐ ☐ ☐ |
| 27 | ASMR / satisfying | One locked continuous take + a 2.2 s hold; the sound IS the product (dense, loud). A near-silent brand reel flopped | [44.7K](https://www.instagram.com/reel/DaQQ9EuuNu4/) | Loud dense foley · one take by default · frame 1 already makes the sound | ☐ ☐ ☐ |
| 15 | Action / sport | Two modes: an **anthem** (accelerating 3.75 → 2.3 → 1.0 s, cut on VO lines, `sport-anthem`) vs **gym hype** (0.44-0.62 s on the beat, `action-hype`); the money rep plays uncut 3-12 s | [Nike "Winning Isn't for Everyone"](https://www.instagram.com/reel/C9po_ojpF6t/) | Pick the mode · the proof plays uncut · loudness and cut rate build together | ☐ ☐ ☐ |
| 9 | Feel-good (+9c festive film, in the research file) | Medians 1.8-2.9 s (not 3-5 s), one 9-11 s reveal hold, music drops ~15 dB before the payoff; 90-180 s film map + cutdown | [Thai Life "Unsung Hero"](https://www.instagram.com/reel/DWXnBo1DMbN/) | Brisk story + one long hold · take the music away before the payoff · show first, say last | ☐ ☐ ☐ |
| 11 | Founder | High-engagement founder reels are talk-led (4-10 s shots, 150-235 wpm, words from frame 0, ~7 s header, ONE specific scene). New `founder-clip`; the cinematic `founder-inspire` is kept, unmeasured | [Sara Blakely](https://www.instagram.com/reel/DC47FDWxlpv/) | One scene, not the journey · words from frame 0 + stakes header · real voice, real room | ☐ ☐ ☐ |
| 7 | Drama / conflict (+7a micro-drama episode) | Much faster than the old 2-4 s: a 1.2-1.5 s median, dialogue at 0.0 s, ~1 s of silence after the hit. Micro-drama: one scene and one turn per episode, freeze-frame cliffhanger | [Dhar Mann 238K](https://www.instagram.com/reel/Da9ltsbPQAf/) | Conflict line at frame 1 · fast into the cruelty, then true silence · the turn is evidence (chat/CCTV), not a speech | ☐ ☐ ☐ |
| 14 | Mystery / reveal | **Fixed a copy-paste bug** (the card had edu-song's sound/compliance/preset). One closeable question, a clue per insert, silence before the reveal, a clue rewind. Evidence weak (3-352 likes) | [narrated mystery](https://www.instagram.com/reel/DbYOd-HD7E3/) | One specific question · every clue its own insert + sound · silence, then a rewind | ☐ ☐ ☐ |
| 13 | Thriller / heist | A plan the viewer can follow (rule or step cards), inserts at 0.6-1.0 s with a tick each, silence on the hitch. A slow "cinematic AI heist" got 3 likes | [heist short 3.4K](https://www.instagram.com/reel/Csyv74MAu-e/) | A plan, not vibes · fast inserts with ticks · the hitch gets silence | ☐ ☐ ☐ |
| 10 | Romance (+10a slow-burn texting) | Romance that performs is serial and music-led (~2 s median, ≤60 wpm, cold open on the charged moment, then "a few months earlier"). Implied-only line kept: adults 25+, clothed, cut before the kiss in paid ads | [C-drama serial](https://www.instagram.com/reel/DewJSY9AquY/) | Cold open, then a time jump · structure from C-drama, explicitness from our ledger · chats as plot beats | ☐ ☐ ☐ |
| 22 | News / scam-expose (+22b trick-on-the-viewer remix, 22c news-card carousel) | Voice or kicker at frame 0; official advisories (7.6-9.8 s to the first word) were the weakest. A one-take parody that plays the scam on the viewer got ~400-1,600× the likes of the police advisories | [Hougang NPC "Singa(pore) Inferno" 370K](https://www.instagram.com/reel/DWkv0WID7gG/) | Voice at frame 0 · one trick per post, performed on the viewer · one stat with source + date | ☐ ☐ ☐ |
| 20 | Documentary | Medians 1.2-3.2 s inside 6-10 s VO beats at 170-216 wpm (not 3-6 s shots); the investigator on screen in the cold open; a source tag on every evidence shot. New `doc-paper-trail` | [Johnny Harris paper trail](https://www.instagram.com/reel/DRfLDUfk4qJ/) | See research file §D | ☐ ☐ ☐ |
| 21 | Explainer / myth-buster | The myth as its own artefact → "look closely" → labelled evidence + expert PiP → where it started → one-line verdict. 230-240 wpm; dead air loses, not shot length. New default `myth-buster-stitch` | [Dr Karan Rajan 75K](https://www.instagram.com/reel/CxkzKPFs6Dx/) | See research file §D | ☐ ☐ ☐ |

## Decisions only you can make
1. **Crash zoom** in your own skits: the new deadpan default has none (the measured reels use none). Keep your BUFF BOY-style crash zooms as proposal B?
2. **Side-choosing endings** ("comment Team A or B"): Meta demotes vote-bait. Replace with an open question or a Part-2 tease? (This touches a ledger rule, so it's your call.)
3. **Before/after for Physio Spot's own channels:** my reading of HCSA reg 5(1)(d) is "no people before/after anywhere, including own social". Confirm with your compliance contact.
4. **Trick-the-viewer scam remix:** allowed on brand or health accounts, or personal only?
5. **Romance paid vs organic line:** proposal is that organic may show a completed kiss between adults, while paid stops at the near-kiss with no bed framing.
6. **The white/black 9:16 frame container** (the picture inside a frame with a header, common in drama and mystery reels): on brand accounts it can read like a repost page. Build it anyway?
7. **AI/CGI labels** for FOOH-style spectacle: caption only, or on screen too?
8. **Send references** you rate for mystery/heist, gym edits and SG founder reels: the evidence there was the thinnest.

## Engine features the research asks for (not built yet; marked `_needs_feature` in presets)
Ordered by how many modules need them:
- a protected pause before the punch, plus silence beats;
- uncut "money" holds;
- a wipe/split before|after reveal card;
- cut-rate acceleration targets;
- a music dip longer than 0.3 s and a music build;
- the frame container layout;
- name, time-jump and date/place end cards;
- freeze-frame and episode labels;
- speed ramps;
- a clue-rewind montage.
