from rest_framework import serializers
from .models import Cooperatives
from validations.validations import white_space_handler

class CooperativesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperatives
        fields = ['id', 'cooperative_manager', 'name', 'registration_code', 'phone_number', 'email']
        
    def validate(self, attrs):

        if 'name' in attrs:
            attrs["name"] = white_space_handler(attrs["name"])
            names = Cooperatives.objects.values_list('name', flat=True)
            if attrs['name'] in names:
                raise serializers.ValidationError({"name": "یک تعاونی با این نام وجود دارد"})

        return attrs 
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        request = self.context.get('request')
        if request and request.method == 'GET':
            self.fields.update({
                'phone_number': serializers.CharField(),
                'email': serializers.EmailField(),
                'vehicle_count': serializers.IntegerField(),
                'slug': serializers.SlugField(),
            })