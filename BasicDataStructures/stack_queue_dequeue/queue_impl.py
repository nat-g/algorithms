#!/usr/bin/env python

class Queue(object):
	def __init__(self):
		self.items = []

	def size(self):
		return len(self.items)

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self,item):
		self.items.pop(item)

	def isEmpty(self):
		return self.items == []


q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print q.isEmpty()
print q.size()