from django.contrib import admin
from booking.models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ("room", "date_from", "date_till", "user", "price")
    list_filter = ("room", "date_from", "date_till", "user")
    fieldsets = (
        (None, {
            "fields": ("room", "user", "price")
        }),
        ("Dates", {
            "fields": ("date_from", "date_till")
        })
    )


admin.site.register(Booking, BookingAdmin)
