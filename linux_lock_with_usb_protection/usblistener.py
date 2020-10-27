#!bin/python3

import sys
import os
import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        os.system("mplayer ~/PATH/TO/myalarm.mp3 &")
        sys.exit()
