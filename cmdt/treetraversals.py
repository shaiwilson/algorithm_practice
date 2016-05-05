# tree traversals

class BinaryTree(object):

    def __init__(self, root):
        self.root = root
        self.left = None
        self.right  = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            newNode = BinaryTree(newNode)
            newNode.left = self.left
            self.left = newNode.left

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            newNode = BinaryTree(newNode)
            newNode.right = self.right
            self.right = newNode.right

    def getRootVal(self):
        return self.root

    def setRoot(self, root):
        self.root = root

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    # as a class method
    # def preorder(self):
    #     print(self.root)
    #     if self.left:
    #         self.left.preorder()
    #     if self.right:
    #         self.right.preorder()

# outside of the class
# recursive traversals

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# depth first traversal
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


# NOTES

# depth first search
# explore children nodes first


# breadth first search - visit all nodes at the same level
# before moving on to child nodes
# level order traversal - start at root 

# preorder
    # visit the root node first
    # recursively do a preorder traversal of the 
    # left subtree
    # followed by a recursive preorder traversal
    # of the right subtree
# postorder
    # recursively do a postorder traversal of the 
    # left subtree and the right subtree
    # followed by a visit to the root node
# inorder
    # inorder traversal recursively do an inorder
    # traversal of the left subtree
    # visit the root node
    # do a recursive traversal of the right subtree

