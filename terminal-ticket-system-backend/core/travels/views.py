from .serializers import TravelsSerializer, CitiesSerializer, ProvincesSerializer, SeatsSerializer
from rest_framework import generics, filters, permissions
from .models import Travels, Cities, Provinces
from .seatModel import Seats
from vehicles.models import Vehicles

class TravelsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer
    search_fields = ['destination']
    filter_backends = [filters.SearchFilter]

    def perform_create(self, serializer):
        # Save the Travels instance
        travel = serializer.save()  # Corrected to use `serializer.save()`, not `self.create()`
        
        # Create seats based on vehicle capacity
        vehicle_capacity = travel.vehicle.capacity
        seats = [Seats(travel=travel, seat_number=i+1) for i in range(vehicle_capacity)]
        Seats.objects.bulk_create(seats)

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer
    lookup_field = "slug"

class SeatMap(generics.ListAPIView):
    serializer_class = SeatsSerializer

    def get_queryset(self):
            travel_id = self.kwargs['travel_id']
            return Seats.objects.filter(travel_id=travel_id)


class SeatsList(generics.ListAPIView):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer

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
