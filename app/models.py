class User:
    """
    User model class 
    """

    def __init__(self, username, password, name=None):
        self.username = username
        self.name = name
        self.password = password
        self.buckets = {}

    def create_bucket(self, bucket):
        if bucket.id in self.buckets.keys():
            return False
        else:
            self.buckets[bucket.id] = bucket
            return True

    def get_buckets(self):
        return self.buckets

    def get_bucket(self, bucket_id):
        if bucket_id in self.buckets.keys():
            return self.buckets[bucket_id]
        return None


class Bucket:
    """
    Bucket class
    """

    def __init__(self, bucket_id, name):
        self.id = bucket_id
        self.name = name
        self.items = {}

    def create_item(self, item):
        if item.id in self.items.keys():
            return False
        else:
            self.items[item.id] = item
            return True

    def get_items(self):
        return self.items


class BucketItem:
    """
    BucketItem class
    """

    def __init__(self, item_id, name, description, deadline):
        self.id = item_id
        self.name = name
        self.description = description
        self.deadline = deadline
