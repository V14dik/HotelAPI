from django.contrib import admin
from room.models import Room, Equipment


class RoomAdmin(admin.ModelAdmin):
    list_display = ['description', 'room_level', 'square', 'cost']
    list_filter = ['room_level', 'square', 'cost']


admin.site.register(Room, RoomAdmin)
admin.site.register(Equipment)
