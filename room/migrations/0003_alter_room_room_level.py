# Generated by Django 5.1.3 on 2024-11-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_rename_roommodel_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_level',
            field=models.CharField(choices=[('STANDARD', 'Standard'), ('IMPROVED', 'Improved'), ('APARTMENT', 'Apartment'), ('STUDIO', 'Studio'), ('SUITE', 'Suite')], default='STANDARD'),
        ),
    ]
