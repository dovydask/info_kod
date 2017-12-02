import math
import sys

if sys.argv[1] != "C1" and sys.argv[1] != "C2":
	print("Nenurodytas režimas (C1 arba C2).")
	sys.exit()
elif len(sys.argv) < 3:
	print("Trūksta argumentų.")
	print("Programos naudojimo pavyzdys:")
	print("interval.py [C1 arba C2] [failo vardas]")
	sys.exit()
elif len(sys.argv) > 3:
	print("Per daug argumentų.")
	print("Programos naudojimo pavyzdys:")
	print("interval.py [C1 arba C2] [failo vardas]")
	sys.exit()
elif sys.argv[1] == "C1": c2_rezimas = 0
elif sys.argv[1] == "C2": c2_rezimas = 1

debug = False
pranesimo_failas = sys.argv[2]

indices = []
S = []
for s in range(0, 256):
	S.append(format(s, "08b"))
	indices.append(s)
	
locations = dict(zip(S, indices))
current_location = 256
code = ""

with open(pranesimo_failas) as rf:
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
		current += c
		if len(current) == 8:
			last_location = locations[current]
			k = current_location - last_location - 1
	
			if debug:
				print("Gautas zodis: ", current)
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
			locations[current] = current_location
			current = ""
			current_location += 1
			if debug: print()

code = str(c2_rezimas) + code
while len(code)%8 != 0:
	code += "0"
sys.stdout.write(code)