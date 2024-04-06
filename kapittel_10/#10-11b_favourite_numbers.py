import json

filename = 'number.json'

with open(filename) as f:
    number = json.load(f)
    print(f"I think the number is {number}")