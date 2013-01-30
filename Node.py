"""simple Node class for tree"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    #left is a Node object
        self.right = right  #right is a Node object

    def get_value(self):
        return self.value

    def is_leaf(self):
        return (not self.left and not self.right)
    
    def __le__(self, other):
        """returns True if value of self is less than or equal to that of other; both self and other are Node instances""" 
        if self.value <= other.value:
            return True
        else:   
            return False

    def set_Lchild(self, left_value):
        self.left = Node(left_value) 

    def set_Rchild(self, right_value):
        self.right = Node(right_value)

    def get_Lchild(self):
        return self.left

    def get_Rchild(self):
        return self.right

    def __repr__(self):
        return "Node(%s)" %(self.value)

    def __str__(self):
        return str(self.value)

