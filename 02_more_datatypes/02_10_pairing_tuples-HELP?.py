# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

l = randlist
print(l)
y = randlist
print(y)
x = randlist
x = sorted(x)
# if len(l) % 2 != 0:
#     l.append[0]

out = [tuple(l[i: i + 2]) for i in range(0, len(l), 2)]

# for i in range(0, len(l), 2):
#     if len(l) % 2 != 0:
#         out = tuple(l[i: i + 2].append(0))
#     else:
#         out = tuple(l[i: i+2])


print(x)
print(out)

#print(out)
# Write your code below here
