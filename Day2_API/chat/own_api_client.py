import requests
import json

def get_currency(currency):
	res = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/C/{currency}/")
	data = res.json()
	return f"""
--------
Koszt zakupu i sprzedaży { data['currency'] } na dzień { data['rates'][0]['effectiveDate'] } :
Zakup: { data['rates'][0]['bid'] }
Sprzedaż: { data['rates'][0]['ask'] }
--------
"""

def gold_price():
	res = requests.get(f"https://api.nbp.pl/api/cenyzlota/")
	data = res.json()
	return data


#print(get_currency("GBP"))

while True:
	inp = None
	print("what you want to do?")
	try:
		inp = int(input("""
 		If you want to check currency - click 1
 		If you want to check price of gold - click 2
 			"""))
		print(inp)
		if int(inp) == 1:
			inpu = input("What currency you want to check?")
			print(get_currency(inpu))
		elif int(inp) == 2:
			print(gold_price())
		else:
			print("go fuck yourself.")
			break
	except ValueError as e:
		print("Weź nie kombinuj")