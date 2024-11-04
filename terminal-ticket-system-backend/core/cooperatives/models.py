from django.db import models
from account.models import User
from account.validators import phone_validator
from django.utils.text import slugify
from django.core.validators import validate_email

class Cooperatives(models.Model):
    cooperative_manager = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, verbose_name="مدیر تعاونی")
    name = models.CharField(verbose_name="نام تعاونی", max_length=255, unique=True)
    registration_code = models.CharField(verbose_name="کد ثبت رسمی", max_length=128, unique=True, help_text="کد ثبت رسمی تعاونی")
    # headquarter_address = models.CharField(verbose_name="", max_length=255, null=True, blank=True)
    phone_number = models.CharField(verbose_name="شماره تماس", max_length=12, validators=[phone_validator], null=True, blank=True)
    email = models.EmailField(verbose_name="ایمیل", max_length=254, null=True, blank=True, validators=[validate_email])
    # established_date = models.DateField(verbose_name="", null=True, blank=True)
    vehicle_count = models.IntegerField(verbose_name="تعداد ماشین‌ها", default=0)
    driver_count = models.IntegerField(verbose_name="تعداد رانندگان", default=0)
    slug = models.SlugField(verbose_name="اسلاگ", max_length=255, unique=True)

    class Meta:
        db_table = "Cooperative"
        verbose_name = "تعاونی"
        verbose_name_plural = "تعاونی‌ها"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Cooperatives, self).save(*args, **kwargs)

