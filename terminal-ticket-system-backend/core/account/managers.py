from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
from django.contrib.auth.password_validation import validate_password
import uuid

class CustomUserManager(BaseUserManager):

    def _create_user(self, phone_number, password=None, **extra_fields):
        email = extra_fields.get('email')
        email = self.normalize_email(email=email)

        if not phone_number:
            raise ValueError("شماره تلفن اجباری است")
        if not password:
            raise ValueError("رمز عبور اجباری است")

                
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user = self.model(
            phone_number=phone_number,
            email=email,
            **extra_fields
        )
        extra_fields.setdefault('id', uuid.uuid4())

        user.set_password(password)
        user.save()

        return user

    def create_user(self, phone_number, password, **extra_fields):
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self._create_user(phone_number, password, **extra_fields)

        