# Physio Spot v5 edit pipeline (rebuilt 2026-10-10 from Higgsfield job outputs; no v4 file needed)
1. text.py  - renders hook, captions, turn card, beige panel, conditions, brand as 1080x1920 RGBA PNGs (fonts: DejaVu Sans Bold, Cormorant Garamond Italic, Playfair Display Italic from google/fonts, Noto Color Emoji)
2. seg.sh   - cuts + normalises every shot (1080x1920, 30fps, 48k stereo); drop shot gets synthesized whoosh->boom at the zoom freeze (2.27s); Nik gets bulb flicker + 1.6s hold
3. ov.py    - concat, then windowed overlays (each PNG only lives for its own window - full-length looped layers time out), loudnorm -14 LUFS
Shot map (job ids): s01/s03 e3a730ce (0-1.2 / 2.9-5.75) | s02 413e6791 Benji, pause cut 0.95->2.1 | s04 249b4bfc | s05 62a531a8 1.25-3.0 | s06 bca0744b | s07 493b670b | s08 d914ec35 0-4.5 | s10 turn card | s11 Nik e548123c
