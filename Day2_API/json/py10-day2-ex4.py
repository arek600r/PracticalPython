#!/usr/bin/python3

# Nie musisz modyfikować kodu w tym zadaniu aby je rozwiązać.
# Ale bardzo zachęcamy do zapoznania się z nim!

import json
def read_json(fname):
  try:
    with open(fname, "r") as f:
      return json.load(f)
  except FileNotFoundError:
    return f"File {fname} was not found"
  except json.decoder.JSONDecodeError as e:
    return f"File {fname} is not a correct JSON file: {e}"

func = read_json
final_results = []
all_good = True
for args, expected_result in [
  (("value.json",), 42),
  (("list.json",), [False, 1, "two"]),
  (("dict.json",), {"list": [3,4,5], "str": "hi there", "number": 42,
                    "null": None, "bool": True }),
]:
  print(f"Testing {args}: ", end="")
  actual_result = func(*args)
  if actual_result == expected_result:
    print("GOOD!")
  else:
    print(f"Wrong! Expected result: {expected_result}, "
          f"Actual result: {actual_result}")
    all_good = False
  final_results.append(actual_result)

if not all_good:
  print("Flag remains hidden until all tests pass.")

# Kod rozszyfrowujący flagę... jeśli wszystkie testy przeszły :)
import json
import hashlib
tmp = json.dumps(final_results)
hash = hashlib.sha512(tmp.encode()).digest()

GOOD_HASH = "de59350bd121f675800e91415dae8d3c9c517ec4"
ENC_FLAG = ("0b09c008ceb64dd8190f0e2fe46f446e064d68ec4593"
            "5d14816fc8474564ce139ae50fcb2e5ff9c81c87ff97")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

