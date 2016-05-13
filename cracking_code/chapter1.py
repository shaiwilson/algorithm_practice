#! /usr/bin/env python
# Author: Shai Wilson 

# 0(n)

""" Simple, Pythonic solutions to question 1-1 """

import unittest

# solution using a set 
def isUniqueSet(thestr):

    unique_set = set()
    for char in thestr:
        if char in unique:
            retrun False

        unique_set.add(char)
    return True

def isUnique1(thestr):
    """ implement an algorithm to determine if a string has
    all unique characters """

    # immediately return false if the string length exceeds
    # the number of unique characters in the alphabet
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

# same solution without using additional data structures
def isUnique(thestr):

    if len(thestr) > 128:
        return False

    for letter in thestr:

        if thestr.count(letter) > 1:
            return False
        else:
            return True

class NoDuplicatesTest(unittest.TestCase):

    # Two-element tuples: input string and expected result

    TEST_DATA = [
        ('a', True),
        ('aa', False),
        ('ab', True),
        ('ab ', True),
        ('', True),
        (' ', True),
        ('  ', False),
        ('qwerty', True),
        ('qwerte', False)]

    def test_no_duplicates_both_versions(self):
        for str_, expected_result in self.TEST_DATA:
           
            result = isUnique(str_)
            self.assertEqual(result, expected_result)


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

# more robust implementation of isPermutation
def anagram(word, thestr):

    word = word.lower()
    thestr = thestr.lower()

    # sort, convert to str, and strio
    s1 = ''.join(sorted(word)).strip()
    s2 = ''.join(sorted(thestr)).strip()

    return s1 == s2

words = ( ('So dark the con          of man', 'Madonna of        The Rocks'),
              (' ba ', ' Ab   '),
              ('anne', 'annea') )

for w1, w2 in words:
        print('anagram({}, {}): {}'.format(w1, w2, anagram(w1, w2)))
        print('anagram({}, {}): {}'.format(w1, w2, anagram2(w1, w2)))


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

  
# problem aovid using + and += operators to accumulate a string within
# a loop. Since strings are immutable, this creates unncessary 
# temporary objects and results in quadratic rather than linear running time.
# Instead, add each substring to a list and ''.join the list after
# the loop terminates  
def urlify(word):
    """ replace all spaces in a string with '%20'"""
    new_str = ''

    for letter in word:
        if letter == ' ':
            letter = '%20'
        new_str = new_str + letter 
    return new_str

# better version
def urlify(word):
    """ using a list to store each char and change spaces
    to %20, then join list into a string """

    charList = []

    for char in word:
        if char == ' ':
            char = '%20'
        charList.append(char)
    return ''.join(charList)

# better implementation
def urlify(word):
    return '%20'.join(word.split())


def reverse_str(thestr):
    """ recursive solution to reversing a string """

    if thestr == '':
        return thestr

    subproblem = thestr[1:]
    subsolution = reverse_str(subproblem)
    solution = subsolution + thestr[0]
    return solution


if __name__ == "__main__":
    unittest.main()
