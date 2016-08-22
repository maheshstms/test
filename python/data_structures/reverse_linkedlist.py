#!/usr/bin/env python

class Node(object):
    def __init__(self, a_data=None, a_nextNode=None):
        self.data = a_data
        self.nextNode = a_nextNode

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, a_nextNode):
        self.nextNode = a_nextNode

    def setData(self, a_data):
        self.data = a_data

head = Node()
nextN = head
for i in range(10):
    # Create new node
    newNode = Node(i)
    nextN.setNextNode(newNode)
    nextN = newNode


nextN = head.getNextNode()
for i in range(10):
    print str(nextN.getData()) + "\n"
    nextN = nextN.getNextNode()

def reverseList(old_head, new_element = None):
    node = Node(old_head.getData(), new_element)

#    if old_head.getData() is None:
#        return  new_element

    if old_head.getNextNode() is None:
        return  node

#    node.setData(old_head.getData())
#    node.setNextNode(new_element)

    return reverseList(old_head.getNextNode(), node)




#    if old_head.getData() is not None and old_head.getNextNode() is None:
#        return  new_element
#    node.old_head.getData(), new_element)
#    return reverseList(old_head.getNextNode(), node)

print "-----------------------------------------"
import pdb; pdb.set_trace()
new_head = reverseList(head.getNextNode(), None)
nextN = new_head
for i in range(10):
    print str(nextN.getData()) + "\n"
    nextN = nextN.getNextNode()

