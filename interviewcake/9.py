""" Write a function to check that a binary 
tree is a valid binary search tree """


class BinaryTree(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertLeft(self, value):

        if self.left == None:
            self.left = BinaryTree(value)
        else:
            newNode = BinaryTree(value)
            newNode.left = self.left
            self.left = newNode

    def insertRight(self, value):

        if self.right == None:
            self.right = BinaryTree(value)
        else:
            newNode = BinaryTree(value)
            newNode.right = self.right
            self.right = newNode

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, value):
        self.left = value

    def setRight(self, value):
        self.right = value

    def setRootVal(self,obj):
        self.value = obj

    def getRootVal(self):
        return self.value 

# check to see if a node is in a valid pos
# relative to ancestors
# node must be greater than any node in its
# right subtree and less than any node it the left
# subtree 


def check_binary_tree(root):
    """ a depth first walk through testing each node for validity 
    as you go """ 


    # start at the root, with an arbitrary lower bound

    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # depth first traversal
    while len(node_and_bounds_stack):

        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if (node.value < lower_bound) or (node.value > upper_bound):
            return False

        if node.left:

            # this node must be less than the curr node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))

        if node.right:

            # must be greater than the current node
            node_and_bounds_stack.append((node.right, node.value, node.value))

    return True

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getRight().setRootVal('hello')
print(check_binary_tree(r))





