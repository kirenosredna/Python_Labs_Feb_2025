#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""
# source collection
students = ['euler', 'jorge', 'aram', 'mark', 'elizabeth', 'jeremy', 'erik', 'javonn', 'kirill']

wee_names = []

# iterator to filter and copy to a dest
for name in students:
    if len(name) <= 5:
        wee_names.append(name) #
print(f"1.Short names = {wee_names}")


def filter_names(name):
    """ return true if name is less than 5 chars"""
    if len(name) <= 5:
        return True
    else:
        return False

for name in students:
    if filter_names(name):
        wee_names.append(name)
print(f"2.short names = {wee_names}")


# built in filter() function

wee_names = list(filter(filter_names, students))
print(f"3.short names = {wee_names}")


# using built in filter with lambda
wee_names = list(filter(lambda name:len(name) <= 5, students))
print(f"4.short names = {wee_names}")

wee_names = [name.upper() for name in students if len(name) <= 5] # list comprehension expression, optional condition
print(f"5.short names = {wee_names}")

wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ] # LIST comprehension expression, optional condition
print(f"5.1.short names = {wee_names}")

wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 } # DICT comprehension expression, optional condition
print(f"5.2.short names = {wee_names}")

wee_names = { name.upper() for name in students if len(name) <= 5 } # SET comprehension expression, optional condition
print(f"5.3.short names = {wee_names}")