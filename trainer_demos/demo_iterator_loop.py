#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO ITERATE through a SEQUENCE
# ONE item at a time using an ITERATOR for loop.
"""
    Docstring:
"""
#            0             1              2           3             4
films = ['casshern', 'pulp fiction', 'idiocracy', 'matrix', 'pursuit of happiness',
         'titanic', 'lotr', 'top gun']

# ITERATE through my list sequence one film at a time
# Using an ITERATOR for loop.
for film in films:
    print(film, end="\n")

# ITERATE through and MODIFY my list sequence one film at a time
# Using an ITERATOR for loop.
idx = 0
for film in films:
    print(film.upper(), end="\n")
    films[idx] = film.upper()
    idx += 1
print(films)

# ITERATE through and MODIFY my list sequence one film at a time
# Using an ITERATOR for loop and built-in enumerate() function.
# enumerate(seq, start=0) returns TUPLE(idx, object)
for (idx, film) in enumerate(films, start=0):
    print(film.title(), end="\n")
    films[idx] = film.title()
print(films)