#!/usr/bin/env python3

import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file.read())
        file.close()
        print("Validate YAML!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: checkyaml.py <file>")
