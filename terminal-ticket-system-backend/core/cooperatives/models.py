from django.db import models
from account.models import User
from account.validators import phone_validator
from django.utils.text import slugify

class Cooperatives(models.Model):
    activity_status = (
        ('active', 'active'),
        ('inactive', 'inactive')
    )
    cooperative_manager = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, unique=True)
    registration_code = models.CharField(max_length=128, unique=True, help_text="کد ثبت رسمی تعاونی")
    headquarter_address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=12, validators=[phone_validator], null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    status = models.CharField(choices=activity_status, max_length=255, default='active')
    established_date = models.DateField(null=True, blank=True)
    vehicle_count = models.IntegerField(default=0)
    driver_count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = "Cooperative"
        verbose_name = "cooperative"
        verbose_name_plural = "cooperatives"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Cooperatives, self).save(*args, **kwargs)

