
# Section 9.2 Exercises

fin = open('turtle/tenitems.txt')
i = 0
for line in fin:
    word = line.strip() 
    if len(word) > 15 :
        i += 1

# Exercise 9.2
fin = open('turtle/words.txt')
i=0
j=0
for line in fin:
    word = line.strip()
    j += 1
    if 'e' not in word :
        i += 1

print float(i)/j * 100 # give % w/o and e

def has_no_e(word) :
    if 'e' not in word :
        return True
    else :
        return False

 # Exercise 9.3 - avoids funtion
 def avoids(word,xlist) :
     for char in xlist:
         if char in word :
             return False
     return True

def censor() :
    fin = open('turtle/words.txt')
    i=0
    j=0
    xlist = raw_input('list censored letters (e.g., abcd): ')
    for line in fin:
        word = line.strip()
        j += 1
        if avoids(word,xlist) :
            i += 1
    return i, j, float(i)/j * 100 # give % w/o and e

# Exercise 9.4
# function that checks if a word is made only of letters in list
def uses_only(word,string) :
    for char in word :
        if char not in string :
            return False
    return True

#Exercise 9.5
"""Write a function named uses_all that takes a word and a string 
of required letters,and that returns True if the word uses all the 
required letters at least once. How many words arethere that use all 
the vowels aeiou? How about aeiouy? """

def uses_all(word,string) :
    for char in string :
        if char not in word :
            return False
    return True

# how many words in words.txt use all vowels 'aeiou' and 'aeiouy'?

fin = open('turtle/words.txt')
i = 0
j = 0
for line in fin :
    word = line.strip()
    j +=1 
    if uses_all(word,'aeiouy') :
        i += 1

print i, j, i/j*100

# 'aeiou' --> count = 598
# 'aeiouy' --> count = 42

# Exercise 9.6
"""Write a function called is_abecedarian that returns True if the 
letters in a word appear in alphabetical order (double letters are ok). 
How many abecedarian words are there?"""
def is_abecedarian(word) :
    pchar = ''
    for char in word :
        if char < pchar :
            return False
        pchar = char
    return True


fin = open('turtle/words.txt')
i = 0
for line in fin :
    word = line.strip() 
    if is_abecedarian(word) :
        i += 1

print i

# answer 596

# Section 9.7 Exercises
# Exercise 9.7 - find word with 2 consecutive double letters
#
# A - find words with consecutive letters
fan = open('turtle/animals.txt')
for line in fan :
    word = line.strip()
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            print word

# counts words with double letters
fin = open('turtle/words.txt')
j = 0
for line in fin :
    word = line.strip()
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            j += 1

print j

# Count workds with 2 consectutive double letters
fin = open('turtle/words.txt')
c1 = c2 = c3 = 0
for line in fin :
    word = line.strip()
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            c1 += 1
            if i+3 <= len(word)-1 :  #check to see word long enough/index in range
                if word[i+2] == word[i+3] :
                    c2 += 1
                    if i+5 <= len(word)-1 : #check to see word long enough/index in range
                        if word[i+4] == word[i+5] :
                            c3 += 1
                            print word 

print c1, c2, c3
# Recall that for a word of length L the indices are [0.L-1]
""" This solution works but kind of brute force - 
    try doing with a recursive function that identifies doublet letters - have 
    to be careful to rule out non-consecutive cases like "misssissippi" 
    The brute force works b/c the indices are consecutive. """

def double(word) :
    i = j = 0
    lag = ''
    for char in word :
        j += 1
        if char == lag :
            i += 1
            print word
        lag = char

fan = open('turtle/animals.txt')
k = 0 
for line in fan :
    k += 1
    word = line.strip()
    double(word)

# version above works to print out words with double letters
#  recursive version below needs work
def rec_double(word) :
    i = j = 0
    lag = ''
    for char in word :
        j += 1
        if char == lag :
            i += 1
            print word
            double(word[j:])
        lag = char

def rec_doubles(word) :
    lag = ''
    i = j = 0
    for char in word :
        i += 1
        if char == lag :
            j += 1
            rec_doubles(word[i:])
        lag = char
    return j 
# j is the number of doubles in the word - not limited to consecutive

# program below calls rec_doubles to find count of words with 3 doubles
fin = open('turtle/words.txt')
k = 0
for line in fin :
    word = line.strip()
    j = rec_doubles(word)
    if j >2 :
        k += 1

print k

# Not sure I can improve on brute force for consecutive doubles ... moving on

#Excercise 9.8

# Create function to create leading 0s for odometer
def pad(i) :
    if len(str(i)) < 6 :
        j = (6-len(str(i))) * '0' + str(i)
    else :
        j = str(i)[-6:]
    return j

def odometer() :
    for i in range(1000000) :
        j = pad(i)
        if is_palindrome(j) :  #check for 6 digit palindrome at mile
            if is_palindrome(pad(i-1)[1:-1]) :  #check that middle 4 mile -1
                if is_palindrome(pad(i-2)[1:]) : #check last 5 mile -2
                    if is_palindrome(pad(i-3)[2:]) : #check last 4 mile -3
                        return j, pad(i-3)
# Answer: odometer was at 198,888 initially.

#Exercise 9.9
# Find max number of pairs of ages for parent & child where childs age is 
# inverse of the parents

def invert(string) :
    return string[::-1]

def invert2(string) :
    return ''.join(reversed(string))

# function that takes parent age at birth of child and checks for # of
# inverse pairs
def countem(p_age) :
    cnt = 0
    for c_age in range(99) :
        # print p_age, c_age, p_age - c_age
        if invert(str(p_age)) == str(c_age):
            cnt += 1
        p_age += 1
    return cnt

def countit() :
    for p_age in range(14,100) :
        cnt = countem(p_age)
        if cnt != 0 :
            print p_age, cnt


def countem_p(p_age) :
    cnt = 0
    for c_age in range(99) :
        print p_age, c_age, p_age - c_age, cnt
        if invert(str(p_age)) == str(c_age) :
            cnt += 1
        p_age += 1
    return cnt

# accounting for mother changing age during year and padding
def countem(p_age) :
    cnt = 0
    for c_age in range(99) :
        # print p_age, c_age, p_age - c_age
        if str(c_age).zfill(2) in (invert(str(p_age)),invert(str(p_age+1))) :
            cnt += 1
        p_age += 1
    return cnt

def countit() :
    for p_age in range(14,70) :
        cnt = countem(p_age)
        if cnt != 0 :
            print p_age, cnt


def countem_p(p_age) :
    cnt = 0
    for c_age in range(99) :
        if str(c_age).zfill(2) in (invert(str(p_age)),invert(str(p_age+1))) :
            cnt += 1
            print p_age, c_age, p_age+1, cnt
        p_age += 1
    return cnt


# Answer: Car Talk dude is 57






