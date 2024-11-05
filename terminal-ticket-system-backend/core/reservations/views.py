from rest_framework import generics, filters, permissions
from .models import Reservations
from .serializers import ReservationsSerializer 

class ReservationsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    search_fields = ['tracking_code', 'travel.destination']
    filter_backends = [filters.SearchFilter]

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    
