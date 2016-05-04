# binary tree

class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        # a node with no existing left tree
        if self.left == None:
            self.left = BinaryTree(newNode)

        else:
            newNode = BinaryTree(newNode)
            newNode.left = self.left
            self.left = newNode

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            newNode = BinaryTree(newNode)
            newNode.right = self.right
            self.right = newNode

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())




