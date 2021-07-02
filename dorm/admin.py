from django.contrib import admin
from .models import Dormitory, Room, Floor


# Register your models here.

class DormitoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')


class FloorAdmin(admin.ModelAdmin):
    list_display = ('dorm_name', 'number')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('floor', 'room_id', 'room_type', 'amount', 'is_status')


admin.site.register(Dormitory, DormitoryAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Floor, FloorAdmin)
