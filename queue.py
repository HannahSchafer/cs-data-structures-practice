
"""Implementing a queue in Python using a linked list and a Python list
Common queue methods
enqueue
dequeue
is_empty
length
empty
"""

class Node(object):
    """Node class for a Linked List"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue(object):
    """A queue using a linked list"""

    def __init__(self, inlist):
        self.length = len(inlist)
        self.tail = None

        prev = None
        for item in inlist[::-1]:
            node = Node(item, next = prev)
            if self.tail is None:
                self.tail = node
            self.head = prev

    def __repr__(self):
        if not self.head:
            return "<Empty Queue"

        else:
            return "<Queue head=%s tail=%s length=%s>" % 
            (self.head.data, self.tail.data, self.length)


    def enqueue(self, data):
        """Add item with this data to the end of the queue"""

        self.length += 1
        node = Node(data)

        if not self.tail:
            self.head = self.tail = node 
            return

        self.tail.next = node 
        self.tail = node
        return

    def dequeue(self):
        """remove and return node from beginning of queue"""

        if not self.head:
            return

        self.length -= 1

        item = self.head
        self.head.next = self.head
        if self.head is None:
            self.tail = None

        return item.data


    def length(self):
        """Returns length of queue."""

        return self.length


    def is_empty(self):



    def empty(self):
        """Empties entire queue"""









