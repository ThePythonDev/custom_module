#-*- coding:utf-8 *-
import os, sys, math
from math import sqrt as racine
from math import pi,cos,sin,tan,acos,asin,atan

def launch():
	os.system("cls")
	calcul = print('Enter calculation ("help" and "quit" available): ')
	main()

def main():
	calcul = input()
	if calcul == "help":
		os.system("cls")
		print("addition = +")
		print("subtraction = -")
		print("multiplication = *")
		print("division = /")
		print("square root = sqrt()")
		print("power = **")
		print("cosine = cos()")
		print("sine = sin()")
		print("tangent = tan()")
		print("cos-1 = acos()")
		print("sin-1 = asin()")
		print("tan-1 = atan()")
		print("pi")
		main()
	elif calcul == "quit":
		sys.exit(0)
	else:
		print(eval(calcul))
		print()
	main()