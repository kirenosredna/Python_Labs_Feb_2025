#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 RANDOM lottery numbers.
"""
    A collection of Search Functions to search for Regex
    Patterns in one or more files.:
"""
import re

# Example of a user VARIADIC function that allows a
# variable number of parameters (captures in a TUPLE)
def search_pattern(pattern=r"^.{19}$", *files):
    """ Search for a Regex Pattern and return number of lines matched """
    lines = 0
    for file in files:
        fh_in = open(file, mode="rt")

        for line in fh_in:
            m = re.search(pattern, line)  # Match lines 5 char palindromes
            # m = re.search(r"^([A-Z]).*\1$", line, flags=re.IGNORECASE)  # Match lines start/end with SAME CAPITAL!
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
        fh_in.close()
    return lines


search_pattern(r"^([A-Z]).*\1$", r"c:\labs\words", r"c:\labs\words2", r"c:\labs\words3")

