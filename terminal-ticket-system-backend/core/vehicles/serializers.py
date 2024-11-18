from .models import Vehicles
from rest_framework import serializers

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['id', 'cooperative', 'model', 'vehicle_type', 'capacity', 'licence_plate', 'driver']

            
