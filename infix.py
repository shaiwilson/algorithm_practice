""" postfix and prefix """

# prefix expression notation requires that all operands
# precede the two operands that they work on
# ex: A + B * C -> + A * B C

# postfix -> A B C * +

class Stack():
    # 0(1) append and pop
    # will perform in constant time no matter how many items
    # are on the stacks

    # insert(0) and pop(0) require 0(n)
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

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    # empty stack for keeping operators    
    opStack = Stack()

    #an empty list for output
    postfixList = []

    # convert input infux to list
    tokens = infixexpr.split()

    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"

    for token in tokens:
        # if the token is an operand append it to ourput
        if token in APLHA or DIGITS:
            postfixList.append(token)
        elif token == '('
            opStack.push(token)
        elif token == ')'
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

        else:
            while (not opStack.isEmpty()) and \
            (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
