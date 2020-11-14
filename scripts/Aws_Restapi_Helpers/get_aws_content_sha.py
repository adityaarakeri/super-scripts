import hashlib
import sys

if len(sys.argv) < 2:
    payload = ''
else:
    payload = sys.argv[1]

print(hashlib.sha256(payload.encode('utf-8')).hexdigest())