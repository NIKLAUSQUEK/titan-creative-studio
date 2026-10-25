# Brand image library

`index.csv` is the searchable index (path, tags, people, consent, source, licence, attribution, brand). It's built by `editor.py assets scan` (own photos) and `editor.py assets fetch "query"` (free-licensed downloads).

## Where images come from, in order
1. **Own photos**
   - `assets/people/<who>/` (founder, staff)
   - `assets/library/<brand>/` (product, premises, equipment)
   - `assets/brands/<brand>/` (logos, brand graphics)
2. **Free-licensed downloads (Openverse, no key):**
   - CC0, Public Domain Mark and CC BY only, by default. CC BY-SA is opt-in, because text over the image would make our slide ShareAlike. NC and ND licences are never used.
   - Licence and credit are recorded automatically. Credits print on the slide and in `CREDITS.md`.
   - **No identifiable strangers in brand ads.** CC licences don't cover a person's portrait rights. Use downloads for places, objects, textures and hands.
3. **AI-generated (`gen:<prompt>`):**
   - The cards engine renders a labelled placeholder and writes `ASSETS_NEEDED.md` with ready prompts.
   - Free: Nano Banana in the Gemini app / Google Flow images. Premium: Higgsfield after a cost quote.
   - Never AI-generate real people, patients or "results". Label AI imagery at /publish.
