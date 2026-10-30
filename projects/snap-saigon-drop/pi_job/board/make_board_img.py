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
  for t in["hi! I need shots of my model tomorrow, from afar. he's very camera shy so don't let him notice","he'll be at a co-working space, just looking busy. I've paid your entry already","a few natural shots every hour. I'll send the address"]:
    yy=bub(d,x,yy,w,t,False)
  d.text((x+16,yy+6),"Trâm is typing…",font=F(15,False),fill=(37,160,90))
phone((236,229,221),"+84 90 ••• ••• (Trâm)",(7,94,84),"p05",wa,base="raw/f02.png")
# 09 typing + delete
def typ(d,x,y,w):
  yy=y+26
  for t in["just 2 rules:","1) don't talk to him","2) only talk to me. got it?"]:yy=bub(d,x,yy,w,t,False)
  d.rounded_rectangle((x+12,y+560,x+w-12,y+612),26,fill="white")
  d.text((x+30,y+574),"why can't I talk to h|",font=F(19,False),fill=(20,20,20))
  d.line((x+30,y+586,x+300,y+586),fill=(230,60,60),width=3)
  d.text((x+30,y+622),"x deleted → \"is this legal\" x deleted",font=F(15,False),fill=(160,60,60))
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
for i,(t,y) in enumerate([("a camera-shy… model?",120),("don't TALK to him??",230),("this is so sus.",340)]):
  f=F(30);w=d.textlength(t,font=f)+40;x=40+i*40
  d.rounded_rectangle((x,y,x+w,y+70),22,fill=(255,199,39));d.text((x+20,y+17),t,font=f,fill=(30,22,84))
im.save("img/p08.jpg",quality=86)
print("ok")
# p07r: the 2 rules land (no typing yet)
def rules(d,x,y,w):
  yy=y+26
  for t in["a few natural shots every hour. I'll send the address","just 2 rules:","1) don't talk to him","2) only talk to me. got it?"]:yy=bub(d,x,yy,w,t,False)
phone((236,229,221),"Trâm",(7,94,84),"p07r",rules,base="raw/f06.png")
# p11 thought over customer-service smile
im=Image.open("img/f10b.jpg");d=ImageDraw.Draw(im)
f=F(30);t="good customer service. 5 stars."
w_=d.textlength(t,font=f)+40;d.rounded_rectangle((40,120,40+w_,190),22,fill=(255,199,39));d.text((60,137),t,font=f,fill=(30,22,84))
im.save("img/p11.jpg",quality=86)

# p05b: snapsaigon.com booking approval + payment
def booking(d,x,y,w):
  d.rounded_rectangle((x+20,y+30,x+w-20,y+700),22,fill=(255,255,255))
  d.text((x+44,y+56),"snapsaigon.com",font=F(22),fill=(30,22,84))
  d.rounded_rectangle((x+44,y+110,x+w-44,y+200),16,fill=(232,246,236));d.text((x+64,y+128),"Booking approved",font=F(26),fill=(31,138,76));d.text((x+64,y+166),"Payment received",font=F(18,False),fill=(60,110,80))
  for i,(k,v) in enumerate([("Date","Tomorrow"),("Time","2:00 pm - 6:00 pm"),("Snapper","Hân (Junior)"),("Where","address to follow")]):
    d.text((x+44,y+240+i*58),k,font=F(16,False),fill=(120,120,130));d.text((x+190,y+240+i*58),v,font=F(20),fill=(30,22,84))
  d.rounded_rectangle((x+44,y+520,x+w-44,y+580),30,fill=(255,199,39));d.text((x+w/2-80,y+536),"Confirmed ✓".replace("✓","(ok)"),font=F(24),fill=(30,22,84))
phone((236,229,221),"snapsaigon.com",(30,22,84),"p05b",booking,base="raw/f02.png")
