#readFiles.py

# this is for reading the mem images.

import cPickle as pickle
import io, pprint
# load files 
x1=pickle.load(open("uay.addr",'r'))
#x2=pickle.load(open("uay.objs",'r'))
x2=pickle.load(open("uay.allobjs",'r'))
x3=pickle.load(open("uay.segment_str",'r'))

#print x2

#f2 = open("uay.objs",'r')
#x2=pickle.load(open("uay.objs",'r'))
#pprint.pprint(x1)
#pprint.pprint(x2)
#pprint.pprint(x3)
#addrObj1 = x2.keys()[1]

# get length for keys of x1 x2 and x3
#x1length = len(x1.keys())
#x2length = len(x2.keys())
#x3length = len(x3.keys()) 
#print x1length # 8591566
#print x2length # 270
#print x3length # 386

# check if x2 is in x1 or x3
matchflag1 = 0
matchflag3 = 0
offset     = 0
#objectRes  = [1,1]
#objectStr  = []

# check match in x3
for i in range(len(x2.keys())):
	if x2.keys()[i] in x1:
		print x2.keys()[i]
		matchflag1 = 1
if matchflag1 == 0:
	print 'no match in x1'
for i in range(len(x2.keys())):
	if x2.keys()[i] in x3:
		print x2.keys()[i]
		matchflag3 = 1
if matchflag1 == 0:
	print 'no match in x3'


## binary object detection
# find address for object in x3 
objectMatchCnt = 0
objectMatchFlag =0
f1 = open('thread','a')
f2 = open('process','a')
for i in range(len(x2.keys())):
	for j in range(len(x3.keys())):
		if x2.keys()[i] > x3.keys()[j] and x2.keys()[i] < x3.keys()[j] + 4*len(x3[x3.keys()[j]]):
			objectMatchCnt = objectMatchCnt + 1 
			objectMatchFlag =1
			offset = (x2.keys()[i] - x3.keys()[j]) / 4
			n = x2[x2.keys()[i]][1]
			#with open('thread','r+') as f

			str2write = x3[x3.keys()[j]][offset:offset+n/4]
			if x2[x2.keys()[i]][0] == 'Thread':
				f1.write(str2write + '\n')
			else:
				f2.write(str2write + '\n')

			#objectRes = objectRes.append(offset)
			
			#if i == 1:
			#	print (x3[x3.keys()[j]][offset:offset+n/4], len(x3[x3.keys()[j]][offset:offset+n/4]))
			
			#print (i , j , x2.keys()[i], x3.keys()[j], offset, x2[x2.keys()[i]][1])
			#objectStr = objectStr.append( )
#print objectMatchCnt
#print offset
f1.close()
f2.close()
