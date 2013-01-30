"""
simple implementation of Binary Search Tree (BST)
    - left descendants of a parent node <= parent node 
    - right descendants of a parent node > parent node 
    - Node object comparison methods are defined in Node class
"""
class BST:
    def __init__(self, root=None):
        """root is a Node object"""
        self.root = root

    def insert(self, key):
        """Insert key into this BST; modifies BST in place"""
        if self.root is None:
            self.root = Node(key)

    #is there an advantage to using self.getLchild() instead of self.left?
        if key <= self.root:
            self.left.insert(key)
        else:
            self.right.insert(key)

    def find_min(self):
        """non-recursive implementation
           returns the node with the smallest key in a BST
        """ 
        # do I need a separate fcn for find_min_Node?
        current_node = self 
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def find_max(self):
        """non-recursive implementation
           returns the node with the largest key in the BST
        """ 
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    def find_node(self, value):
        """non-recursive implementation
           returns True if value is in a given BST"""
        if value <= self.left:
        
    def find_node_rec(self, value):
        pass

        #BFS is non-recursive
        #DFS is easier recursive
            
    def remove(self, node):
        pass

    def look_up(self, key):
        """
        recursive implementation
        returns True if key exists in the BST
        """
        if key == self.value:
            return True
        if key <= self.left:
            return look_up(key)
        else:
            return look_up(key)
        return False

    def get_max_depth(self):
        if self == None:
            return 0
        else:
            lDepth = get_max_depth()
    def print_inorder(self):
        pass
    def print_preorder(self):
        pass
    def print_postorder(self):
        pass
"""
other potential methods: get_children / get_ancestors/ ..
    def __repr__(self):
        pass
    def __str__(self):
        pass
"""
