from .serializers import TravelsSerializer
from rest_framework import generics, filters
from .models import Travels

class TravelsList(generics.ListCreateAPIView):
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer
    search_fields = ['destination']
    filter_backends = [filters.SearchFilter]

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer
    lookup_field = "slug"