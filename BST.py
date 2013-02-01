from __future__ import print_function

"""
A simple implementation of Binary Search Tree (BST)
   - Node object comparison methods are defined in Node class
"""
class BST:
    def __init__(self, root=None):
        """root is a Node object"""
        self.root = root

    def size(self): # count nodes
        """Returns the total number of nodes in a tree"""
        if not self.root: return 0
        else:
            return size(self.root.left) + 1 + size(self.root.right)

    def insert(self, value):
        """Insert value into this BST; modifies BST in place"""
        ## broken-- please fix
        
        def insert_helper(node, value):
            if node is None:
                self.root = Node(value)
            elif value <= self.root:
                insert_helper(node.left, value)
            else:
                insert_helper(node.right, value)

        insert_helper(self.root, value)    
        
    def find_min(self):
        """Returns the node with the smallest value in a BST"""        
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def find_min_rec(self):
        if self.root.left is None:
            return self
        return find_min_rec(self.left)

    def find_max(self):
        """Returns the node with the largest value in the BST""" 
        current = self
        while current.right is not None:
            current = current.right
        return current

    def find_max_rec(self):
        if self.right is None:
            return self
        return find_max_rec(self.right)

    # make it more elegant
    def lookup(self, value):
        """Returns True if value is in a given BST"""
        if self.value == value:
            return True
        if value <= self.left:
            return lookup(self.left)
        else:
            return lookup(self.right)
        return True

        #BFS is non-recursive
        #DFS is easier recursive
            
    def remove(self, node):
        pass

    def is_balanced(self, root):
        pass

    def balance(self):
        pass

    # make it more elegant
    def get_max_depth(self):
        if self == None:
            return 0
        return max(get_max_depth(self.left), get_max_depth(self.right)) + 1

    def print_inorder(self):
        """Print Node objects in their value order"""
        if self is None:     return
        print_inorder(self.left)
        print(self)     # prints Node object in repr format
        print_inorder(self.right)

    def traverse_inorder(self):
        """closure / generator"""
        def inorder_generator(self):
            """A recursive generator that generates Tree leaves inorder"""
            if self:
                for child in inorder(self.left):
                    yield child
                yield self.val
                for child in inorder(self.right):
                    yield child
        for data in inorder_generator(self):
            print(data)

    def print_preorder(self):
        """Prints the parents node first, its left children next, and its right children last"""
        if self is None:    return
        print(self)
        print_preorder(self.left)
        print_preoreder(self.right)

    def print_postorder(self):
        """Prints parent node after its descendants"""
        if self is None:    return 
        print_postorder(self.left)
        print_postorder(Self.right)
        print(self)

    def clear(self):
        self.val = None
        self.left = None
        self.right = None

    def is_empty(self):
        return self.is_empty()
"""
other potential methods: get_children / get_ancestors/ ..
    def __repr__(self):
        pass
    def __str__(self):
        pass
"""
