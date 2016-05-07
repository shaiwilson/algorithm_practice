"""You're given a list that contains the prices of a stock during one trading day, 
at 1 minute intervals. The list is chronologically ordered. You want to buy and 
sell the stock the same day, and maximize your profit. Write a method that takes 
the list and returns the time to buy and time to sell in order to maximize your 
profit."""

def stock_prices(stock_prices_yesterday):

    # init max profit to buying and selling the first opportunity
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    min_price = stock_prices_yesterday[0]

    if len(stock_prices_yesterday) < 2:
        raise IndexError('too few items in list')

    for index, curr_price in enumerate(stock_prices_yesterday):

        # u cannot buy & sell the first item
        if index == 0:
            continue

        potential_price = curr_price - min_price

        # update max profit
        max_profit = max(potential_price, max_profit)

        # update min price
        min_price = min(min_price, curr_price)

    return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print(stock_prices(stock_prices_yesterday))


"""Write a Python method that takes a string S, 
and returns a string containing the characters in S 
with duplicates removed. For example, if it gets 'ABA%%3', 
it should return 'AB%3'."""

# iterative
def isDup(word):

    new_str = ''
    uniq_letter = set()
    for letter in word:
        if letter not in uniq_letter:
            uniq_letter.add(letter)
            new_str = new_str + letter
    return new_str

# recursive
# deletes the first occurence of the letter
def isDup_rec(word):

    if len(word) == 0:
        return word

    if word[0] not in word[1:]:
        new_word = word[0] + isDup(word[1:])
    else:
        new_word = isDup(word[1:])

    return new_word



word = 'ABA%%3'
print(isDup_rec(word))
print(isDup(word))







