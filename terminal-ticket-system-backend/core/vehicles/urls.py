from django.urls import path
from .views import (VehicleList, VehicleDetail)

urlpatterns = [
    path('vehicles/', VehicleList.as_view()),
    path('vehicle/<slug:slug>/', VehicleDetail.as_view()),
]