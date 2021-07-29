# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.
import statistics
example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(*integers):
  # define the function here
  for x in integers:
    print(f'The maximum number is {max(x)}')
    print(f'The minimum number is {min(x)}')
    print(f'The average number is {sum(x) / len(example_list)}')
    print(f'The sum is {sum(x)}')

# call the function below here
stats(example_list)
