#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Use data in country.txt file create a dictionary where country name is the key and other records are
    values stored as a list. pickle the data structure as file named country.p

"""

filename = r"labs/country.txt"
with open(filename, 'rt') as file:
    country = {}
    for line in file:
        if line.isspace(): continue
        line = line.strip()
        name, *values = line.split(',')
        country[name] = values

file.close()

for name, values in country.items():
    print(name, values)