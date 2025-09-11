import json
from fastapi import FastAPI
from typing import List


app = FastAPI()

@app.post('/api/add-numbers')
def add_numbers(
  api_key: str,
  numbers: List[int]
):
  if api_key != "TAJNEHASLO":
    return{
      "result": None,
      "error": True,
      "error_msg": "access denied"
    }

  acc = 0
  for n in numbers:
    acc += n
  return { 
    "result": acc,
    "error": False,
    "error_msg": None
  }
# r = add_numbers([1,2,3,4])
# print(json.dumps(r))