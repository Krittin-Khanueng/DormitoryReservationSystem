from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookingRoomView.as_view(), name="booking"),
    path("confirm/", views.ConfirmRoomView.as_view(), name="confirm"),
    path("success/", views.BookingSuccessView.as_view(), name="booking_success"),
    path("confirm/booking/", views.ConfirmToBookView.as_view(),
         name="booking_confirm"),
    # path("history/",)
    # path("cancel/",),
    # path("cancel-succes/"),



]
