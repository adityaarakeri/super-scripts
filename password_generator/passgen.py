import random
import string

up = string.ascii_uppercase
lo = string.ascii_lowercase
num = string.digits
sym = string.punctuation

len=int(input("Enter password length\n"))

s= []
s.extend(list(up))
s.extend(list(lo))
s.extend(list(num))
s.extend(list(sym))
#print(s)
random.shuffle(s)
#print(s)
print("".join(s[0:len]))