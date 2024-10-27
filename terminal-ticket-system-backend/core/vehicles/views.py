from django.shortcuts import render
from .models import Vehicles, Drivers
from .serializers import VehiclesSerializer, DriversSerializer
from rest_framework import generics, filters

class VehiclesList(generics.ListCreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer
    search_fields = ['vehicle_type', 'license_plate']
    filter_backends = [filters.SearchFilter]

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer
    lookup_field = "slug"

class DriversList(generics.ListCreateAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer
    search_fields = ['first_name', 'last_name', 'national_code']
    filter_backends = [filters.SearchFilter]

class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer
    lookup_field = "slug"