# -*- coding: utf-8 -*-
import sys
import struct
import time
import numpy
#from bitarray import bitarray
start_time = time.time()

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
	
def c2_decode(input, output):
	indices = []
	S = []
	for s in range(0, 256):
		S.append(format(s, "08b"))
		indices.append(s)

	locations = dict(zip(indices, S))
	current_location = 256

	with open(input, "rb") as rf:
		rf.read(1)
		byte = rf.read(1)
		print (byte)
		binary_string = bin(ord(byte))[2:].rjust(8, '0')
		#a = bitarray(endian='big')
		#a.frombytes(byte)
		#print (a)
		with open(output, "wb") as wf:
			while True:
				zeros = 0
				start = 0
				#print(binary_string)
				i = 0
				to_break = False
				while True:
					if not "1" in binary_string:
						byte = rf.read(1)
						if not byte:
							to_break = True
							break
						#print("+", bin(ord(byte))[2:].rjust(8, '0'))
						binary_string += bin(ord(byte))[2:].rjust(8, '0')
					if binary_string[i] == "0":
						zeros += 1
						i += 1
					else:
						binary_string = binary_string[zeros:]
						#print (binary_string)
						break
						
				if to_break: 
					break
					
				while len(binary_string) <= (zeros + 1):
					byte = rf.read(1)
					if not byte:
						to_break = True
						break
					#print("+", bin(ord(byte))[2:].rjust(8, '0'))
					binary_string += bin(ord(byte))[2:].rjust(8, '0')
				
				if to_break:
					break
				
				#print(binary_string, zeros+1)
				bits_to_get = ""	
				bits_to_get = binary_string[:zeros+1]
				#print (bits_to_get)
				#print("btg:", bits_to_get)
				if bits_to_get == "":
					break
				to_dec = int(bits_to_get, 2)
				
				binary_string = binary_string[len(bits_to_get):]
				#print (binary_string)
				
				while len(binary_string) <= (to_dec):
					byte = rf.read(1)
					if not byte:
						to_break = True
						break
					#print("+", bin(ord(byte))[2:].rjust(8, '0'))
					binary_string += bin(ord(byte))[2:].rjust(8, '0')
				
				if to_break:
					break
				
				to_decode = binary_string[:to_dec]
				decoded_dec = int(to_decode, 2)
				binary_string = binary_string[to_dec:]
				
				k = decoded_dec
				byte_index = current_location - k
				byte = locations[byte_index]
				locations = {v: k for k, v in locations.items()}
				locations[byte] = current_location
				locations = {v: k for k, v in locations.items()}
				current_location += 1
				
				n = int(byte, 2)
				data = bytes([n])
				wf.write(data)
		

def c1_decode(input, output):
	indices = []
	S = []
	for s in range(0, 256):
		S.append(format(s, "08b"))
		indices.append(s)

	locations = dict(zip(indices, S))
	current_location = 256

	with open(input, "rb") as rf:
		rf.read(1)
		byte = rf.read(1)
		binary_string = bin(ord(byte))[2:].rjust(8, '0')
		#a = bitarray(endian='big')
		#a.frombytes(byte)
		#print (a)
		with open(output, "wb") as wf:
			while True:
				zeros = 0
				start = 0
				#print(binary_string)
				i = 0
				to_break = False
				while True:
					if not "1" in binary_string:
						byte = rf.read(1)
						if not byte:
							to_break = True
							break
						#print("+", bin(ord(byte))[2:].rjust(8, '0'))
						binary_string += bin(ord(byte))[2:].rjust(8, '0')
					if binary_string[i] == "0":
						zeros += 1
						i += 1
					else:
						binary_string = binary_string[zeros:]
						break
						
				if to_break: 
					break
					
				while len(binary_string) <= (zeros + 1):
					byte = rf.read(1)
					if not byte:
						to_break = True
						break
					#print("+", bin(ord(byte))[2:].rjust(8, '0'))
					binary_string += bin(ord(byte))[2:].rjust(8, '0')
				
				if to_break:
					break
				
				#print(binary_string, zeros+1)
				bits_to_get = ""	
				bits_to_get = binary_string[:zeros+1]
				#print("btg:", bits_to_get)
				if bits_to_get == "":
					break
				to_dec = int(bits_to_get, 2)

				binary_string = binary_string[zeros+1:]
				
				k = to_dec
				byte_index = current_location - k
				byte = locations[byte_index]
				locations = {v: k for k, v in locations.items()}
				locations[byte] = current_location
				locations = {v: k for k, v in locations.items()}
				current_location += 1
				
				n = int(byte, 2)
				data = bytes([n])
				wf.write(data)
				
				
uzkoduota = sys.argv[1]
rezultatas = sys.argv[2]
c2_rezimas = False


with open(uzkoduota, "rb") as f:
	baitai = []
	
	mode = f.read(1)
	mode = bin(ord(mode))[2:].rjust(8, '0')
	if mode == "00000000":
		c2_rezimas = False
	elif mode == "11111111":
		c2_rezimas = True

	if c2_rezimas:
		#print ("aaaa")
		c2_decode(uzkoduota, rezultatas)
	else:
		c1_decode(uzkoduota, rezultatas)


print(time.time() - start_time, " seconds.")
