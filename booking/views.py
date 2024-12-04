from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsOwnerOrAdminBookingPermission
from .pagination import BookingPagination


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOrAdminBookingPermission]
    pagination_class = BookingPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.action == 'list' and not self.request.user.is_staff:
            return Booking.objects.filter(user=self.request.user)
        return Booking.objects.all()
