#!/usr/bin/python3

import math
import sys

if len(sys.argv) < 4:
    print("Usage: quickmath.py <add|mul|div|sub|avg> <num01> <num02> [num03..num99]")
    exit(1)

w_addition = {"+", "add", "addition", "plus"}
w_subtraction = {"-", "sub", "subtraction", "minus"}
w_multiply = {"*", "x", "mul", "multiply"}
w_divide = {"/", "div", "divide"}

for counter in range(2, len(sys.argv)):
    if not sys.argv[counter].isdigit():
        print("Usage: quickmath.py <add|mul|div|sub|avg> <num01> <num02> [num03..num99]")
        exit(1)

result = float(sys.argv[2])

if sys.argv[1] in w_addition:
    for counter in range(3, len(sys.argv)):
        result = result + float(sys.argv[counter])
elif sys.argv[1] in w_subtraction:
    for counter in range(3, len(sys.argv)):
        result = result - float(sys.argv[counter])
elif sys.argv[1] in w_multiply:
    for counter in range(3, len(sys.argv)):
        result = result * float(sys.argv[counter])
elif sys.argv[1] in w_divide:
    for counter in range(3, len(sys.argv)):
        result = result / float(sys.argv[counter])
else:
    print("Usage: quickmath.py <add|mul|div|sub|avg> <num01> <num02> [num03..num99]")
    exit(1)

print(str(result))
