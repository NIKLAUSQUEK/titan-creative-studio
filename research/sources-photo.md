# Sources — photo effects & product VFX research (2026-10-21)
Feeds: `.claude/skills/higgsfield-creative-director/references/photo-effects.md` and `product-vfx.md`.
Fetch methods: TinyFish fetch_content (captions), Exa web_fetch (article), vidIQ watch_shortform_content (visual analysis + on-screen text). vidIQ: 10 submits, 3 failed and were refunded (URLs that had a `/<username>/reel/` path), 7 completed = **70 credits spent**. Firecrawl not used.
Pattern note: almost every creator gates the exact prompt behind "comment X for the prompt" DMs. Where the prompt wasn't shown on screen, the library's template is marked "recon" (rebuilt from the visible result + public prompt libraries).

## Supplied links
| # | Link | What it shows | Caption fetched | Visual watched | Key takeaways |
|---|---|---|---|---|---|
| 1 | youtube.com/shorts/4EV2HRZTPuY | Higgsfield Relight demo: "Bad lighting almost ruined this shot… Relight saved it" | title only | yes (vidIQ) | Relight UI: direction presets Top/Front/Right/Left/Back/Bottom or drag sphere; Soft vs Hard; Brightness %; colour hex. Hard + warm back/rim = cinematic; Soft = natural fill. |
| 2 | instagram.com/reel/DcqabXsiM3o (@declann, Higgsfield creator) | Overcast NYC footage → golden hour via Higgsfield Relight | yes | yes | Full recipe: preset Contre Jour → light behind/in front → orange #FFD800, brightness 100%, diffusion 10% → prompt (transcribed verbatim from screen, in photo-effects §1.1). Works on video. |
| 3 | instagram.com/reel/DeG80_sTYnY (@sherlynheon) | 5 ChatGPT edits: /fisheye /ccd /removepeople /goldenhour /ricohflash | yes (prompts gated) | yes | Before/after of each look described; CCD = saturated, punchy, digital grain, orange date stamp; Ricoh flash = hard on-camera flash, fast falloff to black. Slash codes are shorthand, not real commands. |
| 4 | instagram.com/reel/DeSJCWHDF-d (@charliehills) | ChatGPT "photo commands": fisheye/wormseye, panning, zoomburst, topdown, crowdblur, multipleexposure, tinyplanet | yes (full list in caption) | yes | "Talk to ChatGPT like a photographer: name the lens, angle and shutter." Same photo re-shot. Expanded into photo-effects §3. Extra commands from his Substack (0.5selfie, 85mm f1.4, telephoto 200mm). |
| 5 | instagram.com/p/Dd6k910Ch6n (@skaigenerated, carousel) | ChatGPT camera-angle cheat codes: drone, worm's-eye, fisheye, speed shot, back view | yes (prompts gated) | no (carousel — vidIQ can't watch images) | Angle list only; merged into §3. |
| 6 | instagram.com/skaigenerated/reel/DeubOShqafl | "Minecraft Food Prompt" (AI video) | yes (prompt gated) | **failed** (URL format; refunded, budget exhausted before retry) | Caption only → recon voxel food template in product-vfx §F. |
| 7 | instagram.com/skaigenerated/p/Deq7nKICjKX | "Frame Break" prompt, GPT Image 2 | yes (gated) | no (carousel) | Template built from BigPromptHub IG pop-out + YouMind screen-breakout prompts (photo-effects §5). |
| 8 | instagram.com/skaigenerated/p/DeuXGRkiiUx | "Background Sketch" prompt, GPT Image 2 | yes (gated) | no (carousel) | Recon: real subject + pencil-sketch background; trompe-l'oeil sketchbook variant (gptimgprompts). |
| 9 | instagram.com/skaigenerated/p/Del1RmKijNL | "Loading Me" prompt, GPT Image 2 | yes (gated) | no (carousel) | Recon: half-rendered person + progress bar; images not seen, so composition is a best guess. |
| 10 | instagram.com/skaigenerated/p/DeuXgJwihLh | "Block Print" editorial art poster, GPT Image 2 | yes (gated) | no (carousel) | Recon: linocut/woodblock poster, 2-3 inks, carved type. |
| 11 | instagram.com/skaigenerated/p/Deq7GWciiv5 | "Shadow Lift" prompt, Nano Banana 2 | yes (gated) | no (carousel) | Meaning unclear from caption; recon = shadow recovery + dappled-light portrait. Verify against the actual images before relying on it. |
| 12 | instagram.com/skaigenerated/reel/DeuZwBDqKT9 | "iPhone Blurry Effect" via Gemini (Nano Banana) | yes (gated) | **failed** (URL format; refunded) | Caption: upload photo to Gemini + one prompt → real-looking iPhone motion-blur shot. Recon from PromptHero/SweetPrompt "mediocre iPhone selfie" prompts. |
| 13 | tiktok.com/@fashionbyally/video/6836877826898070790 | 2020 Picsart tutorial: DIY "Vogue" magazine cover (crop 9:16, masthead sticker, blend modes) | page blocked (site maintenance) | yes | Pre-AI technique. Takeaway: magazine-cover look = gpt_image_2_5 with a made-up masthead; never use real mastheads (trademark). |
| 14 | zemith.com/en/contents/chatgpt-photo-editing-prompts | Article: 20 copy-paste photo-edit prompts that keep your face (ChatGPT/Gemini) | yes, full (Exa) | n/a | Core rule: KEEP clause before CHANGE clause; name features; one change per message; "don't slim, smooth or age". 20 prompts (eras, art styles, headshots, seasonal, magazine, action figure, poster, younger self) summarised in photo-effects §4-5. |
| 15 | instagram.com/reel/DetquOiI5AD (@raoulvanmullem, Higgsfield partner) | Pixel-art animation from two photos (self + car) | yes (prompt gated, workflow in caption) | not watched (caption explained the workflow) | NB 2.1 → pixel character reference sheets → Wan 3.0 with a viral reference video + sheets. |
| 16 | instagram.com/reel/DcQ2IiJTDLj (@danielchiang0620) | Poster Animation Effect: you leap out of a movie poster | yes (full steps) | yes | Higgsfield Layers poster → Layer Decomposition (1K, Standard, 8 layers) → edit layer ("Replace to a cool sunglasses") → Seedance 2.5 1080p 16:9 6 s, bitrate high. Partial on-screen prompt captured (poster stays LEFT, pure white space, sunglasses caught, hero pose). |
| 17 | instagram.com/danielchiang0620/reel/DXt3ctpkepO | ASSEMBLY EFFECT for products | yes (full 8 steps) | yes (2nd attempt with /reel/ URL) | NB Pro 9:16 4K: remove hand → clean floating product → exploded view (4 gens) → Hailuo 02 1080p 6 s, start = exploded, end = assembled. Three prompts partially transcribed from screen (product-vfx §A). |

## Web sources added to fill gaps
| Source | Used for |
|---|---|
| masonry.so/blog/exploded-view-animation-guide-nanobananapro-kling (+ YouTube tir7IcqEJ8k) | Exploded-concept still prompt, Kling first/last-frame motion prompt, acceptance checklists, "concept not teardown" caveat |
| somyanayak.com/resources/5k-assembly-animation-higgsfield | Matched START/END prompts (identical except state), Seedance motion prompt, scroll-linked GSAP build |
| nim.video/blog/product-assembly-effect-prompt | Guardrail structure (identity lock → scene lock → one motion → bans → finish), explode-and-return prompt |
| sume.com/guides/ai-exploded-view-animation | Invented-internals warning; CAD for real parts; reverse clip for reassembly |
| aitoolsforkids.com/projects/kling-robot-toy-cinematic-video-ai | Multi-keyframe chain (5 stills → 4 first/last clips); "no labels or annotations" fix |
| queststudio.io/blog/camera-lighting-prompt-cheatsheet | Lighting description order; identity-safe portrait relight + product relight prompts |
| morphed.app, photoworkout.com, chasejarvis.com, imgstyler.com, nanobananapro.photo | Relight clauses (Rembrandt, window, midday fix, neon), background-swap + rim, 4K source tip, natural retouch |
| arjavjain.org (23 prompt codes), designprompting.com, charliehills.substack.com, resources.limormarkman.com, files.johnsavageai.com (400+ codes PDF), leadwithzoe.com presets | Slash codes are shorthand; code→meaning tables; master primer prompt; /PhotoRestore, /ObjectRemove, /IdentityPreserve |
| techpilot.ai/chatgpt-photo-editing-prompts | "Change only X. Keep everything else exactly the same."; object removal prompt; Select tool for local edits |
| bigprompthub.com (IG pop-out), youmind.com, picxstudio.com, gptimgprompts.com | Frame-break and trompe-l'oeil sketch templates |
| prompthero.com, sweetprompt.com | iPhone flash / motion-blur "mediocre snapshot" prompts |
| fal.ai/learn/tools/prompting-gpt-image-2, nemovideo.com | GPT Image 2 edit structure (Change/Preserve/Constraints); keep text/labels in centre 80% for frames that will be animated |

## Couldn't fetch / gaps
- Exact prompts for all @skaigenerated posts (DM-gated). Five carousels can't be watched by vidIQ; two reels failed on URL format and the 10-call budget ran out before retrying with `/reel/<id>/` URLs (both refunded). Retry later with `https://www.instagram.com/reel/DeuZwBDqKT9/` and `/reel/DeubOShqafl/` to replace the recon templates for iPhone blur and Minecraft food.
- TikTok page itself returned a maintenance error (vidIQ watched the video fine).
- Daniel Chiang's prompts only partly visible on screen; the start of prompts 1 and 3 and most of the poster video prompt are reconstructed.
