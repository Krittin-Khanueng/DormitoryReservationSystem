from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField('เบอร์โทรศัพท์', max_length=10, null=True, blank=True)
    gender = models.CharField('เพศ', max_length=7, choices=[('ผู้ชาย', 'ผู้ชาย'), ('ผู้หญิง', 'ผู้หญิง')], null=True,
                              blank=True)
    image = models.ImageField(upload_to="students/", blank=True)
    current_state = models.CharField('สถานะ', max_length=14,
                                     choices=[('ไม่มีสิทธิ์จอง', 'ไม่มีสิทธิ์จอง'), ('มีสิทธิ์จอง', 'มีสิทธิ์จอง'),
                                              ('รอยืนยัน', 'รอยืนยัน'), ('ยืนยัน', 'ยืนยัน')], default='ไม่มีสิทธิ์จอง')

    def __str__(self):
        return self.user.username


class Group(models.Model):
    pass