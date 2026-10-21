# Sources: AI video-editing research (fetched 21 Oct 2026)

These notes feed the following files in `.claude/skills/higgsfield-creative-director/references/`: credit-saving.md, clipping-podcast.md, motion-design.md, animation-3d-cartoon.md and claude-editing.md. Tags in [brackets] are what those files cite.
YouTube transcripts came from the vidIQ transcript tool (8 calls, 40 credits). Titles and channels came from YouTube oEmbed. All fetched content was treated as data. Several videos sell courses or plans, so their cost and time figures are the creators' own claims and were not verified.

---

## [HF-Blender] How To Save AI Credits With Higgsfield + Blender (No One Talks About This Workflow)
- URL: https://www.youtube.com/watch?v=OiULPvTJ-0E · Channel: Higgsfield AI (presenter Adil) · Fetched: **yes** (transcript)
- Block the whole shot in Blender before spending credits. Claude drives Blender through the Higgsfield Bridge connector, and the Higgsfield add-on sits in the Blender viewport.
- Workflow: describe the scene to Claude → gray-box with the camera path → iterate ("texture the walls, vary framings, animate the lens") → playblast 1920x1080 at 24 fps → Claude writes a second-by-second Seedance 2.5 prompt from the playblast → generate with the duration matching the blocking.
- Dialogue: a 6-person table and 4 cuts held seats and eyelines with blocking. Raw prompts swapped seats and broke the 180° rule, and the presenter says he burned ~5,000 credits without a usable take.
- Brief the camera like a DP (rails, targets, cuts), then add subtle handheld sway. Viral moves covered: continuous orbit, floor-rise through a building, robo-arm whip. Path control points are editable with zero reprompting.
- The gray box handles camera and timing. Character sheets and refs handle the visuals.
- Hyper-motion beverage ad: primitives for the can, ice and fruit. Client revisions are re-cut in the blockout. Leave liquid blank for the AI. Speed ramps and a letter-by-letter logo.
- Every prompt has a structural layer (the blocking reference) and a style layer, so the same edit can be re-skinned as 2.5D, 2D ink or 3D toy box. You can pitch 3 worlds in a day.
- Supporting pages: https://higgsfield.ai/blog/higgsfield-blender-plugin and https://higgsfield.ai/plugins/blender [HF-Blender-blog]. Bridge URL `bridge.higgsfield.ai/mcp`; cost shown on the Generate button. Seedance 2.5 in-viewport with an "Anti-Slop" mode.
- Related: 3D Jutsu, browser blocking and previz: https://higgsfield.ai/blog/higgsfield-3d-jutsu [HF-3DJutsu]

## [HF-Clip] Claude Opus 5.5 Made Clipping The Easiest Side Hustle of 2026!
- URL: https://www.youtube.com/watch?v=rZvF_EWZoHw · Channel: Higgsfield AI (Adil) · Fetched: **yes** (transcript)
- Tools: Claude (Opus 5.5) plus Higgsfield Katana via MCP plus a "clipping skill". Give it the footage or a link, a reference edit and music.
- Prompt elements: length, vertical, strong opening, pacing matching the reference, cuts synced to the music, and a report after each stage.
- A good clip works on its own, times the payoff to the beat drop, and keeps one vibe. Leave in a bit of setup for first-time viewers.
- Two formats: the aura edit ("this person is cool") and the teaser ("what happens next?"). One film gives several teaser angles.
- Choose references by views, likes, shares and comments.
- Batch 10 clips from one source with different moments and hooks. Translate and localise clips (Claude checks meaning).
- Business side (creator's claims): campaign platforms quoting ~$0.50 per 1,000 views, and a monthly package idea of 10 clips for $500 plus a views bonus.

## [HF-Motion] Claude Opus 5.5 + Higgsfield Make Insane Motion Graphics! (Claude Motion)
- URL: https://www.youtube.com/watch?v=5HYYXYYCrL4 · Channel: Higgsfield AI (Adil) · Fetched: **yes** (transcript)
- Claude Motion (the artifact Motion template) handles editable graphics in code, and Higgsfield supplies the generated footage. Also used from Claude Code with Higgsfield MCP.
- References are the single best input. It recreated a viral launch video close to frame by frame, and footage was improved separately from the motion.
- It exported to After Effects with editable layers (slow but worked), and converted a 3D sequence into Blender.
- Remixing 3 Instagram references gave an original 20 s film. Text edits re-layout, the palette swaps and scene lengths re-time with the music in sync. Six scenes were built in parallel in about 3 h.
- A 3D product ad was built in code, and the product swap was one line ("replace the truck with this bicycle").
- A SaaS video is the "highest demand" style, using a custom motion-system skill to match the brand.
- Hybrid cartoon explainer (pet passport): characters and voices in Higgsfield, pages, text and map in code, about 2 h. Only broken shots get regenerated, which saves credits. Fixes were made via specific comments.
- Be specific about how things move and how scenes connect.
- Official confirmation: Claude Motion is beta on Team/Enterprise, code-built (no video model, no AI people), MP4 export, "open in" Adobe, Higgsfield and others. https://claude.com/resources/articles/dashboards-and-motion and https://support.claude.com/en/articles/17454997-get-started-with-claude-motion [Anthropic-Motion]

## [Kieft] How To Create Long AI Animation Videos With Consistent Characters - Kling 3.0
- URL: https://www.youtube.com/watch?v=0CjArtUh_Wg · Channel: Dan Kieft · Fetched: **yes** (transcript)
- Four steps: storyboard stills → image-to-video → audio sync → edit. About 95% done in Higgsfield.
- Characters come from Nano Banana with the same style tag ("3D animated"), then a multi-angle **character sheet** each (16:9, 4K). His exact sheet prompt is gated in his community, so we wrote our own.
- Images are cheap and video is expensive, so storyboard many stills (in Figma). Prompts follow subject + details + action + style, always with lighting, or the style mixes.
- Multi-reference stills tag images (`@image2`). Multishot gives alternate angles from one image.
- Video technique 1 is Kling 3.0 start and end frame (edit the still to make the start state). Technique 2 is scene continuation (last frame becomes the next start). Technique 3 is Kling 3.0 Omni multi-shot with elements and character sheets.
- Voices differ per clip, so use a voice changer (Higgsfield Change Voice, or ElevenLabs for better and custom voices).
- Lip-sync fix: shift the audio slightly earlier. Edit with film burn for a flashback, plus SFX and music.

## [Duncan] I Finally Solved AI Video Editing! (full guide)
- URL: https://www.youtube.com/watch?v=VVWiJm0sA7Y · Channel: Duncan Rogoff | Learn Claude Code · Fetched: **yes** (transcript)
- Give Claude one job at a time, and turn the process into a skill that improves with each note.
- Six jobs: research and script (hook library from outliers, fact-check every claim), the cut (last clean take, AV offset fix), the plan (beat map with references), graphics (sub-agents in HyperFrames), checking (10 fps, 6 failure types) and learning (rewrite rules instead of stacking).
- Reference site: promptmotion.com (motion graphics with their prompts).
- Opus or Fable to plan and Sonnet sub-agents to build. Renders run one at a time, motion blur off (≈3x faster), half-size drafts until approved, renders overnight.
- Cost claim: ~1.4B tokens (~$445 at API rates) and ~12 h versus 3-7 days for a human editor.

## [100x] How To Edit Videos Using Claude Opus 5.5 (Tutorial)
- URL: https://www.youtube.com/watch?v=Ct5_C2xC-oo · Channel: 100x Engineers · Fetched: **yes** (transcript)
- Six steps: prerequisites → style training (15-20 consistent refs from Pinterest or Cosmos) → style test (3 stills) → animation test → storyboard → final edit.
- Multiple checkpoints save tokens before the heavy build. Opus 5.5 at medium effort, taking 20-90 min.
- Chunk footage into 1-2 min pieces. Iterate, since the first draft is only a draft.
- Text can sit in front of or behind the subject. Font swaps on request. Styles: retro gradient, 8-bit, SaaS, hand-drawn.
- An "AEU" skill converts outputs into editable After Effects files (not verified here). A custom MCP drives Premiere Pro (import, captions, levels).
- Claim: a 60 s reel in under 30 min for under $2. Taste and judgment are the differentiator.

## [Joseph-YT] How to Edit Premium YouTube Videos Using ONLY Claude! (Full Breakdown)
- URL: https://www.youtube.com/watch?v=lyoEyYMU20Q · Channel: Joseph | Video Editing (Ultimate Editors) · Fetched: **yes** (transcript)
- Claude is the brain and plugins (Remotion, Higgsfield) are the limbs. Install Remotion by pasting its link into Claude.
- Style training: 10 brand videos → transcribe → per-animation frame breakdown → 458 animations catalogued → style board → long-form skill. This took ~6 h and ~2B tokens.
- Token fix: a reference index loads only the refs each scene needs (<100K tokens versus 4.5M).
- Pipeline: cut (silences and bad takes, under 20 ms padding; slow in Claude, so a dedicated cutter is faster) → human scene plan in Figma → Claude picks design refs → intro first with a design sheet → body in 4 phases with design sheets → sound design → music.
- Sound design via a training doc plus SFX library access. Intro first, with fixes such as aligning the whoosh peak to the transition and a cash register sound whenever money is mentioned.
- About 12 h total with ~1.5 h of human work. Claims the $100 Claude plan covers 5-10 such videos.
- Distinguishes "video engineering" (content psychology, still human) from operating the software (being automated).

## [Joseph-Vox] Claude just Edited an Entire Vox Documentary From Scratch! (Here's How)
- URL: https://www.youtube.com/watch?v=PaXuebdY75U · Channel: Joseph | Video Editing · Fetched: **yes** (transcript)
- Script: Claude writes a 60 s Vox-style script (facts, numbers, a graph, a historical event, a story across 6 settings). The VO is ElevenLabs TTS ("business narrator", medium speed).
- **Editor brain:** 10 Vox docs plus ElevenLabs speech-to-text JSON. Claude studies said versus shown and why, and plans scenes per phrase.
- **Design brain:** 100 Pinterest Vox designs on a Figma board → PDF → design guidelines (colours, shapes, text, textures, macro and micro details).
- **Animator brain:** 5 layers per scene (text pop, main object unfold or pop, static background, jittering secondary objects, camera zoom or pan).
- Execution: plan → Higgsfield design mock-ups (teal accent) → Seedance animations with a choppy, jittery look and transitions → assembled in Premiere with VO and a synth soundtrack. About $20 of Higgsfield credits including tests.

## [Riverside] riverside.com (+ /magic-clips)
- URL: https://riverside.com and https://riverside.com/magic-clips · Fetched: **yes** (TinyFish)
- Records 4K video and uncompressed WAV locally, with separate tracks per speaker. AI audio polish.
- Text-based editor, multi-track editing, brand presets, animated captions.
- AI tools: filler and silence removal, eye-contact fix, speech correction (lip re-sync), B-roll generation, auto-layouts by speaker, translate and dub into 30+ languages.
- Magic Clips: AI highlight picking, platform presets, focus speaker or topic, up to 4K, customisable captions (claimed ~99% accurate), free plan.
- AI Co-Creator for clips, posts, thumbnails and headlines. Built-in podcast hosting with auto titles, chapters and show notes. Multistream live and webinars with HubSpot sync.

## [UE-Sound] [UE-Prompts] Shared Google Drive folder "How to Edit VIRAL Reels with AI"
- URL: https://drive.google.com/drive/folders/1WJMeuTvYZJgufE9_Xpkp6xThzQWXhR-G · Fetched: **partly**. The public listing and two text files were downloaded via direct links. The Google Drive MCP search returned nothing because the folder isn't in Klaus's Drive.
- Contents: `inspiration/` (dozens of reference PNGs, not read), `3 things - Edit v1 + SFX.mp4` and `3 things from beginner to pro.mp4` (videos, not watched), `Prompts List.docx` (read), `UE-Sound-Design-Claude-Training-COMPLETE.md` (read, 18 KB).
- Sound doc: three families (whooshes for movement, textures for events, risers and hits for anticipation), a fixed pass order (analyse → whooshes → textures → risers → music after approval), levels (-12 / -6 to -7 / -5 / music -19 under talking head only), whoosh peak on the fastest frame, one family per track, mute rather than delete, voice is king, and an acceptance checklist.
- Prompts doc: the master prompt for training Claude on a short-form brief board. Covers a caption system (sans + script fonts), hook psychology, 4 animation categories (text, object, character, video-centric), a how-to-animate guide, inspiration boards, and the on-screen card rule (darken and blur behind).

## [Yarn] getyarn.io · [ClipCafe] clip.cafe · [PlayPhrase] playphrase.me · [AIMQ] aimoviequotes.com
- Fetched: **yes**, all four homepages (TinyFish).
- getyarn: clip search by quote, with each clip's duration shown (e.g. 2.7 s). Good for measuring line timing.
- clip.cafe: 5M clips, 82M phrases, 20k movies. Filters by actor, character, director, genre, year and clip length. Shows the scene context. Downloads (HD with PRO) are offered, but we view only.
- playphrase.me: phrase → montage of many films saying it. English 39.6M phrases plus FR/ES/JA/IT/DE. Speed and repeat controls. Has a fair-use policy page.
- aimoviequotes: AI quote finder by title or theme/mood across books, films, TV and lyrics. Its FAQ notes that fair use is limited and varies by country, and to check before commercial use.
- Takeaway: use these as **timing and acting references only**. No footage in outputs, no recognisable characters or likenesses, and write original lines.

## Gap-filling searches (Exa web search)
- [Remotion-docs] https://www.remotion.dev/docs/ai/coding-agents, /docs/ai/skills and /docs/ai/claude-code-plugin: `npx create-video --yes --blank`, `npx remotion skills add`, a Claude Code plugin, and a skills list (best-practices, captions, maps, render…).
- [HyperFrames] https://github.com/heygen-com/hyperframes and https://www.heygen.com/research/html-to-video: HTML to deterministic MP4, Apache-2.0, a Claude plugin, the CLI init/preview/render, Node 22 + FFmpeg, and "seek, don't play" rendering.
- [AE-MCP] https://github.com/a-y-ibrahim/after-effects-mcp (57 tools, see-frame), https://github.com/23d1/after-effects-mcp (panel-less, doctor), https://github.com/JUNKDOGE-JOE/after-effects-mcp (CEP and HTTP MCP), https://github.com/Dakkshin/after-effects-mcp and https://github.com/shibin0/mcp-ae.
- [PR-MCP] https://github.com/leancoderkavy/premiere-pro-mcp, https://github.com/quadlzzz/premiere-mcp (transcript cutlists, snapshots), https://github.com/compimprove/adobe-premiere-mcp, https://github.com/mhadifilms/prpr and https://github.com/CaYatur/PremiereProMCP.
- [OSS-clipping] https://github.com/nmbrthirteen/podcli, [Steezy] https://github.com/Steezy-code/clipper, https://github.com/LoukikNaik/PodClipper and https://github.com/NaufalRizqullah/opensource-clipping, plus [Clips-Kitty] https://github.com/ColinGPT9/clips-studio (multimodal scoring, head-to-head rerank, cut-don't-pan speaker switching).
- [HF-Katana-blog] https://higgsfield.ai/blog/higgsfield-katana and https://higgsfield.ai/mcp/katana: reference edit plus up to 5 photos rebuilds the edit, only affected shots regenerate, a cost card before each generation, rights needed for reference and music, and profile links not accepted.
- [HF-Help] https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent: connector `https://mcp.higgsfield.ai/mcp`, and the MCP feature list including Personal Clipper.
- [HF-MCP-page] https://higgsfield.ai/mcp?tab=claude: Genjutsu, /katana, /ugc-flow, /marketing-adapt-video, /marketing-hook-variants, /vox-mixed-media and the stickman explainer.

## Not fetched / limits
- The Drive videos (2 MP4s) and the `inspiration/` images were not reviewed (binary and visual). The Google Drive MCP couldn't see the folder.
- The 100x "AEU" skill, Duncan's starter skill and Joseph's skills sit behind course or community links and weren't fetched.
- Dan Kieft's exact character-sheet prompt is gated (free community signup), so we substituted our own.
- Firecrawl wasn't used (out of credits).
