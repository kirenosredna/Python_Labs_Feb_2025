#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, close, and
# read, write and append to a TEXT file.
"""
    Docstring:
"""
import sys

movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'mahendran': ['titanic', 'rambo', 'men in black']
}

# Open a file handle for WRITING in TEXT mode
fh_out = open(r"/movies.txt", mode="at")

# ITERATE through dict and WRITE key+values to file handle.
for name in movies.keys():
    print(f"{name} {movies[name]}", end="\n", file=sys.stdout)
    print(f"{name} {movies[name]}", end="\n", file=fh_out)
    # fh_out.write(f"{name} {movies[name]}\n")

# fh_out.flush() # Manually flush buffers
fh_out.close() # Flush buffers and close file handle

print("-" * 60)

# Open a file handle for READING in TEXT mode
fh_in = open(r"/movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str object. Be careful of HUGE files.
# text = fh_in.read(30) # Read NEXT 30 chars into str.
# text = fh_in.readline() # Read NEXT LINE into str.
# lines = fh_in.readlines() # Read ENTIRE file into a LIST. Be careful of HUGE files.
# print(lines[-1]) # Good as we can INDEX to get specific lines!

# ITERATE through file handle ONE LINE AT A TIME!
# USING an ITERATOR loop plus filehandle (iterator object - next/iter).
for line in fh_in:
    print(line, end="")

fh_in.close()

