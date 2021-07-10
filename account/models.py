from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from uuid import uuid4
import datetime
import os



def path_and_rename(instance, filename):
    today = datetime.datetime.today()
    path = os.path.join('account', 'images', today.strftime('%Y'), today.strftime('%m'))
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.user.username, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(path, filename)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    phone_number = models.CharField(verbose_name='เบอร์โทรศัพท์', max_length=10, null=True, blank=True)
    bank_account = models.CharField(verbose_name='บัญชีธนาคาร', max_length=20, null=True, blank=True)
    motorcycle_registration = models.CharField(verbose_name="ป้ายทะเบียนรถจักรยานยนต์", max_length=15, null=True,
                                               blank=True)
    car_registration = models.CharField(verbose_name="ป้ายทะเบียนยนต์", max_length=15, null=True, blank=True)
    gender = models.CharField(verbose_name='เพศ', max_length=7, choices=[('ผู้ชาย', 'ผู้ชาย'), ('ผู้หญิง', 'ผู้หญิง')],
                              null=True,
                              blank=True)
        
    image = models.ImageField(upload_to=path_and_rename, blank=True)
    current_state = models.CharField(verbose_name='สถานะ', max_length=14,
                                     choices=[('ไม่มีสิทธิ์จอง', 'ไม่มีสิทธิ์จอง'), ('มีสิทธิ์จอง', 'มีสิทธิ์จอง')],
                                     default='ไม่มีสิทธิ์จอง')
    is_booking_state = models.BooleanField(verbose_name="สถานะการจอง", default=False)
    created_at = models.DateTimeField(auto_now_add=True)       
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.user.username

    
    #ressize_image 
    def save(self, *args, **kwargs):       
        super(Account, self).save(*args, **kwargs)       
        img = Image.open(self.image.path)       
        if img.height > 500 or img.width > 500:       
            output_size = (500, 500)       
            img.thumbnail(output_size)       
            img.save(self.image.path)

