# Render routes: free → cheap → premium (Higgsfield is one option, not the only one)

Every shot gets the **cheapest route that meets the brief**. Higgsfield (Seedance 2.5, Kling, Soul ID, explainer presets) stays the premium route, used when a shot needs it. Free and cheap routes are first-class options.

Research date: 2026-10-25. Free tiers change monthly, so check each plan page on the day you use it. Sources and verification flags are in `research/sources-free-video-tools.md`.

## Rules that don't change
- **Cost gate applies to every paid route** (Veo API, Kling, Dreamina, Runway, Luma, Higgsfield): approved spec plus a cost quote first. Free routes skip the quote, but the spec and Gate 4 asset approval still apply.
- **Commercial rights come first:**
  - Client and brand ads only use routes whose terms allow commercial use **at the tier used**.
  - Content made on a free, non-commercial plan does not become licensed after you upgrade. Generate client work while on the paid plan.
- **Never crop or erase a watermark.** It doesn't change the licence.
- **AI labels:**
  - Google outputs always carry SynthID + C2PA, even with the visible watermark toggled off. So do OpenAI-era and many others.
  - TikTok, YouTube and Meta read these.
  - Label proactively at `/publish`. Health topics (Physio Spot, heal360) get prominent labels on YouTube.
- **Likeness:** real staff on camera beat avatars. No real-person deepfakes. Fictional characters only (character-design.md).
- **Dead routes:**
  - Sora: app ended 2026-04-26, API 2026-09-24.
  - Whisk: moved into Flow 2026-04-30.
  - Bing Video Creator: built on Sora, non-commercial, status unclear.
  - Grok Imagine: free tier reportedly removed.

## Route table (the tools worth using)

| Tool | Use for | Free | Cheap | Commercial | Notes |
|---|---|---|---|---|---|
| **Cards engine** (`editor.py cards` / boards) | kinetic type, stat/chart/step boards, carousels, LinkedIn PDFs | unlimited, local | — | yes (own output) | our default for anything text- or data-led |
| **HyperFrames** (HTML→MP4) | premium motion graphics, kinetic type, data-viz | Apache-2.0 | — | yes | already in the stack |
| **Remotion** | React video templates | free for companies of **≤3 people** | $25/seat/mo above that | yes within licence | check the headcount rule |
| **Manim CE / Motion Canvas** | diagrams, whiteboard-style builds, maths/data | free (MIT) | — | yes | code-drawn, so text is perfect |
| **DepthFlow** | 2.5D parallax on stills and real photos | free, local, no watermark | — | yes for rendered videos (AGPL code) | best free "documentary" motion |
| **Wan 2.2** (ComfyUI, local) | image→video motion on non-hero shots: anime, 3D, clay, B-roll | free, unlimited | GPU time | **Apache-2.0** | newer Wan versions are API-only |
| **LTX-2** (local) | fast drafts with audio, motion tests | free | — | free under **US$10M group ARR**; no competing products | |
| **HunyuanVideo 1.5** (local) | high-quality local text→video | free | — | not licensed in **EU, UK, South Korea** | avoid for UK clients |
| **Google Flow** (Veo 3.1 + Omni Flash) | photoreal/stylised hero clips with native audio | **50 credits/day for everyone**: Veo 3.1 Lite = 10, Fast = 20, Quality = 100. So 5 Lite or 2 Fast a day, no rollover. Free users may be blocked 10 pm–1 am SGT | AI Plus 200 credits/mo; AI Pro 1,000/mo | consumer terms claim no ownership but give no explicit commercial licence; IP indemnity is enterprise Vertex only | visible watermark can be toggled off in SG; SynthID stays |
| **Gemini app** | quick 8–10 s clips | no video on the free plan | Pro "up to 3/day" Veo 3.1 Fast | as Flow | Nano Banana stills are free here |
| **Google Vids** | templated explainers, generic avatar presenters | 10 generations/mo (personal) | Workspace / AI plans | as Google terms | avatars are US-first; SG unverified |
| **Veo / Omni API** (Gemini API) | metered hero shots under paid terms | — | Veo 3.1 Lite ~$0.05/s at 720p ($0.08 at 1080p); Fast $0.10–0.12/s; Omni Flash ~$0.10/s | paid API terms | clearest Google commercial cover |
| **Dreamina / CapCut** (Seedance 2.x) | same model family as our default, cheaper | 120 daily credits (Aug 2026), may watermark | paid tiers (prices not public; promos) | "subject to plan/model conditions" | closest substitute for the Higgsfield Seedance route |
| **Kling** | image→video motion quality, lip-sync | promo credits only (disputed), watermark | Standard ~$7–10/mo | **paid only** | |
| **Runway** | editing tools, restyle, references | 125 credits one-time | Standard $12/mo (annual) | not stated, so use paid | |
| **Adobe Firefly** (video) | commercially safe stock-style B-roll (clinic, product) | daily free gens (video unclear) | Standard $9.99, ~20 five-second clips/mo | marketed "safe for commercial use"; indemnity enterprise-only | good for health brands' neutral B-roll |
| **Luma** (Ray3) | cinematic camera moves, keyframes | no free plan now | Plus $30/mo, commercial | paid only | |
| **Pika / Hailuo / PixVerse / Vidu** | effects, anime, cheap tests | watermark and/or non-commercial | ~$8–10/mo | paid only | test-only for us |
| **Kokoro-82M** TTS | draft voiceovers | free, local (Apache-2.0) | — | check each voice's licence | finals: real voice or paid ElevenLabs |
| **ElevenLabs** | final VO | 10k credits/mo, **non-commercial** | Starter $6/mo | paid only | |
| **Higgsfield** | premium: Seedance 2.5 omni_reference, Kling motion control, Soul ID, explainer presets, Genjutsu | free plan: 0 credits, no commercial rights | from ~$19/mo | paid | studio default for performance-critical, character-consistent finals |

## Route per style (free / cheap / premium)
Each style's card in `styles/animation.json` carries the same three routes (`routes`).

| Style | Free | Cheap | Premium (Higgsfield) |
|---|---|---|---|
| Stickman / doodle | Rive/Manim/HyperFrames rigs or Nano Banana stills + editor Ken Burns + Kokoro VO | Flow Veo Lite on the stickman style key | explainer skill stickman preset |
| Whiteboard | Manim / HyperFrames stroke reveal of Nano Banana final frames | Google Vids templates | explainer custom whiteboard key |
| Flat vector explainer | Rive/Lottie + HyperFrames | Vids (10 free/mo) + Canva Pro | explainer flat preset (Omni) |
| Anime | Nano Banana stills → Wan 2.2 local | Dreamina Seedance / Kling Standard | Nano Banana key → Seedance/Kling |
| 3D cartoon | Gemini stills → Wan 2.2 local | Flow (50 credits/day) → AI Pro for 1080p | Nano Banana 2 → Seedance 2.5 |
| Claymation | stills + Wan 2.2, decimate to 12 fps in the editor | Flow Fast / Dreamina | as 3D |
| Paper collage | stills + DepthFlow layers + HyperFrames | Runway Standard | Nano Banana collage key → Kling, or `/vox-mixed-media` |
| Kinetic typography | **cards engine / HyperFrames** (free is best) | — | not needed |
| Data-viz | **cards engine / HyperFrames / Manim** (sourced stats only) | — | not needed |
| 2.5D parallax | **DepthFlow** | Immersity paid packs | Higgsfield camera-move presets |
| Isometric diorama | stills + DepthFlow push-in | Flow Fast / Luma Plus | Nano Banana diorama key → Seedance |
| Photoreal faceless doc | real footage/photos + DepthFlow + Kokoro | Flow Lite/Fast or Veo API Lite ($0.40–0.64 per 8 s) | Seedance 2.5 omni_reference → 1080p → 4K upscale |
| Talking head | **film real staff/Klaus** | Vids generic avatars (not for health brands) | Soul ID / AI Influencer, fictional characters only |
| UGC-style ads | real creator footage + editor | Dreamina Seedance / Kling for inserts | Marketing Studio / Seedance + Genjutsu |

## Free-first workflow (default unless Klaus asks for premium)
1. **Script and boards.** Run Gate 3. Text and data beats go straight to the cards engine or HyperFrames at zero AI cost.
2. **Stills first.**
   - Asset Bible frames come from real photos or Nano Banana (free in the Gemini app) / Flow images.
   - Lock style and characters at Gate 4 on stills, where redoing is cheap.
3. **Local motion pass, no credits:**
   - DepthFlow parallax and push-ins
   - Wan 2.2 / LTX-2 image→video for non-hero shots
   - Rive/Manim rigs
   - Kokoro draft VO
4. **Rough cut and QC.** Assemble in `editor.py`, run `qc_frames.py`, and get Klaus's sign-off on the draft.
5. **AI video only for hero shots:**
   - Free: Flow (5 Lite clips/day, off-peak).
   - Cheap: Veo API Lite or Dreamina.
   - Premium: Higgsfield Seedance 2.5 at 1080p → 4K, after draft approval. The cost gate applies.
6. **Finish.** Real voice or paid ElevenLabs. Add AI and paid labels at `/publish`.

Rule of thumb (unmeasured): about 80–90% of shots at zero credit cost. For each piece, state the route mix in the spec, e.g. `"render_routes": {"s1": "cards", "s2": "depthflow", "s3": "flow:veo-lite", "s4": "higgsfield:seedance-2.5"}`.

## Picking a route for one shot
1. **Is it text, numbers, a diagram or a chart?** → cards engine or HyperFrames. Never generate text in a video model.
2. **Is it a real person or place we can film or photograph?** → film it. Use DepthFlow for stills.
3. **Is it a non-hero motion beat?** → Wan 2.2 or LTX-2 locally, or a Flow Lite free credit.
4. **Is it a hero shot that needs performance, physics, a consistent character or 1080p+?** → Higgsfield Seedance 2.5 (Genjutsu for performance), or Veo API Quality when Klaus prefers Google. Quote either one first.
5. **Is it a client deliverable?** → confirm commercial terms for that route and tier.
