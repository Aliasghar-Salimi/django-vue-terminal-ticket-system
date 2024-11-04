from django.db import models
from cooperatives.models import Cooperatives
from django.utils.text import slugify
from account.models import User

class Vehicles(models.Model):
    cooperative = models.ForeignKey(Cooperatives, on_delete=models.CASCADE, verbose_name='تعاونی مربوطه')
    driver = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, verbose_name="راننده")
    license_plate = models.CharField(verbose_name="شماره پلاک", max_length=10, unique=True)
    model = models.IntegerField(verbose_name="سال تولید")
    capacity = models.SmallIntegerField(verbose_name="ضرفیت")
    vehicle_type = models.CharField(verbose_name="نوع ماشین", max_length=255)
    color = models.CharField(verbose_name="رنگ", max_length=254, null=True, blank=True)
    slug = models.SlugField(verbose_name="اسلاگ", unique=True, max_length=255)
    
    class Meta:
        db_table = "Vehicle"
        verbose_name = "ماشین"
        verbose_name_plural = "ماشین‌ها"

    def __str__(self):
        return str(self.vehicle_type) +" | "+ str(self.model)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.license_plate, allow_unicode=True)
        super(Vehicles, self).save(*args, **kwargs)

