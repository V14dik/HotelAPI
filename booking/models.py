from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from room.models import Room


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_from = models.DateTimeField()
    date_till = models.DateTimeField()
    price = models.IntegerField(validators=[MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.room} {self.date_from}'
