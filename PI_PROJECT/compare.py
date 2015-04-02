import re
def test ():
	reff = open("piref.txt","r")
	ref = reff.read()
	outf = open("out.txt","r")
	out = outf.read()
	a = 0
	for char in enumerate(out):
		if char[1]==ref[char[0]]:
			a = a+1
		else: 
			break
	print (a-2)
	reff.close()
	outf.close()

test()