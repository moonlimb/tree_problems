import unittest
from Node import Node
# modify test functions to use unittest module


nodes = [Node(num) for num in xrange(1,11)]

def test_Node_methods():
    n_str1 = Node('hello')
    n_str2 = Node('world')
    nodes[5].left = nodes[4]
    nodes[5].right = nodes[5]

    assert nodes[0] <= nodes[1] 
    assert nodes[5] <= nodes[-1] 
    assert n_str1 <= n_str2
    assert (nodes[3].is_leaf() and not nodes[5].is_leaf())
    assert n_str1.get_value() == 'hello'

def build123():
    one_two_three = [Node(num) for num in xrange(1,4)]
    root = one_two_three[len(one_two_three/2]
    root.left = one_two_three[0]
    root.right = one_two_three[2]

    # make print123 fcn --> [1,2,3] == [1,2,3]

def test_isBST():
    """
    build BST using makeBST() then call isBST() to check whether it is indeed BST 
    non_BST = nodes[2]
    non_BST.left = nodes[9]  
    non_BST.right = nodes[0]

    assert isBST(makeBST(nodes)) == True
    assert isBST(build123) == True
    assert isBST(non_BST) == False 
    """
    pass 

def run_tests():
    test_Node_methods()
    test_isBST()

if __name__ == "__main__":
    run_tests()
