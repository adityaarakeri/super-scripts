# sourse: https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

import sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

md5 = hashlib.md5()
sha1 = hashlib.sha1()

file_path = ""
have_command_arg = len(sys.argv) > 1
if have_command_arg:
	file_path = sys.argv[1]
else:
	file_path = input("what if the path of the file?: ")

with open(file_path, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)

print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))
