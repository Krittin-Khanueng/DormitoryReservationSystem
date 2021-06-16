from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name="account/profile.html")),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout")
]
