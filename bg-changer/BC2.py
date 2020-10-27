
import os
from os.path import isfile, join
from time import sleep
import random
mypath = "/home/tatan/Desktop/Tests/BGC"
onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
print onlyfiles
while True:
	i = onlyfiles[int(random.random()*len(onlyfiles))]
	print(i)
	if i.endswith("jpg"):
		os.system("gsettings set org.gnome.desktop.background picture-uri file://"+os.getcwd()+"/"+i)
		sleep(60)
	else:
		continue