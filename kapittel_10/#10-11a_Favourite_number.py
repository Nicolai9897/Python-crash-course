import json

number = input("what is your favourite number?")

filname = 'number.json'
with open(filname, 'w') as f:
    json.dump(number, f)
    print(f"thanks, I'll try to remember the number {number}")

