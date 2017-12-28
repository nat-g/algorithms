#!/usr/bin/env python

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

# Solution 1
def findcycle(node):
	prevNode = None

	while node != None:
		prevNode = node
		node = node.nextnode

		if node.nextnode = prevNode:
			return True

	return False


#Solution 2
def check_cycle(self, node):
	marker1 = node
	marker2 = node

	while marker2 != None and marker2.nextnode != None:
		marker1 = marker1.nextnode
		marker2 = marker2.nextnode.nextnode

		if marker1 == marker2:
			return True

	return False