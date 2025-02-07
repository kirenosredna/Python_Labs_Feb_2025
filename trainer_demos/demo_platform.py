#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo how to check which platform
# your script is running on.
"""
    Docstring:
"""

import sys
import os

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"] # Pick
else:
    home_dir = os.environ["HOME"]

print(home_dir)