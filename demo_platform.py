#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo how to check which platform the script is
# running on.
"""
    Docstring:
"""

import sys
import os

print(sys.platform)
if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print(home_dir)


