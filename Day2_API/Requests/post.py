import requests

data = None
res = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex2", data=data)

while True:
	if 'next_secret' in res.json():
		data = res.json()['next_secret']
		print(data)
		res = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex2", data=data)
	else:
		print(res.json())
		break