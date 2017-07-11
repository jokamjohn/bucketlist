import unittest
from app.user import User
from app.app import Application


class TestUserAuthentication(unittest.TestCase):
    """
    Class to test the user authentication, both the registration
    and login.
    """

    def setUp(self):
        self.user = User('John', 'jokamjohn', '123456')
        self.app = Application()

    def test_user_is_added_to_dictionary_when_created(self):
        return self.assertTrue(self.app.register_user(self.user))

    def test_user_already_exists_in_user_dictionary(self):
        self.app.users = {'jokamjohn': self.user}
        return self.assertFalse(self.app.register_user(self.user))

    def test_user_sigining_in_is_already_registered(self):
        self.app.users = {'jokamjohn': self.user}
        return self.assertTrue(self.app.login_user('jokamjohn', '123456'))

    def test_user_trying_to_login_has_entered_a_wrong_password(self):
        self.app.users = {'jokamjohn': self.user}
        return self.assertFalse(self.app.login_user('jokamjohn', 'sdfgdsfj'))


if __name__ == '__main__':
    unittest.main()
