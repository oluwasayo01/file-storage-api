from rest_framework import serializers
from .models import Bucketdb

class BucketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bucketdb
        fields = '__all__'