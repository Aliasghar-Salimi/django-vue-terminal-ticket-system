from rest_framework import serializers
from .models import Reservations
from travels.seatModel import Seats
from django.db import transaction
from validations.validations import white_space_handler

class ReservationsSerializer(serializers.ModelSerializer):
    seats = serializers.ListField(
        child=serializers.IntegerField(), 
        write_only=True,
        required=True,
        help_text="لیست آی دی‌ها برای رزرو شدن"
    )

    class Meta:
        model = Reservations
        fields = ['id', 'travel', 'leader_first_name', 'leader_last_name',
                   'leader_national_code', 'leader_phone_number', 'seats']
    
    def validate(self, attrs):
        if 'leader_first_name' in attrs:
            attrs['leader_first_name'] = white_space_handler(attrs['leader_first_name'])
        if 'leader_last_name' in attrs:
            attrs['leader_last_name'] = white_space_handler(attrs['leader_last_name'])

        return attrs
  
    def validate_seats(self, seat_ids):
        travel = self.initial_data.get('travel')
        seats = Seats.objects.filter(id__in=seat_ids, travel_id=travel, status=False)

        if len(seats) != len(seat_ids):
            raise serializers.ValidationError("یک یا چند صندلی نامعتبرند یا قبلا رزرو شدند")

        return seat_ids

    def create(self, validated_data):
        seat_ids = validated_data.pop('seats')
        travel = validated_data['travel']

        with transaction.atomic():
            reservation = Reservations.objects.create(**validated_data)
            seats_updated = Seats.objects.filter(id__in=seat_ids, travel=travel).update(status=True, reservation=reservation)
            if seats_updated != len(seat_ids):
                raise serializers.ValidationError("رزرو همه صندلی‌ها ناموفق بود. لطفا دوباره سعی کنید")

        return reservation

    def to_representation(self, instance):
        data = super().to_representation(instance)
        reserved_seats = instance.seats.filter(reservation=instance)
        data['reserved_seats'] = [seat.seat_number for seat in reserved_seats]
        return data
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')
        if request and request.method == 'GET':
            self.fields.update({
                'tracking_code' : serializers.IntegerField(),
                'slug' : serializers.SlugField(),
            })

class ReservationDetailSerializer(serializers.ModelSerializer):
    seats = serializers.ListField(
        child=serializers.IntegerField(), 
        write_only=True,
        required=False,
        help_text="لیست آی دی‌ها برای به‌روزرسانی رزرو"
    )

    class Meta:
        model = Reservations
        fields = ['id', 'travel', 'leader_first_name', 'leader_last_name',
                   'leader_national_code', 'leader_phone_number', 'seats']
    
    def update(self, instance, validated_data):
        seat_ids = validated_data.pop('seats', None)
        travel = validated_data.get('travel', instance.travel)

        with transaction.atomic():
            instance.seats.update(status=False, reservation=None)

            if seat_ids:
                seats_updated = Seats.objects.filter(id__in=seat_ids, travel=travel).update(status=True, reservation=instance)
                if seats_updated != len(seat_ids):
                    raise serializers.ValidationError("رزرو همه صندلی‌ها ناموفق بود. لطفا دوباره سعی کنید")

            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()

        return instance
