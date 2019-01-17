# Python code for ThinkPython Exercise 12.4 
# This should get pasted into the Chapter12.py file

# Exercise 12.1 : Write a function called sumall that takes any number of arguments
#    and returns their sum.
def sumall(*nums) :
    summer = 0
    for item in nums :
        summer += item
    return summer

""" Built in functions
    zip() combines two tuples creating a list of tuples with
    lengthe equal to the shortest tuple.
    d.items() returns a list of tuples with the contents of the dict
    dict() can be used to convert a list of tuples to a dict
    Combining dict with zip gives a convenient way to make a dictionary:
    d = dict(zip('abc',range(3)))"""

# sort by lenght function from 12.7 Comparing tuples
def sort_by_length(words) :
    t = []
    for word in words :
        t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t :
        res.append(word)
    return res

# modify to randomize order if words have same length (rather than the
#    words being in reverse alphabetic order due to sort method)

def sortof_by_length(words) :
    t = []
    for word in words :
        t.append((len(word), random.random(), word))
    t.sort(reverse=True)
    res = []
    for length, randy, word in t :
        res.append(word)
    return res

# Exercise 12.3: Write a function called most_frequent that takes a string
#    and prints the letters in decreasing order of frequency.
def let_freq(in_string) :
    chd = {}
    for char in in_string :
        if char in chd :
            chd[char] += 1
        else :
            chd[char] = 1
    chlist = chd.items()
    chsort = []
    for char, freq in chlist :
        chsort.append((freq,char))
    chsort.sort(reverse=True)
    for freq,char in chsort :
        print char, freq


# Excercise 12.4.1:  Write a program that reads a word list from a file 
#   (see Section 9.1) and prints all the sets of words that are anagrams.

""" 
Create index for all words by taking the words.txt file and sorting the 
    letters, then matching all the words that have that same "key", which 
    is the set of sorted letters.  
"""

# from Chapter 10 exercises
def anagram_dict() :
    anagrams = dict()
    fin = open('turtle/words.txt')
    for line in fin :
        word = line.strip()
        sword = ''.join(sorted(word)) # creates a string of sorted chars
        if sword not in anagrams :
            anagrams[sword] = [word]
        else :
            anagrams[sword].append(word)
    return anagrams

# put anagrams into a dict
anagrams = anagram_dict()

# Find entry with greatest len(anagrams[word]) 
def most_ans() :
    n_anograms = 0
    ano_cnt = dict()
    for item in anagrams :
        ano_cnt[item] = len(anagrams[item])
        if ano_cnt[item] > n_anograms :
            n_anograms = ano_cnt[item]
    print "Max # anograms: ", n_anograms
    return ano_cnt

ano_cnt = most_ans()

def findmaxano() :
    for item in ano_cnt :
        if ano_cnt[item] >= 11 :
            print item, ano_cnt[item], anagrams[item]

# Max anagrams: two strings have 11 anagrams: aeprs and aelrst
# All anagrams would result if printing all entries of annograms 
#    where len(ano_cnt[item]) > 1, which yields 10,157 cases of 
#    letter combinations in words.txt that can be formed into anagrams

# Exercise 10.4.2: 2. Modify the previous program so that it prints the 
#    largest set of anagrams first, followed by the second largest set, 
#    and so on.
# This is already available via anagrams and ano_cnt dicts

# Exercise 10.4.3: In Scrabble a “bingo” is when you play all seven tiles 
#    in your rack, along with a letter on the board, to form an eight-letter 
#    word. What set of 8 letters forms the most possible bingos?


def bingos() :
    max_bingo = 0
    for item in ano_cnt :
        if len(item) == 8 :
            if ano_cnt[item] > max_bingo :
                max_bingo = ano_cnt[item]
    for item in ano_cnt :
        if len(item) == 8 :
            if ano_cnt[item] == max_bingo :
                print item, ano_cnt[item], anagrams[item]



