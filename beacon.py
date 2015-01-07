#!/usr/bin/env python

"""
This example streams the raw floating point (freq, msec) tuples to stdout
in 4-byte single precision format (8 bytes per tuple), so that it can be
processed outside PySSTV.

Usage example using unixsstv/gen_values:
beacon.py | gen_values 44100 | play -r 44100 -t f32 -c 1 --norm -
"""

from PIL import Image, ImageFont, ImageDraw
from pysstv.color import MartinM2, Robot36
from subprocess import check_output
from cStringIO import StringIO
#import RPi.GPIO as GPIO
import struct, sys

#TX_PIN = 18

def main():
    img = Image.open(StringIO(check_output(['raspistill', '--output', '-',
        '--width', '256', '--height', '240', '-n', '-e', 'bmp'])))
    img = img.resize((MartinM2.WIDTH, MartinM2.HEIGHT))
#    img = img.resize((Robot36.WIDTH, Robot36.HEIGHT))
    font = ImageFont.truetype("/home/pi/skyPi/merchantcopydouble.ttf", 12)
    draw = ImageDraw.Draw(img)
    draw.text((17, 17), "Your callsign", (0, 0, 0), font=font)
    draw.text((16, 16), "Your callsign", (255, 255, 255), font=font)
    sstv = MartinM2(img, 44100, 16)
#    sstv = Robot36(img, 44100, 16)
    sstv.vox_enabled = True
    for freq, msec in sstv.gen_freq_bits():
        sys.stdout.write(struct.pack('ff', freq, msec))
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(TX_PIN, GPIO.OUT)
#    GPIO.output(TX_PIN, True)

if __name__ == '__main__':
    main()
