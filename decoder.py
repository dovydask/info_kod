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
	print bits_to_get
	if bits_to_get == "":
		return values
		quit()
	to_dec = int(bits_to_get, 2)
	print(to_dec)
	to_decode = binary_string[(zeros*2)+1: (zeros*2+1)+to_dec]
	print to_decode
	decoded_dec = int(to_decode, 2)
	print decoded_dec
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


uzkoduota = "kodas3"
dekoduota = "dekoduota3"
values = []
with open(uzkoduota) as f:
	kodas1 = [line.rstrip('\n') for line in f]
        kodas = ''.join(kodas1)
	print(kodas)
	if kodas[0] == "0":
		new_uzkoduota = kodas[1:]
		print("c1")
		c1_decode(new_uzkoduota)
	if kodas[0] == "1":
		new_uzkoduota = kodas[1:]
		print(new_uzkoduota)
		print("c2")
		c2_decode(new_uzkoduota)

print values

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
	print byte
	print letter
	current_location += 1
#print word
#print all_bytes
print ''.join(word)
#print ''.join(all_bytes)

with open(dekoduota, 'w') as file:
    file.write(''.join(all_bytes))

	
	
#c1_decode("000000010010100000000010100000000000010100000010000000010010001")
#c2_decode("00010100011101100000101011001011100000000")
#c1_decode("000101000011110000")
