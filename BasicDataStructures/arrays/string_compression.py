#!/usr/bin/env python

import collections

def compress(s):

	count = collections.defaultdict()
	output = ""
	dict1 = {}

	for char in s:
		dict1[count] += 1

	for key, val in dict1.iteritems():
		output = output + k + v

	return output

print compress('AAAAABBBBCCCC')