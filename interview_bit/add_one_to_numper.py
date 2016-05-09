""" Given a non-negative number represented as an array of digits
add 1 to the number (increment the number represented by the digits)
the digits are stored such that the most significant digit is at the
head of the list """

def add_one(lst):
    i = len(lst) - 1
    carry = 1

    while (carry and i >= 0):
        n = lst[i]
        if n == 9:
            lst[i] = 0
        else:
            lst[i] = lst[i] + carry
            carry = 0
            break
        i = i - 1

    if carry == 1:
        lst.insert(0, 1)
        return lst
    else:
        i = 0
        while i < len(lst):
            if lst[i] > 0:
                break
            i += 1
        return lst[i:]       


lst1 = [ 0, 6, 0, 6, 4, 8, 8, 1 ]
lst = [ 9, 9, 9, 9, 9, 9 ]
print(add_one(lst1))



