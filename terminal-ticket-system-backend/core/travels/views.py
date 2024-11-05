from .serializers import TravelsSerializer, CitiesSerializer, ProvincesSerializer
from rest_framework import generics, filters, permissions
from .models import Travels, Cities, Provinces

class TravelsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer
    search_fields = ['destination']
    filter_backends = [filters.SearchFilter]

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer
    lookup_field = "slug"

class ProvincesList(generics.ListAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]

class CitiesList(generics.ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    search_fields = ['name']
    filter_backends = [filters.SearchFilter]
