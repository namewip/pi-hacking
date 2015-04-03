from decimal import *
from math import *
from time import *
from threading import Thread
import compare
import os
n = 0
def calculate (it,prec,fb,rf):
	global n
	it += 1
	t = Thread(target=progression, args=(it,fb,rf,)) #itt lehet változtatni a 2-3. argumentumot
	t.start()
	getcontext().prec = int(prec)
	k1,k2,k3,k4,k5,k6 = 545140134,13591409,640320,100100025,327843840,53360		
	s = Decimal(0)
	for n in range(it):
		a = (-1)**n
		b = factorial(6*n)
		c = k2+n*k1
		d = factorial(n)**3
		e = factorial (3*n)
		f = (8*k4*k5)**n
		z = Decimal(a*b*c)/Decimal(d*e*f)
		s += Decimal(z)
	ans = Decimal(k6*Decimal(k3).sqrt())/s
	fajl = open("out.txt","w")
	fajl.write (str(ans))
	fajl.close()

def progression(osszes, felbontas=20, refresh=0.25):
	while True:
		prog = (n/(osszes-1)) # százalékot számít
		os.system('clear')
		print ("{:.2%}".format(prog),end=" ") #kiiírja a százalékot
		print (progressbar(n,osszes-1,felbontas)) #progressbar kiiratás
		if n == it: #ha kész van a művelet
			os.system('clear') 
			prog = (n/(osszes-1)) # újra kiszámít mindent és kiirat egy törlés után
			print ("{:.2%}".format(prog),end=" ") 
			print (progressbar(n,osszes-1,felbontas))
			print ("Pontosság:{} tizedesjegy".format(compare.test())) #megadja a pontosságot
			print ("A PI értéke sikeresen kiszámításra került, megtekinthető az out.txt fájlban")
			break
		sleep (refresh) 

def progressbar(pill,ossz,felbontas): #elkészíti a kis ábrát a progression barhoz
	ertek = round(pill/ossz,2)*100 #rész/egész*100 -> százalék érték -> 0<ertek<100
	x = int(round(ertek/(100/felbontas),0)) 
	string ="["+"█"*x+" "*(felbontas-x)+"]"
	return string 

def szamitas():
	saves=[]
	save = open("save.txt","r")
	for line in save:
		saves.append(float(line))
	it = int(saves[0])
	global it
	calculate(int(saves[0]),int(saves[1]),int(saves[2]),saves[3])

def settings():
	os.system("clear")
	print ("Beállítások:")
	it = int(input("Iterációk száma:"))
	prec = int(input("Precízió:"))
	fb = int(input("Ábra-Felbontás:"))
	rf = float(input("Ábra-Frissítés:"))
	setting = [it,prec,fb,rf]
	save = open("save.txt","w")
	for elem in setting:
		save.write(str(elem)+"\n")
	save.close()
	main()

def main():
	os.system('clear')
	print ("""Pi-calculator 1.1 by lmaresz
2015-04-03

0 - Pi számítás
1 - Beállítások

""")
	ans = input("Menüpont száma:")
	if ans == "0":
		szamitas()
	elif ans == "1":
		settings()

main()