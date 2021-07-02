# Generated by Django 3.2.4 on 2021-07-01 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('booking', '0007_auto_20210701_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room_confirmation',
            name='room',
        ),
        migrations.RemoveField(
            model_name='room_confirmation',
            name='user',
        ),
        migrations.AddField(
            model_name='room_confirmation',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='booking_confirm', to='booking.booking'),
        ),
        migrations.AlterField(
            model_name='room_confirmation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]