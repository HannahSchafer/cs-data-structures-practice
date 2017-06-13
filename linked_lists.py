"""Practice implementing linked lists in Python

Common Linked List methods to know:
1) print all items in list
2) find a node (True/False)
3) Find the index (Same as above with count)
4) append
5) remove
6) remove by index
7) length
8) insert at particlar index

Common Questions:
1) Reverse a Linked List
2) Remove nth item from the end of a linked list (try with tail and without tail)
3) Rotate Linked List clockwise by k 
"""
class Node(object):
    """Node class for a LinkedList"""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def print_all_LL_items(self):
        """print all items in a Linked List"""

        current = self.head

        while current is not None:
            print current.data
            current = current.next

    def find_node(self, data):
        """Does the list contain a certain value (T/F)?"""
        
        current = self.head

        while current:
            if current.data == self.data:
                return True
            current = current.next

        return False

    def find_node_by_idx(self, idx):
        """Find and return node at a certain idx."""

        count = 0
        current= self.head

        while current:
            if count == idx:
                return current
            count +=1
            current = current.next

        return 'index out of range'


    def append(self, data):
        """Append new node with new data to end of list."""

        new_node = Node(data)

        # if list is empty
        if not self.head:
            self.head = new_node

        if self.tail:
            self.tail.next = new_node

        self.tail = new_node

    def remove(self, data):
        """Remove node with this data."""

        # if removing head
        if self.head is not None and self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        # if removing anything else besides head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.tail = current
                return

            else:
                current = current.next



    def remove_by_index(self, idx):
        """Remove node in linked list by its index"""

        count = 0

        # if removing head
        if count == idx:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        while current.next is not None:
            if count == idx:
                current.next = current.next.next
            count += 1
            current = current.next

    def insert(self, idx, data):
        """Inserts a new node at a particular index"""

        new_node = Node(data)

        count = 0
        current = self.head

        if idx == count:
            new_node.next = self.head
            self.head = new_node
            return



    def length(self):
        """Count all items in the list and return number"""

        if not self.head:
            return 0

        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count


    def pop(self):
        """Remove the last thing from the list and return it"""

        # if empty list
        if not self.head:
            raise EmptyListError

        # if only one item in list
        if self.head == self.tail:
            to_return = self.head
            self.head = self.tail = None
            return to_return

        # if list is more than 1

        current = self.head
        while current.next is not None:
            if current.next.next is None:
                to_return = current.next
                self.tail = current
                current.next = None
                return to_return
            else:
                current = current.next


    def reverse(self):
        """Reverses linked list"""

        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.tail = self.head
        self.head = prev


    def rotate(self, k):
        """Rotates linked list clockwise by k amount of spaces"""

        if not self.head:
            return

        while k !=0:
            new_tail = self.head
            self.tail.next = new_tail
            self.tail = new_tail
            self.head = self.head.next
            new_tail.next = None
            k -= 1


    def rotate(self, k):

        if not self.head:
            return

        while k != 0:
            new_tail = self.head
            self.tail.next = new_tail
            self.tail = new_tail
            new_tail.next = None
            self.head = self.head.next
            k -= 1


    def reverse(self):
        """reverse a linked list"""

        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.tail = self.head
        self.head = prev


    def remove_node(self, data):


if __name__ == "__main__":

    luna = Node('luna')
    natasha = Node('natasha')
    samira = Node('samira')
    tihtina = Node('tihtina')
    hadiza = Node('hadiza')
    hannah = Node('hannah')

    luna.next = natasha
    natasha.next = samira
    samira.next = tihtina
    tihtina.next = hadiza
    hadiza.next = hannah

    ll = LinkedList()

    ll.head = luna
    ll.tail = hannah

    print "Connected to Linked List functions"











