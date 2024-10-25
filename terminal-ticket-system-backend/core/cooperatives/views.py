from rest_framework import generics
from .models import Cooperatives
from .serializers import CooperativesSerializer

class CoopertivesList(generics.ListCreateAPIView):
    queryset = Cooperatives.objects.all()
    serializer_class = CooperativesSerializer

class CoopertiveDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cooperatives.objects.all()
    serializer_class = CooperativesSerializer
    lookup_field = "slug"
