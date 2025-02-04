#! /usr/bin/python
#                    1         2         3         4
#          012345678901234567890123456789012345678901234567890
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'


print("-" * len(Belgium)) # never would have thought to do this.
length = len(Belgium.split(','))
print(f"There are {length} comma separated fields in the string Belgium")
print(f" The length of the string Belgium is {len(Belgium)} chars")

print(Belgium.replace(',',':'))


for field in Belgium.split(','):
    print(field, end=" ")

