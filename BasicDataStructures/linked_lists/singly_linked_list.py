#!/usr/bin/env python


"""
Pros:
1) Linked lists have constant insertion and deletion time at any position 
n comparison arrays will always require linear (meaning O(n)) to do the 
same thing
2) Linked lists can also expand without specifying their size ahead of 
time (amortization reference)
Cons:
1)  Lookup time is O(K) where K is the Kth element. In contrast, arrays 
have constant time operations to access elements in the array.
"""

class SinglyNode(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None




a = SinglyNode(1)
b = SinglyNode(2)
c = SinglyNode(3)
a.nextnode = b
b.nextnode = c
