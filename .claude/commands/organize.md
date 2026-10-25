Organise Klaus's big photo and video library with **Immich**, an open-source, self-hosted photo platform that runs on his PC. A thin studio bridge (`tools/editor/titan_editor/immich_bridge.py`) adds consent rules, sensitive tags, best-shot ranking and the export into cards and B-roll. The argument is a request such as `setup`, `pick <query> [@person]`, `sync`, `tag-sensitive`, or `consent <name> yes`.

## Why Immich and not our own script
Klaus's library lives on his PC and Drive, not in this repo. Our own CLIP script scored 83% on categories, and the research (`research/sources-photo-library.md`) found Immich does it better:
- benchmarked SigLIP2 smart search (about 85–86% recall)
- InsightFace face recognition, where you name a person once
- duplicate detection
- timeline and map
- OCR
- phone backup
- a REST API

His folders are mounted **read-only**, so nothing is ever moved, edited or deleted.

## Setup (once, on Klaus's PC, about 1–2 h of hands-on time, then indexing overnight)
1. **Google Drive.** Switch Drive for desktop to *Mirror files* (Settings → My Drive), e.g. into `D:\GDriveMirror`, or copy the photo folders to a local disk. Docker can't read the streamed `G:` drive reliably.
2. **Install:** run `tools\immich\Setup-Immich.ps1 -Photos "D:\GDriveMirror\My Drive\Photos","D:\Phone backup" -Email <his email>`. It:
   - installs or checks Docker Desktop
   - starts Immich v3.3.5 (with the GPU image if there's an NVIDIA card)
   - picks the smart-search model: `ViT-B-16-SigLIP2__webli` on CPU, `ViT-SO400M-16-SigLIP2-384__webli` on GPU
   - creates a read-scoped API key, saved in `%LOCALAPPDATA%\TitanEditor\immich.json` (never in the repo)
   - adds the read-only library
   - starts indexing
3. **Name faces.** Next day, either Klaus does it at http://localhost:2283 → Explore → People (name his face `Klaus`, merge strays), or he pastes `tools/immich/COWORK_PROMPT.md` into Claude Cowork with Claude in Chrome. Cowork then names him, asks before naming anyone else (with consent), builds the "Studio Picks" album and walks him through the Sensitive review albums. It never deletes anything.
4. **Optional:** install the Immich phone app for automatic backup.

## Studio use
- `editor.py immich pick "speaking on stage" --person klaus --out projects/<p>/picks`
  - Immich smart search, filtered to Klaus.
  - Sensitive or unconsented items are dropped.
  - One image per duplicate group.
  - Results are re-ranked by sharpness and exposure.
  - Output: a contact sheet plus local paths. **LOOK** at the sheet before using.
- On cards: `"image": "immich:speaking on stage@klaus"`, or curate first and use `lib:`.
- `editor.py immich sync-library`: Klaus's hearts and the "Studio Picks" album go into `assets/library/index.csv` (`lib:<tags>`).
- `editor.py immich tag-sensitive`: run nightly or weekly. Candidates for children, documents and patients go into the review albums **"⚠ Sensitive – minors / documents / patients"**, and the studio never uses anything in them. Klaus removes a fine photo from the album and it is never re-added. These are albums rather than tags because Immich stores tags in XMP files next to the photo, and those can't be written on read-only folders.
- `editor.py immich consent <name> yes`: anyone other than Klaus is unusable until this is set.
- `editor.py immich queries`: the saved studio searches (speaking, meeting, headshot, screen, gym…).
- **Video moments:** Immich indexes one poster frame per video. To find the exact second inside a clip, use the B-roll index (`editor.py broll-index` + `broll-search`), which samples several frames.

## Rules
- Immich runs locally; keep it off the public internet (no port forwarding; use Tailscale only if remote access is needed).
- Patients are never used for health brands.
- People photos, the API key and `tools/immich/.env` stay out of git.
- Nothing is uploaded to third-party services.

## Google Drive + Google Photos (one script, no Mirror needed)
- **Drive folders:** `tools\immich\Import-Google.ps1 -DriveFolders "G:\My Drive\Photos"` copies them to `D:\Photos\Drive` with resumable robocopy. Then use that folder with `Setup-Immich.ps1 -Photos`.
- **Google Photos:** its API can't read the library, so use takeout.google.com: choose Google Photos only, .zip, 50 GB, and download to `D:\Takeout`. Create an Immich API key with all permissions (Account Settings → API Keys). Then run `Import-Google.ps1 -Takeout "D:\Takeout"`. It downloads immich-go (open source), asks for the key in a hidden prompt that is never saved, and imports with dates, albums, GPS and de-duplication.
- Uploaded copies live in Immich's storage, so set up with `-DataDir "D:\ImmichData"` on a drive with room. Add `-DryRun` to preview either step.
