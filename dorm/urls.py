from django.urls import path
from . import views

urlpatterns = [
    path("", views.DormView.as_view(), name="dorm"),
    path("room/<int:pk>/", views.RoomView.as_view(), name="room-name")
]
