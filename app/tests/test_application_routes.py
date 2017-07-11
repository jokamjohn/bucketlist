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
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_home_page_status_code(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")


if __name__ == '__main__':
    unittest.main()
