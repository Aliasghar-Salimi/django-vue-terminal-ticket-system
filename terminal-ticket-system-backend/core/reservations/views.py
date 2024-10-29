from rest_framework import generics, filters
from .models import Reservations
from .serializers import ReservationsSerializer 

class ReservationsList(generics.ListCreateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    search_fields = ['tracking_code', 'travel.destination']
    filter_backends = [filters.SearchFilter]

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    
