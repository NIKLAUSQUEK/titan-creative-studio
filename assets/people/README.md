# People photos (founder-friendly)

Your own photos make the most human, on-brand slides. Drop them in, run one command, and use them by tag.

## Folders (one per person)
```
assets/people/klaus/
  headshots/   clean upright face + shoulders, plain-ish background (best for cutouts and the slide header)
  stage/       speaking, panels, workshops
  office/      working, whiteboard, client calls, the team
  lifestyle/   gym, coffee, travel: personal-brand moments
  events/      meetups, awards, launches
  screens/     real screenshots: dashboards, workflows, results (crop anything private)
```
- **Name files with what's in them.** Tags come from folder and file names, e.g. `office/whiteboard-scoping-call-client-x.jpg` → `lib:whiteboard scoping`.
- **Header headshot:** `headshots/headshot.jpg` (or set `author.photo` in `brands/<brand>.md`).
- **Phone photos are fine.** Natural light and a real setting beat anything stock or AI.

## Then
```
python tools/editor/editor.py assets scan --brand titan-ai             # index new photos (assets/library/index.csv)
python tools/editor/editor.py assets cutout assets/people/klaus/headshots/headshot.jpg   # background removed -> *_cutout.png (local, free)
```
On a slide: `"image": "lib:klaus whiteboard"` or a path. Layouts: `photo`, `split`, `inset`, `screen`, `polaroid`, `cutout`.

## Consent
`people` and `consent` columns in `assets/library/index.csv`:
- Photos of you are marked consent=yes automatically.
- Anyone else in the frame (team, clients, event attendees) needs consent=yes before the photo can be used.
- Patients: never, for any health brand (SG health rules).
