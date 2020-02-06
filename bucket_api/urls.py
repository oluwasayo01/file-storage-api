from django.urls import path
from .detail import BucketDetail
from .views import BucketView

urlpatterns = [
    path('buckets/', BucketView.as_view(), name='all_buckets'),
    path('buckets/<int:pk>/', BucketDetail.as_view()),
]