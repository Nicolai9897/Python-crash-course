#10-3/4. Guest:
filename = 'guestbook.txt'
def guests():
    """method for adding names to a guest book"""
    run = True

    print("type \"exit\" to exit the application")
    while run:
        name = input("please iwrite you name for the guestbook:")
        if name == "exit":
            run = False
        else:
            print(f"it's a pleasure to meet you {name} \n")
            with open(filename, 'a') as file_object:
                file_object.write(f"{name} \n")

#guests()


#10-5. Programming poll:
filename = 'responeses.txt'
def poll():
    """poll for askin people why they like programming,
    and adding the reasons to a text file after every answer"""
    run2 = True
    print('type "exit" to exit the application')
    print("Please write some of the reasons to why you like programming."
          "press enter after every reason.")
    while run2:
        reason = input("reason: ")

        if reason == "exit":
            run2 = False
        else:
            with open(filename, 'a') as file_object:
                file_object.write(f"{reason} \n")

poll()


