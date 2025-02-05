#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo how to open, close, and
# read, write and append to text file.
"""
    Docstring:
"""
movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'erik': ['star wars', 'blue velvet', 'dune']


           }
filename = "yubby.txt"
fh_out = open(r"yubby.txt", mode="wt")

# iterate through dict  and write keys+values to file

for name in movies.keys():
    print(f"{name} {movies[name]}", end="\n")
    fh_out.write(f"{name} {movies[name]}\n")

fh_out.flush()
fh_out.close() # flush buffer and close file handle

print('-' *60)
fh_in = open(r"yubby.txt", mode="rt")
text = fh_in.read() # entire file into str obj
text = fh_in.read(30) # read next 30 chars into str
text = fh_in.readline() # read entire file into a LIST
lines = fh_in.readlines() # index to get specific lines
print(text)
# iterate through file handle one line at a time
#using an iterator loop plus file handle
for line in fh_in:
    print(line, end='')


fh_in.close()