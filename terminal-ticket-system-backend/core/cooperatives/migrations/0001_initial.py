# Generated by Django 5.1.2 on 2024-10-28 19:46

import account.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('registration_code', models.CharField(help_text='کد ثبت رسمی تعاونی', max_length=128, unique=True)),
                ('headquarter_address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, validators=[account.validators.phone_validator])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=255)),
                ('established_date', models.DateField(blank=True, null=True)),
                ('vehicle_count', models.IntegerField(default=0)),
                ('driver_count', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('cooperative_manager', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cooperative',
                'verbose_name_plural': 'cooperatives',
                'db_table': 'Cooperative',
            },
        ),
    ]
