from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Dormitory, Room


# Create your views here.


class IndexView(View):
	def get(self,request):
		dorm = Dormitory.objects.all()
		# print(dorm[0].dormitory.filter(amount__gt=0).count())

		context = {
			"dormitorys": dorm,

		}
		return render(request, 'dorm/dorm.html',context)


class GetAllRoomView(View):
	def get(self, request, pk):
		context = {}
		dorm = Dormitory.objects.get(pk=pk)
		context["rooms"] = dorm.dormitory.all()
		return render(request, "dorm/all-room.html", context)

