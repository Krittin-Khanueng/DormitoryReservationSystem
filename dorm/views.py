from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


from .models import Dormitory, Room


class DormView(LoginRequiredMixin, View):
	login_url = "login"

	def get(self, request):
		dorm = Dormitory.objects.all()
		context = {
			"dormitorys": dorm,

		}
		return render(request, 'dorm/dorm.html', context)


class RoomView(LoginRequiredMixin, View):
	login_url = "login"

	def get(self, request, pk):
		context = {}
		dorm = Dormitory.objects.get(pk=pk)
		context["floors"] = dorm.dormitory.all()
		return render(request, "dorm/room.html", context)

