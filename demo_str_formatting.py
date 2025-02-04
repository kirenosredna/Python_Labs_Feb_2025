#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo howto format strings
# using str concatenation and escape chars, str justification methods,
# the str.format() and f-strings.
"""
    Docstring:
"""

# dict of planetary info including
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597787,
           'Mars': 227.94}

for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm\t" + str(hex(0xff)))

print("-" *60)

for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).center(12,'.') + " Gm\t" + str(hex(0xff)))



print("-" *60)

for planet in planets.keys():
    print("{0:>12s}: {1:>12.3f} Gm {2:#6x}".format(planet, planets[planet], 0xff))

print("-" *60)
# using f-stings Python 3.5 later
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:>12.3f} Gm {2:#6x}".format(planet,planets[planet], 0xff))