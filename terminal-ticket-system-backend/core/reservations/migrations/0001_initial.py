# Generated by Django 5.1.2 on 2024-11-08 17:48

import django.core.validators
import validations.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_first_name', models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(3), validations.validations.just_letter_validator], verbose_name='نام سرپرست')),
                ('leader_last_name', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(3), validations.validations.just_letter_validator], verbose_name='نام خانوادگی')),
                ('leader_phone_number', models.CharField(max_length=12, validators=[validations.validations.iran_phone_validator, validations.validations.required_validator, validations.validations.no_space_validator], verbose_name='شماره سرپرست')),
                ('leader_national_code', models.CharField(max_length=10, validators=[validations.validations.iranian_national_code_validator], verbose_name='کدملی سرپرست')),
                ('tracking_code', models.IntegerField(unique=True, verbose_name='کد رهگیری')),
                ('slug', models.SlugField(unique=True, verbose_name='اسلاگ')),
            ],
            options={
                'verbose_name': 'رزرو',
                'verbose_name_plural': 'رزروها',
                'db_table': 'Reservation',
            },
        ),
    ]
