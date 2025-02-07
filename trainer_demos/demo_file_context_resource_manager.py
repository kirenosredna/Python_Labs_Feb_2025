#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, close, and
# read, write and append to a TEXT file.
"""
    Docstring:
"""

movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'mahendran': ['titanic', 'rambo', 'men in black']
}

# Open a file handle for WRITING in TEXT mode
with open(r"/movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name} {movies[name]}", end="\n")
        fh_out.write(f"{name} {movies[name]}\n")
    # END OF Block - file handle closed automatically.

print("-" * 60)

# Open a file handle for READING in TEXT mode
with open(r"/movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")



