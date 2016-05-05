""" 
you have a list of integers, and for each index you 
want to find the product of every integer except
the integer at that index 
"""

# takes a list of integers and returns a list of the products
def version1(int_list):

    products_of_all_ints_before_index = [None] * len(int_list)
    products_of_all_ints_after_index = [None] * len(int_list)

    # for each int find the product of all the integers
    product_so_far = 1

    for i in xrange(len(int_list)):
        print i, "i"
        products_of_all_ints_before_index[i] = product_so_far
        print products_of_all_ints_before_index
        product_so_far *= int_list[i]
        print product_so_far

    # walk thru the lst backwards
    j = len(int_list) - 1
    while j >= 0:
        products_of_all_ints_after_index[i] = product_so_far
        product_so_far *= int_list[i]
        i -= 1


  # input list
inputList = [3, 1, 2, 5, 6, 4]
version1(inputList)