from django.shortcuts import render
from .models import Vehicles
from .serializers import VehicleSerializer
from rest_framework import generics

class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = "slug"
