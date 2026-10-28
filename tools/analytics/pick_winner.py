"""Pick giveaway winners fairly and leave an audit trail people can check.

  python tools/analytics/pick_winner.py comments.csv [--reposters reposters.csv] [--winners 1 --backups 2]
         [--must-contain "#saigon"] [--exclude staff.txt] [--seed "<post id + draw time>"] --out marketing/giveaways/<giveaway-id>.md

comments.csv / reposters.csv: any export with a username/handle column (and optionally a text/comment column).
One entry per person (duplicates removed, comments and reposts merged unless --separate). The seed is printed in the
result so anyone can re-run the draw and get the same winners; announce the seed with the winner.
"""
import argparse, csv, hashlib, random, re
from datetime import datetime
from pathlib import Path


def users(path, must=None):
    out = {}
    with open(path, encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            low = {k.lower().strip(): (v or "") for k, v in r.items() if k}
            u = next((low[k] for k in low if re.search(r"user|handle|author|name|account", k)), "").strip().lstrip("@").lower()
            text = next((low[k] for k in low if re.search(r"comment|text|message|content", k)), "")
            if not u or (must and must.lower() not in text.lower()):
                continue
            out.setdefault(u, text)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("comments")
    ap.add_argument("--reposters")
    ap.add_argument("--winners", type=int, default=1)
    ap.add_argument("--backups", type=int, default=2)
    ap.add_argument("--must-contain")
    ap.add_argument("--exclude", help="file with one handle per line (staff, partners, past winners)")
    ap.add_argument("--seed")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    pool = users(a.comments, a.must_contain)
    if a.reposters:
        for u, t in users(a.reposters).items():
            pool.setdefault(u, t or "(repost)")
    if a.exclude:
        for ln in Path(a.exclude).read_text(encoding="utf-8").splitlines():
            pool.pop(ln.strip().lstrip("@").lower(), None)
    entrants = sorted(pool)
    if not entrants:
        raise SystemExit("no valid entries")
    seed = a.seed or datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    rng = random.Random(int(hashlib.sha256(seed.encode()).hexdigest(), 16))
    picks = rng.sample(entrants, min(len(entrants), a.winners + a.backups))
    lines = [f"# Giveaway draw ({datetime.now():%Y-%m-%d %H:%M})", "",
             f"- Entries: {len(entrants)} unique people (duplicates removed{', must contain ' + repr(a.must_contain) if a.must_contain else ''})",
             f"- Seed: `{seed}` (re-run with the same files and seed to get the same result)", ""]
    lines += [f"{'Winner' if i < a.winners else 'Backup'} {i + 1 if i < a.winners else i - a.winners + 1}: @{u}  ({pool[u][:80]})" for i, u in enumerate(picks)]
    txt = "\n".join(lines) + "\n"
    print(txt)
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(txt, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
