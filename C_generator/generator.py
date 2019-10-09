#!/usr/bin/python
from sys import argv

def checkInt(val):
    try:
        val = int(val)
        return True
    except ValueError:
        return False

size = len(argv)
if (size>1):
    command = argv[1]
    if (command == "for"):
        indicator = "i"
        maxi = 0
        if (size>2):
            if (not checkInt(argv[2])):
                indicator = argv[2]
            else:
                argv = argv[:2] + [argv[2]] + argv[2:]
                size += 1
        if (size>3):
            maxi = argv[3]
        print("for ({0}=0; {0} < {1}; {0}++)".format(indicator,maxi))
        print("{")
        print("")
        print("}")
    if command=="struct":
        name = "myStruct"
        if size > 2:
            name = argv[2]
        print("typedef struct {0}".format(name))
        print("{")
        print("")
        print("} {0};".format(name))
    if command == "main":
        print("int main(int argc, char** argv)")
        print("{")
        print("")
        print("}")
    if command == "includes":
        print ("#include <stdio.h>")
        print ("#include <stdlib.h>")
        print ("#include <string.h>")
    if command == "pi":
        arr = argv[2:]
        if (len(arr) == 0):
            arr = ["i"]
        arr2 = ["%i" for l in arr]
        print("printf(\"{0}\\n\",{1})".format(" ".join(arr2), ", ".join(arr)))
