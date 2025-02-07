#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO ITERATE through multiple
# separate but index-related sequences (str/list/tuple/dict/sets)
"""
    Docstring:
"""
import sys

# Create multiple SEPARATE but INDEX-related LISTS.
students = ['erik', 'roberto', 'lokesh']
fav_heroes = ['ghandi', 'sean connery', 'john travolta']
fav_bands = ['rolling stones', 'beatles', 'ac/dc']
fav_locations = ['bassano del grappa', 'venice', 'switzerland']

# ITERATE through the SEPARATE but INDEX-RELATED lists and link indice values
# together using an ITERATOR for loop plus built-in zip() function.
for (s, fh, fb, fl) in zip(students, fav_heroes, fav_bands, fav_locations):
    print(s + " likes to listen to " + fb + " with " + fh + " in " + fl)

sys.exit(0) # Exit script with error code (0=success, 1-255=error code)