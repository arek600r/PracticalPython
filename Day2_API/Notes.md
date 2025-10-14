API - aplication programming intrerface
---

RPC - remove procedure call (zdalne wywołanie funkcji)
SDK - software developer kit
json - javascript objection notation
SOAP - XML
MCP - 
jaml - tworzenie configów

curl https://api/ | jless 
jless (reader dla json'a)


---

```python
def add_numbers(numbers):
    acc = 0
    for n in numbers:
        acc += n
    return acc
    #albo return sum(numbers)

>>> add_numbers([2, 40])
42
```

```http
https://example.com/api/addNumbers
```
```json
{
    "numbers": [2, 40]
}
{
    "result": 42
}
```
info
API googlowe są mało przyjemne do pracy ;)

W pythonie '' i "" to jest kompletnie to samo

VirtualEnvironment:
python -m venv env
.\env\Sripts\Activate.ps1

naprawa PIP
python -m pip install --upgrade pip

