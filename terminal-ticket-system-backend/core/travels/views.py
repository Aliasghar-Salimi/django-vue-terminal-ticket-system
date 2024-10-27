from .models import Cities
from .serializers import CitiesSerializer, TravelsSerializer
from rest_framework import generics, filters

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
    search_fields = ['destination']
    filter_backends = [filters.SearchFilter]

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cities.objects.all()
    serializer_class = TravelsSerializer
    lookup_field = "slug"