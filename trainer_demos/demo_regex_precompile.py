#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 RANDOM lottery numbers.
"""
    Docstring:
"""
import re


# Open File Handle for READING in TEXT mode
fh_in = open(r"c:\labs\words", mode="rt")

reobj = re.compile(r"^([A-Z]).*\1$") # PRECOMPILE Pattern JUST ONCE!

# ITERATE through file handle one line at a time.
for line in fh_in:
    # m = re.search(r"^([A-Z]).*\1$", line)  # Match lines start/end with SAME CAPITAL!
    m = reobj.search(line)  # Use precompiled pattern
    if m:
        print(line, end="")
