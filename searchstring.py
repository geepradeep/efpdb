#!/usr/bin/python
"""
USAGE: python script.py <fullpp.log> <fragmentedpp.log>

remember: first argval is reference and second is fragmented

Credits: Pradeep Gurunathan, Lyudmila V. Slipchenko, Purdue University.
"""
try:
	import sys, re
	from chemsimilarity import *
	import random
except ImportError:
    print "module load error!!!"
    
randvar = 0

def main(filename, dbname):
	b = stringprint(filename)
	c = validatestring(b, dbname)
	randvar = str(random.randint(0,1000000))
	if c == False:
		print xyztogmsinp(filename, randvar)
	filenam = re.sub('uploads/','',filename)
	e = 'dhcpa211.chem.purdue.edu/gamess/'+filenam+'.'+randvar+'.efp'
	d = re.sub(' ','',e)
	print 'Your EFP file will be available at',d,'after pressing the submit button below.'
	return
main(sys.argv[1], 'database.txt')
