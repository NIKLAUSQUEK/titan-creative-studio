"""Creator clips with credit: bring real people's footage into edits the right way, and turn every use into outreach.

  editor.py collab dm @handle --ask feature|ads|collab [--clip URL]   DM/email text to ask permission or pitch a collab
  editor.py collab add URL|FILE --creator @handle --permission dm|email|licence:<file> [--ads] [--browser firefox]
      downloads the clip into the collab B-roll folder, writes <clip>.rights.json (credit burned on screen as "via @handle"),
      logs it in marketing/collabs/<brand>.csv and indexes it so broll-match can use it
  editor.py collab remix URL --creator @handle      log an in-app Remix/Stitch/Duet (no download: the platform licence covers it)
  editor.py collab list

Rules (ledger 2026-10-28): in-app Remix/Stitch/Duet needs no permission; a downloaded clip in a brand post needs the
creator's yes (a DM screenshot counts); paid ads need explicit paid-use permission (or Meta Partnership / TikTok Spark codes).
"""
import csv, json, time
from pathlib import Path
from types import SimpleNamespace

from .common import REPO, log, studio, wjson
from .broll import default_index_dir, cmd_index

FIELDS = ["date", "brand", "creator", "source", "use", "permission", "ads", "file", "status", "next_step"]

ASKS = {
    "feature": ("Hey {h}! I run {brand}. Your video ({clip}) is genuinely one of the best takes on this. "
                "Could we feature a few seconds of it in a {brand} post? You'd be credited on screen and tagged as @{hn} in the caption. "
                "Happy to send you the edit before it goes up. A yes here is all we need 🙏"),
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
    h = handle(a.creator) if a.creator else None
    if a.action == "list":
        p = tracker(brand)
        print(p.read_text(encoding="utf-8") if p.exists() else f"no collab clips logged for {brand} yet ({p})")
        return 0
    if a.action == "dm":
        h = handle(a.target or a.creator)
        print(ASKS[a.ask].format(h=h, hn=h.lstrip("@"), brand=brand.replace("-", " ").title(), clip=a.clip or "your recent video", weeks=a.weeks))
        return 0
    if not a.target or not h:
        raise SystemExit("collab: pass the clip (URL or file) and --creator @handle")
    today = time.strftime("%Y-%m-%d")
    if a.action == "remix":
        p = log_row(brand, {"date": today, "brand": brand, "creator": h, "source": a.target, "use": "in-app remix/stitch/duet",
                            "permission": "platform licence", "ads": "no", "status": "to post", "next_step": f"tag {h}; DM after posting (collab dm {h} --ask collab)"})
        log(f"logged in {p}. Post it with the app's Remix/Stitch/Duet and tag {h} in the caption.")
        return 0
    # add: a downloaded clip in our own edit needs the creator's yes
    if not a.permission:
        raise SystemExit(f"collab add needs --permission (dm|email|licence:<file>): ask first with `editor.py collab dm {h} --ask feature`. "
                         f"No permission yet? Use `collab remix` and post it in-app instead.")
    if a.ads and not a.permission.startswith(("licence:", "email", "dm")):
        raise SystemExit("paid use needs the creator's explicit paid-use yes (or a Partnership/Spark code)")
    root = Path(a.root) if a.root else Path(default_index_dir()) / "collab" / brand
    d = root / h.lstrip("@")
    src = Path(a.target)
    if src.exists():
        d.mkdir(parents=True, exist_ok=True)
        f = d / src.name
        if f.resolve() != src.resolve():
            f.write_bytes(src.read_bytes())
    else:
        from .study import fetch
        f = fetch(a.target, d, a.browser)
    rights = {"creator": h, "credit": f"via {h}", "licence": "creator-permission", "permission": a.permission,
              "source": a.target if not src.exists() else "", "ads": bool(a.ads), "date": today}
    wjson(f.with_name(f.name + ".rights.json"), rights)
    p = log_row(brand, {"date": today, "brand": brand, "creator": h, "source": a.target, "use": "clip in our edit",
                        "permission": a.permission, "ads": "yes" if a.ads else "no", "file": str(f), "status": "in library",
                        "next_step": f"tag {h} in the caption + invite as Collab; send them the final cut"})
    log(f"saved {f} (+ rights.json, credit burns on screen as 'via {h}'); logged in {p}")
    cmd_index(SimpleNamespace(roots=[str(root)], index_dir=a.index_dir or str(default_index_dir()), frames=4, min_dur=0.8,
                              images=False, creator_brain_work=None, no_faces=False))
    return 0
