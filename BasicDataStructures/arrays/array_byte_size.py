#!/usr/bin/env python

import sys

# Amount of elements in the array - arbitrary number 
n = 10

data = []

for i in range(n):
	# Number of elements
	a = len(data)
	#Actual size in Bytes
	b = sys.getsizeof(data)

	print 'Length: {0:3d}; Size in Bytes: {1:4d}'.format(a,b)
	# Increase length by one
	data.append(n)