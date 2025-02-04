#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo to display entire unicode table
"""
    Docstring:
"""
# iterate
for pos in range(0, 65536):
    try:
        print( chr(pos), end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeError:
        print(" ")
