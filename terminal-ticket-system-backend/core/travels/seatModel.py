from django.db import models
from .models import Travels


class Seats(models.Model):
    reservation = models.ForeignKey('reservations.Reservations', on_delete=models.SET_NULL, null=True, blank=True, related_name="seats", verbose_name="رزرو مربوطه")
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE, verbose_name="سفر مربوطه")
    seat_number = models.SmallIntegerField(verbose_name="شماره صندلی")
    status = models.BooleanField(default=0)


    class Meta: 
        db_table = 'Seat'
        verbose_name = 'صندلی'
        verbose_name_plural = 'صندلی‌ها'

    def __str__(self):
        return str(self.seat_number)
    