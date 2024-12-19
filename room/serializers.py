from rest_framework import serializers
from room.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'description', 'cost', 'square', 'room_level', 'equipments']
