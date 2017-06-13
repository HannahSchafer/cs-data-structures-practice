class Stack(object):

    def __init__(self):
        self._list = []

    def push(self, item):
        """Add item to end of stack."""

        self._list.append(item)

    def pop(self):
        """Remve item from end of stack and return it."""

        if not self._list:
            raise StackEmptyError()

        return self._list.pop()

    def length(self):
        """Return length of stack"""

        return len(self._list)

    def empty(self):
        """Empty the stack"""

        self._list = []

    def is_empty(self):
        """check to see if stack is empty"""

        return not self._list