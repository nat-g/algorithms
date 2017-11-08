#!/usr/bin/env python

import ctypes

class DynamicArray(object):
	def __init__(self):
		self.n = 0
		self.capacity = 1  #can accept only one element
		self.A = self.make_array(self.capacity)

	def __len__(self):
		return self.n

	def getitem(self,k):
		if not 0 < k < self.n:
			return IndexError("K is out of bounds!")
		
		return self.A[k]

	#add element to the end of the array; ele == new element
	def append(self,ele):
		if self.n == self.capacity:
			self._resize(2*self.capacity) #2x capacity

		self.A[self.n] = ele #since index starts with 0, that would be next index
		self.n += 1

	def _resize(self,new_cap):
		B = self.make_array(new_cap)  #utilizing ctypes library

		for k in range(self.n):
			B[k] = self.A[k]

		self.A = B
		self.capacity = new_cap

	def make_array(self, new_cap):
		return (new_cap * ctypes.py_object)()  #basically just take those raw bytes and doubles them



arr = DynamicArray()
arr.append(2)
len(arr)
arr.append(1)
len(arr)
print arr.getitem(1)
