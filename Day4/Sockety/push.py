import socket
MB = b'X' * (1024**2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("192.168.0.180", 1234))
    s.sendall(MB)