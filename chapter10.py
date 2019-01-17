# Chapter10.py

"""Exercise 10.1: Write a function called nested_sum that takes a nested list of 
integers and add up the elements from all of the nested lists."""
""" Easy if all elements are unnested lists of integers but harder the list is a 
    mix of lists and integers ... and probably harder still if characters are 
    permitted """

# This works over integer entries - have to add logic to cull out non-int
def onlynest_sum(listy) :
    agg = 0
    for item in listy :
        if isinstance(item,list) :
            agg += sum(item)
    return agg

# sum integer elements of a list:
def sum_ints(listy) :
    summer = 0
    for item in listy :
	    if isinstance(item,int) :
	        summer += item

# still need the general case that tests for sublists and sums only integers

"""Exercise 10.2: Use capitalize_all to write a function named capitalize_nested 
    that takes a nested list of strings and returns a new nested list with all 
    strings capitalized.""" 

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

# Includes tests to see if element is string or nested string then capitalizes.
# Note: does not check for multi-layer nesting, e.g., nested strings 
# being nested strings themselves.

def capitalize_nested(nstring) :
    newstring = []
    for s in nstring :
        if isinstance(s,str) :
            newstring.append(s.capitalize())
        elif isinstance(s,list) :
            newstring.append(capitalize_all(s))
        else :
            return "Error - non-string input"
    return newstring 

# copied from text in Chapter 10 SS 10.7:
def only_upper(t) :
    res = []
    for s in t :
        if s.isupper() :
            res.append(s)
    return res


""" Exercise 10.3. Write a function that takes a list of numbers and returns the 
    cumulative sum; that is, a new list where the ith element is the sum of the first 
    i + 1 elements from the original list. Forexample, the cumulative sum of [1, 2, 3] 
    is [1, 3, 6]. """

# presumes input is list of integers but added a check
def cummulist(int_list) :
    agg = 0 
    out_list = []
    for val in int_list :
        if isinstance(val,int) :
            agg += val
            out_list.append(agg)
        else :
            return "Error - non-integer element"
    return out_list

# Exercise 10.4 
def middle(int_list) :
    return int_list[1:-1]

# Exercise 10.5
def chop(list) :
    del list[0]
    del list[-1]
    return None

""" Exercise 10.6: Write a function called is_sorted that takes a list as a parameter 
    and returns True if the list is sorted in ascending order and False otherwise. You 
    can assume (as a precondition) that the elements of the list can be compared with 
    the relational operators <, >, etc. """ 

def is_sorted(in_list) : 
    return in_list == sorted(in_list)

""" Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to 
    spell the other.  Write a function called is_anagram that takes two strings and 
    returns True if they are anagrams. """

def is_anagram(string1,string2) :
    return sorted(string1) == sorted(string2)

"""Exercise 10.8: write a function that returns True for dups in a list without modifying 
    original list """

#Two of the many ways to skin this cat

def has_duplicates(in_list) :
    sortie = sorted(in_list)
    itemlag = ''
    for item in sortie :
        if item == itemlag :
            return True
        itemlag = item
    return False

def has_duplicates(in_list) :
    sortie = sorted(in_list)
    for i in range(1,len(sortie)) : 
        if sortie[i] == sortie[i-1] :
            return True
        return False

# Exercise 10.9 - write a dedup function
def de_dup(in_list) :
    sortie = sorted(in_list) 
    for i in range(1,len(sortie)) :
        if sortie[i] == sortie[i-1] :
            in_list.remove(sortie[i])
    return in_list

""" Exercise 10.10: Write a function that reads the file words.txt and builds a list with 
    one element per word. Write two versions of this function, one using the append method 
    and the other using the idiom t = t + [x]. Which one takes longer to run? Why? 
    Hint: use the time module to measure elapsed time. """


def append_list() :
    wordlist = []
    fin = open('turtle/words.txt')
    for line in fin :
        word = line.strip()
        wordlist.append(word)
    return len(wordlist)


def add_list() :
    wordlist = []
    fin = open('turtle/words.txt')
    for line in fin :
        word = line.strip()
        wordlist = wordlist + [word]
    return len(wordlist)

def run_append():
    start_time = time.time()
    t = append_list()
    elapsed_time = time.time() - start_time
    return t, elapsed_time

def run_add():
    start_time = time.time()
    t = add_list()
    elapsed_time = time.time() - start_time
    return t, elapsed_time

""" Exercise 10.11: bisect in search """

def get_wordlist() :
    wordlist = []
    fin = open('turtle/words.txt')
    for line in fin :
        word = line.strip()
        wordlist.append(word)
    return wordlist


def bisect(word) :
    biglist = get_wordlist() 
    while len(biglist) > 50 :
        if word == biglist[len(biglist)/2] :
            return biglist.index(word)
        elif word > biglist[len(biglist)/2] :
            biglist = biglist[len(biglist)/2:]
        else :
            biglist = biglist[:len(biglist)/2]
    if word in biglist :
        biglist = get_wordlist()
        return biglist.index(word)
    else :
        return None

# not used in 10.11, just a function to return the index
def idx_word(word) :
    biglist = get_wordlist() 
    return biglist.index(word)

""" Exercise 10.12. Two words are a “reverse pair” if each is the reverse of the other. 
    Write a program that finds all the reverse pairs in the word list. """

# works but slow - will try again
def rev_pairs() :
    pairlist = []
    biglist = get_wordlist() 
    for word in biglist :
        if bisect(word[::-1]) > 0 :
            pairlist.append([word,word[::-1]])
    return len(pairlist)

# think this may be faster
def flippers() :
    pairlist = []
    biglist = get_wordlist()
    for i in range(len(biglist)) :
        if bisect(biglist[i]) > 0 and bisect(biglist[i][::-1])>0 :
            pairlist.append([biglist[i],biglist[i][::-1]])
    return pairlist

def run_revpairs() :
    start_time = time.time() 
    t = rev_pairs()
    elapsed_time = time.time() - start_time
    return elapsed_time, t

def run_flippers() :
    start_time = time.time() 
    t = flippers()
    elapsed_time = time.time() - start_time
    return elapsed_time, len(t)


# sccaled back version for smaller, more managable list to debug with
# works fine

def rev_pair2(in_list) :
    pairlist = []
    for word in in_list :
        if word[0] <= word[-1] and word[::-1] in in_list :
            pairlist.append([word,word[::-1]])
    return pairlist

