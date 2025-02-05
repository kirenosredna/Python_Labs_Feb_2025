#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""

import re

# open filehandle  for reading in text
fh = open(r"c:\labs\words", mode="rt")

# iterate on each line
for line in fh:
    #line = line.strip()
    #if line.startswith("Y") and line.strip().endswith("n") and "town" in line:
    m = re.search("the", line) # returns NoneType(False) or REmatch(True)
    if m:
        print(line, end="")