from django.urls import path
from .views import TripList

urlpatterns = [
    path('', TripList.as_view(), name='trip-list'),
]