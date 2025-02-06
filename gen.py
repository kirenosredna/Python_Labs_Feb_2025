#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
 function similar to range but take a floating point number as the step.
"""

def frange(start, stop, step=0.25):
    starting = float(start)
    if step == 0:
        print(f"don't use zero as the step value")
        return []

    while starting < stop:
        yield starting
        starting += step

print(frange(1, 2, 0))
print(list(frange(1, 3, 0)))
print(list(frange(1, 3, 0.33)))
print(list(frange(1, 3, 1)))         # Should return [1.0, 2.0], not [1, 2]
print(list(frange(3, 1)))            # Should return an empty list
# print(list(frange(-1, -0.5, 0.1)))

# for num in frange(3.142, 12):
#     print(f"{num:05.2f}")