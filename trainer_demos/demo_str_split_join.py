#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO split and rejoin strings
# using the .split() and .join() methods
"""
    Docstring:
"""

# Sample line from /etc/passwd on Linux for the root user login.
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# AND I want to MODIFY the string! BUT str are IMMUTABLE!
fields = line.split(":") # Return a LIST - LISTA are MUTABLE!
fields[4] = "The Administrator"
fields[6] = "/bin/bash"
line = ":".join(fields) # Returns a new str object

print(line)
