""" FIFO que implemented as a linked list and circular array """

__author__ = "Shai Wilson"

class Node(object):
    """ Node in a queue """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

