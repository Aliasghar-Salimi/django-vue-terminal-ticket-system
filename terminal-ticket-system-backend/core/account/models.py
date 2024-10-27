from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from .validators import phone_validator
from django.core.validators import validate_email

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True, validators=[phone_validator])
    email = models.CharField(max_length=254, validators=[validate_email], null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
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