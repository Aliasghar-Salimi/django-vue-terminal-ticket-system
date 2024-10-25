from .models import Vehicles, Drivers
from rest_framework import serializers

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['id', 'cooperative', 'model', 'vehicle_type', 'capacity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')
        if request and request.method == 'GET':
            self.fields.update({'slug': serializers.CharField(), 
                                'color': serializers.CharField(),
                                'licanse_plate': serializers.CharField(),
                                })
            
class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = ['id', 'first_name', 'last_name', 'cooperative', 'vehicle', 'national_code']
