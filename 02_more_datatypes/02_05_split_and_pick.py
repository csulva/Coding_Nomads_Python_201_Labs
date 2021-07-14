# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.
from collections import Counter
import statistics

ran_string = input('What are your thoughts? ')
x = ran_string.split()
print(x)
for i in x:
    print(i)
print(statistics.mode(x))
#print(Counter(x).most_common)