from django.urls import path
from .views import (TravelsList, TravelDetail)

urlpatterns = [
    path('travels/', TravelsList.as_view(), name='travels'),
    path('travel/<slug:slug>/', TravelDetail.as_view(), name='travel'),
]