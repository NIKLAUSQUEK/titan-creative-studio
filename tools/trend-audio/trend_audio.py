#!/usr/bin/env python3
"""Regional trending-audio radar (free): what music is hot in a market right now.

  python trend_audio.py VN            # Vietnam
  python trend_audio.py SG MY TH ID   # several markets
  python trend_audio.py VN --out marketing/audio

Sources (public, no login): kworb.net charts (Spotify daily + YouTube weekly per country), with rising
tracks flagged (biggest climbs and NEW entries). TikTok's own chart needs either the Higgsfield
TikTok connection (tiktok_music_trending, licensed Commercial Music Library) or TikTok Creative Center
in a logged-in browser; the /sound command combines all three.

LICENSING: chart songs are for awareness and in-app use only (personal/creator accounts adding the
sound inside TikTok/IG). Brand and ad content must use licensed audio (TikTok CML, Meta Sound
Collection, licensed libraries) or original music. Never imitate a specific song or artist.
"""
import argparse, html, re, sys, time, urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (trend-audio radar)"}
NAMES = {"VN": "Vietnam", "SG": "Singapore", "MY": "Malaysia", "TH": "Thailand", "ID": "Indonesia", "PH": "Philippines",
         "US": "United States", "GB": "United Kingdom", "AU": "Australia", "IN": "India", "NG": "Nigeria", "KR": "South Korea",
         "JP": "Japan", "TW": "Taiwan", "HK": "Hong Kong", "AE": "UAE"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def rows(page):
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", page, re.S):
        tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        if len(tds) >= 3:
            yield [strip(t) for t in tds]


def spotify(cc):
    out = []
    for r in rows(get(f"https://kworb.net/spotify/country/{cc.lower()}_daily.html")):
        if not r[0].isdigit():
            continue
        title = next((c for c in r if " - " in c), None)
        if title:
            out.append({"pos": int(r[0]), "move": r[1], "track": title})
    return out


def youtube(cc):
    out = []
    try:
        page = get(f"https://kworb.net/youtube/insights/{cc.lower()}.html")
    except Exception:
        return out
    for r in rows(page):
        if r[0].isdigit():
            out.append({"pos": int(r[0]), "move": r[1], "track": r[2]})
    return out


def rising(chart, n=10):
    def score(x):
        m = x["move"]
        if m in ("NEW", "RE"):
            return 1000 - x["pos"]
        try:
            return int(m.replace("+", "")) if m.startswith("+") else -999
        except ValueError:
            return -999
    return sorted([x for x in chart if score(x) > 0], key=score, reverse=True)[:n]


def report(cc, top):
    name = NAMES.get(cc.upper(), cc.upper())
    sp, yt = [], []
    try:
        sp = spotify(cc)
    except Exception as e:
        print(f"{cc}: spotify chart unavailable ({e})", file=sys.stderr)
    yt = youtube(cc)
    lines = [f"# Trending audio radar: {name} ({cc.upper()}), {time.strftime('%Y-%m-%d')}",
             "Use: pick the vibe and energy, then source a LICENSED match via `/sound` (TikTok CML / Meta Sound Collection) for brand posts. "
             "Chart songs themselves only go on personal or creator accounts, added in-app.", ""]
    if yt:
        lines += ["## YouTube weekly top (local taste)", *[f"{x['pos']}. {x['track']} ({x['move']})" for x in yt[:top]], ""]
    if sp:
        lines += ["## Spotify daily top", *[f"{x['pos']}. {x['track']} ({x['move']})" for x in sp[:top]], ""]
        lines += ["## Rising fastest (NEW / biggest climbs, Spotify)", *[f"- {x['track']} ({x['move']}, now #{x['pos']})" for x in rising(sp)], ""]
    if not (sp or yt):
        lines += ["_No public chart for this market; rely on TikTok CML (`tiktok_music_trending country_code=" + cc.upper() + "`) and local web search._", ""]
    lines += ["Sources: kworb.net (Spotify/YouTube charts). TikTok-native chart: Higgsfield tiktok_music_trending or TikTok Creative Center (logged in)."]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("countries", nargs="+", help="ISO country codes, e.g. VN SG MY")
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--out", help="folder to save <CC>-<date>.md (e.g. marketing/audio)")
    a = ap.parse_args()
    for cc in a.countries:
        md = report(cc, a.top)
        if a.out:
            Path(a.out).mkdir(parents=True, exist_ok=True)
            p = Path(a.out) / f"{cc.upper()}-{time.strftime('%Y-%m-%d')}.md"
            p.write_text(md, encoding="utf-8")
            print(f"saved {p}")
        else:
            print(md + "\n")


if __name__ == "__main__":
    main()
