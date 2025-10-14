import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 1234))
s.listen()
c, addr = s.accept()
# można zapisać też jako:
#res= s.accept()
#c = res[0]
#addr = res[1]
#print(c)

print("CONNECTED:", addr)

start = time.time()
total = 0
while True:
    print("2")
    data = c.recv(1024)
    if not data:
        print("discontected")
        break

    total += len(data)
    now = time.time()
    print("1")
    interval = now - start
    if interval >= 1.0:
        
        speed = total / interval
        print(f"Speed: {speed / 1024} KB per second")

        total = 0
        start = now

#c.shutdown(socket.SHUT_RDWR)
c.close()
s.close()


#print(s)

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.bind((HOST,PORT))
#s.listen(1)
#conn, addr = s.accept()
#with conn:
