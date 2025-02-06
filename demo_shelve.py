#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""
import shelve

movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'erik': ['star wars', 'blue velvet', 'dune']
         }

tv_series = { 'william': ['fame', 'walking dead'],
              'kirill': ['got', 'outlander'],
              'mark': ['cagney and lacey', 'scooby doo']
              }

books = { 'william': [ 'the hobbit'],
           'kirill': ['lotr'],
          'mark': ['world war z']
          }

with shelve.open(r"movies") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"movies") as db:
    print(f"{db['movies']['william']}")
    print(f"{db['tv_series']['kirill'][0]}")

    set called all ports and use range function to generate ports 1- 200 = allports
    allports = set(range(1, 201))
    usedports = set()
    add etc/services to in windows32

    (\dt)/(tcp|udp)
    m.group