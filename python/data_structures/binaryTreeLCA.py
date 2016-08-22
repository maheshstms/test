#!/usr/bin/env python

class Node(object):
    def __init__(self, a_data):
        self.data = a_data
        self.left = None
        self.right = None

def findLCA(a_head, a_x, a_y):
    if a_head is None:
        return None

    if a_head.data  == a_x or a_head.data == a_y:
        return a_head

    left_node = findLCA(a_head.left, a_x, a_y)
    right_node = findLCA(a_head.right, a_x, a_y)

    if left_node and right_node:
        return a_head

    import pdb; pdb.set_trace()
    return left_node if left_node is not None else right_node
    #return None
'''
               1
            2     3
           4 5   6 7


'''

root =  Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print "LCA(4,5) = ", findLCA(root, 4, 5).data
#import pdb; pdb.set_trace()
#print "LCA(4,6) = ", findLCA(root, 4, 6).data
#print "LCA(3,4) = ", findLCA(root, 3, 4).data
#print "LCA(2,4) = ", findLCA(root, 2, 4).data

