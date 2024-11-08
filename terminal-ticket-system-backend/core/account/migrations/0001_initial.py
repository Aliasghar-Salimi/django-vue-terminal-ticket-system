# Generated by Django 5.1.2 on 2024-11-08 17:48

import django.core.validators
import validations.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=60, null=True, validators=[django.core.validators.MinLengthValidator(3), validations.validations.just_letter_validator], verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(3), validations.validations.just_letter_validator], verbose_name='نام خانوادگی')),
                ('phone_number', models.CharField(max_length=12, unique=True, validators=[validations.validations.iran_phone_validator, validations.validations.required_validator, validations.validations.no_space_validator], verbose_name='شماره تلفن')),
                ('email', models.CharField(max_length=254, null=True, validators=[django.core.validators.EmailValidator()], verbose_name='ایمیل')),
                ('national_code', models.IntegerField(null=True, unique=True, verbose_name='کد ملی')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد حساب')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت فعالیت')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='وضعیت سوپر یوزری')),
                ('is_staff', models.BooleanField(default=False, verbose_name='وضعیت کارمندی')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='اسلاگ')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
                'db_table': 'User',
            },
        ),
    ]
