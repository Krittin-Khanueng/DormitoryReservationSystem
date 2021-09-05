# Generated by Django 3.2.7 on 2021-09-05 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20210831_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opening_booking',
            name='academic_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='opening_booking', to='booking.academic_year', verbose_name='ปีการศึกษา'),
        ),
    ]
