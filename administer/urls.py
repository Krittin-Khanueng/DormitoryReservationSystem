from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home/', views.administerView.as_view()),
    path('dashboard/', views.administerdashboardView.as_view(), name='dashboard'),
    path('dorm/', views.administerdormView.as_view(), name='management_dorm'),

]
