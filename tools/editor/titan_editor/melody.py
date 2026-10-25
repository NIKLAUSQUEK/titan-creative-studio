"""Edu-song helper (Klaus 2026-10-25: "teach physio / men's health like science channels and kids' shows do, with songs").

`editor.py song` turns lyrics + a public-domain tune (or a rap beat) into:
- a syllable-fit report (LYRICS.md): which lines are too long or short for the melody, plus rhyme and flow checks in rap mode;
- guide.wav: a synthesised melody and/or beat at the chosen BPM. It is a guide track for singing or recording; the original audio is ours;
- lyrics.srt + lyrics.json: per-line and per-word timings, for karaoke captions in any editor.
Only the COMPOSITIONS below are public domain (traditional, or composers dead 100+ years). Recordings and modern arrangements are not:
never lift audio from a recording, play or synthesise it yourself. Copyrighted pop songs are never built here (see edu-songs-mnemonics.md §5).
"""
import json, math, re, wave
from pathlib import Path

from .common import log

# (pitch, beats) per note; phrases = notes per lyric line. "R" = rest.
TUNES = {
    "twinkle": {"title": "Twinkle Twinkle / ABC song (trad. French, 1761)", "bpm": 100, "phrases": [7, 7, 7, 7, 7, 7],
                "notes": "C4 C4 G4 G4 A4 A4 G4:2 F4 F4 E4 E4 D4 D4 C4:2 G4 G4 F4 F4 E4 E4 D4:2 G4 G4 F4 F4 E4 E4 D4:2 C4 C4 G4 G4 A4 A4 G4:2 F4 F4 E4 E4 D4 D4 C4:2"},
    "row-your-boat": {"title": "Row, Row, Row Your Boat (trad., 1852)", "bpm": 104, "phrases": [5, 5, 12, 5],
                      "notes": "C4 C4 C4:0.75 D4:0.25 E4 E4:0.75 D4:0.25 E4:0.75 F4:0.25 G4:2 C5:0.333 C5:0.333 C5:0.334 G4:0.333 G4:0.333 G4:0.334 "
                               "E4:0.333 E4:0.333 E4:0.334 C4:0.333 C4:0.333 C4:0.334 G4:0.75 F4:0.25 E4:0.75 D4:0.25 C4:2"},
    "frere-jacques": {"title": "Frere Jacques / Are You Sleeping (trad.)", "bpm": 110, "phrases": [4, 4, 3, 3, 6, 6, 3, 3],
                      "notes": "C4 D4 E4 C4 C4 D4 E4 C4 E4 F4 G4:2 E4 F4 G4:2 G4:0.5 A4:0.5 G4:0.5 F4:0.5 E4 C4 G4:0.5 A4:0.5 G4:0.5 F4:0.5 E4 C4 "
                               "C4 G3 C4:2 C4 G3 C4:2"},
    "mary-lamb": {"title": "Mary Had a Little Lamb (trad., 1830)", "bpm": 112, "phrases": [7, 3, 3, 8, 5],
                  "notes": "E4 D4 C4 D4 E4 E4 E4:2 D4 D4 D4:2 E4 G4 G4:2 E4 D4 C4 D4 E4 E4 E4 E4 D4 D4 E4 D4 C4:4"},
    "london-bridge": {"title": "London Bridge Is Falling Down (trad.)", "bpm": 112, "phrases": [7, 3, 3, 7, 4],
                      "notes": "G4:1.5 A4:0.5 G4 F4 E4 F4 G4:2 D4 E4 F4:2 E4 F4 G4:2 G4:1.5 A4:0.5 G4 F4 E4 F4 G4:2 D4:2 G4:2 E4 C4:3"},
    "ode-to-joy": {"title": "Ode to Joy (Beethoven, 1824)", "bpm": 120, "phrases": [8, 7, 8, 7],
                   "notes": "E4 E4 F4 G4 G4 F4 E4 D4 C4 C4 D4 E4 E4:1.5 D4:0.5 D4:2 E4 E4 F4 G4 G4 F4 E4 D4 C4 C4 D4 E4 D4:1.5 C4:0.5 C4:2"},
    "mountain-king": {"title": "In the Hall of the Mountain King (Grieg, 1875)", "bpm": 120, "phrases": [7, 3, 3, 8, 5],
                      "notes": "A3:0.5 B3:0.5 C4:0.5 D4:0.5 E4:0.5 C4:0.5 E4 D#4:0.5 B3:0.5 D#4 D4:0.5 A#3:0.5 D4 A3:0.5 B3:0.5 C4:0.5 D4:0.5 E4:0.5 C4:0.5 E4:0.5 A4:0.5 "
                                "G4:0.5 E4:0.5 C4:0.5 E4:0.5 G4:2"},
}
NOTE = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
SR = 44100


def parse(notes):
    out = []
    for tok in notes.split():
        p, _, b = tok.partition(":")
        out.append((p, float(b or 1)))
    return out


def freq(p, shift=0):
    if p == "R":
        return 0.0
    m = re.match(r"([A-G]#?)(\d)", p)
    midi = 12 * (int(m.group(2)) + 1) + NOTE[m.group(1)] + shift
    return 440.0 * 2 ** ((midi - 69) / 12)


# ---------------- syllables, rhyme ----------------
SMALL = {"0": 2, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 2, "8": 1, "9": 1, "10": 1, "11": 3, "12": 1, "20": 2, "30": 2, "100": 3}


def syl_word(w):
    if "-" in w.strip("-"):
        return sum(syl_word(x) for x in w.split("-") if x)
    if w.isdigit():
        return SMALL.get(w, 2 * len(w) - 1)
    w = re.sub(r"[^a-z]", "", w.lower())
    if not w:
        return 0
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1
    if w.endswith("ed") and not w.endswith(("ted", "ded")) and n > 1:
        n -= 1
    return max(1, n)


def words(line):
    return [w for w in re.findall(r"[\w'-]+", line) if re.search(r"\w", w)]


def syllables(line):
    return sum(syl_word(w) for w in words(line))


VOWEL = [("oa", "o"), ("ow", "o"), ("oe", "o"), ("ee", "e"), ("ea", "e"), ("ie", "e"), ("ey", "e"), ("ai", "a"), ("ay", "a"), ("igh", "i"), ("y", "i")]


def rhyme_key(line):
    ws = words(line)
    if not ws:
        return ""
    w = re.sub(r"[^a-z]", "", ws[-1].lower())
    if len(w) > 2 and w.endswith("e") and w[-2] not in "aeiou":
        w = w[:-1]                                       # magic e: code -> cod, frame -> fram
    for a, b in VOWEL:
        w = w.replace(a, b)
    m = re.search(r"[aeiou]+[^aeiou]*$", w)
    return m.group(0) if m else w


# ---------------- fit + timing ----------------
def fit_tune(lines, tune, bpm):
    notes = parse(TUNES[tune]["notes"])
    phrases = TUNES[tune]["phrases"]
    beat = 60.0 / bpm
    starts, t = [], 0.0
    for _, b in notes:
        starts.append(t); t += b * beat
    loop_len = t
    rows, timing, idx = [], [], 0
    bounds = [sum(phrases[:i]) for i in range(len(phrases) + 1)]
    for li, line in enumerate(lines):
        k = li % len(phrases)
        loop = li // len(phrases)
        n0, n1 = bounds[k], bounds[k + 1]
        s, n = syllables(line), n1 - n0
        status = "ok" if s == n else ("tight (+1, slur two syllables on one note)" if s == n + 1 else
                                      ("short (-1, hold the last note)" if s == n - 1 else f"{'cut' if s > n else 'add'} {abs(s - n)} syllable(s)"))
        rows.append({"line": line, "syllables": s, "notes": n, "status": status})
        off = loop * loop_len
        si, wt = 0, []
        for w in words(line):
            ns = syl_word(w)
            a = min(n0 + si, n1 - 1)
            e = min(n0 + si + ns - 1, n1 - 1)
            wt.append({"word": w, "start": round(off + starts[a], 3), "end": round(off + starts[e] + notes[e][1] * beat, 3)})
            si += ns
        timing.append({"line": line, "start": wt[0]["start"] if wt else off + starts[n0],
                       "end": round(off + starts[n1 - 1] + notes[n1 - 1][1] * beat, 3), "words": wt})
    return rows, timing, notes, beat, loop_len


def fit_rap(lines, bpm, bars_per_line=1):
    beat = 60.0 / bpm
    bar = 4 * beat * bars_per_line
    rows, timing = [], []
    for li, line in enumerate(lines):
        s = syllables(line)
        status = "ok" if 6 <= s <= 14 else ("sparse (<6: fine for a hook, slow it down)" if s < 6 else "crowded (>14: cut words or give it 2 bars)")
        rk = rhyme_key(line)
        if li % 2 == 1:
            prev = rows[-1]
            if rk and prev["rhyme"] and rk != prev["rhyme"]:
                status += "; couplet end-rhyme weak (" + prev["rhyme"] + " / " + rk + ")"
            if abs(s - prev["syllables"]) > 3:
                status += f"; flow uneven vs previous line ({prev['syllables']} vs {s})"
        rows.append({"line": line, "syllables": s, "notes": "1 bar", "status": status, "rhyme": rk})
        t0, ws, wt, si = li * bar, words(line), [], 0
        slot = bar / max(s, 1) if s > 8 else beat / 2          # <=8 syllables ride the 8th-note grid from the downbeat
        for w in ws:
            ns = syl_word(w)
            wt.append({"word": w, "start": round(t0 + si * slot, 3), "end": round(t0 + (si + ns) * slot, 3)}); si += ns
        timing.append({"line": line, "start": round(t0, 3), "end": round(t0 + bar, 3), "words": wt})
    return rows, timing, len(lines) * bar


# ---------------- synthesis ----------------
def _tone(f, dur, amp=0.32):
    import numpy as np
    n = int(dur * SR)
    t = np.arange(n) / SR
    if f <= 0 or n == 0:
        return np.zeros(n)
    y = np.sin(2 * math.pi * f * t) + 0.45 * np.sin(4 * math.pi * f * t) + 0.18 * np.sin(6 * math.pi * f * t)
    env = np.minimum(1.0, t / 0.012) * np.exp(-2.2 * t / max(dur, 0.2))
    rel = np.minimum(1.0, (dur - t) / 0.04)
    return amp * y * env * np.clip(rel, 0, 1) / 1.63


def _beat(total, bpm, style="boom-bap"):
    import numpy as np
    out = np.zeros(int(total * SR) + SR)
    beat = 60.0 / bpm
    rng = np.random.default_rng(7)

    def put(sig, t):
        i = int(t * SR)
        out[i:i + len(sig)] += sig[:max(0, len(out) - i)]
    tk = np.arange(int(0.25 * SR)) / SR
    kick = 0.9 * np.sin(2 * math.pi * (45 + 90 * np.exp(-tk * 30)) * tk) * np.exp(-tk * 12)
    tn = np.arange(int(0.18 * SR)) / SR
    snare = 0.45 * rng.uniform(-1, 1, len(tn)) * np.exp(-tn * 22) + 0.2 * np.sin(2 * math.pi * 190 * tn) * np.exp(-tn * 30)
    th = np.arange(int(0.05 * SR)) / SR
    hat = 0.12 * rng.uniform(-1, 1, len(th)) * np.exp(-th * 90)
    k, t = 0, 0.0
    while t < total:
        pos = k % 4
        if pos in (0, 2):
            put(kick, t)
        if pos in (1, 3):
            put(snare, t)
        put(hat, t); put(hat * 0.7, t + beat / 2)
        if style == "boom-bap" and pos == 3:
            put(kick * 0.8, t + beat * 0.75)
        k += 1; t = k * beat
    return out[:int(total * SR)]


def write_wav(path, y):
    import numpy as np
    y = np.clip(y / max(1e-9, np.max(np.abs(y))) * 0.89, -1, 1)
    st = np.repeat((y * 32767).astype("<i2")[:, None], 2, axis=1)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def make_song(lyrics, out_dir, tune=None, bpm=None, shift=0, rap=False, beat=False, count_in=True):
    import numpy as np
    out_dir = Path(out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    lines = [l.strip() for l in lyrics.splitlines() if l.strip() and not l.strip().startswith("#")]
    if rap or not tune:
        bpm = bpm or 92
        rows, timing, total = fit_rap(lines, bpm)
        mel = np.zeros(int(total * SR))
        beat = True
    else:
        bpm = bpm or TUNES[tune]["bpm"]
        rows, timing, notes, b, loop_len = fit_tune(lines, tune, bpm)
        ph = TUNES[tune]["phrases"]
        used = (len(lines) - 1) // len(ph) * len(notes) + sum(ph[:(len(lines) - 1) % len(ph) + 1])   # stop after the last sung phrase
        mel = np.concatenate([_tone(freq(p, shift), d * b) for p, d in (notes * (used // len(notes) + 1))[:used]])
        total = len(mel) / SR
    y = mel + (0.8 * _beat(total, bpm) if beat else 0)
    lead = 4 * 60.0 / bpm if count_in else 0.0            # one bar of count-in clicks so a singer can come in on time
    if count_in:
        clicks = np.concatenate([_tone(1568 if i == 0 else 1046, 60.0 / bpm, 0.25) for i in range(4)])
        y = np.concatenate([clicks, y])
        for tl in timing:
            tl["start"] = round(tl["start"] + lead, 3); tl["end"] = round(tl["end"] + lead, 3)
            for w in tl["words"]:
                w["start"] = round(w["start"] + lead, 3); w["end"] = round(w["end"] + lead, 3)
    write_wav(out_dir / "guide.wav", y)
    (out_dir / "lyrics.json").write_text(json.dumps({"tune": tune, "rap": rap or not tune, "bpm": bpm, "shift": shift, "count_in_s": lead,
                                                     "lines": timing}, indent=1), encoding="utf-8")
    (out_dir / "lyrics.srt").write_text("".join(f"{i + 1}\n{srt_time(t['start'])} --> {srt_time(t['end'])}\n{t['line']}\n\n" for i, t in enumerate(timing)),
                                        encoding="utf-8")
    bad = [r for r in rows if not r["status"].startswith("ok")]
    md = [f"# Lyric fit: {'rap beat' if (rap or not tune) else TUNES[tune]['title']} @ {bpm} BPM", "",
          f"{len(rows) - len(bad)}/{len(rows)} lines sit cleanly. guide.wav = synthesised guide (original audio; the composition is public domain).", "",
          "| # | Line | Syllables | Notes | Fit |", "|---|---|---|---|---|"]
    md += [f"| {i + 1} | {r['line']} | {r['syllables']} | {r['notes']} | {r['status']} |" for i, r in enumerate(rows)]
    md += ["", "Next: record the vocal over guide.wav (or a TTS/voice take), then `editor.py assemble --music <mix.wav> --music-licence original`,",
           "and load lyrics.srt as karaoke captions. Fix every non-ok line first: scansion is the whole trick."]
    (out_dir / "LYRICS.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    log(f"song -> {out_dir} ({total + lead:.1f} s, {len(rows) - len(bad)}/{len(rows)} lines fit)")
    return rows, timing


def cmd_song(a, edit_dir):
    if a.list:
        for k, v in TUNES.items():
            print(f"{k:15s} {v['title']}  ({v['bpm']} BPM, lines of {v['phrases']} syllables)")
        return 0
    if a.tune and a.tune not in TUNES:
        raise SystemExit(f"unknown tune {a.tune}; public-domain tunes: {', '.join(TUNES)} (or --rap)")
    lyr = Path(a.lyrics).read_text(encoding="utf-8") if a.lyrics and Path(a.lyrics).exists() else (a.lyrics or "")
    if not lyr.strip():
        raise SystemExit("give --lyrics <file or text>")
    out = Path(a.out) if a.out else edit_dir / "song"
    rows, _ = make_song(lyr, out, None if a.rap else a.tune, a.bpm, a.shift, a.rap, a.beat)
    for r in rows:
        print(f"  {r['syllables']:>2} / {r['notes']!s:>5}  {r['status']:<40} {r['line']}")
    return 0
