import socket
import time
import hashlib
import struct 

FRAG_SZ = 1024 * 1024

def recvall(s, sz):
    total = 0
    data = []

    while True:
        part_data = s.recv(sz - total)
        if not part_data:
            return None
        total += len(part_data)
        data.append(part_data)


        if total == sz:
            return b''.join(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.180", 1234))

print("CONNECTED: ")

frag_number = -1
with open ("bigfile", "r+b") as f:
    while True:
        frag_number += 1
        fdata = f.read(FRAG_SZ)
        if not fdata:
            break

        h_our = hashlib.sha256(fdata).digest()

        h_serv = recvall(s, 32)

        if h_serv is None:
            print("Done. Disconnected")
            break

        
        if h_our == h_serv:
            print(f"Frag {frag_number} is good")
            s.sendall(b"OK")
            continue

        print(f"Frag {frag_number} is BAD: ", 
              end="", flush=True)
        s.sendall(b"UP")
        
        frag_len = struct.unpack(
            "<I", recvall(s,4)
        )[0]

        print(f"{frag_len // 1024} KB... ", end="", flush=True)
        sdata = recvall(s, frag_len)

        print(f"{len(sdata) // 1024} downloaded... ", end="",
              flush=True)
        
        offset = f.tell()
        f.seek(offset - len(fdata))
        f.write(sdata)
        print("patched!")
s.close()
