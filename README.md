#skyPi
============================================

skyPi allows a Raspberry Pi to send low-resolution images over SSTV from a
high-altitude balloon (or, optionally, the ground), while storing
high-resolution images locally.

Installation
------------

Dependencies:
pySSTV

Compile `gen_values.c` to `gen_values` in the `skyPi` folder.

The following assumes the `skyPi` folder is in the `pi` user's home directory.

Add `@reboot sh /home/pi/skyPi/beacon.sh` to the `pi` user's crontab.

Add `@reboot python /home/pi/skyPi/shutdown.py` to `root`'s crontab
to be able to safely shutdown the RPi by pulling GPIO pin 17 low. The RPi
is doing a lot of disk writes for the images, so unplugging it without shutting
down properly will probably result in unhappiness.

Usage
-----

Connect a camera to RPi.

Plug audio cable into RPi's 3.5mm output. Plug other end into something (ham 
radio, laptop, garbage disposal, etc).

Boot RPi. It will periodically transmit SSTV images as audio over the 3.5mm
output. Default SSTV format is MartinM2. Many are supported.

Credit
------

This project is based upon https://github.com/hsbp/rpi-sstv.
