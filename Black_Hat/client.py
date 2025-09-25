import socket

target_host = "www.google.com"
target_port = 80

target_host_udp = "127.0.0.1"
target_port_upd = 9997

def tcp(target_host, target_port):
	#gniazdo obiektu
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#połączenie
	client.connect((target_host, target_port))
	#wysłanie
	client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
	respone = client.recv(4096)
	client.close()
	
	return respone.decode()


def upd(target_host, target_port):
	#gniazdo obiektu
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	#Wysłanie danych
	client.sendto("AAABBBCCC", (target_host_udp, target_port_upd))

	data, addr = client.recvform(4096)
	client.close()
	return data.decode()

print(tcp(target_host, target_port))

