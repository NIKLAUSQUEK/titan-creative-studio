"""PI Job Part 5-6 v5: ONE continuous scene (after Klaus: "feels like a lot of individual parts").
Built on one absolute timeline instead of glued segments:
 - continuous cafe ambience + one original music cue under every cut (music dies on "I know you want it", splash hit, comedic resume)
 - J-cuts (next line starts ~0.12 s before its picture) and L-cuts (line tail rings over the reaction)
 - eyeline chain: Hân looks at the shirt -> insert of the eagle -> back to her
 - every shot drifts in slowly (1.00 -> 1.04), one caption style (word-by-word, lower third) + one thought-bubble style
 - same cafe, Hân LEFT / Jake RIGHT in every two-shot (v5/ re-shoots), calm crowd until the splash
python3 assemble_p56_v5.py <out.mp4>"""
import subprocess,sys,os
import numpy as np
from PIL import Image,ImageDraw,ImageFont
OUT=sys.argv[1];W="_v5";os.makedirs(W,exist_ok=True)
FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf";FX="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
if not os.path.exists(FX):FX=FB
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
  """lower-third caption, words revealed up to `shown`, current word yellow"""
  ws=text.split()
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
def bubble(name,text):
  def d(dr):
    f=F(46);ls=wrap(dr,text,f,800);bh=len(ls)*58+70;bw=max(dr.textlength(l,font=f) for l in ls)+64;x=(1080-bw)/2;y=250
    dr.rounded_rectangle((x,y,x+bw,y+bh),32,fill=(255,199,39));dr.text((x+32,y+12),"Hân, thinking…",font=F(26),fill=(30,22,84))
    yy=y+48
    for l in ls:dr.text((x+32,yy),l,font=f,fill=(30,22,84));yy+=58
    dr.ellipse((x+bw*0.3,y+bh+10,x+bw*0.3+34,y+bh+44),fill=(255,199,39));dr.ellipse((x+bw*0.3-26,y+bh+54,x+bw*0.3-6,y+bh+74),fill=(255,199,39))
  return png(name,d)
def top(name,text,sub=None):
  def d(dr):
    f=F(62,FX);y=150
    for ln in wrap(dr,text,f,960):
      w=dr.textlength(ln,font=f);dr.text(((1080-w)/2,y),ln,font=f,fill="white",stroke_width=7,stroke_fill=(0,0,0));y+=78
    if sub:w=dr.textlength(sub,font=F(42));dr.text(((1080-w)/2,y+10),sub,font=F(42),fill=(255,199,39),stroke_width=5,stroke_fill=(0,0,0))
  return png(name,d)
# ---------- timeline ----------
shots=[]   # dict(src, ss, du, still, crop, overlays=[(png, t0, t1)], fx)
audio=[]   # (file, at_s, gain, src_ss, src_du)
T=[0.0]
def add(src,ss,du,still=False,crop=None,ov=(),fx=None):
  shots.append(dict(src=src,ss=ss,du=du,still=still,crop=crop,ov=list(ov),fx=fx,t=T[0]));T[0]+=du
def say(src,vo,text,lead=0.12,tail=0.18,extra=0.0,ovx=()):
  """lip-synced line: picture starts `lead` s AFTER the line starts (J-cut: the line begins under the previous shot);
  shot ends `tail` s after the last word (L-cut: the reaction picks up the ring-out)"""
  lag=offset(src,vo);a,b=speech(vo);t_line=T[0]-lead          # when the first word sounds on the master timeline
  ss=max(0.0,lag+a+lead-0.0);du=min(dur(src)-ss,(b-a)-lead+tail+extra)
  audio.append((vo,t_line-a,1.15,0,None))
  ws=text.split();n=len(ws);sp=(b-a)/n;ov=[]
  for i in range(n):
    t0=T[0]+max(0,(i*sp)-lead);t1=T[0]+((i+1)*sp-lead) if i<n-1 else T[0]+du
    ov.append((cap_words(f"w{len(shots)}_{i}",text,i+1),max(T[0],t0),t1))
  add(src,ss,du,ov=ov+list(ovx))
def think(vo,text,at):
  a,b=speech(vo);audio.append((vo,at-a,1.0,0,None));return (bubble(f"b{len(audio)}",text),at,at+(b-a)+0.35),(b-a)
P="p56";L="ls";V="vo";N="v5"
# 1 WIDE: Hân arrives. hook on top. "Hi… J?"
hook=top("hook","he said “I know you want it”…","(this one's a story)")
add(f"{N}/s2.mp4",0.0,0.55,ov=[(hook,0,3.2)])
say(f"{N}/s2.mp4",f"{V}/v1.mp3","Hi… J?",lead=0.0,tail=0.25,ovx=[(hook,0,3.2)])
# 2 Jake CU slow smirk (reaction)
add(f"{P}/c2.mp4",0.3,0.9)
# 3 Hân CU, closed mouth: thought starts; her eyes drop to the shirt -> 4 insert eagle (eyeline) -> back
b1,l1=think("vo_tight/v2.wav","ok. this is easier than it looks. he's a GI. just say no to his advances.",T[0]+0.15)
add(f"{L}/han_cu.png",0,1.5,still=True,ov=[(b1[0],b1[1],b1[2])])
add(f"{P}/c2.mp4",1.2,1.1,crop=(120,390,240,427),ov=[(b1[0],b1[1],b1[2])])     # eagle insert (her POV)
add(f"{L}/han_cu.png",0,max(0.5,b1[2]-T[0]-0.25),still=True,ov=[(b1[0],b1[1],b1[2])])
# 5 Jake: "hot in Saigon" (J-cut)
say(f"{L}/s5.mp4",f"{V}/v3.mp3","So, is it hot in Saigon, or is it just you?")
# 6 Hân reaction: frozen polite smile (start of the lean-back clip, dry)
add(f"{N}/t10.mp4",0.0,0.9)
# 7 two-shot (same set): arm slides along her chair — "Relax. I don't bite…"
say(f"{N}/s7.mp4",f"{V}/v4.mp3","Relax. I don't bite. Unless you ask nicely.")
# 8 Hân CU leaning back, thought
b2,l2=think("vo_tight/v5.wav","just say no… say it NICELY though…",T[0]+0.1)
h=round((l2+0.35)*0.55,2);add(f"{N}/t10.mp4",0.9,h,ov=[b2])
add(f"{N}/s7.mp4",max(0,dur(f"{N}/s7.mp4")-((l2+0.35)-h)-0.05),(l2+0.35)-h,ov=[b2])   # cutaway: his arm on her chair, thought carries over (L-cut)
# 9 Jake: "Come on… I know you want it" + pucker lean. MUSIC DIES on "want it"
s9_start=T[0]
say(f"{L}/s9.mp4",f"{V}/v6.mp3","Come on… I know you want it.",tail=0.6)
MUSIC_STOP=T[0]-0.45
# 10 Hân tipping back, tiny panicked thought
b3,l3=think("vo_tight/v7.wav","how do I say no NICELY??",T[0]+0.05)
add(f"{N}/t10.mp4",max(0,4.0-(l3+0.35)),l3+0.35,ov=[b3])
# 11 SPLASH (sound only, 0.2 s black) -> damp jeans: "WAIT. DID I JUST…"
SPLASH=T[0]
shots.append(dict(src="black",ss=0,du=0.2,still=False,crop=None,ov=[],fx="black",t=T[0]));T[0]+=0.2
say(f"{L}/s11.mp4",f"{V}/v8.mp3","WAIT. DID I JUST…",lead=0.0,tail=0.3)
# 12 REWIND -> 13 the real splash (Trâm throws) at normal speed
rw=png("rw",lambda d:(d.text((70,120),"<< REWIND",font=F(72,FX),fill="white",stroke_width=6,stroke_fill=(0,0,0)),d.text((70,212),"2 seconds earlier…",font=F(44),fill=(255,199,39),stroke_width=4,stroke_fill=(0,0,0))))
RW=T[0];add(f"{P}/c6.mp4",0.2,0.8,fx="rewind",ov=[(rw,T[0],T[0]+0.8)])
SPLASH2=T[0]+0.25;add(f"{P}/c6.mp4",0.2,1.5)
# 14 relief thought (L-cut over the splash tail)
b4,l4=think("vo_tight/v9.wav","…oh thank god. it was HER.",T[0]-0.1)
add(f"{P}/c7.mp4",2.0,l4+0.3,ov=[b4])
# 15 Trâm  16 Jake soaked
say(f"{L}/s15.mp4",f"{V}/v10.mp3","CLIENT MEETING, JAKE?!",tail=0.15)
say(f"{L}/s16.mp4",f"{V}/v11.mp3","Babe! This is… my… accountant?",tail=0.3)
END=T[0]
p7=top("p7","Part 7 →","what Hân did next 📸".replace("📸",""))
add(f"{L}/s16.mp4",3.6,0.0001)   # placeholder to keep last ss sane
shots.pop()
# freeze last frame 1.3 s with Part 7 overlay (no dead navy card)
last=shots[-1];shots.append(dict(src=last["src"],ss=last["ss"]+last["du"]-0.05,du=1.3,still=False,crop=None,ov=[(p7,T[0],T[0]+1.3)],fx="freeze",t=T[0]));T[0]+=1.3
TOTAL=T[0]
# ---------- render picture ----------
VF="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30"
parts=[]
for i,s in enumerate(shots):
  o=f"{W}/p{i:02d}.mp4";du=s["du"]
  drift=f"scale=w='trunc(1080*(1+0.04*t/{du:.3f})/2)*2':h='trunc(1920*(1+0.04*t/{du:.3f})/2)*2':eval=frame,crop=1080:1920"
  if s["fx"]=="black":
    run(["-f","lavfi","-i","color=c=black:s=1080x1920:r=30","-t",f"{du}","-c:v","libx264","-pix_fmt","yuv420p","-r","30",o]);parts.append(o);continue
  if s["still"]:inp=["-loop","1","-t",f"{du+0.5:.3f}","-i",s["src"]]
  elif s["fx"]=="freeze":inp=["-ss",f"{max(0,s['ss']):.3f}","-i",s["src"]]
  else:inp=["-ss",f"{s['ss']:.3f}","-t",f"{du+0.3:.3f}","-i",s["src"]]
  base=VF
  if s["crop"]:x,y,w,h=s["crop"];base=f"crop={w}:{h}:{x}:{y},"+VF   # source pixels
  if s["fx"]=="rewind":base=f"reverse,setpts=0.6*PTS,{VF},hue=s=0.25"
  if s["fx"]=="freeze":base=f"trim=end_frame=1,loop=loop=60:size=1,setpts=N/30/TB,{VF}"
  fc=f"[0:v]{base},tpad=stop_mode=clone:stop_duration=3,{drift}[v0]";last="v0";k=1;ins=list(inp)
  for (p,t0,t1) in s["ov"]:
    a=max(0,t0-s["t"]);b=min(du,t1-s["t"])
    if b<=0 or a>=du:continue
    ins+=["-i",p];fc+=f";[{last}][{k}:v]overlay=enable='between(t,{a:.3f},{b:.3f})'[v{k}]";last=f"v{k}";k+=1
  run(ins+["-filter_complex",fc,"-map",f"[{last}]","-t",f"{du:.3f}","-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-r","30","-an",o]);parts.append(o)
open(f"{W}/v.txt","w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
run(["-f","concat","-safe","0","-i",f"{W}/v.txt","-c","copy",f"{W}/v.mp4"])
# ---------- one audio master ----------
subprocess.run(["python3","v5/bed.py",f"{TOTAL:.2f}",f"{MUSIC_STOP:.2f}",f"{SPLASH:.2f}",f"{END:.2f}"],check=True,cwd=".")
ins=["-i","amb.wav","-i","music.wav"];fl=["[0:a]volume=1.0[am]","[1:a]volume=0.9[mu]"];mix=["[am]","[mu]"];k=2
for (f,at,g,_,_) in audio:
  ins+=["-i",f];ms=int(max(0,at)*1000);fl.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms},volume={g}[x{k}]");mix.append(f"[x{k}]");k+=1
# splash on screen (rewind payoff) + chair creak + rewind whine
ins+=["-f","lavfi","-t","0.8","-i","aevalsrc='0.6*(random(0)-0.5)*exp(-t*5)':s=44100","-f","lavfi","-t","0.8","-i","aevalsrc='0.16*sin(2*PI*(1900-1500*t/0.8)*t)':s=44100"]
for nm,at in(("spl",SPLASH2),("rww",RW)):
  ms=int(at*1000);fl.append(f"[{k}:a]aformat=channel_layouts=stereo,adelay={ms}|{ms}[x{k}]");mix.append(f"[x{k}]");k+=1
fl.append("".join(mix)+f"amix=inputs={len(mix)}:normalize=0:duration=longest,atrim=0:{TOTAL:.3f},alimiter=limit=0.95[a]")
run(ins+["-filter_complex",";".join(fl),"-map","[a]","-ar","44100",f"{W}/a.wav"])
run(["-i",f"{W}/v.mp4","-i",f"{W}/a.wav","-map","0:v","-map","1:a","-c:v","libx264","-crf","24","-preset","slow","-c:a","aac","-b:a","160k","-shortest",OUT])
print("ok",round(TOTAL,1),"music stop",round(MUSIC_STOP,2),"splash",round(SPLASH,2))
