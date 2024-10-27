from django.db import models
from django.utils.text import slugify
from cooperatives.models import Cooperatives
from vehicles.models import Vehicles


class Cities(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        db_table = 'City'
        verbose_name = "city"
        verbose_name_plural = "cities"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Cities, self).save(*args, **kwargs)

class Travels(models.Model):
    status_choices = {
        'scheduled':'scheduled',
        'in_progress':'in_progress',
        'completed': 'completed',
        'canceled':'canceled'
    }
    cooperative = models.ForeignKey(Cooperatives, on_delete=models.CASCADE)
    destination = models.ForeignKey(Cities, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    status = models.CharField(max_length=128, choices=status_choices, default='scheduled')
    ticket_price = models.IntegerField()
    total_seats = models.SmallIntegerField()
    # booked_seats = models.SmallIntegerField(null=True)
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        db_table = "Travel"
        verbose_name = "travle"
        verbose_name_plural = "travles"

    def __str__(self):
        return f"{str(self.destination)}-{str(self.departure_time)}"
    
    def save(self, *args, **kwargs):
        self.total_seats = self.vehicle.capacity
        self.slug = slugify(f"{self.destination.name}-{self.vehicle.vehicle_type}", allow_unicode=True)
        super(Travels, self).save(*args, **kwargs)


