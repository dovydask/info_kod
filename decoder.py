def c2_decode(binary_string):
	zeros = 0
	start = 0
	for i in range(start, len(binary_string)):
		if binary_string[i] == "0":
			zeros += 1
		else:
			break
	print(zeros)
	bits_to_get = ""	
	bits_to_get = binary_string[zeros: (zeros*2)+1]
	print(bits_to_get)
	if bits_to_get == "":
		return values
		quit()
	to_dec = int(bits_to_get, 2)
	print(to_dec)
	to_decode = binary_string[(zeros*2)+1: zeros*2+1+to_dec]
	print (to_decode)
	decoded_dec = int(to_decode, 2)
	print(decoded_dec)
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
	print(zeros)
	bits_to_get = ""	
	bits_to_get = binary_string[zeros: (zeros*2)+1]
	print(bits_to_get) 
	if bits_to_get == "":
		return values
		quit()
	to_dec = int(bits_to_get, 2)
	print(to_dec)
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

print(locations)

uzkoduota = "kodas2"
dekoduota = "dekoduota"
values = []
with open(uzkoduota) as f:
	kodas = f.read()
	print(kodas)
	if kodas[0] == "0":
		new_uzkoduota = kodas[1:-1]
		print("c1")
		c1_decode(new_uzkoduota)
	if kodas[0] == "1":
		new_uzkoduota = kodas[1:-1]
		print(new_uzkoduota)
		print("c2")
		c2_decode(new_uzkoduota)

print(values)
#new_values = tuple(values)
#for k, val in enumerate(new_values):
#	print k, val
#atstumai = dict(zip(k, val))
#print atstumai

current_location = 256
for k in values:
	byte_index = current_location - k - 1
	byte = locations[byte_index]
	locations = {v: k for k, v in locations.items()}
	locations[byte] = current_location
	locations = {v: k for k, v in locations.items()}
	print(byte)
	current_location += 1
	

new_location = current_location - values[0] - 1
print(new_location)
#print values[0]

	
#c1_decode("000000010010100000000010100000000000010100000010000000010010001")
#c2_decode("00010100011101100000101011001011100000000")
#c1_decode("000101000011110000")
