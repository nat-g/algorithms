#!/usr/bin/env python

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

def reverse_linked_list(node):
	currentnode = node
	prevnode = None
	nextnode = None

	while currentnode != None:
		nextnode = currentnode.nextnode 
		currentnode.nextnode = prevnode
		prevnode = currentnode
		currentnode = nextnode

	return currentnode



