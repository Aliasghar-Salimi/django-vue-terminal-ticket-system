from django.db import models
from django.utils.text import slugify
from cooperatives.models import Cooperatives
from vehicles.models import Vehicles


class Provinces(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام استان")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Province'
        verbose_name = 'استان'
        verbose_name_plural = 'استان‌ها'


class Cities(models.Model):
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE, verbose_name="استان مربوطه")
    name = models.CharField(max_length=255, verbose_name="نام شهر")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'City'
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'


class Travels(models.Model):
    cooperative = models.ForeignKey(Cooperatives, on_delete=models.CASCADE, verbose_name="تعاونی")
    province = models.OneToOneField(Provinces, on_delete=models.CASCADE, verbose_name="استان")
    city = models.OneToOneField(Cities, on_delete=models.CASCADE, verbose_name="شهر")
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE, verbose_name="ماشین")
    departure_time = models.DateTimeField(verbose_name="زمان حرکت")
    ticket_price = models.IntegerField(verbose_name="قیمت بلیط")
    total_seats = models.SmallIntegerField(verbose_name="تعداد کل صندلی‌ها")
    slug = models.SlugField(verbose_name="اسلاگ", unique=True, max_length=255)

    class Meta:
        db_table = "Travel"
        verbose_name = "سفر"
        verbose_name_plural = "سفرها"

    def __str__(self):
        return f"{str(self.destination)}-{str(self.departure_time)}"
    
    def save(self, *args, **kwargs):
        self.total_seats = self.vehicle.capacity
        self.slug = slugify(f"{self.destination.name}-{self.vehicle.vehicle_type}", allow_unicode=True)
        super(Travels, self).save(*args, **kwargs)
