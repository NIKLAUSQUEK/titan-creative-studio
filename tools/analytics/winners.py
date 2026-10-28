"""Winners report: rank posts by how much they got people talking, and justify next month's content from the last 2-3 months.

  python tools/analytics/winners.py --brand snap-saigon [--days 90] [--month 2026-12]

Inputs (all CSV, any platform):
  marketing/analytics/<brand>/posts.csv     our post log: url, date, platform, lane, hook, hook_ladder, cta, format, giveaway, notes
  marketing/analytics/<brand>/exports/*.csv  platform exports (IG/FB Insights, TikTok Studio, Metricool, vidIQ...): any column names,
                                             matched by meaning (permalink/link/url, views/plays/reach, shares, saves, comments, likes, follows)
Output:
  marketing/reviews/<brand>-<yyyy-mm>-winners.md   winners, losers, what wins by lane / hook ladder / CTA / format / giveaway,
                                                    and the "do more / do less / test" calls with the numbers behind them
  marketing/analytics/<brand>/scored.csv
Talk score = per 1,000 views: shares and sends x3, saves x2, comments x1.5, follows x5, likes x0.5. Shares/sends/comments are what
"people talking and sharing" looks like in the numbers, so they weigh most.
"""
import argparse, csv, glob, re, statistics
from datetime import date, datetime, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COLS = {  # meaning -> header patterns (lower-case, matched as substrings)
    "url": ["permalink", "post link", "link", "url", "video link"],
    "date": ["publish time", "published", "post time", "date", "created"],
    "views": ["views", "plays", "video views", "impressions", "reach"],
    "shares": ["shares", "reposts"],
    "sends": ["sends", "sent"],
    "saves": ["saves", "saved", "favorites", "bookmarks"],
    "comments": ["comments"],
    "likes": ["likes", "reactions"],
    "follows": ["follows", "new followers", "followers gained"],
}
WEIGHTS = {"shares": 3, "sends": 3, "saves": 2, "comments": 1.5, "follows": 5, "likes": 0.5}
DIMS = ["lane", "hook_ladder", "cta", "format", "giveaway", "platform"]


def num(v):
    v = str(v or "").replace(",", "").strip().lower()
    m = re.match(r"([\d.]+)\s*([km]?)", v)
    if not m:
        return 0.0
    return float(m.group(1)) * {"k": 1e3, "m": 1e6}.get(m.group(2), 1)


def key(url):
    """Normalise a post URL so exports and the post log join (drops query strings and trailing slashes)."""
    u = re.sub(r"[?#].*$", "", str(url or "").strip()).rstrip("/").lower()
    m = re.search(r"/(reel|p|video|videos|shorts)/([\w-]+)", u)
    return m.group(2) if m else u


def parse_date(v):
    for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S", "%m/%d/%Y %H:%M"):
        try:
            return datetime.strptime(str(v).strip()[:19], fmt).date()
        except ValueError:
            continue
    return None


def read_exports(folder):
    rows = {}
    for f in sorted(glob.glob(str(folder / "*.csv"))):
        with open(f, encoding="utf-8-sig") as fh:
            for r in csv.DictReader(fh):
                low = {k.lower().strip(): v for k, v in r.items() if k}
                pick = {}
                for meaning, pats in COLS.items():
                    for p in pats:
                        hit = next((k for k in low if p in k), None)
                        if hit:
                            pick[meaning] = low[hit]
                            break
                if not pick.get("url"):
                    continue
                k = key(pick["url"])
                cur = rows.setdefault(k, {"url": pick["url"]})
                for m in WEIGHTS.keys() | {"views"}:  # keep the max seen across exports (latest snapshot wins)
                    cur[m] = max(cur.get(m, 0.0), num(pick.get(m)))
                cur.setdefault("date", pick.get("date"))
    return rows


def score(r):
    v = max(r.get("views", 0.0), 1.0)
    return round(1000 * sum(w * r.get(m, 0.0) for m, w in WEIGHTS.items()) / v, 2)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", required=True)
    ap.add_argument("--days", type=int, default=90)
    ap.add_argument("--month", default=date.today().strftime("%Y-%m"), help="report label")
    ap.add_argument("--today", help="YYYY-MM-DD (tests)")
    a = ap.parse_args(argv)
    base = REPO / "marketing" / "analytics" / a.brand
    today = parse_date(a.today) if a.today else date.today()
    since = today - timedelta(days=a.days)
    log = {}
    if (base / "posts.csv").exists():
        with open(base / "posts.csv", encoding="utf-8-sig") as fh:
            log = {key(r["url"]): r for r in csv.DictReader(fh) if r.get("url")}
    stats = read_exports(base / "exports")
    posts = []
    for k in set(log) | set(stats):
        r = {**stats.get(k, {}), **{d: v for d, v in log.get(k, {}).items() if v}}
        d = parse_date(r.get("date"))
        if d and d < since:
            continue
        if not stats.get(k):
            r["status"] = "no numbers yet"
        r["date"] = d.isoformat() if d else ""
        r["talk"] = score(r) if stats.get(k) else None
        posts.append(r)
    scored = sorted([p for p in posts if p["talk"] is not None], key=lambda p: -p["talk"])
    out = REPO / "marketing" / "reviews" / f"{a.brand}-{a.month}-winners.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    base.mkdir(parents=True, exist_ok=True)
    with open(base / "scored.csv", "w", newline="", encoding="utf-8") as fh:
        fields = ["url", "date", "platform", "lane", "hook_ladder", "hook", "cta", "format", "giveaway", "views", "shares", "sends", "saves", "comments", "likes", "follows", "talk"]
        w = csv.DictWriter(fh, fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(scored)

    L = [f"# {a.brand}: winners report {a.month} (last {a.days} days, {since} → {today})", ""]
    if not scored:
        L += ["No posts with numbers in this window yet.",
              f"Drop platform exports (CSV) into `marketing/analytics/{a.brand}/exports/` and log each post in `posts.csv`, then re-run."]
        out.write_text("\n".join(L) + "\n", encoding="utf-8")
        print(out)
        return 0
    med = statistics.median(p["talk"] for p in scored)
    n = len(scored)
    top = scored[: max(1, round(n * 0.2))]
    bottom = scored[-max(1, round(n * 0.2)):] if n >= 5 else []
    L += [f"**{n} posts scored.** Median talk score {med:.1f} per 1,000 views (shares/sends x3, saves x2, comments x1.5, follows x5, likes x0.5).", ""]
    row = lambda p: f"| {p['date']} | {p.get('lane', '')} | {p.get('hook', '')[:60]} | {p.get('hook_ladder', '')} | {p.get('cta', '')[:40]} | {int(p.get('views', 0)):,} | {int(p.get('shares', 0) + p.get('sends', 0)):,} | {int(p.get('comments', 0)):,} | **{p['talk']:.1f}** | [link]({p['url']}) |"
    head = ["| Date | Lane | Hook | Ladder | CTA | Views | Shares+sends | Comments | Talk | Post |", "|---|---|---|---|---|---|---|---|---|---|"]
    L += ["## Winners (top 20%)", *head, *map(row, top), ""]
    if bottom:
        L += ["## Losers (bottom 20%)", *head, *map(row, bottom), ""]
    calls = []
    L += ["## What wins (each group vs the median)"]
    for d in DIMS:
        groups = {}
        for p in scored:
            if p.get(d):
                groups.setdefault(p[d], []).append(p["talk"])
        if len(groups) < 2:
            continue
        L += ["", f"**By {d.replace('_', ' ')}**", "", "| Value | Posts | Avg talk | vs median |", "|---|---|---|---|"]
        for val, ts in sorted(groups.items(), key=lambda kv: -statistics.mean(kv[1])):
            avg = statistics.mean(ts)
            x = avg / med if med else 0
            L.append(f"| {val} | {len(ts)} | {avg:.1f} | {x:.2f}x |")
            if len(ts) >= 2 and x >= 1.2:
                calls.append(f"- **Do more:** {d.replace('_', ' ')} = \"{val}\": {len(ts)} posts averaged {x:.1f}x the median talk score.")
            elif len(ts) >= 2 and x <= 0.8:
                calls.append(f"- **Do less:** {d.replace('_', ' ')} = \"{val}\": {len(ts)} posts averaged only {x:.1f}x the median.")
            elif len(ts) == 1 and x >= 1.5:
                calls.append(f"- **Test again:** {d.replace('_', ' ')} = \"{val}\" scored {x:.1f}x on its only post; one more test before calling it.")
    L += ["", "## Calls for next month (justified by the numbers above)", *(calls or ["- Not enough repeat data yet: keep testing 3-5 hook ladders per post and log every post in posts.csv."]), "",
          "The monthly hype-series run reads this file: it picks next month's hero lane, hook ladder and CTA from the **Do more** lines, and drops the **Do less** ones.", ""]
    nos = [p for p in posts if p["talk"] is None]
    if nos:
        L += [f"_{len(nos)} logged posts have no numbers yet (export missing or too new)._", ""]
    out.write_text("\n".join(L), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
