#!/bin/bash
origdir=/home/pi/skyPi/pics/run
num=0
while [[ -d $origdir$num ]]; do
  let num++
done
directory=$origdir$num
echo Saving images to $directory
mkdir $directory

while [ true ]; do

filename=image
num=0
while [[ -e $directory/$filename-$num.jpg ]] ; do
  let num++
done
filename=$filename-$num

raspistill --width 1920 --height 1080 -n -e jpg -o $directory/$filename.jpg

python /home/pi/skyPi/beacon.py | /home/pi/skyPi/gen_values 44100 > /tmp/wav.bin
play -q -r 44100 -t f32 -c 1 --norm /tmp/wav.bin > /dev/null 2>&1
rm -f /tmp/wav.bin
done
