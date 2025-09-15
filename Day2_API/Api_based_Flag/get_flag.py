import requests
import json

ADDR = "https://py10-day2-577570284557.europe-west1.run.app/ex5"
POSTT = ["get-columns","get-row-count", "get-entry"]
GETT = "get-tables"
"""
GET /ex5/get-tables
POST /ex5/get-columns
POST /ex5/get-row-count
POST /ex5/get-entry

r = requests.get(...)
r.json()
requests.post(..., json={...})
sorted()
"""
headers = {
	"Content-Type": "application/json"
}

def get_tables():
	res = requests.get(f"{ADDR}/get-tables")
	return res.json()

def get_columns(table):
		data = {"table": table}
		#print(table)
		res = requests.post(f"{ADDR}/get-columns",headers=headers, json=data)
		return res.json()

def get_row(table):
	data = {"table": table}
	#print(table)
	res = requests.post(f"{ADDR}/get-row-count",headers=headers, json=data)
	return res.json()['row_count']

def get_entry(table, column, row):
	data = {
		"table": table,
		"row": row,
		"column":column
		}
	#print(f"{table}, {column}")
	res = requests.post(f"{ADDR}/get-entry",headers=headers, json=data)
	return res.json()['entry']

def execute_flag():
	character = []
	index = []
	for j in get_columns("flag"):
	 	for x in range(get_row("flag")):
	 		#print(get_entry("flag",j,x))
	 		if j == 'character':
	 			character.append(get_entry("flag",j,x))
	 			
	 		elif j == 'index':
	 			index.append(get_entry("flag",j,x))

	slownik = dict(zip(index, character))
	values_sorted = [v for k, v in sorted(slownik.items())]
	return "".join(values_sorted)

print(execute_flag())