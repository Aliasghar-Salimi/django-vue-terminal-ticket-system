from django.urls import path, re_path
from .views import (VehiclesList, VehicleDetail)

urlpatterns = [
    path('vehicles/', VehiclesList.as_view(), name='vehicles'),
    re_path('vehicle/(?P<slug>[-\w]+)/', VehicleDetail.as_view(), name='vehicle'),
]