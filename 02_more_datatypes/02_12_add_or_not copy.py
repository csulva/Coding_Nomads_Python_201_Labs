# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input hasn't been added and deduce a point.
# If the user gets loses 5 points, quite the program.
# They wil if they manage to create a set that has more than 10 items.

new_set = set()
count = 5

while len(new_set) < 10:
    guess = input('Guess a number: ')
    guess = int(guess)
    if guess not in new_set:
        new_set.add(guess)
    else:
        print(f'You already guessed that! You lose one point. You have {count - 1} points left.')
        count -= 1
        if count == 0:
            print('Sorry, you lose!')
            break
    if guess == ValueError:
        print('Guess must be a number!')
    if len(new_set) == 10:
        print('Congrats, you win!')
    print(count)
    print(new_set)
