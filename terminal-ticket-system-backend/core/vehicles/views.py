from django.shortcuts import render
from .models import Vehicles, Drivers
from .serializers import VehiclesSerializer, DriversSerializer
from rest_framework import generics

class VehiclesList(generics.ListCreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer
    lookup_field = "slug"

class DriversList(generics.ListCreateAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer

class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer
    lookup_field = "slug"