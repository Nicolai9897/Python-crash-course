import random
n_0 = random.randint(0, 1000000)
n_1 = random.randint(0, 1000000)
n_2 = random.randint(0, 1000000)
n_3 = random.randint(0, 1000000)
n_4 = random.randint(0, 1000000)



#6-1 Person
person = {'first_name': 'Mathias', 'last_name': 'Hansen', 'city': 'Eidsvoll'}

first_name = person.get('first_name', 'ingen navn i listen')
print(first_name)

last_name = person.get('last_name', 'ingen etternavn i listen')
print(last_name)

city = person.get('city', 'personen bor ikke i en by')
print(city)
print("\n")

#6-2 Favourite numbers
favourite_numbers = {
    'Aurora': n_0,
    'Andrea': n_1,
    'Mathias': n_2,
    'Ludo': n_3,
    'Stian': n_4,
}

print(favourite_numbers['Aurora'])
print(favourite_numbers['Andrea'])
print(favourite_numbers['Mathias'])
print(favourite_numbers['Ludo'])
print(favourite_numbers['Stian'])
print("\n")

#6-3 Glossary
glossary = {
    'Dictionary': 'Dictionary:\nTo store multiple different values and making it easier to search for a specific key',
    'Print': 'Print:\nTo display the chosen output on the console window',
    'List': 'List:\nTo add multiple values in a list, and the finding it by its index number',
    'Del': 'Del:\nTo deleted a specific variable for a list or dictionary',
    'Get': 'Get:\nUsed to get a key from dictionary, and return a statement rather than an error if key dosen\'t exist',
    'values': 'Values: \nvalues are the values of the dictionary',
    'Key': 'Key: \nBasically key i hashmap fra java',
}

dictionary = glossary.get('Dictionary', 'No dictionary found. Check if you have any spelling errors')
toPrint = glossary.get('Print', 'No Print found. Check if you have any spelling errors')
toList = glossary.get('List', 'No List found. Check if you have any spelling errors')
delete = glossary.get('Del', 'No Del found. Check if you have any spelling errors')
get = glossary.get('Get', 'No Get found. Check if you have any spelling errors')

print(f"{dictionary} \n\n{toPrint} \n\n{toList} \n\n{delete} \n\n{get}")
print("\n")
print("---------------------------------")

#6-4 Glossary 2
for glosses in glossary.values():
    print(f"{glosses}\n")
print("\n\n")

#6-5 Rivers
rivers = {
    'glomma': 'norway',
    'nile': 'egypt',
    'the Mississipi': 'USA',
}

for river, countries in rivers.items():
    print(f"{river.title()} runs through {countries.title()}")
print("\n\n")

#6-6 Polling
favorite_languages = {
    'jen': 'python',
    'Sarah': 'python',
    'edward': 'ruby',
    'Phil': 'python',
}

folk = ['Hans', 'Edward', 'sarah']

fav_lang_lower = {mennesker.lower(): språk for mennesker, språk in favorite_languages.items()}
for folks in folk:
    if folks.lower() not in fav_lang_lower:
        print(f"{folks}, du må ta undersøkelsen")
    else:
        print(f"{folks}, takk for at du tok testen!")
print("\n")


#6-7 People
people = {
    'Mads_Mikkelsen': {
        'first_name': 'Mads',
        'last_name': 'Mikkelsen',
        'city': 'Oslo',
    },
    'Kari_Gåse': {
        'first_name': 'Kari',
        'last_name': 'gåse',
        'city': 'Bergen',
    },
    'Nicolai_Olsen': {
        'first_name': 'Mads',
        'last_name': 'Mikkelsen',
        'city': 'Oslo',
    },
}
for person, person_info in people.items():
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    city = f"{person_info['city']}"
    print(f"\nFull name: {full_name.title()} city: {city}.")
print("\n\n")

#6-8 Pets
pets = []

pet = {
    'Animal': 'Dog',
    'Owner': 'Ida',
}
pets.append(pet)

pet = {
    'Animal': 'cat',
    'Owner': 'Aurora',
}
pets.append(pet)

pet = {
    'Animal': 'spider',
    'Owner': 'Siri',
}
pets.append(pet)

pet = {
    'Animal': 'Horse',
    'Owner': 'Mathias',
}
pets.append(pet)

for dyr in pets:
    owner = dyr['Owner']
    pet = dyr['Animal']
    print(f"The {pet} is owned by {owner}.")
print("\n\n")

#6-9 Favorite Places
favourite_places = {
    'Ida': ['Gran', 'Maura', 'Oslo'],
    'Aurora': ['Amsterdam', 'Neverfjord'],
    'Joachim': ['Gjøvik']
}

for name, places in favourite_places.items():
    if len(places) < 2:
        for place in places:
            print(f"{name}'s favorite place is {place}.")
    else:
        print(f"{name}'s favorite places are ", end="")
        for place in places[:-1]:
            print(f"{place}, ", end="")
        print(f"and {places[-1]}.")

        #print(f"{name}'s fav place are {places[:-1]} and {places[-1]}")


