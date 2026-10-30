"""EP 1 rough assembly: AI cold open (Seedance 480p drafts) -> Ben outburst -> real-footage drop -> end card.
python3 assemble_ep1.py <clips_dir> <drop_dir> <out.mp4>   (clips_dir has c1..c6.mp4, c8.mp4; drop_dir has C0..C9.mp4 + D.mp4 from build_draft_v2.py)"""
import subprocess,sys,os
from PIL import Image,ImageDraw,ImageFont
CL,DR,OUT=sys.argv[1:4];W=os.path.dirname(os.path.abspath(OUT))
FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FS="/usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf"
def F(s,f=FB):return ImageFont.truetype(f,s)
def run(a):subprocess.run(["ffmpeg","-y","-v","error"]+a,check=True)
V="-c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -r 30 -an".split()
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def sub(name,text,size=52,y=1520,big=False):
  im=Image.new("RGBA",(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im);f=F(size);yy=y
  for ln in wrap(d,text,f,940):
    w=d.textlength(ln,font=f);x=(1080-w)/2
    if big:d.text((x,yy),ln,font=f,fill="white",stroke_width=7,stroke_fill=(30,22,84))
    else:d.rounded_rectangle((x-18,yy-8,x+w+18,yy+size+14),14,fill=(0,0,0,150));d.text((x,yy),ln,font=f,fill="white")
    yy+=size+(30 if big else 22)
  im.save(f"{W}/{name}")
im=Image.new("RGBA",(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im)
d.text(((1080-d.textlength("EP 1",font=F(40)))/2,560),"EP 1",font=F(40),fill="white",stroke_width=2,stroke_fill=(0,0,0))
f=F(124,FS);d.text(((1080-d.textlength("Photos of Us",font=f))/2,620),"Photos of Us",font=f,fill="white",stroke_width=2,stroke_fill=(0,0,0))
yy=790
for ln in wrap(d,"every couple has that one trip with zero photos together",F(38),800):
  d.text(((1080-d.textlength(ln,font=F(38)))/2,yy),ln,font=F(38),fill="white",stroke_width=2,stroke_fill=(0,0,0));yy+=50
im.save(f"{W}/t1.png")
sub("t2.png","Can we get one photo of us?");sub("t3.png","Later. I'm busy.");Image.new("RGBA",(1080,1920)).save(f"{W}/t4.png")
sub("t5.png","You've been on your phone the whole trip.");sub("t6.png","Who do you think is planning all this?!")
sub("t8.png","I'M GOING TO HO CHI MINH, B*TCH!",92,1380,True)
plan=[("c1",0.6,2.6),("c2",0.5,1.5),("c3",0.5,1.5),("c4",0.8,1.0),("c5",1.0,1.7),("c6",1.2,1.7)]
parts=[]
for k,(c,ss,du) in enumerate(plan,1):
  run(["-ss",str(ss),"-t",str(du),"-i",f"{CL}/{c}.mp4","-i",f"{W}/t{k}.png","-filter_complex",
   "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[b];[b][1]overlay[v]","-map","[v]","-t",str(du)]+V+[f"{W}/p{k}.mp4"]);parts.append(f"{W}/p{k}.mp4")
run(["-f","lavfi","-i","color=black:s=1080x1920:r=30","-t","0.5"]+V+[f"{W}/blk.mp4"]);parts.append(f"{W}/blk.mp4")
run(["-ss","0.4","-t","1.8","-i",f"{CL}/c8.mp4","-i",f"{W}/t8.png","-filter_complex",
 "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30[b];[b][1]overlay[v]","-map","[v]","-t","1.8"]+V+[f"{W}/p8.mp4"]);parts.append(f"{W}/p8.mp4")
parts+=[f"{DR}/C{i}.mp4" for i in range(10)]+[f"{DR}/D.mp4"]
open(f"{W}/list.txt","w").write("".join(f"file '{p}'\n" for p in parts))
run(["-f","concat","-safe","0","-i",f"{W}/list.txt","-c","copy",f"{W}/silent.mp4"])
# timings: cold open 0-10.0, black 10.0-10.5, Ben 10.5-12.3 (bleep ~11.3), drop 12.3-18.3, end 18.3-21.3
a=("aevalsrc='if(lt(t,10.0),0.10*(sin(2*PI*220*t)+sin(2*PI*277.2*t)+sin(2*PI*329.6*t))*(0.6+0.4*sin(2*PI*0.25*t))*min(1,t/1.5),0)"
   "+if(between(t,6.2,6.5),0.25*sin(2*PI*1318*t)*exp(-(t-6.2)*10),0)"
   "+if(between(t,10.5,10.65),0.6*sin(2*PI*120*t)*exp(-(t-10.5)*30),0)"
   "+if(between(t,11.3,11.65),0.3*sin(2*PI*1000*t),0)"
   "+if(gte(t,12.3)*lt(t,18.3),0.7*sin(2*PI*(60+120*exp(-mod(t-12.3,0.3)*30))*t)*exp(-mod(t-12.3,0.3)*14),0)"
   "+if(gte(t,18.3),0.12*sin(2*PI*220*t)*exp(-(t-18.3)*0.8),0)':s=44100:d=21.5'")
run(["-i",f"{W}/silent.mp4","-f","lavfi","-i",a,"-map","0:v","-map","1:a","-c:v","libx264","-crf","26","-preset","slow","-c:a","aac","-b:a","96k","-shortest",OUT])
print("ok")
