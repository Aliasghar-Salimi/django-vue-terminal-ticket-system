from .models import Vehicles
from rest_framework import serializers

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ['id', 'cooperative', 'model', 'vehicle_type', 'capacity', 'license_plate']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')
        if request and request.method == 'GET':
            self.fields.update({'slug': serializers.CharField(), 
                                'color': serializers.CharField(),
                                'license_plate': serializers.CharField(),
                                })
            
