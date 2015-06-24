#!/usr/bin/python

import sys

def add(a,b):
	return a+b
	
age = add(30,int(sys.argv[1]))
print("Age : %d" %age)