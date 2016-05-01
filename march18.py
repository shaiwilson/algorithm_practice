# string manipulations

# calculate the greates common divisor of 
# two integers using the Euclidean algorithm

def euclid(m, n):
    if n == m:
        return n
    elif n < m:
        return euclid(n, m)
    elif m < n:
        if m == 0:
            return n
        else:
            return euclid(m, n%m)

print euclid(26,26)
print euclid(26,39)
print euclid(89,13)

# recursive function to check
# matching nested brackets

def brackets(x):
   if x == "":
     return "OK"
   elif len(x) == 1 and (x[0] == "(" or x[0] == ")"):
     return "Error"
   elif (x[0] == ")") or (x[len(x)-1] == "("):
     return "Error"
   elif x[0] != "(":
     return brackets(x[1:])
   elif x[len(x)-1] != ")":
     return brackets(x[0:len(x)-1])
   elif x[0] == "(" and x[len(x)-1] == ")":
     return brackets(x[1:len(x)-1])

print ")n" ,brackets(")n")
print ")n()" ,brackets(")n()")
print "(c(()b))" ,brackets("(c(()b))")
print "(())()" ,brackets("(())()")


# fibonnaci
def fib(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return (fib(x-1) + fib(x-2))

# use recursion to reverse a string
def reverse(word):
    if (word == ""):
        return word
    else:
        subProblem = word[1:]
        subSolution = reverse(subProblem)
        solution = subSolution + word[0]
        return solution

# use recursion for palindrome check
def isPal(s):
    isPalindrome = True
    if (len(s) == 0 or len(s) == 1):
        return isPalindrome
    elif s[0] != s[len(s)-1]:
        isPalindrome = False
    else:
        return isPal(s[1:len(word) -1])

print "radar:", isPal("radar")
print "abba:", isPal("abba")
print "top:", isPal("top")
print "Python:", isPal("Python")

# use recursion to sum a list
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

# use recursion to convert decimal to binary
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

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


