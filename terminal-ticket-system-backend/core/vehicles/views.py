from django.shortcuts import render
from .models import Vehicles
from .serializers import VehiclesSerializer
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
