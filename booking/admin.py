from django.contrib import admin
from .models import Booking, Opening_booking, Booking_confirmation


class Opening_bookingAdmin(admin.ModelAdmin):
    list_display = ('academic_year', 'group', 'opening_day',
                    'closed_day', 'is_status')


class Booking_confirmationAdmin(admin.ModelAdmin):
    list_display = ('booking', 'is_confirmed', 'confirm_date')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'booking_at')


admin.site.register(Booking, BookingAdmin)
admin.site.register(Opening_booking, Opening_bookingAdmin)
admin.site.register(Booking_confirmation, Booking_confirmationAdmin)
