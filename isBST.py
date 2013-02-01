from Node import Node

def is_BST(node):
    """returns True if a given node is a root node of a binary search tree"""
    if node.is_leaf():
        return True
    else:
        # Node class contains comparison methods
        if (node.left and node.left >= node) or (node.right and node >= node.right):
            return False 

    return isBST(node.left) and isBST(node.right)
