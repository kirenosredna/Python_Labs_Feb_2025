#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    A collection for search functions searching one or more files:
"""
import re
# ex of user variadic function
def search_pattern(pattern=r"^.{19}$", *files):
    """ search for regex pattern and return number of lines matched """
    lines = 0
    for file in files:
        fh_in = open(file, mode="rt")

        for line in fh_in:
            m = re.search(pattern, line)

            if m:
                lines += 1
                print(f"matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
        fh_in.close()
    return lines

search_pattern(r"^([A-Z]).*\1$", r"c:\labs\words", r"c:\labs\words2", r"c:\labs\words3")
