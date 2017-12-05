# -*- coding: utf-8 -*-
import sys
from bitstring import BitArray

def c2_decode(binary_string):
	zeros = 0
	start = 0
	for i in range(start, len(binary_string)):
		if binary_string[i] == "0":
			zeros += 1
		else:
			break
	#print(zeros)
	bits_to_get = ""	
	bits_to_get = binary_string[zeros: (zeros*2)+1]
	#print bits_to_get
	if bits_to_get == "":
		return values
		quit()
	to_dec = int(bits_to_get, 2)
	#print(to_dec)
	to_decode = binary_string[(zeros*2)+1: (zeros*2+1)+to_dec]
	#print to_decode
	decoded_dec = int(to_decode, 2)
	#print decoded_dec
	values.append(decoded_dec-1)
	new_string = binary_string[zeros*2+1+to_dec:]
	c2_decode(new_string)


def c1_decode(binary_string):
	zeros = 0
	start = 0
	for i in range(start, len(binary_string)):
		if binary_string[i] == "0":
			zeros += 1
		else:
			break
	#print(zeros)
	bits_to_get = ""	
	bits_to_get = binary_string[zeros: (zeros*2)+1]
	#print(bits_to_get) 
	if bits_to_get == "":
		return values
		quit()
	to_dec = int(bits_to_get, 2)
	#print(to_dec)
	values.append(to_dec-1)
	new_string = binary_string[zeros*2+1:]
	c1_decode(new_string)



indices = []
S = []
for s in range(0, 256):
	S.append(format(s, "08b"))
	indices.append(s)

locations = dict(zip(indices, S))
current_location = 256

uzkoduota = sys.argv[1]

values = []
with open(uzkoduota, "rb") as f:
	baitai = []
	while True:
		if not f.read(1):
			break
		baitai.append(f.read(1))
	
	kodas_str = ""
	for b in baitai:
	#print (kodas)
		kodas = ord(b)
		kodas = bin(kodas)[2:].rjust(8, '0')
	#for bit in kodas:
		kodas_str += kodas
	print (kodas_str)
	#kodas1 = [line.rstrip('\n') for line in f]
    #kodas = ''.join(kodas1)
	#if kodas[0] == "0":
	#	new_uzkoduota = kodas[1:]
	#	print("c1")
	#	c1_decode(new_uzkoduota)
	#if kodas[0] == "1":
	#	new_uzkoduota = kodas[1:]
	#	print("c2")
	#	c2_decode(new_uzkoduota)

print (values)

current_location = 256
word = []
all_bytes = []
for k in values:
	byte_index = current_location - k - 1
	byte = locations[byte_index]
	locations = {v: k for k, v in locations.items()}
	locations[byte] = current_location
	locations = {v: k for k, v in locations.items()}
	letter = chr(int(byte,base=2))
	word.append(letter)
	all_bytes.append(byte)
	#print byte
	#print letter
	current_location += 1
#print word
#print all_bytes
#print ''.join(word)
#print ''.join(all_bytes)

sys.stdout.write(''.join(word))
sys.stdout.write('\n')
sys.stdout.write(''.join(all_bytes))
sys.stdout.write('\n')

	
