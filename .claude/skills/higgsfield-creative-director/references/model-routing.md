# Model routing (built from the live Higgsfield catalog via models_explore, 10 Oct 2026)
Re-verify with `models_explore action:get model_id:<id>` at the start of each session - params and ranges change.

## Video
**Default for cinematic ads (Klaus, 20 Oct 2026): Seedance 2.5 omni_reference + Genjutsu (`hf_mult_motion_control`, motion transfer from a phone reference video) + 4K upscale on the final. Both max 1080p natively.**

| Job | Model id | Why | Key params / limits |
|---|---|---|---|
| Dialogue skit, 2-6 angles, one scene | `kling_o3_image_reference` (Kling 3.0 Omni, up to 7 ref images) or `kling_o3_flf` (first/last frame) | Native multi-shot + speaker-attributed lip-sync in ONE generation; identity held across cuts | `multi_shots:true`, `multi_prompt:[...]` (ordered shot prompts + durations), duration 3-15 s, mode std/pro/4k, sound on |
| Single shot from a start frame w/ dialogue | `kling3_0` | Good motion + audio; honours Elements only if a `start_image` is supplied | 3-15 s (min 3 - do NOT default to 3 for spoken lines), std/pro/4k |
| Longer story/ad 15-30 s, reference-driven, edits, extensions | `seedance_2_5` | 4-30 s, omni_reference (image/video/audio refs), video_edit, video_extension, **draft mode** | `mode`, `draft:true` (480p preview) -> finalize with `draft_job_id`; 1080p max |
| Identity-locked reference video, product/multi-SKU | `seedance_2_0` | Up to 9 img / 3 video / 3 audio refs, Elements supported, 4k | 4-15 s, std/fast |
| Hero cinematic shot, director controls | `cinematic_studio_video_4_0` | Camera body/lens/aperture/era/pacing/genre/lighting/palette ids | 4-30 s, 480/720p; t2v/omni/edit/extension |
| Cinematic w/ genre + multi-shot, cheaper | `cinematic_studio_video_v2` | genre, speedramp, multi_shots, cfg_scale (prompt adherence) | 3-12 s |
| Product ad / UGC preset formats | `marketing_studio_video` | Hooks, settings, avatars, ad_reference recreate | 12-15 s |
| Recreate an existing ad for new cast/market | `ad_multiplier_v2` | Keeps structure/beats/pacing | source 4-30 s |
| Copy motion from a reference clip onto your character | `hf_mult_motion_control` (Genjutsu) / `motion_control` | Motion transfer | - |
| Fix one thing in an existing clip | `kling_video_edit`, `flux_3_video_edit`, `seedance_2_5 mode:video_edit` | Avoid full regen | - |
| Re-voice / dub / lipsync existing clip | `voice_change`, `dubbing`, `sync_so` | Post only - prefer native dialogue at generation | - |
| Upscale / HDR / deflicker | `upscale_video` (topaz/bytedance aigc preset), `topaz_hyperion_2_5`, `video_deflicker` | Only after the edit is locked | - |

## Image
| Job | Model id | Notes |
|---|---|---|
| Start frames / photoreal people, multi-reference consistency | `nano_banana_pro` (2k/4k) / `nano_banana_2_1` (img+video refs, seed) | Best for "same room, new angle" from a master still |
| Typography, carousels with text, edits | `gpt_image_2_5` (variant flare/sunburst, quality up to max, 4:5 supported) | Default image model; use `quality:medium+` for finals |
| Real person identity (Klaus) | `soul_2` / `soul_cinematic` + `soul_id` | Train once from 5-20 photos |
| Cinematic stills / mood boards | `soul_cinematic`, `cinematic_studio_2_5` | Anti-"slop" look |
| Consistent set from multiple angles | `3d_jutsu_angles`, `nano_banana_pro` with master still as ref | |
| Logos, icons, vector | `recraft_v4_1` (`vector`/`utility_vector`, palette hexes) | Outputs SVG-capable art |
| Product/ad statics | `marketing_studio_image`, `ms_image` (needs style_id), Ads Studio | |
| Text-heavy infographic | `ideogram_4_5`, `openai_hazel` | |
| Inpaint / edit region | `nano_banana_2` / `seedream_v5_pro` with mask | |

## Reference systems (use them - this is where consistency comes from)
- **Elements** (`manage_reference_elements create`) - character/environment/prop from one image; inject with `<<<element_id>>>` in the prompt. Works with nano_banana_pro/2, gpt_image_2, seedream 4.5/5 lite, cinematic_studio_2_5, Cinema Studio Video 2/3, seedance_2_0, kling3_0 (+start_image required).
- **Soul** - trained identity, soul_2 / soul_cinematic only, one person per generation.
- **Voices** - `list_voices` / `create_voice` for a consistent narrator or character voice.

## Cost discipline
- `get_cost:true` preflight on every planned call.
- Composition passes at low quality / std / draft; upgrade only the approved take.
- Never regenerate a whole clip to fix one element - use an edit model.
