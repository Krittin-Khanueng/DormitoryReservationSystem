from django.contrib.auth.views import LoginView, LogoutView


class LoginView(LoginView):
    template_name = "account/login.html"


class LogoutView(LogoutView):
    next_page = 'index'

