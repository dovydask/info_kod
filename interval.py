import math
import sys

if len(sys.argv) < 3: 
	print("Nenurodytas rezimas (C1 arba C2) ir/arba failas")
	sys.exit()
elif len(sys.argv) > 3:
	print("Per daug argumentų!")
	sys.exit()
elif sys.argv[1] == "C1": c2_rezimas = False
elif sys.argv[1] == "C2": c2_rezimas = True

debug = False
pranesimo_failas = sys.argv[2]
#uzkoduoto_pranesimo_failas = "kodas"

indices = []
S = []
for s in range(0, 256):
	S.append(format(s, "08b"))
	indices.append(s)

locations = dict(zip(S, indices))
current_location = 256

with open(pranesimo_failas) as rf:
	#c2_rezimas = int(rf.read(1))
	if debug:
		if c2_rezimas: print("Rezimas: C2")
		else: print("Rezimas: C1")
		print()
	#with open(uzkoduoto_pranesimo_failas, 'w') as wf:
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
				#wf.write(v)
				sys.stdout.write(v)
			else:
				u = ""
				for z in range(0, math.floor(math.log((k+1), 2))):
					u += "0"
				u = u + "{0:b}".format(k+1)
				if debug: print("u_k: ", u)
				#wf.write(u)
				sys.stdout.write(u)
				locations[current] = current_location
			current = ""
			current_location += 1
			if debug: print()