import requests
import json
from pprint import pprint

def add_numbers(numbers):
	xyz  = json.dumps(numbers)
	r = requests.post("http://127.0.0.1:8000/api/add-numbers?api_key=TAJNEHASLO", data=xyz)
	#res = json.loads(r.text)
	res = r.json()
	return res["result"]

print(add_numbers([1,2,3,4]))
print(add_numbers([1,2,3,42]))