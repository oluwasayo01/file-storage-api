from rest_framework.views import APIView
from rest_framework import status
from .models import Bucketdb
from .serializers import BucketSerializer
from rest_framework.response import Response

class BucketDetail(APIView):
    """
    Retrieve, update or delete a bucket instance.
    """
    def get_object(self, pk):
        try:
            return Bucketdb.objects.get(pk=pk)
        except Bucketdb.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format='json'):
        bucket = self.get_object(pk)
        serializer = BucketSerializer(bucket)
        return Response(serializer.data)

    def put(self, request, pk, format='json'):
        bucket = self.get_object(pk)
        serializer = BucketSerializer(bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format='json'):
        bucket = self.get_object(pk)
        bucket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)