from rest_framework import serializers
from .models import Cooperatives

class CooperativesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperatives
        fields = ['id', 'cooperative_manager', 'name', 'registration_code']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Check if the context has the request and if the method is GET
        request = self.context.get('request')
        if request and request.method == 'GET':
            # For GET requests, include all fields
            self.fields.update({
                'headquarter_address': serializers.CharField(),
                'phone_number': serializers.CharField(),
                'email': serializers.EmailField(),
                'status': serializers.CharField(),
                'established_date': serializers.DateField(),
                'vehicle_count': serializers.IntegerField(),
                'driver_count': serializers.IntegerField(),
                'slug': serializers.SlugField(),
            })