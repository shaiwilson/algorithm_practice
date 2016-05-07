def ana_of_pal(str):
    """ is the word an anagram of a palindrome? """

    seen = {}

    # count each letter

    for letter in word:
        cound = seen.get(letter, 0)
        seen[letter] = count + 1

    # it's a palindrome if the number of odd counts is 0 or 1
    seen_an_odd = False

    for count in seen.values():
        if count %2 != 0:
            if seen_an_odd:
                return False
            seen_an_odd = True
    return True


def dec2bin(num, base):
    """Convert a decimal number to binary representation."""
    convertString = "0123456789ABCDEF"

    if num < base:
        return convertString[n]
    else:
        return dec2bin(n // base, base) + convertString[n%base]

def add_to_zero(lst):
    """Return True if any two ints in a list add to zero else return False
        >>> add_to_zero([])
        False
        >>> add_to_zero([1])
        False
        >>> add_to_zero([1, 2, 3])
        False
        >>> add_to_zero([1, 2, 3, -2])
        True
    """

    if len(lst) == 0:
        return False
    for item in list_of_ints:
            if -item in list_of_ints:
                return True
    return False
        

if __name__ == "__main__":
    import doctest
    # add_to_zero([1, 2, 3])
    doctest.testmod(verbose=True)