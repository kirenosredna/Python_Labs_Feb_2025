#! /usr/bin/env python3
# Author: Erik Anderson
# Description: This script will demo how to display unused ports from etc/services
"""
    set called all ports and use range function to generate ports 1- 200 = allports
    allports = set(range(1, 201))
    usedports = set()
    add etc/services from  windows/system32/drivers/
    (\d+)/(tcp|udp) regex
    m.group
"""

import re
import sys
from http.cookiejar import user_domain_match

if sys.platform == "win32":
    filename = r"c:\Windows\System32\drivers\etc\services"
else:
    filename = r"/etc/services"

with open(filename, mode="rt") as fh_in:
    allports = set(range(1,201))
    used_ports = set()

    for line in fh_in:
        # if line.isspace(): continue
        # if line.startswith("#"):continue
        # line = line.strip()
        match = re.search(r"(\d+)(/tcp|/udp)", line)
        if match:
            port = int(match.group(1))
            if port <= 200:
                used_ports.add(port)
print(used_ports)
        # used_ports.add(port)
        # line = allports - used_ports
        # print(used_ports)


# # Working code
# allports = set(range(1,201))
# used_ports = set()
# with open(filename, mode="rt") as fh_in:
#     for line in fh_in:
#         m = re.search(r"(\d+)/(tcp|udp)", line)
#         if m:
#             port = int(m.group(1))
#             if port <= 200:
#                 used_ports.add(port)
# print(f"All Ports = {allports}")
# print(f"Used Ports = {used_ports}")
# print(f"{allports} - {used_ports}")
