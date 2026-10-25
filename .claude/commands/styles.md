Style home. Show, find or offer styles from every family: edit presets, script/voice styles, animation and faceless styles, carousel archetypes, LinkedIn formats and creator StyleCards. Argument: nothing (show the menu), a style or creator name, or a goal.

1. **No argument.** Show the families with their counts, then the top picks for the active brand. Do this by running `python scripts/styles.py offer --brand $(cat .studio/active_brand) --goal "general"`. Point to `styles/STYLE_MENU.md` for the full menu.
2. **A name or alias** (for example "hormozi", "stickman", "adam meakins", "myth vs fact", "kurzgesagt"). Run `python scripts/styles.py show "$ARGUMENTS"`. Present the style as a one-tap card with these fields:
   - what it is
   - how we make it (its route: editor preset, explainer skill preset, Seedance/Kling key or the cards engine)
   - the fill-in template or style key
   - compliance notes for the active brand
   - what it pairs with (script + edit + animation + carousel)

   For a real creator, also run `/style <name>` to get the measured StyleCard.
3. **A goal** (for example "explain AI agents on LinkedIn" or "faceless back-pain explainer for TikTok"). Run `python scripts/styles.py offer --brand <active> --platform <p> --goal "$ARGUMENTS"`. Give 3 numbered options per relevant family, with one line each on why it fits, and mark one as Recommended. Klaus taps a number.
4. **After Klaus picks**, route the request:
   - edit → `/edit` with that `--preset`
   - script → `/story` or `/ad` with that template as the structure
   - animation → its route (stickman/whiteboard/flat → higgsfield-video-explainer, after resolving the live preset via `get_explainer_presets`; 3D/anime/clay → Nano Banana key + Seedance/Kling; kinetic/data → the cards engine or HyperFrames)
   - carousel or LinkedIn document → write the cards JSON, then run `python tools/editor/editor.py cards <spec> --aspect 4:5 --brand <b>`, then LOOK at the contact sheet
   - LinkedIn → `/linkedin`

   Normal gates still apply: brief, spec approval, cost quote, draft at lowest quality, QC.

**Rules**
- Script styles borrow structure only. Never a creator's catchphrases, signature openers, voice clone or implied endorsement.
- A health brand never gets a style locked "not for health". The SG health pack applies to whatever is picked.
- Precedence: ledger > brand file > Klaus's brief > style.
- After editing any `styles/*.json` or preset, run `python scripts/styles.py build`.
