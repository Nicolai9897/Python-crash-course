import json

def greet_user():
    """Greet the user by name."""
    username = get_store_username()
    if username:
        print(f"velkom tilbake, {username}!")
    else:
        username = get_new_username()
        print(f"We'll rememberyou for the next time")

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def get_store_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username





def welcome():
    print(f"Hello there, is {get_store_username()} your name?")
    answer = input("type 'y' if it ir, or 'n' if it is not")
    if(answer == 'y'):
        greet_user()
    elif(answer == 'n'):
        get_new_username()
        print("we")
    else:
        print("sorry you cant follow instructions")

welcome()

