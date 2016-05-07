# facebook code lab 
# 4/23
# Shai Wilson


############ problem 1 ##################################################

def performOps(A):

    """Return the a copy of a 2D array in reverse column order

    >>> B = performOps([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    4 3 2 1 8 7 6 5 12 11 10 9

    """

    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    
    for i in xrange(len(B)):
        for j in xrange(len(B[i])):
            print B[i][j],

    return B


A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
B = performOps(A)


if __name__ == "__main__":
    import doctest
    doctest.testmod()