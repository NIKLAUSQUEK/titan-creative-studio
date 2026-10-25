# Sources: style library research (2026-10-25)

Feeds `tools/editor/presets/*.json` (30 research presets), `.claude/skills/higgsfield-creative-director/references/style-catalog.md` and `.claude/skills/story-sync/references/style-sync-patterns.md`.

**Method and limits.** Three research agents used only public web pages: editing breakdowns, creators' and editors' interviews, production memos, job ads, award and credit listings, and tutorials. **No video was downloaded.** YouTube blocked downloads, and the TikTok route was refused as bot-check circumvention. Very few numbers are measured; the main measured ones are MrBeast's cuts per minute (Tubefilter) and the production memo's minute marks, Dhar Mann's runtimes, Iman Gadzhi-style animation density and Reddit-story word counts. Everything else is an estimate. **Calibrate** a preset before locking it for a client, using `/style` StyleCards (vidIQ/StyleLab), measured reference clips Klaus supplies, or `scripts/qc_frames.py` plus shot detection on licensed references.

## Viral creator formats
### mrbeast
Thumbnail-matched cold open; stakes in the first 5 s; stair-step escalation; re-engagement spikes around 3:00 and 6:00; abrupt ending. 2023: 38 cuts/min (ASL ~1.6 s). 2024 "let scenes breathe": 23 cuts/min (ASL ~2.6 s). Evidence: high for structure.
- https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/
- https://tubefilter.com/2024/03/04/mrbeast-editing-style-number-of-cuts-per-video/
- https://passionfru.it/youtube-editing-mrbeast-54202/

### ryan-trahan
Constraint challenge told as a serial; named recurring segments; running counters; real re-filmed moments; shot mostly on iPhone.
- https://news.thepublishpress.com/p/inside-ryan-trahan-s-50-day-youtube-marathon-d08f84877f8a7a62
- https://colinandsamir.com/resources/how-ryan-trahan-changed-youtube-with-0-01
- https://blog.youtube/creator-and-artist-stories/between-two-creators-ryan-trahan-benoftheweek/

### ali-abdaal
Kinetic text beside the speaker with yellow keywords; paper tear transitions; framework cards; low lo-fi bed; ASL 2–5 s.
- https://www.choppity.com/tools/recreate-video-editing-style/ali-abdaal/
- https://www.submagic.co/blog/make-captions-like-ali-abdaal

### iman-gadzhi
Luxury B-roll under VO; angle switch plus subtle zoom on key phrases; accent-colour UI and graph pops; the intro carries 2–5× the body's animation density.
- https://sozai.app/transcript/ai-edit-iman-gadzhi-videos/index.md
- https://www.opus.pro/de-de/blog/how-to-edit-instagram-reels-exactly-like-iman-ghadzi

### dhar-mann
Injustice hook, escalation, reveal, consequence, then the moral stated to camera. Shorts run 2–3 min, with 4–5 test versions per short.
- https://bdnews24.com/lifestyle/the-moral-philosopher-of-youtube
- https://www.builtinla.com/job/head-shorts-testing/11337585
- https://en.wikipedia.org/wiki/Dhar_Mann

### zach-king
Invisible cuts (whip, lens block, object pass); single-take feel; SFX sells the reveal; loopable endings.
- https://en.wikipedia.org/wiki/Zach_King
- https://www.adobe.com/creativecloud/video/hub/ideas/what-is-an-invisible-cut-in-film.html

### khaby-lame
Stitch of an over-complicated hack; deadpan stare; the simple fix; long silent hold; palms-up gesture.
- https://krdo.com/news/national-world/cnn-world/2021/10/02/hes-the-most-popular-man-on-tiktok-and-he-doesnt-say-a-word/
- https://shapes.inc/fandom/khaby-lame/content-style

### podcast-clips
Hook claim first; switching between speaker-fill and stacked split; bold karaoke captions; 30–90 s.
- https://www.bytecap.io/blog/how-to-turn-podcast-into-shorts-reels-tiktoks-2026
- https://quso.ai/blog/how-to-edit-podcast-shorts-like-a-pro.html
- https://www.opus.pro/de-de/blog/how-to-edit-podcast-shorts-like-a-pro-using-opus-clip-pc-mac

### street-interview
One fixed question asked every time; persistent title bar; natural sound. SubwayTakes shot 15 episodes in a day.
- https://en.wikipedia.org/wiki/SubwayTakes
- https://en.wikipedia.org/wiki/Daniel_Mac
- https://www.thedrive.com/news/37511/viral-tiktok-star-asks-supercar-owners-the-big-question-what-do-you-do-for-a-living

### storytime
Script of 150–200 words; story 40–50 s plus a 5–10 s ending; word-by-word captions. The studio rule: original scripts only, over brand-owned B-roll.
- https://ghostshorts.com/blog/how-to-make-reddit-story-videos-for-tiktok-2026
- https://www.kapwing.com/resources/how-to-make-tiktok-videos-from-reddit-stories/

## Professional / cinematic / commercial
### apple
Macro edge-light sweep along the chassis; word-by-word kinetic claim synced to the beat; colourway "paint" transitions; hard cut to a silent hero hold plus logo. Motion-control robots are confirmed. Evidence: medium.
- https://9to5mac.com/2022/09/09/behind-the-scenes-iphone-14-ad/
- https://motion.so/learn/apple-style-product-launch-video
- https://www.moonb.io/blog/kinetic-typography

### nike
Each VO line cuts literally to the athlete who embodies it; escalation from unknown athletes to icons; the narrator is revealed on camera near the end; black tagline card. Evidence: medium.
- https://shots.net/news/view/96371-nike-dream-crazy
- https://www.thedrum.com/news/2018/09/05/colin-kaepernick-narrates-and-stars-nike-s-dream-crazy-film
- https://effie.org/case_studies/case/BOTB_2021_E-600-760

### gymshark
Routine and repetition montage (66-day habit series); family or mentor VO over training; creator-led humour; dark "Blackout" palette for sales.
- https://shots.net/news/view/ryan-garcia-returns-with-gymshark
- https://blog.audionetwork.com/the-edit/advertising/best-gymshark-ads
- https://www.kolsquare.com/en/blog/gymshark-the-marketing-strategy-behind-the-fast-growing-brand

### johnny-harris-vox
Textured 3D globe zooming down to a region; archival photos sliding in with blur and projector SFX; highlighted document reveals; host whiteboard sketches (GEOlayers / After Effects).
- https://aescripts.com/learn/how-johnny-harris-makes-maps/
- https://rndr.beehiiv.com/p/5-visuals-next-video-ead0
- https://www.journalism.co.uk/how-a-vox-reporter-uses-social-audiences-to-inspire-his-latest-video-series/

### kurzgesagt
VO-first timing; flat 2D plus 3D; zoom-across-scales transitions; recurring bird characters; custom score.
- https://kurzgesagt.org/youtube/

### mckinnon
Speed ramps (fast to slow-mo on the action peak); whip pans; match cuts on shape or motion; hand and object wipes; sensory hooks.
- https://async.com/blog/who-is-peter-mckinnon/
- https://www.nikon.co.uk/en_GB/learn-and-explore/magazine/tips-and-tricks/cut-to-the-chase-10-tricks-to-add-pace-and-energy-to-your-edits

### neistat
Jump cuts across a locked-off frame to compress time; cutting off mid-sentence; whip-pan location changes; timelapse bridges; lens-slap transitions.
- https://indepthcine.com/videos/casey-neistat
- https://artlist.io/blog/editing-storytelling-techniques-casey-neistat/

### doc-trailer
Sound bite over black, then a hard cut to image; title cards between escalating bites; accelerating montage on a riser; silence; a final "button" line; title and date.
- https://jonnyelwyn.co.uk/film-and-video-editing/how-to-edit-a-movie-trailer/
- https://nofilmschool.com/the-perfect-neighbor-lieberman

### liquid-death
Straight-faced set-up, then absurd escalation; "it's just water" deflation tag; metal sting on the logo; parody of a recognisable ad trope.
- https://www.marketingdive.com/news/liquid-death-creative-beverage-category-brand-interview/723142/
- https://www.shopify.com/blog/liquid-death-comedy-marketing-billion-dollar-brand

### duolingo
The mascot reacts to news within hours; trending audio; shoots take 15 min to 2 h; comment replies are made as Duo videos.
- https://digiday.com/marketing/how-duolingo-is-using-its-unhinged-content-with-duo-the-owl-to-make-people-laugh-on-tiktok/
- https://www.thedrum.com/news/2025/02/25/duolingo-s-tiktok-mastermind-its-unhinged-social-strategy-and-killing-its-mascot
- Scrub Daddy (brand-as-creator): https://www.ypulse.com/newsfeed/2022/06/23/scrub-daddys-self-aware-tiktok-videos-are-continuing-their-appeal-to-gen-z-humor/

### clinic-films
Clinician-to-camera sincerity; close-ups of hands-on guidance; return to daily movement with no outcome claims; calm logo resolve. Examples: Horder Healthcare "Hip & Knee", AKFA Medline, CSP "Never Too Late". Evidence: low–medium. Ask Klaus for SG references he admires.
- https://www.egta.com/?p=22255
- https://acpopc.csp.org.uk/node/1256466

### b2b-founder
Headline bar plus burned captions (LinkedIn autoplays muted); alternating 100%/115% punch-ins; data callouts; 1:1 or 4:5; under 2 min.
- https://www.opus.pro/blog/ideal-linkedin-video-length-format-for-retention
- https://www.kapwing.com/resources/linkedin-video-size-guide-aspect-ratios-resolution-length-and-best-practices-3/

### night-owl-cinematics
Existing StyleCard in Supabase `style_cards`: Singapore branded sketch comedy, Singlish/Mandarin, listicle sketches in letterbox text bars.

## Niche experts, SEA, ad formats
### adam-meakins
The myth is stated, then bluntly rejected; sarcasm; a simple "do this instead" loading demo. Brand versions drop the profanity.
- https://www.physitrack.com/insights/top-physical-therapy-influencers-instagram

### prehab-guys
The exercise demo is the A-roll; cue overlays; progression and regression ladders; one consistent template across 4,000+ videos.
- https://library.theprehabguys.com/enterprise/professional/

### doctor-mike
Pause-the-clip reaction; freeze-frame verdict; diagram overlays; public self-correction.
- https://en.wikipedia.org/wiki/Doctor_Mike
- https://www.ama-assn.org/delivering-care/patient-support-advocacy/dr-mike-using-social-media-combat-medical-misinformation

### kayla-itsines
Circuit cards (exercise plus reps); beat-matched cuts between exercises; short-session promise. Avoid her historical before/after framing.
- https://sweat.com/blogs/community/kayla-itsines-fitness-journey

### sam-sulek
Average ~34 min; no B-roll, captions or music; car-ride intro. Evidence: medium-high (vidIQ stats).
- https://vidiq.com/blog/post/sam-sulek-breaks-youtube-rules-goes-viral/

### whitney-simmons
Pastel grade; music-first montages; diary VO; minimal lowercase text. Evidence: low.
- https://vloggingpro.com/setups/whitney-simmons/

### nick-digiovanni
About 85% of his views come from Shorts; extreme-scale premise; beat-cut ASMR montage; the bite happens in silence.
- https://www.tubefilter.com/2025/01/06/nicks-kitchen-nick-digiovanni/

### khairul-aming
Catchphrase opener; "30 Hari 30 Resipi" Ramadan series posted daily at noon; RM100k+ of gear; record livestream sales on TikTok Shop.
- https://www.bernama.com/en/general/news.php?id=2397703
- https://www.malaymail.com/news/malaysia/2026/02/21/khairul-aming-sets-new-tiktok-shop-malaysia-livestream-record-with-rm23m-in-one-day/209910

### mkbhd
RED cameras plus a motion-control robot; matte dark set with a red accent; balanced "is it worth it" verdict.
- https://rosetta.to/u/mkbhd/the-mkbhd-gear-tour-2019

### mikayla-nogueira
Product held to the lens; catchphrases. The 2023 mascara controversy is the cautionary tale: disclose #ad and never alter results.
- https://www.bostonglobe.com/2021/04/11/lifestyle/how-massachusetts-makeup-artist-built-tiktok-empire

### ugc-ads
Hook stacking (re-hook every 5–15 s); problem, product, proof, CTA; hook-matrix testing; refresh hooks every 7–10 days.
- https://ugcsocial.substack.com/p/hook-stacking-the-secret-to-longer
- https://www.gotolstoy.com/blog/how-to-structure-ugc-ads

### puspa-wafiy
Malay drama parodies; one-person multi-character skits; music stops dead on the punchline.
- https://www.kosmo.com.my/?p=623273

### pelvicsanity
Pelvis model or diagram instead of bodies; normalising language; guidance on when to see a pelvic PT. Founders: Nicole and Jesse Cozean.
- https://buzzsprout.com/1009216/6716989
