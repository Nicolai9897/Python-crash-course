class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_readin = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """print a statement showing a car's milage"""
        print(f"This car has {self.odometer_readin} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_readin:
            self.odometer_readin = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_readin += miles


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initilaize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

    def battery_upgrade(self):
        """checks the battery size, and upgrades it if its battery is applicable"""
        if self.battery_size == 75:
            self.battery_size = 100
        else:
            print("Battery type is not applicable for upgrade")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


bil = ElectricCar('Tesla', 'Model S', 2022)
bil.battery.describe_battery()
bil.battery.battery_upgrade()
bil.battery.describe_battery()
bil.battery.get_range()
bil.battery.battery_upgrade()