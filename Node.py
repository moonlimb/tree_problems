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
    
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        """returns True if value of self is less than or equal to that of other; both self and other are Node instances""" 
        return self.value <= other.value
    
    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value 

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __repr__(self):
        return "Node(%s)" %(self.value)

    def __str__(self):
        return str(self.value)

