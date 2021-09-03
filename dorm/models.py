from django.db import models
from django.db.models import Sum


# Create your models here.


class Dormitory(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="images/dorm/", blank=True, null=True)
    images_room_plan = models.ImageField(
        upload_to="images/dorm/room_plan/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # check room amount > 0 and is_status  in floor
    def is_room_available_floor(self):
        return Floor.objects.filter(dorm_name=self, floor__amount__gt=0, floor__is_status=True).count()

    # check room amount < 0 and is_status  in floor
    def is_room_not_available_floor(self):
        return Floor.objects.filter(dorm_name=self, floor__amount__lte=0, floor__is_status=True).count()

    def get_all_rooms(self):
        return Room.objects.filter(floor__dorm_name=self).count()

    def get_room_amount_total(self):
        return Room.objects.filter(floor__dorm_name=self).aggregate(Sum('amount'))
    # get all floor in dorm
    def get_floor_list(self):
        return Floor.objects.filter(dorm_name=self)


class Floor(models.Model):
    dorm_name = models.ForeignKey(Dormitory, on_delete=models.PROTECT, related_name='dormitory',
                                  related_query_name="dormitory",
                                  verbose_name="ชื่อหอพัก")
    number = models.PositiveIntegerField(default=1, verbose_name="ชั้น")

    def __str__(self):
        return f"หอพัก:{self.dorm_name.name} ชั้น:{self.number}"

    def get_room_type(self, type_room):
        if type_room == "ผู้ชาย":
            return Room.objects.filter(floor_id=self.id, room_type="MALE", is_status=True)
        if type_room == "ผู้หญิง":
            return Room.objects.filter(floor_id=self.id, room_type="FEMALE", is_status=True)
        return None


class Room(models.Model):
    TYPE_IN_ROOM = [('MALE', 'ผู้ชาย'), ('FEMALE', 'ผู้หญิง')]
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT, related_name="floor", related_query_name="floor",
                              verbose_name="ชั้น")
    room_id = models.CharField(
        max_length=10, blank=True, null=True, unique=True, verbose_name="เลขห้อง")
    room_type = models.CharField(
        max_length=10, choices=TYPE_IN_ROOM, verbose_name="ประเภทห้องพัก")
    amount = models.PositiveIntegerField(default=3, verbose_name="จำนวน")
    is_status = models.BooleanField(default=True, verbose_name="สถานะของห้อง")

    def __str__(self):
        return f"หอพัก:{self.floor.dorm_name} ชั้น:{self.floor.number} ห้อง:{self.room_id} จำนวน:{self.amount}"

    # check room amount > 0 and is_status = True
    def get_amount(self):
        return self.amount
    
    def room_not_full(self):
        return self.amount > 0 and self.is_status
