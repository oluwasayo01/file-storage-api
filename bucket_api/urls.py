from django.urls import path
from .detail import BucketDetail
from .views import BucketView

urlpatterns = [
    path('buckets/', BucketView.as_view()),
    path('buckets/<int:pk>/', BucketDetail.as_view()),
]