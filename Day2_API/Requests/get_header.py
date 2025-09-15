import requests
addr = "https://py10-day2-577570284557.europe-west1.run.app/ex3"
res = requests.get(addr)
print(res.json())

while True:
	if 'next_secret' in res.json():
		headers = res.json()['next_secret']
		print(headers)
		res = requests.get(addr,headers={"X-Secret": headers})
		
	else:
		print(res.json())
		break