#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo how to create, grow, shrink,
#a set and combine sets using set operators ( venn diagram)
# Sets are unordered
"""
    Docstring:
"""
marvel_fans = {'donald','erik','stephen', 'aram', 'jorge', 'lokesh'}

dc_fans = set() # create empty set

dc_fans.add('donald')
dc_fans.add('zane')
dc_fans.add('matthew')

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")
print('-' * 60)


# combine the sets
print(f"Fans of marvel OR dc = {marvel_fans.union(dc_fans)}")
print(f"Fans of marvel AND dc = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of marvel ONLY dc = {marvel_fans.difference(dc_fans)}")
print(f"Fans of marvel ONLY OR DC {marvel_fans.symmetric_difference(dc_fans)}")

print('-' * 20)
# combine the sets
print(f"Fans of marvel OR dc = {marvel_fans | dc_fans}")
print(f"Fans of marvel AND dc = {marvel_fans & dc_fans}")
print(f"Fans of marvel ONLY dc = {marvel_fans - dc_fans}")
print(f"Fans of marvel ONLY OR DC {marvel_fans ^ dc_fans}")