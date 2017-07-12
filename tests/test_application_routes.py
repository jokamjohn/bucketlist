import unittest
from app import app


class TestApplicationRoutes(unittest.TestCase):
    """
    This class contains tests for the application routes.
    """

    def setUp(self):
        """
        This method activates the flask testing config flag, which disables
        error catching during request handling.
        The testing client always provided an interface to the application.
        :return: 
        """
        app.testing = True
        self.app = app.test_client()

    def test_home_status_code(self):
        response = self.app.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_home_page_status_code(self):
        response = self.app.get('/home', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_sign_up_page_status_code(self):
        response = self.app.get('/signup', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_login_page_status_code(self):
        response = self.app.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_sign_up_page_loads(self):
        response = self.app.get('/signup', content_type="html/text")
        self.assertTrue(b'Sign Up' in response.data)

    def test_login_page_loads(self):
        response = self.app.get('/login', content_type="html/text")
        self.assertTrue(b'Login' in response.data)

    def test_user_passwords_do_not_match_during_sign_up(self):
        data = {'name': 'john', 'username': 'jokamjohn', 'password': '123', 'password-confirmation': '234'}
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertIn(b'The passwords do not match', response.data)


if __name__ == '__main__':
    unittest.main()
