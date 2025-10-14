import json
from fastapi import FastAPI
def add_numbers(numbers):
    acc = 0
    for n in numbers:
        acc += n
    return { 
        "result": acc,
        "error": False,
        "error_msg": None
    }
#r = add_numbers([1,2,3,4])
#print(json.dumps(r))

#różnice miedzy słownikiem a json'em 
# cudzysłowie zamiast apostrofu, false zamiast False i null zamiast None

