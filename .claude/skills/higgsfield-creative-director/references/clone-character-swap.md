# Clone / character-swap workflow ("this is me… and this is also me")

Klaus, 2026-10-25: "look-alike or clone workflow… he gatekeeps his methods through a paywall."
This file is the method, reverse-engineered from:
- @terencesia's "Which is better?" reel (Wan 3.0 vs Seedance 2.5 on Higgsfield; 465 likes, 391 comments from a comment-to-get CTA);
- @hi.boly's Higgsfield creator reel, which says the steps out loud.

Status: the method is [measured] from both reels; the credit numbers are the creators' own claims (Seedance 320 vs Wan 70 credits per 20 s).

## What it is
1. You film yourself performing: talking, walking, holding a cup.
2. An AI video model re-renders that exact performance as a different character: your movement, timing, gestures and usually your voice; their face, hair, body and outfit.
3. "The image gives the look, the video gives the movement" (@hi.boly).

It is motion transfer / video-to-video with a character reference. It is not a face-swap of a real person, and that line is the hard rule below.

## The workflow (our stack: Higgsfield MCP tools)
1. **Film the driver clip** (phone, 1080p, 30 fps):
   - 5-15 s per shot, even light, plain background or the real location;
   - the whole body in frame if the outfit matters, the face large if expression matters;
   - one clear action ("holding a drink", "walking to camera");
   - no fast spins, hands crossing the face or heavy motion blur, because these break identity.
   - Film 2-3 takes. Keep the original audio: video-to-video keeps your real voice and lip timing (filmmaking-longform.md).
2. **Design the character** (character-design.md: an original card, never a real-person lookalike). Build the character sheet:
   - **Fast:** Higgsfield AI Influencer builder: `ai_influencer_prepare` (face, hair, outfit; optionally your photo as the base reference) → `ai_influencer_generate`. Free accounts get 5 free character images. This is the step @hi.boly shows.
   - **Controlled:** a Nano Banana Pro / GPT Image character sheet (front + three-quarter + back, full body, neutral light). @terencesia's inset shows exactly this: a 3-view sheet.
   - Gate 4: Klaus approves the sheet. Save it as an Element and register it in `cast/registry.md` so the character returns identical next time.
3. **Transfer the motion** with the cheapest viable route first (credit-saving.md: draft, approve, then final):
   - **Genjutsu** (`generate_video`, model `hf_mult_motion_control`): character image + driver video. The studio default for performance shots.
   - **Seedance 2.5 omni_reference**: the highest realism of the two in the comparison reel. Prompt pattern: "@Image1 performs the exact movements, gestures and lip timing of @Video1; keep @Image1's face, hair and outfit; [action detail, e.g. holding an iced coffee]; [location/light]". Name the prop explicitly: both reels call out "I'm supposed to be holding a drink".
   - **Wan 3.0**: about 4.5× cheaper per the reel (70 vs 320 credits per 20 s), slightly less detail. Use it for drafts and for volume.
   - Draft at the lowest resolution, QC, then the final at 1080p. Optional 4K upscale of the locked final.
4. **QC against the sheet** (qc-rubric.md + realism.md). Run `scripts/qc_frames.py` and look at the contact sheet.
   - Check face consistency at the start, middle and end, skin texture, eyes, clothes, the prop in hand, hands and fingers, and lip sync.
   - These are the exact checkpoints @terencesia narrates: "look at my face, the texture, my eyes, my clothes".
   - Common failures: identity drift on head turns, the prop morphing, the background melting where your body was. If so, re-roll that shot only.
5. **Edit:** one of the formats below. `editor.py` takes the AI clips as footage or B-roll.

## Content formats that use it
- **A/B model test** (@terencesia):
  - layout: a top header "WHICH IS BETTER?" with the key word in a lime highlight box; model labels "WAN 3.0 vs SEEDANCE 2.5" under it with credit bars; side-by-side columns (original | AI);
  - the 3-view reference sheet inset as a small card, with check pills (face texture ✓ eyes ✓ clothes ✓ holding a drink ✓) ticking on as he says them;
  - bold italic caps captions, 1-3 words, with the keyword in lime; a cost tag in red ("320 CREDITS") vs lime ("70 CREDITS", "4.5X CHEAPER");
  - ends on a face-to-camera "Comment AI" CTA.
  - Editor: `broll.mode: "side"` (side-by-side), `texts` kicker/label cards. Format guide: playbook below.
- **"This is me, and this is also me"** (@hi.boly):
  - one walk, cut on the footstep into 4-6 different characters every ~1.5-2.5 s (a match cut: same framing, same stride, a new person);
  - then the tutorial: the creator cut-out with a thick yellow sticker outline over a retro desktop (XP-style sky wallpaper + a Paint window holding the screen recording);
  - lowercase serif karaoke words; the CTA "comment create" in script lettering with a red scribble underline.
- **One actor, every role** (comedy): Klaus films every character of a skit himself, and each take is swapped into a different original character (the boss, the patient-type, the gym bro, the auntie). The cheapest way to cast a whole skit. Combine with playbook-skit.md: whose body carries the gag stays a hard rule per role.
- **Then vs now / alternate-universe me:** the same monologue performed as the 1990s, 2050 or "if I never did rehab" version of yourself (aging and styling are allowed on YOUR own likeness).
- **Brand mascot with a human performance:** the founder or physio performs; the mascot character (animation-3d-cartoon.md) delivers it. Keeps real staff off camera when they prefer.

## Hard rules (non-negotiable)
- **Drivers:** footage of Klaus, the team, hired talent, or real people's clips brought in through the collab workflow (Klaus handles rights, 2026-10-29). The output keeps only the motion: never the driver's face or voice (replace the audio with the character's own voice).
- **Characters:** original only (character-design.md composite method). Never a celebrity, influencer, politician or private person lookalike, never "make me look like <real name>", never a real person's voice. That is impersonation / deepfake territory and is refused even "as a joke".
- **No AI label** in the video or caption (Klaus, 2026-10-29: it takes away from the video). Switch on the platform's own AI-disclosure toggle where TikTok/Meta require it for photorealistic AI.
- **Health brands (SG pack):** a transformed character never poses as a patient, doctor or customer giving an experience (no testimonials, no implied results). Fine for skits, explainers and clearly fictional characters.
- **Comment-to-get CTAs** ("comment AI") are fine on personal accounts. On brand accounts, give the value in the post instead of gating it.

## Cost ladder (per 20 s shot, the creators' numbers; check `get_cost` before each run)
Wan 3.0 draft (≈70 credits) → pick the best take → Seedance 2.5 or Genjutsu 1080p final for hero shots only (≈320) → upscale only the locked final.
A 30 s "this is also me" reel with 5 characters × 2-3 s each needs about 5 short clips: draft them all on the cheap route, and finalise only the ones used.
