from .models import Travels, Cities, Provinces
from rest_framework import serializers
from .seatModel import Seats

class TravelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = ['id', 'cooperative', 'vehicle', 'departure_time', 'return_time', 'status', 'ticket_price', 'province', 'city']

    def validate(self, attrs):
        start = attrs['departure_time']
        finish = attrs['return_time']

        if finish <= start:
            raise serializers.ValidationError('شروع و پایان سفر را منطقی تخمین بزنید')

        vehicle = attrs['vehicle']
        travels = Travels.objects.filter(vehicle=vehicle)

        for travel in travels:
            min = travel.departure_time

            max = travel.return_time

            if start >= min and start <= max or finish >= min and finish <= max:
                raise serializers.ValidationError('یک سفر برای این زمان تعریف شده')
            
        return attrs

    
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
