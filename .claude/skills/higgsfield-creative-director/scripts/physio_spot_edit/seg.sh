#!/bin/bash
set -e
V=/tmp/v4
VF="scale=1080:1920,setsar=1,fps=30,format=yuv420p"
AF="aresample=48000,aformat=channel_layouts=stereo"
enc(){ ffmpeg -v error -y "$@" -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k -ar 48000 -ac 2 ; }
cut(){ enc -ss $2 -t $3 -i $V/$1 -vf "$VF" -af "$AF" $4; }
cut 20261009_182233_e3a730ce.mp4 0    1.2  s01.mp4
cut 20261010_050511_413e6791.mp4 0    0.95 s02a.mp4
cut 20261010_050511_413e6791.mp4 2.1  0.85 s02b.mp4
cut 20261009_182233_e3a730ce.mp4 2.9  2.85 s03.mp4
cut 20261010_050533_249b4bfc.mp4 0    2.9  s04.mp4
cut 20261010_042634_62a531a8.mp4 1.25 1.75 s05.mp4
cut 20261010_050354_bca0744b.mp4 0    2.7  s06.mp4
enc -t 3.0 -i $V/20261009_182233_493b670b.mp4 -i sfx_drop.wav -map 0:v -map 1:a -vf "$VF" -af "$AF" s07.mp4
cut 20261010_050354_d914ec35.mp4 0    4.5  s08.mp4
enc -f lavfi -t 0.5 -i color=black:s=1080x1920:r=30 -f lavfi -t 0.5 -i anullsrc=r=48000:cl=stereo -vf format=yuv420p s09.mp4
enc -f lavfi -t 2.4 -i color=black:s=1080x1920:r=30 -f lavfi -t 2.4 -i anoisesrc=r=48000:a=0.002:c=pink \
  -filter_complex "[0:v]format=yuv420p[v];[1:a]aformat=channel_layouts=stereo[a]" -map "[v]" -map "[a]" s10.mp4
# Nik: bulb flicker (black, 0.12s flash, black, fade in) + 1.6s hold
enc -i $V/20261009_180801_e548123c.mp4 -filter_complex \
 "[0:v]$VF,split[a][b];[a]fade=t=in:st=0.70:d=0.8[fa];[fa][b]overlay=enable='between(t,0.45,0.57)',tpad=stop_mode=clone:stop_duration=1.6[v];[0:a]$AF,apad=pad_dur=1.6[a]" \
 -map "[v]" -map "[a]" s11.mp4
for f in s*.mp4; do echo "$f $(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)"; done
