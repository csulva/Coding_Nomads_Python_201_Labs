# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.
list_1 = [4, 6, 8, 12, 14, 5, 6, 7, 3, 5]
new_gen = (x**2 for x in list_1 if x < 10)
print(new_gen) #OUTPUT <generator object <genexpr> at 0x10e8fb890>

def list_it(generator):
    generator = list(generator)
    print(generator)

list_it(new_gen)
    


