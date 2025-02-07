#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, close, and
# read, write and append RANDOMLY to a TEXT file using .seek() and .tell()
"""
    Docstring:
"""

movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'mahendran': ['titanic', 'rambo', 'men in black']
}
SOF = 0 # Start of file
CUR = 1 # Current file position
EOF = 2 # End of File

# Open a file handle for READING in TEXT mode
with open(r"/movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, SOF) # Seek forwards 90 chars from SOF.
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(140, SOF) # Seek forwards 140 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

# Open a file handle for READING in BINARY mode
with open(r"/movies.txt", mode="rb") as fh_in:
    fh_in.seek(-90, EOF) # Seek backwards 90 bytes from EOF.
    text = fh_in.read(30)
    print(f"Bytes at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(-65, CUR) # Seek back 65 bytes from CURRENT position
    text = fh_in.read(140)
    print(f"Bytes at {fh_in.tell() - len(text)} = {text}")



