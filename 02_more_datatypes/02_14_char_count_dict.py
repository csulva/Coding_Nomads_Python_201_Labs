# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}
new_dict = {}
new_input = input('Type something here: ')

for x in new_input:
    new_dict[x] = new_input.count(x)


print(new_dict)