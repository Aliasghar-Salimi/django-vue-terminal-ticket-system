from django.urls import path
from .views import (TravelsList, TravelDetail, 
                    CitiesList, ProvincesList)

urlpatterns = [
    path('travels/', TravelsList.as_view(), name='travels'),
    path('travel/<slug:slug>/', TravelDetail.as_view(), name='travel'),
    path('provinces/', ProvincesList.as_view(), name='provinces'),
    path('cities/', CitiesList.as_view(), name='cities'),

]