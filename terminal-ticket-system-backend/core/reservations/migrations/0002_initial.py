# Generated by Django 5.1.2 on 2024-11-08 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '0001_initial'),
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travels.travels', verbose_name='سفر مربوطه'),
        ),
    ]
