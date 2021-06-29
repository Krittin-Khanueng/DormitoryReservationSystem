# Generated by Django 3.2.3 on 2021-06-21 21:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
		('booking', '0001_initial'),
	]

	operations = [
		migrations.RemoveField(
			model_name='booking',
			name='user',
		),
		migrations.AddField(
			model_name='booking',
			name='user',
			field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
		),
	]