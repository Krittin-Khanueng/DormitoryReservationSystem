from django.urls import path
from . import views

urlpatterns = [
	path("", views.DormView.as_view(), name="dorm"),
	path("room/<str:dorm_name>/", views.RoomView.as_view(), name="room-name"),
	path("dorm/<str:dorm_name>/", views.DormDetailsView.as_view(), name="dorm-name"),)
]
