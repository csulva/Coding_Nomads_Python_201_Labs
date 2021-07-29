# Fix the code below to make it possible to print out
# the uppercase copy of the name.
# - use `return` to create an output for the function
# - assign the output to a variable
# - print that variable

def shout(name):
    name = str(name)
    loud_name = name.upper()
    return loud_name

print_name = shout("wilma")
print(print_name)
