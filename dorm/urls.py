from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("room/<int:pk>/", views.GetAllRoomView.as_view(), name="room-name")
]
