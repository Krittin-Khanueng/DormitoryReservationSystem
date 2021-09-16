import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render
from django.views import View

from account.models import Account


class HomePageView(View):
	@staticmethod
	def get(request):
		return render(request, 'main/index.html')


class CallBackView(View):
	def get(self, request):
		"""
		PSUPassport Callback
		"""
		code = request.GET['code']
		url = 'https://oauth.psu.ac.th/'
		token_url = url + '?oauth=token'
		### LOCALTEST ###

		redirect_uri = 'http://localhost:8080/psupassport/callback'
		data = {
			'grant_type': 'authorization_code',
			'client_id': 'oauthpsu823',
			'client_secret': 'f1e72bc2eec72d7ff455ecab8d0d3f4c',
			'code': code,
			'redirect_uri': redirect_uri
		}

		response = requests.post(token_url, data=data).json()
		access_token = response['access_token']
		# refresh_token = response['refresh_token']

		profile_url = url + '?oauth=me'
		header = {
			'Authorization': "Bearer " + access_token
		}
		data = {
			'redirect_uri': redirect_uri
		}
		profile_response = requests.post(
			profile_url,
			headers=header,
			data=data
		).json()
		user_login = profile_response['user_login']
		displayname = profile_response['displayname']
		description = profile_response['description']
		email = profile_response['user_email']

		user, created = User.objects.get_or_create(
			username=user_login)
		if created:
			user.first_name = description.split(' ')[0]
			user.last_name = description.split(' ')[1]
			user.email = email
			user.set_password(user_login + email + displayname)
			user.save()
			# user create account
			Account(user=user, first_name_en=displayname.split(' ')[
				0], last_name_en=displayname.split(' ')[1]).save()

			if not self.check_groups(user_login[:2]):
				# create Groups
				Group(name=user_login[:2]).save()

			group = Group.objects.get(name=user_login[:2])
			user = User.objects.get(username=user_login)
			user.groups.add(group)
			user.save()
			# user login
			login(request, user)
			return redirect('index')
		user = authenticate(request, username=user_login,
							password=user_login + email + displayname)
		if user is not None:
			login(request, user)
		else:
			messages.warning(request, 'กรุณา login ใหม่อีกครั้ง')
			return redirect('index')
		return redirect('index')

		# check groups

	@staticmethod
	def check_groups(first_two_codes):
		groups = Group.objects.all()
		for group in groups:
			return group.name == first_two_codes


class ContextPageView(View):
	def get(self, request):
		return render(request, 'main/context.html')
