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
    fin = open('words.txt')  # assumes words.txt in current directory
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

# Exercise 12.4.2: 2. Modify the previous program so that it prints the
#    largest set of anagrams first, followed by the second largest set,
#    and so on.
# This is already available via anagrams and ano_cnt dicts

# Exercise 12.4.3: In Scrabble a “bingo” is when you play all seven tiles
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


# Exercise 12.5  Two words form a “metathesis pair” if you can transform
#    one into the other by swapping two letters; for example, “converse”
#    and “conserve.” Write a program that finds all of the metathesis pairs
#    in the dictionary

""" matathesis pairs are a subset of anagrams - same letters but with a
    special restricted re-ordering.  Hence search the dict of anagrams
    for the metathesis pairs.
    The challenge is the possible combination of pairs for the richer
    anagrams - a letter sequence with 11 anagrams has C(11,n) possible
    pairings where n is the word length.

"""
# First - let's get a frequency count for anagrams that shows how many
#    letter combinations have n anagrams for each n.  (e.g., n = [1,11])

def ano_freq() :
    ano_freqs = dict()
    for item in ano_cnt :
        if ano_cnt[item] not in ano_freqs :
            ano_freqs[ano_cnt[item]] = 1
        else :
            ano_freqs[ano_cnt[item]] += 1
    return ano_freqs

def ano_freql() :
    ano_freql = list()
    for item in ano_freqs :
        ano_freql.append([item,ano_freqs[item]])
    return ano_freql

# To list the frequence from highest to lowest:

# Check count of combos at each frequency
import math
def ano_combo() :
    ano_combo = dict()
    for cnt in ano_freqs :
        if cnt > 1 :
            ano_combo[cnt] = math.factorial(cnt)/(2*math.factorial(cnt-2))
    return ano_combo

ano_combo = ano_combo()

for cnt in ano_combo :
    print cnt, ano_combo[cnt]

# Total pairs to check: number of letter combos with n annagrams times
#   combination of pairs from n annagrams
#   = sum over idx {ano_freqs[idx] * ano_combo[idx]}
def totcomps() :
    tots = 0
    for idx in ano_combo :
        tots = tots + ano_freqs[idx] * ano_combo[idx]
    print tots

# have to check 19,194 pairs that could be metathesis pairings

"""
Approach: compare the letters of each pair and increment a counter
for each time the letters are different.  IFF n=2 they are metathesis
pairs.
"""
from itertools import combinations

def letcomp(word1,word2) :
    diffex = 0
    for i in range(len(word1)) :
        if word1[i] != word2[i] :
            diffex += 1
    return diffex

def metathesis() :
    meta = list()
    for item in ano_cnt :
        if ano_cnt[item] > 1 :
            combos = combinations(anagrams[item],2)
    for tup in combos :
        diffex = letcomp(tup[0],tup[1])
    if diffex == 2 :
    meta.append(tup)
    return meta

# Holy Shizzle - it worked!!!
# Yields 3311 pairs of metathesis pairs from Words.txt

# Exercise 12.6: Word reduction by removing letters.  Seems tedious ... skipping for now.

"""
A couple other interesting tasks:
1. List the frequency of letters found in Word.txt.  (Function let_freq above
    does so for a string and freqs_ano
"""
# Create a dict with words of Words.txt and a blank for value
def makedict() :
    fin = open('turtle/words.txt')
    wlist_dict = dict()
    for line in fin :
        word = line.strip()
        wlist_dict[word] = ''
    print len(wlist_dict)
    return wlist_dict

wlist_dict = makedict()

# Histogram of letter frequency in Words.txt (via wlist_dict)
def letter_freq(in_dict) :
    freqs_dict = dict()
    for word in in_dict :
        for char in word :
            if char not in freqs_dict :
                freqs_dict[char] = 1
            else :
                freqs_dict[char] += 1
    return freqs_dict

freqs_dict = letter_freq(wlist_dict)

# histolet() reverses the freqs_dict and sorts decending to print
def histolet() :
    histodict = dict()
    for item in freqs_dict :
        histodict[freqs_dict[item]] = item
    for cnt in sorted(histodict,reverse=True) :
        print cnt, histodict[cnt]
