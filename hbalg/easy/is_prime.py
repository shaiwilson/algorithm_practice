
def is_prime(num):

    if num < 2:
        return False

    for n in xrange(2, num):
        if num % n == 0:
            return False

    return True

