import base64
import sys

action_type = sys.argv[1]
src_file = sys.argv[2]
dest_file = sys.argv[3] if action_type == "decode" else None

if action_type == "encode":
  with open(src_file, "rb") as image_file:
      encoded_string = base64.b64encode(image_file.read())
      print(encoded_string)
else:
  imgdata = base64.b64decode(imgstring)
  with open(dest_file, 'wb') as f:
      f.write(imgdata)
