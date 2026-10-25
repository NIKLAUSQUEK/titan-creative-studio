# Edit & style menu (Phase 1.5 - offer as tappable choices; every option maps to a real execution route)
Route key: HF = Higgsfield generation (prompt/preset/model) | FF = ffmpeg/local edit script | MG = vidiq_motion_graphics / compose | ED = needs CapCut/human editor (say so honestly)

## 1. Vibe / genre (pick 1-2)
GenZ chaos (jump cuts, meme inserts, overlays) HF+FF | Deadpan comedy (static, held beats, silence) HF | Realistic UGC (handheld phone, natural light, imperfect) HF | Thirst-trap / tasteful sexy (slow-mo, golden light, body-forward framing, no nudity) HF | Serious workout (low angles, sweat, grade crush, bass) HF+FF | Aura farming (slow push-ins, silhouette, rim light, dramatic music, minimal words) HF+FF | Accent/character comedy (voice persona) HF voice | Premium clinic (calm, beige, slow) HF | Documentary/recon (handheld, VO, map/text cards) HF+MG

## 2. Camera language
Static tripod | Handheld drift | POV (state WHOSE eyes) | Low-angle hero | Overhead | Dolly/push-in | Crash zoom | Orbit | Whip-pan | Snorricam  -> all HF (Kling/Seedance/Cinema Studio camera fields)

## 3. Pacing
Shot length: 0.5-1s (hyper) | 1.5-3s (standard TikTok) | 3-6s (cinematic)  FF | Speed ramps HF(Cinema Studio speedramp)/FF | Freeze-frame holds FF | Jump-cut dead air removal FF (whisper word timing)

## 4. Transitions
Hard cut FF | Match cut (object/motion) HF start/end frames + FF | Whip-pan transition HF | Zoom-through FF | Flash/bulb flicker FF | Dip to black FF | Glitch FF | Mask/body wipe ED (or HF first/last frame) | Spin ED

## 5. Zooms & emphasis
Snap punch-in 5-10% FF | Crash zoom + freeze FF/HF | Slow Ken Burns FF/MG | Shake on impact FF

## 6. SFX
Whoosh/riser FF(synth) | Boom/impact FF(synth) | Record scratch, vine boom, bruh, ding, camera shutter FF (needs licensed SFX pack - stock in repo /assets/sfx) | Silence beat FF

## 7. Captions & text
Word-pop karaoke FF | Static bold (DejaVu-style) FF | Hook headline (all caps + emoji) FF | Highlighted keyword colour FF | Handwritten/notes app style FF | Kinetic typography MG

## 8. Motion graphics / art / animation
Stat counters, lists, lower-thirds, quote cards MG | Arrows/circles callouts FF/MG | Anatomy/diagram explainer (pelvic floor!) HF image + MG | 2D/anime/claymation style shots HF (style prompt / Soul cinematic) | 3D scene HF (scene_builder_3d)

## 9. Voice
On-camera native lip-sync HF (Kling sound on) | Voice swap HF voice_change (e.g. Benji) | Narrator VO HF generate_audio / vidiq voiceover | Accent persona HF voice + prompt | Yapping style: fast/no-pause/run-on (cut pauses FF) vs calm explainer

## 10. Music & sound bed
Trending TikTok Commercial Music Library track (HF tiktok_music_trending - licensed for ads) | Original generated track (vidiq_generate_music) | Room tone only | Music ducking under VO FF
RULE: brand ads must use commercially licensed sounds. Personal-account trending sounds are added in-app at upload, never baked into a brand ad.

## Presets
Menu of 44 ready presets (viral, pro, niche, house, UGC) with brand/funnel fit and compliance locks: `style-catalog.md`. Beat-by-beat B-roll / filler / music placement: the `story-sync` skill (Sync Map).
A creator StyleCard (library/styles/<handle>.md) is a one-tap bundle of the above. Offer "Edit like <creator>" first, then let him override individual rows.
For real footage, every FF row above is a parameter in the auto-editor (`tools/editor`, references/editor.md): `editor.py preset from-stylecard <creator>` turns a StyleCard into a `style-<creator>` preset, and the UGC formats (selfie talking head, unboxing, try-on/demo, reaction, POV, experience-style, day in the life, green screen) ship as presets.
