from decimal import *
from math import *
def calculate (it,prec):
	k1=545140134
	k2=13591409
	k3=640320
	k4=100100025
	k5=327843840
	k6=53360
	getcontext().prec = int(prec)
	s=Decimal(0)
	for n in range(int(it)):
		a = (-1)**n
		b = factorial(6*n)
		c = k2+n*k1
		d = factorial(n)**3
		e = factorial (3*n)
		f = (8*k4*k5)**n
		z = Decimal(a*b*c)/Decimal(d*e*f)
		s += Decimal(z)
	ans = Decimal(k6*Decimal(k3).sqrt())/s
	print (ans)

calculate(100,1000)