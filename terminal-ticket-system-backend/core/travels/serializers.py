from .models import Travels, Cities, Provinces
from rest_framework import serializers


class TravelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = ['id', 'cooperative', 'vehicle', 'departure_time', 'ticket_price']

class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = ['id', 'name']

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'name', 'province_id']
