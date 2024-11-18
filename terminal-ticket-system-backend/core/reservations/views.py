from rest_framework import generics, filters, permissions
from .models import Reservations, Cancelations
from .serializers import ReservationsSerializer, ReservationDetailSerializer, CancelationsSerializer

class ReservationsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
    search_fields = ['tracking_code', 'travel.destination']
    filter_backends = [filters.SearchFilter]

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'
    queryset = Reservations.objects.all()
    serializer_class = ReservationDetailSerializer
    
class CancelationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cancelations.objects.all()
    serializer_class = CancelationsSerializer
    search_fields = ['date']
    filter_backends = [filters.SearchFilter]