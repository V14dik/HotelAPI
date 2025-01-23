from rest_framework import viewsets

from room.permissions import IsAdminOrReadOnly
from room.models import Room, Equipment
from room.serializers import RoomSerializer
from room.pagination import RoomPagination


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = RoomPagination

    def perform_create(self, serializer):
        equipments_inst = self.request.data["equipments_inst"]
        equipments = []
        for eq in equipments_inst:
            equipment = Equipment.objects.get_or_create(name=eq["name"].strip())
            equipments.append(equipment[0].id)
        serializer.save(equipments=equipments)
