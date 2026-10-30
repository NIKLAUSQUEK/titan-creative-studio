"""Look test: Hân texts back -> Trâm's brief bubbles. One timeline, room tone + pop sfx under both."""
import subprocess,numpy as np,wave
B="board/ov";C="v4set/clips";SR=44100
def run(a):subprocess.run(["ffmpeg","-y","-v","error"]+a,check=True)
VF="scale=1080:1920:flags=lanczos,setsar=1,fps=30"
# shot 1: Hân (3.0 s) with her outgoing bubble from 0.9 s ; shot 2: Trâm (4.0 s) bubbles at 0.5,1.2,1.9,2.6 s
run(["-i",f"{C}/han_texts.mp4","-loop","1","-i",f"{B}/han_out.png","-filter_complex",f"[0:v]{VF}[b];[b][1:v]overlay=enable='gte(t,0.9)'[v]","-map","[v]","-t","3.0","-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-r","30","_lt1.mp4"])
ins=["-i",f"{C}/tram_typing.mp4"];fc=f"[0:v]{VF}[v0]";last="v0"
for k,t in enumerate([0.5,1.2,1.9,2.6],1):
  ins+=["-loop","1","-i",f"{B}/brief_{k}.png"];fc+=f";[{last}][{k}:v]overlay=enable='gte(t,{t})'[v{k}]";last=f"v{k}"
run(ins+["-filter_complex",fc,"-map",f"[{last}]","-t","4.0","-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-r","30","_lt2.mp4"])
open("_lt.txt","w").write("file '_lt1.mp4'\nfile '_lt2.mp4'\n");run(["-f","concat","-safe","0","-i","_lt.txt","-c","copy","_lt.mp4"])
T=7.0;N=int(T*SR);rng=np.random.default_rng(5)
def lp(x,a):
  y=np.empty_like(x);acc=0.0
  for i in range(len(x)):acc+=a*(x[i]-acc);y[i]=acc
  return y
room=lp(rng.standard_normal(N),0.015)*0.5+0.02*np.sin(2*np.pi*95*np.arange(N)/SR)
ev=np.zeros(N)
def tone(f,d,a,dec):
  tt=np.arange(int(.5*SR))/SR;x=a*np.sin(2*np.pi*f*tt)*np.exp(-tt*dec);x[int(d*SR):]=0;return x
def put(t,x):
  i=int(t*SR);ev[i:i+len(x)]+=x[:N-i]
for k in range(8):  # fast thumb taps on Hân
  put(0.15+k*0.11,lp(rng.standard_normal(int(.03*SR)),.5)*np.exp(-np.arange(int(.03*SR))/SR*120)*.5)
put(0.9,tone(520,.08,.25,10)+np.roll(tone(780,.2,.25,10),int(.08*SR)))          # send whoosh
for t in [3.0+0.5,3.0+1.2,3.0+1.9,3.0+2.6]:put(t,tone(880,.25,.2,18)+tone(1320,.2,.08,18)) # WhatsApp pops
for k in range(6):put(3.0+0.1+k*0.14,lp(rng.standard_normal(int(.03*SR)),.5)*np.exp(-np.arange(int(.03*SR))/SR*120)*.35)
x=np.clip((room*0.22+ev)*0.9,-1,1);s=(np.stack([x,x],1)*32767).astype(np.int16)
w=wave.open("_lt.wav","wb");w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(s.tobytes());w.close()
run(["-i","_lt.mp4","-i","_lt.wav","-map","0:v","-map","1:a","-c:v","libx264","-crf","22","-c:a","aac","-b:a","128k","-shortest","pi_job_part1_looktest_480p.mp4"])
print("ok")
