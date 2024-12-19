from rest_framework import serializers
from datetime import datetime
from booking.models import Booking
import pytz


class BookingSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['date_from'] > attrs['date_till']:
            raise serializers.ValidationError("Date from must be less than date till", code=400)

        if attrs['date_from'] < datetime.now(pytz.timezone('Etc/GMT+3')):
            raise serializers.ValidationError("Dates must be more than today", code=400)

        return attrs

    class Meta:
        model = Booking
        fields = ['id', 'room', 'date_from', 'date_till', 'user', 'price', 'created_at', 'updated_at']
        read_only_fields = ['user']
