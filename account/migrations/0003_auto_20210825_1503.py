# Generated by Django 3.2.6 on 2021-08-25 15:03

from django.db import migrations, models

import account.models


class Migration(migrations.Migration):
	dependencies = [
		('account', '0002_alter_account_image'),
	]

	operations = [
		migrations.RenameField(
			model_name='account',
			old_name='image',
			new_name='image_profile',
		),
		migrations.AddField(
			model_name='account',
			name='bank_account_number',
			field=models.CharField(blank=True, max_length=20, null=True, verbose_name='บัญชีธนาคาร'),
		),
		migrations.AddField(
			model_name='account',
			name='bill_number',
			field=models.CharField(blank=True, max_length=30, null=True, verbose_name='เลขที่บิล'),
		),
		migrations.AddField(
			model_name='account',
			name='image_bill',
			field=models.ImageField(blank=True, null=True, upload_to=account.models.path_upload_bill),
		),
		migrations.AlterField(
			model_name='account',
			name='bank_account',
			field=models.CharField(blank=True, max_length=30, null=True, verbose_name='ธนาคาร'),
		),
	]
