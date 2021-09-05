from django.contrib.auth.models import User
from django.db import models
from uuid import uuid4
import datetime
import os


def path_and_rename(instance, filename):
    today = datetime.datetime.today()
    path = os.path.join('account', 'images',
                        today.strftime('%Y'), today.strftime('%m'))
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.user.username, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(path, filename)


def path_upload_bill(instance, filename):
    today = datetime.datetime.today()
    path = os.path.join('account', 'bill',
                        today.strftime('%Y'), today.strftime('%m'))
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}.{}.{}.{}'.format(instance.user.username,  today.strftime(
            '%Y'), today.strftime('%m'), today.strftime('%d'), ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(path, filename)


class Account(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='account')
    first_name_en = models.CharField(
        verbose_name="ชื่อภาษาอังกฤษ", max_length=100, null=True)
    last_name_en = models.CharField(
        verbose_name="นามสกุลภาษาอังกฤษ", max_length=100, null=True)
    birthday = models.DateField(verbose_name="วันเกิด", null=True)
    # address
    address = models.CharField(
        verbose_name="ที่อยู่", max_length=200, null=True)
    phone_number = models.CharField(
        verbose_name='เบอร์โทรศัพท์', max_length=10, null=True, blank=True)
    bank_account_number = models.CharField(
        verbose_name='บัญชีธนาคาร', max_length=20, null=True, blank=True)
    bank_account = models.CharField(
        verbose_name="ธนาคาร", max_length=30, null=True, blank=True)
    bill_number = models.CharField(
        verbose_name="เลขที่บิล", max_length=30, null=True, blank=True)
    motorcycle_registration = models.CharField(verbose_name="ป้ายทะเบียนรถจักรยานยนต์", max_length=15, null=True,
                                               blank=True)
    car_registration = models.CharField(
        verbose_name="ป้ายทะเบียนยนต์", max_length=15, null=True, blank=True)
    gender = models.CharField(verbose_name='เพศ', max_length=7, choices=[('ผู้ชาย', 'ผู้ชาย'), ('ผู้หญิง', 'ผู้หญิง')],
                              null=True,
                              blank=True)

    image_profile = models.ImageField(
        upload_to=path_and_rename, blank=True, null=True)
    image_bill = models.ImageField(
        upload_to=path_upload_bill, blank=True, null=True)
    current_state = models.CharField(verbose_name='สถานะ', max_length=14,
                                     choices=[
                                         ('ไม่มีสิทธิ์จอง', 'ไม่มีสิทธิ์จอง'), ('มีสิทธิ์จอง', 'มีสิทธิ์จอง')],
                                     default='ไม่มีสิทธิ์จอง')
    is_booking_state = models.BooleanField(
        verbose_name="สถานะการจอง", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    # ressize_image
    # def save(self, *args, **kwargs):
    #     super(Account, self).save(*args, **kwargs)
    #     # check image
    #     if self.image:
    #         img = Image.open(self.image.path)
    #         if img.height > 500 or img.width > 500:
    #             output_size = (500, 500)
    #             img.thumbnail(output_size)
    #             img.save(self.image.path)
