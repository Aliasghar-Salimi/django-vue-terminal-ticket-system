from .models import Cities, Travels
from rest_framework import serializers


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'name']

class TravelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = ['id', 'cooperative', 'destination', 'vehicle', 'departure_time', 'ticket_price']