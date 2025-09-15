import requests

res = requests.get("https://py10-day2-577570284557.europe-west1.run.app/ex1")

while True:
		print(res.json())
		try: 
			addr = res.json()['next_url']
			print(addr)
			res1 = requests.get(addr)
			if res1.status_code == 200:
				res = res1
				continue

		except KeyError as e:
			print("Nie ma takiej wartości w słowniku jak ", e)
			break