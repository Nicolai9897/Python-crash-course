# 4-1 Pizzas
pizzas = ["hawai", "pepperoni", 'margharitha']

for pizza in pizzas:
    print(f"jeg liker {pizza} pizza.")

print("Men egentlig, så liker jeg all pizza")
print()

# 4-2 Annimals:
animals = ['løve', 'tiger', 'Leopard', 'husholdningskatt', 'gris']

for animal in animals:
    print(f"En {animal} ville vært ett morsomt kjeledyr")

print("Alle disse dyrene er i katte familien")
print()

# 4-3 Counting to twenty
numbers = list(range(1, 21))

# for number in numbers:
# print(number)

# 4-4 One Million
millions = list(range(1, 1000001))
# for million in millions:
# print(million)

# 4-5 Summming a million
print(min(millions))
print(max(millions))
print(sum(millions))
print()

# 4-6 Odd numbers
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
print()

# 4-7 Threes
threes = list(range(3, 30, 3))
for three in threes:
    print(three)
print()

# 4-8 Cubes
values = list(range(1, 11))
for value in values:
    print(value**3)
print()

# 4-9 Cube comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)
print()

# 4-10 Slices
print("the first three animals in your #4-2 list are:")
print(animals[:3])
print("The three middle animals in your list are:")
print(animals[1:4])
print("The last three items in your list are")
print(animals[-3:])
print()

# 4-11 My pizzas, Your pizzas
friends_pizzas = pizzas[:]

pizzas.append('bbq')
friends_pizzas.append('chicken')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print()

print("my friends favorite pizzas are")
for friends_pizza in friends_pizzas:
    print(friends_pizza)
    print()

# 4-12 Buffet
buffet_foods = ("bread", "eggs", "fish", "hot_dogs", "chicken")

print("This restaurant offers these foods for your enjoyment:")
for food in buffet_foods:
    print(food)

# buffet_foods[0] = "pigs"

buffet_foods = ("bread", "eggs", "fish", "rice", "cheese")
print("this is our revised buffet menu:")
for food in buffet_foods:
    print(food)
