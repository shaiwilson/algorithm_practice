class Node(object):
    """Linked list node."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):
        """Represent data for this node and it's successors as a string.

        >>> l1 = Node(3)
        >>> l1.as_rev_string()
        '3'

        >>> l1 = Node(3, Node(2, Node(1)))
        >>> l1.as_rev_string()
        '123'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))

# recursive
def add_linked_lists(l1, l2):
    """Given two linked lists, treat them like numbers and add them together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    if l1 == None or l2 == None:
        return 

    first = l1
    second = l2
    count = first.data + second.data
    return Node(count, add_linked_lists(first.next, second.next))

# iterative
def add_linked_lists2(l1, l2):
    """Given two linked lists, treat them like numbers and add them together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    # new ll
    out_head = out_tail = None

    while l1 or l2:

         # If we're not done list 1, get digit, move to next. If done, use 0.

        if l1:
            digit1 = l1.data
            l1 = l1.next
        else:
            digit1 = 0

        # If we're not done list 2, get digit, move to next. If done, use 0.

        if l2:
            digit2 = l2.data
            l2 = l2.next
        else:
            digit2 = 0

        count = digit1 + digit2

        # connect ll
        if not out_head:
            out_head = out_tail = Node(count)
        else:
            out_tail.next = Node(count)
            out_tail = out_tail.next

    return out_head

# iterative + edge cases
def add_linked_lists2(l1, l2):
    """Given two linked lists, treat them like numbers and add them together.

    l1: the head node of a linked list in "reverse-digit" format
    l2: the head node of another "reverse-digit" format

    Returns: head node of linked list of sum in "reverse-digit" format.
    """

    # new ll
    out_head = out_tail = None

    while l1 or l2:

         # If we're not done list 1, get digit, move to next. If done, use 0.

        if l1:
            digit1 = l1.data
            l1 = l1.next
        else:
            digit1 = 0

        # If we're not done list 2, get digit, move to next. If done, use 0.

        if l2:
            digit2 = l2.data
            l2 = l2.next
        else:
            digit2 = 0

        count = digit1 + digit2
        carry_over, count = divmod(count, 10)

        # connect ll
        if not out_head:
            out_head = out_tail = Node(count)
        else:
            out_tail.next = Node(count)
            out_tail = out_tail.next

    if carry_over:
        out_tail.next = Node(carry_over)

    return out_head


l1 = Node(3, Node(2, Node(1)))
l2 = Node(6, Node(5, Node(5, Node(5))))
result = add_linked_lists(l1, l2)
result2 = add_linked_lists2(l1, l2)
print (result.as_rev_string())
print (result2.as_rev_string())
print(l1.as_rev_string())