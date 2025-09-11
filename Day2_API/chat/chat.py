from openai import OpenAI
import os
import requests
import time

os.system("")

def city_to_gps(city):
	time.sleep(1)
	r = requests.get('https://nominatim.openstreetmap.org/search.php',
		params={
		"city":city,
		"format":"jsonv2"
		},
		headers={
			"User-Agent": "SimpleChat"
		}
	)
	res = r.json()
	if len(res) == 0:
		return None
	lat = res[0]["lat"]
	lon = res[0]["lon"]

	return lat, lon

print(city_to_gps("Krakow"))
"""
api_key = open("C:\\Users\\arek_\\Documents\\GitHub\\Secrets\\Key.key").read().strip()
client = OpenAI(api_key=api_key)

log = []
print("You can start your chat now")

while True:
	try:
		input_text = input("? ")
	except KeyboardInterrupt:
		break
	log.append({
		"role": "user",
		"content": input_text
		})

	responses = client.responses.create(
		model="gpt-4.1-nano",
		input=log
)
	print(f'\x1b[1;32m{responses.output_text}\x1b[m')	

print("End.")
"""