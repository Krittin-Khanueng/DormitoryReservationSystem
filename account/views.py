from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


def get_user_account(self, request):
	user = request.user
	return user.account


class Login_by_PSUPASSPORTView(LoginRequiredMixin):
	login_url = "https://oauth.psu.ac.th/?oauth=authorize&client_id=oauthpsu823&response_type=code&state" \
				"=55ba8fa8a83fce7ca120ec14058f8a4a&redirect_uri=http://localhost:8080/psupassport/callback "


class LogoutView(LogoutView):
	next_page = 'index'


class ProfileView(Login_by_PSUPASSPORTView, View):
	def get(self, request):
		# get request user and account

		account = get_user_account(self, request)
		return render(request, 'account/profile.html', {'account': account})


class ProfileEditView(Login_by_PSUPASSPORTView, View):
	def get(self, request):
		# get request user and account
		account = get_user_account(self, request)
		return render(request, 'account/profile-edit.html', {'account': account})

	@staticmethod
	def post(request):
		# get all data from request
		data = request.POST.copy()
		user = User.objects.get(id=request.user.id)
		# update user data
		user.first_name = data['first_name_th']
		user.last_name = data['last_name_th']
		user.email = data['email']

		# update account in user
		# convert birth_date to datetime object

		account = user.account
		account.first_name_en = data['first_name_en']
		account.last_name_en = data['last_name_en']
		account.address = data['address']
		account.birthday = datetime.strptime(
			data["birth_date"], "%Y-%m-%d").strftime('%Y-%m-%d')
		account.phone_number = data['phone_number']
		account.motorcycle_registration = data['motorcycle_registration']
		account.car_registration = data['car_registration']

		# save account and user
		account.save()
		user.save()

		return HttpResponseRedirect(reverse('profile'))
