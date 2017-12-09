import sys
import struct

def compress(input, output, dict_limit, dict_freeze):
	frozen = False
	with open(input, "rb") as rf:
		with open(output, "wb") as wf:
			dict_size = 256
			dictionary = {format(i, "08b"): i for i in range(dict_size)}
			
			wf.write(bytes([int(format(dict_limit, "08b"),2)]))
			wf.write(bytes([int(format(dict_freeze, "08b"),2)]))
			
			dict_limit = 2**dict_limit
			w = ""
			while True:
				if dict_size == dict_limit and dict_freeze:
					frozen = True
				elif dict_size == dict_limit and not dict_freeze:
					dict_size = 256
					dictionary = {}
					dictionary = {format(i, "08b"): i for i in range(dict_size)}
				
				c = rf.read(1)
				if not c:
					break
				c = bin(ord(c))[2:].rjust(8, '0')
				wc = w + c
				if wc in dictionary:
					w = wc
				else:
					n = format(dictionary[w], "016b")
					c1 = n[0:8]
					c2 = n[8:16]
					wf.write(bytes([int(c1, 2)]))
					wf.write(bytes([int(c2, 2)]))
					if not frozen:
						dictionary[wc] = dict_size
						dict_size += 1
						w = c
	
			#print(dictionary)
			if w:
				for i in range(0, len(w), 8):
					n = format(dictionary[w[i:i+8]], "016b")
					c1 = n[0:8]
					c2 = n[8:16]
					wf.write(bytes([int(c1, 2)]))
					wf.write(bytes([int(c2, 2)]))
				

def main():
	if len(sys.argv) < 5:
		print("Trūksta argumentų.")
		print("Programos naudojimo pavyzdys:")
		print(sys.argv[0] + " [koduojamas failas] [užkoduotas failas] [žodyno dydis] [šaldyti ar ištrinti žodyną (0 arba 1)]")
		sys.exit()
	elif len(sys.argv) > 5:
		print("Per daug argumentų.")
		print("Programos naudojimo pavyzdys:")
		print(sys.argv[0] + " [koduojamas failas] [užkoduotas failas] [žodyno dydis] [šaldyti ar ištrinti žodyną (0 arba 1)]")
		sys.exit()
		
	input = sys.argv[1]
	output = sys.argv[2]
	dict_limit = int(sys.argv[3])
	dict_freeze = int(sys.argv[4])
	
	compress(input, output, dict_limit, dict_freeze)

if __name__ == "__main__": main()