import unittest
from Node import Node
# modify test functions to use unittest module

def test_Node_methods():
    nodes = [Node(num) for num in xrange(1,11)]
    n_str1 = Node('hello')
    n_str2 = Node('world')
    nodes[5].left = nodes[4]
    nodes[5].right = nodes[5]

    assert nodes[0] <= nodes[1] 
    assert nodes[5] <= nodes[-1] 
    assert n_str1 <= n_str2
    assert (nodes[3].is_leaf() and not nodes[5].is_leaf())
    assert n_str1.get_value() == 'hello'

def test_isBST():
    pass 

def run_tests():
    test_Node_methods()
    test_isBST()

if __name__ == "__main__":
    run_tests()
