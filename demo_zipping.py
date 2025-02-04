#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo how to iterate through multiple
# sequences (str/list/tuple/dict/sets)
# separate but index related  sequences
"""
    Docstring:
"""

students = ["erik", "roberto", "lokesh"]
fav_heroes = ['ghandi','sean connery', 'john travolta']
fav_bands = ['rolling stones', 'beatles', 'ac/dc']
fav_locations = ['bassano del grappa', 'venice', 'switzerland']

for (s, fh, fb, fl)  in zip(students, fav_heroes, fav_bands, fav_locations):
    print(f"{s} likes to listen to {fb} with {fh} in {fl}")