#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""
import re

def search_pattern(pattern=r"^.{19}$", file=r"c:\labs\words"):
    lines = 0
    fh_in = open(file, mode="rt")

    for line in fh_in:
        m = re.search(pattern, line)

        if m:
            lines += 1
            print(f"matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")

    return lines

search_pattern()
num_lines = search_pattern(r"^([A-Z]).*\1$", r"c:\labs\words")
print(f"Matched {num_lines} lines")