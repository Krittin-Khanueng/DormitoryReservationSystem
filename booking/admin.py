from django.contrib import admin
from .models import Booking, Opening_booking


class Opening_bookingAdmin(admin.ModelAdmin):
    list_display = ('academic_year', 'group', 'opening_day', 'closed_day', 'is_status')





class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'booking_at')


admin.site.register(Booking, BookingAdmin)
admin.site.register(Opening_booking, Opening_bookingAdmin)

