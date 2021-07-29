# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def square_number(number):
    return number**2

def cube_number(number):
    return square_number(number)**3

def divide_by_4(number):
    return cube_number(number) / 4

print(divide_by_4(2))