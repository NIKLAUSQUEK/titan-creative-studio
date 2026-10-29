"""PI Job Part 5-6 v4: screenplay coverage. Speaking shots use the lip-synced clip's OWN audio (in sync);
thoughts are voice-over on closed-mouth close-ups; natural pauses + reaction beats; no speed-up.
python3 assemble_p56_v4.py <out.mp4>   (reads p56/, ls/, vo/)"""
import subprocess,sys,os,json
from PIL import Image,ImageDraw,ImageFont
OUT=sys.argv[1];W="_v4";os.makedirs(W,exist_ok=True)
FB="/usr/share/fonts/opentype/inter/Inter-Bold.otf"
def F(s):return ImageFont.truetype(FB,s)
def run(a):subprocess.run(["ffmpeg","-y","-v","error"]+a,check=True)
def dur(f):return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout)
def speech(f,th="-35dB"):
  """first/last speech time in a file (silencedetect)"""
  r=subprocess.run(["ffmpeg","-i",f,"-af",f"silencedetect=noise={th}:d=0.15","-f","null","-"],capture_output=True,text=True).stderr
  st=[float(l.split("silence_start: ")[1].split()[0]) for l in r.splitlines() if "silence_start" in l]
  en=[float(l.split("silence_end: ")[1].split()[0]) for l in r.splitlines() if "silence_end" in l]
  D=dur(f);a=en[0] if st and st[0]<0.05 and en else 0.0
  b=st[-1] if st and st[-1]>a+0.3 else D
  return a,b
def wrap(d,t,f,w):
  out=[];line=""
  for x in t.split():
    if d.textlength((line+" "+x).strip(),font=f)>w:out.append(line);line=x
    else:line=(line+" "+x).strip()
  return out+[line]
def card(name,sub=None,bubble=None,top=None,size=54,rewind=False):
  im=Image.new("RGBA",(1080,1920),(0,0,0,0));d=ImageDraw.Draw(im)
  if top:
    f=F(64);y=150
    for ln in wrap(d,top,f,960):
      w=d.textlength(ln,font=f);d.text(((1080-w)/2,y),ln,font=f,fill="white",stroke_width=6,stroke_fill=(0,0,0));y+=80
  if bubble:
    f=F(48);ls=wrap(d,bubble,f,820);bh=len(ls)*60+40;y=260
    bw=max(d.textlength(l,font=f) for l in ls)+60;x=(1080-bw)/2
    d.rounded_rectangle((x,y,x+bw,y+bh),30,fill=(255,199,39));yy=y+20
    for l in ls:d.text((x+30,yy),l,font=f,fill=(30,22,84));yy+=60
  if sub:
    f=F(size);y=1500
    for ln in wrap(d,sub,f,940):
      w=d.textlength(ln,font=f);x=(1080-w)/2
      d.rounded_rectangle((x-18,y-8,x+w+18,y+size+14),14,fill=(0,0,0,170));d.text((x,y),ln,font=f,fill="white");y+=size+22
  if rewind:
    d.text((70,120),"<< REWIND",font=F(72),fill="white",stroke_width=5,stroke_fill=(0,0,0))
    d.text((70,210),"2 seconds earlier…",font=F(44),fill=(255,199,39),stroke_width=4,stroke_fill=(0,0,0))
  im.save(f"{W}/{name}.png")
VF="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30"
segs=[]   # (video file, audio file or None)
n=[0]
def shot(src,ss,du,cardkw=None,still=False,zoom=False,audio=None,a_ss=0.0,vo=None,vo_at=0.0,sfx=None):
  i=n[0];n[0]+=1;o=f"{W}/s{i:02d}.mp4"
  ins=(["-loop","1","-t",f"{du:.3f}","-i",src] if still else ["-ss",f"{ss:.3f}","-t",f"{du:.3f}","-i",src])
  vf=VF+(",zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30" if zoom else "")
  vf+=",tpad=stop_mode=clone:stop_duration=2"
  if cardkw:card(f"c{i}",**cardkw);ins+=["-i",f"{W}/c{i}.png"];fc=f"[0:v]{vf}[b];[b][1:v]overlay[v]"
  else:fc=f"[0:v]{vf}[v]"
  run(ins+["-filter_complex",fc,"-map","[v]","-t",f"{du:.3f}","-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-r","30","-an",o])
  # audio for this shot: clip's own sync audio, or VO, or silence; plus optional sfx
  ao=f"{W}/a{i:02d}.wav"
  if audio:run(["-ss",f"{a_ss:.3f}","-t",f"{du:.3f}","-i",audio,"-af",f"apad,atrim=0:{du:.3f}","-ar","44100","-ac","2",ao])
  elif vo:run(["-i",vo,"-af",f"adelay={int(vo_at*1000)}|{int(vo_at*1000)},volume=1.15,apad,atrim=0:{du:.3f}","-ar","44100","-ac","2",ao])
  else:run(["-f","lavfi","-t",f"{du:.3f}","-i","anullsrc=r=44100:cl=stereo",ao])
  if sfx:
    o2=f"{W}/a{i:02d}x.wav";run(["-i",ao,"-f","lavfi","-t",f"{du:.3f}","-i",sfx,"-filter_complex","[0:a][1:a]amix=inputs=2:normalize=0[a]","-map","[a]","-ar","44100","-ac","2",o2]);ao=o2
  segs.append((o,ao))
def clip_line(src,lead=0.15,tail=0.45,cardkw=None):
  a,b=speech(src);ss=max(0,a-lead);du=min(dur(src)-ss,(b-a)+lead+tail)
  shot(src,ss,du,cardkw,audio=src,a_ss=ss)
def vo_len(f):a,b=speech(f);return b
P="p56";L="ls";V="vo"
SPL="aevalsrc='0.5*(random(0)-0.5)*exp(-t*5)':s=44100:d=0.8"
shot(f"{P}/c1.mp4",0.3,2.0,dict(top="he said 'I know you want it'…"))                               # 1 wide
clip_line(f"{L}/s2.mp4",cardkw=dict(sub="Hi… J?"))                                                   # 2 Hân speaks
shot(f"{P}/c2.mp4",0.2,0.8)                                                                          # 3 Jake smirk
shot(f"{L}/han_cu.png",0,vo_len(f"{V}/v2.mp3")+0.4,dict(bubble="ok. this is easier than it looks. he's a GI. just say no to his advances."),still=True,zoom=True,vo=f"{V}/v2.mp3",vo_at=0.15)  # 4 thought
clip_line(f"{L}/s5.mp4",cardkw=dict(sub="So, is it hot in Saigon, or is it just you?"))             # 5 Jake
shot(f"{P}/c5.mp4",0.2,0.8)                                                                          # 6 Hân awkward
clip_line(f"{L}/s7.mp4",cardkw=dict(sub="Relax. I don't bite. Unless you ask nicely."))             # 7 Jake
shot(f"{P}/c3.mp4",1.6,vo_len(f"{V}/v5.mp3")+0.3,dict(bubble="just say no… say it NICELY though…"),vo=f"{V}/v5.mp3",vo_at=0.1)  # 8 thought
clip_line(f"{L}/s9.mp4",cardkw=dict(sub="Come on… I know you want it."))                            # 9 Jake lean
shot(f"{P}/c5.mp4",1.0,vo_len(f"{V}/v7.mp3")+0.35,dict(bubble="how do I say no NICELY??"),vo=f"{V}/v7.mp3",vo_at=0.1)  # 10 thought
clip_line(f"{L}/s11.mp4",lead=0.3,cardkw=dict(bubble="WAIT. DID I JUST…"))                           # 11 panic (spoken)
# 12 rewind
card("rw",rewind=True);run(["-ss","0.3","-t","1.4","-i",f"{P}/c7.mp4","-i",f"{W}/rw.png","-filter_complex",f"[0:v]reverse,setpts=0.5*PTS,{VF},hue=s=0.3[b];[b][1]overlay[v]","-map","[v]","-t","0.75","-c:v","libx264","-crf","20","-pix_fmt","yuv420p","-r","30","-an",f"{W}/rw.mp4"])
run(["-f","lavfi","-i","aevalsrc='0.18*sin(2*PI*(1800-1400*t/0.75)*t)':s=44100:d=0.75","-ac","2",f"{W}/rw.wav"]);segs.append((f"{W}/rw.mp4",f"{W}/rw.wav"))
shot(f"{P}/c6.mp4",0.3,1.4,sfx=SPL)                                                                  # 13 splash
shot(f"{P}/c7.mp4",2.1,vo_len(f"{V}/v9.mp3")+0.35,dict(bubble="…oh thank god. it was HER."),vo=f"{V}/v9.mp3",vo_at=0.1)  # 14 relief
clip_line(f"{L}/s15.mp4",lead=0.1,tail=0.35,cardkw=dict(sub="CLIENT MEETING, JAKE?!",size=64))       # 15 Trâm
clip_line(f"{L}/s16.mp4",cardkw=dict(sub="Babe! This is… my… accountant?"))                         # 16 Jake
card("end",top="Part 7 →");run(["-f","lavfi","-i","color=c=0x1e1654:s=1080x1920:r=30","-i",f"{W}/end.png","-filter_complex","[0:v][1:v]overlay[v]","-map","[v]","-t","1.2","-c:v","libx264","-pix_fmt","yuv420p","-r","30","-an",f"{W}/end.mp4"])
run(["-f","lavfi","-t","1.2","-i","anullsrc=r=44100:cl=stereo",f"{W}/end.wav"]);segs.append((f"{W}/end.mp4",f"{W}/end.wav"))
open(f"{W}/v.txt","w").write("".join(f"file '{os.path.abspath(v)}'\n" for v,a in segs))
open(f"{W}/a.txt","w").write("".join(f"file '{os.path.abspath(a)}'\n" for v,a in segs))
run(["-f","concat","-safe","0","-i",f"{W}/v.txt","-c","copy",f"{W}/v.mp4"])
run(["-f","concat","-safe","0","-i",f"{W}/a.txt","-c:a","pcm_s16le",f"{W}/a.wav"])
T=dur(f"{W}/v.mp4")
bed=f"aevalsrc='0.035*(sin(2*PI*261.6*t)+sin(2*PI*329.6*t)+sin(2*PI*392*t))*(0.7+0.3*sin(2*PI*0.5*t))':s=44100:d={T:.2f}"
run(["-i",f"{W}/v.mp4","-i",f"{W}/a.wav","-f","lavfi","-i",bed,"-filter_complex","[2:a]aformat=channel_layouts=stereo[b];[1:a][b]amix=inputs=2:normalize=0:duration=first[a]","-map","0:v","-map","[a]","-c:v","libx264","-crf","26","-preset","slow","-c:a","aac","-b:a","128k",OUT])
print("ok",round(T,1))
