from rest_framework import serializers
from .models import Reservations


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ['id', 'travel', 'leader_first_name', 'leader_last_name', 'leader_national_code', 'leader_phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')
        if request and request.method == 'GET':
            self.fields.update({
                'tracking_code' : serializers.IntegerField(),
                'slug' : serializers.SlugField(),
            })