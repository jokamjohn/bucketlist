import random
import string

"""
This class handles User registration and login
"""


class Application:
    users = {}

    def register_user(self, user):
        """
        This methods checks whether a user already exists, if not
        the user is added registered by adding them to the dictionary otherwise
        False is returned.
        :param user: 
        :return: bool
        """
        if user.username in self.users.keys():
            return False
        else:
            self.users[user.username] = user
        return True

    def login_user(self, username, password):
        """
        This method logins in a user by first checking whether their passwords match. 
        Otherwise False is returned.
        :param username: str
        :param password: str
        :return: bool 
        """
        if self.users[username].password == password:
            return True
        return False

    def does_user_exist(self, username):
        """
        This method check whether the user already exists within the
        user dictionary.
        :param username: 
        :return: 
        """
        if username in self.users.keys():
            return True
        return False

    def generate_random_key(self):
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
