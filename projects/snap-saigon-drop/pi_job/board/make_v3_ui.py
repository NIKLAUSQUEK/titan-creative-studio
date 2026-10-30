"""Part 1 v3 storyboard UI: swipe cards, J's blurry body-shot profile, rude work-notification interrupt, face-reveal joke."""
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageOps
import os
W,H=540,960;FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FR="/usr/share/fonts/opentype/inter/Inter-Medium.otf";FX="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
def F(s,b=True,x=False):return ImageFont.truetype(FX if x else (FB if b else FR),s)
PINK=(255,90,110);NAVY=(30,22,84);YEL=(255,199,39)
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w and line:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def blurbg(path,r=14):return Image.open(path).convert("RGB").resize((W,H)).filter(ImageFilter.GaussianBlur(r))
def phone(bg,title,top_bg,base):
  im=blurbg(base) if isinstance(base,str) else base.copy();d=ImageDraw.Draw(im,"RGBA");px,py,pw,ph=70,70,400,820
  d.rounded_rectangle((px-10,py-10,px+pw+10,py+ph+10),46,fill=(20,20,24));d.rounded_rectangle((px,py,px+pw,py+ph),38,fill=bg)
  d.rounded_rectangle((px,py,px+pw,py+86),38,fill=top_bg);d.rectangle((px,py+50,px+pw,py+86),fill=top_bg);d.text((px+24,py+30),title,font=F(22),fill="white");d.text((px+pw-74,py+12),"23:04",font=F(15),fill="white")
  return im,d,px,py+100,pw
def bub(d,x,y,w,txt,mine,cm=(220,248,198),ct=(255,255,255)):
  f=F(19,False);ls=wrap(d,txt,f,w-150);bw=max(d.textlength(l,font=f) for l in ls)+30;bh=len(ls)*26+18;bx=x+w-bw-16 if mine else x+16
  d.rounded_rectangle((bx,y,bx+bw,y+bh),14,fill=cm if mine else ct)
  for i,l in enumerate(ls):d.text((bx+15,y+9+i*26),l,font=f,fill=(20,20,20))
  return y+bh+12
def avatar(d,cx,cy,col,sc=1.0):
  d.ellipse((cx-70*sc,cy-90*sc,cx+70*sc,cy+50*sc),fill=col);d.rounded_rectangle((cx-120*sc,cy+60*sc,cx+120*sc,cy+260*sc),90,fill=col)
# --- swipe cards ---
cards=[("Brad, 34","crypto. gym. crypto.",(120,140,170)),("Kevin, 29","9 photos holding a fish",(140,170,130)),("Dan, 31","just ask me anything",(170,140,150))]
for i,(nm,bio,col) in enumerate(cards,1):
  im,d,x,y,w=phone((255,255,255),"Flirtly",PINK,"raw/f02.png")
  d.rounded_rectangle((x+24,y+20,x+w-24,y+560),24,fill=(236,236,244));avatar(d,x+w/2,y+210,col)
  d.text((x+44,y+470),nm,font=F(30),fill=NAVY);d.text((x+44,y+512),bio,font=F(18,False),fill=(90,90,110))
  d.ellipse((x+90,y+600,x+170,y+680),fill=(255,255,255),outline=(220,60,60),width=5);d.text((x+116,y+612),"✕".replace("✕","X"),font=F(40),fill=(220,60,60))
  d.ellipse((x+w-170,y+600,x+w-90,y+680),fill=(255,255,255),outline=(40,170,90),width=5);d.text((x+w-148,y+612),"♥".replace("♥","<3"),font=F(26),fill=(40,170,90))
  d.text((x+w/2-70,y+722),"swipe left… ew",font=F(18,False),fill=(120,120,130))
  im.save(f"img/v3_sw{i}.jpg",quality=86)
# --- J's profile: slightly blurry, body shots only ---
def jprofile():
  photos=[Image.open(f"raw/{n}.png").convert("RGB") for n in ["j1","j2","j3"] if os.path.exists(f"raw/{n}.png")]
  im,d,x,y,w=phone((255,255,255),"Flirtly",PINK,"raw/f04.png")
  gw=(w-60)//2
  slots=[(x+24,y+20,gw,330),(x+36+gw,y+20,gw,160),(x+36+gw,y+190,gw,160)]
  for p,(sx,sy,sw,sh) in zip(photos,slots):
    t=ImageOps.fit(p.filter(ImageFilter.GaussianBlur(3.2)),(sw,sh),centering=(0.5,0.35));im.paste(t,(sx,sy))
  d.text((x+24,y+372),"J, 32",font=F(30),fill=NAVY);d.text((x+24,y+414),"traveller. coffee snob. good listener.",font=F(16,False),fill=(90,90,110));d.text((x+24,y+440),"2 km away",font=F(15,False),fill=(130,130,140))
  d.rounded_rectangle((x+24,y+490,x+w-24,y+548),16,fill=(255,243,214));d.text((x+40,y+506),"3 photos · 0 faces",font=F(18),fill=(150,100,10))
  d.ellipse((x+w/2-40,y+610,x+w/2+40,y+690),fill=(255,255,255),outline=(40,170,90),width=5);d.text((x+w/2-17,y+628),"<3",font=F(26),fill=(40,170,90))
  im.save("img/v3_jprofile.jpg",quality=86)
jprofile()
# --- rude work interruption over annoyed Hân ---
im=Image.open("raw/annoyed.png").convert("RGB").resize((W,H));d=ImageDraw.Draw(im,"RGBA")
d.rounded_rectangle((24,40,W-24,196),26,fill=(255,255,255,245));d.ellipse((44,60,104,120),fill=(37,211,102));d.text((60,70),"W",font=F(34,x=True),fill="white")
d.text((120,62),"WhatsApp  ·  now",font=F(16,False),fill=(110,110,120));d.text((120,88),"+84 90 ••• •••",font=F(22),fill=(20,20,20));d.text((44,134),"hi is this snap saigon? weird request…",font=F(21,False),fill=(30,30,30))
d.rounded_rectangle((W/2-120,H-170,W/2+120,H-110),20,fill=(0,0,0,170));d.text((W/2-96,H-156),"\"…seriously? at 11pm?\"",font=F(20),fill="white")
im.save("img/v3_interrupt.jpg",quality=86)
# --- end chat: face joke ---
im,d,x,y,w=phone((255,255,255),"J",PINK,"raw/f11.png")
yy=y+14
for t,m in[("J: what are you up to tomorrow? ;)",False),("can't say. classified (shh)",True),("J: mysterious. i like it",False),("J: i'll reveal everything tomorrow. including my face ;)",False)]:
  yy=bub(d,x,yy,w,t,m,cm=(255,214,222),ct=(242,242,246))
d.rounded_rectangle((x+20,yy+22,x+w-20,yy+130),24,fill=YEL);d.text((x+40,yy+34),"Hân, thinking…",font=F(15),fill=NAVY);d.text((x+40,yy+60),"…wait. have I ever",font=F(24),fill=NAVY);d.text((x+40,yy+90),"seen his face?",font=F(24),fill=NAVY)
im.save("img/v3_facejoke.jpg",quality=86)
# --- montage: 3 blurry torsos with big ? ---
photos=[Image.open(f"raw/{n}.png").convert("RGB") for n in ["j1","j2","j3"] if os.path.exists(f"raw/{n}.png")]
m=Image.new("RGB",(W,H),(20,16,40))
for i,p in enumerate(photos):
  t=ImageOps.fit(p.filter(ImageFilter.GaussianBlur(3)),(W//3-8,H),centering=(0.5,0.4));m.paste(t,(i*(W//3)+4,0))
d=ImageDraw.Draw(m)
for i in range(len(photos)):
  cx=i*(W//3)+W//6;d.ellipse((cx-44,200-44,cx+44,200+44),fill=YEL);d.text((cx-14,200-34),"?",font=F(64,x=True),fill=NAVY)
d.rounded_rectangle((60,H-200,W-60,H-120),24,fill=(0,0,0,180));d.text((W/2-170,H-186),"face: not found",font=F(34,x=True),fill="white")
m.save("img/v3_montage.jpg",quality=86)
print("ui ok",len(photos),"photos")
