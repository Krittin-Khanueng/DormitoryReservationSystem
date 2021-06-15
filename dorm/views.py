from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from .models import Dormitory, Room


# Create your views here.


class IndexView(ListView):
    model = Dormitory
    context_object_name = "dormitorys"
    template_name = "dorm/dorm.html"


class GetAllRoomView(View):

    def get(self, request, name):
        context = {}
        dorm = Dormitory.objects.get(name=name)
        context["rooms"] = dorm.dormitory.all()
        return render(request, "dorm/all-room.html", context)
