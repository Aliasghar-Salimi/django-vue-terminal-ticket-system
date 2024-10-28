from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .validators import phone_validator, password_validator
import re


class CustomUserManager(BaseUserManager):

    def create_user(self, phone_number, password, **extra_fields):
        email = extra_fields.get('email')

        if not phone_number:
            raise ValueError("the phone number must be set")
        if not password:
            raise ValueError("the password must be set")

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user = self.model(
            phone_number=phone_number,
            email=email,
            **extra_fields
        )

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, phone_number, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        user = self.create_user(phone_number, password, **extra_fields)

        user.save()

        return user

        