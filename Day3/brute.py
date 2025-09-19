import hashlib
import time
import multiprocessing

user = 'asdf'
passwordhash = '422dce237cd6ba98fbcfea312c8f1fd1f042a81e11b78de3b31663cddcc08a14'.lower()

PROCESS_COUNT = 20

# 1 -> 4,37
# 2 -> 2,30
# 3 -> 1,96 <----
# 4 -> 2,17
# 20 -> 5,36

def brute(passwordhash, i, total_count, the_end, very_start):
	print(f"Process {i} started..." )
	while not the_end.value:
		h = hashlib.sha256(str(i).encode()).hexdigest()
		if h == passwordhash:
			print(f"ZNalezione hasło: {i} (w {time.time()-very_start} sek.)")
			
			with the_end.get_lock():
				the_end.value += 1
			
			break
		i += total_count
	print(f"Process {i} ended.")

def main():
	very_start = time.time()
	the_end = multiprocessing.Value('i', 0)
	pool = []
	for i in range(PROCESS_COUNT):
		p = multiprocessing.Process(
			target=brute, 
			args=(passwordhash, i, PROCESS_COUNT, the_end, very_start),
		)
		pool.append(p)
		p.start()
	print("All processes have started")
	for th in pool:
		th.join()


if __name__ == "__main__":
	main()
	



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