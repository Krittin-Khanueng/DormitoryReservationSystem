from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookingRoomView.as_view(), name="booking"),
]
