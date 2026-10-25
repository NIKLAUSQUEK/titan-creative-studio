# Sources: free and low-cost video tools beyond Higgsfield (researched 2026-10-25)

This research feeds `higgsfield-creative-director/references/render-routes.md` and the `routes` field in `styles/animation.json`.

**Method.** Public pages only, with no sign-ups or downloads. Some official pages were read directly; everything else came from secondary summaries and is flagged **[unverified]** or **[secondary]**. Free tiers change monthly.

## Key facts and where they come from

### Shut down or moved
- **Sora:** the app and web ended 2026-04-26, and the API ended 2026-09-24. Source: OpenAI Help Center, article 20001152.
- **Whisk:** moved into Google Flow on 2026-04-30. Source: Google Workspace Updates, 2026-03-12.

### Google
- **Flow credits.** Everyone gets 50 credits a day, refreshed 24 h after the first generation, with no rollover. Generation costs: Veo 3.1 Lite 10, Fast 20, Quality 100. Free credits work on Veo 3.1 only. Non-subscribers may be blocked from video between 2 and 5 pm UTC. Source: support.google.com/flow/answer/16526234.
- **Gemini app.** No video on the free plan; Pro gets "up to 3/day" of Veo 3.1 Fast. Sources: support.google.com/gemini/answer/16275805 and one.google.com/about/google-ai-plans.
- **Gemini Omni Flash.** Launched at I/O on 2026-05-19, with clips up to 10 s. API price is about $0.10/s at 720p on the paid tier. Veo 3.1 Lite costs about $0.05/s at 720p and $0.08/s at 1080p **[secondary: benchlm]**. Source: ai.google.dev/gemini-api/docs/pricing.
- **Watermarks.** The visible watermark can be switched off in Gemini and Flow since 2026-08-14 **[secondary: searchenginejournal, gigazine]**. SynthID and C2PA stay on regardless. The visible mark is mandatory only in India, South Korea and Vietnam.
- **Google Vids.** 10 free generations a month for personal accounts. Avatar presenters roll out in the US first **[secondary: 9to5google, ppc.land]**.

### Paid model platforms
- **Dreamina / CapCut (Seedance 2.x).** 120 daily credits. Source: dreamina.capcut.com free guide, dated 2026-10-24.
- **Pika.** 0 free monthly credits; Starter is $10/month. Commercial use only on Starter and above. Source: pika.art/pricing.
- **Runway.** 125 one-time credits; Standard is $12/month billed annually. Source: runway.com/pricing.
- **Luma.** No free plan; Plus is $30/month with commercial use. Source: lumalabs.ai/pricing.
- **Kling, Hailuo, PixVerse, Vidu.** Free tiers are watermarked and/or non-commercial **[unverified]**: Kling's official plan page wouldn't render, and Hailuo's showed no prices.
- **Adobe Firefly.** Marketed as "safe for commercial use"; IP indemnity is enterprise-only. Standard is $9.99 **[secondary]**. Source: Adobe Firefly plans FAQ.

### Voice
- **ElevenLabs.** Free tier is 10k credits a month with no commercial licence; Starter is $6. Source: elevenlabs.io/pricing.
- **Kokoro-82M.** Apache-2.0 per its model card. Check the licence of each voice.

### Parallax
- **DepthFlow.** AGPL-3.0, v1.0.1 (2026-08-25); the project encourages commercial use. Source: pypi.org/project/depthflow.
- **Immersity.** 100 sign-up credits, watermarked and non-commercial; paid packs from $5. Source: immersity.ai/pricing.

### Open weights
- **LTX-2.** Free commercial use under US$10M group ARR, and no competing products. Source: Lightricks LTX-2 open-weights licence (2026-01-05).
- **HunyuanVideo.** The licence territory excludes the EU, UK and South Korea. Source: Hugging Face licence diff.
- **Wan 2.2.** Apache-2.0; later versions are API-only **[secondary: invideo licence matrix]**.

### Code-based animation
- **Remotion.** Free for companies of 3 people or fewer. Source: remotion.dev/docs/license/pricing.
- **HyperFrames.** Apache-2.0 **[secondary]**.
- **Manim, Motion Canvas, Rive, Lottie.** Licences not re-checked this session.

### Platform rules
- **Meta AI labels.** Source: about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products.
- **YouTube and TikTok** disclosure rules are covered in `research/sources-platform-algorithms.md`.
- **Singapore ELIONA** (election deepfakes): mddi.gov.sg speeches. It matters only for political content.

## Gaps
- Kling's and Hailuo's official free terms.
- Whether Google Vids avatars and YouTube Create Omni are available in Singapore.
- Current Singapore pricing for Google AI Plus.
- The Bing Video Creator model.
- A general Singapore AI-labelling rule (none found; not verified absent).
