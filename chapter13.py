# Excercises and notes for Chapter 13 of ThinkPythong by Allen Downy on
#   Grean Tea Press
#
# change for testing branch logic

# name.strip() strips leading and trailing whitespaces out of a string

#Try removing whitespaces, punctuation, and capitalization in a loop
#     and returning the letters sorted
def squishsort(string_in) :
    string_out = ''
    string_low = string_in.lower()
    for char in string_low :
        if char not in string.whitespace :
            if char not in string.punctuation :
                string_out += char
    return ''.join(sorted(string_out))

# Exercise 13.1: Write a program that reads a file, breaks each line into
#    words, strips whitespace and punctuation from the words, and converts
#    them to lowercase.
