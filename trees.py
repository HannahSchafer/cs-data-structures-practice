
"""Trees, BinaryTrees, and Binary Search"""

class Node(object):
    """Node class for a regular tree."""

    def __init__(self, data, children=None):
        self.data = data
        self.children = children


class Node(object):
    """Node class for a BST."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    """Tree class."""

    def __init__(self, root):
        self.root = root


    def bfs_find(self, data):
        """BFS. Finds a node in the tree. Returns None if node isn't found"""

        to_visit = [self]

        while to_visit:

            current = to_visit.pop(0) # Ideally this would be a queue

            if current.data == data:
                return current
            else:
                to_visit.extend(current.children)

        return None


    def dfs_find(self, data):
        """DFS. Finds a node in the tree. Returns None if node isn't found"""

        to_visit = [self]

        while to_visit:

            current = to_visit.pop() # Ideally this would be a stack

            if current.data == data:
                return current
            else:
                to_visit.extend(current.children)

        return


    def print_children_r(node, depth=0):
        """Prints a node and all of its children, recursively"""

        print " " * depth + node.data

        for child in node.children:
            print_children_r(child, depth + 1)

            












