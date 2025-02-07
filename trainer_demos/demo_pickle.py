#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import pickle
import pprint
import gzip # Others such tarfile, shutil, bz2

movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'mahendran': ['titanic', 'rambo', 'men in black']
}

# Open a file handle for WRITING in BINARY mode
# with open(r"c:\users\donal\course\Python_Labs_Feb_2025\movies.p", mode="wb") as fh_out:
with gzip.open(r"/movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Pickle Protocol (0=ASCII, 1-5=Binary)
    # pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL) # Default 5
    pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL) # Highest 5


# Open a file handle for READING in BINARY mode
# with open(r"c:\users\donal\course\Python_Labs_Feb_2025\movies.p", mode="rb") as fh_in:
with gzip.open(r"/movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)



