"""PI Job Part 5-6 v2: 'did I just…' first, then REWIND to the water throw; voice-driven pacing.
python3 assemble_p56_v2.py <clips_dir> <vo_dir> <out.mp4>"""
import subprocess,sys,os
from PIL import Image,ImageDraw,ImageFont
CL,VO,OUT=sys.argv[1:4];W=os.path.join(os.path.dirname(os.path.abspath(OUT)),"_v2");os.makedirs(W,exist_ok=True)
FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf"
def F(s):return ImageFont.truetype(FB,s)
def run(a):subprocess.run(["ffmpeg","-y","-v","error"]+a,check=True)
def dur(f):return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)
V="-c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -r 30 -an".split()
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def card(name,sub=None,bubble=None,top=None,size=54,rewind=False):
  im=Image.new("RGBA",(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im)
  if top:
    f=F(64);y=150
    for ln in wrap(d,top,f,960):
      w=d.textlength(ln,font=f);d.text(((1080-w)/2,y),ln,font=f,fill="white",stroke_width=6,stroke_fill=(0,0,0));y+=80
  if bubble:
    f=F(48);ls=wrap(d,bubble,f,820);bh=len(ls)*60+40;y=360 if top else 260
    bw=max(d.textlength(l,font=f) for l in ls)+60;x=(1080-bw)/2
    d.rounded_rectangle((x,y,x+bw,y+bh),30,fill=(255,199,39));yy=y+20
    for l in ls:d.text((x+30,yy),l,font=f,fill=(30,22,84));yy+=60
  if sub:
    f=F(size);y=1500
    for ln in wrap(d,sub,f,940):
      w=d.textlength(ln,font=f);x=(1080-w)/2
      d.rounded_rectangle((x-18,y-8,x+w+18,y+size+14),14,fill=(0,0,0,170));d.text((x,y),ln,font=f,fill="white");y+=size+22
  if rewind:
    f=F(72);t="<< REWIND";d.text((70,120),t,font=f,fill="white",stroke_width=5,stroke_fill=(0,0,0))
    d.text((70,210),"2 seconds earlier…",font=F(44),fill=(255,199,39),stroke_width=4,stroke_fill=(0,0,0))
    for y in range(0,1920,6):d.line((0,y,1080,y),fill=(255,255,255,18))
  im.save(f"{W}/{name}.png")
vo={}
for i in range(1,12):   # squeeze pauses to 0.12 s and speed up 8%: voices move as fast as the cuts
  o=f"{W}/p{i}.wav";run(["-i",f"{VO}/v{i}.mp3","-af","silenceremove=start_periods=1:start_threshold=-40dB:stop_periods=-1:stop_duration=0.12:stop_threshold=-40dB:stop_silence=0.12,atempo=1.08",o]);vo[i]=o
L={i:dur(p) for i,p in vo.items()}
P=0.12   # breath between lines
# shots: (clip, start, [(card kwargs, voice idx or None, min_dur)], extra video fx)
shots=[
 ("c1",0.3,[(dict(top="he said 'I know you want it'…",sub="Hi… J?"),1,1.0),(dict(bubble="ok. this is easier than it looks. he's a GI. just say no to his advances."),2,0)]),
 ("c2",0.4,[(dict(sub="So… is it hot in Saigon, or is it just you?"),3,0)]),
 ("c3",0.4,[(dict(sub="Relax. I don't bite. Unless you ask nicely."),4,0),(dict(bubble="just say no… say it NICELY though…"),5,0)]),
 ("c4",0.3,[(dict(sub="Come on… I know you want it."),6,0.4)]),
 ("c5",0.3,[(dict(bubble="how do I say no NICELY??"),7,0)]),
 ("c7",0.3,[(dict(bubble="WAIT. DID I JUST…"),8,0.5)]),           # the panic FIRST
 ("REWIND",0,[]),                                                    # then rewind
 ("c6",0.3,[(dict(),None,1.3)]),                                     # the throw
 ("c7b",2.1,[(dict(bubble="…oh thank god. it was HER."),9,0.1)]),
 ("c8",0.3,[(dict(sub="CLIENT MEETING, JAKE?!",size=64),10,0.2)]),
 ("c9",0.4,[(dict(sub="Babe! This is… my… accountant?"),11,0.3)]),
]
parts=[];vtrack=[];t=0;k=0;cues={}
for c,ss,beats in shots:
  if c=="REWIND":
    card("rw",rewind=True);src=f"{CL}/c7.mp4"
    run(["-ss","0.3","-t","1.4","-i",src,"-i",f"{W}/rw.png","-filter_complex",
         "[0:v]reverse,setpts=0.5*PTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,hue=s=0.3,eq=contrast=1.2[b];[b][1]overlay[v]",
         "-map","[v]","-t","0.75"]+V+[f"{W}/rw.mp4"])
    parts.append(f"{W}/rw.mp4");cues["rewind"]=t;t+=0.75;continue
  segd=[];
  for kw,vi,mn in beats:segd.append(max(mn,(L[vi]+P) if vi else 0))
  du=sum(segd);src=f"{CL}/{'c7' if c=='c7b' else c}.mp4"
  ins=["-ss",str(ss),"-t",str(du),"-i",src];fc="[0:v]tpad=stop_mode=clone:stop_duration=3,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[v0];";last="v0";a=0;ii=0
  for j,((kw,vi,mn),sd) in enumerate(zip(beats,segd)):
    if vi:vtrack.append((vo[vi],t+a))
    if kw:
      n=f"k{k}";k+=1;card(n,**kw);ins+=["-i",f"{W}/{n}.png"];ii+=1
      fc+=f"[{last}][{ii}:v]overlay=enable='between(t,{a:.2f},{a+sd-0.01:.2f})'[w{j}];";last=f"w{j}"
    a+=sd
  if c=="c6":cues["splash"]=t
  if c=="c7":cues["panic"]=t
  if c=="c8":cues["slam"]=t
  out=f"{W}/{c}.mp4";run(ins+["-filter_complex",fc.rstrip(";"),"-map",f"[{last}]","-t",f"{du:.3f}"]+V+[out]);parts.append(out);t+=du
card("end",top="Part 7 →");run(["-f","lavfi","-i","color=c=0x1e1654:s=1080x1920:r=30","-i",f"{W}/end.png","-filter_complex","[0:v][1:v]overlay[v]","-map","[v]","-t","1.2"]+V+[f"{W}/end.mp4"]);parts.append(f"{W}/end.mp4");T=t+1.2
open(f"{W}/l.txt","w").write("".join(f"file '{p}'\n" for p in parts));run(["-f","concat","-safe","0","-i",f"{W}/l.txt","-c","copy",f"{W}/silent.mp4"])
p,sp,rw,sl=cues["panic"],cues["splash"],cues["rewind"],cues["slam"]
bed=(f"aevalsrc='if(lt(t,{p}),0.05*(sin(2*PI*261.6*t)+sin(2*PI*329.6*t)+sin(2*PI*392*t))*(0.7+0.3*sin(2*PI*0.5*t)),0)"
     f"+if(between(t,{p},{p}+0.5),0.45*(random(0)-0.5)*exp(-(t-{p})*6),0)"
     f"+if(between(t,{rw},{rw}+0.75),0.18*sin(2*PI*(1800-1400*(t-{rw})/0.75)*t),0)"
     f"+if(between(t,{sp},{sp}+0.7),0.5*(random(0)-0.5)*exp(-(t-{sp})*5),0)"
     f"+if(between(t,{sl},{sl}+0.25),0.5*sin(2*PI*90*t)*exp(-(t-{sl})*12),0)"
     f"+if(gt(t,{sl}+0.3),0.05*sin(2*PI*196*t)*sin(2*PI*2*t),0)':s=44100:d={T}'")
ins=["-i",f"{W}/silent.mp4","-f","lavfi","-i",bed];fl=[]
for j,(f,st) in enumerate(vtrack):
  ins+=["-i",f];ms=int(st*1000);fl.append(f"[{j+2}:a]aresample=44100,adelay={ms}|{ms},volume=1.6[a{j}]")
mix="".join(f"[a{j}]" for j in range(len(vtrack)))
fc=";".join(fl)+f";[1:a]volume=0.6[bd];[bd]{mix}amix=inputs={len(vtrack)+1}:normalize=0:duration=first[aout]"
run(ins+["-filter_complex",fc,"-map","0:v","-map","[aout]","-c:v","libx264","-crf","26","-preset","slow","-c:a","aac","-b:a","128k","-t",f"{T:.2f}",OUT])
print("ok",round(T,1))
