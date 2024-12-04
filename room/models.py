from django.db import models
from django.contrib.postgres.fields import ArrayField


ROOM_LEVELS = {
    "STANDARD": "Standard",
    "IMPROVED": "Improved",
    "APARTMENT": "Apartment",
    "STUDIO": "Studio",
    "SUITE": "Suite",
}


class Room(models.Model):
    description = models.CharField()
    cost = models.IntegerField()
    square = models.DecimalField(decimal_places=1, max_digits=3)
    room_level = models.CharField(choices=ROOM_LEVELS, default='STANDARD')
    equipment = ArrayField(models.CharField(), null=False, blank=False)
