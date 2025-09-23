import zlib
import itertools
import string
import random
import sys
ALPHABET_LOW = string.ascii_lowercase
DIGITS = [1,2,3,4,5,6,7,8,9,0]

alph_digit = {}

#for i in range(4,5):
	#słownik z litermia
for chars in itertools.product(ALPHABET_LOW, repeat=5):
	chars = "".join(chars)
	key_alpha = zlib.crc32(chars.encode())
	alph_digit[key_alpha] = chars

while True:
	for i in range(10000):
		for j in range(1,7):
			passwd = "".join(random.choices("0123456789", k=j))
			crcpass = zlib.crc32(passwd.encode())
			#print(crcpass)
			if crcpass in alph_digit:
				print(f"Kolizja! CRC={crcpass}, cyfry: {passwd}, litery: {alph_digit[crcpass]}")
				sys.exit()
