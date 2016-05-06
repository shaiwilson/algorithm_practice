""" 
write a function that, given:
1. an amount of money
2. a list of coin denominations
computes the number of ways to make amount of money
with coins of the available denominations.
"""

def change_top_down(amount_left, denominations_left):

    # base case
    if amount_left == 1:
        return 1

    # overshoot
    if amount_left < 0:
        return 0

    if len(denominations_left) == 0:
        return 0

    print "checking ways to make %i with %s" % (amount_left, denominations_left)

    current_coin, rest_of_coins = denominations_left[0], denominations_left[1:]

    # see how many possibilites there are
    # for each number of times to use current_coin

    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_top_down(amount_left, rest_of_coins)
        amount_left -= current_coin

    return num_possibilities

# version 2
class Change(object):

    def __init__(self):
        self.memo = {}

    def change_possibilities_top_down(self, amount_left, denominations_left):
        memo_key = str((amount_left, denominations_left))

        if memo_key in self.memo:
            print "grabbing memo[%s]" % memo_key
            return self.memo[memo_key]

        # base case
        if amount_left == 0: 
            return 1

        if amount_left < 0:
            return 0

        if len(denominations_left) == 0:
            return 0














