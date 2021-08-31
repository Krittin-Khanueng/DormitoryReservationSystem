from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Dormitory, Room, Floor
from booking.models import Opening_booking
from django.http import HttpResponseRedirect
from django.urls import reverse
from account.views import Login_by_PSUPASSPORTView


class DormView(Login_by_PSUPASSPORTView, View):

    @staticmethod
    def get(request):
        # get request user groups
        try:
            user_groups = request.user.groups.values_list('name', flat=True)[0]
        except IndexError:
            user_groups = None

        if user_groups:
            # get all dorms
            dorm = Dormitory.objects.filter(is_active=True)
            # get open booking filter with user group
            try:
                opening_booking = Opening_booking.objects.filter(
                    group__name=user_groups, is_status=True).latest("created_at")
            except Opening_booking.DoesNotExist:
                opening_booking = None

            context = {
                "dormitorys": dorm,
                "opening_booking": opening_booking,
                "user_is_booking_state": request.user.account.is_booking_state

            }
            return render(request, 'dorm/dorm.html', context)
        else:
            return HttpResponseRedirect(reverse('index'))


class RoomView(Login_by_PSUPASSPORTView, View):

    @staticmethod
    def get(request, dorm_name):
        context = {}
        # get user gender
        gender = request.user.account.gender
        # get dorm and floors
        floors = Floor.objects.select_related("dorm_name").filter(
            dorm_name__name=dorm_name, dorm_name__is_active=True)
        dormitory = {
            floor.number: list(floor.get_room_type(gender)) for floor in floors
        }

        context["dormitory"] = dormitory
        return render(request, "dorm/room.html", context)


class DormDetailsView(View):
    # show dorm details for current
    @staticmethod
    def get(request, dorm_name):
        dorm = get_object_or_404(Dormitory, name=dorm_name)
        context = {
            "dorm": dorm,
        }
        return render(request, "dorm/dorm_details.html", context)
