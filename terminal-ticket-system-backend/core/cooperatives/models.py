from django.db import models
from account.models import User
from validations.validations import (iran_phone_validator, required_validator, no_space_validator,
                                     white_space_handler, iranian_national_code_validator)
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django.core.validators import validate_email

class Cooperatives(models.Model):
    cooperative_manager = models.OneToOneField(User, on_delete=models.SET_NULL, 
                                               null=True, verbose_name="مدیر تعاونی")
    
    name = models.CharField(verbose_name="نام تعاونی", max_length=255, unique=True,
                            validators=[white_space_handler, MinLengthValidator(3)])
    
    registration_code = models.CharField(verbose_name="کد ثبت رسمی",
                                        max_length=128, 
                                        unique=True, help_text="کد ثبت رسمی تعاونی",
                                        validators=[no_space_validator,
                                        iranian_national_code_validator])
    
    phone_number = models.CharField(verbose_name="شماره تماس", max_length=12,
                                    validators=[iran_phone_validator, 
                                                required_validator, 
                                                no_space_validator,], null=True, blank=True)
    
    email = models.EmailField(verbose_name="ایمیل", max_length=254, null=True, blank=True, 
                              validators=[validate_email])
    
    vehicle_count = models.IntegerField(verbose_name="تعداد ماشین‌ها", default=0)
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

