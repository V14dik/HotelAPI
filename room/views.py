from django.shortcuts import render
from rest_framework import viewsets

from .permissions import IsAdminOrReadOnly
from .models import Room
from .serializers import RoomSerializer
from .pagination import RoomPagination

# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = RoomPagination
