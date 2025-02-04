#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo howto iterate through a
# sequence one item at a time using an iterator for loop
"""
    Docstring:
"""
films = ['casshern','pulp fiction','idoiocracy', 'matrix', 'pursuit of happieness',
         'titanic', 'lotr', 'top gun']

#iterate through list sequence one at at time iterator for loop
for film in films:
    print(film, end='\n')

#iterate through list sequence and Modify one at at time iterator for loop
idx = 0
for film in films:
    #print(film.upper(), end='\n')
    films[idx] = film.upper()
    idx += 1
print(films)


for (idx, film) in enumerate(films):
    #print(film.title())
    films[idx] = film.title()
print(films)



