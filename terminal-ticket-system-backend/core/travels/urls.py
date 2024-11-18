from django.urls import path, re_path
from .views import (TravelsList, TravelDetail, 
                    CitiesList, ProvincesList,
                    SeatsList)

urlpatterns = [
    path('travels/', TravelsList.as_view(), name='travels'),
    re_path('travel/(?P<slug>[-\w]+)/', TravelDetail.as_view(), name='travel'),
    path('seats/', SeatsList.as_view(), name='seats'),
    path('provinces/', ProvincesList.as_view(), name='provinces'),
    path('cities/', CitiesList.as_view(), name='cities'),

]