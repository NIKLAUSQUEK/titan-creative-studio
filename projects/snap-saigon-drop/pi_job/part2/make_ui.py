from PIL import Image,ImageDraw,ImageFont,ImageFilter
W,H=540,960;FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FR="/usr/share/fonts/opentype/inter/Inter-Medium.otf"
def F(s,b=True):return ImageFont.truetype(FB if b else FR,s)
def phone(bg,title,top_bg,fn,body,base):
  im=Image.open(base).convert("RGB").resize((W,H)).filter(ImageFilter.GaussianBlur(14));d=ImageDraw.Draw(im,"RGBA");px,py,pw,ph=70,70,400,820
  d.rounded_rectangle((px-10,py-10,px+pw+10,py+ph+10),46,fill=(20,20,24));d.rounded_rectangle((px,py,px+pw,py+ph),38,fill=bg)
  d.rounded_rectangle((px,py,px+pw,py+86),38,fill=top_bg);d.rectangle((px,py+50,px+pw,py+86),fill=top_bg);d.text((px+24,py+30),title,font=F(22),fill="white");d.text((px+pw-74,py+12),"15:12",font=F(15),fill="white")
  body(d,px,py+100,pw);im.save(f"img/{fn}.jpg",quality=86)
def bub(d,x,y,w,txt,mine,cm=(220,248,198),ct=(255,255,255)):
  f=F(19,False);lines=[];line=""
  for wd in txt.split():
    if d.textlength((line+" "+wd).strip(),font=f)>w-150:lines.append(line);line=wd
    else:line=(line+" "+wd).strip()
  lines.append(line);bw=max(d.textlength(l,font=f) for l in lines)+30;bh=len(lines)*26+18;bx=x+w-bw-16 if mine else x+16
  d.rounded_rectangle((bx,y,bx+bw,y+bh),14,fill=cm if mine else ct)
  for i,l in enumerate(lines):d.text((bx+15,y+9+i*26),l,font=f,fill=(20,20,20))
  return y+bh+12
def u1(d,x,y,w):
  yy=y+20;yy=bub(d,x,yy,w,"J: thinking about you at work ;)",False,ct=(242,242,246))
  d.rounded_rectangle((x+20,yy+30,x+w-20,yy+110),24,fill=(255,199,39));d.text((x+40,yy+42),"Hân, thinking…",font=F(15),fill=(30,22,84));d.text((x+40,yy+68),"he's so thoughtful.",font=F(24),fill=(30,22,84))
phone((255,255,255),"J",(255,90,110),"u1",u1,"raw/s04.png")
def u2(d,x,y,w):
  yy=y+20
  for t in["got the photos! thank you!!","wait… is he on his phone?","who is he texting?","is he with anyone?"]:yy=bub(d,x,yy,w,t,False)
  d.text((x+16,yy+6),"Trâm is typing…",font=F(15,False),fill=(37,160,90))
phone((236,229,221),"Trâm",(7,94,84),"u2",u2,"raw/s09.png")
def u3(d,x,y,w):
  yy=y+20;yy=bub(d,x,yy,w,"J: can't wait to see you tonight",False,ct=(242,242,246))
  yy=bub(d,x,yy,w,"J: wear something nice",False,ct=(242,242,246))
  d.rounded_rectangle((x+20,yy+30,x+w-20,yy+110),24,fill=(255,199,39));d.text((x+40,yy+42),"Hân, thinking…",font=F(15),fill=(30,22,84));d.text((x+40,yy+68),"ok J. you're ON.",font=F(24),fill=(30,22,84))
phone((255,255,255),"J",(255,90,110),"u3",u3,"raw/s12.png")
def u4(d,x,y,w):
  d.rounded_rectangle((x+20,y+30,x+w-20,y+500),22,fill=(255,255,255))
  d.text((x+44,y+56),"snapsaigon.com",font=F(22),fill=(30,22,84))
  d.rounded_rectangle((x+44,y+110,x+w-44,y+200),16,fill=(232,246,236));d.text((x+64,y+128),"Booking extended",font=F(26),fill=(31,138,76));d.text((x+64,y+166),"+2 hours · paid by Trâm",font=F(18,False),fill=(60,110,80))
  for i,(k,v) in enumerate([("Time","6:00 pm - 8:00 pm"),("Snapper","Hân"),("Note","\"please, one more shift\"")]):
    d.text((x+44,y+240+i*58),k,font=F(16,False),fill=(120,120,130));d.text((x+190,y+240+i*58),v,font=F(20),fill=(30,22,84))
phone((236,229,221),"snapsaigon.com",(30,22,84),"u4",u4,"raw/s02.png")
print("ok")
