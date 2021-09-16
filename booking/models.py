import datetime
import uuid

from django.contrib.auth.models import User, Group
from django.db import models

from dorm.models import Room


class Academic_year(models.Model):
    academic_year = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.academic_year


class Opening_booking(models.Model):
    academic_year = models.ForeignKey(
        Academic_year, on_delete=models.CASCADE, verbose_name="ปีการศึกษา", related_name="opening_booking")
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="group", verbose_name="กลุ่ม")
    opening_day = models.DateTimeField(verbose_name="เวลาเปิดจอง")
    closed_day = models.DateTimeField(verbose_name="เวลาปิดจอง")
    is_status = models.BooleanField(
        default=True, verbose_name="สถานะการใช้งาน")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="วันที่สร้าง")

    def __str__(self):
        return f"ปีการศึกษา:{self.academic_year} กลุ่ม:{self.group.name}"

    # Check the current time and the opening and closing times.
    def is_open(self):
        now = datetime.datetime.now()
        return self.opening_day < now < self.closed_day

    def get_academic_year_in_booking(self):
        return self.academic_year

    class Meta:
        verbose_name = "เวลาเปิดจองห้องพัก"


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='booking_room',
                             verbose_name="เลขห้อง")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="คนจอง", null=True, related_name="booking_user")
    booking_at = models.DateTimeField(
        auto_now_add=True, verbose_name="วันที่จอง")

    open_booking = models.ForeignKey(
        Opening_booking, on_delete=models.CASCADE, null=True, related_name="open_booking")

    def __str__(self):
        return f"{self.user.username} ห้อง:{self.room.room_id} {str(self.booking_at)}"

    class Meta:
        verbose_name = "การจอง"

    def get_academic_year_in_open_booking(self):
        return self.open_booking.academic_year

    def get_user_group(self):
        return self.user.groups.all()[0].id


class Booking_confirmation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE,
                                   related_name="booking_confirmation", null=True, verbose_name="การจอง")
    is_confirmed = models.BooleanField(
        null=True, verbose_name="สถานะการยืนยัน")
    confirm_date = models.DateTimeField(
        auto_now_add=True, verbose_name="วันที่ยืนยัน")

    class Meta:
        verbose_name = "ยืนยันการจองห้องพัก"
        verbose_name_plural = "ยืนยันการจองห้องพัก"

    def __str__(self):
        return f"{self.booking.user.username} ห้อง:{self.booking.room.room_id} สถานะการยืนยัน:{self.is_confirmed}"
