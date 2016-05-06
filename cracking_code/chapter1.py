
# first ask the interviewer if the string is an
# ASCII string or a Unicode string. This function assumes
# that the character set is ASCII

# immediately return false if the string length exceeds
# the number of unique characters in the alphabet
# 0(n)


def isUnique(thestr):
    """ implement an algorithm to determine if a string has
    all unique characters """

    # 256 characters would be extended ascii
    if len(thestr) > 128:
        return False

    mydict = {}
    for letter in thestr:
        if letter not in mydict:
            mydict[letter] = 1
        else:
            mydict[letter] += 1
            return False
    return True


# details:
# is the permutation case sensitive
# ex: is God a permutation of dog?
# is whitespace significant?
# strings of different lengths cannont be permuations of eachother

def isPermutation(word, thestr):
    """ given two strings, decide if one is a permutation of the other"""
    
    if len(word) != len(thestr):
        return False

    return sorted(word) == sorted(thestr)

# using an algorithm
def isPermutation2(word, thestr):

    if len(word) != len(thestr):
        return False

    mydict = {}
    for letter in thestr:
        if letter not in mydict:
            mydict[letter] = 1
        else:
            mydict[letter] += 1

    for letter in word:
        if letter in mydict:
            mydict[letter] -= 1
            if mydict[letter] < 0:
                return False

    return True

    
def urlify(word):
    """ replace all spaces in a string with '%20'"""
    new_str = ''

    for letter in word:
        if letter == ' ':
            letter = '%20'
        new_str = new_str + letter 
    return new_str
              



  
print(urlify("hi j b"))
print(isUnique("abhjski"))
print(isUnique("abhjsski"))
print(isPermutation("abhjski", "abhjski"))
print(isPermutation2("aBbhjski", "abhjski"))
