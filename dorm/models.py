from django.db import models


# Create your models here.


class Dormitory(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="images/dorm/", blank=True, null=True)
    images_room_plan = models.ImageField(upload_to="images/dorm/room_plan/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    def __str__(self):
        return self.name


    def room_not_full(self):
        return Floor.objects.filter(dorm_name=self, floor__amount__gt=0).count()


  

class Floor(models.Model):
    dorm_name = models.ForeignKey(Dormitory, on_delete=models.PROTECT, related_name='dormitory',
                                  related_query_name="dormitory",
                                  verbose_name="ชื่อหอพัก")
    number = models.PositiveIntegerField(default=1, verbose_name="ชั้น")

    def __str__(self):
        return f"หอพัก:{self.dorm_name.name} ชั้น:{self.number}"

    #get Room type MALE
    
    def get_room_type(self, type_room):
        if type_room == "ผู้ชาย":
            return Room.objects.filter(floor_id=self.id, room_type="MALE", is_status=True)
        elif type_room == "ผู้หญิง":
            return Room.objects.filter(floor_id=self.id, room_type="FEMALE", is_status=True)
        else:
            return None
        

    

class Room(models.Model):
    TYPE_IN_ROOM = [('MALE', 'ผู้ชาย'), ('FEMALE', 'ผู้หญิง')]
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT, related_name="floor", related_query_name="floor",
                              verbose_name="ชั้น")
    room_id = models.CharField(max_length=10, blank=True, null=True, unique=True, verbose_name="เลขห้อง")
    room_type = models.CharField(max_length=10, choices=TYPE_IN_ROOM, verbose_name="ประเภทห้องพัก")
    amount = models.PositiveIntegerField(default=3, verbose_name="จำนวน")
    is_status = models.BooleanField(default=True, verbose_name="สถานะของห้อง")

    def __str__(self):
        return f"หอพัก:{self.floor.dorm_name} ชั้น:{self.floor.number} ห้อง:{self.room_id} จำนวน:{self.amount}"


