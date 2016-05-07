
#The approach:
#   rank of word is position in the alphabetized list of permutations
#   first get word, alphabetize it.
#   must get number of repeated letters and divide total permutations by the number of repeats factorial
#   e.g. bookkeeper = 10!/2!/2!/3! = 151200 permutations because o and k are repeated twice, e thrice.
#
#   We then go through a binary search of the list, looking at each 0th index letter in the string as we
#   remove one letter from said index recursively and adjust the window of indices we're looking at.
#   return rank

import sys
import math

#get command line argument, becomes string we want to rank
#yourString = sys.argv[1]
word = 'caabbc'


#Get the total number of permutations for your word
def getPerms(word):

    total = math.factorial(len(word))
    perm_dict = {}
    for i in word:
        if i not in perm_dict:
            perm_dict[i] = 1
        else:
            perm_dict[i] += 1
            
    print 'perm_dict', perm_dict
            
    for i in sorted(perm_dict, reverse=True):
        if (perm_dict[i] > 1):
            total = total / math.factorial(perm_dict[i])
    
    return total

end = getPerms(word)

#gets the first instance of the passed letter in the string
def getFirstIndexOf(string, letter):
    for i in (range(0, len(string))):
        if string[i] == letter:
            return i

#gets the last instance of the passed letter in the string arg
def getLastIndexOf(string, letter):
    for i in reversed(range(len(string))):
        if string[i] == letter:
            return i

# Ranks string
# start is the last beginning position of our search
# end is the last ending of the chunk of our search
# We recursively cut down the word and search through the permutation space for its position!
def rankString(yourString, start, end):

    tempString = sorted(yourString)
    range = end - start
  
    if len(yourString) != 0:
        sections = range/len(tempString)
    if(len(tempString)<=0):
        return start 
    else:
        letter = yourString[0]
        #print("looking at letter " + letter)
        first = getFirstIndexOf(tempString, letter)
        last = getLastIndexOf(tempString, letter)
        newStart = start + sections*first
        newEnd = start + sections*(last+1)

        #remove first letter to go through the search
        yourString = yourString[1:]

        return rankString(yourString, newStart, newEnd)

print('The rank of your string, {0}, is... {1} '.format(word, rankString(word,0,end)))