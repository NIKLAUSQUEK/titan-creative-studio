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
