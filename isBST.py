import Node

def isBST(node):
    """returns True if a given node is a root node of a binary search tree"""
    if is_leaf(node):
        return True
    else:
        # Node class contains a __le__ method that compares the value of two Node objects
        if node.left && (node.left <= node):
            return False
        if node.right && (node <= node.right):
            return False 

    return isBST(node.left) && isBST(node.right)
