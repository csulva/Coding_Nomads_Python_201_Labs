# Write a script where you complete the following tasks:

# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
def divisible_4_or_7(integer):
    if integer % 4 == 0 or integer % 7 == 0:
        return True
    else:
        return False

# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
def divisible_4_and_7(integer):
    if integer % 4 == 0 and integer % 7 == 0:
        return True
    else:
        return False

# - take in a number from the user between 1 and 1,000,000,000
user_input = input('Enter a number between 0 and 1,000,000,000: ')
user_input = int(user_input)

# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
x = divisible_4_or_7(user_input)
y = divisible_4_and_7(user_input)

# - print your the result variables with descriptive messages
if x == True:
    print(f'{user_input} is divisible by 4 or 7!')
else:
    print(f'{user_input} is not divisible by 4 or 7')

if y == True:
    print(f'{user_input} is divisible by 4 AND 7!')


