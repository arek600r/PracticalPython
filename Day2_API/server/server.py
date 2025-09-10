import json
def add_numbers(numbers):
    acc = 0
    for n in numbers:
        acc += n
    return { 
        "result": acc,
        "error": False,
        "error_msg": None
    }
r = add_numbers([1,2,3,4])
print(json.dumps(r))