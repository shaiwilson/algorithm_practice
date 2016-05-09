""" write a function fib() that takes an integer n
and returns the nth fib number"""

# o(n2)
# each call to fib makes 2 more calls
# draw it out - forms a binary tree
# exponential time cost
# recurrence tree gets twice as big each time u add 1 to n
def fib(n):
    if n in [1, 0]:
        return n
    else:
        return fib(n-1) + fib(n-2)

# solution
# 0(n)
class Fibber(object):
    def __init__(self):
        self.memo = {}

    def fib(self, n):

        # edge case: negative index
        if n < 0:
            raise Exception("Index was negative")

        # base case: 0 or 1
        elif n in [0, 1]:
            return n

        # see if we've already calculated this
        if n in self.memo:
            return self.memo[n]

        result = self.fib(n - 1) + self.fib(n - 2)

        # memoize
        self.memo[n] = result

        return result

# 0(n)
def fib_iterative(n):

    # edge cases:
    if n < 0:
        raise Exception("Index was negative. No such thing as a negative index in a series.")

    elif n in [0, 1]:
        return n

    prev = 0
    prev_prev = 1

    for _ in xrange(n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current


    