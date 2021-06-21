from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookingRoomView.as_view(), name="booking"),
    path("confirm/", views.ConfirmRoomView.as_view(), name="confirm")
]
