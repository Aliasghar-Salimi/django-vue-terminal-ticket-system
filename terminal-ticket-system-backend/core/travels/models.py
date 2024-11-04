from django.db import models
from django.utils.text import slugify
from cooperatives.models import Cooperatives
from vehicles.models import Vehicles


class Provinces(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Province'
        verbose_name = 'province'
        verbose_name_plural = 'provinces'


class Cities(models.Model):
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'City'
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Travels(models.Model):
    status_choices = {
        'scheduled':'scheduled',
        'in_progress':'in_progress',
        'completed': 'completed',
    }
    cooperative = models.ForeignKey(Cooperatives, on_delete=models.CASCADE)
    province = models.OneToOneField(Provinces, on_delete=models.CASCADE)
    city = models.OneToOneField(Cities, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    status = models.CharField(max_length=128, choices=status_choices, default='scheduled')
    ticket_price = models.IntegerField()
    total_seats = models.SmallIntegerField()
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
