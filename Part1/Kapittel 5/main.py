import random
n = random.randint(0, 95)

##5-1 Conditional Tests
#car = "BMW"
#print("Jeg tror ikke car == bmw")
#print(car == "bmw")
#print()
#
#print("jeg tror car == BMW")
#print(car == "BMW")
#print()
#
#print("jeg tror car == bmw nå. rofl.")
#print(car.lower() == "bmw")
#print()
#
#print ("Jeg tror car == 'bMw'.lower")
#print(car == 'bMw'.lower())
#print()
#
#print("jeg tror car =! pizza")
#print(car == "Pizza")
#print()
#
#mat = ["Taco", "pizza", "grøt", "kjøttkaker", "lammekotteletter"]
#print("jeg ror tace er en del av mat listen")
#print("taco".title() in mat)
#print()
#
#print("jeg tor ikke grønnsaker er en del av matlisten")
#print("grønnsaker" in mat)
#print()
#
#print("Om jeg stiller spørsmplet riktig, så kan jeg få true nå")
#print("grønnsaker" not in mat)
#
#for mats in mat:
#    if "pizza" not in mats:
#        print(f"{mats}, er en del av matrettene")
#    else:
#        print("pizza er også en del, men jeg ville ikke liste opp dan av politiske årsaker")
#print()
#
#if "pizzza" and "taco" in (mats.lower() for mats in mat): # Her går jeg igjennom hele listen med mat, og sjekker hvert
#    # element, en etter en om den inneholder taco i lowercase.
#    print("maten inneholder både pizza og taco. nice")
#print("\n")

#5-3 Alien colors #1
alien_color = "green"
if alien_color == "green":
    print("green alien. 5 points!")
    print()

alien_color = "red"
if alien_color == "Green":
    print("green alien. 5 points!")
else:
    print("non green alien. 0 points!")
    print("\n")

#5-4 Alien colors #2
alien_color = "blue"
if alien_color == "green":
    print("5 Points!")
else:
    print("10 points!")
    print()


alien_color = "green"
if alien_color == "green":
    print("5 Points!")
else:
    print("10 points!")
print("\n")

#5-5 Alien colors #3
alien_color = "green"
if alien_color == "green":
    print("5 Points!")
elif alien_color == "yellow":
    print("10 Points!")
else:
    print("15 points!")
print()

alien_color = "yellow"
if alien_color == "green":
    print("5 Points!")
elif alien_color == "yellow":
    print("10 Points!")
else:
    print("15 points!")
print()

alien_color = "red"
if alien_color == "green":
    print("5 Points!")
elif alien_color == "yellow":
    print("10 Points!")
else:
    print("15 points!")
print("\n")

# 5-6 Stages of life
person_age = n
stage_of_life = None

if person_age <2:
    stage_of_life = " baby"
elif person_age <4:
    stage_of_life = " toddler"
elif person_age <13:
    stage_of_life = " kid"
elif person_age <20:
    stage_of_life = " teenager"
elif person_age < 65:
    stage_of_life = "n adult"
else:
    stage_of_life = "n oldtimer"

print(f"you are {person_age} years. That means you are a{stage_of_life}.")
print("\n")

#Favourite fruit
favourite_fruits = ['apples', 'bananas', 'potatoes']

if 'mushroom' in favourite_fruits:
    print("jævle soppløk")
if "bananas" in favourite_fruits:
    print("ape?")
if "onion" in favourite_fruits:
    print("crying much?")
if "tomatoe" in favourite_fruits:
    print("pizza")
if "apples" in favourite_fruits:
    print("apple pie!")
print("\n")

#5-8 hello admin
usernames = ['admin', 'nick', 'Mike', 'john', 'John Cena']

for user in usernames:
    if user == "admin":
        print(f"Hello there {user}, how would  you like to control the server today?")
    else:
        print(f"Hello {user}, have a good day.")
print("\n")

#5-9 No user
del usernames [:]
if usernames:
    for user in usernames:
        if user == "admin":
            print(f"Hello there {user}, how would  you like to control the server today?")
        else:
            print(f"Hello {user}, have a good day.")
else:
    print("Vi trenger noen brukere....")
print("\n")

#5-10 Checking usernames
current_users = ['john', 'cena', 'Sheffiels', 'Nicolai', 'Master', 'slave']
new_users = ['mike', ' master', 'cripple', 'slaVe', 'Aurora', 'Lene']

current_users_lower = [user.lower().strip() for user in current_users]

for new_user in new_users:
    if new_user.lower().strip() in current_users_lower:
        print(f"{new_user.strip()}, is unavailable, please select another username")
    else:
        print(f"welcome to the party {new_user}")
print("\n")

#5-11 Ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

