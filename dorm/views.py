from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Dormitory, Room


# Create your views here.


class DormView(View):
	def get(self, request):
		dorm = Dormitory.objects.all()
		context = {
			"dormitorys": dorm,

		}
		return render(request, 'dorm/dorm.html', context)


class RoomView(View):
	def get(self, request, pk):
		context = {}
		dorm = Dormitory.objects.get(pk=pk)
		context["floors"] = dorm.dormitory.all()
		return render(request, "dorm/room.html", context)
