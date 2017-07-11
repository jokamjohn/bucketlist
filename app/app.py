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
        pass
