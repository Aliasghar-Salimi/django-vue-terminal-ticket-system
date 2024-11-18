# Generated by Django 5.1.2 on 2024-11-18 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cooperatives', '0001_initial'),
        ('reservations', '0001_initial'),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام استان')),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'استان\u200cها',
                'db_table': 'Province',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام شهر')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.provinces', verbose_name='استان مربوطه')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهرها',
                'db_table': 'City',
            },
        ),
        migrations.CreateModel(
            name='Travels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('departure_time', models.DateTimeField(verbose_name='زمان حرکت')),
                ('ticket_price', models.IntegerField(verbose_name='قیمت بلیط')),
                ('total_seats', models.SmallIntegerField(verbose_name='تعداد کل صندلی\u200cها')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='اسلاگ')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.cities', verbose_name='شهر')),
                ('cooperative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperatives.cooperatives', verbose_name='تعاونی')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.provinces', verbose_name='استان')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles', verbose_name='ماشین')),
            ],
            options={
                'verbose_name': 'سفر',
                'verbose_name_plural': 'سفرها',
                'db_table': 'Travel',
            },
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.SmallIntegerField(verbose_name='شماره صندلی')),
                ('status', models.BooleanField(default=0)),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seats', to='reservations.reservations', verbose_name='رزرو مربوطه')),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.travels', verbose_name='سفر مربوطه')),
            ],
            options={
                'verbose_name': 'صندلی',
                'verbose_name_plural': 'صندلی\u200cها',
                'db_table': 'Seat',
            },
        ),
    ]
