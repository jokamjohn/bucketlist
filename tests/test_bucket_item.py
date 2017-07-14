import unittest
from app.models import Bucket
from app.models import BucketItem


class TestBucketItems(unittest.TestCase):
    def setUp(self):
        self.bucket = Bucket("AZXDJSA", "Travel")

    def test_user_can_create_bucket(self):
        item = BucketItem('XZBNVLK', 'Kampala', 'Find Baganda', '2017-07-27')
        self.assertTrue(self.bucket.create_item(item))

    def test_item_already_exists_in_the_bucket(self):
        item = BucketItem('XZBNVLK', 'Kampala', 'Find Baganda', '2017-07-27')
        self.bucket.items = {'XZBNVLK': item}
        self.assertFalse(self.bucket.create_item(item))

    def test_an_item_in_the_bucket_is_returned_when_an_id_is_specified(self):
        item = BucketItem('XZBNVLK', 'Kampala', 'Find Baganda', '2017-07-27')
        self.bucket.items = {'XZBNVLK': item}
        self.assertEqual(self.bucket.get_item(item.id), item)

    def test_none_is_returned_when_an_item_is_not_found_by_its_id(self):
        self.assertIsNone(self.bucket.get_item("VBDHJFS"))

    def test_that_an_item_in_a_bucket_is_updated(self):
        item = BucketItem('XZBNVLK', 'Kampala', 'Find Baganda', '2017-07-27')
        self.bucket.items = {'XZBNVLK': item}
        self.bucket.update_item('XZBNVLK', 'Nairobi', "Find Baganda", '2017-07-27')
        self.assertEqual(self.bucket.get_item('XZBNVLK').name, 'Nairobi')

    def test_item_to_be_updated_is_missing(self):
        self.assertFalse(self.bucket.update_item('AGHGJC', 'Kampala', 'Find Baganda', '2017-07-27'))

    def test_item_is_successfully_deleted(self):
        item = BucketItem('XZBNVLK', 'Kampala', 'Find Baganda', '2017-07-27')
        self.bucket.items = {'XZBNVLK': item}
        self.bucket.delete_item('XZBNVLK')
        self.assertEqual(self.bucket.items, {})

    def test_an_item_that_does_not_exist_cannot_be_deleted(self):
        self.assertFalse(self.bucket.delete_item("HJJJFG"))


if __name__ == '__main':
    unittest.main()
