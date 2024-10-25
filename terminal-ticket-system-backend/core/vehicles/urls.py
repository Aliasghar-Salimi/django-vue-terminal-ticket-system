from django.urls import path
from .views import (VehiclesList, VehicleDetail, 
                    DriversList, DriverDetail)

urlpatterns = [
    path('vehicles/', VehiclesList.as_view(), name='vehicles'),
    path('vehicle/<slug:slug>/', VehicleDetail.as_view(), name='vehicle'),
    path('drivers/', DriversList.as_view(), name='drivers'),
    path('driver/<slug:slug>/', DriverDetail.as_view(), name='driver'),
]