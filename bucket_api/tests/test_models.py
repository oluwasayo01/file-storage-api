from django.test import TestCase
from bucket_api.models import Bucketdb

class BucketTestCase(TestCase):
    def setUp(self):
       self.bucket1 =  Bucketdb.objects.create(name="test bucket 1")
       self.dbcount = Bucketdb.objects.count()
       self.bucket1.save()

    def test_bucket_creation(self):
        self.assertEqual(Bucketdb.objects().count(),  self.dbcount + 1)

    def test_bucket_repr(self):
        self.assertEqual(self.bucket1.name, str(self.bucket1))