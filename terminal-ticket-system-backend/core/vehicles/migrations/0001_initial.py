# Generated by Django 5.1.2 on 2024-10-28 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cooperatives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=10, unique=True)),
                ('model', models.IntegerField()),
                ('capacity', models.SmallIntegerField()),
                ('vehicle_type', models.CharField(max_length=255)),
                ('color', models.CharField(blank=True, max_length=254, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('cooperative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperatives.cooperatives')),
            ],
            options={
                'verbose_name': 'vehicle',
                'verbose_name_plural': 'vehicles',
                'db_table': 'Vehicle',
            },
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('national_code', models.IntegerField(unique=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('license_number', models.IntegerField(blank=True, null=True, unique=True)),
                ('license_issue_date', models.DateField(blank=True, null=True)),
                ('license_expiry_date', models.DateField(blank=True, null=True)),
                ('license_type', models.CharField(blank=True, choices=[('A-AM', 'موتور'), ('B-B1', 'پایه سوم'), ('C1-B1', 'پایه دوم'), ('C-D-CE', 'پایه یکم')], max_length=128, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cooperatives.cooperatives')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicles')),
            ],
            options={
                'verbose_name': 'driver',
                'verbose_name_plural': 'drivers',
                'db_table': 'Driver',
            },
        ),
    ]
