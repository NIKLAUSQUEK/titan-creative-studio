# Cowork prompt: name people and curate in Immich

Run this **after** `Setup-Immich.ps1` has finished and Immich has indexed overnight. Open the Claude desktop app → Cowork, with Claude in Chrome enabled. Paste everything inside the box. Have your Immich admin password ready; type it yourself when asked, and never put it in the prompt.

```
You are helping me (Niklaus "Klaus" Quek) finish setting up my self-hosted photo library, Immich, at http://localhost:2283, in my Chrome browser. Immich has already indexed my photos and videos. My folders are read-only, so nothing you do in Immich can change or delete my files. Still: never delete, trash, archive or "resolve duplicates" on anything, and never upload or share anything outside this computer.

Step 1 - Log in
Open http://localhost:2283. When the login page appears, stop and ask me to type the password myself. Don't read it, store it or repeat it.

Step 2 - Name me
- Go to Explore → People (or the People page). The largest face groups are usually me.
- To recognise me, compare them with my reference photos in this folder: <PASTE PATH, e.g. D:\GDriveMirror\My Drive\Photos\Headshots>. If no folder is given, show me the top 6 face groups as screenshots and ask which ones are me.
- Name my face group exactly: Klaus
- If I appear in more than one group (different years, glasses, beard), merge them into "Klaus" using Immich's merge option. Before each merge, show me both groups side by side and wait for my "yes".
- Open "Klaus" and scroll through it. Show me any photo that isn't me, and remove it from my group only after I confirm.

Step 3 - Other people (consent first)
- List the next 10 most frequent unnamed face groups as screenshots (no names).
- Ask me: who is this, and can the studio use their photos in marketing (yes/no)?
- Name only the people I identify, exactly as I spell them.
- Never name, guess or search for children, patients or strangers. Hide those face groups (People → hide) only if I say so.
- At the end, give me a list of "name - consent yes/no", so I can paste it into the studio.

Step 4 - Studio Picks album
- Use Immich's search bar (it understands plain English) to find my best photos for content, about 30 in total:
  - "Klaus speaking on stage"
  - "Klaus at a whiteboard"
  - "Klaus working on a laptop"
  - "professional headshot of Klaus"
  - "Klaus with clients or team in a meeting"
  - "Klaus at the gym"
- From each search, choose sharp, well-lit, flattering shots: eyes open, no motion blur, only one shot per near-identical burst.
- Skip anything with children, patients, documents or screens showing private information.
- Add the chosen photos to an album named exactly: Studio Picks (create it if it doesn't exist). Then show me the album as a grid, and remove any photo I veto.

Step 5 - Sensitive review albums
- Open the albums whose names start with "⚠ Sensitive" (minors / documents / patients), if they exist.
- Tell me how many photos each one holds and show me a grid.
- Don't remove anything yourself. Ask me which ones are fine, and remove only those from the album.

Step 6 - Report back
Give me a short summary:
- how many photos are in "Klaus"
- the people you named, with my consent answers
- how many photos are in Studio Picks
- what's in each Sensitive album
- anything that looked wrong (missing photos, offline files, Immich errors)

Rules: ask before any action you're unsure about, and work in small steps with screenshots so I can follow.
```

## Afterwards (Claude Code, or a terminal on the PC)
```
python tools\editor\editor.py immich consent "<name>" yes        # once for each person you said yes to
python tools\editor\editor.py immich sync-library --brand titan-ai
python tools\editor\editor.py immich pick "speaking on stage" --person klaus --out projects\test\picks
```

---

# Cowork prompt: download every Google Photos picture of me

Use this when your photos live in Google Photos and you only want the ones Google has already grouped under your face. It's much smaller than a full Takeout, and nothing in Google Photos is changed.

Before you start:
1. In Chrome, go to Settings → Downloads.
2. Set Location to a new folder, e.g. `C:\Photos\GooglePhotos-Klaus`, and turn **off** "Ask where to save each file".
3. Sign in to photos.google.com yourself.

```
You are helping me (Niklaus "Klaus" Quek) download the photos and videos of me from my own Google Photos, in my Chrome browser. Read-only job: never delete, archive, edit, share, move to album, remove from face group, or change any setting in Google Photos. Only select and download.

Step 1 - Open my face group
Go to photos.google.com → Search (or Explore) → People. Open the face group that is me (it may already be labelled with my name; if not, show me the top face groups as screenshots and ask which one is me). Tell me how many items it shows if Google displays a count.

Step 2 - Download in batches
Large selections can fail as one download, so work in batches of roughly 200-300 items (rule of thumb):
- In my face group, select items one date section at a time: hover a date heading and tick its checkbox (or click the first item, then Shift+click the last item of the batch).
- Click the ⋮ (More options) menu → Download (or press Shift+D). Google prepares a .zip; wait until Chrome shows it finished before starting the next batch.
- Clear the selection, then continue with the next date sections, oldest to newest or newest to oldest, until you reach the end of the group.
- Keep a running log for me: batch number, date range covered, items selected, zip file name.

Step 3 - Check
At the end, open Chrome's Downloads page (chrome://downloads) and confirm every zip completed (none "Failed"). Retry any failed batch once. Give me the log and the total item count, and list any date range you couldn't download.

Rules: if Google asks me to sign in or verify, stop and let me do it. Work in small steps with screenshots so I can follow.
```

## Afterwards (PowerShell)
Unzip every batch into one folder, then point Immich at it. The zips are only deleted after you've checked the photos:
```
Get-ChildItem "C:\Photos\GooglePhotos-Klaus\*.zip" | ForEach-Object { Expand-Archive $_.FullName -DestinationPath "C:\Photos\GooglePhotos-Klaus\photos" -Force }
(Get-ChildItem "C:\Photos\GooglePhotos-Klaus\photos" -Recurse -File).Count
.\tools\immich\Setup-Immich.ps1 -Photos "C:\Photos\GooglePhotos-Klaus\photos" -Email <your email>
```
These are already your best "Klaus" reference photos, so naming your face in Immich becomes a 1-minute job.
