"""Transparent 1080x1920 chat-bubble overlays for the video edit (same look as the board)."""
from PIL import Image,ImageDraw,ImageFont
S=2;W,H=540*S,960*S;FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FR="/usr/share/fonts/opentype/inter/Inter-Medium.otf"
def F(s,b=True):return ImageFont.truetype(FB if b else FR,s*S)
GREEN=(7,94,84);PINK=(255,90,110)
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w and line:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def overlay(fn,chip,col,msgs,y0,upto=None):
  ov=Image.new("RGBA",(W,H),(0,0,0,0));d=ImageDraw.Draw(ov);f=F(21,False);msgs=msgs[:upto] if upto else msgs
  rows=[]
  for who,t in msgs:
    ls=wrap(d,t,f,330*S);bw=max(d.textlength(l,font=f) for l in ls)+32*S;bh=len(ls)*28*S+20*S;rows.append((who,ls,bw,bh))
  tot=sum(r[3]+10*S for r in rows)+60*S;y0*=S
  d.rounded_rectangle((24*S,y0-6*S,W-24*S,y0+tot),26*S,fill=(18,16,30,150))
  d.rounded_rectangle((36*S,y0+8*S,36*S+d.textlength(chip,font=F(15))+30*S,y0+38*S),15*S,fill=col+(255,));d.text((50*S,y0+14*S),chip,font=F(15),fill="white")
  y=y0+52*S
  for who,ls,bw,bh in rows:
    x=W-40*S-bw if who=="out" else 40*S
    d.rounded_rectangle((x,y,x+bw,y+bh),16*S,fill=((220,248,198,245) if col==GREEN else (255,214,222,245)) if who=="out" else (255,255,255,245))
    for i,l in enumerate(ls):d.text((x+16*S,y+10*S+i*28*S),l,font=f,fill=(20,20,20))
    y+=bh+10*S
  ov.save(fn)
import os;os.makedirs("ov",exist_ok=True)
overlay("ov/han_out.png","WhatsApp · +84 90 ••• •••",GREEN,[("out","Hi! Snap Saigon here. Can't talk right now. How can I help?")],590)
msgs=[("in","hi! I need natural shots of my model tomorrow, from afar"),("in","he's very camera shy, so don't let him notice"),("in","he'll be at a co-working space. I've paid your entry already"),("in","a few natural shots every hour. I'll send the address")]
for k in range(1,5):overlay(f"ov/brief_{k}.png","WhatsApp · Trâm",GREEN,msgs,420,upto=k)
print("ok")
