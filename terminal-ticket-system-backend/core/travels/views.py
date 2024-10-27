from .models import Cities
from .serializers import CitiesSerializer, TravelsSerializer
from rest_framework import generics

# Create your views here.

class CitiesList(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    lookup_field = "slug"

class TravelsList(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = TravelsSerializer

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = TravelsSerializer
    lookup_field = "slug"