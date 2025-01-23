from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from datetime import datetime
import pytz

from booking.models import Booking
from booking.serializers import BookingSerializer
from booking.permissions import IsOwnerOrAdminBookingPermission
from booking.pagination import BookingPagination


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOrAdminBookingPermission]
    pagination_class = BookingPagination

    def perform_create(self, serializer):
        self.check_can_book()
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.action == 'list' and not self.request.user.is_staff:
            return Booking.objects.filter(user=self.request.user)
        return Booking.objects.all()

    def check_can_book(self):
        queryset = Booking.objects.filter(room=self.request.data['room'])
        date_from = datetime.strptime(self.request.data['date_from'], '%Y-%m-%d').replace(tzinfo=pytz.utc)
        date_till = datetime.strptime(self.request.data['date_till'], '%Y-%m-%d').replace(tzinfo=pytz.utc)
        for booking in queryset:
            if ((date_from >= booking.date_from) and (date_from <= booking.date_till)
                    or (date_till >= booking.date_from) and (date_till <= booking.date_till)):
                raise APIException(detail="Already booked", code=400)
