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

#Function version - squishy removes punctuation, whitespace, and makes
#   lower case
def squishy(word) :
    word = word.lower()
    newword = ''
    for char in word :
        if char not in (string.punctuation+string.whitespace) :
            newword += char
    return newword


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
"""
I downloaded The Narrative of the Life of Frederick Douglass
       An American Slave from the Gutenberg project.  Determined that
       the actual text starts on line 540 (after header, contents,
       and supporting letters) by a combination of inspection and
       grep -n "[first phrase of book]"
I did not see a clever way to skip over that front material so just gong to
    read starting in the text starting at line 540
Likewise, line 3733 is end of text - rest is added Gutenberg material so
    stopping read at line 3733.
    There are 4106 lines in the file (bash wc -l)
"""

# Input text of book and organize into a dict with freq count
# book = name fo text file, first/last = first/last line of text
def book_words(book,first,last) :
    fin = open('/Users/jimbaer/python/sandbox/text_files/' + book)
    lc = 0
    words_dict = dict()
    for line in fin :
        lc += 1
        if (lc >= first and lc < last) :
            for word in line.split() :
                cleanword = squishy(word)
                if cleanword in words_dict :
                    words_dict[cleanword] += 1
                else :
                    words_dict[cleanword] = 1
    print book," has ",len(words_dict)," distinct words"
    return words_dict

Douglass_words = book_words('Frederick_Douglass.txt',540,3733)

# Can now reverse dict and sort - output is count, list of words or word, count
#   in descending order?  Douglass book has 4777 words ...

# Function to find the highest frequency word in the book (dict)
def getmax(indict) :
    hifreq = 0
    revdict = dict()
    for word in indict :
        if indict[word] > hifreq :
            hifreq = indict[word]
        if indict[word] in revdict:
            revdict[indict[word]].append(word)
        else :
            revdict[indict[word]] = [word]
    print hifreq, revdict[hifreq]
    return revdict
# Returning revdict to explore more on word freqs for the book

Douglass_revdict = getmax(Douglass_words)

def hi_lo(revdict,heads,tails) :
    flist = []
    for cnt in revdict :
        flist.append((cnt,revdict[cnt]))
    sflist = sorted(flist, reverse=True)
    print sflist[:heads]
    print sflist[-tails:]

""" Exercise 13.3: Modify the program from the previous exercise to print
    the 20 most frequently-used words in the book.
"""
