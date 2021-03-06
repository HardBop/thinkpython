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
# Note author's method below [process_line()] using string.strip() is a
#   better solution because it only strips leading & trailing characters
#   but does not remove embedded like apostrophes.
def squishy(word) :
    word = word.lower()
    newword = ''
    for char in word :
        if char not in (string.punctuation+string.whitespace) :
            newword += char
    return newword

def better_squishy(word) :
    word = word.lower().strip(string.punctuation+string.whitespace)
    return word



# For fun, re-working with the translate() method
# seems that maketrans method not available in 2.7 ... waaah!
fin = open('/Users/jimbaer/python/sandbox/turtle/wordlines.txt')
badchar = (string.punctuation+string.whitespace)
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
            for word in line.replace('-',' ').split() :  # see note
                cleanword = squishy(word)
                if cleanword in words_dict :
                    words_dict[cleanword] += 1
                else :
                    words_dict[cleanword] = 1
    print book," has ",len(words_dict)," distinct words"
    return words_dict

# Note: replace().split() allows to split on "-" or " "

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

def hi_lo(revdict,heads=10,tails=0) :
    flist = []
    for cnt in revdict :
        flist.append((cnt,revdict[cnt]))
    sflist = sorted(flist, reverse=True)
    if heads > 0 :
        print 'Most Frequent Words: (count,word)'
        for item in sflist[:heads] :
            print item
    if tails > 0 :
        print sflist[-tails:]

""" Exercise 13.3: Modify the program from the previous exercise to print
    the 20 most frequently-used words in the book.
"""
# Already built the basic function in hi_lo() above
hi_lo(Douglass_revdict,20,0)

""" Exercise 13.4: Modify the previous program to read a word list
    (see Section 9.1) and then print all the words in the book that are
    not in the word list.
"""
# Read words.txt into a dict
def read_words() :
    fin = open('/Users/jimbaer/python/sandbox/text_files/words.txt')
    wordlist = dict()
    for line in fin :
        word = line.strip()
        if word not in wordlist :
            wordlist[word] = ''
        else :
            print "error - word repeated in source file"
            return
    return wordlist

wl_dict = read_words()

# write function to read words from book (Douglass_words dict) and see if they
#   are in wl_dict, putting any not in wl_dict into a missing_dict
def wordmatch(book_words) :
    missing_dict = dict()
    for word in book_words :
        if word not in wl_dict :
            missing_dict[word] = ''
    print len(missing_dict)
    return missing_dict

Douglass_miss_dict = wordmatch(Douglass_words)

def  dump_mismatch(miss_dict,N) :
    i = 0
    for word in miss_dict :
        if i < N :
            i += 1
            print i, word
        else :
            return


# Answer is: mostly mismatch due to contractions, proper names, numbers, and
#   ______ which are not in words.txt file

# Did another example with Tale of Two Cities - longer with more geniune
#   mismatches
"""  Exercise 13.5
    Write a function named choose_from_hist that takes a histogram as defined
    in Section 11.1 and returns a random value from the histogram, chosen with
    probability in proportion to frequency.
"""
# Function to return an item for sample list with probability of any item
#   corresponding to the observed frequency in the sample.

# helper fn for bootstrap() that creates histogram from an observed sample,
#   where sample is a list of discrete observations over a finite set of
#   objects.  (E.g, heads/tails, sides of a die, etc.)
def histogram(sample) :
    freq_dict = dict()
    for item in sample :
        if item in freq_dict :
            freq_dict[item] += 1
        else :
            freq_dict[item] = 1
    return freq_dict

# helper function for bootstrap() to get denomenator
def get_base(histin) :
    denom = 0
    for item in histin :
        denom += histin[item]
    return denom

# function to calculated observed frequency of items in a sample
def bootstrap(sample) :
    histin = histogram(sample)
    denom = get_base(histin)
    distn = dict()
    for item in histin :
        distn[item] = histin[item] / float(denom)
        print item, distn[item]
    return distn

# Now need to create the final funcion that makes a random draw with the
#   probability of an outcome corresponding to the observed frequencies'
#   in the distn dict.
def chooser(distn) :
    cumit = 0
    draw = random.random()
    for item in distn :
        cumit += distn[item]
        if draw <= cumit :
            return item

# chooser() solves problem 13.5 but went further to develop another
#   function gensample() that generates samples according to the
#   distribuiton in the observed histogram, for validation
# histogram(), getbase(), bootstrap(), and chooser() combine to make the
#   choose_from_hist() function requested

def gensample(distn,size) :
    newsample = []
    for i in range(size) :
        newsample.append(chooser(distn))
    return newsample


# Function to identify mismatches between two dicts and put the words
#   only found in one dict into a new dict with a flag indicating
#   which source dict it came from

def dict_comp(dict1,dict2) :
    diff_dict = dict()
    for word1 in dict1 :
        if word1 not in dict2 :
            diff_dict[word1] = '1'
    for word2 in dict2 :
        if word2 not in dict1 :
            diff_dict[word2] = '2'
    print len(diff_dict)
    return diff_dict

Douglass_diff = dict_comp(Douglass_words,Douglass_words2)
# Douglass words created with code above; Douglass_words2 with code below
#   creating "hist" with process_file()
# This dict_comp() function does the same as subtract() below but goes
#    both directions and labels source when there is a discrepency

""" Exercise 13.6
    Python provides a data structure called set that provides many
    common set operations. Wwrite a program that uses set subtraction to
    find words in the book that are not in the word list.
"""

def set_up(dict1,dict2,show=10) :
    set1 = set(dict1.keys())
    set2 = set(dict2.keys())
    diff_set = set1.symmetric_difference(set2)
    i = 0
    for word in diff_set :
        i += 1
        if i < show :
            print i, word
    return diff_set

"""  Exercise 13.7
Alternate approach to a random draw:
1. get cummulative count of words for _words dict
2. Use random package to get a random number and scale to the word count
3. Pick first word from the cummulative distn that passes scaled psuedo-random,
    which will require ordering the (key,value) pairs by value - reverse dict
This approach relies on the ordering of the dict being arbitrary - suspect
    that will further compromise the "ramdom"-ness
"""

# Takes dict with words as keys and frequencies as values and returns
#   dict with words as keys and cummulative word count as values
def cumm_dict(indict) :
    cumm_dict = dict()
    summer = 0
    for word in indict:
        summer += indict[word]
        cumm_dict[word] = summer
    print 'total words: ',max(cumm_dict.values()),'  distinct words:', len(cumm_dict)
    return cumm_dict


# Takes dict with words as keys and cummulative word count as values and
#   inverts to a dict with cummulative count as keys and words as values.
# Not general for dict inversion b/c it errors our rather than concatenation
#   a list in case where initial value would map to more than one key.
def invert_dict(indict) :
    inverted = dict()
    for key in indict :
        if indict[key] in inverted :
            print "Error: key already exists"
            return
        else :
            inverted[indict[key]] = key
    print len(inverted), " entries in new dict"
    return inverted


# Takes inverted cummulative word count dict and draws a (psuedo) random
#   word where the likelihood of draw is based on observed frequencies
def draw_word(indict) :
    cval = max(indict.keys()) * random.random()
    keylist = sorted(indict.keys())
    for item in keylist :
        if item >= cval :
            return indict[item]


if __name__ == '__main__' :
    Douglass_cumm = cumm_dict(Douglass_words2)
    Douglass_cumm_inv = invert_dict(Douglass_cumm)
    print draw_word(Douglass_cumm_inv)

"""  Exercise 13.8 Markhov analysis

1. Write a program to read a text from a file and perform Markov analysis.
    The result should be a dictionary that maps from prefixes to a collection
    of possible suffixes. The collection might be a list, tuple, or dictionary;
    it is up to you to make an appropriate choice. You can test your program
    with prefix length two, but you should write the program in a way that
    makes it easy to try other lengths

"""
# How to split text into prefixes and suffixes?  I.e., how many words in each?
#   First cut: set prefix length to 2 and suffix to 1
#   Need to read words in a sliding window of 2-word bundles to get prefixes
#   Could read words into a dict that takes word and then order, then
#       step through in order and create dict of 2-word tuples.  Have to
#       make the order the key and word the value b/c word not distinct

# read book into a dict with the order of the word as key and the word as
#   value.  Have to use order as key b/c the word itself won't be distinct.
def ordered_words(book,first=0,last=1000000) :
    fin = open('/Users/jimbaer/python/sandbox/text_files/'+book)
    lc = 0
    wc = 0
    ord_words = dict()
    for line in fin :
        lc += 1
        if (lc >= first and lc < last) :
            for word in line.replace('-',' ').split() :  # see note
                wc += 1
                cleanword = squishy(word)
                ord_words[wc] = cleanword
    return ord_words

halfb_owords = ordered_words('eric_the_half.txt')

# Create dict of ordered 2-word tuples as prefixes
def prefix_dict(indict) :
    pref_dict = dict()
    for item in indict :
        if item < len(indict) :
            pref_dict[item] = (indict[item],indict[item+1])
    print len(pref_dict), " prefixes in dict"
    return pref_dict

# Reverse the prefix dict to make searchable by tuples with frequency of
#   the prefix tuple appearing as values
def prefix_rev(prefix_dict) :
    prerev = dict()
    for item in prefix_dict :
        if prefix_dict[item] not in prerev :
            prerev[prefix_dict[item]] = 1
        else :
            prerev[prefix_dict[item]] += 1
    return prerev

halfb_prefreq = prefix_rev(halfb_prefix)

# dict with prefix tuple as key and suffix (list of stings) as value
# pre2suf() takes ordered prefix dict and appends suffix in values
#   e.g., halfb_prefix dict as input
def pre2suf(prefix) :
    pre2suf = dict()
    for item in prefix :
        if item < len(prefix) :
            suffix = prefix[item+1][1]
        else :
            suffix = ''
        if prefix[item] not in pre2suf :
            pre2suf[prefix[item]] = [suffix]
        else :
            pre2suf[prefix[item]].append(suffix)
    return pre2suf

halfb_pre2suf = pre2suf(halfb_prefix)

# Utility function to dump dict, default is top 10 lines
def dict_dump(indict, lines=10) :
    cnt = 0
    for item in indict :
        cnt += 1
        if cnt <= lines :
            print cnt, item, indict[item]
        else :
            return

# A simple Markhov test stream - uses 2-word prefix and single word suffix
#   with random choice of prefix, and suffix also if len(suffix) > 1.
# indict = dict with prefix keys and suffix values
# Arbitrarily kicks out after default 10 iterations through the dict, though
#   that parameter is adjustable
def Markhov1(indict,lins=10) :
    newstring = ''
    cnt = 0
    for item in indict :
        ranpre = random.choice(indict.keys())
        if len(indict[ranpre]) <= 1 :
            suffix = indict[ranpre][0]
        else :
            suffix = random.choice(indict[ranpre])
        newstring = newstring + ' ' + ranpre[0] + ' ' + ranpre[1] + ' ' + suffix
        cnt += 1
        if cnt >= lins :
            print newstring
            return
    return

"""  Exercise 13.9: Word rank
1. Calculate word frequencies from an input file
2. Plot log f v log r, where f is the frequency and r is the rankself.
"""
# book_words() function creates a dict of words with frequencies
#   so use that and then order the results and print N rows
#   Example below with text of Emma
emma_words = book_words('emma.txt',250,17072)

emma_revdict = getmax('emma_words')

# Write a function to create a new dict that has freq of word from x_words
#   as value and the freq rank of the word as key
def freq_rank(revdict) :
    flist = []
    for cnt in revdict :
        flist.append((cnt,revdict[cnt]))
    sflist = sorted(flist, reverse=True)
    # freq_rank = dict()
    rank = 0
    for item in sflist :
        rank += 1
        print rank,' , ' , item[0], ' , ', math.log(rank), ' , ', math.log(item[0])
# Above ignores multiple words that have same freq & rank, e.g., the
#   words with freq=1 and rank = last.
# need to expand out the words & freqs that are grouped together in revdict
# Chart I get is more concave than linear for both eric_the_half and emma
#   though away from the endpoints the linear approx should be good
# Below version writes to a csv
def freq_rank(revdict,csvname) :
    flist = []
    for cnt in revdict :
        flist.append((cnt,revdict[cnt]))
    sflist = sorted(flist, reverse=True)
    # freq_rank = dict()
    rank = 0
    fout = open('/Users/jimbaer/python/sandbox/text_files/'+csvname,'w')
    for item in sflist :
        rank += 1
        comma = ' , '
        wstring = str(rank) + comma + str(item[0]) + comma + str(math.log(rank)) + comma + str(math.log(item[0]))+'\n'
        fout.write(wstring)
    fout.close()
