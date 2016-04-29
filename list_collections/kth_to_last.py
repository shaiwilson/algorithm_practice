""" Write a function kth_to_last_node() that takes an integer 
kk and the head_node of a singly linked list, 
and returns the kkth to last node in the list. """


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# O(n)
def kth_to_last_node(stop, start):
   #length of the linked list
   count = 1
   curr = start
   stopVal = length

   # iterate from the head to the tail and count the nodes
   while (curr.value != None):
       count += 1

   kth_to_last = count - stop

   curr = start
   for i in xrange(kth_to_last):
       curr = curr.next()


   return curr.value

# 0(n)
def kth_to_last_node2(stop, start):
   #length of the linked list
   left_node = start
   right_node = start

   # iterate from the head to the tail and count the nodes
   
   for i in xrange(stop-1):
      right_node = right_node.next()

   while right_node.next:
      left_node = left_node.next
      right_node = right_node.next


   return right_node

# 0(1) constant time

def kth_to_last_node3(stop, start):
   #length of the linked list
   curr = start
   count = 0

   # iterate from the head to the tail and count the nodes
   if left_node == None:
      return 
   else:
      length += legnth + 1 + kth_to_last_node3(curr.next)

   kth_to_last = length - stop

   curr = start
   if count == kth_to_last:
      return curr
   else:
      count += 1
      curr = curr.next

        
    
print(kth_to_last_node(2, a))
# returns the node with