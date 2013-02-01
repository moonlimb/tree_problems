"""simple Node class for tree"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left    #left is a Node object
        self.right = right  #right is a Node object

    def get_val(self):
        return self.val

    def is_leaf(self):
        return (not self.left and not self.right)
    
    def is_empty(self):
        return self.value == None  
    
    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        """returns True if val of self is less than or equal to that of other; both self and other are Node instances""" 
        return self.val <= other.val
    
    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val 

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __repr__(self):
        return "Node(%s)" %(self.val)

    def __str__(self):
        return str(self.val)

