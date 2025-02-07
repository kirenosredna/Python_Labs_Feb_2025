#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO format strings using
# str concatenation and escape chars, str justification methods,
# the str.format() method and f-strings!
"""
    Docstring:
"""

# Dict of planetary info including distance to the SUN in Gigametres.
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# ITERATE through the dict keys and print planet info
# using str concatenation plus escape chars - UGLY!
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm\t" + str(hex(0xff)))

print("-" * 60)
# using str concatenation plus justification methods - OK!
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).center(12, '.') + " Gm " + str(hex(0xff)).rjust(6))

print("-" * 60)
# using str.format() method - GOOD!
for planet in planets.keys():
    print("{0:>12s}: {1:>12.3f} Gm {2:#6x}".format(planet, planets[planet], 0xff))

print("-" * 60)
# using f-strings (Python 3.5 onwards) method - My favourite!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:>12.3f} Gm {0xff:#6x}")