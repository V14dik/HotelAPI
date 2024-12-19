# Generated by Django 5.1.3 on 2024-12-05 21:07

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_room_room_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='cost',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_level',
            field=models.CharField(choices=[('ST', 'Standard'), ('IM', 'Improved'), ('AP', 'Apartment'), ('SD', 'Studio'), ('SI', 'Suite')], default='ST'),
        ),
        migrations.AlterField(
            model_name='room',
            name='equipment',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(), blank=True, size=None),
        ),
    ]
