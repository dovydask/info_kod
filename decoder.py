# -*- coding: utf-8 -*-
import sys

if len(sys.argv) < 3:
	print("Trūksta argumentų.")
	print("Programos naudojimo pavyzdys:")
	print("decoder.py [užkoduoto failo vardas] [atkoduoto failo vardas]")
	sys.exit()
elif len(sys.argv) > 3:
	print("Per daug argumentų.")
	print("Programos naudojimo pavyzdys:")
	print("decoder.py [užkoduoto failo vardas] [atkoduoto failo vardas]")
	sys.exit()

def c2_decode(binary_string):
	while True:
		zeros = 0
		start = 0
		for i in range(start, len(binary_string)):
			if binary_string[i] == "0":
				zeros += 1
			else:
				break
		bits_to_get = ""	
		bits_to_get = binary_string[zeros: (zeros*2)+1]
		if bits_to_get == "":
			return values
			break
		to_dec = int(bits_to_get, 2)
		to_decode = binary_string[(zeros*2)+1: (zeros*2+1)+to_dec]
		decoded_dec = int(to_decode, 2)
		values.append(decoded_dec-1)
		binary_string = binary_string[zeros*2+1+to_dec:]

def c1_decode(binary_string):
	while True:
		zeros = 0
		start = 0
		for i in range(start, len(binary_string)):
			if binary_string[i] == "0":
				zeros += 1
			else:
				break
		bits_to_get = ""	
		bits_to_get = binary_string[zeros: (zeros*2)+1]
		if bits_to_get == "":
			return values
			break
		to_dec = int(bits_to_get, 2)
		values.append(to_dec-1)
		binary_string = binary_string[zeros*2+1:]



indices = []
S = []
for s in range(0, 256):
	S.append(format(s, "08b"))
	indices.append(s)

locations = dict(zip(indices, S))
current_location = 256

uzkoduota = sys.argv[1]
rezultatas = sys.argv[2]

values = []
c2_rezimas = False

with open(uzkoduota, "rb") as f:
	baitai = []
	mode = f.read(1)
	mode = bin(ord(mode))[2:].rjust(8, '0')
	if mode == "00000000":
		c2_rezimas = False
	elif mode == "11111111":
		c2_rezimas = True
	while True:
		b = f.read(1)
		if not b:
			break
		b = bin(ord(b))[2:].rjust(8, '0')
		baitai.append(b)
	
	kodas_str = ""
	for b in baitai:
		kodas_str += b
		
	if c2_rezimas:
		c2_decode(kodas_str)
	else:
		c1_decode(kodas_str)
		
current_location = 256
all_bytes = []
for k in values:
	byte_index = current_location - k - 1
	byte = locations[byte_index]
	locations = {v: k for k, v in locations.items()}
	locations[byte] = current_location
	locations = {v: k for k, v in locations.items()}
	all_bytes.append(byte)
	current_location += 1

allbytestr = ''.join(all_bytes)
allbytes = [allbytestr[i:i+8] for i in range(0, len(allbytestr), 8)]

with open(rezultatas, "wb") as wf:
	for byte in allbytes:
		n = int(byte, 2)
		data = bytes([n])
		wf.write(data)
