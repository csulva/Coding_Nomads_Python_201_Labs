# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

new_list = []
x = input('Show me what you got: ')
list_2 = x.split()
for y in list_2:
    y = tuple(y)
    new_list.append(y)

    
print(new_list)
