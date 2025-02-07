#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 RANDOM lottery numbers.
"""
    Docstring:
"""
import re

# Open File Handle for READING in TEXT mode
fh_in = open(r"c:\labs\words", mode="rt")

# ITERATE through file handle one line at a time.
for line in fh_in:
    # Example of str testing = GOOD!
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search(r"^the", line) # Match lines starting with 'the'
    # m = re.search(r"ing$", line)  # Match lines ending with 'ing'
    # m = re.search(r"^ring$", line)  # Match lines ending with 'ing'
    # m = re.search(r"^.ing$", line)  # Match lines of 4 chars ending with 'ing'
    # m = re.search(r"^...................$", line)  # Match lines of exactly 19 chars
    # m = re.search(r"^.{19}$", line)  # Match lines of exactly 19 chars
    # m = re.search(r"^[adr]ing$", line)  # Match lines with [adr] followed 'ing'
    # m = re.search(r"^[A-Z]", line)  # Match lines starting with a CAPITAL
    # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match lines 3 consecutive vowels
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines 5 consecutive vowels
    # m = re.search(r"[0-9][0-9]", line)  # Match lines 2 consecutive digits
    # m = re.search(r"\.", line)  # Match lines with a DOT. You will be WARNED!
    # m = re.search(r"[.]", line)  # ANOTHER WAY TO ESCAPE!
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines start/end with a CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # Match lines of 6 chars start/end with a CAPITAL
    # m = re.match(r"^[A-Z].{4}[A-Z]$", line)  # AUTO MATCHES LINES STARTING WITH...
    # m = re.fullmatch(r"^[A-Z].{4}[A-Z]\n$", line)  # Match ENTIRE LINE incl HIDDEN chars!
    m = re.search(r"^(.)(.).\2\1$", line)  # Match lines 5 char palindromes
    # m = re.search(r"^([A-Z]).*\1$", line, flags=re.IGNORECASE)  # Match lines start/end with SAME CAPITAL!
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}, "
              f"Groupings = {m.groups()}, Group 1 = {m.group(1)}")
