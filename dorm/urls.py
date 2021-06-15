from django.urls import path
from . import views

urlpatterns = [
	path("", views.IndexView.as_view(),name="dorm"),
	path("room/<int:pk>/", views.GetAllRoomView.as_view(), name="room-name")
]
