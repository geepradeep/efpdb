#!/usr/bin/python
"""
USAGE: python script.py <fullpp.log> <fragmentedpp.log>

remember: first argval is reference and second is fragmented

Credits: Pradeep Gurunathan, Lyudmila V. Slipchenko, Purdue University.
"""
try:
    import sys
    import re
except ImportError:
    print "module load error!!!"

def stringprint(XYZFile):
	try:
		inputXYZ=open(XYZFile,'r')
	except IOError:
		sys.stderr.write('Failed to open the files')
		return 0
	a = []
	b = 0
	c = ''
	dict1 = {}
	for line in inputXYZ:
		kk = re.sub(' +',' ',line)
		jj = kk.split(' ')
		a.append(jj)
	if a[2][0] == '':
		b += 1
	for i in range(2,len(a)):
#		print a[i][b]
		if a[i][b] in dict1:
			dict1[a[i][b]] += 1
		else:
			dict1[a[i][b]] = 1
	for key,value in sorted(dict1.items()):
		c += key
		value = str(value)
		c += value
#	print c
#	print a
	inputXYZ.close()
	return c

def xyztogmsinp(XYZFile, randvar):
	g = open(XYZFile, 'r')
	lines = g.readlines()
	inpfilename = XYZFile+'.'+randvar+'.inp'
	f = open(inpfilename, 'w')
	cc = []
	for line in lines[2:]:
		line = re.sub('\t+',' ',line)
		line = re.sub(' +',' ',line)
		line = re.sub('C','C 6.0',line)
		line = re.sub('H','H 1.0',line)
		line = re.sub('N','N 7.0',line)
		line = re.sub('O','O 8.0',line)
		line = line.split(' ')
		cc.append(line)
	f.write(' $contrl units=angs local=ruednbrg runtyp=makefp \n')
	f.write('       mult=1 icharg=0  coord=cart icut=11\n')
	f.write('       maxit=180 $end\n')
	f.write(' $system timlim=99999 mwords=2500 $end\n')
	f.write(' $scf soscf=.f. dirscf=.t. diis=.t. CONV=1.0d-06\n')
	f.write('       $end\n')
	f.write(' $basis gbasis=n31 ngauss=6 ndfunc=1\n')
	f.write('    $end\n')
	f.write(' $DAMP IFTTYP(1)=3,2 IFTFIX(1)=1,1 thrsh=500.0 $end\n')
	f.write(' $MAKEFP  POL=.t. DISP=.f. CHTR=.f.  EXREP=.f. $end\n')
	f.write(' $data\n')
	f.write(' comment_field\n')
	f.write(' C1\n')
	for i in range(len(cc)):
		f.write(' ')
		f.write(cc[i][0])
		f.write(' ')
		f.write(cc[i][1])
		f.write(' ')
		f.write(cc[i][2])
		f.write(' ')
		f.write(cc[i][3])
		f.write(' ')
		f.write(cc[i][4])
	f.write(' $end\n')
	return 'Done'


def validatestring(string, databasefile):
	try:
		inputdb=open(databasefile,'r')
	except IOError:
		sys.stderr.write('Failed to open the files')
		return 0
	ddd = []
	for line in inputdb:
		kk = re.sub('\t+',' ',line)
		jj = kk.split(' ')
		ddd.append(jj)
	for i in range(len(ddd)):
		if ddd[i][1] == string:
			return True
	return False
	
def main(XYZFile):
	return 0

main(sys.argv[1])
