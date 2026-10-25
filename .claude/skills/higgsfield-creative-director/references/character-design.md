# Original character design — attractive, diverse, ownable (focus: female leads)
Rules: original people only — never "looks like <real person>", never built from a real person's photos/body/voice without their consent (Soul/voice of real people = only consenting talent like Klaus). Adults, default apparent age 25+. Representation: vary ethnicity, skin tone, hair texture, body type and age band across a cast; render darker skin tones with correct undertones and lighting; avoid exoticising language.

## Build archetypes (female)
| Archetype | Build & proportion cues | Styling | Fits |
|---|---|---|---|
| Sprinter | lean, defined quads/glutes, broad shoulders for frame, low body fat, powerful stance | crop top + track briefs/joggers, spikes | sport, energy drinks, Power Protein |
| Glute/fitness athlete | strong curvy lower body, defined back, toned arms | matching gym set, lifting belt | PeachForm, gym content |
| Pilates/dancer | long lines, elegant posture, lean toned limbs | neutral co-ords, ribbed sets | wellness, heal360 |
| Swimmer | broad shoulders, long torso, athletic V | one-piece/rash guard, robe poolside | recovery, sport |
| Tennis/golf | athletic-lean, sunlit, poised | pleated skirt/polo, visor | premium lifestyle |
| Boxer/MMA | compact strength, defined arms/core, scars optional | hand wraps, sports bra, shorts | grit, confidence ads |
| Runway editorial | tall, angular, high cheekbones, minimal styling | monochrome tailoring | luxury, fashion |
| Curvy confident | soft-hourglass, full figure, radiant | bold colour, wrap dress | beauty, body-positive |
| Girl-next-door | approachable, natural features, freckles optional | denim, knitwear | UGC-style ads |
| Corporate chic | polished, groomed, sharp posture | blazer, tailored trousers | B2B, TITAN |
| Street-style | relaxed, layered, expressive | oversized, sneakers, accessories | Gen Z content |
| Mature elegance (40-60) | graceful, silver/salt hair optional, laugh lines | linen, statement jewellery | heal360, longevity |

## Build archetypes (male)
Sprinter, rugby/powerhouse, footballer (lean-athletic, quick feet), F1-driver build (lean, strong neck/core, compact), boxer, swimmer, runway editorial, bearded rugged, dad-bod relatable, silver-fox mature, corporate sharp, street-style.

## Face & feature vocabulary (mix-and-match, specific beats vague)
Face shape: oval, heart, square, diamond, long, round · Cheekbones: high/soft/sculpted · Jaw: defined/soft/tapered · Eyes: almond, hooded, deep-set, monolid, upturned, wide-set; colour · Brows: straight/arched/full/feathered · Nose: straight, button, aquiline, broad, upturned · Lips: full, bow-shaped, wide, thin-defined · Skin: undertone (cool/warm/olive/neutral), texture (pores, freckles, beauty marks, natural asymmetry) · Hair: texture (straight, wavy, curly 3a-3c, coily 4a-4c, locs, braids, cornrows, twists), length, colour, styling · Distinctive marks: dimples, gap tooth, scar, tattoo, piercing.
Ethnicity/region (describe respectfully and specifically): West African, East African, Afro-Caribbean, North African, South Asian (Punjabi, Tamil…), East Asian (Korean, Japanese, Chinese…), Southeast Asian (Malay, Vietnamese, Thai, Filipino, Peranakan…), Middle Eastern, Latina (Brazilian, Mexican…), Mediterranean, Northern European, Pacific Islander, mixed heritage.

## Voice & accent archetypes (original voices only)
Lagos English, London (RP / MLE), Manchester, Scottish, Southern US, NYC, California, Singapore English (light/strong Singlish), Malaysian English, Australian, South African, Indian English, French-accented English, Brazilian-Portuguese-accented English. Spec: pitch, pace, warmth, rasp/breathiness, laugh. Source: Higgsfield preset voices (list_voices), ElevenLabs library, or consenting voice talent.

## Character card (feeds Gate 4 Asset Bible)
@HANDLE · name · age band · heritage · build archetype · face (5-7 feature choices) · skin + hair · signature styling + colour palette · voice archetype · personality in 3 words · brands/formats she fits.
Generation: Higgsfield AI Influencer builder (ai_influencer_prepare → generate; original characters with full trait options) or nano_banana_pro character sheet (front + three-quarter + full body, realism module) → approve → Element for reuse → Genjutsu/Seedance for motion.

## Studio roster (starter — original, female-led, diverse)
Build 6-8 recurring leads across heritages and builds (e.g. West African sprinter, Vietnamese pilates instructor, Punjabi-British corporate lead, Brazilian glute athlete, Malay girl-next-door, Afro-Caribbean boxer, Korean runway editorial, 50s Peranakan mature elegance) + 3-4 male supporting characters. Recurring faces build audience recognition like a TV cast.

## Aesthetic scene archetypes (category-level, learned from public style trends — never per-person)
| Aesthetic | Makeup & hair | Wardrobe & accessories | Pose & setting | Light |
|---|---|---|---|---|
| WAG matchday glam | soft glam, bronzed glow, glossy blow-out | designer jersey-styled-up, oversized shades, statement bag | stadium box, players' lounge, tunnel walk | stadium floodlight + flash |
| F1 paddock glam | clean luxe, sleek bun or bouncy waves | tailored white/neutral co-ords, team-colour accent, lanyard | paddock walkway, grid, Monaco harbour | bright Mediterranean sun |
| Riviera old-money | no-makeup makeup, sun-kissed | linen, knit over shoulders, gold minimal jewellery | yacht deck, terrace lunch | golden hour |
| Courtside / NBA glam | sharp liner, sleek ponytail | streetwear-luxe, bold sneakers | courtside seats, tunnel | arena spotlight |
| Tennis-whites club | fresh, flushed cheeks, high pony | pleated whites, visor, cardigan | grass court, clubhouse | soft daylight |
| Runway editorial | sculpted, graphic liner or bare skin | monochrome tailoring, avant-garde | runway, white cyc, backstage | hard key, high contrast |
| Fitness-influencer | dewy, slicked-back bun | matching gym set, lifting belt | luxury gym, mirror wall | warm gym practicals |
| Beach-villa reality-TV | glam lashes, bronzer | bikini cover-up, resort wear | villa pool, fire pit | sunset + fairy lights |
| K-pop idol | glass skin, gradient lip, coloured hair | coordinated stage outfits | stage, practice room | LED stage wash |
| Bollywood glam | kohl eyes, bindi, glossy waves | saree/lehenga, heavy jewellery | haveli, sangeet stage | warm jewel tones |
| Lagos owambe glam | bold brows, gold highlight, gele | aso-ebi, coral beads | party hall, tent | warm event light |
| Clean girl / coquette / mob-wife / Y2K / Scandi minimal | per trend | per trend | per trend | per trend |

## Composite method (how "similar but original" works)
1. Pick 1 aesthetic + 1 build archetype + heritage + age band.
2. Choose 5-7 facial features from the vocabulary (never "like <name>").
3. Blend ≥3 inspiration sources at category level; no single real person maps to the result.
4. **No real names, team names, or brand logos in any prompt.**
5. **Lookalike QC**: if the output reads as a recognisable real person → REGEN with 2 features changed.
Generator: `scripts/roster_gen.py --n 8 --female-ratio 0.75 --seed 7` → balanced heritage/age/build cards.

## Character sheet v2 (from reference workflows, 2026-10-25)
Run this after the character card is approved (original character, or a real staff member with consent). **Never seed from an internet photo of a real person.**
1. **Face Lock.** 4:3, highest resolution, forehead to upper chest, neutral expression, **18% grey seamless background**, flat shadowless catalog light, 50 mm look. **Pore-level skin texture is mandatory** (realism.md): ignore guides that ask for "no visible pores".
2. **Two-panel body.** 16:9. Image 1 is the face lock; image 2 is an outfit and pose reference. Left panel: full-body front. Right panel: back view in the identical pose ("do not mirror"), divided by a thin line.
3. **Five-panel merge.** 16:9, generated at 4K:
   - large chest-up front portrait
   - left profile and right profile (head and neck)
   - **headless** full-body front, so the model reads the face only from the portrait
   - full-body rear
4. **Duplicate-face erase.** If any panel still shows a second face: "Erase the face from the full-body shot on the right panel."
5. **Single-attribute edits ("Additions").** "Keep the same character-sheet layout, physical features and expression; facial structure must not change at all. Change only: [hair / accessory / tattoo / wardrobe item], as in the reference image."
6. **State variants.** Use a separate sheet per state (dry/wet, clean/dirty, injured/recovering, uniform/casual), saved as `@handle_state`, and list them in the Asset Bible card's `variants[]` field.
7. **Wardrobe ideation.** Ask for 10 outfit prompts, render them, then combine the best items into one prompt. Composite-mask the clothes onto the original still to keep detail (ai-video-playbook.md §10).
8. **Motion test.** Keep 2 face candidates through a 480p motion test before locking (Gate 4).
