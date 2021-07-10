# Generated by Django 3.2.4 on 2021-07-10 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0009_auto_20210702_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_confirmation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_confirmed', models.BooleanField(null=True, verbose_name='สถานะการยืนยัน')),
                ('confirm_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='booking_at',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_user', to=settings.AUTH_USER_MODEL, verbose_name='คนจอง'),
        ),
        migrations.DeleteModel(
            name='Room_confirmation',
        ),
        migrations.AddField(
            model_name='booking_confirmation',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_confirmation', to='booking.booking', verbose_name='การจอง'),
        ),
    ]
