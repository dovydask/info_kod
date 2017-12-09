import sys
import struct

def decompress(input, output):
	frozen = False
	with open(input, "rb") as rf:
		with open(output, "wb") as wf:
			dict_size = 256
			dictionary = {i: format(i, "08b") for i in range(dict_size)}
			
			dict_limit = 2**ord(rf.read(1))
			dict_freeze = ord(rf.read(1))
			
			print("Spaudimo parametrai: ")
			print("Maksimalus žodyno dydis: ", dict_limit)
			if dict_freeze: print("Pasiekus ribą, žodynas šaldomas")
			else: print("Pasiekus ribą, žodynas trinamas")
			
			c1 = bin(ord(rf.read(1)))[2:].rjust(8, '0')
			c2 = bin(ord(rf.read(1)))[2:].rjust(8, '0')
			w = c1 + c2
			n = int(w, 2)
			wf.write(bytes([int(dictionary[n], 2)]))
			while True:
				if dict_size == dict_limit and dict_freeze:
					frozen = True
				elif dict_size == dict_limit and not dict_freeze:
					dict_size = 256
					dictionary = {}
					dictionary = {format(i, "08b"): i for i in range(dict_size)}
				
				k1 = rf.read(1)
				k2 = rf.read(1)
				if not k1 or not k2:
					break
				
				k1 = bin(ord(k1))[2:].rjust(8, '0')
				k2 = bin(ord(k2))[2:].rjust(8, '0')
				k = k1 + k2
				k = int(k, 2)
				if k in dictionary:
					entry = dictionary[k]
				elif k == dict_size:
					entry = w + w[0:8]
				
				for i in range(0, len(entry), 8):
					temp = entry[i:i+8]
					wf.write(bytes([int(temp, 2)]))
				
				if not frozen:
					dictionary[dict_size] = w + entry[0:8]
					w = entry
				else:
					w = ""
				dict_size += 1
			
			print(dictionary)
			
			if entry:
				for i in range(0, len(entry), 8):
						temp = entry[i:i+8]
						wf.write(bytes([int(entry, 2)]))
				
	
def main():
	if len(sys.argv) < 3:
		print("Trūksta argumentų.")
		print("Programos naudojimo pavyzdys:")
		print(sys.argv[0] + " [koduojamas failas] [užkoduotas failas]")
		sys.exit()
	elif len(sys.argv) > 3:
		print("Per daug argumentų.")
		print("Programos naudojimo pavyzdys:")
		print(sys.argv[0] + " [koduojamas failas] [užkoduotas failas]")
		sys.exit()
		
	input = sys.argv[1]
	output = sys.argv[2]
	
	decompress(input, output)

if __name__ == "__main__": main()