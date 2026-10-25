# Code motion (tools/motion)

Animated graphic cards made in code (HTML + CSS + JS, rendered frame by frame by headless Chromium, encoded by ffmpeg). Exact text, numbers and brand colours. These are the panels AI video can't get right: step cards, stat counters, comparisons and kinetic quotes. Ref: research/refs-2026-10-25/ai-animation.md (anim2, anim3), editors-A.md (ed02, ed10), and millee.md's Remotion/HyperFrames workflow.

```
npm i playwright && npx playwright install chromium        # once (Run-Editor.ps1 -Motion does it)
node render.mjs templates/step-cards.html out.mp4 --data data.json --w 1080 --h 1920 --fps 30
```
The editor calls this itself for a B-roll entry `{"kind": "motion", "template": "step-cards", "data": {...}, "dur": 4, "mode": "full|split|side|pip"}`, or use `editor.py motion <template> --data file.json`.

| Template | Use | DATA keys |
|---|---|---|
| step-cards | "Step 1. Set it up" cards, bullets type on, progress dots (millee / neon-card founder edits) | theme{bg,ink,accent,card}, steps[{label,kicker,title,icon,bullets[],dur}], typing |
| stat-counter | a big number counts up, with a bar and a source line (study receipts, @dr.longevity-style) | value, prefix, suffix, decimals, pre, post, source, dur, count_s |
| compare-loop | "Same X. Only one added Y." Two columns grow under a month ticker, then a typed end line; loops (anim3) | ticker, steps, step_s, a{label,start,add}, b{...}, unit, end |
| kinetic-quote | serif words rise and unblur one by one, with an *italic accent* word, an Exhibit tag and a slow push (getclayhook) | tag, text (wrap the accent word in *stars*), sub, word_s, hold |

Rules: each template exposes `window.seek(t)` and `window.DURATION`; never use clocks or requestAnimationFrame. Design on a 1080-wide stage; the renderer zooms it to any size. Fonts come from tools/editor/fonts (OFL). Stats need a `source`.
To add a template, copy one and keep the seek(t) contract.
