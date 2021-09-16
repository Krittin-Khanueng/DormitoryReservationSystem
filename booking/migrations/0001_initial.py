# Generated by Django 3.2.6 on 2021-08-24 18:14

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
	initial = True

	dependencies = [
		('auth', '0012_alter_user_first_name_max_length'),
		('dorm', '0001_initial'),
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
	]

	operations = [
		migrations.CreateModel(
			name='Booking',
			fields=[
				('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
				('booking_at', models.DateTimeField(auto_now_add=True, verbose_name='วันที่จอง')),
			],
			options={
				'verbose_name': 'การจอง',
			},
		),
		migrations.CreateModel(
			name='Opening_booking',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('academic_year', models.CharField(max_length=10, verbose_name='ปีการศึกษา')),
				('opening_day', models.DateTimeField(verbose_name='เวลาเปิดจอง')),
				('closed_day', models.DateTimeField(verbose_name='เวลาปิดจอง')),
				('is_status', models.BooleanField(default=True, verbose_name='สถานะการใช้งาน')),
				('created_at', models.DateTimeField(auto_now_add=True, verbose_name='วันที่สร้าง')),
				('group',
				 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='auth.group',
								   verbose_name='กลุ่ม')),
			],
			options={
				'verbose_name': 'เวลาเปิดจองห้องพัก',
			},
		),
		migrations.CreateModel(
			name='Booking_confirmation',
			fields=[
				('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
				('is_confirmed', models.BooleanField(null=True, verbose_name='สถานะการยืนยัน')),
				('confirm_date', models.DateTimeField(auto_now_add=True, verbose_name='วันที่ยืนยัน')),
				('booking', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE,
												 related_name='booking_confirmation', to='booking.booking',
												 verbose_name='การจอง')),
			],
			options={
				'verbose_name': 'ยืนยันการจองห้องพัก',
				'verbose_name_plural': 'ยืนยันการจองห้องพัก',
			},
		),
		migrations.AddField(
			model_name='booking',
			name='open_booking',
			field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='open_booking',
									to='booking.opening_booking'),
		),
		migrations.AddField(
			model_name='booking',
			name='room',
			field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_room',
									to='dorm.room', verbose_name='เลขห้อง'),
		),
		migrations.AddField(
			model_name='booking',
			name='user',
			field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_user',
									to=settings.AUTH_USER_MODEL, verbose_name='คนจอง'),
		),
	]
