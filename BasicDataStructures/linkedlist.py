#!/usr/bin/env python

class Node:
	def __init__(self,initdata,next=None):
		self.data = initdata
		self.next = next

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class LinkedList:
	def __init__(self,head=None):
		self.head = head
		self.count = 0

	def isEmpty(self):
		return self.head == None

	#Add to the head of the list
	def add(self, value):
		#assign value 
		newnode = Node(value,self.head)
		self.head = newnode
		self.count = self.count + 1

	def size(self):
 		return self.count

	def search(self,value):
		current = self.head
		found =False
		while current != None and not found:
			if current.getData() == value:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self,value):
		current = self.head
		previous = None
		found = False
		while not found: 
			if current.getData() == value:
				found = True
			else:
				previous = current
				current = current.getNext()
		if found == False:
			print "Couldn't find the node"
		else:
			if previous == None:
				self.head = current.getNext()
			else:
				previous.setNext(current.getNext())



mylist = LinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))








