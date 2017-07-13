import unittest
from app.models import User, Bucket


class TestUserBucket(unittest.TestCase):
    def setUp(self):
        self.user = User('jokamjohn', '123')

    def test_user_can_create_bucket(self):
        bucket = Bucket("AZXDJSA", "Travel")
        self.assertTrue(self.user.create_bucket(bucket))

    def test_user_bucket_already_exists(self):
        bucket = Bucket("AZXDJSA", "Travel")
        self.user.buckets = {"AZXDJSA": bucket}
        self.assertFalse(self.user.create_bucket(bucket))

    def test_a_bucket_is_returned_when_an_id_is_specified(self):
        bucket = Bucket("AZXDJSA", "Travel")
        self.user.buckets = {"AZXDJSA": bucket}
        self.assertEqual(self.user.get_bucket("AZXDJSA"), bucket)

    def test_none_is_returned_for_a_bucket_that_does_not_exist(self):
        self.assertIsNone(self.user.get_bucket("ABGDTAD"))

    def test_a_bucket_is_updated(self):
        bucket = Bucket("AZXDJSA", "Travel")
        self.user.buckets = {"AZXDJSA": bucket}
        self.user.update_bucket("AZXDJSA", 'Sleeping')
        self.assertEqual(self.user.get_bucket("AZXDJSA").name, "Sleeping")

    def test_the_bucket_to_be_updated_does_not_exist(self):
        self.assertFalse(self.user.update_bucket("BDBHGF", "Playing"))

    def test_a_bucket_is_successfully_deleted(self):
        bucket = Bucket("AZXDJSA", "Travel")
        self.user.buckets = {"AZXDJSA": bucket}
        self.user.delete_bucket("AZXDJSA")
        self.assertEqual(self.user.buckets, {})

    def test_false_is_returned_when_deleting_un_existing_bucket(self):
        self.assertFalse(self.user.delete_bucket("AZXDJSA"))

if __name__ == '__main__':
    unittest.main()
