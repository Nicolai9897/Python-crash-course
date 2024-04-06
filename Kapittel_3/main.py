names = ['Ida', 'aurora', 'Nicolai', 'Thomas']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print()

message = "Hello "
print(f"{message}{names[0]}, good to see you!")
print(f"{message}{names[1]}, good to see you!")
print(f"{message}{names[2]}, good to see you!")
print(f"{message}{names[3]}, good to see you!")
print()

# 3-4 Guest List
guest_list = ['Albert Einstein', 'Leo DiCapiro', 'Taylor Swift', 'Barack Obama']
print(f"Hei {guest_list[0].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[1].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[2].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[3].title()}, vil du komme til middag imorgen?")
print()

# 3-5 Changing Guest List
print(f"{guest_list[0].title()} Kan ikke komme allikevel. Det viser seg at han er død")
del guest_list[0]
guest_list.insert(0, "Jens Stoltenberg")

print(f"Hei {guest_list[0].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[1].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[2].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[3].title()}, vil du komme til middag imorgen?")
print()

# 3-6 More guests:
print("Hei alle sammen. Jeg fant ett større bord, så flere kan nå komme til middag!")
guest_list.insert(0, "joe biden")
guest_list.insert(2, "Donald Trump")
guest_list.append("Hillary Clinton")

print(f"Hei {guest_list[0].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[1].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[2].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[3].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[4].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[5].title()}, vil du komme til middag imorgen?")
print(f"Hei {guest_list[6].title()}, vil du komme til middag imorgen?")
print()

# 3-7 Shrinking guest list:
print("Walla folkens. Bordet kommer ikke i tide, så jeg må dessverre yeete noen av dere fra middagen.")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, jeg beklager, men du er yeeted")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, jeg beklager, men du er yeeted")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, jeg beklager, men du er yeeted")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, jeg beklager, men du er yeeted")
popped_guests = guest_list.pop()
print(f"{popped_guests.title()}, jeg beklager, men du er yeeted")
print(f"Hei {guest_list[0].title()}, Du er fortsatt invitert brushan")
print(f"Hei {guest_list[1].title()}, Du er fortsatt invitert brushan")
del guest_list[0]
del guest_list[0]
print(guest_list)
print()

#"bevis" på at sort sorterer egentlig etter ascii tall
cars = ["BMW", "Audi", "Merce", "bmw", "audi", "merce"]
print(sorted(cars))
print(cars)
print()

#3-8 Seeing the world:
places_to_visit = ["Paris", "Amsterdam", "Berlin", "Roma", "New York", "St.Helena"]
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)
print()

#3-9 Dinner guests
print(len(places_to_visit))
print()
print()


#3.10 Every function
list = ["biler", "gardiner", 'håndkler', 'kjøtt', 'pizza']
print(list)

popped_list = list.pop()
print (f"\n{list}")
print(popped_list)
print()

list.append("obama")
print(list)
print()

del list[1]
print(list)
print()

list.insert(1, "pannekaker")
print(list)
print()

print(sorted(list, reverse=True))
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.sort(reverse=True)
print(list)
list.sort(reverse=False)
print(list)