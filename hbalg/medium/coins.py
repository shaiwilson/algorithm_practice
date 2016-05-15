DIME = 10
PENNY = 1

def add_coins(left, total, results):

    if left == 0:
        results.add(total)
        return

    add_coins(left - 1, total + DIME, results)
    add_coins(left - 1, total + PENNY, results)


def coins(num_coins):
     """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    result = set()
    add_coins(left = num_coins, total = 0, results = results)

    return results