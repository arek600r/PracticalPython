import requests
import json
import itertools
import hashlib
# dostajemy hash z API: challange
# doklejamy do niego nowe bajty:
# 807892c60b4822818171eec95815da41fa53448b2c1c4fdf + 0 - > 255 to hex
#-------
#>>> chal = b''.fromhex('807892c60b4822818171eec95815da41fa53448b2c1c4fdf')
#>>> hashlib.sha256(chal + b'\x31\x23\x36\x00\x00\x00\x00\x00').hexdigest()
#'ffffffeeae8f96e29ade369c5e51013f7b34abb12f8c5856ae13863b43538bd7'
#-------

API = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow"
r = requests.get(API)
res = r.json()
hash = res['challenge']
chal = b''.fromhex(hash)
while True:
    found = False
    for x in range(1, 20):
        for kombinacje in itertools.product(range(256), repeat=x):
            bajt = bytes(kombinacje)
            value_new = ((chal+bajt).hex())
            print("good: ", end="") 
            print(b''.fromhex(value_new))
            print(value_new.encode())
            newhash = hashlib.sha256(b''.fromhex(value_new)).hexdigest()
            newhash_a = hashlib.sha256(value_new.encode()).hexdigest()
            #print("goodhash: " + newhash)
            #print("badhash: " + newhash_a)
            if newhash[0:6] == "ffffff":
                print(newhash)
                newr = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-flag?pow="+value_new)
                print(newr)
                newres = newr.json()
                print(newres)
                break

#print(bytes.fromhex(hash))
# 00 -> ff , 00 00 -> ff ff



#data.hex()