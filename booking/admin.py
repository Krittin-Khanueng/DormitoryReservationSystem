from django.contrib import admin
from .models import Booking, Opening_booking, Room_confirmation


class Opening_bookingAdmin(admin.ModelAdmin):
    list_display = ('academic_year', 'group', 'opening_day',
                    'closed_day', 'is_status')


class Room_confirmationAdmin(admin.ModelAdmin):
    list_display = ('booking', 'is_confirmation', 'date')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'date')


admin.site.register(Booking, BookingAdmin)
admin.site.register(Opening_booking, Opening_bookingAdmin)
admin.site.register(Room_confirmation, Room_confirmationAdmin)
