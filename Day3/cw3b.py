import zlib
import random
hashdict = dict()
#print(zlib.crc32(b'asdf'))
#print(zlib.crc32(b'1234'))
while True:
    randk = random.randint(1,30)
    letterss = random.choices("abcdefghijklmnopqrstuvwxyz", k = randk)
    letterss = "".join(letterss)
    hashdict[zlib.crc32(letterss.encode())] = letterss
    
    digitss = random.choices("0123456789", k = randk)
    digitss = "".join(digitss)
    h_dig = zlib.crc32(digitss.encode())
    if h_dig in hashdict:
        print(hashdict[zlib.crc32(digitss.encode())])
        print(digitss) 
        break

