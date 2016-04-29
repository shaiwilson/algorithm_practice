# node class
class Element: 
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            #last item at list
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element
        

    def delete_first(self):
        if self.head:
            delete_elem = self.head
            temp = delete_elem.next
            self.head = temp
            return delete_elem
        else:
            return None


class Stack:
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        pass

    def pop(self):
        pass
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value

