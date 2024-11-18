from .models import Travels, Cities, Provinces
from rest_framework import serializers
from .seatModel import Seats

class TravelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = ['id', 'cooperative', 'vehicle', 'departure_time', 'ticket_price', 'province', 'city']
    
class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = ['id', 'name']

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'name', 'province_id']

class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ['id', 'seat_number', 'travel', 'status', 'reservation']