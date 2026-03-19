# import socket

# MB = b'X'*(1024*1024)
# #print(MB)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.0.180", 1235))

# print("Wysyłam dane...")
# s.sendall(MB)
# print("Dane wysłane!")

# #data = s.recv(1024)
# #print('Received', data)
# input("Naciśnij ENTER, aby fizycznie rozłączyć i zamknąć program...")

import socket

print("1. Przygotowuję paczkę danych...")
MB = b'X' * (1024 * 1024 * 5)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("2. Łączę z serwerem...")
    s.connect(("192.168.0.180", 1235)) # Upewnij się, że to nadal poprawne IP
    
    print("3. Zaczynam wysyłać dane...")
    for x in range(500):
	    s.sendall(MB)
    
except Exception as e:
    print(f"\n[!!!] UWAGA, BŁĄD W KLIENCIE: {e}\n")
finally:
    s.close()
    print("6. Gniazdo zamknięte.")