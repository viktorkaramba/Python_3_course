# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# users = dict()
# for letter in handle:
#     letter = letter.rstrip()
#     l = letter.split()
#     if len(l) == 0:
#         continue
#     else:
#         if l[0] == 'From':
#             print(l)
#             users[l[1]] = users.get(l[1], 0) + 1
#
# mx = 0
# email = None
# for user, count in users.items():
#     if count > mx:
#         mx = count
#         email = user
import re

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for letter in handle:
    l = letter.split()
    if len(l) == 0:
        continue
    else:
        if l[0] == 'From':
            hour = l[5].split(':')
            counts[hour[0]] = counts.get(hour[0], 0) + 1

tmp = list()
for v, k in counts.items():
    tmp.append((v, k))
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)