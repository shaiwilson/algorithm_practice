# stack frame recursion

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

r = Stack()

def toStr(n, base)