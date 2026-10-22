---
name: creator-brain
description: Creator Brain for any founder, spokesperson or creator (default: Klaus; whoever .studio/active_brain names) - life-story interviewing, journaling, story mining and story writing for thought-leadership content. Use when anyone wants to journal, tell or find a story, write a hook/script/caption/essay/post in their voice, build a visual life storyboard, define values/beliefs/principles, write founder stories, or create a fictional parable that teaches one of their principles. Works for short form (reels, carousels, captions) and long form (essays, YouTube, podcasts, films).
---

# Creator Brain

Works for any person: `<who>` = `.studio/active_brain` (Klaus = `klaus`; new people via `/onboard` or by copying `brains/_template/`). Two jobs: **mine** true stories from that person's life (and consenting clients), and **write** them, or fiction built on their principles, into content that makes people feel something and remember a lesson.

## Files
- `brains/<who>/identity/profile.md` - who Klaus is (origin, culture, values, beliefs, principles, wisdom, voice, audiences, no-go zones). Read it before writing anything.
- `brains/<who>/timeline/eras.md` - eras, media index, key moments.
- `brains/<who>/journal/` - raw interview answers. `brains/<who>/stories/` - story cards (`_TEMPLATE.md`).
- `references/question-bank.md` - provoking questions by era and theme.
- `references/story-engine.md` - goals, trope stances, hook formulas, structures, emotive language, short vs long form.
- `references/corpus.md` - how to pull model passages from Supabase `titan_corpus` (5,472 tagged passages from great writers, screenplays, ad scripts and narrative theory).

## Mode 1 - Interview (biographer agent, `/journal`)
1. Pick the era/theme Klaus asks for, or the emptiest era in `eras.md`.
2. Ask 3-5 questions at a time from the question bank: one easy warm-up, then go deeper. Follow the emotion, not the list: when an answer has heat (a name, a smell, "I never told anyone"), ask "what happened next?" / "what did you feel in your body?" / "what did you decide about yourself that day?".
3. Ask for media every session: "Do you have a photo or video from then? Drop it in Drive → Creator Brain/media/<era>."
4. Save verbatim answers to `brains/<who>/journal/YYYY-MM-DD-<era>.md`. Never polish his words in the journal.
5. Mine: create/extend story cards, and add values/beliefs/principles/wisdom lines to `profile.md` marked `[draft]` until Klaus confirms.
Safety: if a memory involves trauma, abuse or self-harm, slow down, don't push, offer to skip, and never turn it into content without explicit consent. Mention professional support if distress shows.

## Mode 2 - Write (story-writer agent, `/story`)
1. Lock the brief: **goal** (wise / expert / trust / sell / founder / entertain), audience, platform + format + length, story source (card id, theme to mine, or fiction), and CTA if any.
2. Choose the trope stance and the structure (story-engine.md). State the one-line lesson before writing.
3. Pull 3-6 model passages from the corpus that match the emotional beat and technique; study the move (subtext, foreshadowing, in medias res…), never copy text.
4. Write: 5 hooks first (Klaus picks or you rank), then the piece. Short form: hook ≤ 2 s / 12 words, one idea, the turn by 60%, wisdom line, CTA. Long form: cold open, stakes, 3 escalations, the low point, the turn, the lesson, the wisdom note, the callback.
5. Self-check: true to profile? one lesson? concrete sensory detail? earned emotion (shown, not told)? contrarian without being cruel? the brand's compliance pack for sell pieces? fiction labelled?
6. Output version A plus up to two variants (different trope stance or audience). Hand visuals to the studio (`/ad`, `/brief`, or `/storyboard`).

## Mode 3 - Visual life storyboard (`/storyboard <era>`)
For each key moment in `eras.md`: a card with the real photo reference, the moment, the emotion, the VO line, and the shot (framing, light, era-accurate wardrobe/props). Real photos are references for GPT Image 2.5 / Nano Banana (image_references) or for a Soul trained on Klaus; children in photos are depicted only in non-sensitive, family-safe moments. Then the normal studio gates: approve stills (Gate 4) → cheap draft → final.
