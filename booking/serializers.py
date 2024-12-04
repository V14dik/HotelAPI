from rest_framework import serializers
from datetime import date
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['date_from'] > attrs['date_till']:
            raise serializers.ValidationError("Date from must be more than date till", code=400)

        if attrs['date_from'] < date.today():
            raise serializers.ValidationError("Dates must be more than today", code=400)

        queryset = Booking.objects.filter(room=attrs['room'])
        for booking in queryset:
            if ((attrs['date_from'] > booking.date_from) and (attrs['date_from'] < booking.date_till)
                    or (attrs['date_till'] > booking.date_from) and (attrs['date_till'] < booking.date_till)):
                raise serializers.ValidationError("Already booked", code=400)

        return attrs

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user']
