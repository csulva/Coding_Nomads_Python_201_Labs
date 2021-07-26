# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

with open('words.txt', 'r') as new_open:
    words = new_open.read()
    # words = words.split()
    reverse_word = words[::-1]
    print(reverse_word)


reverse_out = open('words_reverse.txt', 'w')
reverse_out.write(str(reverse_word))
reverse_out.write('\n')
reverse_out.close()