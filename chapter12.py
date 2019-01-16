# Exercises from Chapter 12 (Tuples) from ThinkPython by XXX, Greentea Press

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
