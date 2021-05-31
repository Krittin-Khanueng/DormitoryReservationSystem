from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Dormitory, Room


# Create your views here.


class IndexView(View):

	def get(self, request):
		context = {}
		dormitorys = Dormitory.objects.all()
		context["dormitorys"] = dormitorys
		return render(request, "dorm/index.html", context)


class GetAllRoomView(View):

	def get(self, request, name):
		context = {}
		dorm = Dormitory.objects.get(name=name)
		context["rooms"] = dorm.dormitory.all()
		return render(request, "dorm/all-room.html", context)
