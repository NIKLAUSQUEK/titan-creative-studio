from PIL import Image, ImageDraw, ImageFont
W,H=1080,1920
DJ="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"; EMO="/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
COR="/tmp/fonts/Cormorant-Italic.ttf"; PLA="/tmp/fonts/Playfair-Italic.ttf"
def canvas(): return Image.new("RGBA",(W,H),(0,0,0,0))
def ctext(d,y,txt,font,fill,stroke=0,sfill=None):
    w=d.textlength(txt,font=font); d.text(((W-w)/2,y),txt,font=font,fill=fill,stroke_width=stroke,stroke_fill=sfill)
# captions
def caption(name,txt):
    im=canvas(); d=ImageDraw.Draw(im); f=ImageFont.truetype(DJ,46)
    ctext(d,int(H*0.74)-28,txt,f,"white",4,"black"); im.save(f"cap_{name}.png")
caption("1","Bro... are you spotting?")
caption("2","Hmph. You're only doing the bar.")
caption("3","Yeah... but are you REALLY spotting?")
caption("4","What?")
# hook
im=canvas(); d=ImageDraw.Draw(im); f=ImageFont.truetype(DJ,74)
ctext(d,300,"BUFF BOY PISSES HIMSELF",f,"white",6,"black")
l2="IN GYM "; w=d.textlength(l2,font=f); ew=88; x=(W-(w+ew))/2
d.text((x,392),l2,font=f,fill="white",stroke_width=6,stroke_fill="black")
e=Image.new("RGBA",(160,160),(0,0,0,0)); ImageDraw.Draw(e).text((0,0),"😂",font=ImageFont.truetype(EMO,109),embedded_color=True)
e=e.crop(e.getbbox()).resize((ew,ew),Image.LANCZOS); im.alpha_composite(e,(int(x+w),402)); im.save("hook.png")
# turn card
im=canvas(); d=ImageDraw.Draw(im); ctext(d,840,"Leaking when you lift?",ImageFont.truetype(COR,88),"#EFE3D3"); im.save("card1.png")
im=canvas(); d=ImageDraw.Draw(im); ctext(d,960,"Common. Not normal.",ImageFont.truetype(PLA,96),"#EFE3D3"); im.save("card2.png")
# nik panel + conditions + brand
im=canvas(); ImageDraw.Draw(im).rectangle([0,1300,W,H],fill=(0xEF,0xE3,0xD3,224)); im.save("panel.png")
cf=ImageFont.truetype(COR,80)
for i,t in enumerate(["Erectile dysfunction","Premature ejaculation","Pelvic pain","Prostate conditions"]):
    im=canvas(); d=ImageDraw.Draw(im); ctext(d,1360+i*112,t,cf,"#4E3B2E"); im.save(f"cond{i}.png")
im=canvas(); d=ImageDraw.Draw(im); ctext(d,1470,"Physio Spot",ImageFont.truetype(PLA,104),"#4E3B2E")
ctext(d,1615,"men's health physiotherapy",ImageFont.truetype(COR,58),"#6B5544"); im.save("brand.png")
print("ok")
