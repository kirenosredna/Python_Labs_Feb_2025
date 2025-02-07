#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, and grow, and shrink
# dictionaries (Unordered Collections with UNIQUE keys).
# NOTE: dict are in INSERTION order after Python 3.6.
"""
    Docstring:
"""
import pprint

movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'mahendran': ['titanic', 'rambo', 'men in black']
}

# Grow the dict
movies['erik'] = ['star wars', 'blue velvet', 'dune']
movies['elizabeth'] = ['gladiator', 'mulan', 'six triple eight']


# Remove key-value pairs from dict
movies.pop('mark') # Remove key + value
movies.popitem() # Remove LAST key+value INSERTED

pprint.pprint(movies)
print("-" * 60)
print(f"Erik's ultimate film is {movies.get('erik')}")
print(f"Erik's favourite films are {movies['erik']}") # Prefer this over above!
print(f"Erik's ultimate film is {movies['erik'][0]}")

# films = movies.copy() # Copy dict
# films.clear() # Empty dictionary
# pprint.pprint(films)

# ITERATE through the dict keys by using the .keys() method
for person in movies.keys():
    print(f"{person} likes {movies[person]}")

# ITERATE through the dict VALUES by using the .values() method
for films in movies.values():
    print(f"Good films = {films}")

# ITERATE through the dict KEYS+VALUES by using the .items() method
for (person, films) in movies.items():
    print(f"{person} loves {films}")