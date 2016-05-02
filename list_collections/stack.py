import test 
# this stack implementation assumes that the end of the list
# will hold the top element of the stack. as the stack grows(push)
# new items will be added on the end of the list. pop operations
# will manipulate that same end

class Stack():
    # 0(1) append and pop
    # will perform in constant time no matter how many items
    # are on the stacks

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peak():
        return self.items[len(self.items)-1]

    def push(self, data):
        self.items.append(data)

    def size(self):
        return len(self.items)


    
def revstring(mystr):
    """ uses a stack to reverse characters in a string """

    m = Stack()
    for letter in mystr:
        m.push(letter)

    rever = ""
    while not m.isEmpty():
        rever = rever + m.pop()

    return rever

def parChecker(symbolString):
    """ implements the Stack class
    returns a boolean result as to whether
    the string of parentheses is balanced """

    s = Stack()
    balanced = True
    index = 0
    opens = '([{'
    close = ')]}'
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in opens:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                # todo
                if not opens.index(opens) == close.index(close):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False 

def divideBy2(num):
    """ converting decimal numbers to binary numbers """ 

    r = Stack() 

    while num > 0:
        result = num % 2  
        r.push(result)
        num = num // 2

    binString = "" 
    while not r.isEmpty():
        binString = binString + str(r.pop())

    return binString

def baseConverter(num, base):
    """ takes any decimal number and any base between 2 - 16
    as parameters """

    # help w bases above 9
    # stores the digits in their corresponding positions
    digits = "0123456789ABCDEF"

    # hexadecimal uses ten decimal digits
    # along with the first six alphabet characters for the 16 digits

    r = Stack()

    while num > 0:
        result = num % base
        r.push(result)
        num = num // base

    newString = ''
    while not r.isEmpty():
        # when a remainder is removed from the stack, 
        # it can be used to index 
        # into the digit string and the correct resulting 
        # digit can be appended to the answer.
        newString = newString + digits[r.pop()]

    return newString

print(baseConverter(25,8))
print(baseConverter(26,26))

print(parChecker('((()))'))
print(parChecker('(()'))

print(divideBy2(42))
# testEqual(revstring('apple'),'elppa')
# testEqual(revstring('x'),'x')
# testEqual(revstring('1234567890'),'0987654321')
