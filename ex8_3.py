#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Use data in country.txt file create a dictionary where country name is the key and other records are
    values stored as a list. pickle the data structure as file named country.p

"""
import pickle
import gzip
import shelve
import pprint


filename = r"labs/country.txt"
with open(filename, 'rt') as file:
    country_dict = {}
    for line in file:
        if line.isspace(): continue
        line = line.strip()
        name, *values = line.split(',')
        country_dict[name] = values

file.close()


# use pickle to writ data structure and read back in from pickle file
out = gzip.open('country.pgz', 'wb')
pickle.dump(country_dict, out, pickle.HIGHEST_PROTOCOL)
out.close()

with gzip.open('country.pgz', 'rb') as file:
    c = pickle.load(file)
file.close()

pprint.pprint(c)

for country, values in c.items():
    print(country, values)






# using a shelve
with shelve.open('country.db') as db:
    for country in country_dict.keys():
        db[country] = country_dict[country]

db.close()

try:
    db = shelve.open('country.db')

    for cn, values in db.items():
        print(cn, values)

    if 'Vietnam' in db:
        print(f"Extracting data on Vietnam: {db['Vietnam']}")
    else:
        print(f"unable to find key in db")
except Exception as e:
    print(f"Unexpected error: {e}")
except FileNotFoundError:
    print("No country shelve file")





# for name, values in country.items():
#     print(name, values)