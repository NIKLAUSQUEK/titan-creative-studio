"""Texting-scene animation (ref: MUSK doc reel, Klaus 2026-10-25): a chat recreation that cuts in while the speaker keeps talking.

Recipe entry (recipe["chats"]):
  {"id": "chat1", "anchor": {"item": "c04", "offset": 0.2}, "style": "dark",
   "messages": [{"side": "me", "name": "Ashley", "text": "Babe we are gonna win!!!!", "at": 0.0},
                {"side": "them", "name": "EM", "text": "I knew that a few hours ago", "at": 1.6, "typing": 0.8},
                {"side": "them", "text": "I have over 10 thousand lasers in space right now.", "at": 4.0, "punch": true}],
   "dur": 6.5}
Grammar from the reference:
- bubbles pop in one by one (theirs grey on the left, mine blue on the right, small sender name above);
- a "•••" typing bubble shows before their reply (`typing` seconds);
- old bubbles scroll up;
- a `punch` message is shown alone and large (the line the story turns on);
- the voice and music continue underneath.
Each message pops with a soft click (sfx "pop"). The clip renders as a full-frame cutaway (a B-roll window) and is built from PNG keyframes only.
"""
import tempfile
from pathlib import Path

from .common import ffmpeg
from .textcard import draw_line, text_font, wrap_lines

STYLES = {"dark": {"bg": (8, 8, 10), "me": (37, 99, 235), "them": (38, 38, 42), "me_text": (255, 255, 255), "them_text": (235, 235, 240), "name": (150, 150, 160)},
          "light": {"bg": (245, 245, 247), "me": (10, 132, 255), "them": (229, 229, 234), "me_text": (255, 255, 255), "them_text": (20, 20, 22), "name": (120, 120, 128)}}


def bubble(msg, W, px, st, scale=1.0):
    from PIL import Image, ImageDraw
    p = int(px * scale)
    f = text_font(None, p, False)
    col = st["me_text"] if msg["side"] == "me" else st["them_text"]
    lines = wrap_lines(msg["text"], f, W * 0.68) if msg.get("text") else [""]
    imgs = [draw_line(l, f, p, col, 0, None) for l in lines if l]
    tw = max((i.width for i in imgs), default=p * 2)
    padx, pady = int(p * 0.7), int(p * 0.45)
    h = sum(i.height for i in imgs) + 2 * pady
    b = Image.new("RGBA", (tw + 2 * padx, h), (0, 0, 0, 0))
    ImageDraw.Draw(b).rounded_rectangle([0, 0, b.width - 1, b.height - 1], radius=int(p * 0.9), fill=st["me"] if msg["side"] == "me" else st["them"])
    y = pady
    for i in imgs:
        b.alpha_composite(i, (padx, y)); y += i.height
    return b


def typing_bubble(px, st, phase):
    from PIL import Image, ImageDraw
    b = Image.new("RGBA", (int(px * 3.2), int(px * 1.9)), (0, 0, 0, 0))
    d = ImageDraw.Draw(b)
    d.rounded_rectangle([0, 0, b.width - 1, b.height - 1], radius=int(px * 0.9), fill=st["them"])
    for k in range(3):
        a = 255 if k == phase % 3 else 120
        cx, cy, r = int(px * (0.85 + 0.75 * k)), b.height // 2, int(px * 0.22)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(200, 200, 205, a))
    return b


def frame(state, W, H, st, px, pop=None, typing=None, clear=False):
    """state: shown messages (oldest first). Newest sits at ~62% height; older ones stack upward and scroll off the top."""
    from PIL import Image, ImageDraw
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0) if clear else st["bg"] + (255,))
    d = ImageDraw.Draw(im)
    nf = text_font(None, int(px * 0.62), False)
    if state and state[-1].get("punch"):            # the punch line, alone and large
        m = state[-1]
        b = bubble(m, W, int(px * 1.55), st, pop if pop is not None else 1.0)
        x = int(W * 0.06) if m["side"] == "them" else W - b.width - int(W * 0.06)
        y = int(H * 0.5 - b.height / 2)
        if m.get("name"):
            d.text((x + int(px * 0.3), y - int(px * 0.95)), m["name"], font=nf, fill=st["name"])
        im.alpha_composite(b, (x, y))
        return im if clear else im.convert("RGB")
    items = [("msg", m) for m in state] + ([("typing", typing)] if typing is not None else [])
    # sender name sits above the first bubble of each run from the same side
    show = [kind == "msg" and m.get("name") and (i == 0 or items[i - 1][0] != "msg" or items[i - 1][1]["side"] != m["side"])
            for i, (kind, m) in enumerate(items)]
    y = int(H * 0.64)
    for i in range(len(items) - 1, -1, -1):
        kind, m = items[i]
        if kind == "typing":
            b = typing_bubble(px, st, m); side = "them"
        else:
            b = bubble(m, W, px, st, pop if (i == len(items) - 1 and pop is not None) else 1.0); side = m["side"]
        y -= b.height
        if y + b.height < 0:
            break
        x = int(W * 0.06) if side == "them" else W - b.width - int(W * 0.06)
        im.alpha_composite(b, (x, y))
        if show[i]:
            y -= int(px * 0.85)
            d.text((x + int(px * 0.3), y), m["name"], font=nf, fill=st["name"])
        y -= int(px * 0.55)
    return im if clear else im.convert("RGB")


def render_chat(chat, W, H, fps, out):
    """Keyframe PNGs + ffconcat durations -> silent video clip of chat['dur'] seconds.
    layout "overlay" (default, ledger [edit]): transparent background (.mov with alpha), laid over the dimmed, blurred shot.
    layout "card": the old full-frame solid card (a variation)."""
    clear = chat.get("layout", "overlay") == "overlay"
    st = STYLES.get(chat.get("style", "dark"), STYLES["dark"])
    px = int(float(chat.get("size", 0.028)) * 1920 * min(W, H) / 1080)
    msgs = sorted(chat["messages"], key=lambda m: m["at"])
    dur = float(chat.get("dur") or (msgs[-1]["at"] + 2.0))
    events = []                                      # (t, state, pop, typing)
    shown = []
    t_cursor = 0.0
    for m in msgs:
        tstart = m["at"] - float(m.get("typing", 0.0)) if m["side"] == "them" else m["at"]
        if tstart > t_cursor:
            events.append((t_cursor, list(shown), None, None))
        if m["side"] == "them" and m.get("typing"):
            ph, tt = 0, tstart
            while tt < m["at"] - 1e-3:
                events.append((tt, list(shown), None, ph)); ph += 1; tt += 0.22
        shown = shown + [m]
        for k, sc in enumerate((0.55, 0.8, 1.06, 1.0)):   # pop: overshoot then settle (4 frames)
            events.append((m["at"] + k / fps, list(shown), sc, None))
        t_cursor = m["at"] + 4 / fps
        if m.get("punch"):
            shown = [m]
    events.append((t_cursor, list(shown), None, None))
    events = [e for e in events if e[0] < dur]
    with tempfile.TemporaryDirectory() as td:
        lines = ["ffconcat version 1.0"]
        for i, (t, state, pop, typ) in enumerate(events):
            nxt = events[i + 1][0] if i + 1 < len(events) else dur
            if nxt - t <= 1e-4:
                continue
            p = Path(td) / f"f{i:04d}.png"
            frame(state, W, H, st, px, pop, typ, clear).save(p)
            lines += [f"file '{p.name}'", f"duration {nxt - t:.4f}"]
        lines.append(f"file '{p.name}'")
        (Path(td) / "list.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        enc = (["-vf", f"fps={fps},format=argb", "-c:v", "qtrle"] if clear else
               ["-vf", f"fps={fps},format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20"])
        ffmpeg(["-f", "concat", "-safe", "0", "-i", "list.txt", "-t", f"{dur:.3f}"] + enc + [str(Path(out).resolve())], cwd=td)
    return out, dur, [m["at"] for m in msgs]
