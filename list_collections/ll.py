"""
this implementation of a linked list adds the new node at the head
of the list. The new item is the first item of the list and the 
existing items are linked to this new first item so that they follow.

"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def addNode(self, newdata):
        newNode = Node(newdata)

        if self.head is None:
            self.head = newNode

        if self.tail is not None:
            self.tail.next = newNode

        self.tail = newNode

    # remove a node by value    
    def removeNode(self, value):

        if self.head and self.head.data == value:
            self.head = self.head.nex
            return

        current = self.head

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return 
            else:
                current = current.next

    def removeNodePrev(self, value):
        prev = None
        curr = self.head

        while curr is not None:

            if curr.data == value:
                if prev is None:
                    self.head = curr.bext
                else:
                    prev.next = curr.next
                return 

            else:
                prev = current
                current = current.next


