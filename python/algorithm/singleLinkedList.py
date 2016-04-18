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
