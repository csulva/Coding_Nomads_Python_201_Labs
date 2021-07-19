# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

from collections import Counter


list_ = [1, 2, 3, 4, 3, 4, 5, 5, 7, 8, 8, 8, 8, 8, 9, 36]
list_2 = set(list_)
list_3 = []

for x in Counter(list_):
    list_3.append(x)
# for x in list_:
#     list_3.append(x)
#     if x in list_3: 
#         list_3.remove(x)
print(list_3)
# enum

#print(list_2)