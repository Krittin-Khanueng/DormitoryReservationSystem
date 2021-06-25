from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from django.shortcuts import render, redirect


# Create your views here.


class LoginView(LoginView):
	template_name = "account/login.html"


class LogoutView(LogoutView):
	next_page = 'index'
