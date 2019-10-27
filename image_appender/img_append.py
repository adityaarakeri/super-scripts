import os
import sys

usage = """
    Usage: python3 img_append.py [+/-] img1 img2 output_file_name
    + for horizontal append
    - for vertical append
"""

if len(sys.argv)<5:
    print(usage)
    sys.exit()

append = sys.argv[1]
img1 = sys.argv[2]
img2 = sys.argv[3]
output = sys.argv[4]

if append not in ['+', '-']:
    print(usage)
    sys.exit()

cmd = "convert {}append {} {} {}".format(append, img1, img2, output)
print(cmd)
os.system(cmd)
