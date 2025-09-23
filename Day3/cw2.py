import hashlib
import string
import itertools
import requests
import os
from pathlib import Path
"""
1. Hasło składa się z nie więcej niż 8 cyfr. Hash: SHA256:
ac3fbb3474801233a338e0f27af3477773ad8772d35c87f70d9489837babb35a

2. Hasło składa się z nie więcej niż 5 małych liter. Hash: SHA1:
4ea78d09f35f05ad59b2a682822efb06b236564c

3. Hasło ma 3 wielkie litery na początku i 4 cyfry potem (np. ABC123). Hash: MD5:
5aeac724d573198038d8b0a8b0542bc9

4. Hasło jest na liście wordlist.txt. Hash: SHA384:
548568964fb078e3a030da81829aa18e88f93339bd1f480fc8fa795bb6bb95b87e9661ee
bea26e72163063d0bda11640

5. Hasło to dwa słowa z wordlist.txt, jedno po drugim, oraz 2 cyfry na końcu. Hash: MD5:
e903d2c82106d626f4986799ce2b55a4
"""

LENGHT = 99999999
ALPHABET_LOW = string.ascii_lowercase
ALPHABET_HIGH = string.ascii_uppercase
DIGITS = [1,2,3,4,5,6,7,8,9,0]
"""
hashes = {
"SHA256" : "ac3fbb3474801233a338e0f27af3477773ad8772d35c87f70d9489837babb35a",
"SHA1" : "4ea78d09f35f05ad59b2a682822efb06b236564c",
"MD5" : "5aeac724d573198038d8b0a8b0542bc9",
"SHA384" : "548568964fb078e3a030da81829aa18e88f93339bd1f480fc8fa795bb6bb95b87e9661eebea26e72163063d0bda11640",
"MD5" : "e903d2c82106d626f4986799ce2b55a4"
}

def brute1(pass_hash):
	for i in range(LENGHT):
		h = hashlib.sha256(str(i).encode()).hexdigest()
		if h == pass_hash:
			print(f"ZNalezione hasło: {i}") // 13371337

brute("ac3fbb3474801233a338e0f27af3477773ad8772d35c87f70d9489837babb35a")


def brute2(pass_hash):
	for i in range(6):
		for candidate in itertools.product(ALPHABET, repeat=5):
			candidate = ''.join(candidate)
			print(candidate)
			h = hashlib.sha1(str(candidate).encode()).hexdigest()
			print(h)
			ifh == pass_hash:
				print(f"ZNalezione hasło: {candidate}") //aloha
				break
brute("4ea78d09f35f05ad59b2a682822efb06b236564c")

"""
# do sprawdzenia
def brute3(pass_hash):
#123AAAA

	for candidate in itertools.product(ALPHABET_HIGH, repeat=3):
		candidate = ''.join(candidate)
		for digit in itertools.product(DIGITS, repeat=4):
			digit = ''.join(str(d)for d in digit)
			passwd = f"{candidate}{digit}"
#			print(passwd)
			h = hashlib.md5(str(passwd).encode()).hexdigest()
#			print(h)
			if h == pass_hash:
				print(f"ZNalezione hasło: {passwd}")  # hex
				break
#brute3("5aeac724d573198038d8b0a8b0542bc9")

def brute4(pass_hash):
	my_file = "wordlists.txt"
	with open(my_file, 'r') as f:
		lines = f.readlines()
		for i in lines:
			h = hashlib.sha384(str(i.strip()).encode()).hexdigest()
			print(f"{i} : {h}")
			if h == pass_hash:
				print(f"ZNalezione hasło: {i}")  # hex
				break
brute4("548568964fb078e3a030da81829aa18e88f93339bd1f480fc8fa795bb6bb95b87e9661eebea26e72163063d0bda11640")

def brute5(pass_hash):
	my_file = "wordlists.txt"
	with open(my_file, 'r') as f:
		lines = f.readlines()
	for i in lines:
		for j in lines:
			for digit in itertools.product(DIGITS, repeat=2):
				digit = ''.join(str(d)for d in digit)
				passwd = f"{i.strip()}{j.strip()}{digit.strip()}"
				h = hashlib.md5(str(passwd).encode()).hexdigest()
	
				if h == pass_hash:
					print(f"ZNalezione hasło: {passwd}") # sunshinePassword42
					break

#brute5("e903d2c82106d626f4986799ce2b55a4")