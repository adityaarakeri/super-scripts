import sys
from PIL import Image

img_src = sys.argv[1]
img_dst = sys.argv[2]
quality = int(sys.argv[3])

img = Image.open(img_src)
img.save(img_dst, optimize=True, quality=quality)