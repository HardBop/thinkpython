# reverse.py

def reverse(string) :
    index = 0 
    while index < len(string) :
        last = len(string) - 1
        backdex = last - index
        letter = string[last - index]
        print letter,
        index += 1


prefixes = 'JKLMNOPQ'
suffix = 'ack'
for char in prefixes :
    print char + suffix


for char in prefixes :
    if char not in ['O','Q'] :
        print char + suffix
    else :
        print char + 'u' + suffix


def find(word,letter) :
    index = 0
    while index < len(word) :
        if word[index] == letter :
            return index
        index += 1
    return -1


# word is a string, letter is a character, start is an integer
# added additional test to eliminate index out of range errors
def find2(word,letter,start) :
    if start >= len(word) :
        print "Error - start index out of range"
        return
    index = start
    while index < len(word) :
        if word[index] == letter :
            return index
        index += 1
    return -1


def count(word,letter) :
    count = 0
    for char in word :
        if char == letter :
            count += 1
    print count


def count2(word,letter,start) :
    count = 0
    index = start
    while index < len(word) :
        if word[index] == letter :
            count += 1
        index += 1
    print count

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
    	print 'i= ', i, 'j = ', j
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True

# Exercise 8.11

def any_lowercase1(s) :
    for c in s :
    	print c
        if c.islower() :
            return True
#        else :              removed last two lines to make it work
#        	return False


def any_lowercase2(s) :
    for c in s :
        if 'c'.islower() :
            return 'True'
        else :
        	return 'False'
# 1. always true b/c 'c' always lower case
# 2. will return string 'True' not a logical variable

def any_lowercase3(s) :
    for c in s :
        flag = c.islower()
    return flag
# will reset flag each time through so last letter will determine outcome

def any_lowercase4(s) :
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# not sure flag = flag or c.islower() is a valid statement
# seems (False or True) resolves to True so this won't work

def any_lowercase5(s) :
    for c in s :
        if not c.islower() :
            return False
    return True
# No good- any upper case letter will cause False

#ROT13 exercise
def rotate_word(word,n) :
    crypt = ''
    master = 'abcdefghijklmnopqrstuvwxyz'
    for c in word :
        j = find(master,c) + n
        if j < len(master) :
    	    crypt += master[j]
    	else :
    	    crypt += master[j-26]
    print crypt






