#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create a set, grow a set, shrink
# a set and combine sets using SET OPERATORS (Remember VENN Diagrams)
# SETS are UNORDERED!
"""
    Docstring:
"""

marvel_fans = {'donald', 'erik', 'stephen', 'aram', 'jorge', 'lokesh'}
dc_fans = set() # Create an empty SET!

# Grow a SET
dc_fans.add('donald')
dc_fans.add('zane')
dc_fans.add('matthew')

# Shrink a SET
# dc_fans.pop() # Randomly REMOVE an object.

comic_fans = dc_fans.copy() # Copy SET
comic_fans.clear() # Empty SET

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")
print("-" * 60)

# COMBINE the SETS using SET operations (Remember VENN Diagrams).
print(f"Fans of Marvel OR DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 20)
# COMBINE the SETS using SET OPERATORS (Remember VENN Diagrams).
print(f"Fans of Marvel OR DC = {marvel_fans | dc_fans}")
print(f"Fans of Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of ONLY Marvel OR DC = {marvel_fans ^ dc_fans}")