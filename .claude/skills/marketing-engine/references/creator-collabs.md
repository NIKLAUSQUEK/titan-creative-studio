# Creator clips, collabs and outreach

Klaus, 2026-10-28: "needs more real people's clips to get branded footage and collab potential plus creator tagging or outreach."
Real creators' footage makes brand posts feel real, and every clip we use is a relationship we can start. This file is the workflow; `editor.py collab` is the tool.

## 1. Three ways to use someone's clip

| Route | When | Permission | Paid ads | Tool |
|---|---|---|---|---|
| **In-app Remix / Stitch / Duet / Collab reshare** | fastest; reacting to or riding a creator's post | none: the platform's terms cover it (only if the creator left Remix/Stitch on) | no | `editor.py collab remix <url> --creator @h` logs it |
| **Clip in our own edit** (downloaded, cut into a brand reel or carousel) | branded footage, montages, "real people" proof | the creator's yes; a DM screenshot counts | no, unless the yes covers paid use | `collab dm` to ask, then `collab add --permission dm` |
| **Creator content as an ad** | a creator video outperforms our own | written paid-use permission and usually a fee | yes | Meta **Partnership Ads** / TikTok **Spark Ads** code, or `collab add --ads` |

Downloading someone's video and posting it on a brand account without their yes risks copyright takedowns and account strikes, and it burns the relationship we want. Asking first is what turns the clip into a collab.

## 2. The loop (every clip becomes outreach)
1. **Find:** creators in the brand's niche and market (IG/TikTok search, vidIQ outliers, our own tagged mentions, customers who posted us).
2. **Ask:** `editor.py collab dm @h --ask feature --clip <url>` (or `--ask ads`, `--ask collab`). Send from the brand account. Keep the screenshot of the yes.
3. **Use:** `editor.py collab add <url> --creator @h --permission dm [--ads] [--browser firefox]`.
   - The clip lands in the collab B-roll folder with `<clip>.rights.json`.
   - The edit burns "via @h" on screen while the clip plays.
   - `broll-match` can now pick it. QC blocks it from ads unless `--ads`.
4. **Tag:** @h in the caption and the first comment; invite as an Instagram **Collab** post (it shows on both feeds); tag on TikTok.
5. **Close the loop:** send them the final cut, reshare their story, and log the result. Creators whose clip performed get `--ask collab` for an original piece.
6. **Track:** `marketing/collabs/<brand>.csv` (date, creator, source, use, permission, ads, status, next step). `editor.py collab list` prints it. `/review` reads it to see which creators drive reach.

## 3. Rules
- Real people only with their yes, except in-app Remix/Stitch/Duet.
- **Credit every time:** on screen ("via @handle") + caption tag. Never crop out watermarks or usernames.
- **No paid use without paid-use permission.** Prefer Partnership/Spark codes, so the ad runs from their handle and they see the numbers.
- **Health brands (SG):** a creator clip is never a testimonial. No patient stories, outcomes or "it fixed my back" lines (compliance-sg.md). Creators show the place, the vibe or the process, never results.
- **Minors:** never use clips featuring minors.
- **Brands that pay creators** disclose it (#ad / paid partnership label) per platform and ASAS rules.

## 4. DM templates (the tool fills them in)
- **feature:** ask to use a few seconds with an on-screen credit and tag, offering to send the edit first.
- **ads:** ask to run their video as a Partnership/Spark ad for N weeks, and ask their rate.
- **collab:** pitch an original Collab post on both feeds, filmed by them or us.
Write them in the brand's voice (brand file §5). For VN creators, write in Vietnamese first.
