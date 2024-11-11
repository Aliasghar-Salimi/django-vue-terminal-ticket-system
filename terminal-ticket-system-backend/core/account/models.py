from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from validations.validations import (iran_phone_validator,
                                    required_validator,
                                    no_space_validator,
                                    just_letter_validator,
                                    iranian_national_code_validator)
from django.core.validators import validate_email
from django.utils.text import slugify
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    role_choices = ((1, "Admin"),
                    (2, "Cooperative manager"),
                    (3, "Driver"))

    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    first_name = models.CharField(verbose_name="نام", max_length=60, null=True, 
                                  validators=[MinLengthValidator(3),
                                              just_letter_validator])
    
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=100, null=True, 
                                 validators=[MinLengthValidator(3),
                                             just_letter_validator])
    
    phone_number = models.CharField(verbose_name="شماره تلفن", max_length=12, unique=True, 
                                    validators=[iran_phone_validator,
                                                required_validator,
                                                no_space_validator])

    role = models.PositiveSmallIntegerField(choices=role_choices)
    email = models.CharField(verbose_name="ایمیل", max_length=254, validators=[validate_email], null=True)
    national_code = models.CharField(verbose_name="کد ملی", max_length=10, unique=True, null=True,
                                      validators=[iranian_national_code_validator])
    
    date_joined = models.DateTimeField(verbose_name="تاریخ ایجاد حساب", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="وضعیت فعالیت", default=True)
    is_superuser = models.BooleanField(verbose_name="وضعیت سوپر یوزری", default=False)
    is_staff = models.BooleanField(verbose_name="وضعیت کارمندی", default=False)
    slug = models.SlugField(verbose_name="اسلاگ", max_length=255, unique=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = "User"
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


    def __str__(self):
        if self.first_name != None and self.last_name != None:
            return str(self.first_name) + " " + str(self.last_name)
        elif self.email:
            return str(self.email).split('@')[0]
        else:
            return str(self.phone_number)
        
    def save(self, *args, **kwargs):
        if self.is_superuser == True:
            self.role = 1
        self.slug = slugify(self.phone_number)
        super(User, self).save(*args, **kwargs)
