#!/usr/bin/env python3

import os
	
# diff: 0 if same, 1 if different, 2 if trouble

# Global list
dontCheck = set()

def checkDup(checkDir, dirdir):
	print("Checking directory {}".format(checkDir))

	# Walk through path and check if there are any duplicates
	if dirdir:
		# For dirpath, dirname, filenames in directory
		for dp, dn, fn in os.walk(checkDir):
			# For file in filenames
    		for f in fn:
				f.replace(" ","\ ")
				pathF = dp + "/" + f
				for dirpath, dirnames, filenames in os.walk(checkDir):
					for pp in filenames:
						pp.replace(" ", "\ ")
						pathD = dirpath + "/" + pp

	else:
		# Only the files directly in the directory
		for files in os.listdir(checkDir):
			files.replace(" ","\ ")
			pathF = checkDir + "/" + files
			# Check files with themselves
			for selif in os.listdir(checkDir):
				selif.replace(" ", "\ ")
				pathD = checkDir + "/" + selif
	

	# If directory found, check for duplicates
	fiFound = ["WD","As", "Pee"]

	# If duplicates found, notify that duplicates have been found
	print("Duplicates found for {}.".format(fiFound))

	# Display all the duplicates of that file in form (1: ... \n 2: ... etc.)
	for key, fi in enumerate(fiFound):
		print("{}. {}".format(key + 1, fi))

	# Prompt if they would like to keep all files
	keepAll = "X"
	while keepAll != "y" and keepAll != "n":
		keepAll = input("Would you like to keep all the above files? (y/n)   ")

	if keepAll == "n":
		for fi in fiFound:
			delFile = "X"
			while delFile != "y" and delFile != "n":
				delFile = input("Would you like to delete {}? (y/n)\t".format(fi))
			if delFile = "y":
				final = input("(Safe Delete) Are you sure you would like to delete {}? (y/n)\t".format(fi))
					if final = "y":
						# Remove from list AND dir
						fiFound.remove(fi)
	
	# Don't check these files again
	dontCheck = dontCheck + fiFound

	print()


print("Duplicate Remover v1.0")
x = "X"
while x != "y" and x != "n":
	x = input("Would you like to check directories within directories? (y/n)   ")
if x == "y"
	dirdir = True
else:
	dirdir = False

print()

while True:
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
