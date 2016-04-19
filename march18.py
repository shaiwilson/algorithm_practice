# string manipulations

# use recursion to reverse a string
def reverse(word):
    if (word == ""):
        return word
    else:
        subProblem = word[1:]
        subSolution = reverse(subProblem)
        solution = subSolution + word[0]
        return solution


# anagram of a palindrome
def ana(word):
    mydict = {}
    for i in word:
        mydict[i] += 1

    times = 0
    for e in mydict.values():
        if times == 2:
            return False
        if e == 1:
            times += 1
    return True

# largest difference in a list
def diff(mylist):
    max_i = 0
    min_i = 0

    for i in range(1, len(mylist)):
        if mylist[i] > mylist[max_i]:
            max_i = i

        if mylist[i] < mylist[min_i]:
            min_i = i

    diff = mylist[max_i] - mylist[min_i]

    return diff


