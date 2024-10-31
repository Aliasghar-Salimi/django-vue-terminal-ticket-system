from django.db import models
from cooperatives.models import Cooperatives
from django.utils.text import slugify

class Vehicles(models.Model):
    cooperative = models.ForeignKey(Cooperatives, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=10, unique=True)
    model = models.IntegerField()
    capacity = models.SmallIntegerField()
    vehicle_type = models.CharField(max_length=255)
    color = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    
    class Meta:
        db_table = "Vehicle"
        verbose_name = "vehicle"
        verbose_name_plural = "vehicles"

    def __str__(self):
        return str(self.vehicle_type) +" | "+ str(self.model)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.license_plate, allow_unicode=True)
        super(Vehicles, self).save(*args, **kwargs)

