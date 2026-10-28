# Creator clips, reposts and outreach

Klaus, 2026-10-28: "needs more real people's clips to get branded footage and collab potential plus creator tagging or outreach… treat remix, stitch, duet and reusing as the same workflow, I will take care of backend and copyright."
Real creators' footage makes brand posts feel real, and every clip we use is a creator we can tag and pitch. Klaus handles rights; the studio (Claude) collects, tags and tracks.

## One workflow for every reuse (repost, Remix, Stitch, Duet, clip in our edit)
1. **Find:** creators in the brand's niche and market (IG/TikTok search, vidIQ outliers, our tagged mentions, customers who posted us). Many viral clips are reposts: credit the **original** creator (Claude finds them when collecting clips).
2. **Use:** `editor.py collab add <url> --creator @h --use repost|remix|stitch|duet|clip [--browser firefox]`.
   - The clip lands in the collab B-roll folder with `<clip>.rights.json`, and is indexed so `broll-match` can use it in posts and ads.
   - **Nothing is written on screen** (Klaus, 2026-10-28: on-screen credits make the content ugly). Credit lives in the caption tag only. With no `--creator`, the tracker says "find the original creator".
   - For in-app Remix/Stitch/Duet, post it in the app; logging it the same way keeps the tracker complete.
3. **Tag:** @h in the caption and first comment; invite them as an Instagram **Collab** post (it shows on both feeds); tag on TikTok.
4. **Reach out:** `editor.py collab dm @h --ask shoutout` (thank-you + collab pitch), `--ask collab` (an original joint post), `--ask ads` (run it from their handle as a Partnership/Spark ad).
5. **Track:** `marketing/collabs/<brand>.csv` (date, creator, source, use, file, status, next step); `editor.py collab list` prints it; `/review` reads it to see which creators drive reach and who to pitch next.

## Compliance that still applies (market law, not copyright)
- **SG health brands:** a creator clip is never a testimonial: no patient stories, outcomes or "it fixed my back" lines (compliance-sg.md).
- **Paid creator partnerships** carry the platform's paid-partnership label (VN Law 75/2025, ASAS).
- No clips featuring minors.
