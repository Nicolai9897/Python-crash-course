from restaurant import *

restauranten = Restaurant('billy', 'regullation kiooosk')
restauranten.open_restaurant()
print("------------------------------------------\n \n")




restaurant_1 = Restaurant('Khalle', 'burger')
print(restaurant_1.name)
print(restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print("------------------------------------------\n \n")

# 9.2 Three restaurants
restaurant_2 = Restaurant('Heims', 'alkohol')
restaurant_3 = Restaurant('mamma mia', ' pizza')

restaurant_2.describe_restaurant()
print("\n")
restaurant_3.describe_restaurant()
print("------------------------------------------\n \n")

# 9-4 Number served
restaurant = Restaurant('BK', 'burger')
print(restaurant.number_served)

restaurant.set_number_served(15)
print(restaurant.number_served)

restaurant.increase_number_served()
restaurant.increase_number_served()
print(restaurant.number_served)
print("------------------------------------------\n \n")

# 9-6 Ice Cream Stand
isbar = IceCreamStand('funky is', 'iskrem')
isbar.display_flavors()

