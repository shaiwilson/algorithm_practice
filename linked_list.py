# print linked list backwards

class Node(self):
    def __init__(self, data=None, next=None):
        self.data
        self.next


def print_backwards(mylist):
    if mylist == None: return
    head = mylist
    tail = mylist.next
    print_backwards(tail)
    print head,

def print_list(mylist):
    if mylist == None: return
    while node:
        print node,
        node = node.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)