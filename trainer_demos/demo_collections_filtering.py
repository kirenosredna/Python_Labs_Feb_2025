#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO copy and optionally filter
# source collection to a destination collection using different methods.
"""
    Docstring:
"""

# Source collection - list of strings
students = ['euler', 'jorge', 'aram', 'mark', 'elizabeth',
            'jeremy', 'erik', 'javonn', 'kirill', 'aram', 'euler']

# Iterate through the collection and copy to a destination
# Using an ITERATOR loop plus source, optional condition, an expression
wee_names = []
for name in students: # 1.Iterator Loop + source
    if len(name) <= 5: # 2.Optional condition - filtering
        wee_names.append(name.upper()) # 3.Expression
print(f"1.Short names = {wee_names}")


# Using an ITERATOR loop plus source, user function for filtering, an expression
def filter_names(name):
    """ Return True if name is shorter < 5 chars """
    if len(name) <= 5:
        return True
    else:
        return False

wee_names = []
for name in students:
    if filter_names(name):
        wee_names.append(name.upper())
print(f"2.Short names = {wee_names}")

# Using built-in filter() function, user function for filtering.
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# Using built-in filter() function, user function for filtering.
wee_names = list(filter(lambda name:len(name) <= 5, students)) # EEK!
print(f"4.Short names = {wee_names}")

# Using LIST COMPREHENSION: expression, optional condition (filtering), iterator loop.
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# Using LIST COMPREHENSION: expression, optional condition (filtering), iterator loop.
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1.Short names = {wee_names}")

# Using DICT COMPREHENSION: expression, optional condition (filtering), iterator loop.
# EXTRA FILTERING - removes DUPLICATE keys!
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2.Short names = {wee_names}")

# Using SET COMPREHENSION: expression, optional condition (filtering), iterator loop.
# EXTRA FILTERING - removes DUPLICATE values!
wee_names = { name.upper() for name in students if len(name) <= 5 }
print(f"5.3.Short names = {wee_names}")