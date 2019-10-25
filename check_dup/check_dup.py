#!/usr/bin/env python3

import os
import subprocess
	
# diff: 0 if same, 1 if different, 2 if trouble

# Global list
dontCheck = set()

def checkPrompt(fiFo, path):
	# If duplicates found, notify that duplicates have been found
	print()
	print("Duplicates found for {}.".format(path))

	# Display all the duplicates of that file in form (1: ... \n 2: ... etc.)
	for key, fi in enumerate(fiFo):
		print("{}. {}".format(key + 1, fi))

	# Prompt if they would like to keep all files
	keepAll = "X"
	while keepAll != "y" and keepAll != "n":
		keepAll = input("Would you like to keep all the above files? (y/n)   ")

	if keepAll == "n":
		for fi in fiFo:
			delFile = "X"
			while delFile != "y" and delFile != "n":
				delFile = input("Would you like to delete {}? (y/n)\t".format(fi))
			if delFile == "y":
				final = "X"
				while final != "y" and final != "n":
					final = input("(Safe Delete) Are you sure you would like to delete {}? (y/n)\t".format(fi))
				if final == "y":
					# Remove from list AND dir
					#if os.path.exists(fi):
  						#os.remove(fi)
					fiFo.remove(fi)
	
	# Don't check these files again
	for i in fiFo:
		dontCheck.add(i)
	

def checkDup(checkDir, dirdir):
	print()
	print("Checking directory {}".format(checkDir))

	# Walk through path and check if there are any duplicates
	if dirdir:
		# For dirpath, dirname, filenames in directory
		for dp, dn, fn in os.walk(checkDir):
			# For file in filenames
			fiFound = []
			for f in fn:
				pathF = dp + "/" + f
				pathF1 = pathF.replace(" ", "\\ ")
				if os.path.isfile(pathF):
					if pathF in dontCheck:
						continue
					for dirpath, dirnames, filenames in os.walk(checkDir):
						for pp in filenames:
							pathD = dirpath + "/" + pp
							pathD1 = pathD.replace(" ", "\\ ")
							cmd = "diff {} {}".format(pathF1,pathD1)
							if os.path.isfile(pathD):
								k = subprocess.call(cmd, shell=True, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
								if k == 0:
									fiFound.append(pathD)



			if len(fiFound) > 1:
				checkPrompt(fiFound, pathF)

	else:
		# Only the files directly in the directory
		for files in os.listdir(checkDir):
			fiFound = []
			pathF = checkDir + "/" + files
			pathF1 = pathF.replace(" ","\\ ")
			if os.path.isfile(pathF):
				if pathF in dontCheck:
					continue
				# Check files with themselves
				for selif in os.listdir(checkDir):
					pathD = checkDir + "/" + selif
					pathD1 = pathD.replace(" ","\\ ")
					cmd = "diff {} {}".format(pathF1,pathD1)
					if os.path.isfile(pathD):
						k = subprocess.call(cmd, shell=True, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
						if k == 0:
							fiFound.append(pathD)
			
				if len(fiFound) > 1:
					checkPrompt(fiFound, pathF)
	print()


print("Duplicate Remover v1.0")
print("++ exit|stop|quit to stop script ++")
print()

x = "X"
while x != "y" and x != "n":
	x = input("Would you like to check directories within directories? (y/n)   ")
	if x == "exit" or x == "stop" or x == "quit":
		bye = "X"
		while bye != "y" and bye != "n":
			bye = input("Exit? (y/n)   ")
			if bye == "y":
				print("Goodbye!")
				exit()

if x == "y":
	dirdir = True
else:
	dirdir = False

print()

while True:
	dontCheck.clear()
	# Prompt inputs (ask which directory to search)
	print("Pick a directory: ", end="")
	checkDir = input()

	# If exit, ask if they want to exit, else check dir
	if checkDir == "exit" or checkDir == "stop" or checkDir == "quit":
		bye = "X"
		while bye != "y" and bye != "n":
			bye = input("Exit? (y/n)   ")
			if bye == "y":
				print("Goodbye!")
				exit()
	
	# Check if directory exists
	if os.path.isdir(checkDir):
		checkDup(checkDir, dirdir)
	else:
		print("Directory {} not found... (try pwd from the directory you want to check) \n".format(checkDir))
		continue
