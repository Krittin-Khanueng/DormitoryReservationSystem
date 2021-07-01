import uuid

from django.contrib.auth.models import User, Group
from django.db import models
from dorm.models import Room


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, null=True, related_name='booking_room')
    user = models.ManyToManyField(User)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room}"


class Opening_booking(models.Model):
    academic_year = models.CharField("ปีการศึกษา", max_length=10)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="group")
    opening_day = models.DateTimeField("เวลาเปิดจอง")
    closed_day = models.DateTimeField("เวลาปิดจอง")
    is_status = models.BooleanField(default=True)

    def __str__(self):
        return f"ปีการศึกษา:{self.academic_year} กลุ่ม:{self.group.name}"
