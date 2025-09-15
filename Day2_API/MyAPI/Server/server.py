import json
from fastapi import FastAPI
from typing import List


app = FastAPI()

@app.post('/api/add-numbers')
def add_numbers(numbers: List[int]):
  acc = 0
  for n in numbers:
    acc += n
  return { 
    "result": acc,
    "error": False,
    "error_msg": None
  }

@app.post('/api/sub-numbers')
#substract rest numbers from the first [42,1,4] -> 42-1-4
def sub_numbers(numbers: List[int]):
  acc = 0
  first_value = False
  for n in numbers:
  	if (first_value == False):
  		acc += n
  		first_value = True
  		continue
  	else:
	    acc -= n
  return { 
    "result": acc,
    "error": False,
    "error_msg": None
  }

@app.post('/api/multi_numbers')
def mutli_numbers(numbers: List[int]):
  acc = 1
  for n in numbers:
  	acc *= n
  return { 
    "result": acc,
    "error": False,
    "error_msg": None
  	}

@app.post('/api/divide_numbers')
def divide_numbers(numbers: List[int]):
  acc = 0
  first_value = False
  for n in numbers:
  	if (first_value == False):
  		acc += n
  		first_value = True
  		continue
  	else:
	    acc /= n
  return { 
    "result": acc,
    "error": False,
    "error_msg": None
  	}