from django.db import models
from .models import Travels
from reservations.models import Reservations

class Seats(models.Model):
    seat_number = models.SmallIntegerField(verbose_name="شماره صندلی")
    reservation = models.ForeignKey(Reservations, on_delete=models.SET_NULL, null=True, verbose_name="رزرو مرطه")
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE, verbose_name="سفر مربوطه")

    class Meta:
        db_table = 'Seat'
        verbose_name = 'صندلی'
        verbose_name_plural = 'صندلی‌ها'

    def __str__(self):
        return self.seat_number
    