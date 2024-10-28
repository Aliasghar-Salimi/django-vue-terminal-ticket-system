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

class Drivers(models.Model):
    license_types = {
        'A-AM': "موتور",
        'B-B1':"پایه سوم",
        'C1-B1':"پایه دوم",
        'C-D-CE': "پایه یکم"
    }
    cooperative = models.ForeignKey(Cooperatives, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.SET_NULL, null=True)
    national_code = models.IntegerField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    license_number = models.IntegerField(unique=True , null=True, blank=True)
    license_issue_date = models.DateField(null=True, blank=True)
    license_expiry_date = models.DateField(null=True, blank=True)
    license_type = models.CharField(max_length=128,choices=license_types , null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        db_table = "Driver"
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.national_code, allow_unicode=True)
        super(Drivers, self).save(*args, **kwargs)
