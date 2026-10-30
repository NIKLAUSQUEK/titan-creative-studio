"""Original audio for PI Job P5-6 v5: continuous cafe ambience + a comedic-romantic music cue.
python3 bed.py <total_s> <music_stop_s> <splash_s> <end_s>  -> amb.wav, music.wav  (44.1k stereo)"""
import numpy as np,sys,wave,subprocess,glob
SR=44100;T,STOP,SPL,END=map(float,sys.argv[1:5]);N=int(T*SR);rng=np.random.default_rng(7)
def save(fn,x):
  x=np.clip(x,-1,1);s=(np.stack([x,x],1)*32767).astype(np.int16) if x.ndim==1 else (np.clip(x,-1,1)*32767).astype(np.int16)
  w=wave.open(fn,"wb");w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(s.tobytes());w.close()
def lp(x,a):
  y=np.empty_like(x);acc=0.0
  for i in range(len(x)):acc+=a*(x[i]-acc);y[i]=acc
  return y
# --- ambience: room tone + distant murmur (heavily filtered, reversed voice lines) + cup/spoon clinks
room=lp(rng.standard_normal(N),0.02)*0.5
mur=np.zeros(N)
for f in sorted(glob.glob("vo/*.mp3")):
  raw=subprocess.run(["ffmpeg","-v","error","-i",f,"-ac","1","-ar",str(SR),"-f","s16le","-"],capture_output=True).stdout
  v=np.frombuffer(raw,np.int16).astype(float)[::-1]/32768
  for k in range(4):
    p=int(rng.uniform(0,max(1,N-len(v))));mur[p:p+len(v)]+=v[:N-p]*rng.uniform(.3,.6)
mur=lp(lp(mur,0.06),0.06)*1.4
cl=np.zeros(N);t=np.arange(int(.25*SR))/SR
for p in rng.uniform(0,T,int(T/1.6)):
  f0=rng.uniform(2400,4200);s=np.sin(2*np.pi*f0*t)*np.exp(-t*28)*rng.uniform(.02,.05);i=int(p*SR);cl[i:i+len(s)]+=s[:N-i]
amb=(room*0.6+mur+cl)
amb=amb/np.abs(amb).max()*0.22
save("amb.wav",amb)
# --- music: light pizzicato/jazzy lounge loop (C maj7 - A min7 - D min7 - G7), 100 bpm, builds, cuts dead at STOP
bpm=100;b=60/bpm;m=np.zeros(N)
prog=[[48,52,55,59],[45,48,52,55],[50,53,57,60],[43,47,50,53]]
def pl(midi,dur,amp):
  f=440*2**((midi-69)/12);tt=np.arange(int(dur*SR))/SR
  return amp*np.exp(-tt*6)*(np.sin(2*np.pi*f*tt)+.35*np.sin(4*np.pi*f*tt)+.12*np.sin(6*np.pi*f*tt))
beat=0;t0=0.0
while t0<STOP:
  ch=prog[(beat//4)%4];bi=beat%4;i=int(t0*SR)
  # bass on 1 and 3
  if bi in(0,2):s=pl(ch[0]-12,b*1.8,.22);m[i:i+len(s)]+=s[:N-i]
  # pluck chord on 2 and 4 (offbeat skip)
  if bi in(1,3):
    for n in ch[1:]:s=pl(n+12,b*.6,.06);m[i:i+len(s)]+=s[:N-i]
  # melody pluck builds after 6 s
  if t0>6 and bi in(0,1,3):
    s=pl(ch[(beat*3)%4]+24,b*.5,.05*min(1,(t0-6)/6+.4));j=i+int(b*.5*SR);m[j:j+len(s)]+=s[:max(0,N-j)]
  # brushed hat every 8th
  for h in(0,.5):
    j=i+int(h*b*SR);hh=rng.standard_normal(int(.04*SR))*np.exp(-np.arange(int(.04*SR))/SR*90)*.03;m[j:j+len(hh)]+=hh[:max(0,N-j)]
  beat+=1;t0+=b
# soft fade-out last 80 ms before STOP (a "record stop" droop)
i0=int((STOP-.25)*SR);i1=int(STOP*SR);m[i0:i1]*=np.linspace(1,0,i1-i0)**2;m[i1:]=0
# splash: low boom + noise burst at SPL
i=int(SPL*SR);tt=np.arange(int(.9*SR))/SR
boom=np.sin(2*np.pi*55*tt*np.exp(-tt*2))*np.exp(-tt*4)*.5+lp(rng.standard_normal(len(tt)),.3)*np.exp(-tt*6)*.35
m[i:i+len(boom)]+=boom[:N-i]
# comedy resume after splash: bouncy bassoon-ish staccato from SPL+1.2 to END, then a button sting at END
t0=SPL+1.2;k=0;notes=[43,47,50,47,45,48,52,48]
while t0<END-.4:
  i=int(t0*SR);s=pl(notes[k%8]-12,b*.4,.2);m[i:i+len(s)]+=s[:N-i];k+=1;t0+=b/2
i=int(END*SR)
for n in(55,59,62,67):s=pl(n+12,1.2,.09);m[i:i+len(s)]+=s[:max(0,N-i)]
save("music.wav",m/np.abs(m).max()*0.35)
print("ok")
