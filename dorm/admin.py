from django.contrib import admin
from .models import Dormitory, Room, Floor


# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('floor', 'room_id', 'room_type', 'amount', 'is_status')


admin.site.register(Dormitory)
admin.site.register(Room, RoomAdmin)
admin.site.register(Floor)
