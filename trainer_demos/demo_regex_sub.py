#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO MATCH and SUBSTITUTE a pattern
# a replacement string.
"""
    Docstring:
"""
import re

# Sample line from /etc/passwd on Linux for the root user login
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# I want to MODIFY the string! BUT its IMMUTABLE!
line = re.sub(r"[Ss]uper [Uu]ser", r"Administrator", line) # Returns Modified str
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns TUPLE (modified str, num changes)

print(f"Modified line = {line} with {num} changes")