#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo howto split and rejoin strings
# using the .split() and .join() methods
"""
    Docstring:
"""

line = "root:x:0:0:The Super User:/root:/bin/ksh"

fields = line.split(":")
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields)
print(line)