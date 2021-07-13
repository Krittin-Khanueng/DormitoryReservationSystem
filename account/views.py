from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from datetime import datetime


class LoginView(LoginView):
    template_name = "account/login.html"


class LogoutView(LogoutView):
    next_page = 'index'


class ProfileView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        # get request user and account
        user = request.user
        account = user.account
        return render(request, 'account/profile.html', {'account': account})


class ProfileEditView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        # get request user and account
        user = request.user
        account = user.account
        return render(request, 'account/profile-edit.html', {'account': account})

    def post(self, request):
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
