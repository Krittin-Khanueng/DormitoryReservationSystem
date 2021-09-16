# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Opening_booking, Booking, Booking_confirmation, Academic_year


@admin.register(Opening_booking)
class Opening_bookingAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'academic_year',
		'group',
		'opening_day',
		'closed_day',
		'is_status',
		'created_at',
	)
	list_filter = (
		'group',
		'opening_day',
		'closed_day',
		'is_status',
		'created_at',
	)
	date_hierarchy = 'created_at'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ('id', 'room', 'user', 'booking_at', 'open_booking')
	list_filter = ('room', 'user', 'booking_at', 'open_booking')


@admin.register(Booking_confirmation)
class Booking_confirmationAdmin(admin.ModelAdmin):
	list_display = ('id', 'booking', 'is_confirmed', 'confirm_date')
	list_filter = ('booking', 'is_confirmed', 'confirm_date')


@admin.register(Academic_year)
class Academic_yearAdmin(admin.ModelAdmin):
	list_display = ('id', 'academic_year',)
