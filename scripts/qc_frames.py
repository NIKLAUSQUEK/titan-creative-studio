#!/usr/bin/env python3
"""QC harness: contact sheet + metadata + 9:16 safe-zone overlay for Higgsfield outputs.

  python qc_frames.py <url|path> [<url|path> ...] [--out qc_out] [--frames 5,35,65,95]

Needs ffmpeg/ffprobe + Pillow. Images get a safe-zone overlay; videos get frames at given % points.
Prints a metadata table and flags: no audio track, < 4s with expected dialogue, non-9:16, low res.
"""
import os, sys, json, subprocess, urllib.request
from PIL import Image, ImageDraw

def fetch(src, out):
    if src.startswith("http"):
        p = os.path.join(out, os.path.basename(src.split("?")[0]))
        if not os.path.exists(p): urllib.request.urlretrieve(src, p)
        return p
    return src

def probe(p):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration:stream=codec_type,width,height,r_frame_rate","-of","json",p],capture_output=True,text=True)
    j = json.loads(r.stdout or "{}"); st = j.get("streams", [])
    v = next((s for s in st if s.get("codec_type")=="video"), {})
    return {"dur": float(j.get("format",{}).get("duration",0) or 0), "w": v.get("width"), "h": v.get("height"),
            "fps": v.get("r_frame_rate"), "audio": any(s.get("codec_type")=="audio" for s in st)}

def safe_zone(img):
    """Overlay TikTok/Reels UI danger zones: top 14%, bottom 20%, right 15% button column."""
    im = img.convert("RGBA"); w, h = im.size
    ov = Image.new("RGBA", im.size, (0,0,0,0)); d = ImageDraw.Draw(ov)
    red = (255,0,0,70)
    d.rectangle([0,0,w,int(h*.14)], fill=red); d.rectangle([0,int(h*.80),w,h], fill=red)
    d.rectangle([int(w*.85),int(h*.35),w,int(h*.80)], fill=red)
    return Image.alpha_composite(im, ov).convert("RGB")

def main():
    args = sys.argv[1:]; out = "qc_out"; pts = [5,35,65,95]
    if "--out" in args: i = args.index("--out"); out = args[i+1]; del args[i:i+2]
    if "--frames" in args: i = args.index("--frames"); pts = [int(x) for x in args[i+1].split(",")]; del args[i:i+2]
    os.makedirs(out, exist_ok=True); rows = []
    for src in args:
        p = fetch(src, out); name = os.path.splitext(os.path.basename(p))[0][-12:]
        if p.lower().endswith((".png",".jpg",".jpeg",".webp")):
            im = Image.open(p); m = {"dur":0,"w":im.width,"h":im.height,"fps":"-","audio":False}
            frames = [safe_zone(im)]
        else:
            m = probe(p); frames = []
            for pc in pts:
                f = os.path.join(out, f"{name}_{pc}.jpg")
                subprocess.run(["ffmpeg","-v","error","-y","-ss",str(m["dur"]*pc/100),"-i",p,"-frames:v","1",f])
                if os.path.exists(f): frames.append(safe_zone(Image.open(f)))
        flags = []
        if m["w"] and m["h"] and abs(m["w"]/m["h"] - 9/16) > .02: flags.append("not 9:16")
        if m["w"] and min(m["w"], m["h"]) < 1000: flags.append("low-res (<1000px short edge)")
        if m["dur"] and not m["audio"]: flags.append("NO AUDIO TRACK")
        if m["dur"] and m["dur"] < 4: flags.append("<4s - too short for a spoken line + reaction")
        rows.append((name, m, flags, frames))
    W = 220
    sheet_h = sum(int(W * (r[3][0].height / r[3][0].width)) + 24 for r in rows if r[3])
    sheet = Image.new("RGB", (W*max(len(pts),1)+10, max(sheet_h,10)), "white"); y = 0
    for name, m, flags, frames in rows:
        if not frames: continue
        h = int(W * frames[0].height / frames[0].width)
        ImageDraw.Draw(sheet).text((4, y+4), f"{name}  {m['dur']:.1f}s  {m['w']}x{m['h']}  audio={m['audio']}  {' | '.join(flags)}", fill="black")
        for i, fr in enumerate(frames): sheet.paste(fr.resize((W, h)), (i*W, y+20))
        y += h + 24
    sp = os.path.join(out, "contact_sheet.jpg"); sheet.save(sp, quality=82)
    print(f"{'asset':14} {'dur':>5} {'res':>11} audio  flags")
    for name, m, flags, _ in rows: print(f"{name:14} {m['dur']:5.1f} {str(m['w'])+'x'+str(m['h']):>11} {str(m['audio']):5}  {'; '.join(flags) or 'ok'}")
    print("contact sheet ->", sp, "(red = platform UI zones; keep faces/text out)")

if __name__ == "__main__": main()
