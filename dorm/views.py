from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Dormitory, Room
from booking.models import Opening_booking


class DormView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        # get request user groups
        user_groups = request.user.groups.values_list('name', flat=True)[0]

        # get all dorms
        dorm = Dormitory.objects.filter(is_active=True)
        # get open booking filter with user group
        opening_booking = Opening_booking.objects.filter(
            group__name=user_groups, is_status=True).latest("created_at")
        context = {
            "dormitorys": dorm,
            "opening_booking": opening_booking,
            "user_is_booking_state": request.user.account.is_booking_state

        }
        return render(request, 'dorm/dorm.html', context)


class RoomView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, dorm_name):
        context = {}
        dormitory = {}
        # get user gender
        gender = request.user.account.gender
        # get dorm
        dorm = get_object_or_404(Dormitory, name=dorm_name, is_active=True)
        # get room filter type
        for floor in dorm.dormitory.all():
            # QuerySet to list
            dormitory[floor.number] = list(floor.get_room_type(gender))
        context["dormitory"] = dormitory
        return render(request, "dorm/room.html", context)
