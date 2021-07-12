from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


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
