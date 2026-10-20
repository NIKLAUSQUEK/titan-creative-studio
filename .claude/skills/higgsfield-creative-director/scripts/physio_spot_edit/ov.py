import subprocess, json
segs=["s01","s02a","s02b","s03","s04","s05","s06","s07","s08","s09","s10","s11"]
def vdur(f): return float(subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=duration","-of","csv=p=0",f"{f}.mp4"]).decode().strip())
S={};t=0
for s in segs: S[s]=t; t+=vdur(s)
total=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0","concat.mp4"]).decode()); nik=S["s11"]
ov=[("hook.png",0.0,S["s06"],0,0),("cap_1.png",S["s02a"]+0.55,S["s03"],0,0),("cap_2.png",S["s03"]+0.9,S["s04"],0,0),
 ("cap_3.png",S["s04"],S["s05"],0,0),("cap_4.png",S["s05"]+0.25,S["s06"],0,0),
 ("card1.png",S["s10"]+0.2,S["s11"],0.4,0.25),("card2.png",S["s10"]+1.05,S["s11"],0.4,0.25),
 ("panel.png",nik+6.5,total,0.6,0),("cond0.png",nik+6.8,nik+12.2,0.5,0.5),("cond1.png",nik+7.6,nik+12.2,0.5,0.5),
 ("cond2.png",nik+8.5,nik+12.2,0.5,0.5),("cond3.png",nik+9.2,nik+12.2,0.5,0.5),("brand.png",nik+12.4,total,0.7,0)]
args=["ffmpeg","-v","error","-y","-i","concat.mp4"]
for f,a,b,*_ in ov: args+=["-loop","1","-framerate","30","-t",f"{b-a:.3f}","-i",f]
fc=[];last="0:v"
for i,(f,a,b,fi,fo) in enumerate(ov,1):
    dur=b-a; ch=f"[{i}:v]format=rgba"
    if fi: ch+=f",fade=t=in:st=0:d={fi}:alpha=1"
    if fo: ch+=f",fade=t=out:st={dur-fo:.3f}:d={fo}:alpha=1"
    ch+=f",setpts=PTS+{a:.3f}/TB[o{i}]"; fc.append(ch)
    fc.append(f"[{last}][o{i}]overlay=0:0:eof_action=pass"+("[vo]" if i==len(ov) else f"[x{i}]")); last=f"x{i}"
args+=["-filter_complex",";".join(fc),"-map","[vo]","-map","0:a","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p","-af","loudnorm=I=-14:TP=-1.5:LRA=11","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","/mnt/user-data/outputs/PhysioSpot_are_you_spotting_v5.mp4"]
json.dump({"S":S,"total":total},open("timeline.json","w"))
subprocess.run(args,check=True); print("DONE")
