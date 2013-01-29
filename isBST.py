from Node import Node

def isBST(node):
    """returns True if a given node is a root node of a binary search tree"""
    if node.is_leaf():
        return True
    else:
        # Node class contains a __le__ method that compares the value of two Node objects
        if node.left and not (node.left <= node):
            return False
        if node.right and not (node <= node.right):
            return False 

    return isBST(node.left) and isBST(node.right)
