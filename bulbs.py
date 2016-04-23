

"""
N light bulbs are connected by a wire. 
Each bulb has a switch associated with it, however due to faulty wiring, 
a switch also changes the state of all the bulbs to the right of current bulb. 
Given an initial state of all bulbs, find the minimum number of switches you 
have to press to turn on all the bulbs. 
You can press the same switch multiple times. 

0 represents the bulb is off and 1 represents the bulb is on.

"""

# SOLUTION:
# if the bulb == 1 then move right
# otherwise switch it on 
# changing any switch the right of it will not effect it anymore


def bulbs(A):

    """Return the minumum number of switches to press to turn the light on


    >>> B = bulbs([0, 1, 0, 1])
    4

    """

    state = 0
    ans = 0

    for i in xrange(len(A)):
        if (A[i] == state):
            ans = ans + 1
            state = 1 - state

    print ans
    return ans

A = [0, 1, 0, 1]
B = bulbs(A)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
