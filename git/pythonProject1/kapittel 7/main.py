#7-1 Rental car
car = input("what car do you wish to buy? \n")
print(f"A {car}? let me see if I can find that for you!")

#7-2 Restaurant seeting
guest_number = input("How many people will eat at this fine establishement today? \n")
guest_number = int(guest_number)

if guest_number < 8:
    print(f"{guest_number} people. Findy dandy, come with me right away!")
else:
    print(f"{guest_number} People? I'm am sorry, but this is a fine establishement, and we do not seat that many people"
          f". Now please leave.")

#7-3 Multiple of ten
guessing_number = input("Tell me a number, and I will tell you if it can be divided by ten! \n")
guessing_number = int(guessing_number)

if guessing_number % 10 == 0:
    print(f"{guessing_number} is divisible by ten!")
else:
    print("I'm sory, you picked a bed number that is not divisible by ten. Please try again next time.")

#7-4 pizza toppings
quit1 = False
print("welcome to nico pizzo. Please write 'quit' when you wish to exit the store page")
while not quit:
    topping = input("what pizza toppings do you wish to have on your pizza? \n")

    if topping != "quit":
        print(f"{topping}? no problemo, I'lll add it straight away!")
    else:
        quit1 = True

#7-5 movie tickets
print("Welcom to Nico's movie theatre. What ages will the viewers be at when watching the movie?")
print("To inndicate that you have ordered all tickets, write 'finished' to the application")

under_3 = 0  # free
age_3_12 = 0  # 10$
over_12 = 0  # 15$

while True:
    age = input("What age will the viewer be?")
    if age == "finished":
        break

    age = int(age)

    if age < 3:
        under_3 += 1
    elif age <= 12:
        age_3_12 += 1
    else:
        over_12 += 1

print("Here is the list of the tickets to purchase:")
print(f"{under_3} tickets to people under three for a price of 0$")
print(f"{age_3_12} tickets to people from the ages 3 to twelve for the price of 10$ each")
print(f"{over_12} tickets to people over twelve for the price of 15$ each")
total_price = (age_3_12 * 10) + (over_12 * 15)
print(f"total price to pay: {total_price}$")


#7-6 three exits
active = True
print("welcome to nico pizzo. Please write 'quit' when you wish to exit the store page")
while active:
    topping = input("what pizza toppings do you wish to have on your pizza? \n")

    if topping != "quit":
        print(f"{topping}? no problemo, I'lll add it straight away!")
    else:
        active = False

print("welcome to nico pizzo. Please write 'quit' when you wish to exit the store page")
while True:
    topping = input("what pizza toppings do you wish to have on your pizza? \n")

    if topping != "quit":
        print(f"{topping}? no problemo, I'lll add it straight away!")
    else:
        break

topping = ""
print("welcome to nico pizzo. Please write 'quit' when you wish to exit the store page")
while topping != "quit":
    topping = input("what pizza toppings do you wish to have on your pizza? \n")

    print(f"{topping}? no problemo, I'lll add it straight away!")

#7-7 infinity
i = 0
while True:
    print(i)
    i += 1


# 7-8. Deli
sandwich_orders = ['BLt', 'steakhouse', 'ham and cheese', 'papa johns', 'nick n colas']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"your {current_sandwich} sandwich is done!")

    finished_sandwiches.append(current_sandwich)

print("\nthese are all the sandwhiches that have been made so far:")
for sandwhich in finished_sandwiches:
    print(sandwhich)

# 7-9. No pastrami
sandwich_orders = [ 'pastrami', 'BLt', 'steakhouse', 'pastrami', 'ham and cheese', 'pastrami', 'papa johns', 'nick n colas']
finished_sandwiches =[]

#Kan alternativt bruke "while pastrami in sandwich_orders:"
#   sandwich_orders.remove('pastrami')

print("Sorry, there are no more pastrami sandwiches left.")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    if current_sandwich is not "pastrami":
        print(f"your {current_sandwich} sandwich is done!")
        finished_sandwiches.append(current_sandwich)

print("\nthese are all the sandwhiches that have been made so far:")
for sandwhich in finished_sandwiches:
    print(sandwhich)


# 7-10 Dream vacation
dream_vacation = {}
active = True

while active:
    name = input("What's your name?")
    vacation_spot = input("what's your dream vacation spot?")

    dream_vacation[name] = vacation_spot

    repeat = input("Would you like to register a new input? please write yes or no.")
    if repeat.strip().lower() == "no":
        active = False

print("These are all the peoples favourite places:")
for name, vacation_spot in dream_vacation.items():
    print(f"{name} : {vacation_spot}")







