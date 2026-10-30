"""The PI Job, Series A carousel (8 slides, 1080x1350). python3 carousel.py <frames_dir> <out_dir>"""
import sys,os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
FR,OUT=sys.argv[1:3];os.makedirs(OUT,exist_ok=True)
B="/usr/share/fonts/opentype/inter/Inter-Bold.otf";R="/usr/share/fonts/opentype/inter/Inter-Medium.otf"
def F(s,b=True):return ImageFont.truetype(B if b else R,s)
NAVY=(30,22,84);Y=(255,199,39);W,H=1080,1350
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def bg(frame=None,blur=0,dim=0):
  if frame:
    im=Image.open(f"{FR}/{frame}").convert("RGB");s=max(W/im.width,H/im.height);im=im.resize((int(im.width*s),int(im.height*s)))
    im=im.crop(((im.width-W)//2,(im.height-H)//2,(im.width-W)//2+W,(im.height-H)//2+H))
    if blur:im=im.filter(ImageFilter.GaussianBlur(blur))
    if dim:im=Image.blend(im,Image.new("RGB",(W,H),(10,8,30)),dim)
    return im
  return Image.new("RGB",(W,H),NAVY)
def headline(im,text,y=90,size=72,col="white",hl=None):
  d=ImageDraw.Draw(im);f=F(size)
  for ln in wrap(d,text,f,W-140):
    x=70
    for w in ln.split(" "):
      c=Y if hl and w.strip("…,.!?'\"").lower() in hl else col
      d.text((x,y),w,font=f,fill=c,stroke_width=4,stroke_fill=(0,0,0));x+=d.textlength(w+" ",font=f)
    y+=size+16
  return y
def chat(im,msgs,y=380,title=None):
  d=ImageDraw.Draw(im)
  if title:
    d.rounded_rectangle((60,y-90,W-60,y-20),20,fill=(245,245,250));d.text((90,y-74),title,font=F(34),fill=NAVY);
  f=F(40,False)
  for who,t in msgs:
    if who=="note":
      tw=d.textlength(t,font=F(30));d.rounded_rectangle(((W-tw)/2-24,y,(W+tw)/2+24,y+56),28,fill=(255,255,255,));d.text(((W-tw)/2,y+12),t,font=F(30),fill=(20,150,90));y+=80;continue
    lines=wrap(d,t,f,640);bw=max(d.textlength(l,font=f) for l in lines)+56;bh=len(lines)*52+36
    me=who=="me";x=W-70-bw if me else 70
    d.rounded_rectangle((x,y,x+bw,y+bh),30,fill=(37,211,102) if me else (255,255,255))
    yy=y+18
    for l in lines:d.text((x+28,yy),l,font=f,fill=(10,10,10));yy+=52
    y+=bh+22
  return y
def tag(im,text="snap saigon shoots photos, not PI work (this one's a story)"):
  d=ImageDraw.Draw(im);f=F(24,False);d.text((70,H-60),text.replace("😅",":)"),font=f,fill=(220,220,235))
def num(im,n):
  d=ImageDraw.Draw(im);d.text((W-140,H-64),f"{n}/8",font=F(28),fill=Y)
S=[]
im=bg("a41.png",dim=0.35);headline(im,"my customer's boyfriend cheated on her… with me",y=860,size=88,hl={"with","me"});ImageDraw.Draw(im).text((70,80),"snap saigon · the weirdest booking",font=F(30),fill=Y);S.append(im)
im=bg("a11.png",blur=18,dim=0.55);headline(im,"it started with a WhatsApp at 11pm",y=90,size=56)
chat(im,[("them","hi is this snap saigon? weird request…"),("them","my bf says he has a 'late client meeting' tonight. won't say where"),("them","he's ALWAYS on his phone lately")],y=420,title="Trâm (new customer)");S.append(im)
im=bg("a11.png",blur=18,dim=0.55);headline(im,"then she asked me to do this:",y=90,size=56)
chat(im,[("them","I know where he works. can you follow his day and take photos? "),("me","I'm a wedding photographer lol"),("them","I'll pay double"),("me","…send the address")],y=420,title="Trâm (new customer)");S.append(im)
im=bg("a21.png",dim=0.15);headline(im,"so I spent my afternoon behind a bánh mì cart",y=980,size=60,hl={"bánh","mì","cart"});S.append(im)
im=bg("a22.png",blur=18,dim=0.55);headline(im,"my shift ended. she begged.",y=90,size=56)
chat(im,[("me","booking's done! I have a dinner date tonight"),("them","PLEASE. booking 2 more hours on the website rn pls"),("note","Booking confirmed · +2 hours"),("me","fine. where is he now?"),("them","near Bitexco I think")],y=420,title="Trâm (new customer)");S.append(im)
im=bg("a31.png",blur=18,dim=0.55);headline(im,"meanwhile, my tinder date:",y=90,size=56)
chat(im,[("me","where are we meeting? I'm near Bitexco"),("them","omg me too haha I'm at the café right under the tower"),("them","just got here, I'm in the corner ;)")],y=420,title="J (Tinder)");S.append(im)
im=bg("a32.png",dim=0.1);headline(im,"I looked up from my phone.",y=980,size=66);headline(im,"he was in the corner.",y=1070,size=66,hl={"corner."});S.append(im)
im=bg("a33.png",dim=0.35);headline(im,"my customer's boyfriend… was my date.",y=860,size=78,hl={"date."})
ImageDraw.Draw(im).text((70,1150),"comment PART 4 and I'll tell you what I did next ".replace("👀",""),font=F(40),fill=Y);S.append(im)
for i,im in enumerate(S,1):
  tag(im);num(im,i);im.save(f"{OUT}/slide{i}.jpg",quality=90)
print("ok",len(S))
