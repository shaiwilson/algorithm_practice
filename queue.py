""" A general simulation of Hot Potato. 
This program will input a list of names and a constant, 
call its to be used for counting. It will return the name 
of the last person remaining after repetitive counting by num. """



Class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, items)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(nList, num):
    """ 
    Assume that the child holding the potato will be at the front of the queue.
    Upon passing the potato, the simulation will simply dequeue and then 
    immediately enqueue that child, putting her at the end of the line. 
    She will then wait until all the others have been at the front before 
    it will be her turn again. After num dequeue/enqueue operations, 
    the child at the front will be removed permanently and another 
    cycle will begin. 
    This process will continue until only one name remains. """

    q = Queue()
    for name in nList:
        q.enqueue(name)

    while q.size() > 1:
        for i in xrange(num):
            q.enqueue(q.dequeue())

            q.dequeue()

        return q.dequeue()


print(hotPotato(["s","t","drake","rih","nao","dvsn"],7))


