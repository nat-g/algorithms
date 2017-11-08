#!/usr/bin/env python

class stack(object):
	def __init__(self):
		self.items = []
		self.size = 0

	def push(self,item):
		self.items.append(item)
		self.size += 1

	def pop(item):
		self.items.pop[len(self.items)-1]
		self.size -= 1

	def peek(self):
		return self.items[len(self.items)-1]

	def get_size(self):
#		return len(self.items)     
#We don't have to create a new var, could just use 
#build-in len to find length
		return self.size

	def isEmpty(self):
		return self.size == 0


s = stack()
s.push(2)
s.push(3)
s.push(4)
print s.peek()
print s.get_size()
print s.isEmpty()