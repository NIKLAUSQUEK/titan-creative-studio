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
# A: episode cold open (static close-ups, 1.2 s each, like @vi_skh)
FS="/usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf"
im=Image.new("RGBA",(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im)
f=F(40);d.text(((1080-d.textlength("EP 1",font=f))/2,1180),"EP 1",font=f,fill="white")
f=ImageFont.truetype(FS,120);d.text(((1080-d.textlength("Photos of Us",font=f))/2,1240),"Photos of Us",font=f,fill="white",stroke_width=2,stroke_fill=(0,0,0))
f=F(38);yy=1400
for ln in wrap(d,"every couple has that one trip with zero photos together",f,800):
  d.text(((1080-d.textlength(ln,font=f))/2,yy),ln,font=f,fill="white",stroke_width=2,stroke_fill=(0,0,0));yy+=50
im.save("title.png")
lab="[AI animated episode scenes go here]"
shots=[("TikTok_7689093724592229639",6.5,"title.png"),("TikTok_7300593523378703662",3,None),
       ("TikTok_7663523152055504149",18.4,("HIM: Can we get one photo of us?",)),("TikTok_7578498506088910088",4,("HER: Later. I'm busy.",)),
       ("TikTok_7663110312534560021",21.2,None),("TikTok_7313075418200837383",31,("HIM: You've been on your phone the whole trip.",)),
       ("TikTok_7663523152055504149",9,("HER: Who do you think is planning all this?!",))]
durs=[2.4,1.2,1.2,1.2,1.0,1.4,1.3]
al=[]
for k,((p,s,ov),du) in enumerate(zip(shots,durs)):
  if ov=="title.png":o="title.png"
  elif ov:png(f"sub{k}.png",[(ov[0],None)],lab if k==2 else None,1560,50,box=True);o=f"sub{k}.png"
  else:Image.new("RGBA",(1080,1920)).save(f"sub{k}.png");o=f"sub{k}.png"
  z="1+0.0025*on" if k in (1,6) else "1.0"
  run(["-ss",str(s),"-t",str(du),"-i",clip(p),"-i",o,"-filter_complex",
   "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,eq=saturation=0.55:brightness=-0.06:contrast=1.05,"
   f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30[b];[b][1]overlay[v]","-map","[v]","-t",str(du)]+V+[f"a{k}.mp4"])
  al.append(f"a{k}.mp4")
run(["-f","lavfi","-i","color=black:s=1080x1920:r=30","-t","0.5"]+V+["blk.mp4"]);al.append("blk.mp4")
open("al.txt","w").write("".join(f"file '{x}'\n" for x in al));run(["-f","concat","-safe","0","-i","al.txt","-c","copy","A.mp4"])
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
      ("TikTok_7300593523378703662",3),("TikTok_7309421754185714952",0.5),("TikTok_7657191469127650580",8),("TikTok_7697546271573183777",5.5),
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
for t,c in [("40 photos + 3 clips, same day.",(255,255,255)),("snapsaigon.com",Y),("follow for EP 2",(255,255,255))]:
  w=d.textlength(t,font=F(64));d.text(((1080-w)/2,yy),t,font=F(64),fill=c);yy+=90
im.save("d.png")
run(["-loop","1","-t","3","-i","d.png","-vf","scale=1080:1920,zoompan=z='1+0.0015*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30"]+V+["D.mp4"])
open("list.txt","w").write("".join(f"file '{x}'\n" for x in ["A.mp4","B.mp4"]+parts+["D.mp4"]))
run(["-f","concat","-safe","0","-i","list.txt","-c","copy","silent.mp4"])
# temp sound: tension drone, 0.2 s of silence, bleep on the swear, then a kick every 0.3 s on the drop
a=("aevalsrc='if(lt(t,9.7),0.10*(sin(2*PI*220*t)+sin(2*PI*277.2*t)+sin(2*PI*329.6*t))*(0.6+0.4*sin(2*PI*0.25*t))*min(1,t/1.5),0)"
   "+if(between(t,6.2,6.5),0.25*sin(2*PI*1318*t)*exp(-(t-6.2)*10),0)"
   "+if(between(t,10.2,10.35),0.6*sin(2*PI*120*t)*exp(-(t-10.2)*30),0)"
   "+if(between(t,11.0,11.35),0.3*sin(2*PI*1000*t),0)"
   "+if(gte(t,11.8)*lt(t,17.8),0.7*sin(2*PI*(60+120*exp(-mod(t-11.8,0.3)*30))*t)*exp(-mod(t-11.8,0.3)*14),0)"
   "+if(gte(t,17.8),0.12*sin(2*PI*220*t)*exp(-(t-17.8)*0.8),0)':s=44100:d=20.3'")
run(["-i","silent.mp4","-f","lavfi","-i",a,"-map","0:v","-map","1:a","-c:v","copy","-c:a","aac","-shortest","drop_draft_v2.mp4"])
run(["-i","drop_draft_v2.mp4","-vf","fps=2,scale=150:-1,tile=8x4","-frames:v","1","sheet.jpg"])
print("ok")
