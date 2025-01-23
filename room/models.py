from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator


class Equipment(models.Model):
    name = models.CharField(max_length=48, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Room(models.Model):
    class Level(models.TextChoices):
        STANDARD = "ST", "Standard"
        IMPROVED = "IM", "Improved"
        APARTMENT = "AP", "Apartment"
        STUDIO = "SD", "Studio"
        SUITE = "SI", "Suite"

    description = models.CharField(max_length=256, blank=True, null=False)
    cost = models.IntegerField(validators=[MinValueValidator(1)])
    square = models.DecimalField(decimal_places=1, max_digits=3)
    room_level = models.CharField(choices=Level.choices, default=Level.STANDARD)
    equipments = models.ManyToManyField('Equipment', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} {self.room_level}"
