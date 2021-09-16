# Generated by Django 3.2.7 on 2021-09-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='Blog',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('title', models.CharField(max_length=100)),
				('content', models.TextField()),
				('created_time', models.DateTimeField(auto_now_add=True)),
				('last_updated_time', models.DateTimeField(auto_now=True)),
				('is_deleted', models.BooleanField(default=False)),
			],
			options={
				'ordering': ['-created_time'],
			},
		),
	]
