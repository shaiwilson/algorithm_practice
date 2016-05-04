# parse tree
# hierarchy of the tree helps to prioritized order
# of operations

"""
How to build a parse tree from a fully parenthesized mathematical expression.
How to evaluate the expression stored in a parse tree.
How to recover the original mathematical expression from a parse tree.

"""

class Binarytree(object):

    def __init__(self, root):
        self.left = left
        self.right = right
        self.root = root

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = Binarytree(newNode)
        else:
            newNode = Binarytree(newNode)
            newNode.left = self.left
            self.left = newNode

    def insertRight(self, newNode):
        if self.right = None:
            self.right = Binarytree(newNode)
        else:
            newNode = Binarytree(newNode)
            newNode.right = self.right
            self.right = newNode

     def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self,root):
        self.root = root

    def getRootVal(self):
        return self.root

class Stack(object):

    def __init__(self):
        self.items = []

    def push(item):
        self.items.append(item)

    def pop():
        return self.items.pop()

    def peek():
        return self.items[-1]

    def isEmpty():
        return self.items == []




def buildParseTree(tokens):
    # break up the expression into a list of tokens
    token_list = tokens.split()
    pStack = Stack()
    parseTree = Binarytree('') # empty root
    pStack.push(parseTree)
    currTree = parseTree

    for i in token_list:
        if i == '(':
            currTree.insertLeft('')
            pStack.push(currTree)
            currTree = currTree.getLeftChild

        elif i not in ['+', '-', '*', '/', ')']:
            currTree.setRootVal(int(i))
            parent = pStack.pop()
            currTree = parent
        elif i in ['+', '-', '*', '/']:
            currTree.setRootVal(i)
            currTree.insertRight('')
            pStack.push(currTree)
            currTree = currTree.getRightChild()
        elif i == ')':
            currTree = pStack.pop()
        else:
            raise ValueError
    return parseTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")







