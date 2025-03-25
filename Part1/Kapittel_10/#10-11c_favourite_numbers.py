import json




def get_stored():
    """gets the stored number to give the user"""
    filename = 'number2.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_number():
    """promts for new number"""
    number = input("what is your favourite number?")
    filname = 'number2.json'
    with open(filname, 'w') as f:
        json.dump(number, f)
    return number



def return_number():
    """Return the number to the user"""
    number = get_stored()
    if number:
        print(f"your number is {number} bitch!")
    else:
        number = get_number()
        print(f"Ill remember the number {number}")


return_number()