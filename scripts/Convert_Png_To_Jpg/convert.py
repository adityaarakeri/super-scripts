import sys
from PIL import Image

src_file = sys.argv[1]
dst_file = 'jpg'.join(src_file.rsplit('png', 1))

im = Image.open(src_file)
rgb_im = im.convert('RGB')
rgb_im.save(dst_file)