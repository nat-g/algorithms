#!/usr/bin/env python

class deque(object):
	def __init__(self):
		self.items = []

	def ifEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def addFront(self,item):
		self.items.insert(0,item)

	def addRear(self,item):
		self.items.append(item)

	def removeFront(self):
		self.items.pop(0)

	def removeRear(self):
		self.items.pop()