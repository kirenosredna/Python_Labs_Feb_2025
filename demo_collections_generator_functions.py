#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Generator function demo
"""


def get_numbers():
    """ return list of numbers"""
    numbers = []
    for x in range(0, 10):
        numbers.append(x)
    return numbers


for z in get_numbers():
    print(z)


def generate_numbers():
    """yield one object at a time"""
    for x in range(0, 100):
        yield x # don't use/need return if using yield more efficient for memory


for z in generate_numbers():
    print(z)

# alternatively , we could use a while loop
gen = generate_numbers()
while True:
    # num = next(gen, False)
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

# request the next yielded number
gen = generate_numbers()
num1 = next(gen, False)
num2 = next(gen)
num3 = next(gen)
print(num1, num2, num3)



