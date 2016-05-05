""" 
    access yesterday's stock prices as a list, where:
    the indices are the time in minutes past trade opening time (9:30am)
    the values are the price in dollars of apple stock at that time.

"""
# version 1
# this doesn't work because you have to buy before you sell
def version1(stock_prices_yesterday):
    max_profit = 0

    for outer_time in xrange(len(stock_prices_yesterday)):

        for inner_time in xrange(len(outer_time)):

            earlier_time = min(outer_time, inner_time)
            later_time = max(outer_time, inner_time)

            # use those to find the earlier and later prices
            earlier_price = stock_prices_yesterday[earlier_time]
            later_price = stock_prices_yesterday[later_time]

            potential_profit = later_price - earlier_price

            # update max_profit 
            max_profit = max(max_profit, potential_profit)

    return max_profit

# version 2
def version2(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Too few')

    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    min_price = stock_prices_yesterday[0]

    for curr_price in stock_prices_yesterday:

        # check which min price is the lowest
        min_price = min(min_price, curr_price)

        # chec what our profit would be if we bought 
        # at the min price and sold at the current pric

        potential_profit = curr_price - min_price

        max_profit = max(max_profit, potential_profit)

    return max_profit

            
# version 3
# 0(n) time
# 0(1) space
def version3(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Too few')

    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    min_price = stock_prices_yesterday[0]

    for index, curr_price in enumerate(stock_prices_yesterday):

        if index == 0:
            continue

        # chec what our profit would be if we bought 
        # at the min price and sold at the current pric

        potential_profit = curr_price - min_price

        # update max
        max_profit = max(max_profit, potential_profit)

        # check which min price is the lowest
        min_price = min(min_price, curr_price)

        

    return max_profit



stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print(version3(stock_prices_yesterday))
# returns 6 (buying for $5 and selling for $11)