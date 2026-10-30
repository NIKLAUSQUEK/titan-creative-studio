"""Storyboard images for PI Job Part 1: resize frames + draw free phone-UI inserts (Pillow)."""
from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=540,960;FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FR="/usr/share/fonts/opentype/inter/Inter-Medium.otf"
def F(s,b=True):return ImageFont.truetype(FB if b else FR,s)
for n in["02","04","06","07","10","11","13"]:
  Image.open(f"raw/f{n}.png").convert("RGB").resize((W,H),Image.LANCZOS).save(f"img/f{n}.jpg",quality=84)
def phone(bg,top_title,top_bg,fn,draw_body,base=None):
  im=(Image.open(base).convert("RGB").resize((W,H)).filter(ImageFilter.GaussianBlur(14)) if base else Image.new("RGB",(W,H),bg))
  d=ImageDraw.Draw(im,"RGBA");px,py,pw,ph=70,70,400,820
  d.rounded_rectangle((px-10,py-10,px+pw+10,py+ph+10),46,fill=(20,20,24))
  d.rounded_rectangle((px,py,px+pw,py+ph),38,fill=bg)
  d.rounded_rectangle((px,py,px+pw,py+86),38,fill=top_bg);d.rectangle((px,py+50,px+pw,py+86),fill=top_bg)
  d.text((px+24,py+30),top_title,font=F(22),fill="white")
  d.text((px+pw-74,py+12),"23:04",font=F(15),fill="white")
  draw_body(d,px,py+100,pw);im.save(f"img/{fn}.jpg",quality=86)
def bub(d,x,y,w,txt,mine,col_me=(220,248,198),col_them=(255,255,255),f=None):
  f=f or F(19,False);lines=[];line=""
  for wd in txt.split():
    if d.textlength((line+" "+wd).strip(),font=f)>w-150:lines.append(line);line=wd
    else:line=(line+" "+wd).strip()
  lines.append(line);bw=max(d.textlength(l,font=f) for l in lines)+30;bh=len(lines)*26+18
  bx=x+w-bw-16 if mine else x+16
  d.rounded_rectangle((bx,y,bx+bw,y+bh),14,fill=col_me if mine else col_them)
  for i,l in enumerate(lines):d.text((bx+15,y+9+i*26),l,font=f,fill=(20,20,20))
  return y+bh+12
# 03 Tinder match
def tinder(d,x,y,w):
  d.text((x+w/2-118,y+80),"It's a Match!",font=F(40),fill=(255,90,110))
  d.ellipse((x+w/2-80,y+170,x+w/2+80,y+330),fill=(150,140,160));d.text((x+w/2-12,y+232),"J",font=F(44),fill="white")
  d.text((x+w/2-96,y+350),"J, 32 · 2 km away",font=F(22),fill=(60,60,60))
  d.text((x+w/2-150,y+386),"\"traveller. coffee snob. good listener\"",font=F(16,False),fill=(110,110,110))
  bub(d,x,y+470,w,"J: you look like trouble 😏".replace("😏",";)"),False,col_them=(242,242,246))
  d.rounded_rectangle((x+40,y+600,x+w-40,y+656),28,fill=(255,90,110));d.text((x+w/2-70,y+614),"Send a message",font=F(20),fill="white")
phone((255,255,255),"tinder",(255,90,110),"p03",tinder,base="raw/f04.png")
# 05 WhatsApp from Trâm (unknown number)
def wa(d,x,y,w):
  d.text((x+16,y-4),"Today",font=F(14,False),fill=(120,120,120))
  yy=y+26
  for t in["hi is this snap saigon? weird request…","my bf has a 'late client meeting' tomorrow. won't say where. ALWAYS on his phone","can you follow him and take photos? 👀".replace(" 👀","")]:
    yy=bub(d,x,yy,w,t,False)
  d.text((x+16,yy+6),"Trâm is typing…",font=F(15,False),fill=(37,160,90))
phone((236,229,221),"+84 90 ••• ••• (Trâm)",(7,94,84),"p05",wa,base="raw/f02.png")
# 09 typing + delete
def typ(d,x,y,w):
  yy=y+26
  for t in["hi is this snap saigon? weird request…","…can you follow him and take photos?"]:yy=bub(d,x,yy,w,t,False)
  d.rounded_rectangle((x+12,y+560,x+w-12,y+612),26,fill="white")
  d.text((x+30,y+574),"I'm a wedding photographer|",font=F(19,False),fill=(20,20,20))
  d.line((x+30,y+586,x+300,y+586),fill=(230,60,60),width=3)
  d.text((x+30,y+622),"✕ deleted → \"ok but why me|\" ✕ deleted".replace("✕","x"),font=F(15,False),fill=(160,60,60))
  for r in range(3):
    for c in range(10):d.rounded_rectangle((x+14+c*37,y+660+r*46,x+46+c*37,y+698+r*46),6,fill=(250,250,250))
phone((236,229,221),"Trâm",(7,94,84),"p09",typ,base="raw/f07.png")
# 12 Tinder chat classified
def tchat(d,x,y,w):
  yy=y+20
  yy=bub(d,x,yy,w,"J: so what are you up to tomorrow? ;)",False,col_them=(242,242,246))
  yy=bub(d,x,yy,w,"can't say. classified 🤫".replace(" 🤫"," (shh)"),True,col_me=(255,214,222))
  yy=bub(d,x,yy,w,"J: a woman of mystery. I like it",False,col_them=(242,242,246))
  d.rounded_rectangle((x+20,yy+40,x+w-20,yy+130),24,fill=(255,199,39));d.text((x+40,yy+52),"Hân, thinking…",font=F(15),fill=(30,22,84))
  d.text((x+40,yy+78),"I am SO mysterious.",font=F(24),fill=(30,22,84))
phone((255,255,255),"J",(255,90,110),"p12",tchat,base="raw/f11.png")
# 08 thought-burst over f07
im=Image.open("img/f07.jpg");d=ImageDraw.Draw(im)
for i,(t,y) in enumerate([("PI ERA.",120),("he's 100% cheating.",230),("secret TWO wives??",340)]):
  f=F(30);w=d.textlength(t,font=f)+40;x=40+i*40
  d.rounded_rectangle((x,y,x+w,y+70),22,fill=(255,199,39));d.text((x+20,y+17),t,font=f,fill=(30,22,84))
im.save("img/p08.jpg",quality=86)
print("ok")
