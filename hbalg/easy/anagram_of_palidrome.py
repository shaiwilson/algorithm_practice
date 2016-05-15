

def isPal(thestr):
    """ is the word an anagram of a palindrome """

    seen = {}    
    # count all letters in the string
    for char in thestr:
        count = seen.get(char, 0)
        seen[char] = count + 1
    
    # it is a pal if the number of odd
    # counts is either 0 or 1

    seen_an_odd = False

    for count in seen.value():
        if count % 2 != 0:
            if seen_an_odd:
                return False
            seen_an_odd
    return True
