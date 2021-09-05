from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_pk>/', views.blogView.as_view(), name='blog_detail'),
]
