from .models import Travels
from rest_framework import serializers


class TravelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = ['id', 'cooperative', 'destination', 'vehicle', 'departure_time', 'ticket_price']