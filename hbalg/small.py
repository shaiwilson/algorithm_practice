
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