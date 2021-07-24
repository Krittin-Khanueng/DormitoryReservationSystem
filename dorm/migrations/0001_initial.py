# Generated by Django 3.2.5 on 2021-07-24 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/dorm/')),
                ('images_room_plan', models.ImageField(blank=True, null=True, upload_to='images/dorm/room_plan/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1, verbose_name='ชั้น')),
                ('dorm_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dormitory', related_query_name='dormitory', to='dorm.dormitory', verbose_name='ชื่อหอพัก')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='เลขห้อง')),
                ('room_type', models.CharField(choices=[('MALE', 'ผู้ชาย'), ('FEMALE', 'ผู้หญิง')], max_length=10, verbose_name='ประเภทห้องพัก')),
                ('amount', models.PositiveIntegerField(default=3, verbose_name='จำนวน')),
                ('is_status', models.BooleanField(default=True, verbose_name='สถานะของห้อง')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='floor', related_query_name='floor', to='dorm.floor', verbose_name='ชั้น')),
            ],
        ),
    ]
