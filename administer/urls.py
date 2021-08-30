from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home/', views.administerView.as_view()),
    path('dashboard/', views.administerdashboardView.as_view(), name='dashboard'),
    path('dorm/', views.administerdormView.as_view(), name='management_dorm'),
    path('dorm/edit/<int:id>/', views.administerdorm_editView.as_view(),
         name='management_dorm_edit'),
    path('dorm/delete/', views.administerdorm_deleteView.as_view(),
         name="management_dorm_delete"),

]
