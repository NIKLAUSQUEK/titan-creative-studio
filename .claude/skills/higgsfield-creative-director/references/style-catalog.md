# Style catalog — pick a preset

> This file covers **edit** presets. Every other style family (script/voice, animation/faceless, carousel, LinkedIn) and the cross-family pairings live in the style home: `/styles`, `python scripts/styles.py offer|find|show`, menu `styles/STYLE_MENU.md`.

Every preset is a one-tap bundle for the auto-editor (`editor.py assemble --preset <name>`) and a style brief for generated work (Gate 3 look + edit rhythm). Brand guide (`edit-brand` block) and ledger still win (precedence). Sync behaviour per preset: `.claude/skills/story-sync/references/style-sync-patterns.md`. Creator evidence: `research/sources-style-library.md`. A specific creator's StyleCard → `editor.py preset from-stylecard <name>` (`style-<creator>`).

**Health brands (Physio Spot, heal360):** only presets without a 'not for health' lock; SG health compliance locks are listed per preset.


## Viral creator formats

| Preset | Use for | Brands | Funnel | Aspect | Compliance lock |
|---|---|---|---|---|---|
| `clean-explainer` | Calm curious talking head, kinetic text beside the speaker with yellow keywords, framework cards per point, paper transitions, low lo-fi bed. | Physio Spot, heal360, TITAN.AI, Klaus personal | TOFU, MOFU | 9:16 | health: factual benefits only, no 'best/guaranteed', no patient quotes |
| `luxury-broll` | Cinematic two-angle talking head over aspirational B-roll, accent-colour UI/graph pops, animation-dense intro (4-10 visuals/min) easing to ~2/min. | TITAN.AI, Klaus personal, Power Protein brand films (grade only) | TOFU, MOFU | 9:16 | no income/lifestyle guarantees; not for health brands |
| `magic-transition` | Single-take feel; a mundane setup transforms through a hidden cut (whip, lens block, object pass); SFX hit sells the magic; loopable end. Sound-off friendly. | Power Protein, PeachForm, TITAN.AI | TOFU, paid hooks | 9:16 | never show an instant body or pain transformation (misleading) |
| `moral-skit` | Scripted archetype drama: injustice hook → escalating wrongs → reveal → consequence → moral stated to camera. Make 4-5 hook/ending variants. | Physio Spot, heal360, PeachForm | TOFU | 9:16 | no testimonials or patient results; no superlatives (best/No.1/leading); no free-consult/discount inducements; general education only, no individual advice; no  |
| `podcast-clip` | Hook claim first (no welcome), speaker-fill ↔ stacked split switching, bold karaoke captions, host reaction cutaways, low tension bed, 30-90 s. | TITAN.AI, Klaus personal, clinician interviews | TOFU, MOFU | 9:16 | keep qualifiers; cut context fairly; health: no patient-guest 'it cured me' clips, no outcome promises |
| `retention-max` | Promise-matched cold open, stakes in 5 s, stair-step escalation with re-engagement spikes, abrupt end. 2024 style lets scenes breathe (~23 cuts/min long-form). | TITAN.AI, Power Protein, Klaus personal | TOFU | 9:16 | health brands: no prizes/giveaways (inducements), no superlatives |
| `silent-deadpan` | Over-complicated 'hack' (recreated with our own cast) → static deadpan stare → the obvious simple way → long hold → palms-up gesture. No speech, no captions. | Physio Spot (myth stretch vs correct one), Power Protein | TOFU | 9:16 | recreate hacks with our cast, never stitch others without rights; health: the correct way is factual, not 'the only' way |
| `story-vlog` | Earnest serialized challenge diary: one-line rules, named recurring segments, running counter, a heart moment, cliffhanger to the next episode. | Klaus personal, TITAN.AI build-in-public, PeachForm/Power Protein creator challenges | TOFU, MOFU | 9:16 | no extreme diet/rapid weight-loss framing; no body shaming or before/after transformations; supplement claims only in label-approved wording; health brands: sta |
| `storytime-text` | Original story (never scraped posts) told by VO over looping brand-owned satisfying B-roll, word-by-word captions on the seam, verdict question or Part 2 ending. | Klaus personal, PeachForm, Physio Spot (fictional parables) | TOFU | 9:16 | original scripts only (no Reddit/others' posts); label AI voice; health: fictional + educational, never first-person 'I was cured' |
| `street-interview` | One fixed recurring question in 0-2 s, persistent top title bar with the question/take, natural ambience, answer as the payoff, host reaction. | TITAN.AI, Power Protein, PeachForm | TOFU | 9:16 | signed releases from everyone on camera; health: no patient vox pops about results |
| `quiz-reveal` | Question card → countdown → reveal → "what did you guess?" (comments + rewatches). Health: educational questions only. | Physio Spot (myth quiz), Power Protein, PeachForm, TITAN.AI | TOFU | 9:16 | health: educational questions only, no self-diagnosis quizzes |

## Professional / cinematic / commercial

| Preset | Use for | Brands | Funnel | Aspect | Compliance lock |
|---|---|---|---|---|---|
| `absurd-sketch` | Straight-faced genre parody that escalates into absurdity, deadpan tag, heavy sting. Never for clinics. | Power Protein, TITAN.AI | TOFU | 9:16 | not for health/clinic brands |
| `linkedin-founder-video` | LinkedIn native vertical founder video: promise in sentence 1 = caption line 1, 2-4 word captions, B-roll/screens every 3-6 s, auto panel boards, low bed, one CTA (linkedin-playbook.md §9). | TITAN.AI, Klaus, clinic directors | TOFU, MOFU | 9:16 (4:5 alt) | clinic: educational only, no patients, no offers |
| `b2b-founder` | Professional talking head: persistent top headline bar, burned captions with accent highlight, punch-in jump cuts, data callouts, name lower third, soft CTA. | TITAN.AI, Klaus, clinic directors | MOFU, BOFU | 1:1 (4:5 alt) | - |
| `cinematic-vlog` | Host-led vlog with cinematic B-roll: sensory cold open, speed ramps, whips, match cuts, jump-cut talking, time-lapse bridges, sincere long-take monologue. | Klaus personal, gym/clinic atmosphere | TOFU | 16:9 (9:16 cut) | - |
| `clinic-trust` | Calm clinician-led brand film: real staff, soft daylight, slow moves, dissolves, low music, factual supers. SG health-compliant by default. | Physio Spot, heal360 | MOFU, BOFU | 16:9 + 4:5 + 9:16 | no testimonials or patient results; no superlatives (best/No.1/leading); no free-consult/discount inducements; general education only, no individual advice; no  |
| `doc-trailer` | Three-act trailer: bite over black, title cards, accelerating montage on risers, silence, button line, title + date. | Klaus origin story, TITAN.AI client case-study docs | TOFU | 16:9 (9:16, 4:5 cutdowns) | - |
| `manifesto-montage` | VO manifesto over documentary/athlete montage, building from solo instrument to full, ending on a held thesis image and tagline card. | PeachForm, Power Protein, TITAN.AI vision | TOFU | 16:9 hero, 9:16 + 4:5 cutdowns | no extreme diet/rapid weight-loss framing; no body shaming or before/after transformations; supplement claims only in label-approved wording |
| `map-explainer` | Host on camera + paper textures, archival, map zooms, serif type; cold-open question, chapters, twist, synthesis. | TITAN.AI, Klaus personal, Physio Spot deep dives | TOFU, MOFU | 16:9 (9:16 shorts cut) | - |
| `mascot-unhinged` | Lo-fi phone skit timed to an audio drop, static meme caption at the top, self-aware brand humour, mascot or staff as recurring character. | Power Protein, TITAN.AI, Klaus personal | TOFU | 9:16 | licensed audio on brand accounts; not for clinics (don't trivialise conditions) |
| `motion-explainer` | No host: flat-vector animation timed to VO, saturated palette, consistent character set, gentle score, chapter cards. | Physio Spot/heal360 anatomy explainers, TITAN.AI | TOFU, MOFU | 16:9 (9:16 shorts cut) | - |
| `product-hero` | Premium reveal with no talking head: macro edge-light, kinetic claim type on the beat, silence before the hero hold, logo end card. | Power Protein, PeachForm merch, TITAN.AI UI | TOFU, launch | 9:16 (also 1:1, 16:9) | - |

## Niche experts, SEA & ad formats

| Preset | Use for | Brands | Funnel | Aspect | Compliance lock |
|---|---|---|---|---|---|
| `aesthetic-lifestyle` | Music-first, soft pastel grade, slow gimbal B-roll, diary VO, minimal lowercase text, sets × reps cards. | PeachForm, Power Protein | TOFU, MOFU | 9:16 | no extreme diet/rapid weight-loss framing; no body shaming or before/after transformations; supplement claims only in label-approved wording; licensed music on  |
| `doctor-reacts` | Recreated claim card or in-app stitch, freeze-frame verdict, diagram explanation, what's actually true, takeaway. | heal360, Physio Spot | TOFU | 9:16 | no testimonials or patient results; no superlatives (best/No.1/leading); no free-consult/discount inducements; general education only, no individual advice; no  |
| `exercise-demo` | The exercise is the A-roll: problem title over a moving demo, cue overlays, mistake vs correct, progression, save CTA + safety line. | Physio Spot, heal360, PeachForm | MOFU | 9:16 | no testimonials or patient results; no superlatives (best/No.1/leading); no free-consult/discount inducements; general education only, no individual advice; no  |
| `fast-recipe` | Hero shot + premise in 1 s, beat-cut ASMR step montage, plating, the bite in silence, verdict. | Power Protein, PeachForm | TOFU | 9:16 | no extreme diet/rapid weight-loss framing; no body shaming or before/after transformations; supplement claims only in label-approved wording; halal check before |
| `myth-buster-expert` | Clinician states a common myth, rejects it in 2 s, gives 1-2 evidence points and a 'do this instead' demo. | Physio Spot, heal360 | TOFU | 9:16 | no testimonials or patient results; no superlatives (best/No.1/leading); no free-consult/discount inducements; general education only, no individual advice; no  |
| `raw-gym-vlog` | Minimal-edit, narration-led long-form gym vlog: car plan, sets with commentary, pump check, ride-home reflection. Continuity over cuts. | Klaus personal, Power Protein (in-use placement) | TOFU | 16:9 | no extreme diet/rapid weight-loss framing; no body shaming or before/after transformations; supplement claims only in label-approved wording |
| `sea-skit` | Localised one-person or couple skit: situation text on top, in-character open, escalation, music stops dead on the punchline, reaction tag. | Klaus personal, Power Protein, PeachForm | TOFU | 9:16 | licensed audio on brand accounts (no drama OSTs); never mock patients; localisation.md pack |
| `sensitive-health-edu` | Calm, destigmatising clinician education: plain-language symptom question, normalise, mechanism on a model/diagram (never bodies), when to seek care. No humour SFX. | heal360, Physio Spot men's health | TOFU, MOFU | 9:16 | no testimonials or patient results; no superlatives (best/No.1/leading); no free-consult/discount inducements; general education only, no individual advice; no  |
| `tech-review-premium` | Calm authority: dark matte set, motion-control product glides, sparse spec callouts, balanced pros/cons, verdict. | Power Protein product hero, TITAN.AI showreel, Physio Spot space/equipment | MOFU | 16:9 (9:16 cut) | no comparative superlatives; an 'honest verdict' must not become a self-review testimonial (health) |
| `ugc-ad-hook-stack` | Native selfie UGC ad: emotion-first hook in 1.5 s, re-hook every 5-15 s, problem → product → proof → CTA. Make a hook matrix (same body, 3-5 hooks). Product brands only. | Power Protein, PeachForm, TITAN.AI client ads | TOFU, BOFU | 9:16 | no extreme diet/rapid weight-loss framing; no body shaming or before/after transformations; supplement claims only in label-approved wording; disclose paid part |

## House styles

| Preset | Use for | Brands | Funnel | Aspect | Compliance lock |
|---|---|---|---|---|---|
| `aura-cinematic` | Slow push-ins, minimal words, big statement captions, contrast-crushed grade with vignette, riser into the drop. | - | - | 9:16 | - |
| `deadpan-comedy` | Held beats, silence kept on purpose, static frame, no zooms except the crash zoom on the reveal, one impact SFX on the payoff, captions static. | - | - | 9:16 | - |
| `documentary` | VO-led, B-roll heavy (every 4 s), lower-thirds for names/facts, sentence captions, clean cuts. | - | - | 9:16 | - |
| `genz-chaos` | 0.8-1.5 s shots, punch-in every cut, 1-2 word captions with keyword colour + emoji, stim every 1.5-3 s, meme inserts as B-roll. | - | - | 9:16 | - |
| `premium-calm` | Slow pace, soft push-ins, serif sentence captions low in frame, warm grade, music low, 0-2 SFX total. | - | - | 9:16 | - |
| `talking-head-punchy` | Jump cuts on every pause, snap punch-ins every ~3 s, 2-3 word pop captions, light whooshes. The safe default for founder/expert reels. | - | - | 9:16 | - |

## House UGC formats

| Preset | Use for | Brands | Funnel | Aspect | Compliance lock |
|---|---|---|---|---|---|
| `ugc-day-in-the-life` | Timestamped vignettes (6:00 AM, 9:30 AM …) as lower-thirds, 1-3 s shots, VO or captions, warm natural grade, steady music bed. | - | - | 9:16 | - |
| `ugc-green-screen` | Creator in front of a screenshot/article/post (the B-roll fills the background), points at it; captions high, keyword colour, punch-ins on the reveal. | - | - | 9:16 | - |
| `ugc-pov` | On-screen 'POV: …' text carries the premise, minimal talking, handheld, quick 1-2 s shots, trending-style sound (licensed for brands). | - | - | 9:16 | - |
| `ugc-reaction` | Source clip top/left, face reaction held 0.6-1.2 s and cut on the eyes, one stim per reaction, captions only on the punch. | - | - | 9:16 | - |
| `ugc-selfie-talking-head` | Phone-in-hand, eye contact, one idea. Hook line straight to camera, keep natural imperfections, light jump cuts. | - | - | 9:16 | - |
| `ugc-testimonial-style` | First-person EXPERIENCE format told by the founder/staff/creator about their own experience, NOT a customer endorsement. For regulated brands (e.g. SG health) never use patients, results claims or 'it cured me'; the compliance pack check is mandatory. | - | - | 9:16 | - |
| `ugc-try-on-demo` | Before → doing it → result framing (no exaggerated claims), mirror/tripod shots, beat-synced cuts between looks or steps. | - | - | 9:16 | - |
| `ugc-unboxing` | Hands + product, ASMR-ish sound, reveal held 1-2 s, captions name what is in the box, close-up B-roll of details. | - | - | 9:16 | - |

## Quick picks by job
| Job | First choice | Alternatives |
|---|---|---|
| Physio/health education short | `myth-buster-expert` | `exercise-demo`, `clean-explainer`, `doctor-reacts`, `sensitive-health-edu` (pelvic/men's) |
| Clinic brand film / trust | `clinic-trust` | `premium-calm`, `motion-explainer` |
| Founder thought leadership | `clean-explainer` | `b2b-founder` (LinkedIn), `podcast-clip`, `luxury-broll`, `storytime-text` |
| Product launch / hero | `product-hero` | `tech-review-premium`, `magic-transition`, `manifesto-montage` |
| Protein/fitness paid social | `ugc-ad-hook-stack` | `fast-recipe`, `exercise-demo`, `ugc-*` house presets |
| Brand film / campaign | `manifesto-montage` | `doc-trailer`, `cinematic-vlog` |
| Comedy / skit | `sea-skit` (local) | `deadpan-comedy`, `moral-skit`, `silent-deadpan`, `absurd-sketch`, `mascot-unhinged` (never clinics) |
| Long-form YouTube | `retention-max` (challenge) | `story-vlog`, `map-explainer`, `raw-gym-vlog`, `cinematic-vlog` |
| Repurposing a podcast / interview | `podcast-clip` | `street-interview` (vox pops) |

All research-derived numbers are estimates from public sources (no frame measurement was possible this session); refine with `/style` StyleCards or measured references, then `/learn`.
