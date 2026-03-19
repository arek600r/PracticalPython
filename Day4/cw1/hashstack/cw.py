import hashlib

FRAG_SZ = 512

with open("hashstack.bin", "r+b") as f:
	while True:
		fdata = f.read(FRAG_SZ)
		#print(f"{len(fdata)}")
		z = hashlib.sha256(fdata).hexdigest()
		if z == "790d88483531ac32a12a57b233818ff698fb4ed7011f5c749f3b7493ba1ac5e1":
			x = fdata.decode()
			x = x[::-1].split()
			print("".join(x))
		if not fdata:
			break