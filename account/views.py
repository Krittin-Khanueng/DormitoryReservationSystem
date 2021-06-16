from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.


class LoginView(LoginView):
    template_name = "account/login.html"


class LogoutView(LogoutView):
    next_page = 'index'
