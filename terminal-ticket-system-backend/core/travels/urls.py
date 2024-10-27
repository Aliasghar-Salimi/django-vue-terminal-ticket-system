from django.urls import path
from .views import (CitiesList, CityDetail, 
                    TravelsList, TravelDetail)

urlpatterns = [
    path('cities/', CitiesList.as_view(), name='cities'),
    path('city/<slug:slug>/', CityDetail.as_view(), name='city'),
    path('travels/', TravelsList.as_view(), name='travels'),
    path('travel/<slug:slug>/', TravelDetail.as_view(), name='travel'),
]