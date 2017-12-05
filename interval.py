# -*- coding: utf-8 -*-
import math
import sys

if sys.argv[1] != "C1" and sys.argv[1] != "C2":
	print("Nenurodytas režimas (C1 arba C2).")
	sys.exit()
elif len(sys.argv) < 4:
	print("Trūksta argumentų.")
	print("Programos naudojimo pavyzdys:")
	print("interval.py [C1 arba C2] [koduojamo failo vardas] [užkoduoto failo vardas]")
	sys.exit()
elif len(sys.argv) > 4:
	print("Per daug argumentų.")
	print("Programos naudojimo pavyzdys:")
	print("interval.py [C1 arba C2] [koduojamo failo vardas] [užkoduoto failo vardas]")
	sys.exit()
elif sys.argv[1] == "C1": c2_rezimas = 0
elif sys.argv[1] == "C2": c2_rezimas = 1

debug = False
pranesimo_failas = sys.argv[2]
kodo_failas = sys.argv[3]

indices = []
S = []
for s in range(0, 256):
	S.append(format(s, "08b"))
	indices.append(s)
	
locations = dict(zip(S, indices))
current_location = 256
code = ""

with open(pranesimo_failas, "rb") as rf:
	if debug:
		if c2_rezimas: print("Rezimas: C2")
		else: print("Rezimas: C1")
		print()
	current = ""
	while True:
		c = rf.read(1)
		if not c:
			if debug: print("Failo pabaiga")
			break
			
		c = bin(ord(c))[2:].rjust(8, '0')
		last_location = locations[c]
		k = current_location - last_location - 1
		
		if debug:
			print("Gautas zodis: ", c)
			print("Dabartine vieta: ", current_location)
			print("Paskutine vieta: ", last_location)
			print("Atstumas: ", k) 
			
		if c2_rezimas:
			v = ""
			u = ""
			k_u = math.floor(math.log((k+1), 2))
			for z in range(0, math.floor(math.log((k_u+1), 2))):
				u += "0"
			u = u + "{0:b}".format(k_u+1)
			v += u + "{0:b}".format(k+1)
			if debug: print("v_k: ", v)
			code += v
		else:
			u = ""
			for z in range(0, math.floor(math.log((k+1), 2))):
				u += "0"
			u = u + "{0:b}".format(k+1)
			if debug: print("u_k: ", u)
			code += u
		locations[c] = current_location
		current_location += 1
		if debug: print()

while len(code)%8 != 0:
	code += "0"

kodas = [code[i:i+8] for i in range(0, len(code), 8)]
with open(kodo_failas, "wb") as wf:
	if c2_rezimas:
		n = int("11111111", 2)
	else:
		n = int("00000000", 2)
	data = bytes([n])
	wf.write(data)
	for kod in kodas:
		n = int(kod, 2)
		data = bytes([n])
		wf.write(data)