from django.db import models
from travels.models import Travels
from validations.validations import (iran_phone_validator, required_validator, no_space_validator,
                                     just_letter_validator, iranian_national_code_validator)
from django.utils.text import slugify
import random
# from validations.validations import 
from django.core.validators import MinLengthValidator

class Reservations(models.Model):
    travel = models.ForeignKey(Travels, on_delete=models.CASCADE, verbose_name="سفر مربوطه")
    leader_first_name = models.CharField(verbose_name="نام سرپرست", max_length=60, 
                                         validators=[MinLengthValidator(3),
                                                     just_letter_validator])
    leader_last_name = models.CharField(verbose_name="نام خانوادگی", max_length=128,
                                        validators=[MinLengthValidator(3),
                                                    just_letter_validator])
    leader_phone_number = models.CharField(verbose_name="شماره سرپرست", max_length=12, 
                                           validators=[iran_phone_validator, 
                                                       required_validator, 
                                                       no_space_validator])
    leader_national_code = models.CharField(max_length=10, verbose_name="کدملی سرپرست", 
                                            validators=[iranian_national_code_validator])
    tracking_code = models.IntegerField(verbose_name="کد رهگیری", unique=True)
    slug = models.SlugField(verbose_name="اسلاگ", unique=True)

    class Meta:
        db_table = 'Reservation'
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزروها'

    def __str__(self):
        return self.tracking_code
    
    def save(self, *args, **kwagrs):
        self.tracking_code = random.randrange(100000, 999999)
        self.slug = slugify(self.tracking_code)
        super(Reservations, self).save(*args, **kwagrs)