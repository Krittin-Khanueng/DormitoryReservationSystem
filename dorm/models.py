from django.db import models


# Create your models here.

class Dormitory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="images/dorm/", blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    TYPE_IN_ROOM = [('MALE', 'ผู้ชาย'), ('FEMALE', 'ผู้หญิง')]
    dorm_name = models.ForeignKey(Dormitory, on_delete=models.PROTECT, related_name='dormitory',
                                  verbose_name="ชื่อหอพัก")
    floor = models.PositiveIntegerField(default=1, verbose_name="ชั้น")
    room_id = models.CharField(
        max_length=10, blank=True, null=True, unique=True, verbose_name="เลขห้อง")
    room_type = models.CharField(
        max_length=10, choices=TYPE_IN_ROOM, verbose_name="ประเภทห้องพัก")
    amount = models.PositiveIntegerField(default=3, verbose_name="จำนวน")
    is_status = models.BooleanField(default=True, verbose_name="สถานะของห้อง")

    def __str__(self):
        return f"หอพัก:{self.dorm_name} ชั้น:{self.floor} ห้อง:{self.room_id} จำนวน:{self.amount}"
