# Snap Saigon AI influencer: look brainstorm [draft, Klaus picks]

Klaus, 2026-10-29: "we want to make a Snap Saigon Genjutsu AI influencer like others are doing now by feeding it real people clips… we need to brainstorm the look."

## How it works (one paragraph)
We design ONE original character (a face and style that belong only to Snap Saigon). Then every week we take real clips of people living Saigon (creator clips from `editor.py collab scout`, plus our snappers filming at the spots) and use Genjutsu motion transfer: the character performs the real person's movement at the real place. The output keeps only the motion. The face is always our character, and the voice is always the character's own voice. No AI label in the video or caption (ledger [ai-labels]); the platform's AI toggle is switched on where required.

## What every concept shares (brand anchors)
- **The yellow:** one item in Snap Saigon accent yellow (#FFC727) in every shot: a scarf, a helmet, a camera strap, sneakers. Viewers learn to spot it.
- **A camera:** the character is a snapper, so a camera is always in hand or round the neck. It explains the brand in one look.
- **Honda Cub / motorbike:** the most Saigon object there is; the "arriving" shot of every video.
- **Lowercase brand voice:** street-smart, warm, matter-of-fact (brand file §5). Never "best", "#1", "guaranteed".
- **Adult, original, not a lookalike** of any real person (character-design.md composite method + lookalike QC).

## Five looks to choose from

### A. "Linh": the Saigon it-girl snapper (recommended hero)
- **Who:** 26, Vietnamese (Saigon-born), the cool local friend every tourist wishes they had.
- **Face:** heart-shaped face, soft high cheekbones, almond eyes with a slight upturn, straight full brows, small straight nose, full lips with a red-brick lip, a beauty mark under the left eye (her signature).
- **Hair:** glossy black bob with blunt bangs; a yellow claw clip on hot days.
- **Signature outfit:** a cropped modern áo dài top in cream or black over wide cargo trousers and white sneakers; yellow scarf on the bag strap. Rain look: clear poncho over the outfit.
- **Props:** a vintage film camera round her neck (no brand logo), a Honda Cub in mint green.
- **Personality:** cheeky, fast, knows every hẻm. **Voice:** warm Saigon-accented English, quick, laughs mid-sentence; Vietnamese for the punchlines.
- **Catchphrase:** "ok, follow me."
- **Best for:** hype trailers, hidden spots, lead magnets (MAP), food lane, giveaways.

### B. "Bảo": the 70s-Saigon motorbike guy (best sidekick)
- **Who:** 28, Vietnamese, the nightlife and football guy.
- **Face:** square face, defined jaw, deep-set eyes, thick straight brows, a short tidy moustache, an easy wide grin.
- **Hair:** slicked-back, a little long at the neck.
- **Signature outfit:** retro short-sleeve printed shirt (1970s Saigon pattern), gold-tone aviators, cream trousers, a yellow half-face helmet.
- **Props:** a chrome Honda Cub, a flag for match nights.
- **Personality:** loud, loyal, funny. **Voice:** deep, playful, Vietnamese-English mix.
- **Catchphrase:** "đi bão thôi!" (let's go storm the streets)
- **Best for:** "if Vietnam win" posts, đi bão street nights, Bui Vien, expat parties, caption contests.

### C. "Cô Mai": the history storyteller
- **Who:** early 30s, Vietnamese, calm and credible: the face of Saigon Stories.
- **Face:** oval face, soft jaw, gentle hooded eyes, feathered brows, natural lips, round tortoiseshell glasses.
- **Hair:** long, low twisted bun with a wooden pin.
- **Signature outfit:** a muted silk áo dài (sage, ink blue) or linen shirt and trousers; a yellow notebook.
- **Props:** a yellow notebook, an old map, archival photos she holds up to the real building.
- **Personality:** curious, precise, quietly funny. **Voice:** low, measured, clear English with Vietnamese place names said properly.
- **Catchphrase:** "you've walked past this a hundred times."
- **Best for:** Saigon Stories, myth-busters (the Post Office), Tết explainers. (Remembrance specials use a real narrator, not an AI host.)

### D. "Kai": the Việt Kiều coming home
- **Who:** 27, Vietnamese-Australian, back in Saigon for the first time since childhood; sees the city with tourist eyes but speaks the language badly (comedy).
- **Face:** long face, wavy hair, sun-tanned skin, freckles, wide smile, slightly crooked tooth.
- **Signature outfit:** surf-casual: loose linen shirt, board shorts, a bucket hat in yellow, sandals.
- **Props:** phone on a gimbal, a bánh mì in hand.
- **Personality:** wide-eyed, self-deprecating, honest. **Voice:** Australian English, butchers Vietnamese tones on purpose.
- **Catchphrase:** "nobody told me this."
- **Best for:** "POV: your first day in Saigon", prices, scam tips, the ghost-town Tết post, relatable comedy.

### E. "Dì Tư": the street-food auntie
- **Who:** 50s, Vietnamese, runs a (fictional) phở stall; roasts everyone with love.
- **Face:** round face, laugh lines, sharp knowing eyes, short permed hair.
- **Signature outfit:** flower-print pyjama set (đồ bộ), a yellow apron, a nón lá when outside.
- **Props:** a plastic stool, a ladle she points with.
- **Personality:** sassy, generous, nosy. **Voice:** fast Vietnamese with broken English zingers.
- **Catchphrase:** "ăn đi!" (eat!)
- **Best for:** food lane, price posts, comedy skits, funny-caption contests.

## Recommendation
- **Hero:** Linh (A). She IS the product: a local snapper who takes you to the right spot. Every format fits her, and the yellow + camera + Cub make her recognisable in one frame.
- **Sidekick:** Bảo (B) for match nights and nightlife, so the hero stays on-brand while the chaos content still has a face.
- **Later:** Cô Mai (C) once Saigon Stories proves itself in the winners report.

## Next steps
1. Klaus picks a concept (or mixes features across them).
2. Generate 3 versions of the pick with the Higgsfield AI Influencer builder (`ai_influencer_prepare` → quote → `ai_influencer_generate`, cheapest settings first) and a 3-view character sheet (front, three-quarter, full body). This needs the Higgsfield connector signed in; it isn't right now.
3. Gate 4: Klaus approves one sheet → save as an Element → register in `cast/registry.md`.
4. Lookalike QC: if she reads as any real person, regenerate with 2 features changed.
5. Voice: design the character's original voice (ElevenLabs/Higgsfield voice design), save its ID in `cast/registry.md`.
6. First test: 3 real Saigon clips from `marketing/collabs/clips-*.csv` → Genjutsu draft at the lowest resolution → QC the face at start/middle/end → Klaus approves → 1080p.
