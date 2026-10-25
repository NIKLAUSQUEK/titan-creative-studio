# Edit references from Klaus (2026-10-25)
These Facebook references were studied for technique only; their content is never reused or re-uploaded. The numbers below were measured locally (ffmpeg cut detection, faster-whisper, audio-energy hits) and checked by looking at frame sheets.

## 1. Gen Z header + SFX: "Who upset lil bro?!" (Tyler Blunden, travel, Pakistan): `genz-header-skit`
- **Stats:** 21 s, 5.7M plays. Only 3 cuts (average shot 5.3 s): raw selfie walk-and-talk, with no jump-cut frenzy.
- **The header does the work.** It stays on screen the whole time at the top:
  - line 1 is context as an emoji (🇵🇰);
  - line 2 is a 2-word CAPS reaction plus 😭💀 ("NAHHH BRO 😭💀");
  - the text is bold white with a heavy black outline.
  - It frames the joke (the viewer knows the feeling before the payoff), and there are no subtitles.
- **SFX:** loud hits at 0.5, 1.95, 3.35, 5.35 and 8.55 s, one per reaction beat (every ~1.5-2 s).
- **Caption copy:** a question plus emoji ("Who upset lil bro?!... 😭💀🇵🇰") plus 4-5 place hashtags.
- **Lesson:** write the header as the viewer's reaction, not as a title. Keep it 2-4 words plus emoji, with an emoji context line.

## 5. Horror tension: bathroom scare short + BTS (DJI RS5 promo): `horror-tension`
- **Stats:** 99 s. Average shot about 10 s: long held, gimbal-smooth shots with slow push-ins.
- **Grade:** cold fluorescent teal/green with crushed blacks and low saturation. Darkness itself is the tension; lights go out and come back.
- **Sound:** sudden hits roughly every 1-2 s in the opening 17 s (1.0, 1.95, 2.95, 4.8 …), a sting/rumble build, and silence before the scare.
- **Structure:** cold open on the scare → story → BTS split-screen (the brand reveal).
- **Lesson:** tension comes from holding the shot longer than is comfortable, plus sound, not from cutting. Flicker the light on scene changes.

## 6. Trend audio beat switch: "My name is … but they call me…" (Alyson Hannigan): `trend-beat-switch`
- **Stats:** 17.5 s, 4.9M plays.
- **Intro (4 s):** to camera, with two white rounded caption boxes: a setup line, then a teaser line ending "…".
- **The drop:** on the beat drop, every clip switches on a beat (cuts at 4.2, 6.1, 7.9, 9.3, 12.2, 13.9, 15.5 s), each with ONE centred white label word (the role name).
- **Lesson:** the format is a fill-in-the-blank promise in the intro, then rapid proof images on the beats. Use licensed or original music for brands; personal accounts add the trend sound in-app.

## 7. Texting scenes + suspense doc-promo: "MUSK" documentary reel (Instagram @muskdoc): `texting-suspense` + `recipe.chats`
- **Stats:** 91.2 s, 93.6K likes; 14 cuts, average shot 6.1 s (cuts at 2.4, 3.4, 7.5, 12.2, 22.4, 30.3, 33.7, 36.5, 46.1, 64.0, 70.2, 75.9, 79.5, 86.3 s). Long holds; the tension comes from sound and the texts, not from cutting.
- **Texting grammar:**
  - full-black frame with iMessage-style bubbles: blue "me" bubbles on the right, dark-grey "them" bubbles on the left, tiny sender names above ("Ashley", "EM");
  - bubbles arrive one at a time, with a "•••" typing bubble before each reply; older bubbles scroll up;
  - the line the story turns on is shown ALONE and LARGE ("I have over 10 thousand lasers in space right now.");
  - no subtitles over the chat cards; the interviewee's voice keeps running underneath.
- **Spine:** the interviewee in a warm interior (white dress), archival inserts, a space/rocket insert with a "T+01:01:41" countdown, and a small persistent title top-left ("MUSK #MuskMovie").
- **Sound:** a suspense bed with a hit or pulse every ~1-3 s (2.55, 3.6, 4.9, 5.3, 5.75, 6.7, 7.75, 8.2 s …); each bubble lands on a soft tick.
- **Strategy:** a person retells what someone said, and the receipts appear as the texts, so the viewer reads ahead of the voice and gets the payoff twice (read + heard). This works for any "they told me…" story: patient-safe for health brands only when the texts are the founder's own or clearly a dramatised recreation (compliance pack: no patient testimonials).
- **Built:** `recipe.chats[]` (tools/editor/titan_editor/chatanim.py) renders this exact grammar as a cutaway with a pop per message and captions hidden; a brief beat's `chat` field creates it; preset `texting-suspense`; genre module §30.

## Not yet studied (Facebook needs a login for these)
- 2 (carousel/static with legitimacy, news/scam-expose vibe like SnapSaigon), 3 (new release / mall / product creative) and 4 (minimal-edit reaction) could not be opened.
- **To share them:** send screenshots of each slide, or download them on the PC with Style Lab using your own logged-in browser (`Run-StyleLab.ps1 -Browser chrome`).
- Until then, the `kicker` card style (coloured tag bar + headline, e.g. "⚠️ SCAM ALERT") is a draft of the news look.
