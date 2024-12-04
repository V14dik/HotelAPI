from django.db import models
from django.contrib.auth.models import User
from room.models import Room


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_till = models.DateField()
    price = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
