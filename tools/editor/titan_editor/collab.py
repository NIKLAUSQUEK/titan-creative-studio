"""Real people's clips in our edits: one workflow for reposts, Remix, Stitch, Duet and reused clips, with credit and outreach.
Klaus handles the backend and copyright (2026-10-28); this tool only credits, tags and tracks.

  editor.py collab add URL|FILE [--creator @handle] [--use clip|repost|remix|stitch|duet] [--browser firefox]
      downloads the clip into the collab B-roll folder, writes <clip>.rights.json (who to tag; nothing is burned on screen),
      logs it in marketing/collabs/<brand>.csv and indexes it so broll-match can use it
  editor.py collab dm @handle --ask shoutout|ads|collab [--clip URL]   outreach text after we use their clip
  editor.py collab list
"""
import csv, json, time
from pathlib import Path
from types import SimpleNamespace

from .common import REPO, log, studio, wjson
from .broll import default_index_dir, cmd_index

FIELDS = ["date", "brand", "creator", "source", "use", "file", "status", "next_step"]

ASKS = {
    "shoutout": ("Hey {h}! {brand} here. Your video ({clip}) was too good not to share, so we featured it with a credit and a tag (@{hn}). "
                 "Thank you! If you're up for it, we'd love to do a proper collab next: you film your way, it goes on both feeds."),
    "ads": ("Hi {h}, {brand} here. We'd love to run your video ({clip}) as a paid ad. You'd stay credited, and we'd boost it from "
            "your account via a Partnership Ad (Instagram) or Spark Ads code (TikTok) so the views count for you too. "
            "We pay a usage fee for {weeks} weeks: what's your rate? We can also brief a fresh version if you prefer."),
    "collab": ("Hey {h}! Big fan of your content, especially {clip}. I'm with {brand}, and our audience would love a collab with you: "
               "one Collab post on both feeds (we film or you film, your style), credited both ways. Open to a quick chat or a rate card?"),
}


def tracker(brand):
    return REPO / "marketing" / "collabs" / f"{brand}.csv"


def log_row(brand, row):
    p = tracker(brand)
    p.parent.mkdir(parents=True, exist_ok=True)
    new = not p.exists()
    with p.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, FIELDS)
        if new:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in FIELDS})
    return p


def handle(h):
    h = (h or "").strip()
    return h if h.startswith("@") else "@" + h


def cmd_collab(a):
    brand = a.brand or studio("active_brand") or "brand"
    h = handle(a.creator) if a.creator else ""
    if a.action == "list":
        p = tracker(brand)
        print(p.read_text(encoding="utf-8") if p.exists() else f"no collab clips logged for {brand} yet ({p})")
        return 0
    if a.action == "dm":
        h = handle(a.target or a.creator)
        print(ASKS[a.ask].format(h=h, hn=h.lstrip("@"), brand=brand.replace("-", " ").title(), clip=a.clip or "your recent video", weeks=a.weeks))
        return 0
    if not a.target:
        raise SystemExit("collab add: pass the clip (URL or file); add --creator @handle so it gets credited and tagged")
    today = time.strftime("%Y-%m-%d")
    root = Path(a.root) if a.root else Path(default_index_dir()) / "collab" / brand
    d = root / (h.lstrip("@") or "unknown")
    src = Path(a.target)
    if src.exists():
        d.mkdir(parents=True, exist_ok=True)
        f = d / src.name
        if f.resolve() != src.resolve():
            f.write_bytes(src.read_bytes())
    else:
        from .study import fetch
        f = fetch(a.target, d, a.browser)
    rights = {"creator": h, "credit": "", "licence": "creator-clip", "use": a.use,
              "source": a.target if not src.exists() else "", "ads": True, "date": today}
    wjson(f.with_name(f.name + ".rights.json"), rights)
    nxt = f"tag {h} in the caption + invite as Collab; then `collab dm {h} --ask shoutout`" if h else "find the original creator, then re-run with --creator"
    p = log_row(brand, {"date": today, "brand": brand, "creator": h, "source": a.target, "use": a.use, "file": str(f),
                        "status": "in library", "next_step": nxt})
    log(f"saved {f} (+ rights.json; tag {h or 'the original creator'} in the caption, nothing on screen); logged in {p}")
    cmd_index(SimpleNamespace(roots=[str(root)], index_dir=a.index_dir or str(default_index_dir()), frames=4, min_dur=0.8,
                              images=False, creator_brain_work=None, no_faces=False))
    return 0
