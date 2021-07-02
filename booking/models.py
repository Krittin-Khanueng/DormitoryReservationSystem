import uuid

from django.contrib.auth.models import User, Group
from django.db import models
from dorm.models import Room


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='booking_room',
                             verbose_name="เลขห้อง")
    user = models.ManyToManyField(User, verbose_name="คนจอง")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ห้อง:{self.room.room_id}"


class Room_confirmation(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="booking_confirm", null=True)
    is_confirmation = models.BooleanField(null=True, verbose_name="สถานะการยืนยัน")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ห้อง:{self.booking.room.room_id} สถานะการยืนยัน:{self.is_confirmation}"


class Opening_booking(models.Model):
    academic_year = models.CharField("ปีการศึกษา", max_length=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group")
    opening_day = models.DateTimeField("เวลาเปิดจอง")
    closed_day = models.DateTimeField("เวลาปิดจอง")
    is_status = models.BooleanField(default=True)

    def __str__(self):
        return f"ปีการศึกษา:{self.academic_year} กลุ่ม:{self.group.name}"
