class User:
    """A class representing a typical user in a program"""

    def __init__(self, first_name, last_name, age, gender, height, weight):
        """Initializable attributes to describe the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.login_attempts = 0

    def describe_user(self):
        """method for describing the induvidual user"""
        print(f"Name = {self.first_name.title()} {self.last_name.title()}")
        print(f"Gender = {self.gender.title()}")
        print(f"'age = {self.age}")
        print(f"Height = {self.height}")
        print(f"Weight = {self.weight}")

    def greet_user(self):
        """methods for greeting the user who is logging in"""
        print(f"Hello the {self.gender} {self.first_name.title()} "
              f"{self.last_name.title()}. Glad to have you here!")

    def increase_login_attempts(self):
        """increment the number of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets the amount of login attempts to 0"""
        self.login_attempts = 0


user_1 = User('Nicolai', 'Olsen', 25, 'Male', 189, 75)
user_2 = User('John', 'ollerud', 35, 'female', 155, 55)
user_3 = User('alfred', 'Hansen', 65, 'Male', 210, 110)

user_1.describe_user()
user_1.greet_user()
print("\n")

user_2.describe_user()
user_2.greet_user()
print("\n")

user_3.describe_user()
user_3.greet_user()
print("------------------------------------------\n \n")

#9-5 Login attempts
login_user = User('bruker', 'brukersen', 15, 'male', 154, 57)
print(login_user.login_attempts)
login_user.increase_login_attempts()
login_user.increase_login_attempts()
login_user.increase_login_attempts()
login_user.increase_login_attempts()
print(login_user.login_attempts)

login_user.reset_login_attempts()
print(login_user.login_attempts)