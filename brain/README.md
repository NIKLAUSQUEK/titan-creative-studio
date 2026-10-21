# Creator Brain: Klaus's life, voice and story bank

The source of truth for WHO is speaking in every piece of content. The studio (ads, films, photos) decides how it looks; the Brain decides what it means and why anyone should care.

```
brain/
  identity/profile.md      origin, cultural identity, values, beliefs, principles, wisdom, voice, audiences, no-go zones
  timeline/eras.md         life timeline by era (birth → now) + media index (photos/videos live in Drive; only pointers here)
  journal/YYYY-MM-DD-*.md  raw answers to provoking questions (Klaus or a client, with consent)
  stories/STORY-###.md     mined story cards: what happened → what it felt like → what it taught → hooks → formats
  storyboard/<era>.md      visual life storyboard: one card per moment, real photo refs → Higgsfield stills/video
```

## The loop
1. `/journal [era|theme]` → the **biographer** agent interviews (3-5 provoking questions at a time, from `.claude/skills/creator-brain/references/question-bank.md`), saves the raw answers to `journal/`, and asks for photos/videos from that era.
2. The biographer mines each entry into **story cards** (`stories/`) and updates `identity/profile.md` whenever a value, belief or principle surfaces.
3. `/story <goal> [story id | theme | "fiction"]` → the **story-writer** agent turns a card (or a fictional parable built on Klaus's principles) into short- or long-form content, using the story engine + the writing corpus (Supabase `titan_corpus`, 5,472 tagged passages).
4. `/storyboard <era>` → a visual life storyboard from the real photos (Gate 4 approval, then the normal studio draft → final flow).

## Rules
- Real memories stay true. Fiction is labelled `fiction` or `composite` on the card and is never presented as Klaus's or a client's real experience.
- Client stories need written consent, are de-identified by default, and follow the SG health-ad rules (no testimonials in ads).
- Photos/videos of Klaus as a child, family or clients: kept in Drive (private), referenced by link. Never committed while the GitHub repo is public.
- Klaus's own words beat polished words. Keep his phrasing in quotes on the card; the writer may sharpen, not replace.
