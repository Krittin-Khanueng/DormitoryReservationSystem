from django.urls import path
from . import views

urlpatterns = [
	path("", views.IndexView.as_view()),
	path("room/<str:name>/", views.GetAllRoomView.as_view(), name="room-name")
]
