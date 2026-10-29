import subprocess,os
from PIL import Image,ImageDraw,ImageFont
SS="/tmp/claude-0/-home-user-titan-creative-studio/68a052f1-4cae-5452-90a6-d9033d4e58c0/scratchpad/ss"
R=[SS+"/gsx/gs/saigon/raw",SS+"/raw"]
def clip(p):
  for d in R:
    if os.path.exists(f"{d}/{p}.mp4"):return f"{d}/{p}.mp4"
FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf"
if not os.path.exists(FB):FB=subprocess.run(["fc-match","-f","%{file}","Inter:bold"],capture_output=True,text=True).stdout
def F(s):return ImageFont.truetype(FB,s)
Y=(255,199,39)
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def png(name,lines,label=None,y=1380,size=64,col=(255,255,255),box=False):
  im=Image.new("RGBA",(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im)
  if label:
    f=F(30);d.rounded_rectangle((60,250,60+d.textlength(label,font=f)+36,300),12,fill=(0,0,0,170));d.text((78,258),label,font=f,fill=(255,255,255,220))
  f=F(size);yy=y
  for t,c in lines:
    for ln in wrap(d,t,f,940):
      w=d.textlength(ln,font=f);x=(1080-w)/2
      if box:d.rounded_rectangle((x-18,yy-8,x+w+18,yy+size+14),14,fill=(0,0,0,150))
      d.text((x,yy),ln,font=f,fill=c or col,stroke_width=0 if box else 3,stroke_fill=(0,0,0));yy+=size+22
  im.save(name)
def run(a):subprocess.run(["ffmpeg","-y","-v","error"]+a,check=True)
V="-c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -r 30 -an".split()
# A: cinematic tension cold open (stand-in for the animated scene)
png("a1.png",[("HIM: You've been on your phone the WHOLE trip planning.",None)],"[ANIMATED SCENE, AI couple at the departure gate]",1500,56,box=True)
png("a2.png",[("HER: ...",None)],"[ANIMATED SCENE, AI couple at the departure gate]",1500,56,box=True)
png("a3.png",[("HIM: Who are you even texting?!",None)],"[ANIMATED SCENE: slow push-in, music cuts out]",1500,56,box=True)
for k,(p,s) in enumerate([("TikTok_7663523152055504149",9),("TikTok_7663523152055504149",18.4),("TikTok_7578498506088910088",4)]):
  run(["-ss",str(s),"-t","1.7","-i",clip(p),"-vf","scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30","-t","1.67"]+V+[f"a{k}.mp4"])
open("al.txt","w").write("file 'a0.mp4'\nfile 'a1.mp4'\nfile 'a2.mp4'\n");run(["-f","concat","-safe","0","-i","al.txt","-c","copy","araw.mp4"])
src="araw.mp4"
run(["-t","5","-i",src,"-i","a1.png","-i","a2.png","-i","a3.png","-filter_complex",
 "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,eq=saturation=0.25:brightness=-0.12:contrast=1.15,"
 "zoompan=z='1+0.0012*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,"
 "drawbox=y=0:w=iw:h=330:color=black:t=fill,drawbox=y=ih-330:w=iw:h=330:color=black:t=fill[b];"
 "[b][1]overlay=enable='lt(t,1.7)'[c];[c][2]overlay=enable='between(t,1.7,3.1)'[d];[d][3]overlay=enable='gte(t,3.1)'[v]",
 "-map","[v]","-t","5"]+V+["A.mp4"])
# B: Ben outburst (placeholder until the AI character exists)
im=Image.new("RGB",(1080,1920),Y);d=ImageDraw.Draw(im)
d.ellipse((340,420,740,820),fill=(232,170,120));d.rectangle((300,800,780,1300),fill=(40,70,120))
d.text((380,560),"BEN",font=F(120),fill=(30,22,84))
f=F(30);t="[AI character shot: Ben, sunburnt backpacker, bolts up in his hostel bunk]";d.text(((1080-d.textlength(t,font=f))/2,330),t,font=f,fill=(30,22,84))
yy=1380
for ln in wrap(d,"I'M GOING TO HO CHI MINH, B*TCH!",F(92),960):
  w=d.textlength(ln,font=F(92));d.text(((1080-w)/2,yy),ln,font=F(92),fill=(255,255,255),stroke_width=6,stroke_fill=(30,22,84));yy+=110
im.save("b.png")
run(["-loop","1","-t","1.6","-i","b.png","-vf","scale=1080:1920,zoompan=z='if(lt(on,4),1.12-0.03*on,1.0+0.004*sin(on*2.5))':x='iw/2-(iw/zoom/2)+6*sin(on*7)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30"]+V+["B.mp4"])
# C: the drop: crash-zoom cuts
cuts=[("TikTok_7689093724592229639",6.5),("TikTok_7578498506088910088",4),("TikTok_7546223491679390984",14),("TikTok_7313075418200837383",31),
      ("TikTok_7300593523378703662",3),("TikTok_7309421754185714952",0.5),("TikTok_7657191469127650580",8),("TikTok_7564156794142985486",16),
      ("TikTok_7692458564622880020",30.5),("TikTok_7663523152055504149",17)]
words=["don't","stress.","we","shoot,","you","just","enjoy","Saigon.","",""]
parts=[]
for i,(p,t) in enumerate(cuts):
  png(f"c{i}.png",[(words[i],Y if i%2 else None)],None,860,130) if words[i] else Image.new("RGBA",(1080,1920)).save(f"c{i}.png")
  run(["-ss",str(t),"-t","0.6","-i",clip(p),"-i",f"c{i}.png","-filter_complex",
   "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,eq=saturation=1.2:contrast=1.08,"
   "zoompan=z='max(1.0,1.35-0.06*on)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30[b];[b][1]overlay[v]","-map","[v]","-t","0.6"]+V+[f"C{i}.mp4"])
  parts.append(f"C{i}.mp4")
# D: the photos + end card
def still(p,t,o):run(["-ss",str(t),"-i",clip(p),"-frames:v","1",o])
still("TikTok_7689093724592229639",6.5,"s1.jpg");still("TikTok_7578498506088910088",4,"s2.jpg")
im=Image.new("RGB",(1080,1920),(30,22,84));d=ImageDraw.Draw(im)
for j,(s,ang,xy) in enumerate([("s1.jpg",-5,(90,260)),("s2.jpg",4,(430,620))]):
  ph=Image.open(s).convert("RGB");ph=ph.crop(((ph.width-ph.height*3//4)//2,0,(ph.width+ph.height*3//4)//2,ph.height)) if ph.width>ph.height*3//4 else ph
  ph=ph.resize((520,693));card=Image.new("RGB",(560,800),"white");card.paste(ph,(20,20))
  ImageDraw.Draw(card).text((24,725),"[your Snap Saigon photo]",font=F(28),fill=(90,86,128))
  card=card.rotate(ang,expand=True,fillcolor=(30,22,84));im.paste(card,xy)
yy=1500
for t,c in [("40 photos + 3 clips, same day.",(255,255,255)),("snapsaigon.com",Y)]:
  w=d.textlength(t,font=F(64));d.text(((1080-w)/2,yy),t,font=F(64),fill=c);yy+=90
im.save("d.png")
run(["-loop","1","-t","3","-i","d.png","-vf","scale=1080:1920,zoompan=z='1+0.0015*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30"]+V+["D.mp4"])
open("list.txt","w").write("".join(f"file '{x}'\n" for x in ["A.mp4","B.mp4"]+parts+["D.mp4"]))
run(["-f","concat","-safe","0","-i","list.txt","-c","copy","silent.mp4"])
# temp sound: tension drone, 0.2 s of silence, bleep on the swear, then a kick every 0.3 s on the drop
a=("aevalsrc='if(lt(t,4.8),0.25*sin(2*PI*55*t)*(t/4.8)+0.05*sin(2*PI*110.7*t),0)"
   "+if(between(t,5.95,6.3),0.3*sin(2*PI*1000*t),0)"
   "+if(between(t,5.0,5.25),0.6*sin(2*PI*80*t)*exp(-(t-5.0)*12),0)"
   "+if(gte(t,6.6)*lt(t,12.6),0.7*sin(2*PI*(60+120*exp(-mod(t-6.6,0.3)*30))*t)*exp(-mod(t-6.6,0.3)*14),0)"
   "+if(gte(t,12.6),0.12*sin(2*PI*220*t)*exp(-(t-12.6)*0.8),0)':s=44100:d=15.6'")
run(["-i","silent.mp4","-f","lavfi","-i",a,"-map","0:v","-map","1:a","-c:v","copy","-c:a","aac","-shortest","drop_draft_v1.mp4"])
run(["-i","drop_draft_v1.mp4","-vf","fps=2,scale=150:-1,tile=8x4","-frames:v","1","sheet.jpg"])
print("ok")
