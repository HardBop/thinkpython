 
# Exercise 11.1: write a function that reads the words from words.txt in as keys 
#  in a dict

def makedict() :
    fin = open('turtle/words.txt')
    wlist_dict = dict()
    for line in fin :
        word = line.strip()
        wlist_dict[word] = ''
    print len(wlist_dict)
    return wlist_dict

# tinkering
def lettercount(word) :
    d = dict()
    for char in word :
        if char not in d :
            d[char] = 1
        else :
            d[char] += 1
    return d

#Exercise 11.2 use .get(,) for letter count function

def let_get(word) :
    word = word.lower() 
    d = dict()
    for char in word :
        d[char] = d.get(char,0) + 1
    return d

def print_hist(h) :
    for c in h :
        print c, h[c]

# print letter count in alphebetic order
def sprint_hist(h) :
    for c in sorted(h.keys()) :
        print c, h[c]

def reverse_lookup(d,v) :
    for k in d :
        if d[k] == v :
            return k
    raise ValueError('Value does not appear in the dictionary')

# Exercise 11.4 Modify reverse_lookup so that it builds and returns a list of all keys 
#   that tmap to v, or an empty list if there are none.

def lookback(d,v) :
    indy = []
    for k in d :
        if d[k] == v :
            indy.append(k)
    return indy

def invert_dict(d):
    inverse = dict()
    for key in d :
        val = d[key]
        if val not in inverse :
            inverse[val] = [key]
        else :
            inverse[val].append(key)
    return inverse

# Exercise 11.5. Read the documentation of the dictionary method setdefault and use it 
#    to write a more concise version of invert_dict

def invert_d2(d):
    inverse = dict()
    for key in d :
        val = d[key]
        inverse.setdefault(val,[]).append(key)
    return inverse

""" Note: In Python Dictionary, setdefault() method returns the value of a key 
    (if the key is in dictionary). If not, it inserts key with a value to the 
    dictionary. """

#Exercise 11.6: Fibonacci numbers with "memo" storage
known = {0:0,1:1}

def fibonacci(n) :
    if n in known :
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def fib1(n) :
    start_time = time.time()
    fibonacci(n)
    elapsed_time = time.time() - start_time
    print "Dict ", n, elapsed_time

# old fibonacci function
def fibold(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibold(n-1) + fibold(n-2)

def fib2(n) :
    start_time = time.time()
    fibold(n)
    elapsed_time = time.time() - start_time
    print "Old", n, elapsed_time

# Exercise 11.7: Ackermann function -- skipping b/c this seems tedious

# Exercise 11.8: RSA Public Key Encryption - way too hard

# Exercise 11.11: Find words that are homophonic if you remove either (but ont both)
#    of the first two letters:  just by inspection I get aardvark and llama.  

# My own excercise: count frequency of letters from words.txt
# have run makedict() function already so have wlist_dict to work with
def letter_freq(in_dict) :
    freqs_dict = dict()
    for word in in_dict :
        for char in word :
            if char not in freqs_dict :
                freqs_dict[char] = 1
            else :
                freqs_dict[char] += 1
    return freqs_dict
# code above stors the letter frequencies in a dict - now figure out how to sort

freqs_dict = letter_freq(wlist_dict)  #creates freq for each letter from wlist_dict
inver_freq = invert_dict(freqs_dict)  #inverts dict so can index by count
sinver_freq = sorted(inver_freq,reverse=True) #sorts
for val in sinver_freq :               # prints sorted freqs with letter label
    print val, inver_freq[val]

# Next self-assigned exercise: create a table with the count of words that contain 
#    each letter, sorted by freq.
import string
alphabet = list(string.ascii_lowercase)

""" word_by_let iterates through letters and counts up the words in words.txt that 
    contain them, creating a dict with {letter,count_of_words} """
def word_by_let(in_dict,alphabet) :
    word_freq = dict()
    for char in alphabet :
        for word in in_dict :
            if char in word :
                if char not in word_freq :
                    word_freq[char] = 1
                else :
                    word_freq[char] += 1
    return word_freq
# invert the dict to sort and index by counts
word_freq = word_by_let(wlist_dict,alphabet)
freq_word = invert_dict(word_freq)
sword = sorted(freq_word, reverse=True)
# print out the sorted list word counts for each letter in freq order
for freq in sword :
    print freq, freq_word[freq]

# Final Jeoparady: what letter occors the most times in any one word 
#	and what is the word?

