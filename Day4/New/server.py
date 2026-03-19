import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 1235))
s.listen(1234)

c, addr = s.accept()
#powyzszy zapis jest tożsamy z:
#res = s.accept()
#c = res[0]
#addr = res[1]

print("CONNECTED: ", addr)

start = time.time()
total = 0
while True:
    data = c.recv(1024)
    if not data:
        print("disconnected")
        break

    total += len(data)

    now = time.time()
    interval = now - start
    if interval >= 1.0:
        speed = total /  interval
        print(f"Speed: {speed / 1024} KB per second")
        
        total = 0
        start = now
# W którym kierunku zamykamy połączenie
#c.shutdown(socket.SHUT_RDWR)
c.close()
# ctrl z
# bg 1
# jobs -p
# ls -la /proc/number/fd
s.close()


"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
"""