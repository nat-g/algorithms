#!/usr/bin/env python


"""
The "dummy" nodes - trailer and header - are called sentinels

"""

class DoublyNode(object):

	def __init__(self, vaue):
		self.value = value
		self.nextnode = None
		self.prevnode = None


a = DoublyNode(1)
b = DoublyNode(2)
c = DoublyNode(3)

a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b


