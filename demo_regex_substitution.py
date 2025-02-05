#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo how to match and substitute
"""
    Docstring:
"""
import re
# sample line from /etc/passwd on Linux root login

line = "root:x:0:0:The Super User:/root:/bin/ksh"

# modify some fields but immutable
line = re.sub(r"[Ss]uper [Uu]ser", r"Administrator", line)
(line, num) = re.subn(r"ksh$", r"bash", line)
print(f"modiied line = {line} with {num} changes")