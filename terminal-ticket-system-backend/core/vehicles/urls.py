from django.urls import path
from .views import (VehiclesList, VehicleDetail)

urlpatterns = [
    path('vehicles/', VehiclesList.as_view(), name='vehicles'),
    path('vehicle/<slug:slug>/', VehicleDetail.as_view(), name='vehicle'),
]