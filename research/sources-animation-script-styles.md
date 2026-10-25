# Sources: animated/faceless styles + script voice DNA (researched 2026-10-25)

Feeds `styles/animation.json` and `styles/script.json` (style home: `python scripts/styles.py`). Kept verbatim as the evidence record; vendor/affiliate figures are labelled as claims in the text.

Research date 2026-10-25. All sources are public and cited inline. No files were written. Brand codes: **PS** Physio Spot / **H360** heal360 (physio clinic education, SG health pack), **PP** Power Protein (VN pack), **PF** PeachForm (women's fitness), **TA** TITAN.AI (AI agency), **KQ** Klaus founder/personal.

**Source quality.** Most "how-to" sources on faceless channels are vendor or affiliate blogs. Figures from them (subscriber counts, RPMs, "$3k/month") are labelled as claims. The one primary source is the local `higgsfield-video-explainer` skill (`/home/user/titan-creative-studio/.agents/skills/higgsfield-video-explainer/SKILL.md` + `references/prompts.md`). I could not fetch the live preset catalog because the Higgsfield MCP needs authorisation in this session.

---

## 0. Higgsfield route facts that apply to every style (verified)

**The explainer skill pipeline:**
- One style key: a CMS preset resolved via `preset resolve`, or a Nano Banana Pro (`nano_banana_2`) swatch or mascot image.
- N blocks of exactly 10 s each (duration in minutes × 6, 1–10 min).
- One `seed_audio` voice take per block. Narration is 20–24 words, about 8–9 s, and must stay under 9.5 s. Numbers are spelled out, and the script never says "in this video".
- One `gemini_omni` clip per block (10 s, 720p). The same style-key image is attached to every clip.
- Server-side `explainer_video` assembles the blocks. It centres short takes, speeds small overruns and never stretches video.
- Aspect is 16:9 or 9:16. Burned subtitles cost 0.05 credit per block, with fonts patrick, caveat, marker or anton.
- Modes are mascot or faceless.
- Hard rules: strictly non-photoreal, no spoken words or lip-sync in clips, all image/video prompts in English.

Source: local skill files above.

**The video-block prompt template is the house format.** Every style key below is written to slot into it:
```
STYLE REFERENCE: Match the attached reference image EXACTLY. <STYLE tokens>
SCENE: <one action> · MOTION: <camera> · AUDIO: <ambient/music, no voice> · NEGATIVE: <drift + realism bans, no text/logos/lip-sync>
```
Every STYLE descriptor ends with: `non-photorealistic, illustrated, not a photo, no live-action, no realism`.

**Known live skills and presets:**
- "Stickman cartoon explainer" uses Google (Gemini) Omni, English narration and optional subtitles ([higgsfield.ai/skills/stickman-cartoon](https://higgsfield.ai/skills/stickman-cartoon)).
- Other named explainer looks: Watercolor Chronicle, Editorial Motion Graphics (= `/vox-mixed-media` per our `motion-design.md`), Paper Diorama, Pastel Flat 2D ([higgsfield.ai/skills/faceless](https://higgsfield.ai/skills/faceless), [explainer-intro](https://higgsfield.ai/explainer-intro), up to 10 min, 9:16 + 16:9).
- Mixed Media is a separate footage-stylising tool with 30+ presets ([HF blog](https://higgsfield.ai/blog/Mixed-Media-AI-Video-Generator-for-Stylized-Video-Edits)).
- Always run `get_explainer_presets` live. Preset names change.

**Routing rule of thumb:**
- Non-photoreal narrated pieces go to the explainer skill (Omni).
- Photoreal or 3D-character pieces go to Nano Banana / GPT Image key frames, then Seedance 2.5 (default) or Kling (character/motion-control).
- Text-, data- or UI-heavy pieces go to HyperFrames/Remotion. AI renders lettering as gibberish ([Morphic](https://morphic.com/resources/videos/whiteboard-animation-videos)), so all real text goes in code or the editor, never in generation.

---

## PART A: Animated / faceless video styles

### A1. Stickman / stick-figure explainer
- **Look:** Black-line stick figures, round heads and often dot eyes, on white or off-white. Props are minimal and there are 1–2 accent colours (red for danger, yellow for highlight). Labels sit beside the figures. Many 2025–26 AI channels add a "doodle" wobble line.
- **Signature channels:**
  - Comedy/education: Casually Explained (~4M subs, per [vidpros](https://vidpros.com/top-faceless-youtube-channels/)), CGP Grey (stick-figure educational, per [breadnbeyond](https://breadnbeyond.com/youtube-marketing/animation-channels/)).
  - Philosophy/psychology: Sisyphus 55, StickBehavior (finance + psychology, under 5 min, [YT](https://www.youtube.com/channel/UCfKjF2hUdxw173PLkXv82ew)), StickFigure Explains (~89k, [autonolab](https://blog.autonolab.com/niches/2026-01-23-faceless-youtube-psychology/)).
  - Pure animation lineage: Alan Becker (Animator vs. Animation).
- **The 2025–26 viral AI format:** "doodle stickman" psychology/history videos of 5–10 min. They run about 1.5 s per image (189 images over 4:47 in one tutorial), with an ElevenLabs-style calm male narrator and no music ([sozai transcript](https://sozai.app/transcript/stickman-animation-faceless-ai-youtube-2026/index.md); the creator claims 60k subs in 90 days, unverified). Vendors describe the formula as "emotional premise + simple consistent visuals + tight scene pacing" ([search summary](https://www.atlabs.ai/blog/how-to-build-a-faceless-youtube-channel-with-ai-in-2026)).
- **Best uses:**
  - PS/H360: "why your back hurts after sitting", pain-science myths.
  - KQ: founder psychology, decision-making.
  - TA: "how an AI agent actually works".
  - PF: habit psychology.
  - PP: "what protein does after you eat it".
- **Pipeline:** research → script (hook, 3–5 beats, payoff) → explainer skill with the Stickman preset, faceless mode or a stickman mascot → voice → Omni blocks → assemble. Add subtitles, or burn captions locally in our editor.
- **Tools:** the explainer skill's stickman preset (first choice). For high-cut-rate 1.5 s pacing, generate Nano Banana stills and assemble them in the local ffmpeg editor with Ken-Burns moves (cheaper than 10 s Omni blocks).
- **STYLE KEY:**
  `hand-drawn stick-figure doodle animation, thin uneven black marker lines on warm off-white paper, round heads with simple dot eyes and line mouths, no shading, no gradients, single accent colour #E63946 used only for emphasis objects, generous negative space, slight line boil, non-photorealistic, illustrated, not a photo, no live-action, no realism`
- **Character consistency:** Use a mascot key with one distinguishing prop (glasses, a tie colour or a cap). Never rely on the face. Repeat the exact identifier phrase in every block.
- **Pacing:**
  - Explainer route: 1 scene per 10 s with internal motion.
  - Viral long-form route: a new image every 1.5–3 s.
  - Shorts: a cut every 1–2 s.
- **Voice:** Calm, slightly wry, second-person ("you"), conversational.
- **Music/SFX:** Often none. Otherwise a soft lo-fi or plucky bed. Use whoosh, pop and scribble SFX on each new element.
- **Length/aspect:** Long-form 6–12 min at 16:9. Shorts 30–60 s at 9:16.
- **Cost tips:** Stills plus local motion beat video generation by an order of magnitude. Reuse a pose library of 30 mascot poses across videos. Draft 1 minute first.
- **Failures:**
  - Models drift into realistic humans. Fix with a style lock and realism negatives ([Selar guide](https://selar.com/55p87p7445)).
  - Garbled on-screen text.
  - Sameness: "interchangeable formats" get suppressed ([satura](https://saturaai.com/blog/how-to-launch-free-stickman-psychology-channel-faceless-youtube-format-built-for-f-ozqevy)). Differentiate with original research and a recurring character.
  - YouTube "inauthentic/mass-produced content" risk.

### A2. Whiteboard / hand-drawn doodle explainer
- **Look:** Marker drawings appear stroke by stroke on a white board. A hand may be visible. Earlier drawings stay on the board as new ones appear. Mostly monochrome with 1–2 colours.
- **Examples:** RSA Animate (the classic), Minute Physics (hand-drawn), many corporate L&D explainers. AI tools include InVideo whiteboard, VideoScribe and Animaker ([InVideo](https://info.invideo.io/which-ai-can-generate-a-whiteboard-style-explainer-video-from), [Atlabs](https://www.atlabs.ai/blog/how-to-make-whiteboard-explainer-videos-in-2026-using-ai)).
- **Best uses:**
  - PS/H360: "how a disc bulge heals", rehab progressions.
  - TA: process diagrams for B2B and sales decks.
  - PP: digestion.
  - Bottom-of-funnel explainers on landing pages.
- **Pipeline:** script at 150–300 words per 1–2 min (Atlabs) → board layout plan (what accumulates where) → stills of each finished drawing → animate the "draw-on" → add text labels as editor layers.
- **Tools:**
  - Best fidelity: Nano Banana final-state frames, then a draw-on reveal with a stroke mask in HyperFrames/Remotion. The mask route is deterministic and cheap.
  - Alternative: the explainer skill with a custom style ("hand-inked black marker on off-white paper" from the skill examples). Omni can do "drawing appears" motion, but drawn letters fail.
- **STYLE KEY:**
  `whiteboard doodle illustration, confident black dry-erase marker linework on bright white board, occasional blue and red marker accents, flat, no shading, slight marker texture and streaks, drawings accumulate on the same board, clean composition with labelled-space left empty, non-photorealistic, illustrated, not a photo, no realism, no on-screen text`
- **Character consistency:** One simple doodle character, with the same described features every time ([Atlabs](https://www.atlabs.ai/blog/how-to-make-whiteboard-explainer-videos-in-2026-using-ai)).
- **Pacing:** A new drawing every 3–6 s. Draw speed synced to VO.
- **Voice:** Teacherly, friendly and clear, with medium pace.
- **Music/SFX:** Light acoustic or ukulele bed. Marker-squeak SFX at low volume.
- **Length/aspect:** 60–180 s at 16:9 for web/YouTube. A 9:16 version works if the board is stacked vertically.
- **Cost tips:** Code-driven reveals cost zero credits. Generate only the final frames.
- **Failures:**
  - AI hand glitches. Fix before render or drop the hand ([satura](https://saturaai.com/blog/how-to-make-ai-whiteboard-videos-fast-workflow-that-turns-one-prompt-into-full-you-aj1-ic)).
  - Gibberish lettering.
  - The board "resets" between clips. Keep accumulation in the editor.

### A3. Kurzgesagt-style flat vector motion explainer (generic)
- **Look:** Flat geometric vector shapes on a saturated dark-navy or deep-space palette. Soft glows and subtle gradients, rounded shapes, cute simplified creatures. Constant gentle motion and loops, rendered at 60 fps.
- **Examples:** Kurzgesagt (built in Illustrator + After Effects at 60 fps with expression loops, per their [Skillshare course](https://www.skillshare.com/en/classes/motion-graphics-with-kurzgesagt-part-1/631970755)), TED-Ed (some), Infographics Show (lower-budget flat).
- **Best uses:**
  - PS/H360: immune and inflammation science.
  - PP: muscle protein synthesis.
  - TA: "how LLMs think".
  - Premium brand explainers with trust and save value.
- **Pipeline:** research → script → style frames → asset library → animate → sound design.
- **Tools:**
  - Explainer skill with the "Pastel Flat 2D" or a custom flat-vector preset (key via Nano Banana).
  - For precise loops and data, use HyperFrames/Remotion with SVG assets generated via GPT Image, cleaned and vectorised.
  - Seedance and Kling are not needed.
- **STYLE KEY (generic, no IP):**
  `flat 2D vector motion-graphics illustration, clean geometric shapes, no outlines, soft inner glows and subtle radial gradients, deep navy #1B1F3B background with saturated teal, coral, gold accents, rounded friendly creature designs with simple dot eyes, crisp edges, calm cosmic lighting, non-photorealistic, illustrated, not a photo, no realism, no on-screen text`
- **Character consistency:** Use a species mascot (for example a round blob cell) with fixed colour hex values in the key.
- **Pacing:** 1 composition per 4–8 s with continuous secondary motion. No hard-cut frenzy.
- **Voice:** Measured, warm, wonder-led, with slight wit. Avoid an accent you cannot license.
- **Music/SFX:** Orchestral or ambient synth score. Soft UI blips and pops.
- **Length/aspect:** 6–12 min at 16:9. 45–60 s cutdowns at 9:16.
- **Cost tips:** Generate a reusable asset sheet once and animate it in code.
- **Failures:**
  - It looks like a cheap clone. Use your own palette and mascot. Never copy their bird or characters.
  - Gradient banding.
  - Over-busy frames.

### A4. 2D anime / hand-painted Japanese-animation-inspired (generic)
- **Look:** Cel-shaded characters and painterly watercolour or gouache backgrounds. Big skies and cumulus clouds, warm nostalgic light, gentle wind in grass, expressive eyes.
- **Examples:** Lo-fi "study girl" loops, anime-style AI shorts and Seedance animation prompt guides ([Magnific, Seedance 2.5 styles](https://www.magnific.com/blog/seedance-2-5-animation-prompts/), page blocked; summarised via search). Never reference a studio, film or character by name.
- **Best uses:**
  - KQ: emotional founder-story flashbacks.
  - PF: the "slow morning routine" mood.
  - H360: recovery journey as fiction, clearly labelled.
  - Storyboards of Klaus's life (/storyboard).
- **Pipeline:** character sheet (Nano Banana, turnaround) → style key → key frames → I2V in Seedance 2.5 or Kling for gentle motion → VO and score.
- **Tools:** Explainer skill (Watercolor Chronicle or a custom key) for narration. Nano Banana keys plus Seedance or Kling for character acting.
- **STYLE KEY:**
  `hand-drawn 2D anime cel animation, clean thin lineart, two-tone cel shading on characters, lush hand-painted gouache backgrounds, towering cumulus clouds, warm golden-hour light, soft film grain, nostalgic slice-of-life mood, original character designs, non-photorealistic, illustrated, not a photo, no realism, no text, no logos`
- **Character consistency:** A character sheet (front, ¾ and side) attached to every generation. A hair silhouette and outfit colour lock. Kling Elements, or Seedance omni_reference with the sheet.
- **Pacing:** 3–6 s holds with slow pans. Let moments breathe.
- **Voice:** Soft, intimate, first-person, reflective.
- **Music/SFX:** Piano and strings or lo-fi. Wind, cicadas, train ambience.
- **Length/aspect:** 30–90 s at 9:16 for story reels. 16:9 for YouTube.
- **Cost tips:** Use the anime look at 480p for drafts. Anime hides compression well.
- **Failures:**
  - IP mimicry (named studio prompts). Avoid it legally and reputationally.
  - Lineart flicker.
  - Off-model faces between shots.

### A5. 3D feature-animation cartoon (generic, no IP)
- **Look:** Stylised 3D with soft subsurface skin, big eyes and heads, appealing shapes, warm cinematic lighting and shallow depth of field. This is our existing `animation-3d-cartoon.md` key.
- **Examples:**
  - Zack D. Films: 3D curiosity-gap Shorts, ~27.6M subs, ~100% Shorts views per [OutlierKit](https://outlierkit.com/channel/zackdfilms) estimates. Its job ads ask for 20–45 s 3D clips ([recruitee](https://zackdfilms.recruitee.com/o/3d-generalist/c/new)).
  - Pixar-style AI shorts.
- **Best uses:**
  - PP: mascot product stories.
  - PF: a body-positive character series.
  - PS/H360: "inside your knee" 3D body Shorts, Zack-D-style "what happens if…".
  - TA: an agent mascot.
- **Pipeline:** character sheet → style key → shots → Seedance 2.5 omni_reference → VO → edit.
- **Tools:** Nano Banana 2 for cartoon characters (Higgsfield default), Seedance 2.5 for video, Kling for motion-control acting. 3D medical interiors can use the `generate_3d` / scene builder for angles.
- **STYLE KEY:** Reuse ours:
  `stylised 3D feature-animation render, soft subsurface skin, slightly oversized heads and eyes, rounded appealing shapes, warm key light with soft rim light, shallow depth of field, rich saturated but gentle colour, polished CG finish, original characters`
  Add `no text, no logos`.
- **Character consistency:** Sheet plus Element. The four-part prompt (subject + details + action + style key) is already in `animation-3d-cartoon.md`.
- **Pacing:** Shorts cut every 1–2.5 s with a visual gag in the first 1 s.
- **Voice:** Zack-D-style dry narrator ("This man ate 1 kg of protein. Here's what happened.") or character VO.
- **Music/SFX:** Heavy foley: squelch, pop, boing.
- **Length/aspect:** 20–45 s at 9:16.
- **Cost tips:** Draft at 480p. Reuse sets.
- **Failures:**
  - Uncanny "almost real" skin.
  - IP-lookalike characters.
  - Gross-out body content flagged by platforms.
  - SG health: anatomical scare tactics.

### A6. Claymation / stop-motion look
- **Look:** Plasticine figures with fingerprints and imperfections, a felt and miniature set, stepped motion on 2s or 12 fps, and tilt-shift miniature lighting.
- **Examples:** Aardman-like aesthetics (generic only), the "felt/plasticine" AI-ad trend. Magnific's Seedance guide advises naming the medium ("felt, plasticine, ink, wax") so the model animates the material ([search summary of Magnific](https://www.magnific.com/blog/seedance-2-5-animation-prompts/)).
- **Best uses:**
  - PP: a cute product hero.
  - PF: playful habit tips.
  - PS: "the angry hamstring" character skits.
  - Brand-safe humour for health topics. Its softness lowers the sense of threat.
- **Pipeline:** clay character key (Nano Banana) → set key → Seedance or Kling I2V with "stop-motion stepped" motion → drop frames locally to 12 fps in ffmpeg for authentic step.
- **STYLE KEY:**
  `handmade claymation stop-motion, plasticine characters with visible fingerprints and slight surface imperfections, felt and cardboard miniature set, soft warm practical lighting, shallow tilt-shift depth of field, tactile matte textures, non-photorealistic, handcrafted, not a photo of real people`
  Motion line: `stop-motion animation on twos, slightly jittery stepped movement`.
- **Character consistency:** Clay simplifies faces, so it is very consistent. Lock colours and props.
- **Pacing:** 2–4 s shots.
- **Voice:** Playful, characterful (persona VO, never a cloned celebrity).
- **Music/SFX:** Pizzicato or quirky. Squish and tap foley.
- **Length/aspect:** 15–45 s, 9:16 or 1:1.
- **Cost tips:** Generate at 24 fps and decimate to 12 fps locally (free authenticity).
- **Failures:**
  - Motion too smooth (reads as CG).
  - Melting faces in fast action. Keep actions simple.

### A7. Paper cut-out / collage (Vox-style editorial mixed media)
- **Look:** Hand-cut paper shapes with torn edges, tape, halftone dots and newspaper clippings. Archival photos are cut out with white borders. Bold flat colour and big cut-out headlines, with highlighter strokes and red-circle annotations ([videoai.me](https://videoai.me/blog/what-is-vox-style-video-explained-2026)).
- **Examples:** Vox, Johnny Harris-era "visual evidence" approach ([Press Gazette](https://pressgazette.co.uk/?p=184694)), the open-source "Vox Director" agent skill ([GitHub](https://github.com/Alisa0808/vox-director)).
- **Best uses:**
  - TA: "how AI changed X industry" commentary.
  - KQ: "the history of the protein industry", founder essays.
  - PS: "the posture myth: where it came from" with receipts.
  - Commentary pieces (with SOURCES.md).
- **Pipeline:** research + receipts (screenshots and documents you have rights to) → script → collage plates → animate layers (parallax, stop-motion jitter, highlighter wipes) → VO.
- **Tools:**
  - Higgsfield `/vox-mixed-media` = "Editorial Motion Graphics" preset (explainer).
  - For real documents and charts, use HyperFrames/Remotion compositing. Real text must be crisp, so never generate it.
- **STYLE KEY:**
  `editorial paper-collage animation, hand-cut paper shapes with torn white edges, visible tape strips, halftone dot textures, aged newsprint and kraft paper, bold flat red, cream and black palette, cut-out archival-photo style elements with white borders, highlighter and red-marker annotations, slight stop-motion jitter, non-photorealistic, illustrated, no legible text, no logos`
- **Character consistency:** Usually no characters. Use cut-out "evidence" objects and one recurring motif (a red string or a pin).
- **Pacing:** A new layer or annotation every 1–2 s. A scene change every 5–8 s.
- **Voice:** Journalistic, curious, confident and precise.
- **Music/SFX:** Minimal synth or pulse bed. Paper rustle, tape rip and marker squeak.
- **Length/aspect:** 3–12 min at 16:9. 60 s at 9:16.
- **Cost tips:** Code-animate real assets. Generate only textures and plates.
- **Failures:**
  - Fake "documents" generated by AI. This is fabricated evidence and a hard no.
  - Unreadable text.
  - Copyrighted photo use.

### A8. Motion typography / kinetic text reel
- **Look:** Words are the visuals. Bold type is animated to the VO and beat, with scale and position punches, highlighted keywords, emoji or icons, and often a solid or gradient background or a blurred B-roll.
- **Examples:** Quote, motivational and "LinkedIn lesson" reels, Hormozi-style captions on talking heads, lyric-video aesthetics.
- **Best uses:**
  - TA and KQ thought-leadership quotes.
  - Repurposing podcast lines, carousel-to-reel.
  - PS myth vs fact.
  - Cheapest high-volume format.
- **Pipeline:** script or transcript (faster-whisper word timestamps) → highlight-word map → HyperFrames/Remotion template → music beat-sync.
- **Tools:** HyperFrames/Remotion or the local editor caption presets. **The explainer skill explicitly excludes motion-typography reels.** No AI video needed.
- **STYLE KEY (as design tokens, not a prompt):** font pair (e.g. Anton + Inter), 2 brand colours plus a highlight colour, an easing curve (expo-out 250 ms), max 3–5 words on screen, keyword highlight box, safe zones for 9:16 UI.
- **Character consistency:** N/A. The brand type system is the consistency.
- **Pacing:** A word-group change every 0.4–1.2 s, synced to syllables or beats.
- **Voice:** Punchy original VO, or Klaus's real voice. Text-only plus music also works.
- **Music/SFX:** Licensed beat. Whoosh and hit on keywords.
- **Length/aspect:** 7–30 s at 9:16. 1:1 for LinkedIn.
- **Cost tips:** Zero generation credits. Template once and batch.
- **Failures:**
  - Text in platform UI zones.
  - Too many words per screen.
  - Off-beat timing.

### A9. Infographic / data-viz animation
- **Look:** Animated charts, counters, maps, timelines and icon arrays in a brand palette, with clean sans type.
- **Examples:** The Infographics Show (lower end), Visual Capitalist-style, Our World in Data-style explainers, Vox charts.
- **Best uses:**
  - TA: ROI and "hours saved" (real client data only).
  - PP: protein per dollar comparisons (substantiated).
  - PS/H360: public-health statistics with a source on screen.
  - Carousels-to-reels.
- **Pipeline:** sourced dataset (SOURCES.md) → chart choice (dataviz skill rules) → animate in HyperFrames/Remotion → VO → source line on screen.
- **Tools:** HyperFrames/Remotion only for charts. Optional Nano Banana background textures or icon sets. Never generate numbers with AI image or video models.
- **STYLE KEY (tokens):** palette (validated categorical/sequential), grid, type scale, animation grammar (bars grow from baseline over 600 ms, counters ease-out, one idea per screen), an on-screen source line in 10 pt.
- **Pacing:** One data point per 3–5 s. Hold the key number for 1.5 s or more.
- **Voice:** Crisp analyst tone: "Here's the number that matters."
- **Music/SFX:** Minimal tech pulse. Tick and counter SFX.
- **Length/aspect:** 20–60 s at 9:16 or 4:5. 2–5 min at 16:9.
- **Cost tips:** Fully deterministic, so zero credits and reusable templates.
- **Failures:**
  - Invented or unsourced stats, which our hard rules forbid.
  - Truncated axes that mislead.
  - SG health superlatives hidden in charts ("#1").

### A10. 2.5D parallax photo animation (history / documentary)
- **Look:** Still photos are split into foreground, midground and background layers. A slow camera dolly creates depth, with dust particles, grain and vignette. This is the "Ken Burns plus depth" documentary look.
- **Examples:** History documentaries, "history in 60 s" channels and true-crime YouTube. Tools: DepthFlow (open-source depth-map parallax, [PyPI](https://pypi.org/project/depthflow/)), ComfyUI Depthflow nodes ([runcomfy](https://www.runcomfy.com/comfyui-nodes/ComfyUI-Depthflow-Nodes)), Immersity AI.
- **Best uses:**
  - KQ: life storyboard from real family photos (best fit; the CLAUDE.md rule says real photos beat generated ones).
  - PS/H360: clinic origin story.
  - TA: case-study before/after of a business (not health).
  - Archival brand history.
- **Pipeline:**
  1. Gather real photos with rights.
  2. Optional restore or upscale (`upscale_image`) and colourise.
  3. Make a depth map.
  4. Do the parallax move locally (DepthFlow, free), or prompt Seedance or Kling I2V with camera-only motion. Describe camera movement, not character movement ([picassoia](https://blog.picassoia.com/ai-tools-flat-anime-art-3d)).
  5. Add grain, VO and score.
- **STYLE KEY (for generated gap-fill plates only):**
  `archival documentary photograph, period-accurate black-and-white silver-gelatin look, film grain, soft vignette, subtle dust and scratches, natural available light`
  Motion line: `slow 2.5D parallax dolly-in, foreground separates from background, no subject movement, no morphing`. Label any AI recreation as a recreation.
- **Character consistency:** Use real photos. Generated people only as labelled recreations.
- **Pacing:** 4–7 s per photo, slow and dignified.
- **Voice:** Documentary narrator, low and steady, or Klaus first-person.
- **Music/SFX:** Piano or cello score. Room tone, era-specific ambience.
- **Length/aspect:** 60 s reels to 15 min docs.
- **Cost tips:** DepthFlow locally costs zero credits. Use AI only for hero shots.
- **Failures:**
  - Face warping when the model animates people. Use camera-only prompts.
  - Fake "archival" images passed off as real (misleading).
  - Edge stretching on large moves.

### A11. Lego/toy-box or isometric 3D diorama
- **Look:**
  - Toy: everything is made of plastic bricks or minifigure-like toys, with stop-motion feel.
  - Isometric: a tiny world on a floating cube or diorama base, orthographic or isometric camera, tilt-shift, cute miniature detail.
- **Examples:** AI "Lego videos" trending on TikTok/IG, including political satire. Lego is not linked to them ([PlastEurope](https://www.plasteurope.com/news/PLASTIC_FANTASTIC_t260243)). Brick-world image-to-video prompt trends ([Carat, May 2026](https://carat.im/it/curated/ai-lego-world-prompt-guide-en)). Isometric "day in the life of a…" dioramas.
- **IP caution:** "LEGO" and minifigure designs are trademarked. Prompt "generic interlocking toy bricks, original toy figures". Never use the logo, studs-with-logo or the minifig head shape for brand ads.
- **Best uses:**
  - TA: "your business as a tiny factory run by agents" (isometric is excellent for systems).
  - PS: clinic tour diorama.
  - PP: supply-chain story.
  - History-in-60 s Shorts.
- **Pipeline:** diorama key (Nano Banana) → camera orbit via Seedance or Kling, or Higgsfield 3D scene builder / `generate_3d` for true-3D consistent angles → editor.
- **STYLE KEY (isometric):**
  `isometric 3D miniature diorama on a floating square base, orthographic camera at 30 degrees, tilt-shift shallow depth of field, soft global illumination, matte clay-plastic materials, cute simplified props and tiny people, pastel brand palette, clean background, no text, no logos`
- **STYLE KEY (toy):**
  `scene built entirely from generic glossy interlocking plastic toy bricks, original toy figures, stop-motion on twos, macro lens, toy-photography lighting, no brand logos`
- **Character consistency:** Toys and figures are simple. Lock colours. Use the 3D scene builder for multi-angle consistency.
- **Pacing:** 2–4 s per beat. Orbit moves.
- **Voice:** Playful narrator.
- **Music/SFX:** Whimsical. Brick-click SFX.
- **Length/aspect:** 15–60 s, 9:16 or 1:1.
- **Cost tips:** One diorama key with many camera moves. 3D GLB lets you render angles cheaply.
- **Failures:**
  - Trademark lookalike.
  - Brick geometry melting.
  - Isometric angle drifting to perspective.

### A12. Faceless "AI documentary" photoreal (Seedance) with VO
- **Look:** Cinematic photoreal B-roll: landscapes, hands, objects, silhouettes, period recreations. Anamorphic grade and documentary VO. People mostly seen from behind, in silhouette or at distance.
- **Examples:** AI history and true-crime "cinematic documentary" channels. Our `documentary-3d.md` and `realism.md` already define the pipeline.
- **Best uses:**
  - KQ: brand-film moments.
  - PP: farm-to-shaker origin (with real footage preferred).
  - TA: "the future of work" essays.
  - PS: avoid photoreal fake patients. If used, a dramatisation label is mandatory.
- **Pipeline:** research → narration timed per clip → style key (look book) → shot list → Nano Banana or GPT Image keyframes → Seedance 2.5 (draft 480p → final 1080p) → VO → music → `/sound` → edit → 4K upscale of the locked final.
- **Tools:** Seedance 2.5 omni_reference (studio default), Kling for character motion-control, Genjutsu for performance shots. The explainer skill cannot be used because it is non-photoreal only.
- **STYLE KEY:**
  `cinematic documentary realism, ARRI Alexa look, 35mm anamorphic lens, natural motivated lighting, muted teal-and-amber grade, fine film grain, shallow depth of field, handheld micro-movement, real-world textures and imperfections, faces mostly unseen or in silhouette, no text, no logos`
- **Character consistency:** Hero characters as Soul or Element, or avoid faces altogether (the faceless advantage). Use the same wardrobe token in every shot.
- **Pacing:** 3–5 s shots, one 6–8 s establishing shot per scene.
- **Voice:** Deep documentary narrator persona (an archetype from voice-persona-audio.md). Never clone a real narrator.
- **Music/SFX:** Licensed cinematic score. Detailed ambience layers.
- **Length/aspect:** 60 s at 9:16 up to 20 min at 16:9 or 2.39:1.
- **Cost tips:**
  - The most expensive style.
  - Script-lock and animatic first with stills.
  - Use the 2.5D parallax of stills (A10) for 50% of shots.
  - Final-render only approved shots.
- **Failures:**
  - Uncanny faces and hands.
  - Physics errors.
  - Fabricated "real" events.
  - Missing platform AI labels (required by our platform-signals rules).
  - YouTube reused/inauthentic-content demonetisation.

### A13. 15 proven faceless/animated Shorts/TikTok formats (2025–26)
Format list synthesised from niche guides ([opus.pro](https://www.opus.pro/blog/faceless-youtube-niches-2026), [vozo](https://www.vozo.ai/blogs/youtube/profitable-faceless-youtube-niches), [fliki](https://fliki.ai/blog/best-faceless-youtube-niches)). The guides warn against broad "facts" channels: narrow the angle. Horror and mystery formats drive completion.

| # | Format | Best style | Our brand fit |
|---|---|---|---|
| 1 | "What happens to your body if you… (stop sitting / eat 200 g protein / sleep 5 h)" | A5 3D body (Zack-D-like) or A1 | PS/H360, PP, PF (no scare claims; "can", "evidence suggests") |
| 2 | Psychology facts / "Why you do X" | A1 stickman | KQ, PF |
| 3 | History in 60 s / "The man who…" | A10 parallax, A7 collage | KQ, TA (history of AI) |
| 4 | Myth vs Fact (2-panel verdict) | A8 kinetic type, A2 | PS/H360, PP, PF |
| 5 | "How X actually works" mechanism explainer | A3 flat vector, A2 | TA, PP, PS |
| 6 | Philosophy/stoic lessons story | A1, A4 anime | KQ |
| 7 | "Day in the life of a… (Roman soldier / your spine / an AI agent)" POV | A11 isometric, A5 | TA, PS |
| 8 | Moral-parable mini-story (kindness / karma twist) | A5 3D, A4 | KQ, PF (label as fiction) |
| 9 | Money/business math breakdown | A9 data-viz, A8 | TA, KQ |
| 10 | Ranked "tier list" / "Top 5 worst…" | A8 + icons | TA, PF (for health brands avoid "best/No.1" claims about own services) |
| 11 | Mystery / unsolved / "the strangest…" | A12 photoreal, A7 | KQ (personal channel only) |
| 12 | Before/after transformation process (non-health) | A10, A12 | TA (systems), PP (product journey) |
| 13 | Satisfying process / "how it's made" | A6 clay, A11 toy | PP |
| 14 | Quiz / "Can you spot…?" interactive | A3, A8 | PS (posture quiz, no diagnosis), TA |
| 15 | Quote / one-lesson reel from long-form | A8 kinetic over B-roll | KQ, TA (repurpose waterfall) |

---

## PART B: Scripting voice DNA (structure only, never impersonation)
**Rules for every entry:**
- Borrow structure, not catchphrases, signature openers, cadence imitation or voice clones.
- Never imply endorsement by the creator.
- SG health pack, for PS/H360 and any clinic-promoting post on KQ: no testimonials or patient stories as proof, no superlatives, no free/discount inducements, no guarantees, every stat sourced, dramatisations labelled, neutral CTA ("Book an assessment"). Source: local `compliance-sg.md`, consistent with SMC testimonial rules ([SMC advisory](https://healthprofessionals.gov.sg/smc/home/announcements/Index/advisory-medical-practitioners-participation-in-online-search-engine-optimisation-platforms), [SMA](https://sma.org.sg/positionstatement/sma-advisories-issued-1/33)). Physiotherapists fall under the AHPC code. Verify per entity.

**Template convention:** six lines, `[ ]` = fill-in.

### 1. Alex Hormozi: business math, binary verdicts
- **DNA:**
  - Hook: a contrarian verdict or "most people [X]; [Y] wins".
  - Rhythm: short declaratives with math stated aloud ("if A then B").
  - Beats: Promise → Proof → Plan. The order is debated in secondary sources ([summary](https://solopreneurcode.substack.com/p/how-i-write-hooks-that-actually-work)).
  - Devices: dichotomies, analogies, value equation (dream outcome × likelihood ÷ time × effort, from *$100M Offers*).
  - Proof: personal numbers. CTA: soft or none in organic.
  - Length: 30–60 s.
- **Template:**
  1. Most [audience] think [belief]. That's why they're stuck.
  2. Here's the math: [input] × [rate] = [result].
  3. If [condition A], do [X]. If [condition B], do [Y].
  4. I saw this when [own example, real numbers].
  5. The fix is [single action].
  6. Do that for [time] and the math does the rest.
- **Fit:** TA, KQ. Top and middle of funnel.
- **SG health:** Never use "free" or "grand slam" discount offers or guaranteed outcomes for PS/H360. Keep the "math" non-clinical.

### 2. Adam Meakins-style blunt myth-busting physio
- **DNA:**
  - Hook: name the myth flatly and call it out.
  - Rhythm: conversational, cheeky, emphatic.
  - Beats: myth → why it's believed → what evidence says (e.g. the core-stability critique, [Lederman 2010](https://pubmed.ncbi.nlm.nih.gov/20006294/)) → nuance ("it depends") → simple advice (load, move, be patient).
  - Devices: rhetorical questions, analogies to everyday life, humility about evidence limits.
  - Proof: research summaries, not anecdotes. CTA: "share this with someone who…".
  - Advocates "simple honest evidence based advice" ([podcast](https://liftthebarpodcast.libsyn.com/adam-meakins-the-problem-with-the-most-popular-physiotherapy-treatments)).
  - Length: 30–90 s.
- **Template:**
  1. "[Myth]." Let's talk about that.
  2. It sounds right because [plausible reason].
  3. But the research says [finding, cited on screen].
  4. That doesn't mean [overcorrection]; it depends on [factors].
  5. What actually helps most people: [simple, safe action].
  6. Send this to the friend who still [myth behaviour].
- **Fit:** PS/H360. Top of funnel, trust-building.
- **SG health:** Ideal fit, but no mocking named clinics or competitors, no "we're the only clinic that…", and cite sources.

### 3. Mel Robbins-style empathetic self-help
- **DNA:**
  - Hook: "If you've ever felt [emotion]…", validation first.
  - Rhythm: warm, direct second-person, pauses.
  - Beats: name the feeling → normalise ("it's not your fault, it's how your brain works") → one simple tool → a tiny first step.
  - Devices: repetition, permission statements, a named tool.
  - Proof: research reference plus listener-like scenario.
  - CTA: "try it today and tell me".
  - Length: 45–90 s.
- **Template:**
  1. If you've ever [relatable struggle], this is for you.
  2. You're not [lazy/broken]; here's what's happening: [simple mechanism].
  3. Try this: [one-step tool].
  4. It works because [plain-language reason, sourced].
  5. Start with [tiny action] today.
  6. Come back and tell me what changed.
- **Fit:** PF, KQ. Top of funnel and nurture emails.
- **SG health:** Avoid "this will fix your pain". Use "can help".

### 4. Jun Yuh-style personal storytelling (vertical life-lesson reels)
- **DNA:**
  - Hook: an in-scene line or a specific memory ("When I was 22, my mom told me…").
  - Rhythm: cinematic B-roll, VO, intimate.
  - Beats: moment → tension or vulnerability → realisation → universal lesson → gentle challenge.
  - Devices: callbacks, sensory detail, aesthetic B-roll.
  - Proof: lived experience.
  - CTA: reflective question.
  - Length: 45–90 s.
- **Template:**
  1. [Specific age/place], [someone] said "[line]."
  2. I didn't understand it until [event].
  3. [Sensory detail of the turning moment].
  4. What I learned: [lesson in one line].
  5. Maybe for you it's [viewer application].
  6. What's the sentence that changed you?
- **Fit:** KQ (founder brand), PF. Top of funnel.
- **SG health:** Do not tell patient stories. Klaus's own story only, with consent rules.

### 5. MrBeast: stakes and escalation
- **DNA:**
  - Hook: the thumbnail promise delivered in the first seconds.
  - Rhythm: fast, high-energy, constant progress.
  - Beats: big premise → escalating stakes and steps → re-engagement roughly every 3 min (long form) → payoff.
  - The leaked production guide (authenticity unconfirmed, ex-staff say genuine) prioritises CTR, AVD and AVP and the first minute ([Passionfruit](https://passionfru.it/mrbeast-leaked-document-81151/), [Jarvis memo](https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/)).
  - Devices: countdowns, numbers, "but then…".
  - Proof: on-camera reality. CTA: minimal.
- **Template:**
  1. I [extreme premise] to find out [question].
  2. Day/Step 1: [baseline], stakes are [X].
  3. Then it got harder: [escalation].
  4. At [point], [unexpected twist].
  5. Final result: [measured payoff].
  6. Which should we test next, [A] or [B]?
- **Fit:** PP ("we tested 10 protein sources for 30 days"), TA ("AI agent runs my business for 7 days"). Top of funnel.
- **SG health:** No giveaways or contests as inducements for clinics. No body-transformation results as patient proof.

### 6. Ali Abdaal-style calm framework
- **DNA:**
  - Hook: "Here are [N] [things] that [benefit], backed by research."
  - Rhythm: calm, friendly, structured.
  - Beats: frame → numbered points, each with concept + study or book + personal example → summary.
  - Devices: named frameworks, book citations, on-screen text lists.
  - Proof: books, studies, personal experiments.
  - CTA: newsletter or lead magnet.
  - Length: 60 s to 15 min.
- **Template:**
  1. [N] ideas that changed how I [outcome].
  2. Idea 1: [name], from [source]: [one-line explanation].
  3. How I use it: [personal example].
  4. Idea 2 / 3: [repeat pattern].
  5. The common thread: [synthesis].
  6. I put the full system in [lead magnet], link in bio.
- **Fit:** TA, KQ, PF. Middle of funnel (lead magnets).
- **SG health:** Lead magnets must not be "free consult" inducements. PDPA consent applies.

### 7. Gary Vaynerchuk-style raw motivational
- **DNA:**
  - Hook: a blunt truth or call-out ("You're not patient enough").
  - Rhythm: rapid, unscripted feel, repetition, emotional emphasis.
  - Beats: provocation → reframe (long-term, self-awareness, kindness + hustle) → practical push.
  - Devices: rants, rhetorical questions, "macro patience, micro speed".
  - Proof: scale of own businesses.
  - CTA: "go do it".
  - Length: 20–60 s, often clipped from talks.
- **Template:**
  1. Real talk: [harsh truth].
  2. You're worried about [short-term thing].
  3. Meanwhile [long-term reality].
  4. Here's what I'd do: [blunt action].
  5. And be kind while you do it: [human note].
  6. Stop watching. Go [action].
- **Fit:** KQ, TA. Top of funnel. A good clipping format from Klaus podcasts.
- **SG health:** Keep profanity out of clinic channels.

### 8. Steven Bartlett-style founder interview / question-led
- **DNA:**
  - Hook: the guest's most shocking line cold-open, then the question.
  - Rhythm: patient, curious, follow-ups ("why?").
  - Beats: cold open → backstory → hard question → vulnerable moment → lesson.
  - Devices: "what would you say to…", silence, a closing ritual question.
  - Proof: guest authority plus data.
  - CTA: subscribe.
  - Short form: 45–60 s clip around one revelation.
- **Template:**
  1. [Guest]: "[shocking line]."
  2. Q: What did you get wrong about [topic]?
  3. Guest backstory beat: [moment].
  4. Q: Why do most people miss that?
  5. Lesson: [one line].
  6. Full conversation: [link/episode].
- **Fit:** KQ podcast, TA (client founders). Top and middle of funnel.
- **SG health:** Clinician-guest content must stay educational. No patient guests endorsing services.

### 9. Dhar Mann-style moral parable
- **DNA:**
  - Hook: an injustice scene in 3 s plus a click-title ("Rich girl mocks…").
  - Rhythm: simple dialogue, clear villain.
  - Beats: judgment or humiliation → reveal or turnaround → consequence → moral spelled out ([Wikipedia](https://en.wikipedia.org/wiki/Dhar_Mann)).
  - Critiques call the moral philosophy "thin and absolutist" and the titles clickbait (NYT via [bdnews24](https://bdnews24.com/lifestyle/the-moral-philosopher-of-youtube)). Write with more nuance (see villains-conflict.md: both sides get humanity).
  - Devices: a twist reveal, an end-card moral.
  - Length: 60 s to 10 min.
- **Template:**
  1. [Character] mocks [underdog] for [trait].
  2. Underdog responds with [quiet dignity/act].
  3. Reveal: [hidden truth].
  4. Consequence for mocker: [proportionate outcome].
  5. Mocker changes: [humanising beat].
  6. Lesson on screen: "[moral]."
- **Fit:** PF (body-image parables), KQ, TA (hiring stories). Top of funnel.
- **SG health:** Must be labelled dramatisation. Actors never presented as patients. The clinic is never the "hero cure".

### 10. Dr Mike-style doctor reacts
- **DNA:**
  - Hook: "Doctor reacts to [viral health claim]" with a visible pause or wince.
  - Rhythm: pause-and-comment on clips.
  - Beats: clip → expert verdict (correct, partially, wrong) → mechanism explanation → safe takeaway.
  - Devices: rating scale, credentials shown, humour.
  - Proof: guidelines and studies.
  - CTA: "talk to your doctor or physio".
  - Length: 30–60 s or long form.
- **Template:**
  1. Physio reacts: "[viral claim]".
  2. Verdict: [true / half-true / false].
  3. What's actually happening: [mechanism].
  4. Where it's right: [fair credit].
  5. Safer approach: [action] (source on screen).
  6. If [red-flag symptom], see a professional.
- **Fit:** PS/H360 (registered physio on camera), PP (nutrition claims). Top of funnel.
- **SG health:** Strong fit. Use only clips you have rights to (stitch/duet features or fair commentary). No ridicule of named practitioners. No "we're better than…". State credentials accurately.

### 11. Simon Sinek-style why-first
- **DNA:**
  - Hook: a counterintuitive "people don't buy what you do…"-type principle. Write your own principle, not his line.
  - Rhythm: slow, deliberate, storytelling with pauses.
  - Beats: Why → How → What (Golden Circle). Example story of a company or person → principle restated.
  - Devices: contrast pairs, repetition, a simple diagram.
  - Proof: case stories.
  - CTA: reflective.
  - Length: 60–120 s.
- **Template:**
  1. Most [businesses] explain what they do. The ones people love start with why.
  2. Our why: [belief].
  3. So we [how: distinctive method].
  4. Which is why we [what].
  5. Example: [story showing the belief in action].
  6. What's your why?
- **Fit:** KQ, TA, all brand manifestos. Top of funnel and about pages.
- **SG health:** Safe if the why makes no outcome claims.

### 12. Justin Welsh-style LinkedIn solopreneur
- **DNA:**
  - Hook: a one-line result or a contrarian statement.
  - Rhythm: whitespace, short lines, lists.
  - Beats: hook → context → numbered steps or framework → summary → soft CTA.
  - Style described as framework-focused, digestible bullets ([contentin](https://contentin.io/blog/the-best-linkedin-posts-35-high-performing-posts-templates-from-7-content-masters/)). His "content matrix" was not verified in sources.
  - Devices: before/after, "here's how".
  - Proof: own metrics.
  - CTA: newsletter.
  - Length: 150–250 words.
- **Template:**
  1. [Result] in [time] without [common pain].
  2. Here's the system:
  3. 1/ [Step] 2/ [Step] 3/ [Step]
  4. The key: [insight].
  5. Most people skip [step] because [reason].
  6. I break this down weekly in [newsletter].
- **Fit:** TA, KQ (LinkedIn). Middle of funnel.
- **SG health:** N/A unless clinic. If so, no patient-count bragging.

### 13. Codie Sanchez-style contrarian business
- **DNA:**
  - Hook: "Everyone's chasing [sexy thing]. The money's in [boring thing]."
  - Rhythm: brisk, street-smart, specific numbers.
  - Beats: contrarian claim → example business economics → how to evaluate → risk caveat.
  - Devices: "boring businesses", deal math, myth inversion.
  - Proof: deal examples.
  - CTA: newsletter or community.
  - Length: 45–75 s.
- **Template:**
  1. Everyone wants [trendy thing]. I'd rather own [unsexy thing].
  2. Here's why: [revenue/margin example].
  3. Nobody competes because [reason].
  4. How to check one: [3 criteria].
  5. The risk: [honest caveat].
  6. Comment "[keyword]" and I'll send the checklist.
- **Fit:** TA, KQ (business owner audience). Top and middle of funnel.
- **SG health:** Keep away from clinic pricing claims.

### 14. Dan Koe-style philosophical one-person business
- **DNA:**
  - Hook: an abstract-provocative line ("Your mind is your product").
  - Rhythm: long reflective sentences mixed with aphorisms.
  - Beats: philosophical premise → critique of the default path → reframe (self-education, creativity, leverage) → practical creator system.
  - Devices: aphorisms, essays, minimal aesthetic visuals.
  - Proof: reasoning plus own model.
  - CTA: newsletter or essay.
  - Length: 60 s or long essay.
- **Template:**
  1. [Abstract thesis about work/identity].
  2. Most people [default path] because [conditioning].
  3. But [reframe].
  4. In practice: [system: learn → create → share].
  5. [Aphorism].
  6. Full essay in [newsletter].
- **Fit:** KQ, TA. Top of funnel.
- **SG health:** N/A.

### 15. Chris Williamson-style intellectual curiosity
- **DNA:**
  - Hook: "Here's a fascinating idea from [researcher/book]…"
  - Rhythm: articulate, quote-rich, wry.
  - Beats: surprising finding → explanation → implication for modern life → personal take.
  - Devices: named studies and thinkers, "the ultimate irony is…".
  - Proof: citations.
  - CTA: full episode.
  - Length: 45–90 s clips.
- **Template:**
  1. One of the most interesting ideas I've heard: [idea], from [source].
  2. The finding: [result].
  3. Why it happens: [mechanism].
  4. What it means for you: [implication].
  5. The twist: [irony/counterpoint].
  6. Full breakdown in [episode].
- **Fit:** KQ podcast, TA. Top of funnel.
- **SG health:** Cite primary sources.

### 16. Huberman-style protocol science
- **DNA:**
  - Hook: "A zero-cost protocol to [outcome]."
  - Rhythm: precise mechanism language.
  - Beats: mechanism (neurobiology) → protocol with dose, timing and duration → caveats → tools.
  - Devices: named studies, specific numbers.
  - Proof: studies.
  - CTA: full episode.
- **Evidence caveat:** Critics say confidence exceeds evidence, with some protocols resting on limited or animal data and supplement promotion ([Wikipedia](https://en.wikipedia.org/wiki/Andrew_Huberman), [Jarry quote via Rethinking Wellness](https://rethinkingwellness.substack.com/p/andrew-huberman-and-the-problem-with)). Our version must grade evidence: "strong / mixed / early".
- **Template:**
  1. A simple protocol for [outcome].
  2. Why it works: [mechanism, plain language].
  3. Protocol: [what], [when], [how long].
  4. Evidence level: [strong/mixed/early] ([source]).
  5. Who should skip it: [contraindications].
  6. Educational only, not individual medical advice.
- **Fit:** PS/H360, PP, PF. Middle of funnel (saves).
- **SG health:** No supplement claims beyond approved wording (PP: VN pack). No dosing advice that implies diagnosis.

### 17. Iman Gadzhi-style aspirational
- **DNA:**
  - Hook: a lifestyle visual plus "At [age] I [result]; here's what I'd do starting from zero."
  - Rhythm: cinematic B-roll and confident VO.
  - Beats: aspiration → origin struggle → the skill or vehicle → steps → "you can too".
  - Devices: luxury contrast, "if I were starting over".
  - Proof: lifestyle and results.
  - CTA: course or program.
- **Caution:** Aspirational income claims attract scrutiny. Keep results real and typical.
- **Template:**
  1. If I lost everything and started over at [age], I'd do this.
  2. [Origin struggle beat].
  3. The vehicle: [skill/business].
  4. Steps: [1], [2], [3].
  5. What it cost me: [honest trade-off].
  6. [Soft CTA to resource].
- **Fit:** KQ, TA (agency-building audience). Top of funnel.
- **SG health:** Never use for clinics. No income guarantees anywhere.

### 18. Jay Shetty-style wisdom stories (attribution caution)
- **DNA:**
  - Hook: "There's an old story about…" or a quote.
  - Rhythm: soothing, poetic.
  - Beats: parable → turn → wisdom line → application.
  - Devices: quotes, metaphors, spoken-word cadence.
  - Proof: tradition and authority.
  - CTA: share.
- **Caution:** Guardian reporting (John McDermott, Feb 2024) alleged plagiarism and exaggerated origin claims. In 2019 he removed 100+ posts after a YouTuber showed copied content with attribution cropped ([Plagiarism Today](https://www.plagiarismtoday.com/2024/03/05/jay-shetty-and-boomerang-plagiarism-allegations/), [Business Today](https://www.businesstoday.in/amp/latest/world/story/life-coach-jay-shetty-accused-of-lying-about-his-past-plagiarising-instagram-posts-report-420087-2024-03-05)).
- **House rule:** Every parable or quote gets an origin check and on-screen attribution, or is marked "adapted from [tradition]" or "original parable". Never present a borrowed story as personal.
- **Template:**
  1. There's a story [attributed to / adapted from: source].
  2. [Setup of the parable].
  3. [Turn].
  4. The lesson: [wisdom line].
  5. In your life, this looks like [application].
  6. Share this with someone who needs it.
- **Fit:** KQ, PF. Top of funnel.
- **SG health:** Fine if no clinic claim.

### 19. Lara Acosta-style LinkedIn storytelling
- **DNA:**
  - SLAY: Story → Lesson → Actionable advice → You/question ([Creator Science](https://podcast.creatorscience.com/lara-acosta/), [Cool Story](https://cool-story.beehiiv.com/p/lara-acosta-slay-framework)). It is a variation on the older SLAP copy formula.
  - Hook: a vulnerable or result-led first line, scroll-stopping.
  - Rhythm: short lines, whitespace.
  - Proof: personal story.
  - CTA: question to drive comments.
  - Length: 150–250 words.
- **Template:**
  1. [Vulnerable or surprising first line].
  2. Story: [what happened, concrete].
  3. Lesson: [one insight].
  4. Action: [one thing to do].
  5. [Reinforcing line].
  6. You: [question to readers]?
- **Fit:** KQ, TA (LinkedIn). Top and middle of funnel.
- **SG health:** No patient stories as proof for clinics.

### 20. Jerome Polin (Nihongo Mantappu, Indonesia): playful edu-challenge
- **DNA:**
  - Math or Japan content made fun via battles and quizzes. Life-in-Japan culture-bridge vlogs. He worried that teaching only Japanese would narrow his audience ([Waseda Weekly](https://www.waseda.jp/inst/weekly/news-en/2021/10/27/91833/)). ~10.6M subs, ~30 min avg videos per [vidIQ](https://vidiq.com/youtube-stats/channel/UC1Gmqqs_Myzl2KHIeqfUC9A) (Jul 2025 snapshot).
  - Hook: a challenge or quiz question.
  - Rhythm: energetic, friends on camera, bilingual jokes.
  - Beats: challenge → attempts with friends → reveal or explanation → cultural fun fact.
  - Proof: live solving.
  - CTA: "try it, comment your answer".
- **Template:**
  1. Can you solve this in [N] seconds? [puzzle/question]
  2. [Friend/guest] tries: [wrong answer, funny].
  3. Hint: [clue].
  4. Answer + why: [explanation].
  5. Bonus fact: [culture/science nugget].
  6. Comment your time below.
- **Fit:** PS (posture or anatomy quiz), PP (VN market quiz formats), TA. Top of funnel, localised for SEA.
- **SG health:** No diagnosis-by-quiz. Add "see a professional for assessment".

### 21. Khairul Aming (Malaysia): warm, consistent cooking series
- **DNA:**
  - Long-running consistent series, e.g. "30 Hari 30 Resipi", with a cheeky persona. Cited for a distinctive way of presenting cooking videos and nine years of relevance ([Kosmo](https://www.kosmo.com.my/?p=712810), [NST 2026](https://www.nst.com.my/amp/lifestyle/groove/2026/09/1537620/showbiz-khairul-aming-sparks-online-proposal-storm-after-sharing)). His success also spawned copycat accusations ([BH](https://www.bharian.com.my/amp/berita/nasional/2026/02/1514941/bhplus)), which shows that originality matters.
  - Hook: the finished dish or a humorous line.
  - Rhythm: brisk ASMR cooking with casual BM/English banter.
  - Beats: tease → ingredients → quick steps → taste reaction → series callback.
  - Proof: visible process.
  - CTA: "save for later / Day X tomorrow".
- **Template:**
  1. Day [X] of [series]: [dish/thing].
  2. You need: [3–5 items].
  3. Step: [quick step], [quick step].
  4. [Cheeky aside].
  5. [Taste/result moment].
  6. Save this. Tomorrow: [next].
- **Fit:** PP (a "30 days 30 protein recipes" series is ideal), PF (meal prep). Top of funnel and retention.
- **SG health:** PP health claims must follow VN rules. No "cures" or "burns fat".

### 22. Night Owl Cinematics (Singapore): relatable local sketch comedy
- **DNA:**
  - Breakthrough with "Shit Singaporean Girlfriends Say"-style observational skits. Later pivoted to "content-driven, not influencer-led". As of 2026 the main channel's videos are set to private ([Wikipedia](https://en.wikipedia.org/wiki/Night_Owl_Cinematics), [Mothership](https://mothership.sg/2022/01/night-owl-cinematics-new-direction//amp)). Reference the format, not specific videos.
  - Hook: an instantly recognisable SG situation.
  - Rhythm: rapid Singlish banter with escalating exaggeration.
  - Beats: setup → stereotype riff list → escalation → twist or tag.
  - Devices: Singlish, local references (MRT, hawker, NS).
  - CTA: "tag your [friend]".
- **Template:**
  1. Things every Singaporean [persona] says at [place]:
  2. "[line 1]"
  3. "[line 2]" (escalate)
  4. "[line 3]" (absurd)
  5. Twist: [reversal/tag].
  6. Tag the [friend] who does this.
- **Fit:** PS ("things physios hear every day"), PF, KQ. Top of funnel, SG localisation pack.
- **SG health:** The skit must not mock patients or show patient testimonials. Label it as a dramatisation.

---

## Gaps
- I could not open the Higgsfield live preset catalog or the Magnific Seedance guide (HTTP 403).
- No primary sources for Justin Welsh's content matrix or the 2024 New York Magazine Huberman piece.
- Physiotherapy-specific SG advertising rules (AHPC) were not found online. Confirm per entity, as `compliance-sg.md` already notes.
- I used no YouTube transcript credits.