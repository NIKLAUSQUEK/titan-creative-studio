"""PI Job Part 5-6 rough cut. python3 assemble_p56.py <clips_dir> <out.mp4>  (clips c1..c9.mp4)"""
import subprocess,sys,os
from PIL import Image,ImageDraw,ImageFont
CL,OUT=sys.argv[1:3];W=os.path.join(os.path.dirname(os.path.abspath(OUT)),"_p56");os.makedirs(W,exist_ok=True)
FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf"
def F(s):return ImageFont.truetype(FB,s)
def run(a):subprocess.run(["ffmpeg","-y","-v","error"]+a,check=True)
V="-c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -r 30 -an".split()
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def card(name,sub=None,bubble=None,top=None,size=52):
  im=Image.new("RGBA",(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im)
  if top:
    f=F(64);y=150
    for ln in wrap(d,top,f,960):
      w=d.textlength(ln,font=f);d.text(((1080-w)/2,y),ln,font=f,fill="white",stroke_width=6,stroke_fill=(0,0,0));y+=80
  if bubble:
    f=F(46);ls=wrap(d,bubble,f,820);bh=len(ls)*58+40;y=360 if top else 260
    bw=max(d.textlength(l,font=f) for l in ls)+60;x=(1080-bw)/2
    d.rounded_rectangle((x,y,x+bw,y+bh),30,fill=(255,199,39));yy=y+20
    for l in ls:d.text((x+30,yy),l,font=f,fill=(30,22,84));yy+=58
  if sub:
    f=F(size);y=1500
    for ln in wrap(d,sub,f,940):
      w=d.textlength(ln,font=f);x=(1080-w)/2
      d.rounded_rectangle((x-18,y-8,x+w+18,y+size+14),14,fill=(0,0,0,170));d.text((x,y),ln,font=f,fill="white");y+=size+22
  im.save(f"{W}/{name}.png")
# (clip, start, dur, cards[(t0,t1,name)])
plan=[
 ("c1",0.3,3.0,[(0,1.4,dict(top="he said 'I know you want it'…",sub="Hi… J?")),(1.4,3.0,dict(bubble="ok. this is easier than it looks. he's a GI. just say no to his advances.",sub="Hi… J?"))]),
 ("c2",0.4,2.6,[(0,2.6,dict(sub="So… is it hot in Saigon, or is it just you?"))]),
 ("c3",0.4,2.8,[(0,1.4,dict(sub="Relax. I don't bite. Unless you ask nicely.")),(1.4,2.8,dict(bubble="just say no… say it NICELY though…"))]),
 ("c4",0.5,2.0,[(0,2.0,dict(sub="Come on… I know you want it."))]),
 ("c5",0.3,1.6,[(0,1.6,dict(bubble="how do I say no NICELY??"))]),
 ("c6",0.4,1.4,[]),
 ("c7",0.3,3.4,[(0,1.8,dict(bubble="WAIT. DID I JUST…")),(1.8,3.4,dict(bubble="…oh thank god. it was HER."))]),
 ("c8",0.3,1.9,[(0,1.9,dict(sub="CLIENT MEETING, JAKE?!",size=64))]),
 ("c9",0.4,2.6,[(0,2.6,dict(sub="Babe! This is… my… accountant?"))]),
]
parts=[];k=0
for c,ss,du,cards in plan:
  ins=["-ss",str(ss),"-t",str(du),"-i",f"{CL}/{c}.mp4"];fc="[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[v0];";last="v0"
  for j,(a,b,kw) in enumerate(cards):
    n=f"k{k}";k+=1;card(n,**kw);ins+=["-i",f"{W}/{n}.png"]
    fc+=f"[{last}][{j+1}:v]overlay=enable='between(t,{a},{b-0.01})'[v{j+1}];";last=f"v{j+1}"
  fc=fc.rstrip(";")
  if not cards:fc="[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[v0]"
  out=f"{W}/{c}_e.mp4";run(ins+["-filter_complex",fc,"-map",f"[{last}]","-t",str(du)]+V+[out]);parts.append(out)
card("end",top="Part 7 →");run(["-f","lavfi","-i","color=c=0x1e1654:s=1080x1920:r=30","-i",f"{W}/end.png","-filter_complex","[0:v][1:v]overlay[v]","-map","[v]","-t","1.5"]+V+[f"{W}/end.mp4"]);parts.append(f"{W}/end.mp4")
open(f"{W}/l.txt","w").write("".join(f"file '{p}'\n" for p in parts));run(["-f","concat","-safe","0","-i",f"{W}/l.txt","-c","copy",f"{W}/silent.mp4"])
# cue times
t=0;cue={}
for c,ss,du,_ in plan:cue[c]=t;t+=du
L=t+1.5;sp=cue["c6"];cl=cue["c8"];lean=cue["c4"]
a=(f"aevalsrc='if(lt(t,{sp}),0.07*(sin(2*PI*261.6*t)+sin(2*PI*329.6*t)+sin(2*PI*392*t))*(0.7+0.3*sin(2*PI*0.5*t)),0)"
   f"+if(between(t,{lean},{sp}),0.05*sin(2*PI*523*t)*(t-{lean}),0)"
   f"+if(between(t,{sp},{sp}+0.6),0.5*(random(0)-0.5)*exp(-(t-{sp})*5),0)"
   f"+if(between(t,{cl},{cl}+0.25),0.5*sin(2*PI*90*t)*exp(-(t-{cl})*12),0)"
   f"+if(gt(t,{cl}+0.3),0.06*sin(2*PI*196*t)*sin(2*PI*2*t),0)':s=44100:d={L}'")
run(["-i",f"{W}/silent.mp4","-f","lavfi","-i",a,"-map","0:v","-map","1:a","-c:v","libx264","-crf","26","-preset","slow","-c:a","aac","-b:a","96k","-shortest",OUT])
print("ok",round(L,1))
