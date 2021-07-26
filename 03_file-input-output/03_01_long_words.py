# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

with open('words.txt', 'r') as file_in:
    words = file_in.read()
    list_of_words = list(words.split())
    for x in list_of_words:
        if len(x) > 20:
            print(x)