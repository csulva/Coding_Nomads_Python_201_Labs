import statistics

# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

with open('words.txt', 'r') as file_in:
    words = file_in.read()
    new_list = list(words.split())
    y = min(new_list, key=len)
    print(y)
    z = max(new_list, key=len)
    print(z)
    print(len(new_list))