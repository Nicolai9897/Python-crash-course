class Restaurant:
    """A class to represent a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize attributes to describe aa restaurant"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 5

    def describe_restaurant(self):
        """method for printing the restaurants information"""
        print(f"The restaurants name is {self.name}")
        print(f"The restaurants cuisins i {self.cuisine_type}")

    def open_restaurant(self):
        """method for opening the restaurant"""
        print(f"{self.name} is now open!")

    def set_number_served(self, number_of_people_served):
        """set the number of people served to a given value"""
        self.number_served = number_of_people_served

    def increase_number_served(self):
        """increments the number of visitors by a set amount"""
        self.number_served += 25


restaurant_1 = Restaurant('Khalle', 'burger')
print(restaurant_1.name)
print(restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print("------------------------------------------\n \n")

#9.2 Three restaurants
restaurant_2 = Restaurant('Heims', 'alkohol')
restaurant_3 =  Restaurant('mamma mia', ' pizza')

restaurant_2.describe_restaurant()
print("\n")
restaurant_3.describe_restaurant()
print("------------------------------------------\n \n")

#9-4 Number served
restaurant = Restaurant('BK', 'burger')
print(restaurant.number_served)

restaurant.set_number_served(15)
print(restaurant.number_served)

restaurant.increase_number_served()
restaurant.increase_number_served()
print(restaurant.number_served)
