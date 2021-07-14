# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?
import itertools

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9,]]
new_list = [num for sublist in starter_list for num in sublist]

new_list_3 = []

for sublist in starter_list:
    for num in sublist:
        new_list_3.append(num)
print(new_list)
print(new_list_3)

second_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9, [10, 11, 14, 14, [15, 16]]]]
new_list_4 = []

#new_list_5 = list(itertools.chain(*new_list_4))

print(new_list_4)