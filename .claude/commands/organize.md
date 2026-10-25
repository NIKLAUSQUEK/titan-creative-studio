Organise a big photo and video library with AI (local, free; Claude only names events if Klaus asks). The argument is the folder(s), or one of: `name <#> <who>`, `apply <dest>`, `review`.

The library lives on Klaus's PC or Drive, not in this repo. So the run happens there:

1. **Klaus runs, in PowerShell from `tools/editor`:**
   ```
   .\Run-Editor.ps1 -Organize "G:\My Drive\Photos","D:\Phone backup"
   ```
   - The first run installs dependencies.
   - About 0.3–0.6 s per item on CPU, so 10,000 items takes roughly 1–1.5 h. It's much faster with an NVIDIA GPU.
   - It's resumable: re-runs only process new files.
   - Add `-Llm claude-cli` to name events: one contact sheet and one short call per event.
2. **What it does** (`tools/editor/titan_editor/organize.py`):
   - CLIP index (shared with B-roll search).
   - Dates from EXIF, then file names. Undated items go to "Undated"; they never get fake events.
   - Sharpness, exposure and resolution feed a quality score.
   - Faces are detected (YuNet) and grouped by person (SFace).
   - 16 categories: Headshots, Selfies, Speaking, Meetings, Working, Screens, Gym, Clinic, Food, Product, Events, Travel, Family, Documents, Memes, Pets.
   - Sensitive flags: children, documents and personal data, patients, and folder markers (`private`, `patients`, `kids`…).
   - Near-duplicates and bursts get one best pick each.
   - Events are split by time gaps.
   - Outputs `REVIEW.html` plus `catalog.csv` in `%LOCALAPPDATA%\TitanEditor\organize\`.
3. **Klaus names faces once:**
   - Open `people_sheet.jpg`. Cluster #1 is usually him.
   - Run `.\Run-Editor.ps1 -NameFace 1,klaus`. His consent is automatic.
   - Other people stay "unknown" until Klaus confirms consent with `editor.py organize name <#> <who> --consent yes`.
4. **Use it:**
   - Best picks of Klaus are exported to `assets/library/index.csv`. Cards can then use `"image": "lib:klaus speaking"`, B-roll search finds the same clips, and Creator Brain `/storyboard` and `/journal` can use event names and "story potential".
   - An optional browsable copy goes in `.\Run-Editor.ps1 -OrganizedTo "D:\Organised"`, laid out as Category\Event\file. Hardlinks on the same drive take no extra space; anywhere else it copies.
   - **Originals are never moved, renamed or deleted.**

**Rules**
- Sensitive items are excluded from library export, event naming and the organised tree. They sit in `_Review_sensitive` only with `--include-sensitive`.
- Flags are deliberately cautious (false positives are fine, misses are not). Klaus clears them by looking.
- Nothing leaves the PC except event contact sheets, and only when `-Llm claude-cli` is used. Never upload the library to a third-party service without Klaus asking.
- Patients are never used for health brands.
- People photos and the index stay out of git (`.gitignore`).
