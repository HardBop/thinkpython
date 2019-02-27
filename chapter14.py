"""  Exercises and Notes for Chapter 14 of Think Python """

""" Exercise 14.2 : Write a function called sed that takes as arguments a
    pattern string, a replacement string, and two filenames; it should read
    the first file and write the contents into the second file (creating it
    if necessary). If the pattern string appears anywhere in the file, it
    should be replaced with the replacement string.  If an error occurs while
    opening, reading, writing or closing files, your program should catch the
    exception, print an error message, and exit.
"""

def sed(patstr,repstr,infil,outfil) :
    try :
        lcnt = 0
        fin = open('/Users/jimbaer/python/sandbox/text_files/'+infil,'r')
        fout = open('/Users/jimbaer/python/sandbox/text_files/'+outfil,'w')
        for lin in fin :
            lcnt += 1
            fout.write(lin.replace(patstr,repstr))
        fin.close()
        fout.close()
        print lcnt, " lines written in new file"
    except:
        print "Error - something went wrong"
    return

sed('Carpenter','Glaser','walrus.txt','glaser.txt')

# Note: would be good to include informative error message,
#   passing any error received in execution
