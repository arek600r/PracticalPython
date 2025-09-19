import hashlib
import time
import threading

user = 'asdf'
passwordhash = '422dce237cd6ba98fbcfea312c8f1fd1f042a81e11b78de3b31663cddcc08a14'.lower()

THREADS_COUNT = 12 

very_start = time.time()
the_end = threading.Event()

def brute(passhash, i, total_count):
	while not the_end.is_set():
		h = hashlib.sha256(str(i).encode()).hexdigest()
		if h == passwordhash:
			print(f"ZNalezione hasło: {i} (w {time.time()-very_start} sek.)")
			the_end.set()
			break
		i += total_count
threads = []
for i in range(THREADS_COUNT):
	th = threading.Thread(
		target=brute, 
		args=(passwordhash, i, THREADS_COUNT),
		daemon=True
	)
	threads.append(th)
	th.start()

for th in threads:
	th.join()



"""
users = {
'asdf': '63b347973bb99fed9277b33cb4646b205e9a31331acfa574add3d2351f445e43'
}

sent_username = 'asdf'
sent_password = '1234567'

if(hashlib.sha256(sent_password.encode()).hexdigest() == users[sent_username]):
	print("UDALO SIE LOGGED IN")
else:
	print("ZLE HASLO") 
"""