#!/usr/bin/env python

sentence = "  What   is   Life  "
print " ".join(sentence.split()[::-1])
print " ".join(reversed(sentence.split()))