import socket
import time
import hashlib
import struct

FRAG_SZ = 1024 * 1024  # 1MB

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
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 1234))
s.listen(10)

c, addr = s.accept()

print("CONNECTED:", addr)

with open("bigfile", "rb") as f:
  while True:
    fdata = f.read(FRAG_SZ)
    if not fdata:
      break

    h = hashlib.sha256(fdata).digest()

    c.sendall(h)

    req = recvall(c, 2)
    if req is None:
      break

    if req == b"OK":
      continue

    if req == b"UP":
      c.sendall(
        struct.pack("<I", len(fdata))
      )
      c.sendall(fdata)
      continue

    raise NotImplementedError(
      f"Unknown request: {req}")

c.shutdown(socket.SHUT_RDWR)
c.close()

s.close()
