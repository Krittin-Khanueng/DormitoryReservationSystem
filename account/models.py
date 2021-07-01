from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='เบอร์โทรศัพท์', max_length=10, null=True, blank=True)
    bank_account = models.CharField(verbose_name='บัญชีธนาคาร', max_length=20, null=True, blank=True)
    motorcycle_registration = models.CharField(verbose_name="ป้ายทะเบียนรถจักรยานยนต์", max_length=15, null=True,
                                               blank=True)
    car_registration = models.CharField(verbose_name="ป้ายทะเบียนยนต์", max_length=15, null=True, blank=True)
    gender = models.CharField(verbose_name='เพศ', max_length=7, choices=[('ผู้ชาย', 'ผู้ชาย'), ('ผู้หญิง', 'ผู้หญิง')],
                              null=True,
                              blank=True)
    image = models.ImageField(upload_to="students/", blank=True)
    current_state = models.CharField(verbose_name='สถานะ', max_length=14,
                                     choices=[('ไม่มีสิทธิ์จอง', 'ไม่มีสิทธิ์จอง'), ('มีสิทธิ์จอง', 'มีสิทธิ์จอง'),
                                              ('รอยืนยัน', 'รอยืนยัน'), ('ยืนยัน', 'ยืนยัน')], default='ไม่มีสิทธิ์จอง')

    room_number = models.CharField(verbose_name="เลขห้อง", max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.username
