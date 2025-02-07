#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import shelve

movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
}

tv_series = { 'william': ['fame', 'walking dead'],
              'kirill': ['got', 'outlander'],
              'mark': ['cagney and lacey', 'scooby doo']
}

books = { 'william': 'the hobbit',
          'kirill': 'lotr',
          'mark': 'world war z'
}

with shelve.open(r"c:\users\donal\course\Python_Labs_Feb_2025\movies") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"c:\users\donal\course\Python_Labs_Feb_2025\movies") as db:
    print(f"Williams favourite movies are {db['movies']['william']}")
    print(f"Kirill's favourite tv_Series is  {db['tv_series']['kirill'][0]}")
    print(f"Mark's favourite book is {db['books']['mark']}")


