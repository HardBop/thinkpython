# Excercises and notes for Chapter 13 of ThinkPythong by Allen Downy on
#   Grean Tea Press
#
# change for testing branch logic

# name.strip() strips leading and trailing whitespaces out of a string

#Try removing whitespaces, punctuation, and capitalization in a loop
#     and returning the letters sorted

import string

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

""" Exercise 13.1
Write a program that reads a file, breaks each line into words, strips
    whitespace and punctuation from the words, and converts them to lowercase.
"""
# 1. read file
# 2. break lines into Words
# 3. mangle by removing whitespace & punctuation and converting to lowercase

# Created file wordlines.txt to test
fin = open('/Users/jimbaer/python/sandbox/turtle/wordlines.txt')
for line in fin :
    for word in line.split() :
        newword = ''
        for char in word :
            if char not in (string.punctuation+string.whitespace):
                newword += char
        print newword.lower()

# For fun, re-working with the translate() method
# seems that maketrans method not available in 2.7 ... waaah!
fin = open('/Users/jimbaer/python/sandbox/turtle/wordlines.txt')
badchar = string.punctuation+string.whitespace)
for line in fin :
    for word in line.split() :
        table = word.maketrans('','',badchar)
        newword = word.translate(table)
        print newword.lower()



"""Exercise 13.2
Fun with out of print books
"""
