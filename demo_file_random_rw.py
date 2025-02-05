#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""

#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo
"""
    Docstring:
"""
#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo how to open, close, and
# read, write and append to text file.
"""
    Docstring:
"""
movies = { 'william': ['fury', 'pulp fiction', 'shawshank redemption'],
           'kirill': ['pulp fiction', 'the departed', 'snatch'],
           'mark': ['fifth element', 'armageddon', 'slapshot'],
           'erik': ['star wars', 'blue velvet', 'dune']
           }

SOF = 0
CUR = 1
EOF = 2

# print can take the arg file = filehandle and print to a file vs filehandle.write

print('-' *60)
with  open(r"yubby.txt", mode="rt") as fh_in:
    fh_in.seek(-90, SOF)
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)}")



