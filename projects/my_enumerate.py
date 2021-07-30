# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(iterable, number=0):
      for x in iterable:
            new_tuple = number, x
            print(new_tuple)
            number += 1

def my_enumerate_2(iterable, number=0):
      for x in iterable:
            print(number, x)
            number += 1


# def new_enumerate(iterable, index=0):
#       print(f'{index}:', iterable)
#       index += 1

list_1 = ['italy', 'spain', 'belgium']
courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']
list_2 = ['spain', 'panama', 'italy']

my_enumerate(list_2, 6)
my_enumerate_2(list_2, 6)

for index, course in enumerate(courses):
    print(index, course)
