from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout")

]
