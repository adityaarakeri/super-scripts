#Created by Timothy Joshua Dy Chua
#For Mac OSX computers
#A script to schedule a shutdown of your computer on the same day or the next day.

from datetime import datetime
from subprocess import Popen, PIPE
import os

if __name__ == "__main__":

  time_to_shutdown = "16:57"
  sudo_password = "" #Please enter your admin password here.
  command = "shutdown -h now".split()

  while(True):
    time_now = datetime.now().time()
    time_now_HH_MM = str(time_now)[0:5]
    if(time_now_HH_MM == time_to_shutdown):
      p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
      sudo_prompt = p.communicate(sudo_password + '\n')[1]
