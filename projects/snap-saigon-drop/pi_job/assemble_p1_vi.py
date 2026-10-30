"""PI Job Part 1 'The Booking' v1 (480p draft): ONE timeline (continuous room tone + music bed, J/L-cuts, drift, one caption/thought style).
python3 assemble_p1_vi.py <out.mp4>   needs p1/clips/{c02,c04,c06,c07,c10,c11,c13}.mp4, p1/vo/L*.mp3, p1/f13b.jpg, p1/ui/*.png"""
import subprocess,sys,os
import numpy as np
from PIL import Image,ImageDraw,ImageFont
OUT=sys.argv[1];W="_p1vi";os.makedirs(W,exist_ok=True)
FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FX="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
def F(s,f=FB):return ImageFont.truetype(f,s)
def run(a):subprocess.run(["ffmpeg","-y","-v","error"]+a,check=True)
def dur(f):return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)
def speech(f,th="-35dB"):
  r=subprocess.run(["ffmpeg","-i",f,"-af",f"silencedetect=noise={th}:d=0.15","-f","null","-"],capture_output=True,text=True).stderr
  st=[float(l.split("silence_start: ")[1].split()[0]) for l in r.splitlines() if "silence_start" in l]
  en=[float(l.split("silence_end: ")[1].split()[0]) for l in r.splitlines() if "silence_end" in l]
  D=dur(f);a=en[0] if st and st[0]<0.05 and en else 0.0
  b=st[-1] if st and st[-1]>a+0.3 else D
  return a,b
def env(f):
  raw=subprocess.run(["ffmpeg","-v","error","-i",f,"-ac","1","-ar","8000","-f","s16le","-"],capture_output=True).stdout
  a=np.abs(np.frombuffer(raw,dtype=np.int16).astype(float));e=np.convolve(a,np.ones(400)/400,"same")[::80]
  return (e-e.mean())/(e.std()+1e-9)
def offset(clip,line):
  c=np.correlate(env(clip),env(line),"full");return max(0.0,(c.argmax()-len(env(line))+1)*0.01)
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w and line:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def png(name,draw):
  im=Image.new("RGBA",(1080,1920),(0,0,0,0));draw(ImageDraw.Draw(im));im.save(f"{W}/{name}.png");return f"{W}/{name}.png"
def cap_words(name,text,shown,size=58):
  def d(dr):
    f=F(size,FX);lines=wrap(dr,text,f,900);y=1430;k=0
    for ln in lines:
      lw=dr.textlength(ln,font=f);x=(1080-lw)/2
      for wd in ln.split():
        col=(255,199,39) if k==shown-1 else (255,255,255)
        if k<shown:dr.text((x,y),wd,font=f,fill=col,stroke_width=7,stroke_fill=(0,0,0))
        x+=dr.textlength(wd+" ",font=f);k+=1
      y+=size+18
  return png(name,d)
def cap_line(name,text,size=50,y=1420):
  def d(dr):
    f=F(size,FX);lines=wrap(dr,text,f,900);yy=y
    for ln in lines:
      lw=dr.textlength(ln,font=f);x=(1080-lw)/2
      dr.rounded_rectangle((x-20,yy-8,x+lw+20,yy+size+16),16,fill=(0,0,0,185));dr.text((x,yy),ln,font=f,fill="white");yy+=size+26
  return png(name,d)
def bubble(name,text):
  def d(dr):
    f=F(46);ls=wrap(dr,text,f,800);bh=len(ls)*58+70;bw=max(dr.textlength(l,font=f) for l in ls)+64;x=(1080-bw)/2;y=250
    dr.rounded_rectangle((x,y,x+bw,y+bh),32,fill=(255,199,39));dr.text((x+32,y+12),"Hân nghĩ thầm…",font=F(26),fill=(30,22,84))
    yy=y+48
    for l in ls:dr.text((x+32,yy),l,font=f,fill=(30,22,84));yy+=58
    dr.ellipse((x+bw*0.3,y+bh+10,x+bw*0.3+34,y+bh+44),fill=(255,199,39));dr.ellipse((x+bw*0.3-26,y+bh+54,x+bw*0.3-6,y+bh+74),fill=(255,199,39))
  return png(name,d)
def top(name,text,sub=None):
  def d(dr):
    f=F(62,FX);y=150
    for ln in wrap(dr,text,f,960):
      w=dr.textlength(ln,font=f);dr.text(((1080-w)/2,y),ln,font=f,fill="white",stroke_width=7,stroke_fill=(0,0,0));y+=78
    if sub:
      y+=14
      for ln in wrap(dr,sub,F(42),940):
        w=dr.textlength(ln,font=F(42));dr.text(((1080-w)/2,y),ln,font=F(42),fill=(255,199,39),stroke_width=5,stroke_fill=(0,0,0));y+=54
  return png(name,d)
shots=[];audio=[];sfx=[];T=[0.0]
def add(src,ss,du,still=False,ov=(),fx=None,label=""):
  shots.append(dict(src=src,ss=ss,du=du,still=still,ov=list(ov),fx=fx,t=T[0]));T[0]+=du
def vo(line,at,g=1.0):a,b=speech(line);audio.append((line,at-a,g));return a,b
def say(clip,line,text,lead=0.1,tail=0.35,g=1.15):
  """lip-synced clip line: our clean line aligned to the clip's own sync, shot trimmed round it (J-cut by `lead`)"""
  lag=offset(clip,line);a,b=speech(line);ln=b-a
  ss=max(0.0,lag+a-0.1+lead);du=min(dur(clip)-ss,ln+tail+0.1)
  audio.append((line,T[0]-lead-a,g))
  ov=[(cap_line(f"vn{len(shots)}",text),T[0],T[0]+du)]
  add(clip,ss,du,ov=ov)
def think(line,text,at):
  q=f"{W}/th_{os.path.basename(line).split('.')[0]}.wav"
  run(["-i",line,"-af","silenceremove=start_periods=1:start_threshold=-40dB:stop_periods=-1:stop_duration=0.3:stop_threshold=-40dB:stop_silence=0.2,atempo=1.0","-ar","44100",q]);line=q
  a,b=speech(line);audio.append((line,at-a,1.0));return (bubble(f"b{len(audio)}",text),at,at+(b-a)+0.45),(b-a)
def pop(t,kind="msg"):sfx.append((kind,t))
C="p1/clips";V="p1/vo";U="p1/ui"
# 1 cold open: freeze on the fake-moustache detective, VO "you might be wondering how I got here…"
hook=top("hook","rule #1: don't talk to him. rule #2: only talk to me.","luật 1: đừng nói chuyện với anh ấy · luật 2: chỉ nói chuyện với mình")
vn0=cap_line("vn0","Có thể bạn đang thắc mắc sao mình lại ở đây…")
a,b=speech(f"{V}/L01.mp3");vo(f"{V}/L01.mp3",T[0]+0.15)
pop(T[0]+0.0,"street");add("p1/f13b.jpg",0,b-a+0.7,still=True,ov=[(hook,0,b-a+0.9),(vn0,0.1,b-a+0.8)],fx="scratch")
SCR=T[0]
# 2 bedroom wide, "no… no… ew…"
add(f"{C}/c02.mp4",0.0,0.0001);shots.pop()
say(f"{C}/c02.mp4",f"{V}/L02.mp3","không… không… ghê… không…",tail=0.5)
# 3 match UI + chime, 4 "oh" CU (silent clip) + thought
pop(T[0],"match");add(f"{U}/p03.png",0,1.4,still=True,ov=[(cap_line("vnU3","J: trông bạn là loại rắc rối đó nha ;)"),T[0]+0.2,T[0]+1.4)])
add(f"{C}/c04.mp4",0.0,1.1);vo(f"{V}/L03.mp3",T[0]-0.7)
b1,l1=think(f"{V}/L04.mp3","gõ nhanh ghê. đúng chuẩn người hành động.",T[0]+0.05)
add(f"{C}/c04.mp4",1.2,l1+0.6,ov=[b1])
# 5 WhatsApp brief (messages pop), 5b booking approved
for k in range(3):pop(T[0]+0.15+k*0.55,"msg")
add(f"{U}/p05.png",0,2.7,still=True,ov=[(cap_line("vnU5","Mình cần chụp tự nhiên người mẫu của mình từ xa. Anh ấy ngại ống kính, đừng để anh ấy biết nhé."),T[0]+0.3,T[0]+2.7)])
pop(T[0]+0.1,"confirm");add(f"{U}/p05b.png",0,1.7,still=True,ov=[(cap_line("vnU5b","Đặt lịch đã được duyệt & thanh toán · 14:00–18:00 · Hân: Ok… đặt xong rồi."),T[0]+0.2,T[0]+1.7)]);vo(f"{V}/L06.mp3",T[0]+0.45)
# 6 Trâm, breezy: "it's nothing major, just natural shots."
say(f"{C}/c06.mp4",f"{V}/L07.mp3","Không có gì to tát đâu, chỉ chụp tự nhiên thôi.")
# 7 two rules land, one by one
for k in range(3):pop(T[0]+0.1+k*0.5,"msg")
add(f"{U}/p07r.png",0,2.3,still=True,ov=[(cap_line("vnU7","Chỉ 2 luật thôi. 1) Không nói chuyện với anh ấy. 2) Chỉ nói chuyện với mình. Hiểu chưa?"),T[0]+0.3,T[0]+2.3)])
# 8 bolt upright (silent clip + whoosh/splat) + 9 thoughts x3 (0.4 s each)
pop(T[0],"whoosh");add(f"{C}/c07.mp4",0.0,1.0);pop(T[0]-0.35,"splat")
t9=[("Người mẫu… ngại ống kính?",f"{V}/L09.mp3"),("Không được NÓI chuyện với anh ấy?",f"{V}/L10.mp3"),("Nghe đáng ngờ quá.",f"{V}/L11.mp3")]
ov=[];t0=T[0]
for txt,l in t9:
  bb,ll=think(l,txt,t0+0.05);ov.append(bb);pop(t0+0.02,"ding");t0+=ll+0.25
add(f"{C}/c07.mp4",0.9,t0-T[0]+0.05,ov=ov)
# 10 typing + deleting (UI), backspace sfx
for k in range(6):pop(T[0]+0.1+k*0.12,"key")
pop(T[0]+0.9,"bksp");pop(T[0]+1.05,"bksp");add(f"{U}/p09.png",0,2.0,still=True,ov=[(cap_line("vnU9","Hân định hỏi… rồi lại xoá."),T[0]+0.2,T[0]+2.0)])
# 11 "Dạ được ạ! Chắc chắn làm được!" + thought
say(f"{C}/c10.mp4",f"{V}/L12.mp3","Dạ được ạ! Chắc chắn làm được!",tail=0.15)
b2,l2=think(f"{V}/L13.mp3","dịch vụ khách hàng tốt. năm sao.",T[0]+0.05)
add(f"{C}/c10.mp4",min(dur(f"{C}/c10.mp4")-1.5,3.0),l2+0.55,ov=[b2])
pop(T[0]-0.1,"send")
# 12 Trâm: "Tuyệt. Nhớ nhé, chỉ nói chuyện với mình thôi."
say(f"{C}/c11.mp4",f"{V}/L14.mp3","Tuyệt. Nhớ nhé, chỉ nói chuyện với mình thôi.",tail=0.1)
# 13 dating-app chat + "I am SO mysterious"
pop(T[0]+0.1,"ding");pop(T[0]+0.9,"ding")
b3,l3=think(f"{V}/L15.mp3","mình bí ẩn quá đi.",T[0]+0.3)
add(f"{U}/p12.png",0,max(l3+0.9,2.6),still=True,ov=[(cap_line("vnU12","J: mai bạn làm gì thế? ;)  ·  Hân: bí mật. tuyệt mật."),T[0]+0.2,T[0]+2.6)])
# 14 Day 1 loop: jaw drop + shades tip, hold
add(f"{C}/c13.mp4",0.0,3.5,fx="drop")
END=T[0]
end=top("end","Ngày 1.","Phần 2 → · bạn có nhận job này không?")
shots[-1]["ov"].append((end,END-2.5,END))
TOTAL=T[0]
VF="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30"
parts=[]
for i,s in enumerate(shots):
  o=f"{W}/p{i:02d}.mp4";du=s["du"]
  drift=f"scale=w='trunc(1080*(1+0.045*t/{du:.3f})/2)*2':h='trunc(1920*(1+0.045*t/{du:.3f})/2)*2':eval=frame,crop=1080:1920"
  if s["still"]:inp=["-loop","1","-t",f"{du+0.4:.3f}","-i",s["src"]]
  else:inp=["-ss",f"{s['ss']:.3f}","-t",f"{du+0.3:.3f}","-i",s["src"]]
  base=VF
  if s["fx"]=="scratch":base=f"{VF},eq=saturation=1.1"
  fc=f"[0:v]{base},tpad=stop_mode=clone:stop_duration=3,{drift}[v0]";last="v0";k=1;ins=list(inp)
  for (p,t0,t1) in s["ov"]:
    a=max(0,t0-s["t"]);b=min(du,t1-s["t"])
    if b<=0 or a>=du:continue
    ins+=["-i",p];fc+=f";[{last}][{k}:v]overlay=enable='between(t,{a:.3f},{b:.3f})'[v{k}]";last=f"v{k}";k+=1
  run(ins+["-filter_complex",fc,"-map",f"[{last}]","-t",f"{du:.3f}","-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-r","30","-an",o]);parts.append(o)
open(f"{W}/v.txt","w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
run(["-f","concat","-safe","0","-i",f"{W}/v.txt","-c","copy",f"{W}/v.mp4"])
# ---- audio: room tone (bedroom fan) + soft lo-fi bed + pops, all on one master ----
SR=44100;N=int(TOTAL*SR);rng=np.random.default_rng(3)
def lp(x,a):
  y=np.empty_like(x);acc=0.0
  for i in range(len(x)):acc+=a*(x[i]-acc);y[i]=acc
  return y
import wave
def save(fn,x):
  x=np.clip(x,-1,1);s=(np.stack([x,x],1)*32767).astype(np.int16);w=wave.open(fn,"wb");w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(s.tobytes());w.close()
room=lp(rng.standard_normal(N),0.015)*0.5+0.02*np.sin(2*np.pi*95*np.arange(N)/SR)  # fan hum + air
street=lp(rng.standard_normal(N),0.12)*0.6;street[int(SCR*SR):]=0;street[:int(0.1*SR)]*=0.2
bed=np.zeros(N);b_=60/84;prog=[[48,52,55,59],[45,48,52,55],[41,45,48,52],[43,47,50,53]]
def pl(m,d,a):
  f=440*2**((m-69)/12);tt=np.arange(int(d*SR))/SR;return a*np.exp(-tt*5)*(np.sin(2*np.pi*f*tt)+.3*np.sin(4*np.pi*f*tt))
t0=SCR;beat=0
while t0<END-0.3:
  ch=prog[(beat//4)%4];i=int(t0*SR)
  if beat%4==0:s=pl(ch[0]-12,b_*1.9,.18);bed[i:i+len(s)]+=s[:N-i]
  if beat%2==1:
    for n in ch[1:]:s=pl(n+12,b_*.6,.04);bed[i:i+len(s)]+=s[:max(0,N-i)]
  beat+=1;t0+=b_
ambient=room*0.22+street*0.18+bed*0.8
def tone(f,d,a,dec=18):
  tt=np.arange(int(.7*SR))/SR;x=a*np.sin(2*np.pi*f*tt)*np.exp(-tt*dec);x[int(d*SR):]=0;return x
ev=np.zeros(N)
def put(t,x):
  i=int(t*SR)
  if 0<=i<N:ev[i:i+len(x)]+=x[:N-i]
for kind,t in sfx:
  if kind=="msg":put(t,tone(880,.25,.18)+tone(1320,.2,.08))
  elif kind=="ding":put(t,tone(1175,.4,.22,9)+tone(1568,.4,.1,9))
  elif kind=="match":put(t,tone(659,.5,.2,6)+tone(988,.5,.15,6)+tone(1319,.6,.12,6))
  elif kind=="confirm":put(t,tone(784,.3,.2,10)+tone(1046,.45,.2,8))
  elif kind=="key":put(t,lp(rng.standard_normal(int(.03*SR)),.5)*np.exp(-np.arange(int(.03*SR))/SR*120)*.5)
  elif kind=="bksp":put(t,tone(260,.12,.25,30));put(t,lp(rng.standard_normal(int(.05*SR)),.4)*.2)
  elif kind=="send":put(t,tone(520,.08,.2,10)+np.roll(tone(780,.2,.2,10),int(.08*SR)))
  elif kind=="whoosh":tt=np.arange(int(.35*SR))/SR;put(t,lp(rng.standard_normal(len(tt)),.15)*np.sin(np.pi*tt/.35)*.4)
  elif kind=="splat":tt=np.arange(int(.25*SR))/SR;nz=np.zeros(int(.7*SR));nz[:len(tt)]=lp(rng.standard_normal(len(tt)),.35)*np.exp(-tt*14)*.5;put(t,nz+tone(110,.25,.3,14))
# record scratch at SCR + bed stops there then restarts with the bedroom
tt=np.arange(int(.28*SR))/SR;ev_s=lp(rng.standard_normal(len(tt)),.45)*(np.linspace(1,0,len(tt)))*.5*np.sin(2*np.pi*(900-800*tt/.28)*tt*0.15+1);put(SCR-0.05,ev_s)
save(f"{W}/amb.wav",ambient);save(f"{W}/ev.wav",ev)
ins=["-i",f"{W}/amb.wav","-i",f"{W}/ev.wav"];fl=["[0:a]volume=1[am]","[1:a]volume=1.0[ev]"];mix=["[am]","[ev]"];k=2
for (f,at,g) in audio:
  ins+=["-i",f];ms=int(max(0,at)*1000);fl.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms},volume={g}[x{k}]");mix.append(f"[x{k}]");k+=1
fl.append("".join(mix)+f"amix=inputs={len(mix)}:normalize=0:duration=longest,atrim=0:{TOTAL:.3f},alimiter=limit=0.95[a]")
run(ins+["-filter_complex",";".join(fl),"-map","[a]","-ar","44100",f"{W}/a.wav"])
run(["-i",f"{W}/v.mp4","-i",f"{W}/a.wav","-map","0:v","-map","1:a","-c:v","libx264","-crf","24","-preset","slow","-c:a","aac","-b:a","160k","-shortest",OUT])
print("ok",round(TOTAL,1))
