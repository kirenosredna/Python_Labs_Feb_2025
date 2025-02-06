#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    User function takes two arguments a value and a list. the list parameter should default to
    and empty list

    def my_function(value, list=[]):

    so if you set the default=None it will be empty each time
"""

def my_function(value, list = None):
    if list == None:
        list = []

    list.append(value)
    print(f"The list is {list}")
    return

my_list = [1, 2, 3]
value = 98
my_function(value,my_list)
my_function(43, )
my_function(13)
my_function(4, my_list)


