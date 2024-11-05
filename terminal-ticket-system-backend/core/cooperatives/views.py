from rest_framework import generics
from .models import Cooperatives
from .serializers import CooperativesSerializer
from rest_framework import filters, permissions

class CoopertivesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Cooperatives.objects.all()
    serializer_class = CooperativesSerializer
    search_fields = ['name', 'registration_code']
    filter_backends = [filters.SearchFilter]

class CoopertiveDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Cooperatives.objects.all()
    serializer_class = CooperativesSerializer
    lookup_field = "slug"
