# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Dormitory, Floor, Room


@admin.register(Dormitory)
class DormitoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'images',
        'images_room_plan',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('id', 'dorm_name', 'number')
    list_filter = ('dorm_name',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'floor',
        'room_id',
        'room_type',
        'amount',
        'is_status',
    )
    list_filter = ('floor', 'is_status')
