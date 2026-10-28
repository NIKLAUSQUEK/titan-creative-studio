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

## 8. Borrowed viral cold open → bait-and-switch: Omegle "ex-lovers" clip → "3 steps to scaling" (Instagram, Vaughn Major / Major Design)
- **Stats:** 40.9 s; 1.3K likes, 41 comments. One cut that matters, at 16.3 s.
- **Structure:**
  - 0-16 s: an already-viral Omegle clip (watermark @romannadolfo) inside an Omegle UI frame, split top/bottom. A girl says "I kinda look like my ex… he even did little beats like that", then "Lizzie?" / "Daniel?": the ex-lovers reunion the audience already knows and loves;
  - 16.3 s: the top window "skips" to the creator himself, who delivers "If you just started a business, here's a 3-step scaling roadmap" (referrals → online presence → paid ads and content), with a growing numbered list top-left and one big CAPS word per beat;
  - the bottom window keeps the original guy's face, now reading as bored or thinking: an accidental reaction track and the joke of the edit.
- **Why it works:** the borrowed clip buys the first 3-16 s of attention for free (recognition + curiosity), and the format switch is the pattern-interrupt. The lesson then rides on the leftover goodwill. Caption: "Lock in 🤦🏽‍♂️… Here's how to grow".
- **Rights:** the footage is someone else's (the original creator, plus two private people on a video-chat). Updated 2026-10-28 (Klaus, ledger [clips]): reposts, Remix, Stitch, Duet and reused clips are one workflow on every account and Klaus handles rights; bring clips in with `editor.py collab add`, tag the creator in the caption (no on-screen credit) and reach out. Format-jack (recreate) stays the fully owned option. See genre-playbooks.md §31.

## 9. "Build your own AI video editor with Claude Code" (Instagram, millee.md)
- **Stats:** 76.9 s, 18.3K likes, 10.2K comments (a comment-to-get CTA: "comment MOTION").
- **Measured:** 16 cuts, median shot 2.7 s, 256 words/min (very fast talker).
- **Edit:**
  - split layout: animated explainer panels on a beige paper background in the top half, the talking head in the bottom half;
  - the hook is a collage of other creators' AI-edited reels;
  - step headers ("Step 1. Set it up") in an orange + black serif-ish sans;
  - one bold white CAPS word per caption at mid-frame;
  - the panels are motion graphics (folders opening, connector lines, a colour-fan icon, prompt cards).
- **The workflow it teaches:** Claude Code desktop plus Remotion, HyperFrames (motion graphics), FFmpeg, Whisper and yt-dlp, then:
  - study 3-5 reference links into a "brand sheet";
  - drop raw footage in;
  - Claude cuts pauses over ~0.1 s, adds captions, music and motion graphics, shows a storyboard, and revises on notes.
- **Vs our editor:** same core (FFmpeg + Whisper + Claude revisions + style from references), and ours adds the strategist brief, compliance, B-roll matching, face recognition, variants, chats and songs. Their one real edge is designed motion-graphic panels. Built in response: `editor.py study` (refs → measured style + preset) and the `split` B-roll layout.

## Not yet studied (Facebook needs a login for these)
- 2 (carousel/static with legitimacy, news/scam-expose vibe like SnapSaigon), 3 (new release / mall / product creative) and 4 (minimal-edit reaction) could not be opened.
- **To share them:** send screenshots of each slide, or download them on the PC with Style Lab using your own logged-in browser (`Run-StyleLab.ps1 -Browser chrome`).
- Until then, the `kicker` card style (coloured tag bar + headline, e.g. "⚠️ SCAM ALERT") is a draft of the news look.
