from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from bucket_api.models import Bucketdb
from rest_framework import status

class BucketTests(APITestCase):
    def test_post_buckets(self):
        """
        Ensure we can create a new account bucket.
        """
        #building the url and data to be inserted
        url = reverse('all_buckets')
        data = {'name': 'The test bucket'}


        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bucketdb.objects.count(), 1)
        self.assertEqual(Bucketdb.objects.get().name, 'The test bucket')
    