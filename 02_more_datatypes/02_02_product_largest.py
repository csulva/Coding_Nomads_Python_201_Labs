# Take in 10 numbers from the user. Place the numbers in a list.
# You can also use the provided random `randlist` list
# to simulate user input.
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

import math
list_1 = []
product = 1
for num in range(10):
    x = input('give me a random number: ')
    x = int(x)
    list_1.append(x)

for y in list_1:
    product = product * y
print(max(list_1))
print(product)
