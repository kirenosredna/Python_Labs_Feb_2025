#! /usr/bin/python
#  Chapter 5 Exercise 4
# Apply changes to a dictionary
             
machines = {'user100': 'yogi',
            'user1': 'booboo',
            'user2': 'rupert',
            'user3': 'teddy',
            'user4': 'care',
            'user5': 'winnie',
            'user6': 'sooty',
            'user7': 'padders',
            'user8': 'polar',
            'user9': 'grizzly',
            'user10': 'baloo',
            'user11': 'bungle',
            'user12': 'fozzie',
            'user13': 'huggy',
            'user14': 'barnaby',
            'user15': 'hair',
            'user16': 'greppy'
            }

# (a)	user14 no longer has a machine assigned
# machines['user14'] = None
# print(machines['user14'])
#
# # (b)	The name of user16's machine is changed to 'cinnamon'
# machines['user15'] = 'cinnamon'
# print(machines['user15'])
#
# # (c)	user16 is leaving the company,
# # and a new user, user17, will be assigned his machine
# machines['user17'] = machines['user16']
# machines.pop('user16')
# for k, v in machines.items():
#     print(k,v)



 
# (d)	user4, user5, and user6 are all leaving at exactly the same time,
# but their machine names are to be stored in a list called unallocated.
# unallocated = []
# keys_to_remove = []
# for k in machines:
#     if k in ['user4', 'user5', 'user6']:
#         keys_to_remove.append(k)
#
# for k in keys_to_remove:
#     unallocated.append(machines.pop(k))
#
# print(machines)
# print(unallocated)

# unallocated = []
#
# for name in machines:
#     if name in ['user4', 'user5', 'user6']:
#         unallocated.append(machines.pop(name))
#
# print(unallocated)
# print(machines)

unallocated = []

for user in 'user4', 'user5', 'user6':
    unallocated.append(machines.pop(user))

print(unallocated)
print(machines)

# (e) user8 gets another machine called 'kodiak' in addition to the one they already have.
if 'user8' in machines:
    if isinstance(machines['user8'], list):
        machines['user8'].append('kodiak')
    else:
        machines['user8'] = [machines['user8'], 'kodiak']
    print(machines['user8'])
    print(machines)



# (f)	Print a list of all the users, with their machines, in any order.
for user, machine in machines.items():
    print(user,machine)

# (g)	Print a list of unallocated machines, sorted alphabetically.
print(sorted(unallocated))
