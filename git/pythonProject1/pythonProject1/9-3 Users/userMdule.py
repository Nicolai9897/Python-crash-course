"""Module for representing a user."""
from userClass import User

class Privileges:
    """Cless for representing the privileges a user can have"""

    def __init__(self, privileges=[
        'can add posts', 'can delete posts', 'can ban users', 'can stalk users'
    ]):
        """initialize the priviliges class with its attributes"""
        self.privileges = privileges

    def show_privileges(self):
        print("the administrators special privelages are the following:")
        print(self.privileges)


class Admin(User):
    """an admin subclass of the user superclass"""

    def __init__(self, first_name, last_name, age, gender, height, weight):
        """initiate the super class, then the admin spesific attributes"""
        super().__init__(first_name, last_name, age, gender, height, weight)
        self.privileges = Privileges()
