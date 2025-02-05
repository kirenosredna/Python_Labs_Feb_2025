#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""
import pickle
import pprint
import gzip # tarfile shutil bz2

movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'erik': ['star wars', 'blue velvet', 'dune']


           }

# with open(r"yubby.p", mode="wb") as fh_out:
with gzip.open(r"yubby.pgz", mode="wb") as fh_out:
    #pickle.dump(movies, fh_out, protocol=0) # pickle 0 ascii and 1-5 binary
    pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL)

# with  open(r"yubby.p", mode="rb") as fh_in:
with  gzip.open(r"yubby.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print('-' *60)
pprint.pprint(films)