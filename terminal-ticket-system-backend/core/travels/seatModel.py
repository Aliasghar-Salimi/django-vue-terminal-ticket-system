from django.db import models
from .models import Travels
from reservations.models import Reservations

class Seats(models.Model):
    seat_number = models.SmallIntegerField()
    reservation = models.ForeignKey(Reservations, on_delete=models.SET_NULL, null=True)
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Seat'
        verbose_name = 'seat'
        verbose_name_plural = 'seats'

    def __str__(self):
        return self.seat_number
    