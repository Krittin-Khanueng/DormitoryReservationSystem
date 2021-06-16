from django.urls import path
from . import views

urlpatterns = [
    path("room/", views.BookingRoomView.as_view(), name="booking"),
]
