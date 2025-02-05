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
    #m = re.search("^the", line) # returns NoneType(False) or REmatch(True)
    #m = re.search(r"ing$", line)  # returns NoneType(False) or REmatch(True)
    #m = re.search(r"^ring$", line)  # returns NoneType(False) or REmatch(True)
    #m = re.search(r"^.ing$", line)  # returns NoneType(False) or REmatch(True)
    #m = re.search(r"^.{19}$", line)  # exactly 19 returns NoneType(False) or REmatch(True)
    #m = re.search(r"^[adr]ing$", line)  # returns NoneType(False) or REmatch(True)
    #m = re.search(r"^[A-Z]", line)  # returns NoneType(False) or REmatch(True)
    #m = re.search(r"[aeiou]{5,}", line)  # returns NoneType(False) or REmatch(True)
    #m = re.search(r"[0-9][0-9]", line)  # returns NoneType(False) or REmatch(True)
    #m = re.search(r"\.", line)
    #m = re.search(r"^[A-Z].*[A-Z]$", line)  # returns NoneType(False) or REmatch(True)
    # m = re.search("^[A-Z].{4}[A-Z]$", line)
    #m = re.match("[A-Z].{4}[A-Z]$", line) # auto matches lines starting don't need anchor
    #m = re.fullmatch("^[A-Z].{4}[A-Z]\n$", line) # has to match entire line including hidden chars!
    # m = re.search(r"^(.)(.).\2\1$", line) # use r" " for raw get in habit
    # m = re.search(r"^([A-Z]).*\1$", line) # lines start end with same capital
    m = re.search(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z]{2}$", line) # UK Postcode regex

    # Alternation (OR)
    #"donald|dcameron|Sir D Cameron"
    # a (bottle|glass) of (beer|wine|lager)"
    if m:
        print(line, end="")
