from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .models import Dormitory, Room


class DormView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        dorm = Dormitory.objects.filter(is_active=True)
        context = {
            "dormitorys": dorm,

        }
        return render(request, 'dorm/dorm.html', context)


class RoomView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, pk):
        context = {}
        dorm = get_object_or_404(Dormitory, pk=pk, is_active=True)
        context["floors"] = dorm.dormitory.all()
        return render(request, "dorm/room.html", context)
