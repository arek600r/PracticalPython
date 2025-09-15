from openai import OpenAI
import os
import requests
import time
import json
import sys

os.system("")

USER_AGENT = "SimpleChat"

def city_to_gps(city):
	time.sleep(1)
	r = requests.get('https://nominatim.openstreetmap.org/search.php',
		params={
		"city":city,
		"format":"jsonv2"
		},
		headers={
			"User-Agent": USER_AGENT
		}
	)
	res = r.json()
	if len(res) == 0:
		return None
	lat = res[0]["lat"]
	lon = res[0]["lon"]

	return lat, lon

def weather(lat, lon):
	time.sleep(1)
	r = requests.get('https://api.open-meteo.com/v1/forecast',
		params={
		"latitude": lat,
		"longitude": lon,
		"daily":"temperature_2m_max"
		},
		headers={
			"User-Agent": USER_AGENT
		}
	)

	res = r.json()
	return f'{res["daily"]["temperature_2m_max"][0]} C'


# lat, lon = city_to_gps("Bydgoszcz")
# print(weather(lat,lon))


api_key = open("C:\\Users\\arek_\\Documents\\GitHub\\Secrets\\Key.key").read().strip()
client = OpenAI(api_key=api_key)

tools = [{
  "type": "function",
  "name": "get_weather",
  "description": "Get current temperature for a given location.",
  "parameters": {
  	"type": "object",
  	"properties": {
  	"location": {
  		"type": "string",
  		"description": "City, without country, e.g London"
  		}
  	},
  	"required": ["location"],
  	"additionalProperties": False
  },
  "strict": True
  }
]

log = []
print("You can start your chat now")

skip_input = False
while True:
	try:
		if not skip_input:
			input_text = input("? ")
	except KeyboardInterrupt:
		break
	log.append({
		"role": "user",
		"content": input_text
		})

	responses = client.responses.create(
		model="gpt-4.1-nano",
		input=log,
		tools=tools
)
	for o in responses.output:
		log.append(o)
		if o.type == "message":
			print(f'\x1b[1;33m{o.content[0].text}\x1b[m')	
			skip_input = False

		elif o.type == "function_call":
			args = json.loads(o.arguments)

			if o.name == "get_weather":
				#print("get_weather")
				lat, lon = city_to_gps(args["location"])
				#print("lat, lon", lat, lon)
				res = weather(lat,lon)
				#print("res: ", res)
				log.append({
					"type": "function_call_output",
					"call_id": o.call_id,
					"output": res
				})
				skip_input = True
				continue
			raise Exception(f"Unknown function: {o.name}")

print("End.")
