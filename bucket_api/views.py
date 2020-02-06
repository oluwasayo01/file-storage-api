from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BucketSerializer
from rest_framework import status

from .models import Bucketdb

class BucketView(APIView):
    def get(self, request):
        buckets = Bucketdb.objects.all()
        serializer = BucketSerializer(buckets,  many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = BucketSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)