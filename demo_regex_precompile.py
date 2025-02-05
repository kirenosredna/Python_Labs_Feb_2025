#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""

import re

# open filehandle  for reading in text
fh = open(r"c:\labs\words", mode="rt")

reobj = re.compile(r"^([A-Z]).*\1$")
# iterate on each line
for line in fh:
    m = reobj.search(line) # UK Postcode regex
    if m:
        print(line, end="")
