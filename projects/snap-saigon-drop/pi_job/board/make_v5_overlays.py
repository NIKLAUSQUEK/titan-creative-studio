"""v5 storyboard: texts appear as bubbles OVER the characters' own shots (no cutaways to flat mock-ups); swipe cards with photos + cringe bios."""
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageOps
W,H=540,960;FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FR="/usr/share/fonts/opentype/inter/Inter-Medium.otf";FX="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
def F(s,b=True,x=False):return ImageFont.truetype(FX if x else (FB if b else FR),s)
V="../v4set/";PINK=(255,90,110);GREEN=(7,94,84);NAVY=(30,22,84);YEL=(255,199,39)
def load(n):return Image.open(V+n+".png").convert("RGB").resize((W,H),Image.LANCZOS)
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w and line:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def chat(base,fn,chip,col,msgs,y0=560,thought=None):
  im=load(base).convert("RGBA");ov=Image.new("RGBA",(W,H),(0,0,0,0));d=ImageDraw.Draw(ov);f=F(21,False)
  rows=[]
  for who,t in msgs:
    ls=wrap(d,t,f,330);bw=max(d.textlength(l,font=f) for l in ls)+32;bh=len(ls)*28+20;rows.append((who,ls,bw,bh))
  tot=sum(r[3]+10 for r in rows)+60
  d.rounded_rectangle((24,y0-6,W-24,y0+tot),26,fill=(18,16,30,150))
  d.rounded_rectangle((36,y0+8,36+d.textlength(chip,font=F(15))+30,y0+38),15,fill=col+(255,));d.text((50,y0+14),chip,font=F(15),fill="white")
  y=y0+52
  for who,ls,bw,bh in rows:
    x=W-40-bw if who=="out" else 40
    d.rounded_rectangle((x,y,x+bw,y+bh),16,fill=((220,248,198,245) if who=="out" and col==GREEN else (255,214,222,245)) if who=="out" else (255,255,255,245))
    for i,l in enumerate(ls):d.text((x+16,y+10+i*28),l,font=f,fill=(20,20,20))
    y+=bh+10
  if thought:
    ft=F(24);ls=wrap(d,thought,ft,380);bh=len(ls)*32+52;bw=max(d.textlength(l,font=ft) for l in ls)+48;x=(W-bw)/2;yy=70
    d.rounded_rectangle((x,yy,x+bw,yy+bh),26,fill=YEL+(255,));d.text((x+22,yy+10),"Hân, thinking…",font=F(13),fill=NAVY)
    for i,l in enumerate(ls):d.text((x+22,yy+30+i*32),l,font=ft,fill=NAVY)
  Image.alpha_composite(im,ov).convert("RGB").save(f"img/{fn}.jpg",quality=86)
# --- swipe cards: photo + cringe bio ---
cards=[("m1","Brad, 38","Moved here 6 months ago. Looking for a traditional Asian girl, not like those Western girls \U0001F644".replace("\U0001F644",":/"),"ugh."),
       ("m2","Chad, 41","Passport bro. Teach me Vietnamese. First word: \"yes\".","ugh. gross."),
       ("m3","Greg, 45","My ex was Thai. My ex-ex was Filipina. Plot twist: I'm a great listener ;)","ugh. passport bros.")]
for i,(m,nm,bio,th) in enumerate(cards,1):
  im=load("s02").filter(ImageFilter.GaussianBlur(14));d=ImageDraw.Draw(im,"RGBA");px,py,pw,ph=60,60,420,840
  d.rounded_rectangle((px-10,py-10,px+pw+10,py+ph+10),46,fill=(20,20,24));d.rounded_rectangle((px,py,px+pw,py+ph),38,fill=(255,255,255))
  d.rounded_rectangle((px,py,px+pw,py+80),38,fill=PINK);d.rectangle((px,py+44,px+pw,py+80),fill=PINK);d.text((px+22,py+26),"Tindre",font=F(22),fill="white")
  ph_=ImageOps.fit(Image.open(V+m+".png").convert("RGB"),(pw-40,430),centering=(0.5,0.3));im.paste(ph_,(px+20,py+96));d=ImageDraw.Draw(im,"RGBA")
  d.text((px+24,py+544),nm,font=F(30),fill=NAVY)
  for k,l in enumerate(wrap(d,bio,F(19,False),pw-48)):d.text((px+24,py+590+k*26),l,font=F(19,False),fill=(70,70,90))
  d.ellipse((px+80,py+736,px+150,py+806),fill=(255,255,255),outline=(220,60,60),width=5);d.text((px+104,py+750),"X",font=F(34),fill=(220,60,60))
  d.ellipse((px+pw-150,py+736,px+pw-80,py+806),fill=(255,255,255),outline=(40,170,90),width=5);d.text((px+pw-126,py+752),"<3",font=F(24),fill=(40,170,90))
  ft=F(22);tw=d.textlength(th,font=ft)+44;d.rounded_rectangle((W/2-tw/2,H-100,W/2+tw/2,H-50),24,fill=YEL+(255,));d.text((W/2-tw/2+22,H-90),th,font=ft,fill=NAVY)
  im.save(f"img/v5_card{i}.jpg",quality=86)
# --- interruption: declined, not accepted ---
im=load("s04");d=ImageDraw.Draw(im,"RGBA")
d.rounded_rectangle((18,34,W-18,214),30,fill=(24,24,30,240));d.ellipse((38,56,98,116),fill=(80,80,96));d.text((57,66),"?",font=F(36),fill="white")
d.text((116,58),"Incoming video call",font=F(16,False),fill=(170,170,180));d.text((116,82),"Unknown number",font=F(24),fill="white");d.text((116,116),"Snap Saigon enquiry",font=F(16,False),fill=(170,170,180))
d.rounded_rectangle((38,150,W//2-8,200),24,fill=(235,60,60));d.text((78,162),"Decline",font=F(20),fill="white");d.rounded_rectangle((W//2+8,150,W-38,200),24,fill=(70,70,80));d.text((W//2+58,162),"Accept",font=F(20),fill=(140,140,150))
d.ellipse((60,130,128,218),outline=(255,255,255,230),width=4)
d.rounded_rectangle((W/2-150,H-170,W/2+150,H-110),20,fill=(0,0,0,170));d.text((W/2-128,H-156),"\"…seriously? Nope.\"",font=F(21),fill="white")
im.save("img/v5_decline.jpg",quality=86)
# --- text overlays on the characters' own shots ---
chat("h5c","v5_text_han",  "WhatsApp · +84 90 ••• •••",GREEN,[("out","Hi! Snap Saigon here. Can't talk right now. How can I help?")],y0=590)
chat("tt1c","v5_text_brief","WhatsApp · Trâm",GREEN,[("in","hi! I need natural shots of my model tomorrow, from afar"),("in","he's very camera shy, so don't let him notice"),("in","he'll be at a co-working space. I've paid your entry already"),("in","a few natural shots every hour. I'll send the address")],y0=420)
chat("tt1c","v5_text_rules","WhatsApp · Trâm",GREEN,[("in","just 2 rules:"),("in","1) don't talk to him"),("in","2) only talk to me. got it?"),("out","got it!")],y0=450)
chat("tt2","v5_text_perfect","WhatsApp · Trâm",GREEN,[("in","perfect. remember… only talk to me.")],y0=640)
chat("s02","v5_text_j","Tindre · J",PINK,[("in","what are you up to tomorrow? ;)"),("out","can't say. classified (shh)"),("in","mysterious. i like it"),("in","i'll reveal everything tomorrow. including my face ;)")],y0=380,thought="…wait. have I ever seen his face?")
# plain frames for the board
for a,b in[("h5c","v5_h5c"),("tt1c","v5_tt1"),("tt2","v5_tt2")]:load(a).save(f"img/{b}.jpg",quality=86)
print("ok")
