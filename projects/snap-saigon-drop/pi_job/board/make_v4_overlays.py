from PIL import Image,ImageDraw,ImageFont,ImageOps
W,H=540,960;FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FR="/usr/share/fonts/opentype/inter/Inter-Medium.otf"
def F(s,b=True):return ImageFont.truetype(FB if b else FR,s)
V="../v4set/"
def load(n):return Image.open(V+n+".png").convert("RGB").resize((W,H),Image.LANCZOS)
for a,b in[("s01","v4_h1"),("s02","v4_h2"),("s03r","v4_h3"),("s05r","v4_h5"),("s06r","v4_h6"),("s07","v4_h7")]:load(a).save(f"img/{b}.jpg",quality=86)
def call_tile(base,name,fn,t):
  im=load(base);d=ImageDraw.Draw(im,"RGBA")
  d.rounded_rectangle((8,8,W-8,H-8),30,outline=(255,255,255,200),width=4)
  d.rounded_rectangle((26,28,26+190,28+44),22,fill=(0,0,0,150));d.ellipse((38,42,52,56),fill=(40,200,100));d.text((62,36),f"{name}  {t}",font=F(18),fill="white")
  sv=load("s05r").crop((60,260,480,820)).resize((120,160));im.paste(sv,(W-150,34));d=ImageDraw.Draw(im,"RGBA");d.rounded_rectangle((W-150,34,W-30,194),14,outline=(255,255,255),width=3)
  for i,c in enumerate([(255,255,255,60),(255,255,255,60),(235,60,60,255)]):
    cx=W//2-80+i*80;d.ellipse((cx-28,H-130,cx+28,H-74),fill=c)
  d.text((W//2-9,H-122),"x",font=F(30),fill="white")
  im.save(f"img/{fn}.jpg",quality=86)
call_tile("s09r","Trâm","v4_t1call","00:14");call_tile("s10","Trâm","v4_t2call","00:31");call_tile("s11","Trâm","v4_t3call","00:49")
# incoming video call banner over the annoyed close-up
im=load("s04");d=ImageDraw.Draw(im,"RGBA")
d.rounded_rectangle((18,34,W-18,214),30,fill=(24,24,30,240));d.ellipse((38,56,98,116),fill=(80,80,96));d.text((57,66),"?",font=F(36),fill="white")
d.text((116,58),"Incoming video call",font=F(16,False),fill=(170,170,180));d.text((116,82),"Unknown number",font=F(24),fill="white");d.text((116,116),"Snap Saigon enquiry",font=F(16,False),fill=(170,170,180))
d.rounded_rectangle((38,150,W//2-8,200),24,fill=(235,60,60));d.text((78,162),"Decline",font=F(20),fill="white");d.rounded_rectangle((W//2+8,150,W-38,200),24,fill=(40,190,100));d.text((W//2+58,162),"Accept",font=F(20),fill="white")
d.rounded_rectangle((W/2-150,H-170,W/2+150,H-110),20,fill=(0,0,0,170));d.text((W/2-128,H-156),"\"…seriously? at 11pm?\"",font=F(21),fill="white")
im.save("img/v4_h4call.jpg",quality=86)
# booking approved banner over the 'sure' close-up
im=load("s08");d=ImageDraw.Draw(im,"RGBA")
d.rounded_rectangle((18,34,W-18,170),26,fill=(255,255,255,245));d.ellipse((38,54,92,108),fill=(30,22,84));d.text((53,64),"S",font=F(30),fill=(255,199,39))
d.text((108,52),"snapsaigon.com · now",font=F(15,False),fill=(110,110,120));d.text((108,76),"Booking approved",font=F(24),fill=(31,138,76));d.text((108,112),"Paid · tomorrow 2:00–6:00 pm",font=F(17,False),fill=(50,50,60))
im.save("img/v4_h8book.jpg",quality=86)
print("ok")
