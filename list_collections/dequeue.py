""" palindrome checker """


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def palchecker(phrase):
    """
    process the string from left to right and 
    add each character to the rear of the deque. 
    At this point, the deque will be acting very 
    much like an ordinary queue. """ 

    q = Deque()
    tokens = phrase.split()

    for token in tokens:
        q.addRear(token)

    isEqual = True

    while q.size() > 1:
        if q.removeFront() != q.removeRear():
            isEqual = False

    return isEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))

