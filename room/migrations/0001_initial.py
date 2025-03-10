# Generated by Django 5.1.3 on 2024-11-29 11:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('cost', models.IntegerField()),
                ('square', models.DecimalField(decimal_places=1, max_digits=3)),
                ('room_level', models.CharField(choices=[('STANDARD', 'Standard'), ('IMPROVED', 'Improved'), ('APARTMENT', 'Apartment'), ('STUDIO', 'Studio'), ('SUITE', 'Suite')])),
                ('equipment', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), size=None)),
            ],
        ),
    ]
