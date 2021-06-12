# Generated by Django 3.2.3 on 2021-06-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='status_room',
        ),
        migrations.AddField(
            model_name='room',
            name='is_status',
            field=models.BooleanField(
                default=True, verbose_name='สถานะของห้อง'),
        ),
    ]
