#! /usr/bin/env python3
# Author: DCameron
# Description: This script will generate 6 RANDOM lottery numbers.
"""
    Docstring:
"""
import re

# Example of a user function with parameter passing
# and default values
def search_pattern(pattern=r"^.{19}$", file=r"c:\labs\words"):
    lines = 0
    fh_in = open(file, mode="rt")
    reobj = re.compile(pattern) # Compile pattern ONCE

    for line in fh_in:
        # m = re.search(pattern, line)  # Match lines 5 char palindromes
        m = reobj.search(line)
        if m:
            lines += 1
            print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")

    return lines

def main():
    search_pattern()

    # Now use the CALLER as a r-val
    num_lines = search_pattern(r"^([A-Z]).*\1$", r"c:\labs\words")
    print(f"Matched {num_lines} lines")
    return None

if __name__ == "__main__":
    import cProfile
    # cProfile.run("main()") # Profile/analyse to console.
    cProfile.run("main()", "stats.prof")  # Profile/analyse to file
    # main()
